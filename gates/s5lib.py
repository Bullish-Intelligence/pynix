"""Shared helpers of the S5 gates: module listing, field listing by AST, tool paths, gap files."""
import ast
import json
import re
from pathlib import Path

import os

# The tools come from the environment (`run_gates.sh` sets them from the uv environment of the repository).
TY = os.environ["GATES_TY"]
PYTHON = os.environ["PY"]

# A gap of this reason maps to JsonValue, dict, or str, not to Native.
# S10: copy of evidence/S9/gates/s5lib.py (S9 copy of S5). Change: the alias count takes NixValue and JsonValue; GAPS_DIR removed.
# S9: copy of evidence/S5/s5lib.py. The fixed generator adds mappings that are not Native: `unspecified` and `raw` to
# JsonValue, and the five Elixir tagged types to dict[str, JsonValue]. Their gap reasons join the set.
NOT_NATIVE_GAPS = {
    "recursive data type: JsonValue", "enum without values",
    "unspecified: JsonValue (S9)", "raw: JsonValue (S9)",
    "rawElixir: tagged attribute set (dict of JsonValue)", "elixirTuple: tagged attribute set (dict of JsonValue)",
    "elixirAtom: tagged attribute set (dict of JsonValue)", "elixirCharlist: tagged attribute set (dict of JsonValue)",
    "elixirMap: tagged attribute set (dict of JsonValue)",
}

ESCAPES = {"ConfigRef", "Native", "UnsetType"}  # the union tail that every option field carries


def module_files(root: Path, package: str):
    """Yield (dotted module name, path) for every module of the package, in sorted order."""
    base = root / package
    for path in sorted(base.rglob("*.py")):
        rel = path.relative_to(root).with_suffix("")
        parts = list(rel.parts)
        if parts[-1] == "__init__":
            parts.pop()
        yield ".".join(parts), path


def segment(lines, node) -> str:
    """The source text of a node. Faster than `ast.get_source_segment`, which splits the file on every call."""
    if node.lineno == node.end_lineno:
        return lines[node.lineno - 1].encode()[node.col_offset : node.end_col_offset].decode()
    first = lines[node.lineno - 1].encode()[node.col_offset :].decode()
    last = lines[node.end_lineno - 1].encode()[: node.end_col_offset].decode()
    return " ".join([first, *lines[node.lineno : node.end_lineno - 1], last])


def fields_of_source(path: Path):
    """Yield (class name, field name, annotation text) for each annotated field of each class.

    ClassVar entries are not fields. `__pydantic_extra__` is a field: it types the free-form keys.
    """
    src = path.read_text()
    lines = src.splitlines()
    tree = ast.parse(src)
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for item in node.body:
            if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                text = segment(lines, item.annotation)
                if text.startswith("ClassVar"):
                    continue
                yield node.name, item.target.id, text


def native_expected(gaps_file: Path) -> int:
    """The number of Native mappings that the generator counted in its gap file."""
    gaps = json.loads(gaps_file.read_text())["gaps"]
    return sum(n for reason, n in gaps.items() if reason not in NOT_NATIVE_GAPS)


def json_expected(gaps_file: Path) -> int:
    return json.loads(gaps_file.read_text())["gaps"].get("recursive data type: JsonValue", 0)


_STRING = re.compile(r"\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*'")
BAD_TOKEN = re.compile(r"\b(Unknown|Any|object|Todo)\b|@Todo")


def strip_strings(text: str) -> str:
    """Remove string literals, so that `Literal["object"]` does not look like `object`."""
    return _STRING.sub('""', text)


def split_union(text: str):
    """Split a revealed type at its top-level `|`."""
    parts, depth, cur = [], 0, ""
    for ch in text:
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == "|" and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    parts.append(cur.strip())
    return parts


def split_args(text: str):
    """Split at the top-level commas."""
    parts, depth, cur = [], 0, ""
    for ch in text:
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    parts.append(cur.strip())
    return parts


def flatten_annotated(members):
    """S10: ty flattens `Annotated[A | B, Expect(...)]` into the union around it. Do the same."""
    for m in members:
        m = m.strip()
        if m.startswith("Annotated[") and m.endswith("]"):
            yield from flatten_annotated(split_union(split_args(m[len("Annotated["):-1])[0]))
        else:
            yield m


def source_view(annotation: str, field: str, flatten: bool = False):
    """The source view of one field annotation.

    Returns (base members, native count, deduped native count, jsonvalue count).
    The base is the annotation without the tail `ConfigRef | Native | UnsetType`.
    A type checker (and `typing`) merges a `Native` member of the base into the tail. That Native
    disappears from the revealed type. `deduped` counts those members.
    """
    members = split_union(annotation)
    if flatten:  # S10: the ty probe sees the flattened union; the runtime gate (typing) does not
        members = list(flatten_annotated(members))
    base = members[:-3] if members[-3:] == ["ConfigRef", "Native", "UnsetType"] else members
    native = sum(len(re.findall(r"\bNative\b", m)) for m in base)
    json_ = sum(len(re.findall(r"\b(?:JsonValue|NixValue)\b", m)) for m in base)  # S10: both aliases
    top = sum(1 for m in base if m == "Native")
    deduped = top - 1 if top and top == len(base) else top
    return base, native, deduped, json_
