"""Every class of pynix_flake_parts in one flat namespace. Generated; do not edit.

`from pynix_flake_parts import all as nixos`, then `nixos.Loader(efi=nixos.Loader_Efi(...))`. Python loads the module of a name at its first use.
"""

from importlib import import_module as _import_module
from typing import TYPE_CHECKING as _TYPE_CHECKING, Any as _Any

if _TYPE_CHECKING:  # the type checker reads these lines; Python skips them
    from pynix_flake_parts.top import (
        Top as Top,
        Top_Flake as Top_Flake,
        Top_Flake_Apps_Value_Value as Top_Flake_Apps_Value_Value,
        Top_Flake_NixosModules_Value as Top_Flake_NixosModules_Value,
        Top_PerSystem as Top_PerSystem,
        Top_Transposition_Value as Top_Transposition_Value,
    )
else:
    _INDEX = {
        "Top": "pynix_flake_parts.top:Top",
        "Top_Flake": "pynix_flake_parts.top:Top_Flake",
        "Top_Flake_Apps_Value_Value": "pynix_flake_parts.top:Top_Flake_Apps_Value_Value",
        "Top_Flake_NixosModules_Value": "pynix_flake_parts.top:Top_Flake_NixosModules_Value",
        "Top_PerSystem": "pynix_flake_parts.top:Top_PerSystem",
        "Top_Transposition_Value": "pynix_flake_parts.top:Top_Transposition_Value",
    }

    def __getattr__(name: str) -> _Any:
        try:
            target = _INDEX[name]
        except KeyError:
            close = [n for n, t in _INDEX.items() if t.endswith(":" + name) and n != name]
            hint = f" Two classes have this name. Write one of: {', '.join(close)}." if close else ""
            raise AttributeError(f"The flat list of {__name__.split('.')[0]} has no class {name}.{hint}") from None
        module, _, real = target.partition(":")
        value = getattr(_import_module(module), real)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(_INDEX)
