#!/usr/bin/env python3
"""Usage: summary.py OUTDIR LIBRARY CHECK... : write summary.txt and summary.json from OUTDIR/checks/*.json. Exit 1 on a FAIL."""
import json
import sys
from pathlib import Path

out, lib, names = Path(sys.argv[1]), sys.argv[2], sys.argv[3:]
recs = []
for n in names:
    p = out / "checks" / f"{n}.json"
    recs.append(json.loads(p.read_text()) if p.exists() else
                {"name": n, "status": "FAIL", "numbers": "no result (the check crashed or did not run)", "seconds": 0, "expected": None, "detail": {}})
ok = all(r["status"] == "PASS" for r in recs)
lines = [f"library: {lib}", f"result: {'PASS' if ok else 'FAIL'} ({sum(r['status'] == 'PASS' for r in recs)} of {len(recs)} checks pass)", ""]
for r in recs:
    status = r["status"] + (f" (expected: {r['expected']})" if r.get("expected") else "")
    lines.append(f"{r['name']:12} {status:12} {r['numbers']}; {r['seconds']} s")
(out / "summary.txt").write_text("\n".join(lines) + "\n")
(out / "summary.json").write_text(json.dumps({"library": lib, "pass": ok, "checks": [{k: r[k] for k in ("name", "status", "numbers", "seconds", "expected")} for r in recs]}, indent=1) + "\n")
print("\n".join(lines))
sys.exit(0 if ok else 1)
