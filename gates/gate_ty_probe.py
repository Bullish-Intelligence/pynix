#!/usr/bin/env python3
"""Gate (a): a ty probe. Reveal the type of every option field of every class, and classify it.

Usage: gate_ty_probe.py PKGROOT PACKAGE GAPS.json PROBEDIR [OUT.json]

Steps:
1. Read each module by AST (no import) and list the fields of each class.
2. Write one probe file per module under PROBEDIR:
       import pkg.mod as m;  _0 = m.Cls();  reveal_type(_0.field)
3. Run `ty check` once on PROBEDIR. Read each `Revealed type` line.
4. A field is BAD when its revealed type holds Unknown, Any, object, or Todo (string literals removed).
   The union tail `ConfigRef | Native | UnsetType` is the escape that every option field carries.
   What is left is the base. A base that holds Native or JsonValue is a named mapping.
5. Compare the Native count of each field with the source (ty merges a Native of the base into the tail,
   so the source count minus the merged members must equal the count that ty shows).
   Compare the total Native count of the source with the gap file of the generator.
   ty shows the alias JsonValue as its first-level expansion; the script folds that back to `JsonValue`.
Pass: no BAD field, no missing reveal, no other ty diagnostic, no per-field mismatch, total equals gap file.
"""
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from s5lib import BAD_TOKEN, ESCAPES, PYTHON, TY, fields_of_source, json_expected, module_files, native_expected, source_view, split_union, strip_strings

root, package, gaps, probedir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
out = Path(sys.argv[5]) if len(sys.argv) > 5 else None

if probedir.exists():
    shutil.rmtree(probedir)
probedir.mkdir(parents=True)

where = {}  # (probe file name, line) -> (module, class, field)
src = {}  # (module, class, field) -> (native count, merged native members, jsonvalue count)
total = 0
for mod, path in module_files(root, package):
    classes = {}
    for cls, field, text in fields_of_source(path):
        classes.setdefault(cls, []).append(field)
        _base, nat, merged, js = source_view(text, field, flatten=True)  # S10: ty flattens Annotated unions
        src[(mod, cls, field)] = (nat, merged, js)
    if not classes:
        continue
    name = f"probe_{mod.replace('.', '_')}.py"
    lines = ["from typing import reveal_type", f"import {mod} as m"]
    for i, (cls, fields) in enumerate(classes.items()):
        lines.append(f"_{i} = m.{cls}()")
        for f in fields:
            lines.append(f"reveal_type(_{i}.{f})")
            where[(name, len(lines))] = (mod, cls, f)
            total += 1
    (probedir / name).write_text("\n".join(lines) + "\n")

t0 = time.monotonic()
p = subprocess.run(
    [TY, "check", "--python", PYTHON, "--extra-search-path", str(root), "--output-format", "concise",
     "--no-progress", str(probedir)],
    capture_output=True, text=True)
secs = time.monotonic() - t0

revealed, other = {}, []
for line in p.stdout.splitlines():
    m = re.match(r"(\S+):(\d+):\d+: (\w+)\[([\w-]+)\] (.*)$", line)
    if not m:
        continue
    file, ln, _sev, rule, msg = m.groups()
    key = (Path(file).name, int(ln))
    r = re.match(r"Revealed type: `(.*)`$", msg)
    if rule == "revealed-type" and r:
        revealed[key] = r.group(1)
    else:
        other.append(line)

# S10: ty prints an alias as its first-level expansion. Fold both aliases back to their names.
JSON_EXPANSIONS = {
    "list[JsonValue] | dict[str, JsonValue] | str | float | None": "JsonValue",  # S9
    "None | float | str | Text | list[NixValue] | dict[str, NixValue]": "NixValue",  # S8
    "None | float | Sequence[NixValue] | Text | Package | ConfigRef | Native | PathRef | Mapping[str, NixValue]": "NixValue",  # SG35
}
bad, missing, mismatch = [], [], []
native_found = json_found = concrete = native_src = 0
for key, ident in where.items():
    r = revealed.get(key)
    if r is None:
        missing.append("%s.%s.%s" % ident)
        continue
    if BAD_TOKEN.search(strip_strings(r)):
        bad.append({"field": "%s.%s.%s" % ident, "type": r})
        continue
    for exp, alias in JSON_EXPANSIONS.items():
        r = r.replace(exp, alias)
    base = [x for x in split_union(r) if x not in ESCAPES]
    n = (0 if base else 1) + sum(len(re.findall(r"\bNative\b", x)) for x in base)
    j = sum(len(re.findall(r"\b(?:JsonValue|NixValue)\b", x)) for x in base)
    nat, merged, _js = src[ident]
    native_found += n
    native_src += nat
    json_found += j
    concrete += n == 0 and j == 0
    if n != nat - merged:
        mismatch.append({"field": "%s.%s.%s" % ident, "type": r, "source_native": nat, "merged": merged})

exp_native = native_expected(gaps)
exp_json = json_expected(gaps)
result = {
    "gate": "ty-probe", "package": package, "fields": total, "revealed": len(revealed),
    "bad_fields": len(bad), "missing_reveals": len(missing), "other_diagnostics": len(other),
    "fully_concrete_fields": concrete,
    "native_in_revealed_types": native_found, "native_in_source": native_src, "native_expected_gap_file": exp_native,
    "per_field_mismatch": len(mismatch),
    "jsonvalue_in_revealed_types": json_found, "jsonvalue_gap_count": exp_json,
    "score_exact": round(1 - len(bad) / total, 6) if total else None,
    "seconds_ty": round(secs, 2),
    "bad_first": bad[:15], "mismatch_first": mismatch[:5], "missing_first": missing[:5], "other_first": other[:5],
}
result["pass"] = not bad and not missing and not other and not mismatch and native_src == exp_native
if out:
    out.write_text(json.dumps(result, indent=1))
print(json.dumps({k: v for k, v in result.items() if not k.endswith("_first")}))
sys.exit(0 if result["pass"] else 1)
