"""Small LSP client for ty over stdio, for the S7 probes. Parametrized by the ty binary and the workspace.

Copy of 008 S10 `lsp7.py` (S7). Change: the ty binary, the site-packages directory, and the search path come from the environment.
"""
import json
import os
import subprocess
import time
from pathlib import Path

# The ty binary, the site-packages directory, and the search path come from the uv environment of the repository.
TY = os.environ["GATES_TY"]
SITE = os.environ["GATES_SITE"]
PATH = os.environ["GATES_PATH"]
WS = Path(os.environ.get("GATES_LSP_WS", "."))

CAPS = {"textDocument": {
    "completion": {"completionItem": {"snippetSupport": False, "documentationFormat": ["markdown", "plaintext"],
                                      "resolveSupport": {"properties": ["documentation", "detail", "additionalTextEdits"]},
                                      "labelDetailsSupport": True}},
    "hover": {"contentFormat": ["markdown", "plaintext"]},
    "signatureHelp": {"signatureInformation": {"documentationFormat": ["markdown", "plaintext"],
                                               "parameterInformation": {"labelOffsetSupport": True},
                                               "activeParameterSupport": True}},
    "publishDiagnostics": {}}}


class Server:
    def __init__(self, ty, home, log, root=WS):
        self.root = Path(root)
        env = {"HOME": str(home), "PATH": PATH, "PYTHONPATH": f"{self.root}:{SITE}",
               "XDG_CACHE_HOME": str(home / ".cache"), "XDG_CONFIG_HOME": str(home / ".config")}
        self.err = open(log, "wb")
        self.proc = subprocess.Popen([ty, "server"], cwd=self.root, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=self.err, env=env)
        self.seq = 0
        self.pending = []

    def send(self, method, params, request=True):
        msg = {"jsonrpc": "2.0", "method": method, "params": params}
        if request:
            self.seq += 1
            msg["id"] = self.seq
        raw = json.dumps(msg, separators=(",", ":")).encode()
        self.proc.stdin.write(f"Content-Length: {len(raw)}\r\n\r\n".encode() + raw)
        self.proc.stdin.flush()
        return self.seq if request else None

    def receive(self, timeout=60):
        start = time.monotonic()
        while time.monotonic() - start < timeout:
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError("server closed stdout")
            if line.lower().startswith(b"content-length:"):
                n = int(line.split(b":", 1)[1].strip())
                while self.proc.stdout.readline().strip():
                    pass
                msg = json.loads(self.proc.stdout.read(n))
                if msg.get("method") and "id" in msg:
                    result = [None] * len(msg.get("params", {}).get("items", [])) if msg["method"] == "workspace/configuration" else None
                    raw = json.dumps({"jsonrpc": "2.0", "id": msg["id"], "result": result}).encode()
                    self.proc.stdin.write(f"Content-Length: {len(raw)}\r\n\r\n".encode() + raw)
                    self.proc.stdin.flush()
                return msg
        raise TimeoutError("LSP timeout")

    def request(self, method, params):
        want = self.send(method, params)
        while True:
            msg = self.receive()
            if msg.get("id") == want and "method" not in msg:
                return msg
            if msg.get("method"):
                self.pending.append(msg)

    def initialize(self):
        root = self.root.as_uri()
        want = self.send("initialize", {"processId": None, "rootUri": root, "capabilities": CAPS,
                                        "workspaceFolders": [{"uri": root, "name": "ws"}]})
        while True:
            msg = self.receive()
            if msg.get("id") == want and "method" not in msg:
                self.init_result = msg["result"]
                break
        self.send("initialized", {}, request=False)
        return self.init_result

    def open(self, name, text):
        uri = (self.root / name).as_uri()
        self.send("textDocument/didOpen", {"textDocument": {"uri": uri, "languageId": "python", "version": 1, "text": text}}, request=False)
        return uri

    def close(self):
        try:
            self.request("shutdown", None)
            self.send("exit", None, request=False)
            self.proc.wait(timeout=10)
        except Exception:
            self.proc.kill()
        self.err.close()


def diagnostics(srv, uri, timeout=60):
    """The diagnostics of the first publishDiagnostics for uri."""
    for msg in list(srv.pending):
        if msg.get("method") == "textDocument/publishDiagnostics" and msg["params"]["uri"] == uri:
            srv.pending.remove(msg)
            return msg["params"]["diagnostics"]
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        msg = srv.receive(timeout)
        if msg.get("method") == "textDocument/publishDiagnostics" and msg["params"]["uri"] == uri:
            return msg["params"]["diagnostics"]
        if msg.get("method"):
            srv.pending.append(msg)
    raise TimeoutError("no diagnostics")
