"""Round 5 (S10) generator: the S9 fixed generator merged with S6 (`Expect`), S8 (`Text`, `NixValue`), S7 (a typed
`__init__` in each root class), and the Q16 union text (`Expect` with the Nix description of an `either`).

S9 copy of the S1 generator. Additions: `PACKAGE-fields.json` (the generated fields with the pool index of their option record).
The fixed copy (S9 step 4) also: nested paths inside a submodule become `__nix_paths__`; `unspecified` and `raw` map to
`JsonValue`; the five Elixir tagged types map to `dict[str, JsonValue]`; a path with no `absolute` flag maps to `str`.

S1 generator: a typed Python package from one pooled nixdantic manifest (format v4, the A1b type table).

Usage: python generate.py MANIFEST OUT PACKAGE [--label TEXT] [--init-nested]

The output is `OUT/PACKAGE/`: one module per option subtree (the first two path parts, as in N3), lazy
package `__init__` files, `py.typed`, and `_generation.py` with the source revisions of the manifest.

Rules (CONCEPT, "The libraries"):
- One mapping per constructor. No rule names an option path.
- An unknown or executable constructor becomes `Native`. The generator counts each one in `gaps.json`.
- A submodule type is one class per module. Two options of one type share the class.
- A submodule type with more than `WHOLE_CONFIG` options holds a whole configuration (`vmVariant`,
  `specialisation`). It becomes `Native`.
- Options with `visible = false` (renamed and removed aliases) and `_module.*` stay out.
- The output is deterministic: sorted input, no time, no absolute path.

Round 4 of the 009 concept adds:
- `Root`: a class with its own option path has the base class `Root`, a part class keeps `Model` (009-D41).
- References in free-form values and `PathRef` on path leaves; `Mapping` and `Sequence` for free-form containers (009-D44).
- `--init-nested`: a typed `__init__` in every class, not only in a root class. The shipped libraries keep it off;
  an input package turns it on (009-D52).
- `all.py`: the lazy flat namespace of the package, with the collision rule (009-D42).
"""

from __future__ import annotations

import argparse
import ast
import json
import keyword
import re
from collections import Counter, defaultdict
from pathlib import Path

WHOLE_CONFIG = 1000
RESERVED = {
    # Names of BaseModel attributes that a field must not shadow.
    "copy",
    "dict",
    "json",
    "schema",
    "schema_json",
    "validate",
    "construct",
    "parse_obj",
    "parse_raw",
    "parse_file",
    "from_orm",
    "register",
    "update_forward_refs",
    "fields",
    "model_config",
    "model_fields",
    "model_computed_fields",
    "model_extra",
    "model_fields_set",
    "model_construct",
    "model_copy",
    "model_dump",
    "model_dump_json",
    "model_json_schema",
    "model_parametrized_name",
    "model_post_init",
    "model_rebuild",
    "model_validate",
    "model_validate_json",
    "model_validate_strings",
}
# A2: named constructors with a serializable mapping. Everything else unknown is `Native`.
# S8: a string with a store path in it is a valid value of these string types, so they accept `Text`.
TEXT_STR = {"str", "nonEmptyStr", "singleLineStr", "separatedString"}
STR_LIKE = {
    "udevValue",
    "kernelParam",
    "home-assistant-component",
    "home-assistant-theme",
    "navidrome plugin",
    "yubiKeyId",
    "goDuration",
    "ipAddress",
    "passwdEntry",
}
ELIXIR = {"rawElixir", "elixirTuple", "elixirAtom", "elixirCharlist", "elixirMap"}
# Names that the generated modules import. A generated class must not take one of them.
IMPORTED = {
    "Annotated",
    "ClassVar",
    "ConfigRef",
    "Expect",
    "Field",
    "JsonValue",
    "Literal",
    "Mapping",
    "Model",
    "Native",
    "NixValue",
    "Package",
    "PathRef",
    "Root",
    "Sequence",
    "TYPE_CHECKING",
    "Text",
    "Unset",
    "UnsetType",
    "matching",
}
JSON_LIKE = {"anything", "systemd option", "nixpkgs-config", "LDAP", "json", "sysctl option value", "sysfs value"}
NATIVE_REASON = {
    "unspecified": "accepts any value with no declared shape (A2)",
    "raw": "a raw value: Nix does not merge or check it",
    "functionTo": "a function",
    "function": "a function",
    "deferredModuleWith": "a module",
    "deferredModule": "a module",
    "optionType": "type metadata",
    "nixpkgs-overlay": "executable Nix code (A2)",
    "secret": "a secret needs its own adapter (CONCEPT)",
    "attrTag": "a tagged union: not mapped in S1",
    "luaInline": "inline Lua code",
    "pkgs": "a package set",
    "Toplevel NixOS config": "a whole configuration",
    "dagOf": "a Home Manager DAG: not mapped in S1",
    "selectorFunction": "a function (A2)",
    "overlayFunction": "a function (A2)",
}


def ident(value: str) -> str:
    """A Python name for a Nix name."""
    result = re.sub(r"\W", "_", value)
    if not result or result[0].isdigit() or result.startswith("_"):
        result = "n_" + result
    if keyword.iskeyword(result) or keyword.issoftkeyword(result) or result in RESERVED or result.startswith("model_"):
        result += "_"
    return result


def camel(value: str) -> str:
    parts = [p for p in re.split(r"[^0-9A-Za-z]+", value) if p]
    text = "".join(p[:1].upper() + p[1:] for p in parts) or "N"
    return "N" + text if text[0].isdigit() else text


ROLE = re.compile(r"\{(option|var|command|file|env|manpage|literal|option-doc|ref)\}`([^`]*)`")


def doc(text: object) -> str:
    """A plain docstring from a NixOS description (the roles become code spans)."""
    if isinstance(text, dict):
        text = text.get("text", "")
    if not isinstance(text, str):
        return ""
    text = ROLE.sub(lambda m: f"`{m.group(2)}`", text).strip()
    text = text.replace("\\", "\\\\").replace('"""', "'''")
    return text + " " if text.endswith('"') else text


def expect(desc: str) -> str:
    """The `, Expect(...)` marker, or nothing when the type has no description: the learner reads `must be DESC`, the words of the NixOS manual."""
    return f", Expect({desc!r})" if desc else ""


class Generator:
    def __init__(self, manifest: dict, package: str, label: str, init_nested: bool = False):
        self.init_nested = init_nested
        self.types: list[dict] = manifest["types"]
        self.pool: list[dict] = manifest.get("optionPool", [])
        self.manifest = manifest
        self.package = package
        self.label = label
        self.gaps: Counter[str] = Counter()
        self.stack: list[int] = []
        self.pool_index = {id(r): i for i, r in enumerate(self.pool)}
        self.sites: list[list] = []  # [module, class, field, pool index]
        self.module_sites: list[list] = []
        self.in_union = False  # True below an `either`: only the outer union gets `Expect` (Q16)

    def record(self, ref: object) -> dict:
        # A pooled or a plain manifest.
        return self.pool[ref] if isinstance(ref, int) else ref  # ty: ignore[invalid-return-type]

    def kept(self, rec: dict) -> bool:
        """An option stays out when it is `_module.*`, or hidden and an alias, a removed option, or internal.

        S9: S1 dropped every option with `visible = false`. Many of those are real options that upstream hides from the
        documentation (`programs.jq.colors.*`, `programs.brave.enable`); Nix accepts values for them.
        An alias (`Alias of ...`) and a removed option (no type, `unspecified`) stay out.
        """
        meta = rec.get("metadata", {})
        if rec["path"][0] == "_module":
            return False
        if meta.get("visible", True) is not False:
            return True
        text = meta.get("description")
        text = text.get("text", "") if isinstance(text, dict) else (text or "")
        hidden_alias = text.startswith("Alias of") or self.types[rec["type"]]["ctor"] == "unspecified"
        return not (hidden_alias or meta.get("internal"))

    # --- one module ---------------------------------------------------------------------------
    def module(self, prefix: tuple[str, ...], records: list[dict]) -> str:
        self.blocks: list[tuple[str, list[str], set[str]]] = []
        self.classes: dict[int, str] = {}  # type id -> class name, per module
        self.names: set[str] = set(IMPORTED)
        self.pending: list[tuple[str, int, str]] = []
        root = camel(prefix[-1]) if prefix else "Top"
        tree: dict = {}
        for rec in records:
            node = tree
            for part in rec["path"][len(prefix) : -1]:
                node = node.setdefault(part, {})
                if "__option__" in node:  # an option with sub-paths: keep the option
                    break
            else:
                node.setdefault(rec["path"][-1], {})["__option__"] = rec
        self.namespace(
            root, tree, prefix, f"Options below `{'.'.join(prefix)}`." if prefix else "Options at the top level."
        )
        while self.pending:
            name, tid, docstring = self.pending.pop(0)
            self.submodule(name, tid, docstring)
        body = self.ordered()
        text = "\n".join(body)
        # A module imports `Mapping`, `Sequence`, `PathRef`, and `Root` only when it uses them.
        collections = sorted(n for n in ("Mapping", "Sequence") if re.search(rf"\b{n}\[", text))
        optional = [
            n for n, pattern in (("PathRef", r"\bPathRef\b"), ("Root", r"\(Root\):")) if re.search(pattern, text)
        ]
        names = sorted(
            {"ConfigRef", "Expect", "JsonValue", "Model", "Native", "NixValue", "Package", "Text", "Unset", "UnsetType"}
            | set(optional),
            key=str.lower,
        )
        head = [
            f'"""{self.label}: options below `{".".join(prefix) or "(top)"}`. Generated by nixdantic S1; do not edit."""',
            "from __future__ import annotations",
            *([f"from collections.abc import {', '.join(collections)}"] if collections else []),
            "from typing import TYPE_CHECKING, Annotated, ClassVar, Literal",
            "from pydantic import Field",
            f"from nixdantic import {', '.join(names)}, matching",
            "",
        ]
        return "\n".join(head + body) + "\n"

    def ordered(self) -> list[str]:
        """Class blocks with each class after the classes that its fields use.

        Pydantic then completes each class when Python creates it. A class in a cycle cannot come after
        all of its dependencies; the module rebuilds it at the end, so the first validation stays fast.
        """
        blocks = {name: (body, deps) for name, body, deps in self.blocks}
        order: list[str] = []
        state: dict[str, int] = {}
        cyclic: list[str] = []

        def visit(name: str) -> None:
            state[name] = 1
            for dep in sorted(blocks[name][1]):
                if dep == name or dep not in blocks:
                    continue
                if state.get(dep) == 1:
                    cyclic.append(name)
                elif dep not in state:
                    visit(dep)
            state[name] = 2
            order.append(name)

        for name, _body, _deps in self.blocks:
            if name not in state:
                visit(name)
        lines = [line for name in order for line in blocks[name][0]]
        selfref = [n for n, (_b, deps) in blocks.items() if n in deps]
        late = sorted(set(cyclic) | set(selfref))
        if late:
            lines.append("for _model in (" + ", ".join(late) + ",):")
            lines.append("    _model.model_rebuild()")
        return lines

    def unique(self, base: str) -> str:
        name, n = base, 2
        while name in self.names:
            name, n = f"{base}{n}", n + 1
        self.names.add(name)
        return name

    def emit_class(
        self,
        name: str,
        docstring: str,
        fields: list[tuple[str, str, str, str]],
        path: tuple[str, ...] | None,
        extra: str | None = None,
        nested: dict[str, tuple[str, ...]] | None = None,
    ) -> None:
        body = [f"class {name}({'Model' if path is None else 'Root'}):"]
        body.append(f'    """{docstring or name}"""' if docstring else f'    """Options of {name}."""')
        if path is not None:
            body.append(f"    __nix_path__: ClassVar[tuple[str, ...]] = {tuple(path)!r}")
        nested = nested or {}
        paths = {py: nested[nix] for py, nix, _, _ in fields if nix in nested and len(nested[nix]) > 1}
        renamed = {py: nix for py, nix, _, _ in fields if py != nix and py not in paths}
        if renamed:
            body.append(f"    __nix_names__: ClassVar[dict[str, str]] = {dict(sorted(renamed.items()))!r}")
        if paths:  # an option below a namespace inside a submodule: Nix wants `{a: {b: value}}`, not the key `a.b`
            body.append(f"    __nix_paths__: ClassVar[dict[str, tuple[str, ...]]] = {dict(sorted(paths.items()))!r}")
        if extra is not None:
            body.append("    model_config = Model.model_config | {'extra': 'allow'}")
            body.append(
                f"    __pydantic_extra__: dict[str, {extra}] = Field(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]"
            )
        for py, _nix, annotation, text in fields:
            body.append(f"    {py}: {annotation} = Unset")
            if text:
                body.append(f'    """{text}"""')
        # S7 (Q15): a root class gets a typed `__init__` that ty reads for field help.
        # With `--init-nested`, every class with fields or extra keys gets one, so ty checks a nested value too.
        if (path is not None and fields) or (self.init_nested and (fields or extra is not None)):
            body += self.init_block(docstring or name, fields, extra)
        deps = set(re.findall(r"\b([A-Z][A-Za-z0-9_]*)\b", " ".join(f[2] for f in fields) + " " + (extra or "")))
        self.blocks.append((name, body + ["", ""], deps))

    @staticmethod
    def init_block(docstring: str, fields: list[tuple[str, str, str, str]], extra: str | None) -> list[str]:
        """`if TYPE_CHECKING: def __init__(self, *, NAME: TYPE = Unset, ...)` with a Google `Args:` docstring (S7).

        It changes nothing at run time. ty shows the `Args:` text on hover, in completion, and in signature help.
        """
        params = ", ".join(f"{py}: {annotation} = Unset" for py, _nix, annotation, _text in fields)
        if extra is not None:
            params += f", **extra: {extra}" if fields else f"**extra: {extra}"
        star = "*, " if fields else ""
        lines = [
            "",
            "    if TYPE_CHECKING:",
            "",
            f"        def __init__(self, {star}{params}) -> None:",
            f'            """{docstring.strip().splitlines()[0] if docstring.strip() else "Options."}',
            "",
            "            Args:",
        ]
        for py, _nix, _annotation, text in fields:
            parts = text.strip().splitlines() or [""]
            lines.append(f"                {py}: {parts[0]}".rstrip())
            lines += [f"                    {part.strip()}".rstrip() for part in parts[1:]]
        return lines + ['            """', "            ..."]

    def fields_of(self, owner: str, items: dict) -> list[tuple[str, str, str, str]]:
        fields = []
        used: set[str] = set()
        for nix in sorted(items):
            py = ident(nix)
            while py in used:
                py += "_"
            used.add(py)
            fields.append((py, nix, *items[nix](owner, py)))
        return fields

    def namespace(self, name: str, tree: dict, path: tuple[str, ...] | None, docstring: str) -> str:
        name = self.unique(name)
        items = {}
        for key, sub in tree.items():
            if key == "__option__":
                continue
            if "__option__" in sub:
                rec = sub["__option__"]
                items[key] = lambda owner, py, rec=rec: (
                    self.option_annotation(owner, py, rec),
                    doc(rec["metadata"].get("description")),
                )
            else:
                items[key] = lambda owner, py, sub=sub: (
                    self.namespace(f"{owner}_{camel(py)}", sub, None, "") + " | UnsetType",
                    "",
                )
        self.emit_class(name, docstring, self.fields_of(name, items), path)
        return name

    def option_annotation(self, owner: str, py: str, rec: dict) -> str:
        self.module_sites.append([owner, py, self.pool_index.get(id(rec), -1)])
        return (
            self.typed(rec["type"], f"{owner}_{camel(py)}", doc(rec["metadata"].get("description")))
            + " | ConfigRef | Native | UnsetType"
        )

    def submodule(self, name: str, tid: int, docstring: str) -> None:
        entry = self.types[tid]
        items = {}
        nested: dict[str, tuple[str, ...]] = {}
        for ref in entry.get("options", []):
            rec = self.record(ref)
            if not self.kept(rec):
                continue
            # Sub-options of a submodule are flat fields; a namespace inside the submodule keeps its path (`__nix_paths__`).
            nested[".".join(rec["path"])] = tuple(rec["path"])
            items[".".join(rec["path"])] = lambda owner, py, rec=rec: (
                self.option_annotation(owner, py, rec),
                doc(rec["metadata"].get("description")),
            )
        extra = None
        if entry.get("freeform") and "freeformType" in entry.get("nested", {}):
            ff = self.types[entry["nested"]["freeformType"]]
            inner = ff.get("nested", {}).get("elemType")
            typed_extra = inner is not None and ff["ctor"] in {"attrsWith", "attrsOf"}
            # An extra value can be a `ConfigRef` (`NixValue` holds all references).
            extra = self.typed(inner, f"{name}_Extra", "") + " | ConfigRef" if typed_extra else "NixValue"
        self.emit_class(name, docstring, self.fields_of(name, items), None, extra, nested)

    # --- one type -----------------------------------------------------------------------------
    def typed(self, tid: int, name: str, docstring: str) -> str:
        if tid in self.stack:  # a recursive data type (a JSON value, for example)
            self.gaps["recursive data type: JsonValue"] += 1
            return "NixValue"
        self.stack.append(tid)
        try:
            return self._typed(tid, name, docstring)
        finally:
            self.stack.pop()

    def _typed(self, tid: int, name: str, docstring: str) -> str:
        t = self.types[tid]
        ctor, kids, payload = t["ctor"], t.get("nested", {}), t.get("payload", {})
        tname, desc = t.get("name", ""), t.get("description", "") or ""
        if t.get("submodule"):
            if len(t.get("options", [])) > WHOLE_CONFIG:
                self.gaps["submodule (whole configuration)"] += 1
                return "Native"
            if tid not in self.classes:
                self.classes[tid] = self.unique(name)
                self.pending.append((self.classes[tid], tid, docstring))
            return self.classes[tid]
        if ctor == "bool":
            return "bool"
        if ctor == "int":
            bounds = []
            m = re.search(r"between (-?\d+) and (-?\d+)", desc)
            if m:
                bounds = [f"ge={m.group(1)}", f"le={m.group(2)}"]
            elif ">0" in desc or tname == "positiveInt":
                bounds = ["ge=1"]
            elif ">=0" in desc or tname == "unsignedInt":
                bounds = ["ge=0"]
            return f"Annotated[int, Field({', '.join(bounds)}){expect(desc)}]" if bounds else "int"
        if ctor in {"float", "number"}:
            return "float | int" if ctor == "number" else "float"
        if ctor == "strMatching" and "pattern" in payload:  # S6 Expect; no Text (S8): a pattern checks the whole string
            return f"Annotated[str, matching({payload['pattern']!r}){expect(desc)}]"
        if ctor in ELIXIR:  # `{_elixirType = "tuple"; value = ...}`: a tagged attribute set, not a plain string or list
            self.gaps[f"{ctor}: tagged attribute set (dict of JsonValue)"] += 1
            return "dict[str, JsonValue]"
        if ctor in {"unspecified", "raw"}:  # any value: free-form data, so a string may hold a store path (S8)
            self.gaps[f"{ctor}: JsonValue (S9)"] += 1  # S9 reason kept, so the gates count it; the type is NixValue
            return "NixValue"
        if ctor in TEXT_STR:
            return "str | Text"
        if ctor in STR_LIKE:
            return "str"
        if ctor in {"path", "absolutePath", "pathWith"}:
            # Nix: `absolute = null` accepts a relative string. Only an absolute or in-store path needs the slash (S9).
            absolute = payload.get("absolute") is True or payload.get("inStore") is True or ctor == "absolutePath"
            return (
                f"Annotated[str, matching('/.*'){expect(desc)}] | Text | PathRef"
                if absolute
                else "str | Text | PathRef"
            )
        if ctor == "enum":
            values = payload.get("values")
            if values:
                return "Literal[" + ", ".join(repr(v) for v in values) + "]"
            self.gaps["enum without values"] += 1
            return "str"
        if ctor in {"package", "ibus-engine"}:  # `ibus-engine` is a custom type that checks for a package, not a string
            return "Package"
        if ctor in JSON_LIKE:
            return "NixValue"
        if ctor == "attrs":
            return "Mapping[str, NixValue]"  # covariant, so ty accepts a nested constant
        if ctor in {"listOf", "unique", "nonEmptyListOf"} and "elemType" in kids:
            if ctor == "unique":  # `types.unique` wraps a type and keeps its shape
                return self.typed(kids["elemType"], name, docstring)
            item = self.typed(kids["elemType"], f"{name}_Item", docstring)
            return f"Sequence[{item}]" if item == "NixValue" else f"list[{item}]"  # free-form items: covariant for ty
        if ctor in {"attrsWith", "attrsOf", "lazyAttrsOf"} and "elemType" in kids:
            item = self.typed(kids["elemType"], f"{name}_Value", docstring)
            return (
                f"Mapping[str, {item}]" if item == "NixValue" else f"dict[str, {item}]"
            )  # free-form values: covariant
        if ctor == "nullOr" and "elemType" in kids:
            return f"{self.typed(kids['elemType'], name, docstring)} | None"
        if ctor == "either" and {"left", "right"} <= kids.keys():
            outer, self.in_union = not self.in_union, True
            try:
                union = f"{self.typed(kids['left'], name, docstring)} | {self.typed(kids['right'], name + '_Or', docstring)}"
            finally:
                self.in_union = not outer
            text = self.nix_desc(tid)[0] if outer else ""
            # Q16: one line per union, on the outer `either` only. A union with a submodule keeps the errors of the
            # submodule (a typo inside it).
            return f"Annotated[{union}{expect(text)}]" if text and "submodule" not in text else union
        if ctor == "coercedTo" and {"coercedType", "finalType"} <= kids.keys():
            return f"{self.typed(kids['finalType'], name, docstring)} | {self.typed(kids['coercedType'], name + '_From', docstring)}"
        if ctor == "tuple":  # `elixirTuple` is in ELIXIR
            return "Sequence[NixValue]"
        self.gaps[f"{ctor}: {NATIVE_REASON.get(ctor, 'unknown constructor')}"] += 1
        return "Native"

    def nix_desc(self, tid: int, seen: frozenset[int] = frozenset()) -> tuple[str, str]:
        """The Nix description of a type and its description class, as `lib/types.nix` builds them.

        The manifest keeps the description of a leaf type only (a nested description can recurse without end), so
        the generator builds the description of `listOf`, `attrsOf`, `nullOr`, `either`, `coercedTo`, and `unique`
        with the words of the pinned `lib/types.nix`. The class of a leaf is a guess: a text with `;` is a
        clause (a bounded number), an enum of two or more values is a conjunction, the rest are nouns.
        """
        t = self.types[tid]
        ctor, kids = t["ctor"], t.get("nested", {})

        def phrase(kid: int, classes: set[str]) -> str:
            text, cls = self.nix_desc(kid, seen | {tid})
            return text if cls in classes else f"({text})"

        if tid in seen:
            return "value", "noun"
        if t.get("submodule"):
            return "submodule", "noun"
        if ctor in {"listOf", "nonEmptyListOf"} and "elemType" in kids:
            return (
                f"{'non-empty ' if ctor == 'nonEmptyListOf' else ''}list of {phrase(kids['elemType'], {'noun', 'composite'})}",
                "composite",
            )
        if ctor in {"attrsWith", "attrsOf", "lazyAttrsOf"} and "elemType" in kids:
            lazy = ctor == "lazyAttrsOf" or (t.get("payload") or {}).get("lazy") is True
            return (
                f"{'lazy attribute set' if lazy else 'attribute set'} of {phrase(kids['elemType'], {'noun', 'composite'})}",
                "composite",
            )
        if ctor == "nullOr" and "elemType" in kids:
            return f"null or {phrase(kids['elemType'], {'noun', 'conjunction'})}", "conjunction"
        if ctor == "unique" and "elemType" in kids:
            return self.nix_desc(kids["elemType"], seen | {tid})
        if ctor == "either" and {"left", "right"} <= kids.keys():
            left, cls = self.nix_desc(kids["left"], seen | {tid})
            if cls == "nonRestrictiveClause":
                return f"{left}, or {phrase(kids['right'], {'noun', 'conjunction'})}", "conjunction"
            return (
                f"{phrase(kids['left'], {'noun', 'conjunction'})} or {phrase(kids['right'], {'noun', 'conjunction', 'composite'})}",
                "conjunction",
            )
        if ctor == "coercedTo" and {"coercedType", "finalType"} <= kids.keys():
            return (
                f"{phrase(kids['finalType'], {'noun'})} or {phrase(kids['coercedType'], {'noun'})} convertible to it",
                "noun",
            )
        text = t.get("description") or t.get("name") or ctor
        if ctor == "enum":
            return text, "conjunction" if len((t.get("payload") or {}).get("values") or []) >= 2 else "noun"
        return text, "nonRestrictiveClause" if ";" in text else "noun"

    # --- the package ----------------------------------------------------------------------------
    def run(self, out: Path) -> dict:
        roots = [self.record(r) for r in self.manifest["options"]]
        roots = [r for r in roots if self.kept(r)]
        groups: dict[tuple[str, ...], list[dict]] = defaultdict(list)
        for rec in sorted(roots, key=lambda r: r["path"]):
            groups[
                tuple(rec["path"][:2])
                if len(rec["path"]) > 2
                else tuple(rec["path"][:1])
                if len(rec["path"]) == 2
                else ()
            ].append(rec)
        pkg = out / self.package
        if any(prefix and ident(prefix[0]) == "all" for prefix in groups):
            raise SystemExit(f"{self.package}: an option module is named `all`, which the flat namespace needs")
        written: dict[tuple[str, ...], str] = {}
        for prefix, records in sorted(groups.items()):
            parts = [ident(p) for p in prefix] or ["top"]
            target = pkg.joinpath(*parts).with_suffix(".py")
            if len(prefix) == 1:  # `networking.hostName` style: the module is the first part
                target = pkg / parts[0] / "__options__.py"
            target.parent.mkdir(parents=True, exist_ok=True)
            self.module_sites = []
            source = self.module(prefix, records)
            module_name = ".".join(target.relative_to(out).with_suffix("").parts)
            self.sites += [[module_name, *site] for site in self.module_sites]
            ast.parse(source)  # fail early on a bad name
            target.write_text(source)
            written[prefix] = str(target.relative_to(out))
        for folder in sorted({p for p in pkg.rglob("*") if p.is_dir()} | {pkg}):
            names = sorted(
                {p.stem for p in folder.glob("*.py") if p.name != "__init__.py"}
                | {p.name for p in folder.iterdir() if p.is_dir()}
            )
            (folder / "__init__.py").write_text(
                '"""Lazy package: each name loads on first use."""\n'
                "from importlib import import_module\nfrom types import ModuleType\n\n"
                f"__all__ = {names!r}\n\n\n"
                "def __getattr__(name: str) -> ModuleType:\n"
                "    if name not in __all__:\n        raise AttributeError(name)\n"
                '    return import_module(f"{__name__}.{name}")\n'
            )
        write_namespace(out, self.package)
        (pkg / "py.typed").write_text("")
        (pkg / "_generation.py").write_text(
            '"""The source of this generated package."""\n\n'
            f"SOURCE: dict[str, str] = {dict(sorted(self.manifest.get('source', {}).items()))!r}\n"
            f"FORMAT: str = {self.manifest['format']!r}\n"
        )
        summary = {
            "package": self.package,
            "source": self.manifest.get("source", {}),
            "roots": len(self.manifest["options"]),
            "rootsKept": len(roots),
            "modules": len(written),
            "gaps": dict(sorted(self.gaps.items())),
        }
        (out / f"{self.package}-fields.json").write_text(json.dumps(self.sites, sort_keys=True) + "\n")
        (out / f"{self.package}-gaps.json").write_text(json.dumps(summary, indent=1, sort_keys=True) + "\n")
        return summary


def camel_words(words: tuple[str, ...]) -> str:
    return "_".join(camel(w) for w in words)


def write_namespace(out: Path, package: str) -> None:
    """Write `PACKAGE/all.py`: every class of the package in one flat namespace (009-D42).

    `from pynix_os import all as nixos`, then `nixos.Loader(efi=nixos.Loader_Efi(...))`. At run time a module
    `__getattr__` backed by a name-to-module index loads the module of a name at its first use. A type checker reads a
    `TYPE_CHECKING` block of explicit imports. A star import cannot be lazy, so the module has none.

    Collision rule: a plain name that two classes share goes to none of them. Each holder gets its option path in front
    (`Networking_Firewall`). The root class named after its own path takes that path as its name.
    """
    path_pattern = re.compile(r"__nix_path__: ClassVar\[tuple\[str, \.\.\.\]\] = \(([^)]*)\)")
    owners: dict[str, list[tuple[str, bool, tuple[str, ...]]]] = defaultdict(
        list
    )  # name -> [(module, root, path words)]
    for file in sorted((out / package).rglob("*.py")):
        if file.name == "all.py":
            continue
        module = ".".join(file.relative_to(out).with_suffix("").parts)
        for block in re.split(r"(?m)^(?=class )", file.read_text()):
            found = re.match(r"class (\w+)\((?:Model|Root)\):", block)
            if not found:
                continue
            path = path_pattern.search(block)
            if path:
                words = tuple(re.findall(r"""['"]([^'"]*)['"]""", path.group(1)))
            else:
                words = tuple(p for p in module.split(".")[1:] if p != "__options__")
            owners[found.group(1)].append((module, path is not None, words))
    index: dict[str, str] = {}  # public name -> "module:ClassName"
    for name, held in sorted(owners.items()):
        if len(held) == 1:
            index[name] = f"{held[0][0]}:{name}"
            continue
        for module, is_root, words in held:
            own = is_root and words and camel(words[-1]).lower() == name.lower()
            public = camel_words(words) if own else f"{camel_words(words)}_{name}"
            if public in index:
                raise SystemExit(f"{package}: the public name {public} is taken twice")
            index[public] = f"{module}:{name}"
    for public in index:
        if not public.isidentifier() or keyword.iskeyword(public):
            raise SystemExit(f"{package}: the public name {public} is not a Python name")
    by_module: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for public, target in sorted(index.items()):
        module, real = target.split(":")
        by_module[module].append((public, real))
    lines = [
        f'"""Every class of {package} in one flat namespace. Generated; do not edit.',
        "",
        f"`from {package} import all as nixos`, then `nixos.Loader(efi=nixos.Loader_Efi(...))`."
        " Python loads the module of a name at its first use.",
        '"""',
        "",
        "from importlib import import_module as _import_module",
        "from typing import TYPE_CHECKING as _TYPE_CHECKING, Any as _Any",
        "",
        "if _TYPE_CHECKING:  # the type checker reads these lines; Python skips them",
    ]
    for module in sorted(by_module):
        lines.append(
            f"    from {module} import " + ", ".join(f"{real} as {public}" for public, real in by_module[module])
        )
    lines += [
        "else:",
        f"    _INDEX = {json.dumps(index)}",
        "",
        "",
        "    def __getattr__(name: str) -> _Any:",
        "        try:",
        "            target = _INDEX[name]",
        "        except KeyError:",
        "            close = [n for n, t in _INDEX.items() if t.endswith(':' + name) and n != name]",
        "            hint = f' Two classes have this name. Write one of: {', '.join(close)}.' if close else ''",
        "            raise AttributeError(f'The flat list of {__name__.split('.')[0]} has no class {name}.{hint}') from None",
        "        module, _, real = target.partition(':')",
        "        value = getattr(_import_module(module), real)",
        "        globals()[name] = value",
        "        return value",
        "",
        "",
        "    def __dir__() -> list[str]:",
        "        return sorted(_INDEX)",
        "",
    ]
    (out / package / "all.py").write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("package")
    parser.add_argument("--label", default="nixdantic")
    parser.add_argument(
        "--init-nested", action="store_true", help="a typed __init__ for every class with fields or extra keys"
    )
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text())
    summary = Generator(manifest, args.package, args.label, args.init_nested).run(args.out)
    print(json.dumps({k: v for k, v in summary.items() if k != "gaps"}))


if __name__ == "__main__":
    main()
