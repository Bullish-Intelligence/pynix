"""Write the package-name stub of one nixpkgs.

Types: `pkgs.pyi`, and one stub file `sets/NAME.pyi` for each curated package set. Name lists: `names.json` (the top
level), `sets.json` (the index of the package sets), and `sets/ATTR.json` (the members of one set, for every set).

Copy of 009 SV4 `src/gen_pkgs.py` (stub mode), extended by 009 SG36 `gen_nested.py` (shape b, 009-D43). The runtime of
`pynix_pkgs` (`pkgs.py`, `_pkgref.py`) is hand-written and stays in the repository. Learner text says "the package list",
not "nixpkgs" (009-D35).

Usage: python gen_pkgs.py META_JSON SETS_JSON CURATED_FILE OUTDIR

- META_JSON: the top-level names, `{name: {kind, main, desc}}` (`nix/pkgs-meta.nix`).
- SETS_JSON: the members of each package set, `{set: {member: {main, desc}}}` (`nix/pkgs-sets.nix`). A member is a package.
- CURATED_FILE: one package set attribute per line. These sets get a stub file (class `PackageSet_NAME`), so ty checks
  and completes their members. Every other set is declared as a `PkgSet`: ty accepts it and does not check its members.
"""

import json
import keyword
import re
import sys
from collections import Counter
from pathlib import Path


def pyname(attr: str) -> str:
    """The Python name of a nixpkgs attribute: a character that is not allowed becomes `_`; a keyword gets `_`."""
    name = re.sub(r"[^0-9A-Za-z_]", "_", attr)
    if name[:1].isdigit():
        name = "_" + name
    if keyword.iskeyword(name):
        name += "_"
    return name


def doc(entry: dict) -> str:
    text = " ".join((entry.get("desc") or "").split()).replace("\\", "\\\\").replace('"', "'")
    main = entry.get("main")
    if main:
        text += ("" if text.endswith((".", "!", "?")) or not text else ".") + f" Runs as `{main}`."
    return text.strip()


def table(meta: dict) -> tuple[dict[str, list], dict[str, list], list[str], Counter[str]]:
    """The names of one level: `(every name, the kept names, the attributes that lost a collision, counts)`.

    A name is `{python_name: [attr, has_main_program]}`. A name that is already an identifier wins a collision. A
    collision stays reachable by its attribute (`pkgs["a-b"]`), so the first table keeps it under that attribute.
    """
    rows: dict[str, list] = {}
    stats: Counter[str] = Counter()
    # A name that is already an identifier wins a collision.
    for attr in sorted(meta, key=lambda a: (a != pyname(a), a)):
        name = pyname(attr)
        if name in rows:
            stats["collide"] += 1
            continue
        if name != attr:
            stats["renamed"] += 1
        if keyword.iskeyword(attr):
            stats["keyword"] += 1
        rows[name] = [attr, 1 if meta[attr].get("main") else 0]
    kept = {row[0] for row in rows.values()}
    skipped = [a for a in sorted(meta) if a not in kept]
    return {**rows, **{a: [a, 1 if meta[a].get("main") else 0] for a in skipped}}, rows, skipped, stats


def stub_lines(rows: dict[str, list], meta: dict, indent: str, prefix: str = "") -> str:
    """The attribute lines of a stub class. `prefix` goes before the type names: a set can hold a package that is named
    `Pkg` or `str`, and such a name would hide the type in the class body."""
    text = ""
    for name, row in rows.items():
        attr, has_main = row[0], row[1]
        text += f"{indent}{name}: {prefix}{'PyInterp' if len(row) > 2 else 'Prog' if has_main else 'Pkg'}\n"
        if doc(meta[attr]):
            text += f'{indent}"""{doc(meta[attr])}"""\n'
    return text


def main() -> None:
    meta_file, sets_file, curated_file, out = sys.argv[1], sys.argv[2], sys.argv[3], Path(sys.argv[4])
    top = {n: v for n, v in json.loads(Path(meta_file).read_text()).items() if v["kind"] == "drv"}
    set_meta: dict[str, dict] = json.loads(Path(sets_file).read_text())
    curated = [line.strip() for line in Path(curated_file).read_text().splitlines() if line.strip()]
    out.mkdir(parents=True, exist_ok=True)
    (out / "sets").mkdir(exist_ok=True)
    top_all, top_rows, skipped, stats = table(top)

    # A set name that a package already has stays a package.
    sets_json: dict[str, list] = {}
    set_rows: dict[str, dict] = {}
    for attr in sorted(set_meta):
        full, rows, _, _ = table(set_meta[attr])
        name = pyname(attr)
        if name in top_rows or name in sets_json:
            print("set name collides:", attr, file=sys.stderr)
            continue
        sets_json[name] = [attr, len(rows)]
        set_rows[attr] = rows
        (out / "sets" / f"{attr}.json").write_text(json.dumps(full, separators=(",", ":"), sort_keys=True))
    missing = [a for a in curated if a not in set_rows]
    if missing:
        raise SystemExit(f"gen_pkgs: the curated sets {missing} are not package sets of this nixpkgs")

    # A Python interpreter has a package set of the same version (`python3` and `python3Packages`): `with_packages`.
    interpreters = {a for a in top if a.startswith(("python", "pypy")) and a + "Packages" in set_rows}
    for row in top_all.values():  # `top_rows` shares these rows
        if row[0] in interpreters:
            row.append(1)
    (out / "names.json").write_text(json.dumps(top_all, separators=(",", ":"), sort_keys=True))
    (out / "sets.json").write_text(json.dumps(sets_json, separators=(",", ":"), sort_keys=True))

    # The stubs. An interpreter has `with_packages` in the stub only when the stub holds its package set too.
    stub_rows = {
        n: row if row[0] not in interpreters or row[0] + "Packages" in curated else row[:2]
        for n, row in top_rows.items()
    }
    (out / "sets" / "__init__.pyi").write_text("")
    head = '"""Generated: the packages of the package list. Do not edit."""\n\n'
    imports = ""
    for attr in curated:
        # The text is clean for ruff (stub style), so the stub needs no entry in the ruff settings.
        uses_prog = any(row[1] for row in set_rows[attr].values())
        text = head + "from builtins import str as _str\n\nfrom .._pkgref import Pkg as _Pkg\n"
        text += "from .._pkgref import Prog as _Prog\n\n" if uses_prog else "\n"
        text += f"class PackageSet_{pyname(attr)}:\n    def __getitem__(self, attr: _str) -> _Pkg: ...\n"
        text += stub_lines(set_rows[attr], set_meta[attr], "    ", "_")
        (out / "sets" / f"{pyname(attr)}.pyi").write_text(text)
        imports += f"from .sets.{pyname(attr)} import PackageSet_{pyname(attr)}\n"
    names = "Pkg, Prog, PyInterp" if any(len(row) > 2 for row in stub_rows.values()) else "Pkg, Prog"
    body = head + f"from ._pkgref import {names}\nfrom ._pkgref import PkgSet as _PkgSet\n{imports}"
    body += "\n\nclass Pkgs:\n    def __getitem__(self, attr: str) -> Pkg: ...\n" + stub_lines(stub_rows, top, "    ")
    for attr in curated:
        body += f"    {pyname(attr)}: PackageSet_{pyname(attr)}\n"
    # A set outside the curated list has no stub of its own. It is a `PkgSet`: ty accepts the set and any member, and
    # the compile check (`names.json`, `sets/ATTR.json`) names a wrong member. (010-D12)
    plain_sets = [name for name, (attr, _) in sets_json.items() if attr not in curated]
    for name in plain_sets:
        body += f"    {name}: _PkgSet\n"
    (out / "pkgs.pyi").write_text(body + "\n\npkgs: Pkgs\n")
    summary = {
        "packages": len(top_rows),
        "drvs": len(top),
        "renamed": stats["renamed"],
        "collide": stats["collide"],
        "keyword": stats["keyword"],
        "skipped_collision": skipped[:20],
        "sets": len(sets_json),
        "set_members": sum(v[1] for v in sets_json.values()),
        "curated_sets": len(curated),
        "plain_sets": len(plain_sets),
        "interpreters": sorted(interpreters),
    }
    json.dump(summary, sys.stdout)
    print()


if __name__ == "__main__":
    main()
