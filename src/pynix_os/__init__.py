"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "appstream",
    "boot",
    "console",
    "documentation",
    "ec2",
    "environment",
    "fonts",
    "gtk",
    "hardware",
    "i18n",
    "ids",
    "image",
    "lix",
    "location",
    "meta",
    "networking",
    "nix",
    "nixops",
    "nixpkgs",
    "oci",
    "openstack",
    "power",
    "powerManagement",
    "programs",
    "qt",
    "security",
    "services",
    "system",
    "systemd",
    "time",
    "top",
    "users",
    "virtualisation",
    "xdg",
    "zramSwap",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
