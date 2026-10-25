"""Round 4 of the 009 concept: the nested package sets, the name lists, and `with_packages` (009-D43; SG36 probes)."""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

import pynix_pkgs
from nixdantic import supplied
from pynix_pkgs import PackageError, Pkg, PkgSet, Prog, PyEnv, PyInterp, UnknownPackage, pkgs
from pynix_pkgs._pkgref import set_names, sets

PACKAGES = Path(pynix_pkgs.__file__).parent
SRC = PACKAGES.parent
CURATED = [line for line in (SRC / "pynix" / "curated-sets.txt").read_text().split() if line]


def test_a_member_of_a_set_is_a_package() -> None:
    assert isinstance(pkgs.nerd_fonts, PkgSet)
    assert pkgs.nerd_fonts.fira_code.attr == "nerd-fonts.fira-code"
    assert pkgs.nerd_fonts._0xproto.attr == "nerd-fonts._0xproto"  # nixpkgs spells a leading digit this way
    assert pkgs.rocmPackages.amdsmi.attr == "rocmPackages.amdsmi"
    assert isinstance(pkgs.rocmPackages.amdsmi, Prog) and not isinstance(pkgs.nerd_fonts.fira_code, Prog)


def test_dotted_name_gives_the_same_package() -> None:
    assert Pkg("nerd-fonts.fira-code") == pkgs.nerd_fonts.fira_code
    assert isinstance(pkgs["nerd_fonts"], PkgSet)  # the stub types it as `Pkg`; only the stub of a curated set is typed
    assert repr(pkgs.nerd_fonts) == "<the package set `nerd-fonts`>"


def test_unknown_member_says_did_you_mean() -> None:
    with pytest.raises(UnknownPackage) as caught:
        Pkg("nerd-fonts.fira-cod")
    assert str(caught.value) == "The package list has no package `fira-cod` in `nerd-fonts`. Did you mean `fira-code`?"
    assert caught.value.word == "nerd-fonts.fira-cod"  # the compiler puts its column on the whole dotted name


def test_unknown_set_says_did_you_mean() -> None:
    with pytest.raises(UnknownPackage) as caught:
        Pkg("nerd-fontz.fira-code")
    assert str(caught.value) == "The package list has no package `nerd-fontz`. Did you mean `nerd-fonts`?"
    with pytest.raises(UnknownPackage, match="no package `nerd_fontz`. Did you mean `nerd_fonts`"):
        getattr(pkgs, "nerd_fontz")  # noqa: B009


def test_unknown_member_by_attribute_access() -> None:
    with pytest.raises(UnknownPackage, match="no package `amdsm` in `rocmPackages`. Did you mean `amdsmi`"):
        getattr(pkgs.rocmPackages, "amdsm")  # noqa: B009
    with pytest.raises(UnknownPackage, match="no package `requets` in `python3Packages`. Did you mean `requests`"):
        Pkg("python3Packages.requets")


def test_with_packages_wire_value() -> None:
    env = pkgs.python3.with_packages(pkgs.python3Packages.requests, pkgs.python3Packages.pydantic)
    assert isinstance(pkgs.python3, PyInterp) and isinstance(env, PyEnv)
    assert json.dumps(supplied(env)["__nixdantic_ref__"], sort_keys=True, separators=(",", ":")) == (  # ty: ignore[invalid-argument-type, not-subscriptable]
        '{"attr":"python3","kind":"with_packages","packages":["requests","pydantic"]}'
    )


def test_with_packages_takes_libraries_of_its_own_set() -> None:
    with pytest.raises(PackageError) as caught:
        pkgs.python3.with_packages(pkgs.nerd_fonts.fira_code)
    assert (
        str(caught.value)
        == "`python3.with_packages` takes libraries of `python3Packages`, found `nerd-fonts.fira-code`."
    )
    with pytest.raises(PackageError, match="takes libraries of `python312Packages`"):
        pkgs.python312.with_packages(pkgs.python3Packages.requests)


def test_every_set_has_a_name_list() -> None:
    index = sets()
    assert len(index) > 300  # SG36 counted 387 sets with a package at this pin
    for name, (attr, count) in index.items():
        assert (PACKAGES / "sets" / f"{attr}.json").is_file(), name
        assert count > 0
    assert len(set_names("nerd-fonts")) >= 72


def test_the_curated_sets_have_a_stub_and_the_others_do_not() -> None:
    stubs = {path.stem for path in (PACKAGES / "sets").glob("*.pyi")} - {"__init__"}
    assert stubs == {name.replace("-", "_") for name in CURATED}
    text = (PACKAGES / "pkgs.pyi").read_text()
    assert "    nerd_fonts: PackageSet_nerd_fonts\n" in text and "    python3: PyInterp\n" in text
    assert "\nclass PackageSet_nerd_fonts:" in (PACKAGES / "sets" / "nerd_fonts.pyi").read_text()
    assert "    rPackages: _PkgSet\n" in text  # a set that is not curated has no stub file, but ty accepts it (010-D12)
    assert "S_nerd_fonts" not in text.replace("PackageSet_nerd_fonts", "")
    assert text.count(": _PkgSet\n") == len(sets()) - len(CURATED)  # every other set is declared


def test_a_set_that_has_no_stub_still_checks_at_run_time() -> None:
    anywhere: Any = pkgs  # `rPackages` is a plain `PkgSet` in the stub; the run-time check names a wrong member
    assert isinstance(anywhere.rPackages, PkgSet)
    with pytest.raises(UnknownPackage, match="Did you mean `ggplot2`"):
        Pkg("rPackages.ggplot")


def test_gen_pkgs_on_a_small_nixpkgs(tmp_path: Path) -> None:
    meta = {
        "hello": {"kind": "drv", "main": "hello", "desc": "A program."},
        "python3": {"kind": "drv", "main": "python3", "desc": "Python"},
        "alpha-set": {"kind": "set"},
        "beta": {"kind": "set"},
    }
    sets_meta = {
        "python3Packages": {"requests": {"desc": "HTTP"}},
        "alpha-set": {"a-b": {"main": "ab", "desc": 'Text with "quotes"'}, "a_b": {}, "class": {}},
        "beta": {"x": {}},
    }
    (tmp_path / "meta.json").write_text(json.dumps(meta))
    (tmp_path / "sets.json").write_text(json.dumps(sets_meta))
    (tmp_path / "curated.txt").write_text("alpha-set\npython3Packages\n")
    script = SRC / "pynix" / "gen_pkgs.py"
    out = tmp_path / "out"
    run = subprocess.run(
        [
            sys.executable,
            "-I",
            str(script),
            *map(str, (tmp_path / "meta.json", tmp_path / "sets.json", tmp_path / "curated.txt", out)),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    summary = json.loads(run.stdout)
    assert summary["sets"] == 3 and summary["curated_sets"] == 2 and summary["interpreters"] == ["python3"]
    assert json.loads((out / "names.json").read_text()) == {"hello": ["hello", 1], "python3": ["python3", 1, 1]}
    assert sorted(json.loads((out / "sets.json").read_text())) == ["alpha_set", "beta", "python3Packages"]
    # A collision keeps the identifier name, and the other attribute stays reachable by its own name.
    assert json.loads((out / "sets" / "alpha-set.json").read_text()) == {
        "a_b": ["a_b", 0],
        "a-b": ["a-b", 1],
        "class_": ["class", 0],
    }
    stub = (out / "sets" / "alpha_set.pyi").read_text()
    assert "class PackageSet_alpha_set:" in stub and "    a_b: _Pkg\n" in stub and "    class_: _Pkg\n" in stub
    assert not (out / "sets" / "beta.pyi").exists()
    top = (out / "pkgs.pyi").read_text()
    assert "    python3: PyInterp\n" in top and "    alpha_set: PackageSet_alpha_set\n" in top
    assert "    beta: _PkgSet\n" in top and "    python3Packages: PackageSet_python3Packages\n" in top  # 010-D12
    assert "    alpha_set: _PkgSet\n" not in top and summary["plain_sets"] == 1


def test_gen_pkgs_refuses_a_curated_set_that_is_not_a_set(tmp_path: Path) -> None:
    (tmp_path / "meta.json").write_text("{}")
    (tmp_path / "sets.json").write_text("{}")
    (tmp_path / "curated.txt").write_text("nothing\n")
    run = subprocess.run(
        [
            sys.executable,
            "-I",
            str(SRC / "pynix" / "gen_pkgs.py"),
            *map(str, (tmp_path / "meta.json", tmp_path / "sets.json", tmp_path / "curated.txt", tmp_path / "o")),
        ],
        capture_output=True,
        text=True,
    )
    assert run.returncode != 0 and "curated sets ['nothing'] are not package sets" in run.stderr
