"""S9 step 3: hand cases. Nix accepts the value (proved with lib.evalModules); what does the generated Python field do?

Usage: python -I cases.py GENERATOR RUNTIME_DIR OUT_DIR [--nix-json-file]

For each case (a Nix type from `cases.nix`) and each value:
  A. Nix verdict on the JSON text (lib.evalModules, one option module).
  B. Python verdict in json mode (the JSON text) and in python mode (a Python value, as a learner writes it).
  C. When python mode accepts: the text that nixdantic emits (`supplied`, json.dumps) and its Nix verdict.
The generator and the runtime are parameters, so the same cases run before and after a fix.
"""

from __future__ import annotations

import importlib
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
generator, runtime_dir, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve()
out.mkdir(parents=True, exist_ok=True)

# (case id, [(label, python source, JSON text for Nix or None = json.dumps of the Python value, note)])
CASES = [
    ("float_t", [
        ("1.0", "1.0", "1.0", ""),
        ("1 (int)", "1", "1", "Nix refuses an int for float; Python converts to 1.0"),
        ("0.1", "0.1", "0.1", ""),
        ("1e3", "1e3", "1e3", ""),
        ("true", "True", "true", "bool"),
        ("-0.0", "-0.0", "-0.0", ""),
        ("1e308", "1e308", "1e308", ""),
    ]),
    ("number_t", [("1", "1", "1", ""), ("1.0", "1.0", "1.0", ""), ("2.5", "2.5", "2.5", ""), ("true", "True", "true", "bool")]),
    ("number_between_t", [("0", "0", "0", ""), ("1", "1", "1", ""), ("0.5", "0.5", "0.5", ""), ("1.5", "1.5", "1.5", "outside the range")]),
    ("number_nonneg_t", [("0", "0", "0", ""), ("0.0", "0.0", "0.0", ""), ("-1", "-1", "-1", "outside the range")]),
    ("int_t", [
        ("1", "1", "1", ""),
        ("1.0", "1.0", "1.0", "float for int"),
        ("max int64", "9223372036854775807", "9223372036854775807", ""),
        ("min int64", "-9223372036854775808", "-9223372036854775808", ""),
        ("true", "True", "true", "bool"),
        ("2**63", "2**63", None, "outside the Nix integer range"),
    ]),
    ("u8_t", [("0", "0", None, ""), ("255", "255", None, ""), ("256", "256", None, "outside"), ("-1", "-1", None, "outside")]),
    ("s8_t", [("-128", "-128", None, ""), ("127", "127", None, ""), ("128", "128", None, "outside")]),
    ("u16_port_t", [("0", "0", None, ""), ("65535", "65535", None, ""), ("65536", "65536", None, "outside")]),
    ("u32_t", [("4294967295", "4294967295", None, ""), ("4294967296", "4294967296", None, "outside")]),
    ("s32_t", [("-2147483648", "-2147483648", None, ""), ("2147483647", "2147483647", None, "")]),
    ("positive_t", [("1", "1", None, ""), ("0", "0", None, "outside")]),
    ("unsigned_t", [("0", "0", None, ""), ("-1", "-1", None, "outside")]),
    ("between_neg_t", [("-20", "-20", None, ""), ("19", "19", None, ""), ("20", "20", None, "outside"), ("-21", "-21", None, "outside")]),
    ("bool_t", [("true", "True", None, ""), ("1", "1", "1", "int for bool")]),
    ("enum_str_t", [("a", "'a'", None, ""), ("c", "'c'", None, "outside")]),
    ("enum_int_t", [
        ("1", "1", None, ""), ("3", "3", None, ""),
        ("1.0", "1.0", "1.0", "Nix compares 1.0 == 1"),
        ("true", "True", "true", "bool"),
        ("4", "4", None, "outside"),
    ]),
    ("enum_bool_t", [("true", "True", None, ""), ("false", "False", None, ""), ("1", "1", "1", "int for bool enum")]),
    ("enum_null_t", [("null", "None", None, ""), ("a", "'a'", None, "")]),
    ("enum_float_t", [("0.5", "0.5", None, ""), ("1.5", "1.5", None, "")]),
    ("enum_mixed_t", [("a", "'a'", None, ""), ("1", "1", None, ""), ("true", "True", None, "")]),
    ("match_posix_t", [("ab_c-1", "'ab_c-1'", None, ""), ("a b", "'a b'", None, "outside"), ("empty", "''", None, "outside")]),
    ("match_dot_t", [
        ("a-b", "'a-b'", None, ""),
        ("a newline b", "'a\\nb'", None, "POSIX . matches a newline; Python . does not"),
        ("ab", "'ab'", None, ""),
        ("accented", "'a\\u00e9b'", None, "two bytes in Nix"),
    ]),
    ("match_upper_t", [("KEY_A1", "'KEY_A1'", None, ""), ("KEY_a", "'KEY_a'", None, "outside")]),
    ("match_space_t", [("abc", "'abc'", None, ""), ("a b", "'a b'", None, "outside"), ("64 chars", "'x'*64", None, ""), ("65 chars", "'x'*65", None, "outside")]),
    ("match_caret_t", [("abc", "'abc'", None, "")]),
    ("match_bracket_t", [("a]", "'a]'", None, "contrived: backslash is literal inside a POSIX bracket"), ("a", "'a'", None, "")]),
    ("either_int_str_t", [("1", "1", None, ""), ("a", "'a'", None, ""), ("1.5", "1.5", "1.5", "outside"), ("true", "True", "true", "outside")]),
    ("oneof_t", [("1", "1", None, ""), ("a", "'a'", None, ""), ("true", "True", None, ""), ("1.5", "1.5", "1.5", "outside")]),
    ("either_list_str_t", [("list", "['a','b']", None, ""), ("str", "'a'", None, ""), ("tuple", "('a','b')", '["a","b"]', "tuple; Python typing refuses it too"), ("empty list", "[]", None, "")]),
    ("either_int_float_t", [("1", "1", None, ""), ("1.0", "1.0", "1.0", "")]),
    ("coerced_t", [("str", "'a'", None, ""), ("int", "1", None, "coerced by toString")]),
    ("nullor_int_t", [("null", "None", None, ""), ("1", "1", None, "")]),
    ("nullor_float_t", [("null", "None", None, ""), ("1.0", "1.0", "1.0", ""), ("1", "1", "1", "Nix refuses an int")]),
    ("list_str_t", [("list", "['a']", None, ""), ("tuple", "('a',)", '["a"]', "tuple"), ("empty", "[]", None, "")]),
    ("list_float_t", [("1.0", "[1.0, 2.5]", None, ""), ("int", "[1, 2]", "[1, 2]", "Nix refuses ints")]),
    ("attrs_int_t", [("dict", "{'a': 1}", None, ""), ("empty", "{}", None, "")]),
    ("attrs_t", [("dict", "{'a': 1, 'b': [1, 'x', None]}", None, ""), ("empty", "{}", None, "")]),
    ("anything_t", [("int", "1", None, ""), ("list", "[1, [2], {'a': None}]", None, ""), ("float", "1.5", None, ""), ("null", "None", None, ""), ("str", "'x'", None, "")]),
    ("sub_t", [
        ("dict", "{'a': 2, 'b': 'y'}", None, "dict where a nested class is expected"),
        ("instance", "sub('sub_t', a=2, b='y')", '{"a": 2, "b": "y"}', "an instance of the generated class"),
        ("empty dict", "{}", None, ""),
    ]),
    ("list_sub_t", [("dicts", "[{'a': 2}]", None, "dicts"), ("instances", "[sub('list_sub_t', a=2)]", '[{"a": 2}]', "instances")]),
    ("attrs_sub_t", [("dicts", "{'k': {'a': 2}}", None, "dicts"), ("instances", "{'k': sub('attrs_sub_t', a=2)}", '{"k": {"a": 2}}', "instances")]),
    ("ns_sub_t", [
        ("nested dict", "{'eth0': {'name': 'x', 'ipv4': {'addresses': ['a']}}}", None, "the form that Nix takes"),
        ("flat field (instance)", "{'eth0': sub('ns_sub_t', ipv4_addresses=['a'])}", '{"eth0": {"ipv4": {"addresses": ["a"]}}}', "Python writes the namespace as one flat field"),
        ("dotted key", "{'eth0': {'ipv4.addresses': ['a']}}", '{"eth0": {"ipv4.addresses": ["a"]}}', "an attribute named `ipv4.addresses`: Nix has no such option"),
    ]),
    ("rename_t", [
        ("Nix names (dict)", "[{'type': 'hard', 'match': 'x'}]", None, "the form that Nix takes: keys `type` and `match` are Python soft keywords"),
        ("Python names (dict)", "[{'type_': 'hard', 'match_': 'x'}]", '[{"type": "hard", "match": "x"}]', "the Python field names"),
        ("instance", "[sub('rename_t', type_='hard', match_='x')]", '[{"type": "hard", "match": "x"}]', "an instance of the generated class"),
    ]),
    ("unspec_t", [("str", "'x'", None, ""), ("int", "1", None, ""), ("dict", "{'a': 1}", None, ""), ("list", "[1, 'a']", None, ""), ("null", "None", None, ""), ("bool", "True", None, "")]),
    ("raw_t", [("str", "'x'", None, ""), ("dict", "{'a': [1]}", None, "")]),
    ("elixir_tuple_t", [("tagged", "{'_elixirType': 'tuple', 'value': [0, 1]}", None, "the form that Nix accepts"), ("list", "[0, 1]", None, "a plain list: Nix refuses")]),
    ("elixir_raw_t", [("tagged", "{'_elixirType': 'raw', 'value': 'System.get_env(\"X\")'}", None, "the form that Nix accepts"), ("str", "'code'", None, "a plain string: Nix refuses")]),
    ("path_t", [("abs", "'/a/b'", None, ""), ("relative", "'a/b'", None, "outside"), ("abs newline", "'/a\\nb'", None, "POSIX . matches a newline")]),
    ("path_any_t", [("abs", "'/a/b'", None, ""), ("relative", "'a/b'", None, "Nix accepts a relative string when absolute is unset"), ("empty", "''", None, "")]),
    ("path_nostore_t", [("abs", "'/a/b'", None, ""), ("relative", "'a/b'", None, "")]),
    ("path_rel_t", [("relative", "'a/b'", None, ""), ("abs", "'/a/b'", None, "outside")]),
    ("path_instore_t", [("store", "'/nix/store/00000000000000000000000000000000-x'", None, ""), ("other", "'/a'", None, "outside")]),
    ("str_t", [("str", "'x'", None, ""), ("empty", "''", None, ""), ("unicode", "'\\u00e9\\u2603'", None, ""), ("newline", "'a\\nb'", None, "")]),
    ("nonempty_t", [("x", "'x'", None, ""), ("empty", "''", None, "Nix refuses")]),
    ("addcheck_str_t", [("short", "'abc'", None, ""), ("long", "'abcdefgh'", None, "custom check refuses; Python str accepts")]),
    ("addcheck_int_t", [("1", "1", None, ""), ("5", "5", None, "custom check refuses; Python int accepts")]),
    ("addcheck_sub_t", [("with a", "{'a': 1}", None, ""), ("without a", "{'b': 1}", None, "custom check refuses; Python accepts")]),
]


def nix_text(src: str, given: str | None) -> tuple[str | None, str]:
    """The JSON text for Nix, or None with the reason when Nix cannot read it."""
    value = eval(src, {"sub": lambda *a, **k: None})  # noqa: S307  (a literal from this file; sub() is a stub here)
    text = given if given is not None else json.dumps(value)
    if "NaN" in text or "Infinity" in text:
        return None, "not JSON for Nix"
    if isinstance(value, int) and not isinstance(value, bool) and not -(2**63) <= value < 2**63:
        return None, "outside the Nix integer range"
    return text, ""


def nix(expr: str, env: dict[str, str]) -> object:
    result = subprocess.run(["nix", "eval", "--impure", "--json", "--expr", expr], cwd=HERE, capture_output=True, text=True,
                            env={**os.environ, **env})
    if result.returncode != 0:
        raise SystemExit(result.stderr[-3000:])
    return json.loads(result.stdout)


# --- phase A: Nix verdicts and the manifest -----------------------------------------------------------------
texts_a: dict[str, dict[str, str]] = {}
skipped: dict[tuple[str, str], str] = {}
for cid, values in CASES:
    for label, src, given, _note in values:
        text, why = nix_text(src, given)
        if text is None:
            skipped[(cid, label)] = why
        else:
            texts_a.setdefault(cid, {})[label] = text
(out / "texts-a.json").write_text(json.dumps(texts_a, indent=1))
manifest = nix("(import ./cases.nix).manifest", {"S9_CASE_VALUES": "/dev/null"})
(out / "manifest.json").write_text(json.dumps(manifest))
verdict_a = nix("(import ./cases.nix).verdicts", {"S9_CASE_VALUES": str(out / "texts-a.json")})

# --- generate and import ---------------------------------------------------------------------------------
lib = out / "lib"
subprocess.run(["rm", "-rf", str(lib)], check=True)
lib.mkdir()
subprocess.run([sys.executable, "-I", str(generator), str(out / "manifest.json"), str(lib), "pynix_cases"], check=True, capture_output=True)
subprocess.run(["cp", "-r", str(runtime_dir / "nixdantic"), str(lib / "nixdantic")], check=True)
subprocess.run(["chmod", "-R", "u+w", str(lib)], check=True)
sys.path.insert(0, str(lib))
sys.dont_write_bytecode = True
from pydantic import ValidationError  # noqa: E402
from nixdantic import Model, supplied  # noqa: E402

sites = {field: (module, cls) for module, cls, field, _idx in json.loads((lib / "pynix_cases-fields.json").read_text())}


def model_class(cid: str):
    module, cls = sites[cid]
    return getattr(importlib.import_module(module), cls)


def sub(cid: str, **kw):
    """An instance of the generated class that the field `cid` holds (the first Model class in its annotation)."""
    found = []

    def walk(t):
        if isinstance(t, type) and issubclass(t, Model):
            found.append(t)
        for a in getattr(t, "__args__", ()):
            walk(a)

    walk(model_class(cid).model_fields[cid].annotation)
    return found[0](**kw)


def refusal(err: ValidationError, field: str) -> str:
    keep = [e for e in err.errors(include_url=False) if not (len(e["loc"]) > 1 and e["loc"][1] in {"ConfigRef", "Native", "is-instance[UnsetType]"})]
    return "; ".join(sorted({e["type"] for e in keep})) or "(ref branches only)"


rows = []
texts_b: dict[str, dict[str, str]] = {}
for cid, values in CASES:
    cls = model_class(cid)
    for label, src, given, note in values:
        row = {"case": cid, "label": label, "note": note, "python_value": src}
        text = texts_a.get(cid, {}).get(label)
        row["json_text"] = text
        row["nix_accepts_text"] = verdict_a[cid][label] if text is not None else None
        row["skipped"] = skipped.get((cid, label))
        # json mode
        if text is not None:
            try:
                cls.model_validate_json('{"' + cid + '":' + text + '}')
                row["python_json"] = "accepted"
            except ValidationError as err:
                row["python_json"] = "refused: " + refusal(err, cid)
        # python mode
        value = eval(src, {"sub": sub})  # noqa: S307
        try:
            inst = cls.model_validate({cid: value})
            row["python_py"] = "accepted"
            emitted = json.dumps(supplied(inst)[cid])
            row["emitted_text"] = emitted
            if "NaN" in emitted or "Infinity" in emitted or any(not -(2**63) <= int(n) < 2**63 for n in re.findall(r"(?<![\d.eE])-?\d{19,}(?![\d.eE])", emitted)):
                row["emitted_unreadable"] = True  # Nix cannot read this JSON text
            else:
                texts_b.setdefault(cid, {})[label] = emitted
        except ValidationError as err:
            row["python_py"] = "refused: " + refusal(err, cid)
        rows.append(row)
(out / "texts-b.json").write_text(json.dumps(texts_b, indent=1))
verdict_b = nix("(import ./cases.nix).verdicts", {"S9_CASE_VALUES": str(out / "texts-b.json")})
for row in rows:
    if "emitted_text" in row:
        row["nix_accepts_emitted"] = None if row.get("emitted_unreadable") else verdict_b[row["case"]][row["label"]]
for row in rows:
    nix_ok = row["nix_accepts_text"]
    row["false_rejection_json"] = bool(nix_ok and row.get("python_json", "").startswith("refused"))
    row["false_rejection_py"] = bool(nix_ok and row["python_py"].startswith("refused"))
(out / "cases-results.json").write_text(json.dumps(rows, indent=1))


def cell(x):
    return {True: "yes", False: "no", None: "-"}.get(x, x) if not isinstance(x, str) else x


print(f"{'case':20} {'label':20} {'Nix(text)':9} {'Py json':28} {'Py python':28} {'emitted':14} {'Nix(emitted)':12} FALSE-REJ")
for r in rows:
    flags = ("json " if r["false_rejection_json"] else "") + ("python" if r["false_rejection_py"] else "")
    print(f"{r['case']:20} {r['label'][:20]:20} {cell(r['nix_accepts_text']):9} {r.get('python_json', '-')[:28]:28} {r['python_py'][:28]:28} "
          f"{r.get('emitted_text', '-')[:14]:14} {cell(r.get('nix_accepts_emitted')):12} {flags}")
print("false rejections (json mode):", sum(r["false_rejection_json"] for r in rows), " (python mode):", sum(r["false_rejection_py"] for r in rows),
      " of", len(rows), "values")
