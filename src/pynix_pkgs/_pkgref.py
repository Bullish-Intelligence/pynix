"""Typed references to packages of the package list (SV4 + SG36, proposed). `Pkg` is a package. `Prog` is a package with a main program.

SG36 adds: package sets (`pkgs.nerd_fonts.fira_code`), a name check for a dotted `Pkg("a.b")`, and `PyEnv`
(`pkgs.python3.with_packages(pkgs.python3Packages.requests)`).
"""

from __future__ import annotations

import difflib
import json
from functools import cache
from pathlib import Path
from typing import Literal

from nixdantic import Package

__all__ = ["Exe", "Pkg", "PkgSet", "Prog", "PyEnv", "PyInterp", "PackageError", "UnknownPackage", "names"]

_HERE = Path(__file__).parent


class Exe(Package):
    """The main program of a package: Nix resolves it with `lib.getExe`."""

    kind: Literal["exe"] = "exe"  # type: ignore[assignment]


class PackageError(AttributeError):
    """A wrong use of `pkgs`. `word` is the name in the learner line that the error is about."""

    def __init__(self, message: str, word: str):
        self.word = word
        super().__init__(message)


class UnknownPackage(PackageError):
    """`pkgs` has no package of this name."""

    def __init__(self, name: str, close: list[str], where: str = "", word: str = ""):
        advice = f" Did you mean `{close[0]}`?" if close else ""
        place = f" in `{where}`" if where else ""
        super().__init__(f"The package list has no package `{name}`{place}.{advice}", word or name)


@cache
def names() -> dict[str, list]:
    """`{python_name: [nixpkgs_attr, has_main_program]}` of the top level (the release file `names.json`)."""
    return json.loads((_HERE / "names.json").read_text())


@cache
def sets() -> dict[str, list]:
    """`{python_name: [set_attr, member_count]}` of the package sets (the release file `sets.json`)."""
    return json.loads((_HERE / "sets.json").read_text())


@cache
def set_names(set_attr: str) -> dict[str, list]:
    """The members of one package set, loaded only when used (`sets/SET.json`)."""
    return json.loads((_HERE / "sets" / f"{set_attr}.json").read_text())


def _find(table: dict[str, list], name: str) -> list | None:
    row = table.get(name)
    if row is None:
        row = next((r for r in table.values() if r[0] == name), None)
    return row


def check_dotted(attr: str) -> None:
    """Raise `UnknownPackage` when `attr` (`a.b`) does not name a package. Depth two only."""
    head, _, rest = attr.partition(".")
    row = _find(sets(), head)
    if row is None:
        close = difflib.get_close_matches(head, [r[0] for r in sets().values()], n=3, cutoff=0.7)
        raise UnknownPackage(head, close, word=attr)
    table = set_names(row[0])
    if _find(table, rest) is None:
        close = difflib.get_close_matches(rest, [r[0] for r in table.values()], n=3, cutoff=0.7)
        raise UnknownPackage(rest, close, row[0], word=attr)


class Pkg(Package):
    """A package of the package list. Write `pkgs.NAME`, for example `pkgs.ripgrep`."""

    def __init__(self, attr: str) -> None:
        if "." in attr:
            check_dotted(attr)
        super().__init__(attr=attr)

    __init__.__pydantic_base_init__ = True  # ty: ignore[unresolved-attribute]


class Prog(Pkg):
    """A package that has a main program (`meta.mainProgram`). It can run."""


class PyInterp(Prog):
    """A Python interpreter. `with_packages` adds libraries of its package set (SG36)."""

    def with_packages(self, *libs: Pkg) -> PyEnv:
        return make_env(self.attr, libs)


class PyEnv(Pkg):
    """A Python with libraries: `python3.withPackages (ps: [ ps.requests ])`."""

    kind: Literal["with_packages"] = "with_packages"  # type: ignore[assignment]
    packages: list[str]

    def __init__(self, attr: str, packages: list[str]) -> None:
        Package.__init__(self, attr=attr, packages=packages)  # ty: ignore[unknown-argument]

    __init__.__pydantic_base_init__ = True  # ty: ignore[unresolved-attribute]


def make_env(interpreter: str, libs: tuple[Pkg, ...]) -> PyEnv:
    """The libraries must come from the package set of the interpreter: `python3` takes `python3Packages.NAME`."""
    want = interpreter + "Packages"
    members = []
    for lib in libs:
        head, _, rest = lib.attr.partition(".")
        if head != want or not rest:
            raise PackageError(
                f"`{interpreter}.with_packages` takes libraries of `{want}`, found `{lib.attr}`.", lib.attr
            )
        members.append(rest)
    return PyEnv(interpreter, members)


class PkgSet:
    """A set of packages, for example `pkgs.nerd_fonts` (nixpkgs `nerd-fonts`)."""

    def __init__(self, attr: str):
        self._attr = attr

    def __getattr__(self, name: str) -> Pkg:
        if name.startswith("__"):
            raise AttributeError(name)
        return self[name]

    def __getitem__(self, name: str) -> Pkg:
        table = set_names(self._attr)
        row = _find(table, name)
        if row is None:
            raise UnknownPackage(name, difflib.get_close_matches(name, table, n=3, cutoff=0.7), self._attr)
        return (Prog if row[1] else Pkg)(f"{self._attr}.{row[0]}")

    def __dir__(self) -> list[str]:
        return sorted(set_names(self._attr))

    def __repr__(self) -> str:
        return f"<the package set `{self._attr}`>"


def lookup(name: str) -> Pkg | PkgSet:
    """A package by Python name or by nixpkgs attribute; a set gives a `PkgSet`. `UnknownPackage` with a suggestion when there is none."""
    table = names()
    row = _find(table, name)
    if row is None:
        set_row = _find(sets(), name)
        if set_row is not None:
            return PkgSet(set_row[0])
        close = difflib.get_close_matches(name, [*table, *sets()], n=3, cutoff=0.7)
        raise UnknownPackage(name, close)
    return (PyInterp if len(row) > 2 and row[2] else Prog if row[1] else Pkg)(row[0])
