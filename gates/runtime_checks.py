"""Python checks of `Text` and `NixValue` (project 008, spike S8). Each line prints PASS or FAIL.

Copy of 008 S10 `runtime_checks.py` (S8). Changes: the library path comes from the env LIBRARY; the `explain` check is skipped when the runtime has no `explain`.
Run: LIBRARY=DIR PYTHONDONTWRITEBYTECODE=1 python -I runtime_checks.py
"""
import json
import os
import sys

sys.path.insert(0, os.environ["LIBRARY"])  # the library is a parameter
from pydantic import ValidationError  # noqa: E402

from nixdantic import ConfigRef, Native, Package, Text, fragment, supplied  # noqa: E402

try:  # S10: the merged runtime has no `explain` (merge rule R4); the check of its text is skipped then
    from nixdantic import explain
except ImportError:
    explain = None
from pynix_os.environment.__options__ import Environment  # noqa: E402
from pynix_os.networking.__options__ import Networking  # noqa: E402
from pynix_os.systemd.__options__ import Systemd, Systemd_Services_Value as S  # noqa: E402

hello = Package(attr="hello")
failed = 0


def check(name: str, ok: bool, detail: object = "") -> None:
    global failed
    failed += not ok
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f": {detail}"))


def raises(fn) -> BaseException | None:
    try:
        fn()
    except BaseException as error:  # noqa: BLE001
        return error
    return None


t = Text(hello, "/bin/hello", " --greeting ", ConfigRef(path=["networking", "hostName"]))
w = supplied(t)["__nixdantic_ref__"]
check("Text wire: kind text, four parts in order", w["kind"] == "text" and len(w["parts"]) == 4, w)
check("Text wire: a string part is a bare string", w["parts"][1] == "/bin/hello", w)
check("Text wire: a reference part is tagged", w["parts"][0] == {"__nixdantic_ref__": {"kind": "package", "attr": "hello"}}, w)
check("nested Text wire is tagged at both levels", supplied(Text("a", Text(hello)))["__nixdantic_ref__"]["parts"][1]["__nixdantic_ref__"]["kind"] == "text")
check("a literal string part with dollar-brace stays a bare string", supplied(Text("${pkgs.hello}"))["__nixdantic_ref__"]["parts"] == ["${pkgs.hello}"])
check("Text() with no part is valid and empty", supplied(Text())["__nixdantic_ref__"]["parts"] == [])
check("Text(42) raises ValidationError", isinstance(raises(lambda: Text(42)), ValidationError))  # type: ignore[arg-type]
check("Text(None) raises ValidationError", isinstance(raises(lambda: Text(None)), ValidationError))  # type: ignore[arg-type]
check("Text is frozen", raises(lambda: setattr(t, "parts", [])) is not None)
check("two equal Text values are equal", Text(hello, "/bin") == Text(hello, "/bin"))
err = raises(lambda: Text(hello, 42))  # type: ignore[arg-type]
if explain is not None:
    lines = explain(err) if isinstance(err, ValidationError) else []
    check("explain gives one plain line for Text(hello, 42)", lines == ["parts[1]: Input should be a valid string (you gave 42)"], lines)
else:
    print("SKIP explain (not in this runtime)")

# Pydantic must not call Text.__init__ for a dict (this broke the first S8 build).
s = S(serviceConfig={"Nested": {"Deep": [Text(hello, "/share")]}, "A": {"kind": "text", "parts": ["a"]}, "B": {"parts": [1]}})
cfg = s.serviceConfig
check("a nested dict in free-form data stays a dict", isinstance(cfg["Nested"], dict) and isinstance(cfg["A"], dict) and isinstance(cfg["B"], dict), cfg)
check("a Text at depth 3 in free-form data is a Text", isinstance(cfg["Nested"]["Deep"][0], Text))
check("fragment wire: Text at depth 3 is tagged", supplied(s)["serviceConfig"]["Nested"]["Deep"][0]["__nixdantic_ref__"]["kind"] == "text")
check("a dict with the tag key still escapes as literal", supplied(S(serviceConfig={"X": {"__nixdantic_ref__": 1}}))["serviceConfig"]["X"] == {"__nixdantic_literal__": {"__nixdantic_ref__": 1}})

# Where Text is allowed at run time.
check("str option accepts Text", S(script=Text(hello, "/bin/hello")).script == Text(hello, "/bin/hello"))
check("str option still accepts a str", S(script="x").script == "x")
check("str option refuses Package", isinstance(raises(lambda: S(script=hello)), ValidationError))  # type: ignore[arg-type]
check("str option refuses an int", isinstance(raises(lambda: S(script=3)), ValidationError))  # type: ignore[arg-type]
check("bool option refuses Text", isinstance(raises(lambda: S(enable=Text("x"))), ValidationError))  # type: ignore[arg-type]
check("int option refuses Text", isinstance(raises(lambda: S(startLimitBurst=Text("3"))), ValidationError))  # type: ignore[arg-type]
check("pattern option (hostName) refuses Text", isinstance(raises(lambda: Networking(hostName=Text("x"))), ValidationError))  # type: ignore[arg-type]
check("list of Package or str accepts Text", S(path=[hello, "/bin", Text(hello, "/bin")]).path is not None)
check("free-form data accepts a Package (SG35)", S(serviceConfig={"E": hello}).serviceConfig is not None)
check("free-form data refuses an arbitrary object", isinstance(raises(lambda: S(serviceConfig={"E": object()})), ValidationError))  # type: ignore[dict-item]
check("dict of str values accepts Text", Environment(variables={"G": Text(hello, "/bin/hello")}).variables is not None)
check("Native stays valid at the option level", S(script=Native(file="x.nix")).script == Native(file="x.nix"))
frag = fragment(Systemd(services={"h": S(script=Text(hello))}), source="t.py:1")
check("fragment of a Systemd value is version 1 JSON", json.loads(json.dumps(frag))["version"] == 1)
print("FAILED" if failed else "ALL PASS", failed)
sys.exit(1 if failed else 0)
