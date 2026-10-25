"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "accounts",
    "dbus",
    "dconf",
    "editorconfig",
    "fonts",
    "gtk",
    "home",
    "i18n",
    "launchd",
    "manual",
    "meta",
    "mozilla",
    "news",
    "nix",
    "nixpkgs",
    "pam",
    "programs",
    "qt",
    "services",
    "sshAuthSock",
    "submoduleSupport",
    "systemd",
    "targets",
    "top",
    "vdirsyncer",
    "wayland",
    "xdg",
    "xfconf",
    "xresources",
    "xsession",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
