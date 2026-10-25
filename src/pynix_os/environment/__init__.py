"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "__options__",
    "budgie",
    "cinnamon",
    "cosmic",
    "enlightenment",
    "gnome",
    "lxqt",
    "mate",
    "memoryAllocator",
    "pantheon",
    "plasma6",
    "shell",
    "stub_ld",
    "wordlist",
    "wvdial",
    "xfce",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
