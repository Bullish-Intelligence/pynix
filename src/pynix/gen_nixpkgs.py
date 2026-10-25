"""Write the package-name list of one pinned nixpkgs: the package `pynix_nixpkgs_NAME` (009-D54).

A `NixpkgsPin("old", "COMMIT")` in an entry gives `old.pkgs.NAME`. The compiler checks `NAME` against `names.json`. ty reads
`__init__.pyi` when an entry imports the list with `from pynix_nixpkgs_old import pkgs`.

The package holds:

- `__init__.py`: `pkgs = NixpkgsPackages("old")`.
- `__init__.pyi`: one typed name for each package (`NixpkgsPkg`, or `NixpkgsProg` for a main program).
- `names.json`: `{python_name: [attr, has_main_program]}`. A name that collides stays reachable by its attribute.
- `_generation.py`: `SOURCE` with the commit, the narHash, the name, and the generator version. The pair check reads it.

Adapted from SG44 `gen_nixpkgs_pkgs.py`, and from `gen_pkgs.py` for the collision rules. Usage:
`python -m pynix.gen_nixpkgs LIST.json OUTDIR NAME [--docs]`, where LIST.json is the output of `nix/nixpkgs-names.nix`.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

from pynix.gen_pkgs import doc, pyname

__all__ = ["GENERATOR", "generate", "list_names", "names_expression", "nixpkgs_package_name"]

GENERATOR = "nixpkgs-names-1"
"""The version of this generator. It equals `pynix_native.NAMES_GENERATOR`; a test checks that. Raise both together.

The module needs the standard library only, because `nix/input-packages.nix` runs it with a plain Python. It must not
import `pynix_native`, which needs pydantic.
"""


def nixpkgs_package_name(name: str) -> str:
    """The Python package of the name list of `NixpkgsPin(name, ...)`. The same rule as `pynix_native.nixpkgs_package_name`."""
    return "pynix_nixpkgs_" + name.replace("-", "_")


NAMES_NIX = Path(__file__).resolve().parents[2] / "nix" / "nixpkgs-names.nix"
"""The Nix file in a source tree. A caller from an installed package passes the path from the flake."""


def names_expression(locked: dict, nix_file: Path = NAMES_NIX, system: str = "x86_64-linux") -> str:
    """The Nix expression for `nix eval --json --impure`. `locked` is the `locked` part of the lock node `nixpkgs-NAME`.

    `fetchTree` checks the narHash of the node, so a changed source stops here.
    """
    node = json.dumps({k: v for k, v in locked.items() if k != "dir"})
    return (
        f"let locked = builtins.fromJSON ''{node}'';\n"
        f"    src = builtins.fetchTree locked;\n"
        f'in import {nix_file} {{ legacyPackages = import src {{ system = "{system}"; }}; source = locked; }}'
    )


def list_names(locked: dict, nix_file: Path = NAMES_NIX, system: str = "x86_64-linux", offline: bool = False) -> dict:
    """Run `nix eval` on `names_expression` and return the list. It takes about 17 s and 1.8 GB for a full nixpkgs."""
    command = ["nix", "eval", "--json", "--impure", "--expr", names_expression(locked, nix_file, system)]
    if offline:
        command.insert(2, "--offline")
    done = subprocess.run(command, capture_output=True, text=True)
    if done.returncode:
        raise RuntimeError(f"nix eval of the package list failed:\n{done.stderr[-800:]}")
    return json.loads(done.stdout)


def _rows(meta: dict[str, dict]) -> tuple[dict[str, list], dict[str, list]]:
    """The typed rows, and all rows. A name that is already an identifier wins a collision; the rest stay by attribute."""
    drvs = sorted(n for n, v in meta.items() if v["kind"] == "drv")
    rows: dict[str, list] = {}
    for attr in sorted(drvs, key=lambda a: (a != pyname(a), a)):
        rows.setdefault(pyname(attr), [attr, 1 if meta[attr].get("main") else 0])
    kept = {r[0] for r in rows.values()}
    rest = {a: [a, 1 if meta[a].get("main") else 0] for a in drvs if a not in kept}
    return rows, {**rows, **rest}


def generate(data: dict, out: Path, name: str, docs: bool = False) -> dict:
    """Write `OUT/pynix_nixpkgs_NAME` from the output of `nixpkgs-names.nix`. Returns a summary."""
    package = nixpkgs_package_name(name)
    source = data["source"]
    meta = data["packages"]
    rows, every = _rows(meta)
    pkg = out / package
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "py.typed").write_text("")
    (pkg / "names.json").write_text(json.dumps(every, separators=(",", ":"), sort_keys=True))
    (pkg / "__init__.py").write_text(
        f'"""Generated: the packages of the nixpkgs `{name}` (commit {source["commit"]}). '
        'The names are in names.json. Do not edit."""\n\n'
        f'from pynix_native import NixpkgsPackages\n\n__all__ = ["pkgs"]\n\npkgs = NixpkgsPackages("{name}")\n'
    )
    record = {"commit": source["commit"], "generator": GENERATOR, "name": name, "narHash": source["narHash"]}
    body = "".join(f"    {json.dumps(key)}: {json.dumps(value)},\n" for key, value in sorted(record.items()))
    (pkg / "_generation.py").write_text(
        f'"""The source of this generated package."""\n\nSOURCE: dict[str, str] = {{\n{body}}}\n'
    )
    cls = "".join(w.capitalize() for w in name.split("-")) + "Packages"
    lines = [
        f'"""Generated: the packages of the nixpkgs `{name}`. Do not edit."""\n\n'
        "from pynix_native import NixpkgsPkg, NixpkgsProg\n\n\n",
        f"class {cls}:\n    def __getitem__(self, attr: str) -> NixpkgsPkg: ...\n",
    ]
    for python_name, (attr, has_main) in rows.items():
        lines.append(f"    {python_name}: {'NixpkgsProg' if has_main else 'NixpkgsPkg'}\n")
        text = doc(meta[attr]) if docs else ""
        if text:
            lines.append(f'    """{text}"""\n')
    lines.append(f"\n\npkgs: {cls}\n")
    (pkg / "__init__.pyi").write_text("".join(lines))
    return {
        "module": package,
        "packages": len(rows),
        "names": len(every),
        "names_json_bytes": (pkg / "names.json").stat().st_size,
        "pyi_bytes": (pkg / "__init__.pyi").stat().st_size,
    }


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 3:
        sys.exit("usage: python -m pynix.gen_nixpkgs LIST.json OUTDIR NAME [--docs]")
    start = time.monotonic()
    summary = generate(json.loads(Path(args[0]).read_text()), Path(args[1]), args[2], "--docs" in sys.argv)
    print(json.dumps({**summary, "seconds": round(time.monotonic() - start, 2)}))


if __name__ == "__main__":
    main()
