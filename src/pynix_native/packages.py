"""Package references for the packages of an input and of a pinned nixpkgs (009-D47, 009-D54).

`InputPkg` is a package of `packages.<system>` of a flake input. `NixpkgsPkg` is a package of a `NixpkgsPin(...)`. Both
subclass `Pkg`, so `Program(...)` takes them. The sets `InputPackages` and `NixpkgsPackages` are the runtime of the
generated name stubs. They check a name against `names.json` and suggest a close name.
"""

from __future__ import annotations

import difflib
import importlib
import json
from functools import lru_cache
from pathlib import Path
from typing import Literal

from pynix_pkgs import PackageError, Pkg, Prog

__all__ = [
    "InputPackages",
    "InputPkg",
    "InputProg",
    "NixpkgsPackages",
    "NixpkgsPkg",
    "NixpkgsProg",
    "apply_command",
    "set_apply_command",
]

_APPLY: list[str] = ["basix apply"]


def set_apply_command(command: str) -> None:
    """Name the command that makes the generated packages. The layer sets it once: `basix apply` or `minix apply`."""
    _APPLY[0] = command


def apply_command() -> str:
    """The command that makes the generated packages."""
    return _APPLY[0]


class InputPkg(Pkg):
    """A package of the `packages.<system>` output of an input. The decoder reads `inputs.INPUT.packages.<system>.ATTR`."""

    kind: Literal["input_package"] = "input_package"
    input: str

    def __init__(self, input: str, attr: str) -> None:
        super(Pkg, self).__init__(input=input, attr=attr)  # ty: ignore[unknown-argument]

    __init__.__pydantic_base_init__ = True  # ty: ignore[unresolved-attribute]


class InputProg(InputPkg, Prog):
    """A package of an input that has a main program."""


class NixpkgsPkg(Pkg):
    """A package of a nixpkgs that the entry pinned by commit. The decoder reads `inputs.nixpkgs-NAME.legacyPackages.<system>.ATTR`."""

    kind: Literal["nixpkgs_package"] = "nixpkgs_package"
    nixpkgs: str

    def __init__(self, nixpkgs: str, attr: str) -> None:
        super(Pkg, self).__init__(nixpkgs=nixpkgs, attr=attr)  # ty: ignore[unknown-argument]

    __init__.__pydantic_base_init__ = True  # ty: ignore[unresolved-attribute]


class NixpkgsProg(NixpkgsPkg, Prog):
    """A package of a pinned nixpkgs that has a main program."""


@lru_cache(maxsize=8)
def _read_names(path: str, stamp: int) -> dict[str, list]:
    """The rows of one `names.json`. `stamp` is the change time of the file, so a new file gives a new read."""
    return json.loads(Path(path).read_text())


def _rows(path: Path) -> dict[str, list]:
    return _read_names(str(path), path.stat().st_mtime_ns)


class _Names:
    """A set of packages. A name check with a suggestion; the rows are `{python_name: [attr, has_main_program]}`."""

    def _rows(self) -> dict[str, list]:
        raise NotImplementedError

    def _unknown(self, name: str, advice: str) -> PackageError:
        raise NotImplementedError

    def _make(self, attr: str, has_main: bool) -> Pkg:
        raise NotImplementedError

    def _lookup(self, name: str) -> Pkg:
        table = self._rows()
        row = table.get(name) or next((r for r in table.values() if r[0] == name), None)
        if row is None:
            close = difflib.get_close_matches(name, table, n=3, cutoff=0.7)
            raise self._unknown(name, f" Did you mean `{close[0]}`?" if close else "")
        return self._make(row[0], bool(row[1]))

    def __getattr__(self, name: str) -> Pkg:
        if name.startswith("__"):  # a name like `_7zip` is a package; a dunder is Python
            raise AttributeError(name)
        return self._lookup(name)

    def __getitem__(self, attr: str) -> Pkg:
        return self._lookup(attr)

    def __dir__(self) -> list[str]:
        return sorted(self._rows())


class InputPackages(_Names):
    """The runtime of a generated `pkgs.py` of an input package. `names.json` sits beside the generated file."""

    def __init__(self, input: str, generated_file: str) -> None:
        self._input = input
        self._file = Path(generated_file)

    def _rows(self) -> dict[str, list]:
        return _rows(self._file.with_name("names.json"))

    def _unknown(self, name: str, advice: str) -> PackageError:
        return PackageError(f"The packages of the input `{self._input}` have no package `{name}`.{advice}", name)

    def _make(self, attr: str, has_main: bool) -> InputPkg:
        return (InputProg if has_main else InputPkg)(self._input, attr)


class NixpkgsPackages(_Names):
    """`NAME.pkgs` of a `NixpkgsPin`. The names come from the generated package `pynix_nixpkgs_NAME` (`names.json`)."""

    def __init__(self, nixpkgs: str) -> None:
        self._nixpkgs = nixpkgs

    def _rows(self) -> dict[str, list]:
        module = f"pynix_nixpkgs_{self._nixpkgs.replace('-', '_')}"
        try:
            found = importlib.import_module(module)
        except ModuleNotFoundError as error:
            if error.name != module:
                raise
            text = f"The package list `{self._nixpkgs}` is not made yet: run `{apply_command()}`."
            raise PackageError(text, self._nixpkgs) from None
        return _rows(Path(str(found.__file__)).with_name("names.json"))

    def _unknown(self, name: str, advice: str) -> PackageError:
        return PackageError(f"The package list `{self._nixpkgs}` has no package `{name}`.{advice}", name)

    def _make(self, attr: str, has_main: bool) -> NixpkgsPkg:
        return (NixpkgsProg if has_main else NixpkgsPkg)(self._nixpkgs, attr)
