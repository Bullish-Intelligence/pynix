"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "__options__",
    "dhcpcd",
    "firewall",
    "getaddrinfo",
    "ifstate",
    "iproute2",
    "jool",
    "modemmanager",
    "nat",
    "netplan",
    "networkmanager",
    "nftables",
    "openconnect",
    "proxy",
    "resolvconf",
    "rxe",
    "stevenblack",
    "tcpcrypt",
    "ucarp",
    "wg_quick",
    "wireguard",
    "wireless",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
