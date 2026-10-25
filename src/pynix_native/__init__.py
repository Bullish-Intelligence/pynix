"""Native parts of an entry: native modules, flake inputs, nixpkgs pins, and input packages (009-D40, 009-D47 to 009-D54).

- `NativeModule`: a native Nix module file of the workspace.
- `Input`, `NixpkgsPin`, `OWN`: the flake inputs of the entry and the nixpkgs of each (the compiler reads them from the
  syntax tree: `pynix_native.discover`).
- `InputPkg`, `InputProg`, `InputPackages`: the packages of an input (the runtime of a generated name stub).
- `NixpkgsPkg`, `NixpkgsProg`, `NixpkgsPackages`: the packages of a `NixpkgsPin`, `old.pkgs.NAME`.
- `pynix_native.pair`: the pair check of a generated package against `flake.lock`.
"""

from .discover import DiscoveryError, Found, FoundInput, FoundNixpkgsPin, discover, discover_source
from .inputs import Input, input_json, input_package_name, module_attr, set_module_attr
from .lock import (
    InputLock,
    LockError,
    NixpkgsLock,
    follow,
    input_cache_key,
    input_lock,
    names_cache_key,
    nixpkgs_lock,
    read_lock,
)
from .module import NativeModule
from .nixpkgs import (
    NAMES_GENERATOR,
    OWN,
    NixpkgsPin,
    Own,
    nixpkgs_package_name,
    registered_nixpkgs,
    reset_nixpkgs,
)
from .packages import (
    InputPackages,
    InputPkg,
    InputProg,
    NixpkgsPackages,
    NixpkgsPkg,
    NixpkgsProg,
    apply_command,
    set_apply_command,
)
from .pair import Pair, check_input, check_nixpkgs, check_pairs, error_lines, read_source, to_regenerate

__all__ = [
    "NAMES_GENERATOR",
    "OWN",
    "DiscoveryError",
    "Found",
    "FoundInput",
    "FoundNixpkgsPin",
    "Input",
    "InputLock",
    "InputPackages",
    "InputPkg",
    "InputProg",
    "LockError",
    "NativeModule",
    "NixpkgsPin",
    "NixpkgsLock",
    "NixpkgsPackages",
    "NixpkgsPkg",
    "NixpkgsProg",
    "Own",
    "Pair",
    "apply_command",
    "check_input",
    "check_nixpkgs",
    "check_pairs",
    "discover",
    "discover_source",
    "error_lines",
    "follow",
    "input_cache_key",
    "input_json",
    "input_lock",
    "input_package_name",
    "module_attr",
    "names_cache_key",
    "nixpkgs_lock",
    "nixpkgs_package_name",
    "read_lock",
    "read_source",
    "registered_nixpkgs",
    "reset_nixpkgs",
    "set_apply_command",
    "set_module_attr",
    "to_regenerate",
]
