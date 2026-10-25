"""Find the `Input(...)` and `NixpkgsPin(...)` calls of an entry file, from its syntax tree (009-D49, 009-D53).

The reader runs nothing. A missing `pynix_NAME` import cannot stop it, so one apply can write the stub, lock the
inputs, and generate the packages before the entry runs. Only literal arguments count. An argument that is computed
stops the reader with one line that names the file, the line, and the column.

`old = NixpkgsPin("old", "COMMIT")` followed by `nixpkgs=old`, `nixpkgs=OWN`, and `nixpkgs=NixpkgsPin(...)` inline are read.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pydantic_core import PydanticCustomError

from .inputs import _input_name, _input_url, _module_name
from .nixpkgs import _commit, _nixpkgs_name

__all__ = ["DiscoveryError", "Found", "FoundInput", "FoundNixpkgsPin", "discover", "discover_source"]


class DiscoveryError(Exception):
    """The entry has an `Input(...)` or `NixpkgsPin(...)` that the reader cannot use. The text is one plain line."""


@dataclass(frozen=True)
class FoundNixpkgsPin:
    """A `NixpkgsPin(name, commit)` call."""

    name: str
    commit: str
    label: str
    line: int

    @property
    def source(self) -> str:
        return f"{self.label}:{self.line}"

    def to_json(self) -> dict[str, Any]:
        return {"name": self.name, "commit": self.commit, "source": self.source}


@dataclass(frozen=True)
class FoundInput:
    """An `Input(...)` call. `nixpkgs` is None (the layer), "own", or the `NixpkgsPin` that the call names."""

    name: str
    url: str
    flake: bool
    modules: tuple[str, ...]
    nixpkgs: FoundNixpkgsPin | str | None
    label: str
    line: int

    @property
    def source(self) -> str:
        return f"{self.label}:{self.line}"

    def to_json(self) -> dict[str, Any]:
        """The keys of `pynix_native.input_json`. The key `nixpkgs` is absent when the call leaves it out."""
        out: dict[str, Any] = {"name": self.name, "url": self.url, "flake": self.flake, "modules": list(self.modules)}
        if isinstance(self.nixpkgs, FoundNixpkgsPin):
            out["nixpkgs"] = {"name": self.nixpkgs.name, "commit": self.nixpkgs.commit}
        elif self.nixpkgs is not None:
            out["nixpkgs"] = self.nixpkgs
        return {**out, "source": self.source}


@dataclass(frozen=True)
class Found:
    """Every `Input(...)` (in source order) and every `NixpkgsPin(...)` (sorted by name) of one entry."""

    inputs: tuple[FoundInput, ...]
    nixpkgs: tuple[FoundNixpkgsPin, ...]

    def to_json(self) -> dict[str, Any]:
        """The `inputs` and `nixpkgs` keys of the compiled JSON, each present only when it has items."""
        out: dict[str, Any] = {"inputs": [i.to_json() for i in self.inputs]}
        if self.nixpkgs:
            out["nixpkgs"] = [n.to_json() for n in self.nixpkgs]
        return out


def _callee(node: ast.Call) -> str | None:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    return func.attr if isinstance(func, ast.Attribute) else None


def _is_own(node: ast.expr) -> bool:
    return (isinstance(node, ast.Name) and node.id == "OWN") or (isinstance(node, ast.Attribute) and node.attr == "OWN")


class _Reader:
    def __init__(self, tree: ast.Module, label: str) -> None:
        self.tree = tree
        self.label = label
        self.pins: dict[str, FoundNixpkgsPin] = {}  # the Python variable to its NixpkgsPin
        self.made: dict[int, FoundNixpkgsPin] = {}  # id of a NixpkgsPin call to its record

    def where(self, node: ast.AST) -> str:
        return f"{self.label}:{getattr(node, 'lineno', 1)}:{getattr(node, 'col_offset', 0) + 1}"

    def literal(self, node: ast.expr, call: ast.Call) -> Any:
        try:
            return ast.literal_eval(node)
        except ValueError:
            raise DiscoveryError(
                f"{self.where(call)}: {_callee(call)}(...) takes plain text and True or False only"
            ) from None

    def arguments(self, call: ast.Call, names: tuple[str, ...], optional: tuple[str, ...] = ()) -> dict[str, ast.expr]:
        """The arguments of a call by name. The first ones are positional or keyword; a wrong shape stops the reader."""
        found: dict[str, ast.expr] = {}
        callee = _callee(call)
        for position, arg in enumerate(call.args):
            if isinstance(arg, ast.Starred) or position >= len(names):
                raise DiscoveryError(f"{self.where(call)}: {callee}(...) takes plain text and True or False only")
            found[names[position]] = arg
        for keyword in call.keywords:
            if keyword.arg is not None and keyword.arg not in (*names, *optional):
                raise DiscoveryError(f"{self.where(keyword.value)}: {callee}(...) has no argument `{keyword.arg}`")
            if keyword.arg is None or keyword.arg in found:
                raise DiscoveryError(f"{self.where(call)}: {callee}(...) takes plain text and True or False only")
            found[keyword.arg] = keyword.value
        missing = [n for n in names if n not in found]
        if missing:
            raise DiscoveryError(f"{self.where(call)}: {callee}(...) needs {' and '.join(missing)}, as plain text")
        return found

    def text(self, node: ast.expr, call: ast.Call, field: str, check) -> str:
        """A text argument, checked with the validator of its field (the stub writer must not see a bad value)."""
        value = self.literal(node, call)
        owner = _callee(call)
        if not isinstance(value, str):
            raise DiscoveryError(f"{self.where(node)}: {owner}.{field} must be text, found {value!r}.")
        try:
            check(value)
        except PydanticCustomError as error:
            raise DiscoveryError(
                f"{self.where(node)}: {owner}.{field} {error.message()}, found {_quote(value)}."
            ) from None
        return value

    def nixpkgs_call(self, call: ast.Call) -> FoundNixpkgsPin:
        args = self.arguments(call, ("name", "commit"))
        name = self.text(args["name"], call, "name", _nixpkgs_name)
        commit = self.text(args["commit"], call, "commit", _commit)
        return FoundNixpkgsPin(name, commit, self.label, call.lineno)

    def read_nixpkgs(self) -> None:
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and _callee(node) == "NixpkgsPin":
                self.made[id(node)] = self.nixpkgs_call(node)
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign | ast.AnnAssign) and isinstance(node.value, ast.Call):
                pin = self.made.get(id(node.value))
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target in targets:
                    if pin and isinstance(target, ast.Name):
                        self.pins[target.id] = pin

    def nixpkgs_choice(self, node: ast.expr) -> FoundNixpkgsPin | str:
        if _is_own(node):
            return "own"
        if isinstance(node, ast.Name) and node.id in self.pins:
            return self.pins[node.id]
        if isinstance(node, ast.Call) and id(node) in self.made:
            return self.made[id(node)]
        raise DiscoveryError(
            f"{self.where(node)}: nixpkgs= takes OWN, or a name that you set to NixpkgsPin(...) in this file"
        )

    def input_call(self, call: ast.Call) -> FoundInput:
        args = self.arguments(call, ("name", "url"), ("modules", "flake", "nixpkgs"))
        name = self.text(args["name"], call, "name", _input_name)
        url = self.text(args["url"], call, "url", _input_url)
        flake = True
        if "flake" in args:
            flake = self.literal(args["flake"], call)
            if not isinstance(flake, bool):
                raise DiscoveryError(
                    f"{self.where(args['flake'])}: Input.flake must be True or False, found {flake!r}."
                )
        modules: list[str] = []
        if "modules" in args:
            value = self.literal(args["modules"], call)
            if not isinstance(value, list | tuple):
                raise DiscoveryError(
                    f"{self.where(args['modules'])}: Input.modules must be a list of text, found {value!r}."
                )
            for item in value:
                if not isinstance(item, str):
                    raise DiscoveryError(
                        f"{self.where(args['modules'])}: Input.modules must be a list of text, found {item!r}."
                    )
                try:
                    _module_name(item)
                except PydanticCustomError as error:
                    raise DiscoveryError(
                        f"{self.where(args['modules'])}: Input.modules {error.message()}, found {_quote(item)}."
                    ) from None
                modules.append(item)
        chosen = self.nixpkgs_choice(args["nixpkgs"]) if "nixpkgs" in args else None
        return FoundInput(name, url, flake, tuple(modules), chosen, self.label, call.lineno)

    def read(self) -> Found:
        self.read_nixpkgs()
        calls = sorted(
            (n for n in ast.walk(self.tree) if isinstance(n, ast.Call) and _callee(n) == "Input"),
            key=lambda n: (n.lineno, n.col_offset),
        )
        inputs: list[FoundInput] = []
        for call in calls:
            item = self.input_call(call)
            twin = next((i for i in inputs if i.name == item.name), None)
            if twin:
                raise DiscoveryError(f"{self.where(call)}: the input `{item.name}` is already set at line {twin.line}")
            inputs.append(item)
        pins: dict[str, FoundNixpkgsPin] = {}
        for pin in sorted(self.made.values(), key=lambda p: p.line):
            twin = pins.setdefault(pin.name, pin)
            if twin.commit != pin.commit:
                raise DiscoveryError(
                    f"{self.label}:{pin.line}: the nixpkgs `{pin.name}` is already set to another commit at line {twin.line}"
                )
        return Found(tuple(inputs), tuple(sorted(pins.values(), key=lambda p: p.name)))


def _quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def discover_source(text: str, label: str = "system.py") -> Found:
    """Read the calls of an entry from its text. `label` is the file name in the lines."""
    try:
        tree = ast.parse(text, label)
    except SyntaxError as error:
        raise DiscoveryError(f"{label}:{error.lineno or 1}:{error.offset or 1}: {error.msg}") from None
    return _Reader(tree, label).read()


def discover(path: Path, label: str | None = None) -> Found:
    """Read the calls of an entry file. `label` is the file name in the lines (default: the name of the file)."""
    return discover_source(path.read_text(), label or path.name)
