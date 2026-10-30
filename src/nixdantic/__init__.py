"""nixdantic runtime, round 5 (S10): S1 with the S9 fixes, the S6 error text, and the S8 `Text` and `NixValue`.

The 009 concept adds `Root`, `RootOnly`, `PathRef`, and the positional main value of a reference.

The generated libraries (`pynix_os`, `pynix_hm`, `pynix_flake_parts`) import this module. It holds:

- `Model`: the base class of every generated model. Strict, closed (no unknown field), and it emits only the
  fields that the caller supplied.
- `Unset`: the value of a field that the caller did not supply. It is not `None`: `None` is the Nix `null`.
- The typed references `Package`, `ConfigRef`, `Native`, `PathRef`, and `Text`. Nix resolves them (see `decoder.nix`).
  `Package("hello")` takes its main value by position (009-D42).
  `Text` is a string that holds references: `Text(Package("hello"), "/bin/hello")` is `"${pkgs.hello}/bin/hello"`.
- `NixValue`: free-form data (`JsonValue` plus the references, at any depth). Its containers are `Sequence` and `Mapping`.
- `Root` and `RootOnly`: the base class of a class with its own option path, and the check that `options=` takes only such
  a class (009-D41).
- `fragment`: one model value as one wire-format fragment (version 1, the N2 format).
- `Force`, `Default`, `Before`, `After`, and `Order`: the merge priority and the merge order of one value (L128).
- `Expect`: an annotation that names what a value must be, in the words of the NixOS manual.
- `Model` also rewrites its own `ValidationError` into plain messages (S6): see `_plain`.

Field names are Python names. A field whose Nix name is not a Python name lists the Nix name in the class
variable `__nix_names__`. The models use no Pydantic alias, so a type checker and Pydantic accept the same
keyword names.
"""

from __future__ import annotations

import difflib
import enum
import inspect
import re
import sys
import warnings
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Literal, get_args, get_origin

from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    JsonValue,
    PrivateAttr,
    SerializeAsAny,
    ValidationError,
    model_validator,
)
from pydantic_core import PydanticCustomError, core_schema

__all__ = [
    "After",
    "Before",
    "ConfigRef",
    "Default",
    "ExeOf",
    "Expect",
    "Force",
    "JsonValue",
    "Model",
    "Native",
    "NixValue",
    "Order",
    "Package",
    "PathRef",
    "Plain",
    "PriorityError",
    "Root",
    "RootOnly",
    "Text",
    "Unset",
    "UnsetType",
    "fragment",
    "is_root",
    "matching",
    "nested_class_text",
    "supplied",
]


class UnsetType(enum.Enum):
    """The type of `Unset`."""

    UNSET = "__nixdantic_unset__"

    def __repr__(self) -> str:
        return "Unset"


#: The value of a field that the caller did not supply. Emission leaves it out.
Unset = UnsetType.UNSET


class Reference(BaseModel):
    """A value that Nix resolves after Python emits the fragment.

    The main value goes by position (009-D42): `Package("htop")`, `ConfigRef(["networking", "hostName"])`,
    `Native("packages.nix", ["tools"])`. The keyword form still works.
    """

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)
    _positional: ClassVar[tuple[str, ...]] = ()

    def __init__(self, *args: Any, **data: Any) -> None:
        names = type(self)._positional
        if len(args) > len(names):
            raise TypeError(
                f"{type(self).__name__}() takes {len(names)} positional arguments but {len(args)} were given"
            )
        for name, arg in zip(names, args, strict=False):
            if name in data:
                raise TypeError(f"{type(self).__name__}() got multiple values for argument '{name}'")
            data[name] = arg
        super().__init__(**data)

    # Pydantic validates a dict with its own code and calls `__init__` only for `Package(...)` in a learner file (see `Text`).
    __init__.__pydantic_base_init__ = True  # ty: ignore[unresolved-attribute]


class Package(Reference):
    """A package of the pinned nixpkgs, by attribute path, for example `Package("htop")`."""

    _positional: ClassVar[tuple[str, ...]] = ("attr",)
    kind: Literal["package"] = "package"
    attr: str

    if TYPE_CHECKING:

        def __init__(self, attr: str) -> None: ...


class ConfigRef(Reference):
    """The value of another option, for example `ConfigRef(["networking", "hostName"])`."""

    _positional: ClassVar[tuple[str, ...]] = ("path",)
    kind: Literal["config"] = "config"
    path: list[str]

    if TYPE_CHECKING:

        def __init__(self, path: list[str]) -> None: ...


class Native(Reference):
    """A value from a native Nix file of the workspace: `file` relative to the workspace, then `attr`.

    The file can give a value, or a function of the module arguments (`{ pkgs, inputs, ... }:`). The rule for a
    function depends on `attr`:

    - `attr` is not empty (`Native("packages.nix", ["tools"])`): the file must give an attribute set. The decoder
      calls a function with the module arguments that it names.
    - `attr` is empty (`Native("overlay.nix")`): the reference takes the whole value. The decoder calls a function
      only when it names an argument (`{ pkgs, ... }:`). It returns any other value as it is. So an overlay
      `final: prev: { ... }` stays a function, and Nixpkgs can use it.

    Nix cannot tell `{ ... }:` from `final: prev:`: both name no argument. So the decoder returns a whole-value
    file `{ ... }:` as a function. It does not call it.
    """

    _positional: ClassVar[tuple[str, ...]] = ("file", "attr")
    kind: Literal["native"] = "native"
    file: str
    attr: list[str] = []

    if TYPE_CHECKING:

        def __init__(self, file: str, attr: list[str] = ...) -> None: ...


class PathRef(Reference):
    """A Nix path value of a file in the workspace, for example `PathRef(file="fix.patch")` for `./fix.patch`.

    The decoder gives the path `nativeRoot + "/" + file`. A string would stay a string. Nix copies a path into the
    store when it uses the path, as a kernel patch needs.
    """

    kind: Literal["path"] = "path"
    file: str


class ExeOf(Reference):
    """The main program of any package reference: Nix resolves it with `lib.getExe`.

    `of` is a `Package`, an `InputPkg`, a `NixpkgsPkg` (or a `Prog` of those), or a `Native` that gives a package.
    `ExeOf(InputProg("nix-demo", "daemon"))` is the main program of the package of the input, not of `pkgs`.
    The decoder fails when `of` is not a package. The older kind `exe` (`Exe`) takes only an attribute of `pkgs`.
    """

    _positional: ClassVar[tuple[str, ...]] = ("of",)
    kind: Literal["exe_of"] = "exe_of"
    # `SerializeAsAny` keeps the fields of a subclass (`input`, `nixpkgs`) in the JSON.
    of: SerializeAsAny[Package] | SerializeAsAny[Native]

    if TYPE_CHECKING:

        def __init__(self, of: Package | Native) -> None: ...


class Text(Reference):
    """A string that holds references. Each part is literal text or a reference.

    `Text(Package(attr="hello"), "/bin/hello")` is the Nix string `"${pkgs.hello}/bin/hello"`. The string keeps
    the context of the package, so the package stays a dependency of the system. A string part is always
    literal: Nix does not read `${...}` in it. A reference part is a `Package`, a `ConfigRef`, a `Native`, a `PathRef`,
    an `ExeOf`, or another `Text`.
    """

    kind: Literal["text"] = "text"
    parts: list[str | Package | ConfigRef | Native | PathRef | ExeOf | Text]

    def __init__(self, *parts: str | Package | ConfigRef | Native | PathRef | ExeOf | Text) -> None:
        super().__init__(parts=list(parts))

    # Pydantic calls a custom `__init__` with the keys of every dict that it validates against `Text`. That broke
    # free-form data (`TypeError: Text.__init__() got an unexpected keyword argument`). This mark tells Pydantic
    # to validate a dict with its own code and to call `__init__` only when the learner writes `Text(...)`.
    __init__.__pydantic_base_init__ = True  # ty: ignore[unresolved-attribute]


# --- Merge priority and order (L128; SG34 form a) ----------------------------------------------------------------
# `Force(False)` is `lib.mkForce false`. The call returns its argument type for the type checker (`-> T`), so ty
# checks `Force(False)` as a `bool`. At run time it returns a `Wrapped` marker. `Model` strips the marker before it
# validates the field (so the inner value gets the normal check) and writes it back at emission.


class PriorityError(Exception):
    """A priority or order wrapper is used where it has no meaning. The compiler prints it as one line."""


class Wrapped:
    """The run-time marker of `Force(...)` and the other wrappers. It is not a model: it holds any value."""

    __slots__ = ("kind", "level", "name", "value")

    def __init__(self, kind: str, level: int, value: Any, name: str) -> None:
        if isinstance(value, Wrapped):
            raise PriorityError(f"{name}(...) cannot hold {value.name}(...): use one wrapper for one value.")
        if not isinstance(level, int) or isinstance(level, bool):
            raise PriorityError(f"{name}: the level must be a whole number, found {level!r}.")
        self.kind, self.level, self.value, self.name = kind, level, value, name

    def __repr__(self) -> str:
        return f"{self.name}({self.value!r})"


def Force[T](value: T) -> T:
    """The value wins over every normal value of the same option (Nix `mkForce`, priority 50)."""
    return Wrapped("priority", 50, value, "Force")  # ty: ignore[invalid-return-type]


def Default[T](value: T) -> T:
    """The value loses to every normal value (Nix `mkDefault`, priority 1000)."""
    return Wrapped("priority", 1000, value, "Default")  # ty: ignore[invalid-return-type]


def Before[T](value: T) -> T:
    """The text or list goes before the other definitions of the option (Nix `mkBefore`, order 500)."""
    return Wrapped("order", 500, value, "Before")  # ty: ignore[invalid-return-type]


def After[T](value: T) -> T:
    """The text or list goes after the other definitions of the option (Nix `mkAfter`, order 1500)."""
    return Wrapped("order", 1500, value, "After")  # ty: ignore[invalid-return-type]


def Order[T](level: int, value: T) -> T:
    """The text or list has order LEVEL (Nix `mkOrder`). A lower number comes first. Normal is 1000."""
    return Wrapped("order", level, value, "Order")  # ty: ignore[invalid-return-type]


def _strip(value: Any, path: tuple[Any, ...], marks: dict[tuple[Any, ...], tuple[str, int]]) -> Any:
    """`value` with every `Wrapped` replaced by its inner value. `marks` gets path -> (kind, level)."""
    if isinstance(value, Wrapped):
        if path and isinstance(path[-1], int):
            raise PriorityError(f"{value.name}(...) works on a whole value, not on one item of a list.")
        marks[path] = (value.kind, value.level)
        return _strip(value.value, path, marks)
    if isinstance(value, dict):
        return {k: _strip(v, (*path, k), marks) for k, v in value.items()}
    if isinstance(value, list):
        return [_strip(v, (*path, i), marks) for i, v in enumerate(value)]
    return value


def _mark(wire: Any, path: tuple[Any, ...], kind: str, level: int) -> JsonValue:
    """`wire` with the value at `path` tagged as a priority or an order reference."""
    if not path:
        return {"__nixdantic_ref__": {"kind": kind, "level": level, "value": wire}}
    if isinstance(wire, dict) and path[0] in wire:
        wire[path[0]] = _mark(wire[path[0]], path[1:], kind, level)
    return wire


#: Free-form data: `JsonValue`, `Text`, and the references, at any depth (009-D44). `Sequence` and `Mapping` are
#: covariant, so a type checker accepts a `dict[str, dict[str, int]]` constant (ty refuses it for `dict[str, NixValue]`).
type NixValue = (
    None
    | bool
    | int
    | float
    | str
    | Text
    | Package
    | ConfigRef
    | Native
    | PathRef
    | Sequence[NixValue]
    | Mapping[str, NixValue]
)


_POSIX_CLASSES = {
    "[:alnum:]": "a-zA-Z0-9",
    "[:alpha:]": "a-zA-Z",
    "[:digit:]": "0-9",
    "[:lower:]": "a-z",
    "[:upper:]": "A-Z",
    "[:xdigit:]": "0-9A-Fa-f",
    "[:space:]": " \\t\\n\\r\\f\\v",
    "[:blank:]": " \\t",
    "[:punct:]": "!-/:-@\\[-`{-~",
    "[:print:]": " -~",
    "[:graph:]": "!-~",
    "[:cntrl:]": "\\x00-\\x1f\\x7f",
}


def _posix_to_python(pattern: str) -> str | None:
    """The text of a Python regular expression with the meaning of a POSIX ERE, or None when it cannot tell.

    Differences that the translation removes (S9): inside a bracket expression a backslash is a plain character
    (Python reads an escape); the POSIX classes become ranges; `[.x.]` and `[=x=]` are not translated.
    """
    out: list[str] = []
    i, n = 0, len(pattern)
    while i < n:
        c = pattern[i]
        if c == "\\":
            out.append(pattern[i : i + 2])
            i += 2
        elif c == "[":
            j = i + 1
            negated = j < n and pattern[j] == "^"
            j += 1 if negated else 0
            items: list[str] = []
            first = True
            while True:
                if j >= n:
                    return None  # an unterminated bracket expression
                ch = pattern[j]
                if ch == "]" and not first:
                    break
                if ch == "[" and j + 1 < n and pattern[j + 1] in ".=":
                    return None
                if ch == "[" and j + 1 < n and pattern[j + 1] == ":":
                    end = pattern.find(":]", j + 2)
                    name = pattern[j : end + 2] if end >= 0 else ""
                    if name not in _POSIX_CLASSES:
                        return None
                    items.append(_POSIX_CLASSES[name])
                    j = end + 2
                else:
                    items.append("\\" + ch if ch in "\\[]^&~|" else ch)
                    j += 1
                first = False
            out.append("[" + ("^" if negated else "") + "".join(items) + "]")
            i = j + 1
        else:
            out.append(c)
            i += 1
    return "".join(out)


def matching(pattern: str) -> Any:
    """A validator for `strMatching`. Nix uses POSIX ERE on the bytes of the string; Python gets the same meaning.

    The expression is a Python `bytes` pattern with DOTALL (a POSIX `.` matches a newline and one byte), and it matches
    the UTF-8 bytes of the value. A pattern that Python cannot read gets no Python check: Nix checks the value.
    """
    source = _posix_to_python(pattern)
    compiled = None
    if source is not None:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                compiled = re.compile(source.encode("utf-8"), re.DOTALL)
        except (re.error, FutureWarning, UnicodeEncodeError):
            compiled = None  # POSIX ERE that Python cannot read: Nix checks the value

    def check(value: str) -> str:
        if compiled is not None and compiled.fullmatch(value.encode("utf-8", "surrogatepass")) is None:
            raise PydanticCustomError("pattern_mismatch", "must match the pattern {pattern}", {"pattern": pattern})
        return value

    return AfterValidator(check)


class Expect:
    """`Annotated[int, Field(ge=0), Expect("positive integer")]`: every error of the type reads `must be positive integer`.

    The generator passes the `description` of the Nix type. Pydantic keeps the error type `expected` and the text in `ctx`.
    """

    def __init__(self, what: str):
        self.what = what

    def __get_pydantic_core_schema__(self, source: Any, handler: Any) -> core_schema.CoreSchema:
        return core_schema.custom_error_schema(
            handler(source), "expected", custom_error_message="must be {what}", custom_error_context={"what": self.what}
        )


# --- Plain error text (S6) ---------------------------------------------------------------------------
# A field accepts its own type, `ConfigRef`, `Native`, and `Unset`, so Pydantic reports one error per union branch,
# and it labels each branch (`list[constrained-int]`, `ConfigRef`). `Plain` keeps the branch of the real type,
# removes the labels, and rewrites each built-in message from the table below. The error stays a Pydantic
# `ValidationError`: `str(error)`, `errors()`, and `json()` all show the new text.

_REF_TAGS = {
    "ConfigRef",
    "Native",
    "Package",
    "PathRef",
    "Text",
    "is-instance[UnsetType]",
    "enum[UnsetType]",
    "UnsetType",
}
_TAG = re.compile(
    r"^(bool|int|float|str|none|list\[.*\]|dict\[.*\]|literal\[.*\]|function-after\[.*\]|"
    r"nullable\[.*\]|constrained-.*|json-or-python\[.*\]|.*\[.*\]|[A-Z][A-Za-z0-9_]*)$"
)
#: Built-in error type -> text. `{name}` takes a value from the `ctx` of the error. A type that is not here keeps its text.
_PLAIN = {
    "missing": "is required",
    "string_type": "must be text",
    "int_type": "must be a whole number",
    "float_type": "must be a number",
    "bool_type": "must be true or false",
    "list_type": "must be a list",
    "dict_type": "must be a set of NAME: VALUE pairs",
    "model_type": "must be a {class_name}",
    "greater_than_equal": "must be at least {ge}",
    "greater_than": "must be more than {gt}",
    "less_than_equal": "must be at most {le}",
    "less_than": "must be less than {lt}",
    "literal_error": "must be one of {expected}",
    "string_pattern_mismatch": "must match the pattern {pattern}",
}


class Plain(BaseModel):
    """A model whose `ValidationError` reads plainly. Needs `extra="forbid"` to name the unknown settings."""

    @model_validator(mode="wrap")
    @classmethod
    def _plain(cls, data: Any, handler: Any) -> Any:
        try:
            return handler(data)
        except ValidationError as error:
            raise ValidationError.from_exception_data(error.title, cls._plain_lines(error)) from None

    @classmethod
    def _plain_lines(cls, error: ValidationError) -> list[Any]:
        items = [
            d
            for d in error.errors(include_url=True)
            if not any(p in _REF_TAGS for p in d["loc"][: len(d["loc"]) - (d.get("ctx") or {}).get("tail", 0)])
        ]
        lines: list[Any] = []
        seen: set[tuple[Any, str]] = set()
        for d in items or error.errors(include_url=True):  # keep all lines when only reference branches failed
            ctx = dict(d.get("ctx") or {})
            cut = len(d["loc"]) - ctx.get("tail", 0)  # the part after `cut` came from an inner model: keep it
            head = [p for i, p in enumerate(d["loc"][:cut]) if i == 0 or isinstance(p, int) or not _TAG.match(p)]
            loc = (*head, *d["loc"][cut:])
            name = head[0] if head else None
            text = d["msg"]
            if "url" in d:  # a built-in message: a custom one (Expect, a validator, an inner model) stays as it is
                if d["type"] == "extra_forbidden":
                    close = difflib.get_close_matches(str(name), cls.model_fields, n=1)
                    ctx |= {
                        "advice": f" Did you mean `{close[0]}`?" if close else "",
                        "known": f" The settings are: {', '.join(cls.model_fields)}."
                        if len(cls.model_fields) <= 12
                        else "",
                    }
                    text = "is not a setting.{advice}{known}"
                else:
                    text = _PLAIN.get(d["type"], text)
                info = cls.model_fields.get(str(name))
                if info is not None and info.description:
                    ctx["hint"] = info.description
            option = cls._option(name)
            if option and "option" not in ctx:  # Q16: the NixOS option path, where a root class knows it
                ctx["option"] = option
            ctx["tail"] = len(loc)
            if (loc, text) not in seen:
                seen.add((loc, text))
                lines.append({"type": PydanticCustomError(d["type"], text, ctx), "loc": loc, "input": d["input"]})  # ty: ignore[invalid-argument-type]
        return lines

    @classmethod
    def _option(cls, name: object) -> str:
        """The option path of field `name` (`services.openssh.ports`), or "" when the class is not a root class."""
        root: tuple[str, ...] = getattr(cls, "__nix_path__", ())
        if not root or not isinstance(name, str) or name not in cls.model_fields:
            return ""
        paths: dict[str, tuple[str, ...]] = getattr(cls, "__nix_paths__", {})
        names: dict[str, str] = getattr(cls, "__nix_names__", {})
        return ".".join((*root, *paths.get(name, (names.get(name, name),))))


class Model(Plain):
    """The base of every generated model."""

    model_config = ConfigDict(
        extra="forbid", strict=True, protected_namespaces=(), validate_default=False, use_attribute_docstrings=True
    )  # the hint of a plain error

    #: The option path of a root class, for example `("services", "openssh")`. Empty for an inner class.
    __nix_path__: ClassVar[tuple[str, ...]] = ()
    #: Python field name -> Nix option name, for the fields whose names differ.
    __nix_names__: ClassVar[dict[str, str]] = {}
    #: Python field name -> Nix option path, for an option below a namespace inside a submodule (S9). Nix wants
    #: `{ipv4: {addresses: ...}}`; the field is flat (`ipv4_addresses`), and the nested form is accepted as input.
    __nix_paths__: ClassVar[dict[str, tuple[str, ...]]] = {}

    #: The wrappers (`Force(...)` and friends) that the caller used: field path -> (kind, level).
    _marks: dict[tuple[Any, ...], tuple[str, int]] = PrivateAttr(default_factory=dict)

    @model_validator(mode="wrap")
    @classmethod
    def _priority(cls, data: Any, handler: Any) -> Any:
        """Strip `Force(...)` and the other wrappers. The inner value gets the normal check; emission writes them back."""
        if not isinstance(data, dict):
            return handler(data)
        marks: dict[tuple[Any, ...], tuple[str, int]] = {}
        obj = handler({k: _strip(v, (k,), marks) for k, v in data.items()})
        if isinstance(obj, Model):
            obj._marks = marks
        return obj

    @model_validator(mode="before")
    @classmethod
    def _unnest(cls, data: Any) -> Any:
        """Accept the Nix form of the input: the Nix name of a renamed field, and a namespace as nested dicts."""
        paths, names = cls.__nix_paths__, cls.__nix_names__
        if not isinstance(data, dict):
            return data
        out = data
        if names and any(nix in data and py not in data for py, nix in names.items()):
            out = dict(data)  # the Nix name of a field whose Python name differs (`type` -> `type_`)
            for py, nix in names.items():
                if nix in out and py not in out:
                    out[py] = out.pop(nix)
        if not paths or not any(path[0] in out for path in paths.values()):
            return out
        data = out
        out = dict(data)
        rest: dict[str, Any] = {}
        for py, path in paths.items():
            head = path[0]
            if not isinstance(data.get(head), dict):
                continue
            node = rest.setdefault(head, _copy_tree(data[head]))
            found = _pop_path(node, path[1:])
            if found is not _MISSING:
                if py in out and out[py] != found:  # the typed field and the nested form give two values
                    raise PydanticCustomError("set_twice", "{text}", {"text": _twice(path)})
                out[py] = found
        for head, node in rest.items():
            if node:
                out[head] = node
            else:
                out.pop(head, None)
        return out


class Root(Model):
    """The base of a root class: a class that has its own option path (`Loader` is `boot.loader`).

    The generator writes `class Loader(Root)` for a class with `__nix_path__`, and `class Loader_Efi(Model)` for a part.
    A type checker then tells the two apart: `list[Root]` takes `Loader(...)` and refuses `Loader_Efi(...)` (009-D41).
    """


def is_root(cls: type) -> bool:
    """True when `cls` has its own `__nix_path__` (`Top` has the empty path), False for a part of another class."""
    return "__nix_path__" in vars(cls)


_PARENTS: dict[str, dict[type, tuple[type[Model], str]]] = {}


def _holds(annotation: object, target: type) -> bool:
    return annotation is target or any(_holds(a, target) for a in get_args(annotation))


def _parents(module_name: str) -> dict[type, tuple[type[Model], str]]:
    """child class -> (parent class, field name), for the classes of one generated module. Built at the first error."""
    if module_name not in _PARENTS:
        found: dict[type, tuple[type[Model], str]] = {}
        module = sys.modules.get(module_name)
        classes = [v for v in vars(module).values() if isinstance(v, type) and issubclass(v, Model)] if module else []
        for parent in classes:
            for field, info in parent.model_fields.items():
                for child in classes:
                    if (
                        child is not parent
                        and not is_root(child)
                        and child not in found
                        and _holds(info.annotation, child)
                    ):
                        found[child] = (parent, field)
        _PARENTS[module_name] = found
    return _PARENTS[module_name]


def _wrap(annotation: object, text: str) -> str:
    """`X(...)` as the field of its parent holds it: alone, in a list, or as a value of a set."""
    for arg in get_args(annotation):
        if get_origin(arg) is list:
            return f"[{text}]"
        if get_origin(arg) is dict:
            return f'{{"NAME": {text}}}'
    return text


def nested_class_text(cls: type) -> str:
    """One line for a part class used where a root class belongs: it names the parent and the way to write it.

    One level: `Loader_Efi is a part of Loader; write Loader(efi=Loader_Efi(...))`. Two levels show the whole form.
    Three levels or more name the root class and its first field only.
    """
    name, inner = cls.__name__, f"{cls.__name__}(...)"
    chain: list[type[Model]] = []
    fields: list[str] = []
    here = cls
    while not is_root(here):
        link = _parents(here.__module__).get(here)
        if link is None:
            return f"{name} is a part of another class, not a root class. Write the class that holds it."
        parent, field = link
        chain.append(parent)
        fields.append(field)
        inner = f"{parent.__name__}({field}={_wrap(parent.model_fields[field].annotation, inner)})"
        here = parent
    if len(chain) >= 3:
        inner = f"{chain[-1].__name__}({fields[-1]}=...)"
    return f"{name} is a part of {', which is a part of '.join(p.__name__ for p in chain)}; write {inner}"


def _root_only(value: Model) -> Model:
    if not is_root(type(value)):
        raise PydanticCustomError("nested_class", "{text}", {"text": nested_class_text(type(value))})
    return value


#: `Annotated[Model, RootOnly]`: the value must be an instance of a root class (009-D41). The check runs after Pydantic accepts the model.
RootOnly = AfterValidator(_root_only)


_MISSING = object()


def _copy_tree(node: dict[str, Any]) -> dict[str, Any]:
    return {k: _copy_tree(v) if isinstance(v, dict) else v for k, v in node.items()}


def _pop_path(node: dict[str, Any], path: tuple[str, ...]) -> Any:
    """Remove and return the value at `path` below `node`, or `_MISSING`. Empty dicts on the way are removed."""
    if not path:
        return _MISSING
    if len(path) == 1:
        return node.pop(path[0], _MISSING)
    child = node.get(path[0])
    if not isinstance(child, dict):
        return _MISSING
    found = _pop_path(child, path[1:])
    if found is not _MISSING and not child:
        del node[path[0]]
    return found


def _twice(path: tuple[str, ...]) -> str:
    return f"{'.'.join(path)} is set twice: once as the typed field and once as an extra key, with unequal values."


def _merge(result: dict[str, JsonValue], key: str, wire: JsonValue, path: tuple[str, ...] = ()) -> None:
    """Put `wire` at `result[key]`. Two sections of one name join key by key, so no key is lost.

    A leaf that is set twice with unequal values is a conflict: the error names the full key path.
    """
    where = (*path, key)
    if key not in result:
        result[key] = wire
        return
    have = result[key]
    if isinstance(have, dict) and isinstance(wire, dict) and not _is_wire_ref(have) and not _is_wire_ref(wire):
        for sub, item in wire.items():
            _merge(have, sub, item, where)
    elif have != wire:
        raise ValueError(_twice(where))


def _is_wire_ref(wire: dict[str, JsonValue]) -> bool:
    """True for a tagged reference or an escaped literal: a leaf that must not be joined."""
    return "__nixdantic_ref__" in wire or "__nixdantic_literal__" in wire


def supplied(value: object) -> JsonValue:
    """The wire value of `value`: supplied fields only, references tagged, literal data escaped."""
    if isinstance(value, Text):
        return {"__nixdantic_ref__": {"kind": "text", "parts": [supplied(part) for part in value.parts]}}
    if isinstance(value, Reference):
        return {"__nixdantic_ref__": value.model_dump()}
    if isinstance(value, Model):
        names, paths = type(value).__nix_names__, type(value).__nix_paths__
        result: dict[str, JsonValue] = {}
        for key in sorted(value.model_fields_set):
            if key not in type(value).model_fields:
                continue  # an extra key: the loop below joins it with the typed fields
            item = getattr(value, key)
            if item is Unset:
                continue
            wire = supplied(item)
            for path, (kind, level) in value._marks.items():  # a wrapper at this field
                if path[0] == key:
                    wire = _mark(wire, path[1:], kind, level)
            if key in paths:  # a namespace inside a submodule: nest the value under its path
                node = result
                for part in paths[key][:-1]:
                    node = node.setdefault(part, {})  # ty: ignore[unresolved-attribute]
                node[paths[key][-1]] = wire  # ty: ignore[invalid-assignment]
            else:
                result[names.get(key, key)] = wire
        for key, item in sorted((value.__pydantic_extra__ or {}).items()):
            _merge(result, key, supplied(item))  # a typed namespace field may have filled the same section
        for path, (kind, level) in value._marks.items():  # a wrapper inside an extra key or a nested form
            if path[0] not in type(value).model_fields and path[0] in result:
                result[path[0]] = _mark(result[path[0]], path[1:], kind, level)
        return result
    if isinstance(value, dict):
        data = {str(k): supplied(v) for k, v in value.items()}
        if "__nixdantic_ref__" in data or "__nixdantic_literal__" in data:
            return {"__nixdantic_literal__": data}
        return data
    if isinstance(value, (list, tuple)):
        return [supplied(v) for v in value]
    if isinstance(value, enum.Enum):
        return value.value
    return value  # ty: ignore[invalid-return-type]


def caller_source(depth: int = 2) -> str:
    """`file:line` of a caller, for the `_file` of the fragment (provenance)."""
    frame = inspect.stack()[depth]
    return f"{Path(frame.filename).name}:{frame.lineno}"


def fragment(
    value: Model, *, path: tuple[str, ...] | None = None, source: str | None = None, label: str | None = None
) -> dict[str, JsonValue]:
    """One fragment: `{version, source, path, value}`. The decoder makes one module of it."""
    where = source or caller_source()
    if path is None and not is_root(type(value)):  # a part class has no path of its own and would land at `[]`
        raise ValueError(nested_class_text(type(value)))
    name = label or type(value).__name__
    return {
        "version": 1,
        "source": f"{where} ({name})",
        "path": list(path if path is not None else type(value).__nix_path__),
        "value": supplied(value),
    }
