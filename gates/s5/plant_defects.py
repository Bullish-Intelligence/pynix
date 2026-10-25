#!/usr/bin/env python3
"""Plant defects in copies of pynix_os. The source library is never changed.

Usage: plant_defects.py SRCROOT DESTDIR

SRCROOT holds `pynix_os` and `nixdantic`. DESTDIR/<ID>/ gets one copy per defect, and DESTDIR/D0 is a clean copy.
Every defect edits one line: the field `enable` of `pynix_os/services/a2boot.py`.
"""
import shutil
import sys
from pathlib import Path

src, dest = Path(sys.argv[1]), Path(sys.argv[2])
FILE = Path("pynix_os/services/a2boot.py")
CLEAN = "    enable: bool | ConfigRef | Native | UnsetType = Unset"
DEFECTS = {
    "D0": ("clean copy", None, None),
    "D1": ("field annotated Any (in the union)", "    enable: Any | ConfigRef | Native | UnsetType = Unset", "from typing import Any"),
    "D1b": ("field annotated Any (alone)", "    enable: Any = Unset", "from typing import Any"),
    "D2": ("annotation names a missing class", "    enable: MissingClass | ConfigRef | Native | UnsetType = Unset", None),
    "D3": ("field typed object", "    enable: object | ConfigRef | Native | UnsetType = Unset", None),
    "D4": ("a new Native mapping that the gap file does not count", "    enable: Native | ConfigRef | Native | UnsetType = Unset", None),
    "D5": ("field typed with a bare list", "    enable: list | ConfigRef | Native | UnsetType = Unset", None),
}
for ident, (_what, line, extra_import) in DEFECTS.items():
    target = dest / ident
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for pkg in ("pynix_os", "nixdantic"):
        shutil.copytree(src / pkg, target / pkg, copy_function=shutil.copyfile, ignore=shutil.ignore_patterns("__pycache__"))
    for p in target.rglob("*"):
        p.chmod(0o755 if p.is_dir() else 0o644)
    if line is None:
        continue
    f = target / FILE
    text = f.read_text()
    assert text.count(CLEAN) == 1, ident
    text = text.replace(CLEAN, line)
    if extra_import:
        text = text.replace("from pydantic import Field\n", "from pydantic import Field\n" + extra_import + "\n", 1)
    f.write_text(text)
    print(ident, "-", _what)
