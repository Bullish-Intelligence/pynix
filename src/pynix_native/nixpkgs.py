"""`NixpkgsPin(name, commit)`: a nixpkgs pinned by commit, and `OWN` (009-D53, 009-D54)."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import AfterValidator, BaseModel, ConfigDict, ValidationInfo, field_validator
from pydantic_core import PydanticCustomError

from .packages import NixpkgsPackages

__all__ = ["NAMES_GENERATOR", "OWN", "NixpkgsPin", "Own", "nixpkgs_package_name", "registered_nixpkgs", "reset_nixpkgs"]

NAMES_GENERATOR = "nixpkgs-names-1"
"""The version of the name-list generator (`pynix.gen_nixpkgs`). Raise it when a change alters the output."""

RESERVED = {"layer", "own"}
"""Names that a `NixpkgsPin` cannot take: the nixpkgs of the layer and the `OWN` choice."""


def nixpkgs_package_name(name: str) -> str:
    """The Python package of the name list of `NixpkgsPin(name, ...)`."""
    return "pynix_nixpkgs_" + name.replace("-", "_")


def _nixpkgs_name(value: str) -> str:
    if not re.fullmatch(r"[a-z][a-z0-9-]{0,31}", value) or value in RESERVED:
        raise PydanticCustomError(
            "nixpkgs_name", "must be a new name: lower case letters, digits, and '-' ('layer' and 'own' are taken)"
        )
    return value


def _commit(value: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise PydanticCustomError(
            "commit",
            "must be a full commit of nixpkgs: 40 lower case hex digits (a branch name or a short commit does not pin)",
        )
    return value


_REGISTRY: dict[str, str] = {}
"""Every `NixpkgsPin(...)` made in this process, name to commit. The compiler writes it into the JSON."""


class Own(BaseModel):
    """`OWN`: an input keeps the nixpkgs that it locks itself (009-D53)."""

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)

    def __repr__(self) -> str:
        return "OWN"


OWN = Own()


class NixpkgsPin(BaseModel):
    """A nixpkgs pinned by commit: `old = NixpkgsPin("old", "d233902339c02a9c334e7e593de68855ad26c4cb")` (009-D53).

    `Input(..., nixpkgs=old)` makes the input follow it. `old.pkgs.NAME` names a package of it. Only the compiler
    checks `old.pkgs.NAME`; ty does not see it (009-D54).

    The name `Nixpkgs` is the generated class of the options `nixpkgs.*`. It is not this class (010-D55).
    """

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)
    _positional: ClassVar[tuple[str, ...]] = ("name", "commit")
    name: Annotated[str, AfterValidator(_nixpkgs_name)]
    """The name of this nixpkgs: `NAME.pkgs.PACKAGE`."""
    commit: Annotated[str, AfterValidator(_commit)]
    """The full commit (40 hex digits) of the nixpkgs repository."""

    if TYPE_CHECKING:

        def __init__(self, name: str, commit: str, /) -> None:
            """A nixpkgs pinned by commit.

            Args:
                name: The name of this nixpkgs: `NAME.pkgs.PACKAGE`.
                commit: The full commit (40 hex digits) of the nixpkgs repository.
            """
            ...

        @property
        def pkgs(self) -> NixpkgsPackages: ...

    else:

        def __init__(self, name: str, commit: str) -> None:
            super().__init__(name=name, commit=commit)

        __init__.__pydantic_base_init__ = True

        @property
        def pkgs(self) -> NixpkgsPackages:
            return NixpkgsPackages(self.name)

    @field_validator("commit")
    @classmethod
    def _register(cls, value: str, info: ValidationInfo) -> str:
        name = info.data.get("name")
        if name is not None and _REGISTRY.setdefault(name, value) != value:
            raise PydanticCustomError(
                "nixpkgs_twice", "the nixpkgs `{name}` is already set to another commit", {"name": name}
            )
        return value

    def to_json(self) -> dict[str, str]:
        return {"name": self.name, "commit": self.commit}


def registered_nixpkgs() -> list[dict[str, str]]:
    """The `NixpkgsPin(...)` objects of this process, sorted by name (for the compiled JSON)."""
    return [{"name": n, "commit": c} for n, c in sorted(_REGISTRY.items())]


def reset_nixpkgs() -> None:
    """Forget every `NixpkgsPin(...)` of this process. A test or a second compile in one process calls it."""
    _REGISTRY.clear()
