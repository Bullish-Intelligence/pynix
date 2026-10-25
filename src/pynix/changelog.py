"""Render the changelog of a `pynix` release from the manifests of two releases.

Port of 008 A7 `changelog.py` (the manifest diff and the renderer). Two changes from A7. The input is the pooled
manifest of each library (NixOS, Home Manager, flake-parts), so the text has one block per library. The package part
compares the package-name lists (`pynix_pkgs/names.json`) of the two releases. A7 compared the closures of a
minimal system with `nix store diff-closures`. That needs both nixpkgs revisions in the store, so this port leaves it
out. The text has no version changes of packages.

Usage (the release job calls it):
    python -m pynix.changelog --inputs INPUTS.json --manifests DIR --names FILE \
        [--prev-inputs INPUTS.json --prev-manifests DIR --prev-names FILE] \
        [--nixpkgs-src DIR] [--hm-src DIR] [--diff-json OUT.json]
INPUTS.json is `provenance/inputs.json` of a release. The text goes to standard output.
"""

import argparse
import json
import sys
import textwrap
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from pynix.manifest import aliases, option_types

MAX_LINES = 40
WIDTH = 100
LIBRARIES = (
    ("nixos", "NixOS", "nixos/modules"),
    ("home-manager", "Home Manager", "modules"),
    ("flake-parts", "flake-parts", ""),
)


def group(path: str) -> str:
    return ".".join(path.split(".")[:2])


def diff_options(old: dict[str, str], cur: dict[str, str], alias_pairs: set[tuple[str, str]]) -> dict:
    """Added, removed, type changed, and renamed options. A rename is a literal alias pair of the new source."""
    old_names, cur_names = set(old), set(cur)
    added = sorted(cur_names - old_names)
    removed = sorted(old_names - cur_names)
    type_changed = [(n, old[n], cur[n]) for n in sorted(old_names & cur_names) if old[n] != cur[n]]
    added_set, removed_set = set(added), set(removed)
    renames = sorted((a, b) for a, b in alias_pairs if a in removed_set and b in added_set)
    return {"added": added, "removed": removed, "type_changed": type_changed, "renamed": renames}


def diff_names(old: dict[str, object], cur: dict[str, object]) -> dict[str, list[str]]:
    """Added and removed package names."""
    return {"added": sorted(set(cur) - set(old)), "removed": sorted(set(old) - set(cur))}


def short(text: str, width: int) -> str:
    return text if len(text) <= width else text[: width - 3] + "..."


def type_change(old: str, new: str, width: int = 44) -> str:
    """Show a short type change. A long type shows only the words that differ."""
    if len(old) <= 40 and len(new) <= 40:
        return f"{old} -> {new}"
    a, b = old.split(" "), new.split(" ")
    head = 0
    while head < min(len(a), len(b)) and a[head] == b[head]:
        head += 1
    tail = 0
    while tail < min(len(a), len(b)) - head and a[-1 - tail] == b[-1 - tail]:
        tail += 1
    mid_a = " ".join(a[head : len(a) - tail])
    mid_b = " ".join(b[head : len(b) - tail])
    if head == 0 and tail == 0:
        return f"{short(old, width)} -> {short(new, width)}"
    if not mid_a:
        return f"adds {short(mid_b, width)}"
    if not mid_b:
        return f"drops {short(mid_a, width)}"
    return f"{short(mid_a, width)} -> {short(mid_b, width)}"


def day(epoch: int) -> str:
    return datetime.fromtimestamp(epoch, UTC).strftime("%Y-%m-%d")


def gap(a: int, b: int) -> str:
    seconds = b - a
    return f"{seconds // 86400} d {seconds % 86400 // 3600} h"


def wrap(prefix: str, items: list[str], indent: str = "  ") -> list[str]:
    return textwrap.wrap(prefix + ", ".join(items), width=WIDTH, subsequent_indent=indent)


def header(inputs: dict) -> str:
    src = inputs["sources"]
    return (
        f"pynix {inputs['version']} (nixpkgs {src['nixpkgs']['rev'][:7]}, {day(src['nixpkgs']['lastModified'])}; "
        f"Home Manager {src['home-manager']['rev'][:7]}; flake-parts {src['flake-parts']['rev'][:7]})"
    )


def render_first(inputs: dict, counts: dict[str, int], name_count: int) -> list[str]:
    """The text of the first release: there is no previous tag to compare."""
    options = ", ".join(f"{label} {counts[key]}" for key, label, _ in LIBRARIES)
    return [
        header(inputs),
        "Initial release. No previous tag to compare.",
        f"Options: {options}.",
        f"Package names: {name_count}.",
    ]


def render(
    inputs: dict,
    prev: dict,
    counts: tuple[dict[str, int], dict[str, int]],
    diffs: dict[str, dict],
    names: dict[str, list[str]],
    name_counts: tuple[int, int],
    max_lines: int = MAX_LINES,
) -> list[str]:
    """The text of a later release: counts first, then the lists, shortened to fit in MAX_LINES lines."""
    old_n, cur_n = counts
    sp, sc = prev["sources"]["nixpkgs"], inputs["sources"]["nixpkgs"]
    head = [
        header(inputs),
        f"Previous: {prev['version']} (nixpkgs {sp['rev'][:7]}, {day(sp['lastModified'])}). "
        f"Gap: {gap(sp['lastModified'], sc['lastModified'])}.",
    ]
    for key, label, _ in LIBRARIES:
        d = diffs[key]
        head.append(
            f"{label} options: {old_n[key]} -> {cur_n[key]}. Added {len(d['added'])}, removed {len(d['removed'])}, "
            f"type changed {len(d['type_changed'])}, renamed {len(d['renamed'])}."
        )
    head.append(
        f"Package names: {name_counts[0]} -> {name_counts[1]}. Added {len(names['added'])}, removed {len(names['removed'])}."
    )

    def sections(limit: dict[str, int]) -> list[str]:
        out: list[str] = []
        for key, label, _ in LIBRARIES:
            d = diffs[key]
            if not any(d[k] for k in ("added", "removed", "type_changed", "renamed")):
                continue
            out.append(f"{label}:")
            if d["renamed"]:
                out.append(" Renamed (also counted in added and removed):")
                out += [f"  {a} -> {b}" for a, b in d["renamed"][: limit["renamed"]]]
                more = len(d["renamed"]) - limit["renamed"]
                if more > 0:
                    out.append(f"  +{more} more")
            for word, paths, lim in (("Removed", d["removed"], "removed"), ("Added", d["added"], "added")):
                if paths:
                    groups = Counter(group(p) for p in paths).most_common()
                    shown = [f"{g} {n}" for g, n in groups[: limit[lim]]]
                    if len(groups) > limit[lim]:
                        shown.append(f"+{len(groups) - limit[lim]} more subtrees")
                    out += wrap(f" {word} ({len(paths)} options, {len(groups)} subtrees): ", shown, "   ")
            if d["type_changed"]:
                out.append(" Type changed:")
                for path, old, new in d["type_changed"][: limit["types"]]:
                    out.append(f"  {path}: {type_change(old, new)}")
                more = len(d["type_changed"]) - limit["types"]
                if more > 0:
                    out.append(f"  +{more} more")
        for word in ("added", "removed"):
            if names[word]:
                shown = names[word][: limit["packages"]]
                more = len(names[word]) - len(shown)
                out += wrap(
                    f"Package names {word} ({len(names[word])}): ", shown + ([f"+{more} more"] if more > 0 else [])
                )
        return out

    limit = {"renamed": 10, "removed": 8, "added": 8, "types": 20, "packages": 20}
    while len(head) + len(sections(limit)) > max_lines:
        # Shrink the longest list first. Keep one entry per list.
        key = max((k for k in limit if limit[k] > 1), key=lambda k: limit[k], default=None)
        if key is None:
            raise ValueError("the changelog does not fit in max_lines")
        limit[key] -= 1
    lines = head + sections(limit)
    if len(lines) > max_lines:
        raise ValueError(f"the changelog has {len(lines)} lines, more than {max_lines}")
    return lines


def load_side(manifests: Path) -> dict[str, dict[str, str]]:
    return {key: option_types(json.loads((manifests / f"{key}.json").read_text())) for key, _, _ in LIBRARIES}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m pynix.changelog", description=__doc__.split("\n\n")[0])
    ap.add_argument("--inputs", type=Path, required=True)
    ap.add_argument("--manifests", type=Path, required=True)
    ap.add_argument("--names", type=Path, required=True)
    ap.add_argument("--prev-inputs", type=Path)
    ap.add_argument("--prev-manifests", type=Path)
    ap.add_argument("--prev-names", type=Path)
    ap.add_argument("--nixpkgs-src", type=Path, help="nixpkgs source, for the rename pairs of NixOS")
    ap.add_argument("--hm-src", type=Path, help="Home Manager source, for the rename pairs")
    ap.add_argument("--diff-json", type=Path, help="write the structured diff here")
    ap.add_argument("--max-lines", type=int, default=MAX_LINES)
    args = ap.parse_args(argv)

    inputs = json.loads(args.inputs.read_text())
    cur = load_side(args.manifests)
    cur_names = json.loads(args.names.read_text())
    counts = {key: len(cur[key]) for key in cur}
    if args.prev_inputs is None:
        print("\n".join(render_first(inputs, counts, len(cur_names))))
        return 0
    if args.prev_manifests is None or args.prev_names is None:
        ap.error("--prev-inputs needs --prev-manifests and --prev-names")
    prev = json.loads(args.prev_inputs.read_text())
    old = load_side(args.prev_manifests)
    old_names = json.loads(args.prev_names.read_text())
    roots = {"nixos": args.nixpkgs_src, "home-manager": args.hm_src}
    diffs: dict[str, dict] = {}
    for key, _, subdir in LIBRARIES:
        root = roots.get(key)
        pairs = aliases(root, subdir) if root else set()
        diffs[key] = diff_options(old[key], cur[key], pairs)
    names = diff_names(old_names, cur_names)
    lines = render(
        inputs,
        prev,
        ({k: len(v) for k, v in old.items()}, counts),
        diffs,
        names,
        (len(old_names), len(cur_names)),
        args.max_lines,
    )
    print("\n".join(lines))
    if args.diff_json:
        args.diff_json.write_text(
            json.dumps({"libraries": diffs, "package_names": names}, indent=1, sort_keys=True) + "\n"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
