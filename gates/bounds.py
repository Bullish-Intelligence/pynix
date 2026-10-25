"""S9: numeric limits. The extractor finds the true limits of each integer leaf type with the `check` of the type itself
(a binary search), and the answer of each float and number leaf type to a short probe list. This script asks the
generated Python field the same questions.

Usage: python -I bounds.py LIB_DIR PACKAGE MANIFEST OUT_JSON GENERATOR_PY

For an integer type with limits LO and HI: LO-1, LO, HI, HI+1, 0, 1, -1 and the seed. A false rejection is a value that
Nix accepts and Python refuses. A looser Python field (accepts what Nix refuses) is counted apart.
"""

from __future__ import annotations

import importlib
import json
import sys
import warnings
from pathlib import Path

lib_dir, package, manifest_path, out_path = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
generator_py = Path(sys.argv[5])
sys.path.insert(0, lib_dir)
sys.dont_write_bytecode = True
warnings.simplefilter("ignore")
from pydantic import ValidationError  # noqa: E402

MAXI, MINI = 2**63 - 1, -(2**63)
manifest = json.loads(manifest_path.read_text())
pool, types = manifest["optionPool"], manifest["types"]
sites = json.loads((Path(lib_dir) / f"{package}-fields.json").read_text())
first_site: dict[int, list] = {}
for module, cls, field, idx in sites:
    first_site.setdefault(pool[idx]["type"], [module, cls, field])

# The generator maps every integer type from its description. Compare that mapping with the true limits for
# all integer leaf types, also the types that no option holds directly.
import importlib.util  # noqa: E402
import re  # noqa: E402

spec = importlib.util.spec_from_file_location("s9_generator", generator_py)
generator_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator_module)
gen = generator_module.Generator(manifest, package, "s9")
mapping = {"int_types": 0, "no_seed": 0, "limits_equal": 0, "limits_differ": []}
for tid, t in enumerate(types):
    n = t.get("numeric")
    if not n or n["kind"] != "int":
        continue
    mapping["int_types"] += 1
    if n.get("seed") is None:
        mapping["no_seed"] += 1
        continue
    annotation = gen._typed(tid, "X", "")
    ge = re.search(r"ge=(-?\d+)", annotation)
    le = re.search(r"le=(-?\d+)", annotation)
    got = (int(ge.group(1)) if ge else None, int(le.group(1)) if le else None)
    if got == (n["lo"], n["hi"]):
        mapping["limits_equal"] += 1
    else:
        mapping["limits_differ"].append({"description": t["description"], "nix": [n["lo"], n["hi"]], "generator": list(got)})

FLOATS = ["0.0", "1.0", "-1.0", "0.5", "1.5", "1.0e10"]
INTS = ["0", "1", "-1", "100"]
rows, summary = [], {"types": 0, "no_site": 0, "values": 0, "false_rejections": 0, "python_looser": 0}
for tid, t in enumerate(types):
    n = t.get("numeric")
    if not n:
        continue
    if tid not in first_site:
        summary["no_site"] += 1
        continue
    module, cls_name, field = first_site[tid]
    cls = getattr(importlib.import_module(module), cls_name)
    probes: list[tuple[str, bool]] = []
    if n["kind"] == "int":
        if n.get("seed") is None:
            continue
        lo, hi = n["lo"], n["hi"]
        vals = {0, 1, -1, n["seed"]}
        if lo is not None:
            vals |= {lo, lo - 1}
        if hi is not None:
            vals |= {hi, hi + 1}
        for v in sorted(vals):
            if MINI <= v <= MAXI:
                probes.append((str(v), (lo is None or v >= lo) and (hi is None or v <= hi)))
    else:
        probes += list(zip(FLOATS, n["floats"], strict=True)) + list(zip(INTS, n["ints"], strict=True))
    summary["types"] += 1
    for text, nix_ok in probes:
        try:
            cls.model_validate_json('{"' + field + '":' + text + '}')
            py_ok = True
        except ValidationError:
            py_ok = False
        summary["values"] += 1
        if nix_ok and not py_ok:
            summary["false_rejections"] += 1
        if py_ok and not nix_ok:
            summary["python_looser"] += 1
        if nix_ok != py_ok:
            rows.append({"type": tid, "ctor": t["ctor"], "name": t["name"], "description": t["description"], "numeric": n,
                         "site": f"{module}.{cls_name}.{field}", "value": text, "nix": nix_ok, "python": py_ok})
out_path.write_text(json.dumps({"summary": summary, "mapping": mapping, "differences": rows}, indent=1))
print(json.dumps(mapping))
print(json.dumps(summary))
for r in rows[:30]:
    print(r["description"], r["value"], "nix", r["nix"], "python", r["python"])
