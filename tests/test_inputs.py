"""The input packages (`nix/input-packages.nix`, `src/pynix/gen_input.py`; 009-D47, 009-D48, 009-D51, 010-D5).

The tests build the package of a tiny flake input (`tests/fixtures/inputs/fixture`) with the pinned nixpkgs of
`flake.lock`. They need `nix` and that nixpkgs in the store, and no network: a missing prerequisite skips them.
Home Manager is the pinned source of `flake.lock`, called through its own `flake.nix`.
"""

import ast
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from pynix import gen_input
from pynix_native import FoundInput, check_input, input_package_name, read_source

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "inputs" / "fixture"
NIX = ["nix", "--extra-experimental-features", "nix-command flakes", "--offline"]

pytestmark = pytest.mark.skipif(shutil.which("nix") is None, reason="nix is not installed")

# The Nix side of a call: the pinned nixpkgs and Home Manager from `flake.lock` (the store has them, the network is
# not used), the fixture as a real flake object, and `call` as Basix and minix call the function.
PRELUDE = """
let
  root = @ROOT@;
  lock = (builtins.fromJSON (builtins.readFile (root + "/flake.lock"))).nodes;
  fetch = n: builtins.fetchTree (builtins.removeAttrs lock.${n}.locked [ "dir" ]);
  nixpkgsSrc = fetch "nixpkgs";
  pkgs = import nixpkgsSrc { system = "x86_64-linux"; };
  nixpkgs = { rev = lock.nixpkgs.locked.rev; };
  fixture = builtins.getFlake "path:@FIXTURE@";
  # Home Manager as a consumer has it: the flake outputs, with the pinned nixpkgs.
  hmSrc = fetch "home-manager";
  nixpkgsFlake = { inherit (pkgs) lib; legacyPackages.x86_64-linux = pkgs; outPath = nixpkgsSrc; };
  homeManager = (import (hmSrc + "/flake.nix")).outputs { self = homeManager // { outPath = hmSrc; }; nixpkgs = nixpkgsFlake; };
  call = args: import (root + "/nix/input-packages.nix") ({ inherit pkgs nixpkgs; layer = "nixos"; inputs = { inherit fixture; }; } // args);
  hmCall = args: call ({ layer = "home-manager"; inherit homeManager; } // args);
in
"""


def expression(body: str) -> str:
    return PRELUDE.replace("@ROOT@", str(ROOT)).replace("@FIXTURE@", str(FIXTURE)) + body


def nix(command: str, body: str, *flags: str) -> subprocess.CompletedProcess[str]:
    argv = [*NIX, command, "--impure", *flags, "--expr", expression(body)]
    return subprocess.run(argv, capture_output=True, text=True)


def build(body: str) -> Path:
    done = nix("build", body, "--no-link", "--print-out-paths")
    assert done.returncode == 0, done.stderr[-1500:]
    return Path(done.stdout.strip())


def evaluate(body: str) -> Any:
    done = nix("eval", body, "--json")
    assert done.returncode == 0, done.stderr[-1500:]
    return json.loads(done.stdout)


def forced(call: str) -> str:
    """An expression that forces every option of the manifest of the input `fixture` (the walk reads the defaults)."""
    return f"builtins.stringLength (builtins.toJSON {call}.passthru.parts.fixture.passthru.manifest)"


def refused(body: str) -> str:
    """The error text of an expression that must fail."""
    done = nix("eval", body, "--json")
    assert done.returncode != 0
    return done.stderr


@pytest.fixture(scope="module", autouse=True)
def nixpkgs_in_the_store() -> None:
    done = nix("eval", "pkgs.lib.version + hmSrc.rev", "--raw")
    if done.returncode:
        pytest.skip(f"the pinned nixpkgs or Home Manager of flake.lock is not in the store: {done.stderr[-300:]}")


@pytest.fixture(scope="module")
def nixos_inputs() -> Path:
    """The NixOS layer: both modules of the fixture (a path module and a function value)."""
    return build('(call { modules.fixture = [ "fixture" "inline" ]; })')


@pytest.fixture(scope="module")
def home_inputs() -> Path:
    return build('(hmCall { modules.fixture = [ "fixture" ]; })')


@pytest.fixture(scope="module")
def names_only() -> Path:
    return build("(call { })")


def package(output: Path) -> Path:
    return output / input_package_name("fixture")


def python(output: Path, code: str) -> subprocess.CompletedProcess[str]:
    """Run `code` with the package on the path (the way the compiler runs the entry)."""
    argv = [sys.executable, "-c", f"import sys; sys.path.insert(0, {str(output)!r})\n{code}"]
    return subprocess.run(argv, capture_output=True, text=True)


# ---- the filter -------------------------------------------------------------------------------------------------------


def test_only_the_options_of_the_input_stay(nixos_inputs: Path) -> None:
    modules = sorted(p.relative_to(package(nixos_inputs)).as_posix() for p in package(nixos_inputs).rglob("*.py"))
    assert "services/fixture.py" in modules
    assert "services/fixtureInline.py" in modules  # a function value: found through `declarationPositions`
    # The base of NixOS (`systemd`, `users`, `boot`, `networking`, ...) declares thousands of options; none leaks.
    assert {m.split("/")[0] for m in modules if "/" in m} == {"services"}
    text = (package(nixos_inputs) / "services" / "fixture.py").read_text()
    assert "class Fixture(Root):" in text
    assert "systemd" not in text
    done = nix(
        "eval",
        '(builtins.length (call { modules.fixture = [ "fixture" "inline" ]; }).passthru.parts.fixture.passthru.manifest.options)',
        "--json",
    )
    assert done.stdout.strip() == "4"  # enable, port, settings, and the inline enable


def test_the_base_is_there_for_a_default_that_reads_it(home_inputs: Path) -> None:
    # `dataDir` has the default `${config.xdg.dataHome}/fixture`: the walk reads it, so the Home Manager base must be present.
    assert "dataDir" in (package(home_inputs) / "programs" / "fixture.py").read_text()
    message = refused(forced('(hmCall { modules.fixture = [ "fixture" ]; baseModules = [ ]; })'))
    assert "xdg" in message


def test_a_class_in_the_home_manager_layer(home_inputs: Path) -> None:
    text = (package(home_inputs) / "programs" / "fixture.py").read_text()
    assert "theme: Literal['light', 'dark']" in text
    assert "__nix_path__: ClassVar[tuple[str, ...]] = ('programs', 'fixture')" in text
    assert read_source(package(home_inputs) / "_generation.py") is not None


# ---- the record -------------------------------------------------------------------------------------------------------


def test_the_source_record(nixos_inputs: Path) -> None:
    source = read_source(package(nixos_inputs) / "_generation.py")
    flake_hash = evaluate("fixture.narHash")
    lock = json.loads((ROOT / "flake.lock").read_text())["nodes"]
    assert source is not None
    # A `path:` input has no `rev`, and the record then has no `rev` key.
    assert set(source) == {"input", "narHash", "nixpkgs", "generator", "modules"}
    assert source["input"] == "fixture"
    assert source["narHash"] == flake_hash
    assert source["nixpkgs"] == lock["nixpkgs"]["locked"]["rev"]
    assert source["modules"] == "fixture,inline"
    assert re.fullmatch(r"input-gen-[0-9a-f]{12}", source["generator"])
    assert source["generator"] == evaluate("(call { }).passthru.generator")


def test_the_pair_check_reads_the_record(nixos_inputs: Path) -> None:
    source = read_source(package(nixos_inputs) / "_generation.py")
    assert source is not None
    lock = {
        "root": "root",
        "version": 7,
        "nodes": {
            "root": {"inputs": {"fixture": "fixture", "nixpkgs": "nixpkgs"}},
            "fixture": {"locked": {"narHash": source["narHash"], "type": "path"}},
            "nixpkgs": {"locked": {"rev": source["nixpkgs"], "narHash": "sha256-x"}},
        },
    }
    item = FoundInput("fixture", "path:fixture", True, ("fixture", "inline"), None, "system.py", 3)
    check = lambda lock, generator: check_input(item, lock, nixos_inputs, "basix apply", generator).status  # noqa: E731
    assert check(lock, source["generator"]) == "ok"
    # A new generator is no error: apply makes the package again (010-D5).
    assert check(lock, "input-gen-000000000000") == "regenerate"
    moved = json.loads(json.dumps(lock))
    moved["nodes"]["fixture"]["locked"]["narHash"] = "sha256-moved"
    assert check(moved, source["generator"]) == "stale"
    other = json.loads(json.dumps(lock))
    other["nodes"]["nixpkgs"]["locked"]["rev"] = "0" * 40
    assert check(other, source["generator"]) == "stale"


def test_a_changed_generator_gives_another_id(tmp_path: Path) -> None:
    tree = tmp_path / "src" / "pynix"
    tree.mkdir(parents=True)
    for name in ("__init__", "generate", "gen_pkgs", "gen_input"):
        shutil.copy(ROOT / "src" / "pynix" / f"{name}.py", tree / f"{name}.py")
    same = evaluate(f"(call {{ src = {tmp_path / 'src'}; }}).passthru.generator")
    assert same == evaluate("(call { }).passthru.generator")  # the id follows the files, not the place
    (tree / "generate.py").write_text((tree / "generate.py").read_text() + "\n# a change\n")
    assert evaluate(f"(call {{ src = {tmp_path / 'src'}; }}).passthru.generator") != same


# ---- the name stub ----------------------------------------------------------------------------------------------------


def test_the_name_stub(nixos_inputs: Path) -> None:
    pkg = package(nixos_inputs)
    # One typed name for each derivation of `packages.<system>`; the text value `notes` is no package.
    assert json.loads((pkg / "names.json").read_text()) == {
        "fixture": ["fixture", 1],
        "fixture_data": ["fixture-data", 0],
    }
    stub = (pkg / "pkgs.pyi").read_text()
    assert "fixture: InputProg\n" in stub
    assert "fixture_data: InputPkg\n" in stub
    assert "notes" not in stub
    assert "The fixture program. Runs as `fixture`." in stub
    assert "fixture_pkgs: FixturePackages" in stub
    assert 'InputPackages("fixture", __file__)' in (pkg / "pkgs.py").read_text()


def test_the_name_stub_runs(nixos_inputs: Path) -> None:
    code = (
        "from pynix_fixture.pkgs import fixture_pkgs\n"
        "print(fixture_pkgs.fixture.model_dump())\n"
        "try:\n    fixture_pkgs.fixtur\nexcept Exception as error:\n    print(error)\n"
    )
    done = python(nixos_inputs, code)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        str({"kind": "input_package", "attr": "fixture", "input": "fixture"}),
        "The packages of the input `fixture` have no package `fixtur`. Did you mean `fixture`?",
    ]


def test_an_input_with_no_option_gets_the_name_stub_only(names_only: Path) -> None:
    pkg = package(names_only)
    assert sorted(p.name for p in pkg.iterdir()) == [
        "__init__.py",
        "_generation.py",
        "names.json",
        "pkgs.py",
        "pkgs.pyi",
        "py.typed",
    ]
    source = read_source(pkg / "_generation.py")
    assert source is not None and source["modules"] == ""
    assert (
        python(names_only, "from pynix_fixture.pkgs import fixture_pkgs\nprint(fixture_pkgs.fixture.attr)").stdout
        == "fixture\n"
    )


# ---- the classes ------------------------------------------------------------------------------------------------------


def test_each_class_names_the_input(nixos_inputs: Path) -> None:
    classes = 0
    for file in package(nixos_inputs).rglob("*.py"):
        for node in ast.walk(ast.parse(file.read_text())):
            if isinstance(node, ast.ClassDef):
                classes += 1
                first = (ast.get_docstring(node) or "").splitlines()[0]
                assert "(input `fixture`)" in first, (file.name, node.name, first)
    assert classes == 3  # Fixture, Fixture_Settings, FixtureInline


def test_the_classes_run(nixos_inputs: Path) -> None:
    code = (
        "from pynix_fixture.services.fixture import Fixture, Fixture_Settings\n"
        "print(Fixture(enable=True, port=8080, settings=Fixture_Settings(level='high', extra='x')).__nix_path__)\n"
        "try:\n    Fixture(port=70000)\nexcept ValueError as error:\n    print(type(error).__name__)\n"
    )
    done = python(nixos_inputs, code)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == ["('services', 'fixture')", "ValidationError"]


def test_the_package_name_gives_every_class(nixos_inputs: Path, tmp_path: Path) -> None:
    """009-D50: `import pynix_NAME as x`, then `x.Class(...)`, at run time and for ty."""
    done = python(nixos_inputs, "import pynix_fixture as fixture\nprint(fixture.Fixture(enable=True).__nix_path__)")
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "('services', 'fixture')"
    ty = Path(sys.executable).parent / "ty"
    if not ty.exists():
        pytest.skip("ty is not installed")
    entry = tmp_path / "entry.py"
    entry.write_text("import pynix_fixture as fixture\ngood = fixture.Fixture(enable=True)\ntypo = fixture.Fixtur()\n")
    argv = [str(ty), "check", "--output-format", "concise", "--python", sys.prefix]
    done = subprocess.run([*argv, "--extra-search-path", str(nixos_inputs), str(entry)], capture_output=True, text=True)
    flagged = {int(m.group(1)) for line in done.stdout.splitlines() if (m := re.search(r"entry\.py:(\d+):", line))}
    assert flagged == {3}, done.stdout


def test_ty_flags_a_wrong_nested_field(nixos_inputs: Path, tmp_path: Path) -> None:
    ty = Path(sys.executable).parent / "ty"
    if not ty.exists():
        pytest.skip("ty is not installed")
    entry = tmp_path / "entry.py"
    entry.write_text(
        "from pynix_fixture.pkgs import fixture_pkgs\n"
        "from pynix_fixture.services.fixture import Fixture, Fixture_Settings\n"
        "good = Fixture(enable=True, settings=Fixture_Settings(level='high'))\n"  # line 3
        "typo = Fixture(enabel=True)\n"  # line 4: a root field
        "bad_nested = Fixture(settings=Fixture_Settings(level='medium'))\n"  # line 5: a nested field
        "bad_name = fixture_pkgs.fixtur\n"  # line 6: a package name
    )
    argv = [
        str(ty),
        "check",
        "--output-format",
        "concise",
        "--python",
        sys.prefix,
        "--extra-search-path",
        str(nixos_inputs),
        str(entry),
    ]
    done = subprocess.run(argv, capture_output=True, text=True)
    lines = done.stdout.splitlines()
    flagged = {int(m.group(1)) for line in lines if (m := re.search(r"entry\.py:(\d+):", line))}
    assert 3 not in flagged, done.stdout
    assert {4, 5, 6} <= flagged, done.stdout


# ---- the call ---------------------------------------------------------------------------------------------------------


# ---- a named nixpkgs (`NixpkgsPin(name, commit)`; 009-D53, 009-D54) -------------------------------------------------------

#: A pinned nixpkgs as a flake input object: `legacyPackages`, `rev`, `narHash`, `lastModified`. The packages are the
#: two derivations of the fixture, so the build needs no real nixpkgs.
OLD_NIXPKGS = (
    '{ legacyPackages.x86_64-linux = fixture.packages.x86_64-linux; rev = "d233902339c02a9c334e7e593de68855ad26c4cb";'
    ' narHash = "sha256-30sZNZoA1cqF5JNO9fVX+wgiQYjB7HJqqJ4ztCDeBZE="; lastModified = 7; }'
)


@pytest.fixture(scope="module")
def named_nixpkgs() -> Path:
    return build(f"(call {{ nixpkgsInputs.old = {OLD_NIXPKGS}; }})")


def test_a_named_nixpkgs_gets_a_name_list(named_nixpkgs: Path) -> None:
    """Before the argument `nixpkgsInputs`, a `NixpkgsPin(...)` had no package list, so `old.pkgs.NAME` failed."""
    package_folder = named_nixpkgs / "pynix_nixpkgs_old"
    names = json.loads((package_folder / "names.json").read_text())
    assert names == {"fixture": ["fixture", 1], "fixture_data": ["fixture-data", 0]}
    assert sorted(p.name for p in named_nixpkgs.iterdir()) == ["pynix_fixture", "pynix_nixpkgs_old"]
    record = read_source(package_folder / "_generation.py")
    assert record == {
        "commit": "d233902339c02a9c334e7e593de68855ad26c4cb",
        "generator": "nixpkgs-names-1",
        "name": "old",
        "narHash": "sha256-30sZNZoA1cqF5JNO9fVX+wgiQYjB7HJqqJ4ztCDeBZE=",
    }


def test_the_name_list_runs_in_python(named_nixpkgs: Path) -> None:
    done = python(
        named_nixpkgs,
        "from pynix_native import NixpkgsPin\nold = NixpkgsPin('old', 'd233902339c02a9c334e7e593de68855ad26c4cb')\n"
        "print(old.pkgs.fixture.model_dump())\n",
    )
    assert done.returncode == 0, done.stderr
    assert "'attr': 'fixture'" in done.stdout and "'nixpkgs': 'old'" in done.stdout


def test_the_generator_works_with_the_standard_library_only(tmp_path: Path) -> None:
    """`nix/input-packages.nix` runs `gen_nixpkgs` with a plain Python and a tree of five files, with no pydantic."""
    tree = tmp_path / "tree" / "pynix"
    tree.mkdir(parents=True)
    for name in ("__init__", "generate", "gen_pkgs", "gen_input", "gen_nixpkgs"):
        shutil.copy(ROOT / "src" / "pynix" / f"{name}.py", tree / f"{name}.py")
    listing = tmp_path / "list.json"
    listing.write_text(
        json.dumps(
            {
                "source": {"commit": "a" * 40, "narHash": "sha256-x", "lastModified": 1},
                "packages": {"hello": {"kind": "drv", "main": "hello", "desc": None}},
            }
        )
    )
    done = subprocess.run(
        [sys.executable, "-I", "-m", "pynix.gen_nixpkgs", str(listing), str(tmp_path / "out"), "old"],
        capture_output=True,
        text=True,
        env={"PYTHONPATH": str(tmp_path / "tree"), "PYTHONSAFEPATH": "1"},
    )
    assert done.returncode == 0, done.stderr
    assert (tmp_path / "out" / "pynix_nixpkgs_old" / "names.json").is_file()


def test_the_generator_is_a_function_of_its_files() -> None:
    # Both the Python files and the Nix files decide the id: the id is a hash of `generate.py`, `gen_pkgs.py`,
    # `gen_input.py`, `extractor.nix`, and `input-packages.nix`.
    assert re.fullmatch(r"input-gen-[0-9a-f]{12}", evaluate("(call { }).passthru.generator"))


def test_an_input_that_is_not_a_flake_has_no_package() -> None:
    assert (
        evaluate('builtins.attrNames (call { inputs = { plain = { outPath = "/nix/store/none"; }; }; }).passthru.parts')
        == []
    )


def test_unknown_module_and_layer_are_named() -> None:
    message = refused(forced('(call { modules.fixture = [ "nope" ]; })'))
    assert "the input `fixture` has no nixosModules.nope. It has: default, fixture, inline." in message
    assert 'layer must be "nixos" or "home-manager", found "darwin"' in refused(
        '(call { layer = "darwin"; }).passthru.generator'
    )
    assert "needs the argument `homeManager`" in refused(
        forced('(call { layer = "home-manager"; modules.fixture = [ "fixture" ]; })')
    )


def test_the_generator_works_without_a_manifest_option(tmp_path: Path) -> None:
    """`gen_input.generate` with an empty manifest: the package holds the marker and the name stub."""
    manifest = {"format": gen_input.FORMAT, "options": [], "source": {"input": "x", "narHash": "n"}}
    meta: dict[str, dict] = {"hello": {"kind": "drv", "main": "hello", "desc": "Says hello"}, "text": {"kind": "other"}}
    summary = gen_input.generate(manifest, meta, tmp_path, "x-y")
    assert summary["package"] == "pynix_x_y" and summary["packages"] == 1 and summary["object"] == "x_y_pkgs"
    assert (tmp_path / "pynix_x_y" / "pkgs.pyi").read_text().count("InputProg") == 2  # the import and the one name
    assert read_source(tmp_path / "pynix_x_y" / "_generation.py") == {"input": "x", "narHash": "n"}


def test_the_docstring_rule() -> None:
    name = gen_input.name_input
    assert name("Options below `a.b`.", "x", "A") == "Options below `a.b` (input `x`)."
    assert name("The port", "x", "A") == "The port (input `x`)"
    assert name("", "x", "A") == "Options of A (input `x`)."
    assert name("First.\nSecond line.", "x", "A") == "First (input `x`).\nSecond line."


def test_the_wheel_needs_no_nix_folder() -> None:
    """The wheel packages the folders of `src/` only. The generator reads no file of `nix/`: Nix passes two JSON files."""
    packages = re.findall(r'"(src/[^"]+)"', (ROOT / "pyproject.toml").read_text())
    assert "src/pynix" in packages
    tree = ast.parse((ROOT / "src" / "pynix" / "gen_input.py").read_text())
    imports = {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
    imports |= {
        n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.level == 0
    }  # level 0: not a sibling
    assert {i.split(".")[0] for i in imports} <= {
        "__future__",
        "json",
        "re",
        "sys",
        "tempfile",
        "pathlib",
        "shutil",
        "",
    }


# ---- the Python code of an input (`Input(python="src")`) ---------------------------------------------------------------

PYTHON_INPUT = ROOT / "tests" / "fixtures" / "inputs" / "python" / "ok"
HASH = "sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="


def source(folder: Path, flake: bool) -> str:
    """The Nix text of an input object that holds `folder`: a copy in the store, as a locked input has it."""
    kind = '_type = "flake";' if flake else ""
    return f'{{ {kind} narHash = "{HASH}"; outPath = builtins.path {{ path = "{folder}"; name = "pyin"; }}; }}'


def python_call(inputs: dict[str, tuple[Path, bool, str]]) -> str:
    """A call with the given inputs: NAME to (folder, is a flake, `python` folder)."""
    objects = " ".join(f"{name} = {source(folder, flake)};" for name, (folder, flake, _) in inputs.items())
    dirs = " ".join(f'{name} = "{rel}";' for name, (_, _, rel) in inputs.items())
    return f"(call {{ inputs = {{ {objects} }}; pythonDirs = {{ {dirs} }}; }})"


def tree(folder: Path, files: dict[str, str]) -> Path:
    for name, text in files.items():
        (folder / name).parent.mkdir(parents=True, exist_ok=True)
        (folder / name).write_text(text)
    return folder


@pytest.fixture(scope="module")
def python_inputs() -> Path:
    """A flake and a plain source, both with code: the folder `src` and the root of the source."""
    return build(python_call({"flk": (PYTHON_INPUT, True, "src"), "plain": (PYTHON_INPUT, False, ".")}))


def test_the_entries_of_a_python_folder_are_linked(python_inputs: Path) -> None:
    # `src` of the flake holds the package `alpha`, the module `beta`, and the things that Pynix ignores. The plain source
    # gives the module `rootmod` of its root (its folder `src` has no `__init__.py`, so it is not a package).
    assert sorted(p.name for p in python_inputs.iterdir()) == [
        "alpha",
        "beta.py",
        "pynix_flk",
        "pynix_plain",
        "rootmod.py",
    ]
    assert (python_inputs / "alpha" / "sub.py").is_file()


def test_python_code_imports_through_the_output(python_inputs: Path) -> None:
    done = python(
        python_inputs,
        "import alpha, alpha.sub, beta, rootmod\n"
        "print(alpha.NAME, alpha.sub.VALUE, beta.NAME, rootmod.NAME)\n"
        "for name in ('_hidden', 'notes', 'my_mod', 'README'):\n"
        "    try:\n"
        "        __import__(name)\n"
        "    except ImportError:\n"
        "        continue\n"
        "    raise SystemExit(name + ' imports')\n",
    )
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "alpha 7 beta rootmod"


def test_a_plain_source_gets_a_record_for_the_pair_check(python_inputs: Path) -> None:
    text = (python_inputs / "pynix_plain" / "_generation.py").read_text()
    assert read_source(python_inputs / "pynix_plain" / "_generation.py") == {
        "input": "plain",
        "narHash": HASH,
        "modules": "",
        "generator": evaluate("(call { }).passthru.generator"),
        "nixpkgs": evaluate("nixpkgs.rev"),
    }
    assert "SOURCE" in text
    assert (python_inputs / "pynix_plain" / "py.typed").is_file()


def test_a_plain_source_without_python_has_no_package() -> None:
    assert (
        evaluate(f"builtins.attrNames (call {{ inputs.plain = {source(PYTHON_INPUT, False)}; }}).passthru.parts") == []
    )


def test_a_python_name_is_refused_when_two_inputs_give_it(tmp_path: Path) -> None:
    other = tree(tmp_path / "other", {"src/alpha.py": ""})
    message = refused(python_call({"one": (PYTHON_INPUT, True, "src"), "two": (other, False, "src")}) + ".name")
    assert "error: pynix input packages: two inputs give the Python name `alpha`: `one` and `two`" in message


def test_a_python_name_is_refused_when_one_input_gives_it_twice(tmp_path: Path) -> None:
    both = tree(tmp_path / "both", {"src/alpha/__init__.py": "", "src/alpha.py": ""})
    message = refused(python_call({"one": (both, True, "src")}) + ".name")
    assert (
        "error: pynix input packages: the input `one` gives the Python name `alpha` twice (a folder and a module)"
        in message
    )


@pytest.mark.parametrize(
    "name",
    [
        "pynix",
        "pynix_os",
        "pynix_anything",
        "nixdantic",
        "pydantic",
        "pydantic_core",
        "annotated_types",
        "typing_extensions",
        "typing_inspection",
        "minix",
        "minix_config",
        "basix",
        "basix_config",
    ],
)
def test_a_reserved_python_name_is_refused(tmp_path: Path, name: str) -> None:
    code = tree(tmp_path / "code", {f"src/{name}.py": ""})
    message = refused(python_call({"bad": (code, False, "src")}) + ".name")
    assert f"error: pynix input packages: the Python name `{name}` of the input `bad` is reserved" in message


def test_a_missing_python_folder_is_refused() -> None:
    message = refused(python_call({"bad": (PYTHON_INPUT, True, "nope")}) + ".name")
    assert "error: pynix input packages: the input `bad` has no folder `nope` (Input python=...)" in message


def test_a_python_folder_that_is_a_file_is_refused() -> None:
    message = refused(python_call({"bad": (PYTHON_INPUT, True, "rootmod.py")}) + ".name")
    assert "error: pynix input packages: the input `bad` has no folder `rootmod.py` (Input python=...)" in message


def test_a_python_folder_without_an_entry_is_refused(tmp_path: Path) -> None:
    code = tree(
        tmp_path / "code", {"src/README.md": "", "src/notes/a.txt": "", "src/_private.py": "", "src/x-y.py": ""}
    )
    message = refused(python_call({"bad": (code, True, "src")}) + ".name")
    assert (
        "error: pynix input packages: the folder `src` of the input `bad` holds no Python package or module" in message
    )


def test_a_python_dir_for_an_unknown_input_is_refused() -> None:
    message = refused('(call { pythonDirs.ghost = "src"; }).name')
    assert "error: pynix input packages: `python` names the input `ghost`, but the entry has no such input" in message


@pytest.mark.parametrize("flake", [True, False])
def test_a_standard_library_name_fails_the_build(tmp_path: Path, flake: bool) -> None:
    code = tree(tmp_path / "code", {"src/json/__init__.py": "", "src/fine.py": ""})
    done = nix("build", python_call({"bad": (code, flake, "src")}), "--no-link")
    assert done.returncode != 0
    assert "pynix input packages: the Python name `json` of the input `bad` is in the standard library" in done.stderr
    assert "`fine`" not in done.stderr


def test_a_flake_with_modules_gives_options_and_python_code() -> None:
    out = build('(call { modules.fixture = [ "fixture" ]; pythonDirs.fixture = "."; })')
    assert (package(out) / "services" / "fixture.py").is_file()
    done = python(out, "import fixturepy\nprint(fixturepy.NAME)\n")
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "fixturepy"
