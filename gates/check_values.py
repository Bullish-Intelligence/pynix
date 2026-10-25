"""S9 step 2: validate each Nix-accepted default and example value against the generated Python field.

Usage: python -I check_values.py LIB_DIR PACKAGE MANIFEST OUT_DIR

LIB_DIR  directory that holds PACKAGE/, nixdantic/, and PACKAGE-fields.json (the generator writes the last file)
MANIFEST the S9 manifest of the same package (pooled records with `values`)
OUT_DIR  receives summary.json, refusals.jsonl.gz, causes.json

A value is checked in two modes, through the generated class that owns the field (strict models):
- json:   model_validate_json('{"FIELD": TEXT}'), TEXT is the exact text that Nix printed (builtins.toJSON).
- python: model_validate({"FIELD": json.loads(TEXT)}): a Python learner who writes plain dicts and lists.
A value is kept when `type.check` is true and the full check did not fail on a type with no submodule. The tier says how
sure the Nix acceptance is: full, forced (certain), unresolved or shallow (not proven).
"""

from __future__ import annotations

import collections
import gzip
import importlib
import json
import sys
import time
import warnings
from pathlib import Path

lib_dir, package, manifest_path, out_dir = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
sys.path.insert(0, lib_dir)
out_dir.mkdir(parents=True, exist_ok=True)

from pydantic import ValidationError  # noqa: E402

REF_BRANCH = {"ConfigRef", "Native", "Package", "is-instance[UnsetType]", "enum[UnsetType]", "UnsetType"}

manifest = json.loads(manifest_path.read_text())
pool, types = manifest["optionPool"], manifest["types"]
sites = json.loads((Path(lib_dir) / f"{package}-fields.json").read_text())


def signature(tid: int, depth: int = 0, stack: tuple = ()) -> str:
    """Compact Nix constructor tree of a type, for example `nullOr(strMatching)`."""
    t = types[tid]
    name = t["ctor"] + ("*" if t.get("submodule") else "")
    if tid in stack or depth >= 4:
        return name + "..."
    kids = t.get("nested", {})
    if t.get("submodule") or not kids:
        return name
    return name + "(" + ",".join(signature(k, depth + 1, stack + (tid,)) for _, k in sorted(kids.items())) + ")"


def leaf_ctors(tid: int, stack: tuple = ()) -> list[str]:
    t = types[tid]
    kids = t.get("nested", {})
    if tid in stack:
        return []
    if t.get("submodule") or not kids:
        return [t["ctor"] + ("*" if t.get("submodule") else "")]
    out: list[str] = []
    for _, k in sorted(kids.items()):
        out += leaf_ctors(k, stack + (tid,))
    return out


def real_errors(err: ValidationError, field: str) -> list[dict]:
    result = []
    for e in err.errors(include_url=False):
        loc = e["loc"]
        if len(loc) > 1 and loc[0] == field and isinstance(loc[1], str) and loc[1] in REF_BRANCH:
            continue
        result.append({"type": e["type"], "loc": [str(p) for p in loc[1:]], "msg": e["msg"][:160]})
    return result


start = time.perf_counter()
warnings.simplefilter("ignore")
classes: dict[tuple[str, str], type | None] = {}
count = collections.Counter()
distinct = collections.defaultdict(set)  # counter name -> set of (pool index, kind)
refusals = []
cause = collections.defaultdict(lambda: {"count": 0, "examples": []})
state_count = collections.Counter()
import_failures = []

for module, cls_name, field, idx in sites:
    rec = pool[idx]
    values = rec.get("values", {})
    for kind in ("default", "example"):
        info = values.get(kind)
        if info is None:
            continue
        state = info["state"]
        state_count[(kind, state)] += 1
        if state != "plain":
            continue
        count[f"{kind}.plain"] += 1
        deep = info["deep"]
        if not info["check"]:
            count[f"{kind}.nix_refuses.check"] += 1
            continue
        has_sub = info.get("sub", False)
        if deep == "fail" and not has_sub:
            count[f"{kind}.nix_refuses.deep"] += 1
            continue
        # full: no submodule in the type, full merge check ok. forced: a submodule inside; the merged value and all
        # its nested option values evaluate. unresolved: a submodule inside; forcing fails (this can be a nested
        # option with no value, so it does not prove a type error). shallow: only `type.check` ran.
        tier = {"ok": "forced" if has_sub else "full", "fail": "unresolved", "not run": "shallow"}[deep]
        count[f"{kind}.kept.{tier}"] += 1
        count[f"{kind}.kept"] += 1
        key = (module, cls_name)
        if key not in classes:
            try:
                classes[key] = getattr(importlib.import_module(module), cls_name)
            except Exception as exc:  # noqa: BLE001
                classes[key] = None
                import_failures.append([module, cls_name, repr(exc)[:200]])
        cls = classes[key]
        if cls is None:
            count[f"{kind}.no_class"] += 1
            continue
        text = info["json"]
        python_value = json.loads(text)
        for mode in ("json", "python"):
            try:
                if mode == "json":
                    cls.model_validate_json('{' + json.dumps(field) + ':' + text + '}')
                else:
                    cls.model_validate({field: python_value})
                count[f"{kind}.{mode}.accepted"] += 1
                count[f"{kind}.{tier}.{mode}.accepted"] += 1
            except ValidationError as err:
                count[f"{kind}.{mode}.refused"] += 1
                count[f"{kind}.{tier}.{mode}.refused"] += 1
                errs = real_errors(err, field)
                tid = rec["type"]
                sig = signature(tid)
                leaves = sorted(set(leaf_ctors(tid)))
                etypes = sorted({e["type"] for e in errs}) or ["(ref branches only)"]
                item = {
                    "mode": mode, "kind": kind, "tier": tier, "site": f"{module}.{cls_name}.{field}",
                    "path": ".".join(rec["path"]), "ctor": types[tid]["ctor"], "signature": sig, "leaves": leaves,
                    "value": text[:300], "error_types": etypes, "errors": errs[:3],
                    "unknown_keys": sorted({e["loc"][-1] for e in errs if e["type"] == "extra_forbidden" and e["loc"]}),
                    "error_count": len(errs),
                }
                refusals.append(item)
                ck = f"{mode} | {'+'.join(etypes)} | {','.join(leaves)}"
                c = cause[ck]
                c["count"] += 1
                if len(c["examples"]) < 3:
                    c["examples"].append({k: item[k] for k in ("kind", "site", "path", "signature", "value", "errors")})

summary = {
    "package": package,
    "sites": len(sites),
    "sites_with_record_values": sum(1 for s in sites if pool[s[3]].get("values")),
    "state_counts": {f"{k[0]}:{k[1]}": v for k, v in sorted(state_count.items())},
    "counts": dict(sorted(count.items())),
    "import_failures": import_failures,
    "seconds": round(time.perf_counter() - start, 2),
}
(out_dir / "summary.json").write_text(json.dumps(summary, indent=1, sort_keys=True) + "\n")
with gzip.open(out_dir / "refusals.jsonl.gz", "wt") as fh:
    for r in refusals:
        fh.write(json.dumps(r, sort_keys=True) + "\n")
ordered = dict(sorted(cause.items(), key=lambda kv: -kv[1]["count"]))
(out_dir / "causes.json").write_text(json.dumps(ordered, indent=1, sort_keys=True) + "\n")
print(json.dumps({"seconds": summary["seconds"], "counts": summary["counts"]}, indent=1))
