#!/usr/bin/env python3
"""Gate (b): `ty check` on the package. Pass when ty reports zero diagnostics.

Usage: gate_ty_check.py PKGROOT PACKAGE [OUT.json]
"""
import json
import re
import subprocess
import sys
import time
from pathlib import Path

from s5lib import PYTHON, TY

root, package = Path(sys.argv[1]), sys.argv[2]
out = Path(sys.argv[3]) if len(sys.argv) > 3 else None
t0 = time.monotonic()
p = subprocess.run(
    [TY, "check", "--python", PYTHON, "--extra-search-path", str(root), "--output-format", "concise",
     "--no-progress", str(root / package)],
    capture_output=True, text=True)
secs = time.monotonic() - t0
lines = [l for l in p.stdout.splitlines() if re.match(r"\S+:\d+:\d+: (error|warning)\[", l)]
result = {"gate": "ty-check", "package": package, "diagnostics": len(lines), "seconds": round(secs, 2),
          "first": lines[:10], "pass": len(lines) == 0 and p.returncode == 0}
if out:
    out.write_text(json.dumps(result, indent=1))
print(json.dumps({k: result[k] for k in ("gate", "package", "diagnostics", "pass")}))
sys.exit(0 if result["pass"] else 1)
