"""Record the files that an entry (`home.py`, `system.py`) reads while it runs (009-D45, SG38).

The compile writes the result into the JSON as `reads`. The Nix side hashes the same files again, so an edit of a
file that the entry reads marks the JSON stale, as an edit of the entry does.

Use:

    with Reads(source, out) as reads:
        ...run the entry...
    compiled["reads"] = reads.result()      # {"files": {PATH: SHA256}, "absent": [PATH], "dirs": {PATH: [NAME]}, "ignore": [NAME]}
    lines = reads.refusals()                # one plain line for each read outside the workspace

PATH is relative to the folder of the entry. A file below the folder is recorded. A folder listing (`iterdir`,
`glob`, `os.listdir`, `os.scandir`) is recorded as its names. A read of a Nix store path is not recorded, because the
store path names the content. A read of the library code is not recorded. The library code is an entry of `sys.path`
that exists when the audit starts and lies outside the workspace. Two kinds of entry are not library code:

- The folder of the entry and every folder above it. Such an entry would hide every read of the workspace.
- A folder inside the workspace, unless the caller names it in `inside_libs`. The default is `.basix/pynix`, the
  generated input packages. A Nix store path pins that folder.

The audit treats a dropped entry as workspace code. Its reads and modules are recorded and hashed.

Any other read outside the folder is refused. A module that the entry imports from outside the workspace is refused
too, even when a saved bytecode file (`.pyc`) lets Python skip the source. The audit reads the module list after the
run to find such a module.
"""

from __future__ import annotations

import hashlib
import os
import sys
from collections.abc import Iterable
from pathlib import Path
from types import FrameType, ModuleType

__all__ = ["Reads"]

_ACTIVE: Reads | None = None
_SPECIAL = ("/nix/store/", "/proc/", "/sys/", "/dev/")
_WRITE_MODES = set("wax+")


def _hook(event: str, args: tuple) -> None:
    if _ACTIVE is None:
        return
    if event == "open":
        path, mode, flags = args
        if isinstance(mode, str) and _WRITE_MODES & set(mode):
            return
        if mode is None and isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT):
            return
        _ACTIVE._see("file", path)
    elif event in ("os.listdir", "os.scandir"):
        _ACTIVE._see("dir", args[0] if args else None)
    elif event == "import" and args:
        _ACTIVE._note_import(args[0])


def _from_import_machinery(frame: FrameType | None) -> bool:
    while frame is not None:
        if frame.f_code.co_filename.startswith(("<frozen importlib", "<frozen zipimport")):
            return True
        frame = frame.f_back
    return False


class Reads:
    """The audit of one run. Enter it before the entry runs, and read `result()` and `refusals()` after."""

    def __init__(self, entry: Path, out: Path | None = None, *, inside_libs: Iterable[str | Path] = (".basix/pynix",)):
        """`inside_libs` names the folders inside the workspace that count as library code (relative to the entry)."""
        self.entry = Path(os.path.abspath(entry))
        self.root = self.entry.parent
        self.out = Path(os.path.abspath(out)) if out else None
        self.ignore = sorted(
            {"__pycache__"} | ({self.out.name} if self.out and self.out.parent == self.root else set())
        )
        allowed = {os.path.abspath(self.root / p) for p in inside_libs}
        self.libs = [p for p in (os.path.abspath(p or ".") for p in sys.path) if self._is_lib(p, allowed)]
        self._before: dict[str, ModuleType] = {}
        self._import_at: dict[str, tuple[int, int] | None] = {}
        self._files: set[Path] = set()
        self._dirs: set[Path] = set()
        self._outside: dict[str, tuple[int, int]] = {}
        self._busy = False

    def _is_lib(self, path: str, allowed: set[str]) -> bool:
        """Whether a `sys.path` entry is library code: not the workspace, not above it, and not inside it."""
        p = Path(path)
        if p == self.root or p in self.root.parents:
            return False
        return self.root not in p.parents or path in allowed

    def __enter__(self) -> Reads:
        global _ACTIVE
        self._before = dict(sys.modules)  # a module that the toolchain loaded before the run is not the entry's import
        _ACTIVE = self
        return self

    def __exit__(self, *exc: object) -> None:
        global _ACTIVE
        _ACTIVE = None

    def _see(self, kind: str, raw: object) -> None:
        if not isinstance(raw, str | bytes | os.PathLike) or self._busy:
            return
        path = os.path.abspath(os.fsdecode(raw))
        if path.startswith(_SPECIAL) or (path + "/").startswith(_SPECIAL) or path == str(self.entry):
            return
        if self._exempt(path):
            return
        if kind == "dir" and _from_import_machinery(
            sys._getframe(2)
        ):  # the import system lists folders; a module file stays
            return
        p = Path(path)
        if (
            "__pycache__" in p.parts
            or p.suffix in (".pyc", ".so")
            or (sys.pycache_prefix and path.startswith(sys.pycache_prefix))
        ):
            return
        if p == self.root or self.root in p.parents:
            (self._files if kind == "file" else self._dirs).add(p)
        else:
            line, col = self._where()
            self._outside.setdefault(path, (line, col))

    def _exempt(self, path: str) -> bool:
        """Whether `path` is a special path or library code."""
        if path.startswith(_SPECIAL) or (path + "/").startswith(_SPECIAL):
            return True
        return any(path == p or path.startswith(p.rstrip("/") + "/") for p in self.libs)

    def _where(self) -> tuple[int, int]:
        """Line and column (from 1) of the call in the entry that made the read."""
        return self._locate(sys._getframe(3)) or (1, 1)

    def _locate(self, frame: FrameType | None) -> tuple[int, int] | None:
        """Line and column (from 1) of the call in the entry, found from `frame` outward. None if the entry is absent."""
        while frame is not None:
            if os.path.abspath(frame.f_code.co_filename) == str(self.entry):
                positions = list(frame.f_code.co_positions())
                index = frame.f_lasti // 2
                col = positions[index][2] if index < len(positions) else 0
                return frame.f_lineno, (col or 0) + 1
            frame = frame.f_back
        return None

    def _note_import(self, name: object) -> None:
        """Remember where the entry made the first import of a module. The audit hook calls this."""
        if isinstance(name, str) and name not in self._import_at:
            self._import_at[name] = self._locate(sys._getframe(2))

    def _rel(self, p: Path) -> str:
        return p.relative_to(self.root).as_posix() or "."

    def _imported(self) -> set[Path]:
        """The source files of the workspace modules that the entry imported.

        A saved bytecode file hides the read: Python checks the time of the source and loads the `.pyc`, and the
        audit hook never sees an `open` of the source. So the audit reads the module list after the run.
        """
        found: set[Path] = set()
        for module in list(sys.modules.values()):
            name = getattr(module, "__file__", None)
            if not isinstance(name, str) or not name.endswith(".py"):
                continue
            path = Path(os.path.abspath(name))
            if self.root in path.parents and not self._exempt(str(path)):
                found.add(path)
        return found - {self.entry}

    def _outside_modules(self) -> dict[str, tuple[int, int] | None]:
        """The files of the modules that the entry imported from outside the workspace, with the place of the import.

        The audit hook sees an `open` of the source only. A saved bytecode file hides the import, so this reads the
        module list after the run. It skips a module that was loaded before the run, and a module that the hook
        already refused.
        """
        found: dict[str, tuple[int, int] | None] = {}
        for name, module in list(sys.modules.items()):
            if self._before.get(name) is module:
                continue
            path = _origin(module)
            if path is None or path in self._outside or path in found or self._exempt(path):
                continue
            if Path(path) == self.root or self.root in Path(path).parents:
                continue
            found[path] = self._import_at.get(name)
        return found

    def result(self) -> dict:
        """The record for the JSON: file hashes, absent files, folder listings, and the names that the listings skip."""
        self._files |= self._imported()
        files = {self._rel(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(self._files) if p.is_file()}
        absent = sorted(self._rel(p) for p in self._files if not p.exists())
        dirs = {
            self._rel(p): sorted(n for n in os.listdir(p) if n not in self.ignore)
            for p in sorted(self._dirs)
            if p.is_dir()
        }
        return {"files": files, "absent": absent, "dirs": dirs, "ignore": self.ignore}

    def refusals(self) -> list[str]:
        """One plain line for each read or import outside the workspace."""
        name = self.entry.name
        lines = [
            f"{name}:{line}:{col}: reads {path}, which is outside the workspace. "
            f"Copy the file into the folder of {name} and read the copy."
            for path, (line, col) in self._outside.items()
        ]
        for path, place in self._outside_modules().items():
            where = f"{name}:{place[0]}:{place[1]}" if place else name
            lines.append(
                f"{where}: imports {path}, which is outside the workspace. "
                f"Put the module in the folder of {name}, or bring it in through an Input."
            )
        return lines


def _origin(module: ModuleType) -> str | None:
    """The absolute path of the file of a module. None for a built-in, frozen, or namespace module."""
    try:
        name = getattr(module, "__file__", None)
        if not isinstance(name, str):
            name = getattr(getattr(module, "__spec__", None), "origin", None)
    except Exception:  # a lazy module can raise on any attribute
        return None
    if not isinstance(name, str) or not os.path.isabs(name):
        return None
    return os.path.abspath(name)


sys.addaudithook(_hook)
