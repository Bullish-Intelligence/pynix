"""Read an option manifest for the changelog of a release.

Port of 008 A7 `manifest.py`. The A7 code read `options.json`. This code reads the pooled manifest of the option walk
(`nix/evaluate.nix`): one record per option, each with a `path` and a `type` index into the type table. `aliases` is
unchanged in logic.
"""

import re
from pathlib import Path

PLACEHOLDER = "__nixdantic_placeholder__"
DEPTH = 4


def type_text(types: list[dict], tid: int, depth: int = 0) -> str:
    """A short text for a type. Container types have no description, so build it from the element types."""
    t = types[tid]
    if t.get("description"):
        return str(t["description"])
    nested = t.get("nested", {})
    name = t.get("name") or t.get("ctor") or "type"
    if depth >= DEPTH:
        return str(name)
    inner = [type_text(types, i, depth + 1) for i in nested.values()]
    if name == "nullOr" and inner:
        return f"null or {inner[0]}"
    if name == "listOf" and inner:
        return f"list of {inner[0]}"
    if name in {"attrsOf", "lazyAttrsOf"} and inner:
        return f"attribute set of {inner[0]}"
    if inner:
        return f"{name} of ({', '.join(inner)})"
    return str(name)


def option_types(manifest: dict) -> dict[str, str]:
    """Map the dotted path of each option to its type text. A path that occurs twice joins the texts with ` | `."""
    types = manifest["types"]
    seen: dict[str, list[str]] = {}
    for record in manifest["optionPool"]:
        name = ".".join(p.replace(PLACEHOLDER, "<name>") for p in record["path"])
        text = type_text(types, record["type"])
        texts = seen.setdefault(name, [])
        if text not in texts:
            texts.append(text)
    return {name: " | ".join(sorted(texts)) for name, texts in sorted(seen.items())}


_ALIAS = re.compile(
    r"(?:lib\.)?(?:modules\.)?mk(?:Renamed|Alias)OptionModule\s+\[([^\]]+)\]\s+\[([^\]]+)\]",
    re.MULTILINE | re.DOTALL,
)


def aliases(root: Path, subdir: str) -> set[tuple[str, str]]:
    """The literal `mkRenamedOptionModule` and `mkAliasOptionModule` pairs below ROOT/SUBDIR."""
    result: set[tuple[str, str]] = set()
    for file in sorted(Path(root, subdir).rglob("*.nix")):
        source = file.read_text(errors="replace")
        for old, new in _ALIAS.findall(source):
            old_path = re.findall(r'"([^"]+)"', old)
            new_path = re.findall(r'"([^"]+)"', new)
            if old_path and new_path:
                result.add((".".join(old_path), ".".join(new_path)))
    return result
