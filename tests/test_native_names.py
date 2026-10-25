"""The package-name lists: the runtime sets and the generator `pynix.gen_nixpkgs` (009-D54)."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from pynix.gen_nixpkgs import GENERATOR, generate, names_expression
from pynix_native import (
    NAMES_GENERATOR,
    InputPackages,
    InputPkg,
    InputProg,
    NixpkgsPackages,
    NixpkgsPin,
    NixpkgsPkg,
    NixpkgsProg,
    apply_command,
    read_source,
    set_apply_command,
)
from pynix_pkgs import PackageError, Pkg, Prog

OLD = "d233902339c02a9c334e7e593de68855ad26c4cb"
HASH = "sha256-30sZNZoA1cqF5JNO9fVX+wgiQYjB7HJqqJ4ztCDeBZE="
LIST = {
    "source": {"commit": OLD, "narHash": HASH, "lastModified": 1778869304},
    "packages": {
        "hello": {"kind": "drv", "main": "hello", "desc": "A program that produces a familiar, friendly greeting"},
        "zlib": {"kind": "drv", "main": None, "desc": "Lossless data-compression library"},
        "ripgrep-all": {"kind": "drv", "main": "rga", "desc": None},
        "ripgrep_all": {"kind": "drv", "main": None, "desc": None},  # a name that collides after the mapping
        "7zip": {"kind": "drv", "main": "7zz", "desc": None},
        "import": {"kind": "drv", "main": None, "desc": None},
        "python3Packages": {"kind": "set"},
        "broken": {"kind": "fail"},
    },
}


@pytest.fixture
def old_list(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """The package `pynix_nixpkgs_old` on `sys.path`, as the generator writes it."""
    generate(LIST, tmp_path, "old")
    monkeypatch.syspath_prepend(str(tmp_path))
    for key in [k for k in sys.modules if k.startswith("pynix_nixpkgs_")]:
        monkeypatch.delitem(sys.modules, key)
    return tmp_path / "pynix_nixpkgs_old"


def test_old_pkgs_gives_a_nixpkgs_reference(old_list: Path) -> None:
    old = NixpkgsPin("old", OLD)
    hello = old.pkgs.hello
    assert isinstance(hello, NixpkgsProg)
    assert hello.model_dump() == {"kind": "nixpkgs_package", "attr": "hello", "nixpkgs": "old"}
    assert isinstance(old.pkgs.zlib, NixpkgsPkg) and not isinstance(old.pkgs.zlib, NixpkgsProg)


def test_a_nixpkgs_package_fits_program(old_list: Path) -> None:
    """`Program(package: Pkg)` takes it: the model field is strict about the class, and subclasses pass."""
    old = NixpkgsPin("old", OLD)
    assert isinstance(old.pkgs.hello, Pkg)
    assert isinstance(old.pkgs.hello, Prog)
    assert isinstance(old.pkgs.zlib, Pkg)


def test_old_pkgs_says_did_you_mean(old_list: Path) -> None:
    old = NixpkgsPin("old", OLD)
    typo = "helo"
    with pytest.raises(PackageError) as caught:
        getattr(old.pkgs, typo)
    assert str(caught.value) == "The package list `old` has no package `helo`. Did you mean `hello`?"
    assert caught.value.word == "helo"


def test_old_pkgs_with_no_close_name(old_list: Path) -> None:
    with pytest.raises(PackageError) as caught:
        NixpkgsPin("old", OLD).pkgs.qqqqqqqq  # noqa: B018
    assert str(caught.value) == "The package list `old` has no package `qqqqqqqq`."


def test_old_pkgs_by_attribute_and_by_python_name(old_list: Path) -> None:
    pkgs = NixpkgsPin("old", OLD).pkgs
    assert pkgs["ripgrep-all"].attr == "ripgrep-all"
    assert pkgs.ripgrep_all.attr == "ripgrep_all"  # the identifier wins the collision
    assert pkgs["7zip"].attr == "7zip"
    assert pkgs._7zip.attr == "7zip"  # a name with a leading underscore is a package, not Python
    assert pkgs.import_.attr == "import"


def test_old_pkgs_lists_its_names(old_list: Path) -> None:
    assert "hello" in dir(NixpkgsPin("old", OLD).pkgs)


def test_old_pkgs_before_the_list_is_made(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.syspath_prepend(str(tmp_path))
    pkgs = NixpkgsPin("missing-one", OLD).pkgs
    with pytest.raises(PackageError) as caught:
        pkgs.hello  # noqa: B018
    assert str(caught.value) == "The package list `missing-one` is not made yet: run `basix apply`."


def test_the_apply_command_is_set_by_the_layer(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.syspath_prepend(str(tmp_path))
    assert apply_command() == "basix apply"
    set_apply_command("minix apply")
    try:
        with pytest.raises(PackageError) as caught:
            NixpkgsPackages("nothing").hello  # noqa: B018
        assert str(caught.value).endswith("run `minix apply`.")
    finally:
        set_apply_command("basix apply")


def test_input_packages(tmp_path: Path) -> None:
    rows = {"nirinit": ["nirinit", 1], "default": ["default", 1], "doc": ["doc", 0]}
    (tmp_path / "names.json").write_text(json.dumps(rows))
    pkgs = InputPackages("nirinit", str(tmp_path / "pkgs.py"))
    assert isinstance(pkgs.nirinit, InputProg)
    assert pkgs.nirinit.model_dump() == {"kind": "input_package", "attr": "nirinit", "input": "nirinit"}
    assert isinstance(pkgs.doc, InputPkg) and not isinstance(pkgs.doc, InputProg)
    assert isinstance(pkgs.nirinit, Pkg)  # `Program(nirinit_pkgs.nirinit)` fits (009-D54)
    with pytest.raises(PackageError) as caught:
        pkgs.nirnit  # noqa: B018
    assert str(caught.value) == "The packages of the input `nirinit` have no package `nirnit`. Did you mean `nirinit`?"


def test_a_new_names_file_is_read_again(tmp_path: Path) -> None:
    file = tmp_path / "names.json"
    file.write_text(json.dumps({"a": ["a", 0]}))
    pkgs = InputPackages("x", str(tmp_path / "pkgs.py"))
    assert pkgs.a.attr == "a"
    file.write_text(json.dumps({"b": ["b", 0]}))
    assert pkgs.b.attr == "b"


def test_the_generator_writes_the_package(tmp_path: Path) -> None:
    summary = generate(LIST, tmp_path, "old")
    assert summary["module"] == "pynix_nixpkgs_old"
    assert summary["packages"] == 5  # hello, zlib, ripgrep_all, _7zip, import_; ripgrep-all collides
    pkg = tmp_path / "pynix_nixpkgs_old"
    assert sorted(p.name for p in pkg.iterdir()) == [
        "__init__.py",
        "__init__.pyi",
        "_generation.py",
        "names.json",
        "py.typed",
    ]
    names = json.loads((pkg / "names.json").read_text())
    assert names["hello"] == ["hello", 1]
    assert names["zlib"] == ["zlib", 0]
    assert names["ripgrep_all"] == ["ripgrep_all", 0]
    assert names["ripgrep-all"] == ["ripgrep-all", 1]  # reachable by its attribute
    assert "python3Packages" not in names and "broken" not in names
    assert (pkg / "__init__.py").read_text().endswith('pkgs = NixpkgsPackages("old")\n')


def test_the_generator_records_the_source(tmp_path: Path) -> None:
    generate(LIST, tmp_path, "old")
    assert read_source(tmp_path / "pynix_nixpkgs_old" / "_generation.py") == {
        "commit": OLD,
        "generator": NAMES_GENERATOR,
        "name": "old",
        "narHash": HASH,
    }
    assert GENERATOR == NAMES_GENERATOR


def test_the_stub_types_each_name(tmp_path: Path) -> None:
    generate(LIST, tmp_path, "old-2")
    text = (tmp_path / "pynix_nixpkgs_old_2" / "__init__.pyi").read_text()
    assert "class Old2Packages:" in text
    assert "    hello: NixpkgsProg\n" in text
    assert "    zlib: NixpkgsPkg\n" in text
    assert "    _7zip: NixpkgsProg\n" in text
    assert "    import_: NixpkgsPkg\n" in text
    assert text.endswith("pkgs: Old2Packages\n")
    assert '"""' not in text.split("class")[1]  # no descriptions by default
    generate(LIST, tmp_path / "docs", "old", docs=True)
    assert (
        "A program that produces a familiar, friendly greeting. Runs as `hello`."
        in (tmp_path / "docs" / "pynix_nixpkgs_old" / "__init__.pyi").read_text()
    )


def test_the_generator_is_deterministic(tmp_path: Path) -> None:
    generate(LIST, tmp_path / "a", "old")
    generate(LIST, tmp_path / "b", "old")
    for name in ("names.json", "__init__.pyi", "_generation.py", "__init__.py"):
        assert (tmp_path / "a" / "pynix_nixpkgs_old" / name).read_text() == (
            tmp_path / "b" / "pynix_nixpkgs_old" / name
        ).read_text()


def test_the_expression_fetches_the_locked_source() -> None:
    locked = {"narHash": HASH, "rev": OLD, "owner": "NixOS", "repo": "nixpkgs", "type": "github", "dir": "x"}
    text = names_expression(locked, Path("/n/nixpkgs-names.nix"), "aarch64-linux")
    assert "builtins.fetchTree locked" in text
    assert 'system = "aarch64-linux"' in text
    assert "import /n/nixpkgs-names.nix" in text
    assert '"dir"' not in text


@pytest.mark.skipif(shutil.which("nix-instantiate") is None, reason="needs nix-instantiate")
def test_the_nix_file_gives_the_list_the_generator_reads() -> None:
    nix_file = Path(__file__).resolve().parents[1] / "nix" / "nixpkgs-names.nix"
    fake = (
        '{ hello = { type = "derivation"; meta = { mainProgram = "hello"; description = "Greeting"; }; };'
        ' zlib = { type = "derivation"; meta = { }; }; lib = { x = 1; }; boom = throw "no"; }'
    )
    expr = (
        f"import {nix_file} {{ legacyPackages = {fake};"
        f' source = {{ rev = "{OLD}"; narHash = "{HASH}"; lastModified = 7; }}; }}'
    )
    done = subprocess.run(
        ["nix-instantiate", "--eval", "--strict", "--json", "--expr", expr], capture_output=True, text=True
    )
    assert done.returncode == 0, done.stderr
    data = json.loads(done.stdout)
    assert data["source"] == {"commit": OLD, "narHash": HASH, "lastModified": 7}
    assert data["packages"]["hello"] == {"kind": "drv", "main": "hello", "desc": "Greeting"}
    assert data["packages"]["zlib"] == {"kind": "drv", "main": None, "desc": None}
    assert data["packages"]["lib"] == {"kind": "set"}
    assert data["packages"]["boom"] == {"kind": "fail"}
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        assert generate(data, Path(tmp), "fake")["packages"] == 2


def test_the_generator_copy_equals_the_runtime() -> None:
    """`pynix.gen_nixpkgs` needs the standard library only, so it keeps its own copy of two rules. They must agree."""
    from pynix.gen_nixpkgs import nixpkgs_package_name as generator_name
    from pynix_native import nixpkgs_package_name

    assert GENERATOR == NAMES_GENERATOR
    assert all(generator_name(n) == nixpkgs_package_name(n) for n in ("old", "a-b", "x1"))
