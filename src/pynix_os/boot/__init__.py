"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "__options__",
    "bcache",
    "bcachefs",
    "binfmt",
    "bootspec",
    "crashDump",
    "initrd",
    "iscsi_initiator",
    "kernel",
    "kexec",
    "loader",
    "modprobeConfig",
    "plymouth",
    "swraid",
    "tmp",
    "uki",
    "uvesafb",
    "zfs",
    "zswap",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
