#!/usr/bin/env python3
"""Compare the pins of two layers: nixpkgs, `pynix`, and Home Manager.

Usage:
    compare_layers.py LOCK_A LOCK_B [--names NAME_A,NAME_B] [--json]

Each LOCK is a `flake.lock` file or a folder that holds one. The script reads the root inputs `nixpkgs` and
`pynix` of each lock, and the root input `home-manager` when a lock has it. It prints one line per item. It
prints a `warning:` line for each difference.

The script blocks nothing (BSX-389, 009-D28). It exits 0 with or without differences. It exits 2 on wrong use or
on a lock that it cannot read. The code names no layer repository: the labels come from `--names`.

Stdlib only (010-D33).
"""

import argparse
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

TAG_PREFIX = "refs/tags/"
# `pynix-v0.1.0-rc.3` or `v0.1.0`: the prefix is free, the version is `X.Y.Z` with an optional `-rc.N`.
VERSION = re.compile(r"^(?:.*?-)?v?(\d+)\.(\d+)\.(\d+)(?:-rc\.(\d+))?$")
SHORT = 7


class LockError(Exception):
    """A lock that the script cannot read."""


def read_lock(path: str) -> dict:
    """Read a `flake.lock` file, or the `flake.lock` in a folder."""
    target = Path(path)
    if target.is_dir():
        target = target / "flake.lock"
    try:
        data = json.loads(target.read_text())
    except (OSError, ValueError) as error:
        raise LockError(f"cannot read the lock {target}: {error}") from error
    if not isinstance(data, dict) or not isinstance(data.get("nodes"), dict) or "root" not in data:
        raise LockError(f"{target} is not a flake.lock file")
    return data


def resolve(lock: dict, name: str) -> dict | None:
    """Return the node of the root input `name`, or None. A `follows` list leads to the node it names."""
    nodes = lock["nodes"]
    root = nodes.get(lock["root"])
    ref = root.get("inputs", {}).get(name) if isinstance(root, dict) else None
    if isinstance(ref, list):
        key = lock["root"]
        for step in ref:
            node = nodes.get(key)
            nxt = node.get("inputs", {}).get(step) if isinstance(node, dict) else None
            if nxt is None:
                return None
            key = nxt
        ref = key
    node = nodes.get(ref) if isinstance(ref, str) else None
    return node if isinstance(node, dict) and isinstance(node.get("locked"), dict) else None


def day(seconds: object) -> str | None:
    if not isinstance(seconds, int):
        return None
    return datetime.fromtimestamp(seconds, UTC).strftime("%Y-%m-%d")


def pin(lock: dict, name: str) -> dict | None:
    """The rev, the date, and the tag (if any) of a root input."""
    node = resolve(lock, name)
    if node is None:
        return None
    locked = node["locked"]
    original = node.get("original", {})
    ref = original.get("ref") or locked.get("ref")
    tag = ref.removeprefix(TAG_PREFIX) if isinstance(ref, str) and ref.startswith(TAG_PREFIX) else None
    return {"rev": locked.get("rev"), "date": day(locked.get("lastModified")), "tag": tag}


def short_rev(rev: object) -> str:
    return rev[:SHORT] if isinstance(rev, str) else "unknown"


def describe(label: str, value: dict | None, with_tag: bool = False) -> str:
    if value is None:
        return f"{label} has no pin"
    text = short_rev(value["rev"])
    if with_tag:
        text = f"{value['tag'] or 'no tag'} {text}"
    if value["date"] and not with_tag:
        text += f" ({value['date']})"
    return f"{label} {text}"


def version_key(tag: str | None) -> tuple[int, int, int, float] | None:
    """The order key of a tag. A release candidate sorts before its release."""
    match = VERSION.match(tag or "")
    if not match:
        return None
    major, minor, patch, candidate = match.groups()
    return (int(major), int(minor), int(patch), float("inf") if candidate is None else int(candidate))


def same(a: dict | None, b: dict | None, with_tag: bool) -> bool:
    if a is None or b is None:
        return False
    if with_tag and a["tag"] != b["tag"]:
        return False
    return a["rev"] == b["rev"]


def compare_nixpkgs(names: tuple[str, str], pins: tuple[dict | None, dict | None]) -> tuple[str, list[str]]:
    first, second = names
    line = f"nixpkgs: {describe(first, pins[0])}, {describe(second, pins[1])}"
    if pins[0] is None or pins[1] is None:
        missing = first if pins[0] is None else second
        return f"{line}: missing", [f"warning: nixpkgs: the lock of {missing} has no nixpkgs pin"]
    if same(pins[0], pins[1], False):
        return f"{line}: equal", []
    warning = f"warning: nixpkgs differs: {first} {short_rev(pins[0]['rev'])}, {second} {short_rev(pins[1]['rev'])}."
    dates = (pins[0]["date"], pins[1]["date"])
    if dates[0] and dates[1] and dates[0] != dates[1]:
        older = first if dates[0] < dates[1] else second
        warning += f" {older} has the older nixpkgs. Update the nixpkgs pin of {older}."
    return f"{line}: differ", [warning]


def compare_pynix(names: tuple[str, str], pins: tuple[dict | None, dict | None]) -> tuple[str, list[str]]:
    first, second = names
    line = f"pynix: {describe(first, pins[0], True)}, {describe(second, pins[1], True)}"
    if pins[0] is None or pins[1] is None:
        missing = first if pins[0] is None else second
        return f"{line}: missing", [f"warning: pynix: the lock of {missing} has no pynix pin"]
    if same(pins[0], pins[1], True):
        return f"{line}: equal", []
    tags = (pins[0]["tag"], pins[1]["tag"])
    if tags[0] == tags[1]:
        return f"{line}: differ", [
            f"warning: pynix: both layers pin the tag {tags[0] or 'none'} with different revisions "
            f"({first} {short_rev(pins[0]['rev'])}, {second} {short_rev(pins[1]['rev'])})."
        ]
    keys = (version_key(tags[0]), version_key(tags[1]))
    warning = f"warning: pynix tags differ: {first} {tags[0] or 'no tag'}, {second} {tags[1] or 'no tag'}."
    if keys[0] is not None and keys[1] is not None:
        newer, older = (first, second) if keys[0] > keys[1] else (second, first)
        newer_tag = tags[0] if newer == first else tags[1]
        warning += f" {newer} has the newer tag. Release {older} again with {newer_tag}."
    else:
        warning += " The tags have no version order. Pick the newer tag and release the other layer again."
    return f"{line}: differ", [warning]


def note_home_manager(names: tuple[str, str], pins: tuple[dict | None, dict | None]) -> str:
    """Home Manager has no compare. The line shows the pin of each lock that has one."""
    shown = [describe(name, pin_) for name, pin_ in zip(names, pins, strict=True) if pin_ is not None]
    if not shown:
        return "home-manager: no pin in either lock: no compare"
    absent = [name for name, pin_ in zip(names, pins, strict=True) if pin_ is None]
    tail = f"; {' and '.join(absent)} has none" if absent else ""
    return f"home-manager: {', '.join(shown)}{tail}: no compare"


def compare(names: tuple[str, str], locks: tuple[dict, dict]) -> dict:
    """Compare two locks. Return the lines, the warnings, and the pins."""
    nixpkgs = (pin(locks[0], "nixpkgs"), pin(locks[1], "nixpkgs"))
    pynix = (pin(locks[0], "pynix"), pin(locks[1], "pynix"))
    home = (pin(locks[0], "home-manager"), pin(locks[1], "home-manager"))
    lines: list[str] = []
    warnings: list[str] = []
    for line, found in (compare_nixpkgs(names, nixpkgs), compare_pynix(names, pynix)):
        lines.append(line)
        warnings.extend(found)
    lines.append(note_home_manager(names, home))
    return {
        "names": list(names),
        "pins": {
            "nixpkgs": dict(zip(names, nixpkgs, strict=True)),
            "pynix": dict(zip(names, pynix, strict=True)),
            "home-manager": dict(zip(names, home, strict=True)),
        },
        "lines": lines,
        "warnings": warnings,
    }


def parse_names(text: str) -> tuple[str, str]:
    parts = [part.strip() for part in text.split(",")]
    if len(parts) != 2 or not all(parts) or parts[0] == parts[1]:
        raise ValueError("--names needs two different names, separated by a comma")
    return parts[0], parts[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare the nixpkgs and pynix pins of two flake.lock files.")
    parser.add_argument("first", metavar="LOCK_A", help="a flake.lock file, or a folder that holds one")
    parser.add_argument("second", metavar="LOCK_B", help="a flake.lock file, or a folder that holds one")
    parser.add_argument(
        "--names", default="first,second", help="two labels, separated by a comma (default: first,second)"
    )
    parser.add_argument("--json", action="store_true", help="print the result as JSON")
    args = parser.parse_args(argv)  # a usage error exits with 2
    try:
        names = parse_names(args.names)
        result = compare(names, (read_lock(args.first), read_lock(args.second)))
    except (ValueError, LockError) as error:
        print(f"compare_layers: {error}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("\n".join([*result["lines"], *result["warnings"]]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
