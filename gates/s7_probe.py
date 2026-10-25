#!/usr/bin/env python3
"""S10 check s7-lsp: does ty show the field description in hover, completion, and signature help?

Usage: s7_probe.py LIBRARY OUT.json SCRATCH_DIR

No timing. For the class `Machine` (curated tier) and the class `Openssh` (the root class of `services.openssh`),
and for two documented keywords of each, it asks ty (language server, the pinned build of S7) for:
  hover       the hover text on the keyword in a call `Cls(kw=0)`
  completion  the documentation of the completion item `kw=` inside `Cls(`
  signature   the documentation of the parameter `kw` in the signature help at `Cls(`
Pass: the first line of the attribute docstring of the keyword shows in all three, for every probed keyword.
Compare letters and digits only, in lower case, so that Markdown escapes do not matter.

Environment (the defaults hold the fixture of this directory):
  S7_MACHINE       module:Class of the curated class   (curated_fixture:Machine)
  S7_OPENSSH       module:Class of the root class      (pynix_os.services.openssh:Openssh)
  S7_CURATED       the package directory of the curated class   (fixtures/curated_fixture, beside this file)
  S7_EXTRA_PATHS   colon list of directories with more packages
  GATES_TY         the ty binary (set by run_gates.sh from the uv environment)
"""
import ast
import json
import os
import re
import shutil
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lsp7  # noqa: E402

lib, out, scratch = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
MACHINE = os.environ.get("S7_MACHINE", "curated_fixture:Machine")
OPENSSH = os.environ.get("S7_OPENSSH", "pynix_os.services.openssh:Openssh")
CURATED = os.environ.get("S7_CURATED", str(Path(__file__).resolve().parent / "fixtures" / "curated_fixture"))  # the package directory itself
EXTRA = [p for p in os.environ.get("S7_EXTRA_PATHS", "").split(":") if p]
TY = lsp7.TY

if scratch.exists():
    shutil.rmtree(scratch)
ws = scratch / "ws"
ws.mkdir(parents=True)
if Path(CURATED).is_dir():
    (ws / Path(CURATED).name).symlink_to(Path(CURATED).resolve())
# The workspace: one symlink per top-level name of the library, then of the extra paths (first one wins).
for base in [lib, *map(Path, EXTRA)]:
    if not base.is_dir():
        continue
    for entry in sorted(base.iterdir()):
        if entry.name.startswith(".") or entry.suffix in {".json", ".py", ".nix"} and entry.is_file():
            continue
        if entry.is_dir() and not (ws / entry.name).exists():
            (ws / entry.name).symlink_to(entry.resolve())


def norm(text):
    return re.sub(r"[^a-z0-9]", "", (text or "").lower())


def module_file(mod):
    rel = Path(*mod.split("."))
    for cand in (ws / rel.with_suffix(".py"), ws / rel / "__init__.py"):
        if cand.exists():
            return cand
    return None


def documented_fields(path, cls_name, want=2):
    """The first `want` fields of the class that have an attribute docstring: [(field, first docstring line)]."""
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == cls_name:
            found = []
            body = node.body
            for i, item in enumerate(body[:-1]):
                nxt = body[i + 1]
                if (isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name) and isinstance(nxt, ast.Expr)
                        and isinstance(nxt.value, ast.Constant) and isinstance(nxt.value.value, str)):
                    first = nxt.value.value.strip().splitlines()[0]
                    found.append((item.target.id, first))
                    if len(found) == want:
                        break
            return found
    return None


def has_block(text, cls_name):
    """True when the class body holds `if TYPE_CHECKING:` with a def __init__ inside."""
    for node in ast.parse(text).body:
        if isinstance(node, ast.ClassDef) and node.name == cls_name:
            return any(isinstance(i, ast.If) and any(isinstance(j, ast.FunctionDef) and j.name == "__init__" for j in i.body)
                       for i in node.body)
    return False


def doc_text(d):
    if d is None:
        return None
    return d["value"] if isinstance(d, dict) else d


def hover_text(r):
    if not r:
        return ""
    c = r["contents"]
    return c["value"] if isinstance(c, dict) else str(c)


result = {"library": str(lib), "ty": TY, "classes": {}, "pass": False}
t0 = time.monotonic()
srv = None
try:
    srv = lsp7.Server(TY, Path(tempfile.mkdtemp(prefix="home-", dir=scratch)), scratch / "ty-server.txt", root=ws)
    srv.initialize()
    all_ok = True
    for label, spec in (("Machine", MACHINE), ("Openssh", OPENSSH)):
        mod, cls = spec.split(":")
        info = {"spec": spec, "has_block": False}
        result["classes"][label] = info
        path = module_file(mod)
        if path is None:
            info["error"] = f"module {mod} not found in the workspace"
            all_ok = False
            continue
        text = path.read_text()
        info["has_block"] = has_block(text, cls)
        fields = documented_fields(path, cls)
        if not fields:
            info["error"] = f"class {cls} has no attribute docstring"
            all_ok = False
            continue
        head = f"from {mod} import {cls}\n"
        info["keywords"] = {}
        for kw, first in fields:
            snippet = norm(first)[:40]
            row = {"expected": first[:80]}
            # hover on the keyword
            call = f"x = {cls}({kw}=0)"
            uri = srv.open(f"probe_h_{label}_{kw}.py", head + call + "\n")
            col = call.index(kw + "=") + 1
            h = hover_text(srv.request("textDocument/hover", {"textDocument": {"uri": uri}, "position": {"line": 1, "character": col}}).get("result"))
            row["hover"] = snippet in norm(h)
            # completion item doc
            curi = srv.open(f"probe_c_{label}_{kw}.py", head + f"x = {cls}(\n    \n)\n")
            r = srv.request("textDocument/completion", {"textDocument": {"uri": curi}, "position": {"line": 2, "character": 4},
                                                         "context": {"triggerKind": 1}}).get("result") or []
            items = r.get("items", []) if isinstance(r, dict) else r
            it = next((i for i in items if i["label"] == kw + "="), None)
            row["completion"] = bool(it) and snippet in norm(doc_text(it.get("documentation")))
            # signature help: the doc of the parameter kw
            suri = srv.open(f"probe_s_{label}_{kw}.py", head + f"x = {cls}()\n")
            sh = srv.request("textDocument/signatureHelp", {"textDocument": {"uri": suri}, "position": {"line": 1, "character": len(f"x = {cls}(")},
                                                             "context": {"triggerKind": 1, "isRetrigger": False}}).get("result") or {}
            ok = False
            for sig in sh.get("signatures", []):
                for p in sig.get("parameters", []):
                    lab = p["label"]
                    name = sig["label"][lab[0]:lab[1]] if isinstance(lab, list) else lab
                    if name.split(":")[0].strip() == kw and snippet in norm(doc_text(p.get("documentation"))):
                        ok = True
            row["signature"] = ok
            info["keywords"][kw] = row
            all_ok &= row["hover"] and row["completion"] and row["signature"]
    result["pass"] = bool(all_ok)
except Exception as exc:  # noqa: BLE001
    result["error"] = f"{type(exc).__name__}: {exc}"[:300]
finally:
    if srv is not None:
        srv.close()
result["seconds"] = round(time.monotonic() - t0, 2)
out.write_text(json.dumps(result, indent=1))
cells = [f"{c}.{k}:{'h' if r['hover'] else '-'}{'c' if r['completion'] else '-'}{'s' if r['signature'] else '-'}"
         for c, i in result["classes"].items() for k, r in i.get("keywords", {}).items()]
print(json.dumps({"pass": result["pass"], "probes": cells, "error": result.get("error") or [i.get("error") for i in result["classes"].values() if i.get("error")]}))
sys.exit(0 if result["pass"] else 1)
