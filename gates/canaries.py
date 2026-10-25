#!/usr/bin/env python3
"""S10 check s5-canaries: plant the S5 defects D0 to D5 in a writable copy of the library and run the gates on each.

Usage: canaries.py LIBRARY SCRATCH OUT.json

Uses plant_defects.py of S5 (copy in s5/). Needs `pynix_os/services/a2boot.py` with the clean line of S5.
Gates: b ty check, a ty probe, c runtime (the unified S10 copies; d verifytypes is not part of S10).
The expected matrix is s5/matrix-expected.json (the S5 result). D0 must pass every gate. A defect must be caught by
the same gates as in S5. A gate that catches a defect which S5 missed, or misses one that S5 caught, fails the check.
The runs of the defects go in parallel (CANARY_JOBS, default 3).
"""
import concurrent.futures
import json
import os
import subprocess
import sys
import time
from pathlib import Path

here = Path(__file__).resolve().parent
lib, scratch, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
py = os.environ["PY"]
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
t0 = time.monotonic()
defects = scratch / "defects"
scratch.mkdir(parents=True, exist_ok=True)
plant = subprocess.run([py, "-B", str(here / "s5" / "plant_defects.py"), str(lib), str(defects)], capture_output=True, text=True, env=env)
if plant.returncode != 0:
    out.write_text(json.dumps({"pass": False, "error": "plant_defects failed: " + (plant.stderr or plant.stdout)[-400:]}))
    print(json.dumps({"pass": False, "error": "plant_defects failed"}))
    sys.exit(1)
gaps = lib / "pynix_os-gaps.json"
expected = json.loads((here / "s5" / "matrix-expected.json").read_text())


def run_one(name):
    root = defects / name
    work = scratch / "probes" / name
    cmds = {
        "b_ty_check": [py, "-B", str(here / "gate_ty_check.py"), str(root), "pynix_os"],
        "a_ty_probe": [py, "-B", str(here / "gate_ty_probe.py"), str(root), "pynix_os", str(gaps), str(work)],
        "c_runtime": [py, "-B", str(here / "gate_runtime.py"), str(root), "pynix_os", str(gaps)],
    }
    row = {}
    for g, cmd in cmds.items():
        p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=here)
        row[g] = p.returncode != 0
    return name, row


names = sorted(d.name for d in defects.iterdir())
matrix = {}
with concurrent.futures.ThreadPoolExecutor(int(os.environ.get("CANARY_JOBS", "3"))) as pool:
    for name, row in pool.map(run_one, names):
        matrix[name] = row
wrong = []
for name in names:
    for g, caught in matrix[name].items():
        want = expected[name][g]["caught"]
        if caught != want:
            wrong.append(f"{name}/{g}: caught={caught}, S5 caught={want}")
res = {
    "pass": not wrong, "defects": names, "matrix": matrix, "differences_from_S5": wrong,
    "caught_count": {g: sum(matrix[n][g] for n in names if n != "D0") for g in ("b_ty_check", "a_ty_probe", "c_runtime")},
    "seconds": round(time.monotonic() - t0, 1),
}
out.write_text(json.dumps(res, indent=1))
print(json.dumps({k: res[k] for k in ("pass", "caught_count", "differences_from_S5", "seconds")}))
sys.exit(0 if res["pass"] else 1)
