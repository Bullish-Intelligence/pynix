"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "__options__",
    "appvm",
    "containerd",
    "containers",
    "cri_o",
    "docker",
    "hypervGuest",
    "incus",
    "kvmgt",
    "libvirtd",
    "lxc",
    "oci_containers",
    "podman",
    "qemu",
    "rosetta",
    "spiceUSBRedirection",
    "virtualbox",
    "vmware",
    "vswitch",
    "waydroid",
    "xen",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
