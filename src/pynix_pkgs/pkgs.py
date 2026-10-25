"""The packages of the package list, `pkgs.NAME`. The types are in `pkgs.pyi`; the names are in `names.json`."""

from ._pkgref import Pkg, PkgSet, lookup

__all__ = ["pkgs"]


class Pkgs:
    def __getattr__(self, name: str) -> Pkg | PkgSet:
        if name.startswith("__"):
            raise AttributeError(name)
        return lookup(name)

    def __getitem__(self, attr: str) -> Pkg | PkgSet:
        return lookup(attr)

    def __dir__(self) -> list[str]:
        from ._pkgref import names

        return sorted(names())


pkgs = Pkgs()
