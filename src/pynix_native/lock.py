"""Read the nodes of a `flake.lock`: the input of an `Input(...)` and the pin of a `NixpkgsPin(...)` (009-D48)."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

__all__ = [
    "InputLock",
    "LockError",
    "NixpkgsLock",
    "follow",
    "input_cache_key",
    "input_lock",
    "names_cache_key",
    "nixpkgs_lock",
    "read_lock",
]

Lock = Mapping[str, Any]


class LockError(Exception):
    """`flake.lock` has no node for a name. The text is one plain line."""


@dataclass(frozen=True)
class InputLock:
    """What `flake.lock` holds for one `Input`: its source, and the nixpkgs that it uses."""

    narHash: str
    rev: str | None
    nixpkgs_commit: str | None
    nixpkgs_narHash: str


@dataclass(frozen=True)
class NixpkgsLock:
    """What `flake.lock` holds for one `NixpkgsPin`: the input `nixpkgs-NAME`."""

    commit: str
    narHash: str
    last_modified: int | None


def read_lock(path: Path) -> dict[str, Any]:
    """The JSON of a `flake.lock`."""
    return json.loads(path.read_text())


def follow(lock: Lock, ref: str | list[str]) -> str:
    """The node name that an `inputs` entry reaches. A list is a `follows` path from the root."""
    nodes = lock["nodes"]
    if isinstance(ref, str):
        return ref
    node = lock["root"]
    for key in ref:
        try:
            node = follow(lock, nodes[node]["inputs"][key])
        except KeyError:
            raise LockError(f"flake.lock has no input `{'/'.join(ref)}`") from None
    return node


def _root_input(lock: Lock, name: str) -> str:
    refs = lock["nodes"][lock["root"]].get("inputs", {})
    if name not in refs:
        raise LockError(f"flake.lock holds no input `{name}`")
    return follow(lock, refs[name])


def input_lock(lock: Lock, name: str) -> InputLock:
    """The locked source of the input `name`, and the nixpkgs that it follows or locks itself."""
    nodes = lock["nodes"]
    node = nodes[_root_input(lock, name)]
    locked = node["locked"]
    own = node.get("inputs", {})
    pkgs = nodes[follow(lock, own["nixpkgs"]) if "nixpkgs" in own else _root_input(lock, "nixpkgs")]["locked"]
    return InputLock(locked["narHash"], locked.get("rev"), pkgs.get("rev"), pkgs["narHash"])


def nixpkgs_lock(lock: Lock, name: str) -> NixpkgsLock:
    """The locked pin of `NixpkgsPin(name, ...)`: the input `nixpkgs-NAME`."""
    locked = lock["nodes"][_root_input(lock, f"nixpkgs-{name}")]["locked"]
    return NixpkgsLock(locked["rev"], locked["narHash"], locked.get("lastModified"))


def _key(*parts: str) -> str:
    return hashlib.sha256("|".join(parts).encode()).hexdigest()[:12]


def names_cache_key(node: Mapping[str, Any], generator: str) -> str:
    """The cache key of a name list: the narHash of the lock node of `nixpkgs-NAME`, and the generator version.

    `node` is the lock node (`lock["nodes"][NODE]`) or its `locked` part. The command keeps the list in
    `.basix/cache/pynix/nixpkgs-NAME-KEY/`, makes it when that folder is missing, and links
    `.basix/pynix/pynix_nixpkgs_NAME` to it. The same commit under another name reuses the same narHash.
    """
    locked = node.get("locked", node)
    return _key(locked["narHash"], generator)


def input_cache_key(lock: Lock, name: str, generator: str) -> str:
    """The cache key of an input package: the narHash of the input, the narHash of its nixpkgs, and the generator version."""
    info = input_lock(lock, name)
    return _key(info.narHash, info.nixpkgs_narHash, generator)
