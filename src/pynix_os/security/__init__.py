"""Lazy package: each name loads on first use."""

from importlib import import_module
from types import ModuleType

__all__ = [
    "__options__",
    "account_utils",
    "acme",
    "agnos",
    "apparmor",
    "audit",
    "auditd",
    "chromiumSuidSandbox",
    "doas",
    "duosec",
    "googleOsLogin",
    "ipa",
    "isolate",
    "krb5",
    "loginDefs",
    "pam",
    "pki",
    "please",
    "polkit",
    "rtkit",
    "run0",
    "shadow",
    "soteria",
    "sudo",
    "sudo_rs",
    "tpm2",
    "virtualisation",
]


def __getattr__(name: str) -> ModuleType:
    if name not in __all__:
        raise AttributeError(name)
    return import_module(f"{__name__}.{name}")
