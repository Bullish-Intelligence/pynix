#!/usr/bin/env python3
"""Gate checks of the generated libraries (copy of 008 S10 `gates.py`). One subcommand per check. `run_gates.sh` calls this file.

Usage: gates.py CHECK          (the environment holds LIBRARY, OUTDIR, and the parameters; see README.md)

Each check writes OUTDIR/checks/CHECK.json: {name, status, numbers, detail, seconds, expected}.
status is PASS or FAIL. `expected` is a text when the failure has a known cause (see FEATURES).
"""
import gzip
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = os.environ["PY"]
LIB = Path(os.environ["LIBRARY"]).resolve()
OUT = Path(os.environ["OUTDIR"])
LOG = Path(os.environ["LOGDIR"])
SCRATCH = Path(os.environ["SCRATCH"])
MANIFEST_DIR = Path(os.environ["MANIFEST_DIR"])
GENERATOR = os.environ["GENERATOR"]
NIX_UNIT = os.environ["NIX_UNIT"]
PACKAGES = {"pynix_os": "nixos", "pynix_hm": "home-manager", "pynix_flake_parts": "flake-parts"}
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
for d in (OUT / "checks", OUT / "results", LOG, SCRATCH):
    d.mkdir(parents=True, exist_ok=True)


def sh(name, cmd, env=None, cwd=None):
    """Run a command, append its output to LOGDIR/NAME.txt, return (returncode, stdout)."""
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, env=env or ENV, cwd=cwd or HERE)
    with open(LOG / f"{name}.txt", "a") as fh:
        fh.write(f"$ {' '.join(str(c) for c in cmd)}\nrc={p.returncode}\n{p.stdout}\n--- stderr ---\n{p.stderr}\n\n")
    return p.returncode, p.stdout + "\n" + p.stderr


def last_json(text):
    for line in reversed(text.strip().splitlines()):
        try:
            return json.loads(line)
        except ValueError:
            continue
    return {}


def features():
    """Facts about the library that explain a known failure."""
    init = LIB / "nixdantic" / "__init__.py"
    text = init.read_text() if init.exists() else ""
    ssh = LIB / "pynix_os" / "services" / "openssh.py"
    ssh_text = ssh.read_text() if ssh.exists() else ""
    return {
        "has_text": bool(re.search(r"^class Text\b", text, re.M)),
        "has_nixvalue": bool(re.search(r"^NixValue\b|^type NixValue\b|\bNixValue\s*=", text, re.M)),
        "has_fields": all((LIB / f"{p}-fields.json").exists() for p in PACKAGES if (LIB / p).is_dir()),
        "has_s7_block": "if TYPE_CHECKING:" in ssh_text and "def __init__(self, *," in ssh_text,
    }


FEATURES = features()
NO_FIELDS = "no PACKAGE-fields.json in the library (built by a generator without the S9 field list)"
packages = [p for p in PACKAGES if (LIB / p).is_dir()]


def finish(name, ok, numbers, detail=None, seconds=0.0, expected=None):
    rec = {"name": name, "status": "PASS" if ok else "FAIL", "numbers": numbers, "detail": detail or {},
           "seconds": round(seconds, 1), "expected": expected if not ok else None}
    (OUT / "checks" / f"{name}.json").write_text(json.dumps(rec, indent=1))
    print(f"{name}: {rec['status']}{' (expected: ' + rec['expected'] + ')' if rec['expected'] else ''} {numbers}")
    return 0 if ok else 1


def per_package(name, script, extra):
    """Run a per-package S5 gate; collect the JSON line of each."""
    rows, ok = {}, True
    missing = [p for p in PACKAGES if p not in packages]
    for pkg in packages:
        rc, so = sh(name, extra(pkg))
        r = last_json(so)
        r["rc"] = rc
        rows[pkg] = r
        ok &= rc == 0 and bool(r.get("pass"))
    return rows, ok and not missing, missing


def check_s5_ty_check():
    t0 = time.monotonic()
    rows, ok, missing = per_package("s5-ty-check", None, lambda p: [PY, "-B", HERE / "gate_ty_check.py", LIB, p, OUT / "results" / f"ty-check-{p}.json"])
    nums = ", ".join(f"{p} {r.get('diagnostics', '?')}" for p, r in rows.items()) + " diagnostics" + (f"; missing {missing}" if missing else "")
    return finish("s5-ty-check", ok, nums, rows, time.monotonic() - t0)


def check_s5_ty_probe():
    t0 = time.monotonic()
    rows, ok, missing = per_package("s5-ty-probe", None, lambda p: [
        PY, "-B", HERE / "gate_ty_probe.py", LIB, p, LIB / f"{p}-gaps.json", SCRATCH / "probes" / p, OUT / "results" / f"ty-probe-{p}.json"])
    nums = "; ".join(f"{p} {r.get('fields', 0) - r.get('bad_fields', 0)}/{r.get('fields', '?')} exact, Native {r.get('native_in_source', '?')}={r.get('native_expected_gap_file', '?')}"
                     for p, r in rows.items()) + (f"; missing {missing}" if missing else "")
    return finish("s5-ty-probe", ok, nums, rows, time.monotonic() - t0)


def check_s5_runtime():
    t0 = time.monotonic()
    rows, ok, missing = per_package("s5-runtime", None, lambda p: [
        PY, "-B", HERE / "gate_runtime.py", LIB, p, LIB / f"{p}-gaps.json", OUT / "results" / f"runtime-{p}.json"])
    nums = "; ".join(f"{p} {r.get('classes', '?')} classes {r.get('fields', '?')} fields, bad {r.get('bad_fields', '?')}, Native {r.get('native_in_source', '?')}={r.get('native_expected_gap_file', '?')}"
                     for p, r in rows.items()) + (f"; missing {missing}" if missing else "")
    return finish("s5-runtime", ok, nums, rows, time.monotonic() - t0)


def check_s9_values():
    t0 = time.monotonic()
    rows, ok = {}, True
    for pkg in packages:
        manifest = MANIFEST_DIR / f"{PACKAGES[pkg]}.json"
        vdir = SCRATCH / "values" / pkg
        rc1, so = sh("s9-values", [PY, "-I", HERE / "check_values.py", LIB, pkg, manifest, vdir])
        rc2, so2 = sh("s9-values", [PY, "-I", HERE / "values_gate.py", LIB, pkg, manifest, vdir, OUT / "results" / f"values-{pkg}.json"])
        r = last_json(so2)
        r["rc"] = (rc1, rc2)
        rows[pkg] = r
        ok &= rc1 == 0 and rc2 == 0 and bool(r.get("pass"))
    tot = lambda k: sum(r.get(k, 0) for r in rows.values())  # noqa: E731
    nums = (f"kept {tot('kept')}, refused {tot('refused_json')} = {tot('gap')} counted Native gaps + {tot('unproven')} unproven examples"
            f" + {tot('outside_json')} outside (python mode outside {tot('outside_python')})")
    return finish("s9-values", ok, nums, rows, time.monotonic() - t0, NO_FIELDS if not FEATURES["has_fields"] else None)


def check_s9_patterns():
    t0 = time.monotonic()
    out = SCRATCH / "patterns"
    rc, so = sh("s9-patterns", [PY, "-I", HERE / "patterns.py", LIB, MANIFEST_DIR, out])
    try:
        s = json.loads((out / "patterns-results.json").read_text())["summary"]
    except Exception:  # noqa: BLE001
        return finish("s9-patterns", False, "no result", {"rc": rc}, time.monotonic() - t0)
    ok = rc == 0 and s["false_rejection_pairs"] == 0 and s["nix_errors"] == 0
    (OUT / "results" / "patterns-summary.json").write_text(json.dumps(s, indent=1))
    nums = f"{s['patterns']} patterns, {s['pairs']} pairs, false rejections {s['false_rejection_pairs']}, python looser {s['python_accepts_more_pairs']}, Nix errors {s['nix_errors']}"
    return finish("s9-patterns", ok, nums, s, time.monotonic() - t0)


def check_s9_limits():
    t0 = time.monotonic()
    rows, ok = {}, True
    for pkg in ("pynix_os", "pynix_hm"):
        if pkg not in packages:
            ok = False
            continue
        o = OUT / "results" / f"bounds-{pkg}.json"
        rc, so = sh("s9-limits", [PY, "-I", HERE / "bounds.py", LIB, pkg, MANIFEST_DIR / f"{PACKAGES[pkg]}.json", o, GENERATOR])
        try:
            d = json.loads(o.read_text())
            rows[pkg] = {"summary": d["summary"], "limits_equal": d["mapping"]["limits_equal"], "int_types": d["mapping"]["int_types"],
                         "limits_differ": d["mapping"]["limits_differ"]}
            ok &= rc == 0 and d["summary"]["false_rejections"] == 0
        except Exception:  # noqa: BLE001
            rows[pkg] = {"rc": rc}
            ok = False
    nums = "; ".join(f"{p} {r['summary']['values']} values, false rejections {r['summary']['false_rejections']}, python looser {r['summary']['python_looser']}, limits equal {r['limits_equal']}/{r['int_types']}"
                     for p, r in rows.items() if "summary" in r)
    return finish("s9-limits", ok, nums or "no result", rows, time.monotonic() - t0, NO_FIELDS if not FEATURES["has_fields"] else None)


def check_s9_cases():
    t0 = time.monotonic()
    out = SCRATCH / "cases"
    rc, so = sh("s9-cases", [PY, "-I", HERE / "cases.py", GENERATOR, LIB, out])
    try:
        rows = json.loads((out / "cases-results.json").read_text())
    except Exception:  # noqa: BLE001
        return finish("s9-cases", False, "no result", {"rc": rc, "tail": so[-300:]}, time.monotonic() - t0)
    fr_json = [r for r in rows if r["false_rejection_json"]]
    # S9 accepts two python-mode refusals: a tuple where a list is expected (ty refuses it too).
    fr_py = [r for r in rows if r["false_rejection_py"] and r["label"] != "tuple"]
    tuples = [r for r in rows if r["false_rejection_py"] and r["label"] == "tuple"]
    emitted_bad = [r for r in rows if r.get("nix_accepts_emitted") is False and r.get("nix_accepts_text")]
    nix_ok = sum(1 for r in rows if r["nix_accepts_text"])
    ok = rc == 0 and not fr_json and not fr_py and len(tuples) <= 2
    nums = (f"{len(rows)} values, Nix accepts {nix_ok}, false rejections json {len(fr_json)}, python {len(fr_py)} (+{len(tuples)} tuple rows allowed),"
            f" emitted text refused by Nix {len(emitted_bad)}")
    (OUT / "results" / "cases-results.json").write_text(json.dumps(rows, indent=1)[:90000])
    return finish("s9-cases", ok, nums, {"false_json": [r["case"] + "/" + r["label"] for r in fr_json],
                                         "false_python": [r["case"] + "/" + r["label"] for r in fr_py]}, time.monotonic() - t0)


def decoder_path():
    env = os.environ.get("NIXDANTIC_DECODER")
    if env:
        return env, "env NIXDANTIC_DECODER"
    for own in (LIB / "decoder.nix", LIB / "nixdantic" / "decoder.nix"):
        if own.exists():
            return str(own), "library"
    raise FileNotFoundError(f"no decoder.nix in {LIB}; set NIXDANTIC_DECODER")


# The control decoder is the decoder under test with one planted defect: the text kind drops the string context.
GOOD_TEXT = "then lib.concatStrings (lib.imap0 (i: part: textPart i (decode part)) ref.parts)"
BAD_TEXT = "then builtins.unsafeDiscardStringContext (lib.concatStrings (lib.imap0 (i: part: textPart i (decode part)) ref.parts))"


def planted_decoder(decoder):
    """Write the control decoder into the scratch directory. Fail when the decoder has no line to plant into."""
    text = Path(decoder).read_text()
    if text.count(GOOD_TEXT) != 1:
        raise RuntimeError(f"the decoder {decoder} has no line `{GOOD_TEXT}` to plant the control defect into")
    bug = SCRATCH / "decoder-bug-context.nix"
    bug.write_text(text.replace(GOOD_TEXT, BAD_TEXT))
    return bug


def check_s8_nix_unit():
    t0 = time.monotonic()
    dec, where = decoder_path()
    env = dict(ENV, NIXDANTIC_DECODER=dec)
    rc, so = sh("s8-nix-unit", [NIX_UNIT, "--impure", "--expr", f"import {HERE}/unit/tests.nix {{}}"], env=env)
    so = re.sub(r"\x1b\[[0-9;]*m", "", so)
    m = re.search(r"(\d+)/(\d+) successful", so)
    passed, total = (int(m.group(1)), int(m.group(2))) if m else (0, 0)
    # Control: a planted decoder that drops the string context must fail some tests.
    bug = planted_decoder(dec)
    rc2, so2 = sh("s8-nix-unit", [NIX_UNIT, "--impure", "--expr", f"import {HERE}/unit/tests.nix {{ decoder = {bug}; }}"], env=ENV)
    so2 = re.sub(r"\x1b\[[0-9;]*m", "", so2)
    m2 = re.search(r"(\d+)/(\d+) successful", so2)
    ctl = (int(m2.group(1)), int(m2.group(2))) if m2 else (0, 0)
    ok = rc == 0 and total > 0 and passed == total and rc2 != 0 and ctl[0] < ctl[1]
    nums = f"{passed}/{total} pass; planted bug fails {ctl[1] - ctl[0]} of {ctl[1]}; decoder: {where}"
    return finish("s8-nix-unit", ok, nums, {"decoder": dec}, time.monotonic() - t0)


def check_s8_runtime():
    t0 = time.monotonic()
    rc, so = sh("s8-runtime", [PY, "-I", HERE / "runtime_checks.py"], env=dict(ENV, LIBRARY=str(LIB)))
    npass = len(re.findall(r"^PASS ", so, re.M))
    nfail = len(re.findall(r"^FAIL ", so, re.M))
    ok = rc == 0 and nfail == 0 and npass > 0
    nums = f"{npass} of {npass + nfail} checks pass" if (npass + nfail) else "did not run: " + ([x for x in so.strip().splitlines() if x.strip()] or ["no output"])[-1][:100]
    expected = None if (FEATURES["has_text"]) else "no Text in nixdantic (library lacks S8)"
    return finish("s8-runtime", ok, nums, {"tail": so[-300:]}, time.monotonic() - t0, expected)


def check_s7_lsp():
    t0 = time.monotonic()
    o = OUT / "results" / "lsp.json"
    rc, so = sh("s7-lsp", [PY, "-I", HERE / "s7_probe.py", LIB, o, SCRATCH / "s7"])
    r = last_json(so)
    ok = rc == 0 and bool(r.get("pass"))
    probes = r.get("probes", [])
    nums = ("hover/completion/signature (h c s): " + " ".join(probes)) if probes else f"no probe: {r.get('error')}"
    full = json.loads(o.read_text()) if o.exists() else {}
    r = dict(r, classes=full.get("classes", {}))
    no_block = [c for c, i in r.get("classes", {}).items() if not i.get("has_block")]
    failing = [c for c, i in r.get("classes", {}).items() if i.get("error") or not all(all(k.get(x) for x in ("hover", "completion", "signature")) for k in i.get("keywords", {}).values())]
    expected = ("no S7 block in " + ", ".join(no_block)) if (not ok and failing and set(failing) <= set(no_block)) else None
    return finish("s7-lsp", ok, nums, r, time.monotonic() - t0, expected)


def check_s5_canaries():
    t0 = time.monotonic()
    o = OUT / "results" / "canaries.json"
    rc, so = sh("s5-canaries", [PY, "-I", HERE / "canaries.py", LIB, SCRATCH / "canaries", o])
    r = last_json(so)
    ok = rc == 0 and bool(r.get("pass"))
    nums = (f"D0 clean passes; caught D1-D5 (+D1b): ty check {r.get('caught_count', {}).get('b_ty_check')}, ty probe {r.get('caught_count', {}).get('a_ty_probe')},"
            f" runtime {r.get('caught_count', {}).get('c_runtime')} of 6; differences from S5: {len(r.get('differences_from_S5', []))}") if r else "no result"
    return finish("s5-canaries", ok, nums, r, time.monotonic() - t0)


CHECKS = {
    "s5-ty-check": check_s5_ty_check, "s5-ty-probe": check_s5_ty_probe, "s5-runtime": check_s5_runtime,
    "s9-values": check_s9_values, "s9-patterns": check_s9_patterns, "s9-limits": check_s9_limits, "s9-cases": check_s9_cases,
    "s8-nix-unit": check_s8_nix_unit, "s8-runtime": check_s8_runtime, "s7-lsp": check_s7_lsp, "s5-canaries": check_s5_canaries,
}

if __name__ == "__main__":
    name = sys.argv[1]
    if name == "features":
        print(json.dumps(FEATURES))
        sys.exit(0)
    try:
        sys.exit(CHECKS[name]())
    except Exception as exc:  # noqa: BLE001
        sys.exit(finish(name, False, f"crashed: {type(exc).__name__}: {exc}"[:200]))
