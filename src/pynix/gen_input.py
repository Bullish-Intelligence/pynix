"""Write the input package `pynix_NAME` of one flake input (009-D47).

`nix/input-packages.nix` runs this in a derivation, once for each input. It reads two JSON files that Nix writes:

- MANIFEST: the pooled option manifest of the options that the input declares. Its `source` key holds the record that
  the generator writes to `_generation.py` (`input`, `narHash`, `rev`, `nixpkgs`, `generator`, `modules`).
- PACKAGES: the `packages.<system>` output of the input, `{ATTR: {kind, main, desc}}` (the shape of `nix/pkgs-meta.nix`).

The package holds the option classes (made with `--init-nested`, so ty checks a nested value too), the name stub
`pkgs.py`, `pkgs.pyi`, and `names.json`, and `_generation.py`. An input that declares no option gets the name stub only.

Usage: python -m pynix.gen_input MANIFEST PACKAGES OUTDIR NAME

Standard library only: the build runs it with a plain Python.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path
from shutil import copytree

from .gen_pkgs import doc, table
from .generate import Generator

__all__ = ["GenerateInput", "generate", "input_package_name", "name_input", "write_flat_init", "write_names"]

FORMAT = "nixdantic-option-manifest-v4-type-table-once-pool"


def input_package_name(name: str) -> str:
    """The Python package of the input `NAME`: `pynix_NAME`. The same rule as `pynix_native.input_package_name`."""
    return "pynix_" + name.replace("-", "_")


def name_input(docstring: str, name: str, fallback: str) -> str:
    """Put the input into the first line of a class docstring: "Options below `a.b`." becomes "... `a.b` (input `x`).".

    A class with no docstring gets "Options of CLASS." first.
    """
    first, newline, rest = (docstring or f"Options of {fallback}.").partition("\n")
    first = first.rstrip()
    mark = f" (input `{name}`)"
    first = first[:-1] + mark + "." if first.endswith(".") else first + mark
    return first + newline + rest


class GenerateInput(Generator):
    """The generator of the option classes, with `--init-nested` on and the input named in each class docstring."""

    def __init__(self, manifest: dict, package: str, input_name: str):
        super().__init__(manifest, package, f"{package} (input {input_name})", init_nested=True)
        self.input_name = input_name

    def emit_class(self, name: str, docstring: str, *args, **kwargs) -> None:
        super().emit_class(name, name_input(docstring, self.input_name, name), *args, **kwargs)


def write_names(meta: dict[str, dict], pkg: Path, name: str) -> dict:
    """Write the name stub of `packages.<system>`: `pkgs.py`, `pkgs.pyi`, `names.json` (009-D47).

    The entry reads `from pynix_NAME.pkgs import NAME_pkgs`, then `NAME_pkgs.attr`. Only a derivation gets a name. A name
    that collides (`a-b` and `a_b`) stays reachable by its attribute, as in the name list of a nixpkgs.
    """
    drvs = {attr: value for attr, value in meta.items() if value.get("kind") == "drv"}
    every, rows, _skipped, _stats = table(drvs)
    ident = re.sub(r"\W", "_", name)
    obj = f"{ident}_pkgs"
    cls = "".join(word.capitalize() for word in ident.split("_")) + "Packages"
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "names.json").write_text(json.dumps(every, separators=(",", ":"), sort_keys=True))
    (pkg / "pkgs.py").write_text(
        f'"""Generated: the packages of the input `{name}`. The names are in names.json. Do not edit."""\n\n'
        f'from pynix_native import InputPackages\n\n__all__ = ["{obj}"]\n\n{obj} = InputPackages("{name}", __file__)\n'
    )
    lines = [
        f'"""Generated: the packages of the input `{name}`. Do not edit."""\n\nfrom pynix_native import InputPkg, InputProg\n\n\n',
        f"class {cls}:\n    def __getitem__(self, attr: str) -> InputPkg: ...\n",
    ]
    for python_name, (attr, has_main) in rows.items():
        lines.append(f"    {python_name}: {'InputProg' if has_main else 'InputPkg'}\n")
        text = doc(drvs[attr])
        if text:
            lines.append(f'    """{text}"""\n')
    lines.append(f"\n\n{obj}: {cls}\n")
    (pkg / "pkgs.pyi").write_text("".join(lines))
    return {"object": obj, "packages": len(rows), "names": len(every)}


def write_flat_init(pkg: Path) -> None:
    """Give the package every class by name, so `import pynix_NAME as x`, then `x.Class(...)` works (009-D50).

    The import lines are the type-checking block of the generated `all.py`. An input package is small, so the package
    imports every module at once; the shipped libraries stay lazy.
    """
    text = (pkg / "all.py").read_text().splitlines()
    start = next(i for i, line in enumerate(text) if line.startswith("if _TYPE_CHECKING:")) + 1
    lines: list[str] = []
    for line in text[start:]:
        if line and not line.startswith(" "):  # `else:` or the next top-level statement ends the block
            break
        lines.append(line[4:])
    doc = f'"""The option classes of the input package `{pkg.name}`. Generated; do not edit.\n\n'
    doc += f'`import {pkg.name} as x`, then `x.Class(...)`.\n"""'
    (pkg / "__init__.py").write_text(doc + "\n\n" + "\n".join(lines).strip() + "\n")


def write_empty(pkg: Path, manifest: dict) -> None:
    """The package of an input that declares no option: no class, only the record and the marker (SG44)."""
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "py.typed").write_text("")
    (pkg / "__init__.py").write_text('"""The input declares no option: this package holds its package names only."""\n')
    (pkg / "_generation.py").write_text(
        '"""The source of this generated package."""\n\n'
        f"SOURCE: dict[str, str] = {dict(sorted(manifest.get('source', {}).items()))!r}\n"
        f"FORMAT: str = {manifest.get('format', FORMAT)!r}\n"
    )


def generate(manifest: dict, packages: dict[str, dict], out: Path, name: str) -> dict:
    """Write `OUT/pynix_NAME`. Returns a summary: the module, the class count, and the package names."""
    package = input_package_name(name)
    # The generator writes its summary files beside the package, so it writes into a scratch folder first.
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        if manifest["options"]:
            summary = GenerateInput(manifest, package, name).run(work)
            write_flat_init(work / package)
        else:
            write_empty(work / package, manifest)
            summary = {"package": package, "roots": 0, "rootsKept": 0, "modules": 0}
        names = write_names(packages, work / package, name)
        copytree(work / package, out / package)
    return {"package": package, "roots": summary["rootsKept"], "modules": summary["modules"], **names}


def main() -> None:
    if len(sys.argv) != 5:
        sys.exit("usage: python -m pynix.gen_input MANIFEST PACKAGES OUTDIR NAME")
    manifest = json.loads(Path(sys.argv[1]).read_text())
    packages = json.loads(Path(sys.argv[2]).read_text())
    print(json.dumps(generate(manifest, packages, Path(sys.argv[3]), sys.argv[4])))


if __name__ == "__main__":
    main()
