"""`Input(...)`: one extra flake input (009-D49, 009-D52, 009-D53)."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import AfterValidator, BaseModel, ConfigDict
from pydantic_core import PydanticCustomError

from .nixpkgs import NixpkgsPin, Own

__all__ = ["Input", "input_json", "input_package_name", "module_attr", "set_module_attr"]

_MODULE_ATTR: list[str] = ["nixosModules"]


def set_module_attr(word: str) -> None:
    """Name the flake output that holds the modules of an input. The layer sets it once: `nixosModules` or `homeManagerModules`."""
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", word):
        raise ValueError(f"The module output must be a plain name such as `nixosModules`, found {word!r}.")
    _MODULE_ATTR[0] = word


def module_attr() -> str:
    """The flake output that holds the modules of an input (default `nixosModules`)."""
    return _MODULE_ATTR[0]


def input_package_name(name: str) -> str:
    """The Python package of the input package of `Input(name, ...)`: `pynix_NAME`."""
    return "pynix_" + name.replace("-", "_")


def _input_name(value: str) -> str:
    if (
        value in {"self", "basix", "minix", "nixpkgs", "ext"}
        or value.startswith("nixpkgs-")
        or not re.fullmatch(r"[a-z][a-z0-9-]{0,31}", value)
    ):
        raise PydanticCustomError(
            "input_name",
            "must be a new name: lower case letters, digits, and '-' ('basix', 'minix', 'nixpkgs', and 'self' are taken)",
        )
    return value


def _module_name(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", value):
        raise PydanticCustomError(
            "module_name",
            'must be the name of a module in `{output}` of the input, for example "default"',
            {"output": module_attr()},
        )
    return value


def _input_url(value: str) -> str:
    # The URL goes into Nix text (a generated flake). Allow only the characters of a flake reference.
    if not re.fullmatch(r"[A-Za-z0-9+._:/?&=@%~#,-]+", value) or ":" not in value:
        raise PydanticCustomError(
            "input_url", "must be a flake reference such as github:OWNER/REPO or git+file:///path (no spaces or quotes)"
        )
    return value


class Input(BaseModel):
    """One extra flake input: `Input("nirinit", "github:amaanq/nirinit")`. A native module reads it as `inputs.nirinit`.

    The compiler reads `Input(...)` calls from the syntax tree before it runs the entry. Use literal arguments only.
    """

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)
    _positional: ClassVar[tuple[str, ...]] = ("name", "url")
    name: Annotated[str, AfterValidator(_input_name)]
    """The name that a native module uses: `inputs.NAME`."""
    url: Annotated[str, AfterValidator(_input_url)]
    """The flake reference, for example "github:amaanq/nirinit" or "git+https://example.org/repo?ref=v1"."""
    nixpkgs: NixpkgsPin | Own | None = None
    """The nixpkgs of the input (009-D53). Left out: the nixpkgs of the layer. `OWN`: the nixpkgs that the input locks itself. A `NixpkgsPin(...)`: that commit."""
    flake: bool = True
    """False for a source that is not a flake: `inputs.NAME` is then the source folder."""
    modules: list[Annotated[str, AfterValidator(_module_name)]] = []
    """The modules of the input to import (`inputs.NAME.nixosModules.MODULE`; `homeManagerModules` on Home Manager), for example ["nirinit"]. Typed classes of `pynix_NAME` need the module."""

    if TYPE_CHECKING:

        def __init__(
            self,
            name: str,
            url: str,
            /,
            *,
            modules: list[str] = [],  # noqa: B006
            flake: bool = True,
            nixpkgs: NixpkgsPin | Own | None = None,
        ) -> None:
            """One extra flake input.

            Args:
                name: The name that a native module uses: `inputs.NAME`.
                url: The flake reference, for example "github:amaanq/nirinit".
                modules: The modules of the input to import, for example ["nirinit"].
                flake: False for a source that is not a flake.
                nixpkgs: The nixpkgs of the input: left out, the nixpkgs of the layer; `OWN`, its own lock; or a `NixpkgsPin(...)`.
            """
            ...

    else:

        def __init__(self, name: str, url: str, **kw) -> None:
            super().__init__(name=name, url=url, **kw)

        __init__.__pydantic_base_init__ = True


def input_json(item: Input, where: str) -> dict[str, object]:
    """The compiled JSON of one `Input`. The key `nixpkgs` is absent when it is left out."""
    out: dict[str, object] = item.model_dump()
    chosen = item.nixpkgs
    if chosen is None:
        del out["nixpkgs"]
    else:
        out["nixpkgs"] = "own" if isinstance(chosen, Own) else chosen.to_json()
    return {**out, "source": where}
