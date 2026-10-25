"""S9: differential test of `strMatching` patterns. Nix (`builtins.match`, POSIX ERE) against the Python `matching` validator.

Usage: python -I patterns.py RUNTIME_DIR MANIFEST_DIR OUT_DIR

For each distinct pattern of the NixOS and Home Manager manifests, and for a corpus of strings (fixed strings, plus the
default and example values of options of that type and mutations of them), Nix says if the pattern matches the whole
string. `nixdantic.matching(pattern)` says the same for Python. The run counts the pairs where Nix accepts and Python
refuses (a false rejection), the reverse pairs (acceptable), and the patterns where the Python check is off.
"""

from __future__ import annotations

import inspect
import json
import subprocess
import sys
from pathlib import Path
from typing import Annotated

runtime_dir, manifest_dir, out_dir = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(runtime_dir))
sys.dont_write_bytecode = True
from nixdantic import matching  # noqa: E402
from pydantic import TypeAdapter, ValidationError  # noqa: E402

FIXED = [
    "", " ", "a", "A", "0", "9", "_", "-", ".", "/", ":", "@", "%", "+", "=", "~", "\n", "\t", "\r", "a\n", "\na", "a\nb",
    "ab", "AB", "a b", "a_b", "a-b", "a.b", "a/b", "a:b", "a@b", "a,b", "a;b", "a\"b", "a'b", "a\\b", "a]b", "a[b", "a{b", "a}b",
    "abc123", "ABC123", "abc_123-x", "0123456789", "0x10", "255.255.255.255", "10.0.0.1/24", "::1", "fe80::1/64", "2001:db8::1",
    "00:11:22:33:44:55", "aa:bb:cc:dd:ee:ff", "AA:BB", "12:34", "2020-01-02", "1h", "5m", "10K", "10M", "10GiB", "50%", "1-2", "1:2",
    "http://x", "https://x/", "https://example.org/path", "wss://x/", "ws://x", "tcp://1.2.3.4:5", "unix:/run/x", "inet:1.2.3.4", "file:x", "custom:x",
    "a@b.c", "sha256-abc=", "sha256-AAAA=", "ext:abc", "KEY_A", "BTN_LEFT", "KEY_a", "name.service", "a.b.c", "a.timer", "x@y.socket",
    "u+x", "ug=rw,o=r", "0755", "755", "0777", "1777", "a+rwx", "rwx", "#ffffff", "#FFF", "ffffff", "FFFFFF", "zzzzzz",
    "xn--abc", "a" * 32, "a" * 63, "a" * 64, "a" * 65, "x" * 22, "abcdefghijklmnopqrstuvwxyz234567.onion", "$CREDENTIALS_DIRECTORY/x",
    "é", "aéb", "☃", "\x7f", "\x1f", "\x80", "tab\there", "pad ", " pad",
]


def mutations(s: str) -> list[str]:
    return [s, s + "\n", "\n" + s, " " + s, s + " ", s.upper(), s.lower(), s[1:], s[:-1], s + s, s.replace("a", "é"), s + "x", "x" + s]


patterns: dict[str, dict] = {}
for name in ("nixos", "home-manager"):
    m = json.loads((manifest_dir / f"{name}.json").read_text())
    types = m["types"]
    by_type: dict[int, list[str]] = {}
    for rec in m["optionPool"]:
        for kind, info in rec.get("values", {}).items():
            if info.get("state") == "plain" and isinstance(json.loads(info["json"]), str):
                by_type.setdefault(rec["type"], []).append(json.loads(info["json"]))
    for tid, t in enumerate(types):
        if t["ctor"] == "strMatching" and "pattern" in t.get("payload", {}):
            p = patterns.setdefault(t["payload"]["pattern"], {"sets": [], "own": set()})
            p["sets"].append(name)
            p["own"].update(by_type.get(tid, []))
# Option values of other string options also serve as inputs (their shape is near).

results = []
for pattern, info in sorted(patterns.items()):
    corpus = list(dict.fromkeys(FIXED + [x for s in sorted(info["own"]) for x in mutations(s)]))
    (out_dir / "corpus.json").write_text(json.dumps(corpus))
    expr = ("let p = builtins.fromJSON (builtins.getEnv \"S9_PATTERN\"); "
            "ss = builtins.fromJSON (builtins.readFile (builtins.getEnv \"S9_CORPUS\")); "
            "in map (s: builtins.match p s != null) ss")
    import os
    run = subprocess.run(["nix", "eval", "--impure", "--json", "--expr", expr], capture_output=True, text=True,
                         env={**os.environ, "S9_PATTERN": json.dumps(pattern), "S9_CORPUS": str(out_dir / "corpus.json")})
    if run.returncode != 0:
        results.append({"pattern": pattern, "sets": info["sets"], "nix_error": run.stderr.strip().splitlines()[-1][:200]})
        continue
    nix_verdict = json.loads(run.stdout)
    validator = matching(pattern)
    compiled = inspect.getclosurevars(validator.func).nonlocals.get("compiled")
    adapter = TypeAdapter(Annotated[str, validator])
    false_rej, accept_more = [], []
    for s, nix_ok in zip(corpus, nix_verdict, strict=True):
        try:
            adapter.validate_python(s)
            py_ok = True
        except ValidationError:
            py_ok = False
        if nix_ok and not py_ok:
            false_rej.append(s)
        elif py_ok and not nix_ok:
            accept_more.append(s)
    results.append({
        "pattern": pattern, "sets": info["sets"], "strings": len(corpus), "nix_accepts": sum(nix_verdict),
        "python_check_off": compiled is None, "false_rejections": len(false_rej), "false_rejection_examples": false_rej[:4],
        "python_accepts_more": len(accept_more), "python_accepts_more_examples": accept_more[:4],
    })

summary = {
    "patterns": len(results),
    "nix_errors": sum(1 for r in results if "nix_error" in r),
    "python_check_off": [r["pattern"] for r in results if r.get("python_check_off")],
    "patterns_with_false_rejection": [r["pattern"] for r in results if r.get("false_rejections")],
    "pairs": sum(r.get("strings", 0) for r in results),
    "false_rejection_pairs": sum(r.get("false_rejections", 0) for r in results),
    "python_accepts_more_pairs": sum(r.get("python_accepts_more", 0) for r in results),
}
(out_dir / "patterns-results.json").write_text(json.dumps({"summary": summary, "results": results}, indent=1))
print(json.dumps(summary, indent=1))
for r in results:
    if r.get("false_rejections") or r.get("python_check_off") or "nix_error" in r:
        print(json.dumps(r))
