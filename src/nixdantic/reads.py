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
store path names the content. A read of the library code (an entry of `sys.path` outside the workspace) is not
recorded. Any other read outside the folder is refused.
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path
from types import FrameType

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


def _from_import_machinery(frame: FrameType | None) -> bool:
    while frame is not None:
        if frame.f_code.co_filename.startswith(("<frozen importlib", "<frozen zipimport")):
            return True
        frame = frame.f_back
    return False


class Reads:
    """The audit of one run. Enter it before the entry runs, and read `result()` and `refusals()` after."""

    def __init__(self, entry: Path, out: Path | None = None):
        self.entry = Path(os.path.abspath(entry))
        self.root = self.entry.parent
        self.out = Path(os.path.abspath(out)) if out else None
        self.ignore = sorted(
            {"__pycache__"} | ({self.out.name} if self.out and self.out.parent == self.root else set())
        )
        self.libs = [os.path.abspath(p or ".") for p in sys.path]
        self.libs = [p for p in self.libs if Path(p) != self.root]
        self._files: set[Path] = set()
        self._dirs: set[Path] = set()
        self._outside: dict[str, tuple[int, int]] = {}
        self._busy = False

    def __enter__(self) -> Reads:
        global _ACTIVE
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
        if any(path == p or path.startswith(p.rstrip("/") + "/") for p in self.libs):
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

    def _where(self) -> tuple[int, int]:
        """Line and column (from 1) of the call in the entry that made the read."""
        frame: FrameType | None = sys._getframe(3)
        while frame is not None:
            if os.path.abspath(frame.f_code.co_filename) == str(self.entry):
                positions = list(frame.f_code.co_positions())
                index = frame.f_lasti // 2
                col = positions[index][2] if index < len(positions) else 0
                return frame.f_lineno, (col or 0) + 1
            frame = frame.f_back
        return 1, 1

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
            if self.root in path.parents and not any(str(path).startswith(p.rstrip("/") + "/") for p in self.libs):
                found.add(path)
        return found - {self.entry}

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
        """One plain line for each read outside the workspace."""
        return [
            f"{self.entry.name}:{line}:{col}: reads {path}, which is outside the workspace. "
            f"Copy the file into the folder of {self.entry.name} and read the copy."
            for path, (line, col) in self._outside.items()
        ]


sys.addaudithook(_hook)
