"""The pair check (009-D48): a generated package must come from the same locked source that Nix evaluates.

An input package `pynix_NAME` records the narHash and revision of the input, the commit of the nixpkgs that the input
uses, and the generator version, in `SOURCE` of its `_generation.py`. A name list `pynix_nixpkgs_NAME` records the
commit and narHash of the nixpkgs, and the generator version. This module compares the record with the nodes of
`flake.lock`, and follows `follows` the way Nix does.

- A different source gives one plain line that names the package and the command that makes it again.
- A different generator version is no error. The status is `regenerate`: apply makes the package again in place
  (decision 010-D5).

The reader parses `_generation.py` and never imports it, so a stale `.pyc` file cannot hide a change.
"""

from __future__ import annotations

import ast
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

from .discover import Found, FoundInput, FoundNixpkgsPin
from .inputs import input_package_name
from .lock import LockError, input_lock, nixpkgs_lock
from .nixpkgs import NAMES_GENERATOR, nixpkgs_package_name

__all__ = ["Pair", "check_input", "check_nixpkgs", "check_pairs", "error_lines", "read_source", "to_regenerate"]

Status = Literal["ok", "regenerate", "stale", "missing", "unlocked"]


@dataclass(frozen=True)
class Pair:
    """The result for one package. `line` is the plain text for the learner; it is None for `ok` and `regenerate`."""

    kind: Literal["input", "nixpkgs"]
    name: str
    status: Status
    line: str | None = None

    @property
    def is_error(self) -> bool:
        """True when the compiler must stop: the package was made from another source, or it is missing."""
        return self.status in {"stale", "missing", "unlocked"}

    @property
    def needs_regeneration(self) -> bool:
        """True when apply must make the package again, with or without an error line."""
        return self.status != "ok"


def read_source(generation_file: Path) -> dict[str, str] | None:
    """The `SOURCE` record of a generated package, or None when the file or the record is missing."""
    try:
        tree = ast.parse(generation_file.read_text())
    except (OSError, SyntaxError):
        return None
    for node in tree.body:
        targets = (
            node.targets if isinstance(node, ast.Assign) else [node.target] if isinstance(node, ast.AnnAssign) else []
        )
        if any(isinstance(t, ast.Name) and t.id == "SOURCE" for t in targets) and node.value is not None:  # ty: ignore[unresolved-attribute]
            try:
                value = ast.literal_eval(node.value)  # ty: ignore[unresolved-attribute]
            except ValueError:
                return None
            return value if isinstance(value, dict) else None
    return None


def _short(commit: object) -> str:
    return str(commit)[:12] if commit else "unknown"


def check_input(
    item: FoundInput,
    lock: Mapping[str, Any],
    packages_dir: Path,
    command: str,
    generator: str | None = None,
) -> Pair:
    """Compare the input package of `item` with `flake.lock`.

    `packages_dir` holds `pynix_NAME` (the folder `.basix/pynix`). `command` is `basix apply` or `minix apply`.
    `generator` is the version of the input-package generator that apply uses now; None skips that comparison.
    """
    package = input_package_name(item.name)
    try:
        want = input_lock(lock, item.name)
    except LockError:
        text = f"{item.source}: flake.lock holds no input `{item.name}` yet; run `{command}` to lock it"
        return Pair("input", item.name, "unlocked", text)
    have = read_source(packages_dir / package / "_generation.py")
    if not have or not have.get("narHash"):
        return Pair(
            "input",
            item.name,
            "missing",
            f"{item.source}: the package `{package}` is not made yet; run `{command}` to make it",
        )
    again = f"run `{command}` to make it again"
    if have["narHash"] != want.narHash or (have.get("rev") and want.rev and have["rev"] != want.rev):
        text = f"{item.source}: the package `{package}` was made from another version of `{item.name}` than flake.lock holds; {again}"
        return Pair("input", item.name, "stale", text)
    if have.get("nixpkgs") != want.nixpkgs_commit:
        text = (
            f"{item.source}: the package `{package}` was made with another nixpkgs ({_short(have.get('nixpkgs'))}) "
            f"than flake.lock gives `{item.name}` now ({_short(want.nixpkgs_commit)}); {again}"
        )
        return Pair("input", item.name, "stale", text)
    if generator is not None and have.get("generator") != generator:
        return Pair("input", item.name, "regenerate")
    return Pair("input", item.name, "ok")


def check_nixpkgs(
    pin: FoundNixpkgsPin,
    lock: Mapping[str, Any],
    packages_dir: Path,
    command: str,
    generator: str = NAMES_GENERATOR,
) -> Pair:
    """Compare the name list of `pin` with `flake.lock`. The list is `pynix_nixpkgs_NAME` in `packages_dir`."""
    package = nixpkgs_package_name(pin.name)
    try:
        want = nixpkgs_lock(lock, pin.name)
    except LockError:
        text = f"{pin.source}: flake.lock holds no nixpkgs `{pin.name}` yet; run `{command}` to lock it"
        return Pair("nixpkgs", pin.name, "unlocked", text)
    have = read_source(packages_dir / package / "_generation.py")
    if not have or not have.get("commit"):
        text = f"{pin.source}: the package list `{pin.name}` is not made yet; run `{command}` to make it"
        return Pair("nixpkgs", pin.name, "missing", text)
    if have["commit"] != want.commit or have.get("narHash") not in {None, want.narHash}:
        text = (
            f"{pin.source}: the package list `{pin.name}` was made from another commit than flake.lock holds "
            f"({_short(have['commit'])} against {_short(want.commit)}); run `{command}` to make it again"
        )
        return Pair("nixpkgs", pin.name, "stale", text)
    if have.get("generator") != generator:
        return Pair("nixpkgs", pin.name, "regenerate")
    return Pair("nixpkgs", pin.name, "ok")


def check_pairs(
    found: Found,
    lock: Mapping[str, Any],
    packages_dir: Path,
    command: str,
    generator: str | None = None,
) -> list[Pair]:
    """Check every `NixpkgsPin` name list, then every input package of an entry. An input with `flake=False` has no package."""
    pairs = [check_nixpkgs(pin, lock, packages_dir, command) for pin in found.nixpkgs]
    pairs += [check_input(item, lock, packages_dir, command, generator) for item in found.inputs if item.flake]
    return pairs


def error_lines(pairs: list[Pair]) -> list[str]:
    """The plain lines of the pairs that stop the compiler."""
    return [p.line for p in pairs if p.is_error and p.line]


def to_regenerate(pairs: list[Pair]) -> list[Pair]:
    """The pairs whose package apply must make again: a stale, missing, or older-generator package."""
    return [p for p in pairs if p.needs_regeneration and p.status != "unlocked"]
