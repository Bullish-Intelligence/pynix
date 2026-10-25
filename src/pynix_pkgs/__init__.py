"""The packages of one package list, `pkgs.NAME` (proposed `pynix` module, shared by both layers).

The types are in `pkgs.pyi` and `sets/*.pyi`; the names are in `names.json`, `sets.json`, and `sets/*.json`. All come
from one generator (SV4, SG36).
"""

from ._pkgref import PackageError, Pkg, PkgSet, Prog, PyEnv, PyInterp, UnknownPackage
from .pkgs import pkgs

__all__ = ["PackageError", "Pkg", "PkgSet", "Prog", "PyEnv", "PyInterp", "UnknownPackage", "pkgs"]
