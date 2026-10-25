#!/usr/bin/env python3
"""S10 check s9-values, step 2: sort the refusals of check_values.py and fail on a refusal outside the counted gaps.

Usage: values_gate.py LIB PACKAGE MANIFEST VALUES_DIR OUT.json

VALUES_DIR holds the output of check_values.py (summary.json, refusals.jsonl.gz). A refusal is allowed in two cases:
  unproven   tier `unresolved`: Nix acceptance of the example is not proven (S9: probably a wrong upstream example)
  gap        the option type holds a type that the generator maps to `Native` (a counted gap): a constructor that
             the gap file names with a reason outside NOT_NATIVE_GAPS, the type named `Native`, a secret, or a
             whole-configuration submodule. The scan walks the type tree, submodule options and free-form types included.
Every other refusal is outside the counted gaps. The gate fails on it.
"""
import collections
import gzip
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s5lib import NOT_NATIVE_GAPS, fields_of_source, source_view  # noqa: E402

lib, package, manifest_path, vdir, out = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[5])
manifest = json.loads(manifest_path.read_text())
pool, types = manifest["optionPool"], manifest["types"]
sites = {f"{m}.{c}.{f}": idx for m, c, f, idx in json.loads((lib / f"{package}-fields.json").read_text())}
gaps = json.loads((lib / f"{package}-gaps.json").read_text())["gaps"]
native_ctors = {"Native"} | {r.split(":")[0] for r in gaps if r not in NOT_NATIVE_GAPS and not r.startswith("submodule")}
cache: dict[int, bool] = {}


def has_native(tid: int, stack: frozenset = frozenset()) -> bool:
    """True when the type tree under tid holds a type that the generator maps to Native."""
    if tid in cache:
        return cache[tid]
    if tid in stack:
        return False
    t = types[tid]
    found = t["ctor"] in native_ctors or t.get("name") == "Native"
    if not found:
        stack = stack | {tid}
        kids = list(t.get("nested", {}).values())
        if t.get("submodule") and len(t.get("options", [])) <= 1000:
            kids += [pool[r]["type"] for r in t["options"]]
        found = any(has_native(k, stack) for k in kids)
    if found or not stack:  # a False found under a cycle guard may be partial: cache only True or a root result
        cache[tid] = found
    return found


mod_cache: dict[str, dict] = {}


def pure_native(site: str) -> bool:
    """True when the generated field takes only Native, ConfigRef, or Unset (a whole-configuration submodule, a function)."""
    module, cls, field = site.rsplit(".", 2)
    if module not in mod_cache:
        path = lib / Path(*module.split("."))
        path = path.with_suffix(".py") if path.with_suffix(".py").exists() else path / "__init__.py"
        mod_cache[module] = {(c, f): t for c, f, t in fields_of_source(path)}
    text = mod_cache[module].get((cls, field))
    return text is not None and all(m == "Native" for m in source_view(text, field)[0])


rows = collections.Counter()
outside = []
by_mode = collections.Counter()
with gzip.open(vdir / "refusals.jsonl.gz", "rt") as fh:
    for line in fh:
        item = json.loads(line)
        by_mode[item["mode"]] += 1
        idx = sites.get(item["site"])
        if item["tier"] == "unresolved":
            kind = "unproven"
        elif idx is not None and has_native(pool[idx]["type"]):
            kind = "gap"
        elif pure_native(item["site"]):
            kind = "gap"  # the field takes only Native (whole-configuration submodule): the generated class cannot hold a value
        elif any("Native" in e["loc"] for e in item["errors"]):
            kind = "gap"
        else:
            kind = "outside"
            outside.append({k: item[k] for k in ("mode", "kind", "tier", "site", "signature", "value", "error_types")})
        rows[(item["mode"], kind)] += 1

summary = json.loads((vdir / "summary.json").read_text())
c = summary["counts"]
res = {
    "package": package,
    "kept": c.get("default.kept", 0) + c.get("example.kept", 0),
    "accepted_json": c.get("default.json.accepted", 0) + c.get("example.json.accepted", 0),
    "refused_json": by_mode["json"], "refused_python": by_mode["python"],
    "gap": rows[("json", "gap")], "unproven": rows[("json", "unproven")], "outside_json": rows[("json", "outside")],
    "outside_python": rows[("python", "outside")],
    "import_failures": len(summary["import_failures"]), "no_class": c.get("default.no_class", 0) + c.get("example.no_class", 0),
    "seconds": summary["seconds"], "outside_first": outside[:10],
    "native_ctors": sorted(native_ctors),
}
res["pass"] = not outside and not res["import_failures"] and not res["no_class"]
out.write_text(json.dumps(res, indent=1))
print(json.dumps({k: v for k, v in res.items() if k not in ("outside_first", "native_ctors")}))
sys.exit(0 if res["pass"] else 1)
