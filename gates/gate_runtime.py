#!/usr/bin/env python3
"""Gate (c): a runtime check in Python. Run it with the Python that has Pydantic.

Usage: gate_runtime.py PKGROOT PACKAGE GAPS.json [OUT.json]

Steps:
1. Import every module of the package. Each import error is a failure.
2. For each model class defined in a module: `model_rebuild(force=True)`, and
   `typing.get_type_hints(cls, include_extras=True)` (a missing class raises NameError).
3. Walk the annotation of every field (and of `__pydantic_extra__`). A leaf is BAD when it is
   `Any`, `object`, a bare `list`/`dict`/`tuple`/`set`, a TypeVar, a ForwardRef, or a type
   that the walk does not know. `JsonValue` and `Native` are named mappings and count apart.
4. Compare the Native count with the gap file of the generator.
`typing` merges a Native of the base into the tail of the union, so the count of the types is
a lower bound. The script also reads the source (the same AST view as the ty probe) and
requires: types count + merged members == source count == gap file count.
"""
import enum
import importlib
import json
import sys
import time
import types
import typing
from pathlib import Path

root, package, gaps = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
out = Path(sys.argv[4]) if len(sys.argv) > 4 else None
sys.path.insert(0, str(root))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import pydantic  # noqa: E402
import nixdantic  # noqa: E402
from nixdantic import ConfigRef, Model, Native, Package, UnsetType  # noqa: E402

# S10: the library may hold Text and NixValue (S8) or only JsonValue (S9). Both aliases are named mappings.
Text = getattr(nixdantic, "Text", None)
JSON_ALIASES = [a for a in (pydantic.JsonValue, getattr(nixdantic, "NixValue", None)) if a is not None]
from s5lib import fields_of_source, module_files, native_expected, source_view  # noqa: E402

t0 = time.monotonic()
OK_SCALARS = tuple(x for x in (bool, int, float, str, type(None), ConfigRef, Package, Text, UnsetType) if x is not None)
import collections.abc  # noqa: E402  (SG35)
BARE = (list, dict, tuple, set, frozenset, collections.abc.Mapping, collections.abc.Sequence)  # SG35: NixValue containers


def leaves(ann, path=()):
    """Yield (kind, detail) for each leaf of an annotation. kind is ok, native, json, or bad:<why>."""
    if any(ann is a for a in JSON_ALIASES):
        yield "json", getattr(ann, "__name__", "JsonValue")
        return
    if ann is Native:
        yield "native", "Native"
        return
    if ann is typing.Any:
        yield "bad:Any", "Any"
        return
    if ann is object:
        yield "bad:object", "object"
        return
    origin = typing.get_origin(ann)
    if origin is typing.Annotated:
        yield from leaves(typing.get_args(ann)[0])
        return
    if origin is typing.Literal:
        yield "ok", "Literal"
        return
    if origin in (typing.Union, types.UnionType):
        for a in typing.get_args(ann):
            yield from leaves(a)
        return
    if origin in BARE:
        args = typing.get_args(ann)
        if not args:
            yield "bad:bare", repr(ann)
        for a in args:
            yield from leaves(a)
        return
    if origin is not None:
        yield "bad:unknown-generic", repr(ann)
        return
    if ann in BARE:
        yield "bad:bare", ann.__name__
        return
    if isinstance(ann, (typing.TypeVar, typing.ForwardRef, str)):
        yield "bad:unresolved", repr(ann)
        return
    if ann in OK_SCALARS or (isinstance(ann, type) and issubclass(ann, (pydantic.BaseModel, enum.Enum))):
        yield "ok", getattr(ann, "__name__", repr(ann))
        return
    yield "bad:unknown-type", repr(ann)


failures = {"import": [], "rebuild": [], "hints": [], "bad_field": []}
fields = classes = n_native_types = n_json = concrete = native_src = merged_src = 0
mismatch = []
for mod, path in module_files(root, package):
    try:
        m = importlib.import_module(mod)
    except Exception as e:  # noqa: BLE001
        failures["import"].append(f"{mod}: {type(e).__name__}: {e}"[:300])
        continue
    srcview = {}
    for cls_name, f, text in fields_of_source(path):
        srcview[(cls_name, f)] = source_view(text, f)
    for name, cls in vars(m).items():
        if not (isinstance(cls, type) and issubclass(cls, Model) and cls.__module__ == mod and cls.__name__ == name):
            continue
        classes += 1
        try:
            cls.model_rebuild(force=True)
        except Exception as e:  # noqa: BLE001
            failures["rebuild"].append(f"{mod}.{name}: {type(e).__name__}: {e}"[:300])
        try:
            hints = typing.get_type_hints(cls, include_extras=True)
        except Exception as e:  # noqa: BLE001
            failures["hints"].append(f"{mod}.{name}: {type(e).__name__}: {e}"[:300])
            continue
        names = list(cls.model_fields) + (["__pydantic_extra__"] if "__pydantic_extra__" in hints else [])
        for f in names:
            fields += 1
            ls = list(leaves(hints[f]))
            bad = [d for k, d in ls if k.startswith("bad")]
            if bad:
                failures["bad_field"].append(f"{mod}.{name}.{f}: {sorted(set(bad))}"[:300])
                continue
            # Native in the base: top-level members other than the tail; Native alone means a pure Native field.
            ann = hints[f]
            top = [a for a in (typing.get_args(ann) if typing.get_origin(ann) in (typing.Union, types.UnionType) else [ann])]
            base = [a for a in top if a not in (ConfigRef, Native, UnsetType)]
            n = (0 if base else 1) if f != "__pydantic_extra__" else 0
            n += sum(1 for k, _ in (x for b in base for x in leaves(b)) if k == "native")
            j = sum(1 for k, _ in (x for b in base for x in leaves(b)) if k == "json")
            n_native_types += n
            n_json += j
            concrete += n == 0 and j == 0
            sv = srcview.get((name, f))
            if sv is not None:
                native_src += sv[1]
                merged_src += sv[2]
                if n != sv[1] - sv[2]:
                    mismatch.append(f"{mod}.{name}.{f}: types {n}, source {sv[1]} merged {sv[2]}")

exp = native_expected(gaps)
result = {
    "gate": "runtime", "package": package, "classes": classes, "fields": fields,
    "import_failures": len(failures["import"]), "rebuild_failures": len(failures["rebuild"]),
    "hint_failures": len(failures["hints"]), "bad_fields": len(failures["bad_field"]),
    "fully_concrete_fields": concrete,
    "native_in_types": n_native_types, "merged_in_union": merged_src, "native_in_source": native_src,
    "native_expected_gap_file": exp, "per_field_mismatch": len(mismatch),
    "jsonvalue_in_types": n_json, "seconds": round(time.monotonic() - t0, 2),
    "failures_first": {k: v[:8] for k, v in failures.items()}, "mismatch_first": mismatch[:5],
}
result["pass"] = (not any(failures.values()) and not mismatch and native_src == exp
                  and n_native_types + merged_src == exp)
if out:
    out.write_text(json.dumps(result, indent=1))
print(json.dumps({k: v for k, v in result.items() if not k.endswith("_first")}))
sys.exit(0 if result["pass"] else 1)
