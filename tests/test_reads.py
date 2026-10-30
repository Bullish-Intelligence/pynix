"""The read audit (`nixdantic.reads`, 009-D45): which files an entry reads while it runs."""

import hashlib
import importlib
import importlib.util
import os
import py_compile
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

from nixdantic.reads import Reads


@pytest.fixture(autouse=True)
def _in_the_workspace(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The compiler runs an entry in its own folder, so a relative path in the entry names a file of the workspace."""
    (tmp_path / "work").mkdir()
    monkeypatch.chdir(tmp_path / "work")


def run(entry: Path, out: Path | None = None) -> Reads:
    """Run the source of `entry` as the entry, with the audit on. The code object carries the path of the entry."""
    with Reads(entry, out) as reads:
        exec(compile(entry.read_text(), str(entry), "exec"), {})
    return reads


def workspace(tmp_path: Path, source: str) -> Path:
    folder = tmp_path / "work"
    entry = folder / "home.py"
    entry.write_text(source)
    return entry


def test_a_read_inside_the_workspace_is_recorded_with_its_hash(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'text = open("data.txt").read()\n')
    (entry.parent / "data.txt").write_text("hello")
    reads = run(entry)
    assert reads.result() == {
        "files": {"data.txt": hashlib.sha256(b"hello").hexdigest()},
        "absent": [],
        "dirs": {},
        "ignore": ["__pycache__"],
    }
    assert reads.refusals() == []


def test_a_read_in_a_subfolder_has_a_path_relative_to_the_entry(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'from pathlib import Path\ntext = Path("sub/a.txt").read_text()\n')
    (entry.parent / "sub").mkdir()
    (entry.parent / "sub" / "a.txt").write_text("a")
    assert list(run(entry).result()["files"]) == ["sub/a.txt"]


def test_the_entry_file_itself_is_not_recorded(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'text = open("home.py").read()\n')
    assert run(entry).result()["files"] == {}


def test_a_file_that_does_not_exist_is_recorded_as_absent(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'import contextlib\nwith contextlib.suppress(OSError):\n    open("missing.txt")\n')
    result = run(entry).result()
    assert result["absent"] == ["missing.txt"]
    assert result["files"] == {}


def test_a_write_is_not_a_read(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'open("made.txt", "w").write("x")\n')
    result = run(entry).result()
    assert result["files"] == {}
    assert result["absent"] == []


def test_a_folder_listing_is_recorded_as_its_names(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'import os\nnames = os.listdir("shelf")\n')
    shelf = entry.parent / "shelf"
    shelf.mkdir()
    (shelf / "b.txt").write_text("b")
    (shelf / "a.txt").write_text("a")
    assert run(entry).result()["dirs"] == {"shelf": ["a.txt", "b.txt"]}


def test_glob_and_iterdir_are_recorded_as_listings(tmp_path: Path) -> None:
    entry = workspace(
        tmp_path, 'from pathlib import Path\nlist(Path("one").iterdir())\nlist(Path("two").glob("*.txt"))\n'
    )
    for name in ("one", "two"):
        (entry.parent / name).mkdir()
        (entry.parent / name / "f.txt").write_text(name)
    assert run(entry).result()["dirs"] == {"one": ["f.txt"], "two": ["f.txt"]}


def test_the_ignore_list_hides_the_output_and_the_bytecode_folder(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'import os\nnames = os.listdir(".")\n')
    out = entry.parent / "home.json"
    out.write_text("{}")
    (entry.parent / "__pycache__").mkdir()
    (entry.parent / "keep.txt").write_text("k")
    reads = run(entry, out)
    assert reads.result()["ignore"] == ["__pycache__", "home.json"]
    assert reads.result()["dirs"] == {".": ["home.py", "keep.txt"]}


def test_an_output_in_another_folder_is_not_ignored(tmp_path: Path) -> None:
    entry = workspace(tmp_path, "x = 1\n")
    assert Reads(entry, tmp_path / "home.json").ignore == ["__pycache__"]


def test_a_read_outside_the_workspace_is_refused_with_its_place(tmp_path: Path) -> None:
    secret = tmp_path / "secret.txt"
    secret.write_text("s")
    entry = workspace(tmp_path, f"x = 1\nsecret = open({str(secret)!r}).read()\n")
    reads = run(entry)
    assert reads.result()["files"] == {}
    assert reads.refusals() == [
        f"home.py:2:10: reads {secret}, which is outside the workspace. "
        "Copy the file into the folder of home.py and read the copy."
    ]


def test_a_read_after_the_audit_is_not_recorded(tmp_path: Path) -> None:
    entry = workspace(tmp_path, "x = 1\n")
    reads = run(entry)
    (entry.parent / "later.txt").write_text("late")
    (entry.parent / "later.txt").read_text()
    assert reads.result()["files"] == {}
    assert os.path.exists(entry.parent / "later.txt")


def test_a_read_of_a_special_path_is_not_recorded(tmp_path: Path) -> None:
    entry = workspace(tmp_path, 'open("/proc/self/stat").read()\n')
    reads = run(entry)
    assert reads.result()["files"] == {}
    assert reads.refusals() == []


def test_a_helper_module_of_the_workspace_is_recorded(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    entry = workspace(tmp_path, "import audit_helper\nvalue = audit_helper.VALUE\n")
    (entry.parent / "audit_helper.py").write_text("VALUE = 3\n")
    monkeypatch.syspath_prepend(str(entry.parent))
    monkeypatch.delitem(sys.modules, "audit_helper", raising=False)
    # A first import saves the bytecode file. The next import loads it and never opens the source.
    monkeypatch.setattr(sys, "dont_write_bytecode", False)
    importlib.import_module("audit_helper")
    del sys.modules["audit_helper"]
    assert (entry.parent / "__pycache__").is_dir()
    reads = run(entry)
    result = reads.result()  # the module list is read here, so the module must still be loaded
    del sys.modules["audit_helper"]
    assert list(result["files"]) == ["audit_helper.py"]


@pytest.fixture
def clean_imports(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Restore `sys.path`, `sys.modules`, and the finder cache after a test that imports in the audit."""
    modules = dict(sys.modules)
    finders = dict(sys.path_importer_cache)
    monkeypatch.setattr(sys, "path", list(sys.path))
    monkeypatch.setattr(sys, "dont_write_bytecode", True)
    yield
    for name in set(sys.modules) - set(modules):
        del sys.modules[name]
    sys.modules.update(modules)  # a test may pop a module
    sys.path_importer_cache.clear()
    sys.path_importer_cache.update(finders)


def outside_module(
    tmp_path: Path,
    name: str,
    *,
    pyc: bool,
    mode: py_compile.PycInvalidationMode = py_compile.PycInvalidationMode.TIMESTAMP,
) -> Path:
    """A module file in a folder that is not the workspace. `pyc` saves a valid bytecode file next to it.

    A set `SOURCE_DATE_EPOCH` makes Python write a checked-hash file, and Python reads the source to check it. So the
    caller picks the mode: a timestamp file or an unchecked-hash file loads without any read of the source.
    """
    folder = tmp_path / "outside"
    folder.mkdir(exist_ok=True)
    source = folder / f"{name}.py"
    source.write_text("VALUE = 1\n")
    if pyc:
        py_compile.compile(str(source), doraise=True, invalidation_mode=mode)
        assert os.path.exists(importlib.util.cache_from_source(str(source)))
    return source


def import_outside(tmp_path: Path, name: str) -> Path:
    return workspace(tmp_path, f"import sys\nsys.path.insert(0, {str(tmp_path / 'outside')!r})\nimport {name}\n")


@pytest.mark.parametrize(
    "mode", [py_compile.PycInvalidationMode.TIMESTAMP, py_compile.PycInvalidationMode.UNCHECKED_HASH]
)
def test_an_outside_module_with_a_saved_bytecode_file_is_refused(
    tmp_path: Path, clean_imports: None, mode: py_compile.PycInvalidationMode
) -> None:
    source = outside_module(tmp_path, "audit_outside_pyc", pyc=True, mode=mode)
    reads = run(import_outside(tmp_path, "audit_outside_pyc"))
    assert reads.result()["files"] == {}
    assert reads.refusals() == [
        f"home.py:3:1: imports {source}, which is outside the workspace. "
        "Put the module in the folder of home.py, or bring it in through an Input."
    ]


def test_an_outside_module_without_a_bytecode_file_is_refused_once(tmp_path: Path, clean_imports: None) -> None:
    source = outside_module(tmp_path, "audit_outside_src", pyc=False)
    lines = run(import_outside(tmp_path, "audit_outside_src")).refusals()
    assert len(lines) == 1
    assert str(source) in lines[0]


def test_an_outside_module_that_a_helper_imports_is_refused_with_the_place_of_the_helper_import(
    tmp_path: Path, clean_imports: None
) -> None:
    source = outside_module(tmp_path, "audit_outside_deep", pyc=True)
    entry = workspace(tmp_path, f"import sys\nsys.path.insert(0, {str(tmp_path / 'outside')!r})\nimport audit_inner\n")
    (entry.parent / "audit_inner.py").write_text("import audit_outside_deep\n")
    sys.path.append(str(entry.parent))
    lines = run(entry).refusals()
    assert lines == [
        f"home.py:3:1: imports {source}, which is outside the workspace. "
        "Put the module in the folder of home.py, or bring it in through an Input."
    ]


def test_an_outside_module_that_the_toolchain_loaded_before_the_run_is_not_refused(
    tmp_path: Path, clean_imports: None
) -> None:
    outside_module(tmp_path, "audit_outside_early", pyc=False)
    sys.path.insert(0, str(tmp_path / "outside"))
    importlib.import_module("audit_outside_early")
    sys.path.remove(str(tmp_path / "outside"))
    assert run(workspace(tmp_path, "import audit_outside_early\n")).refusals() == []


def test_a_stdlib_and_a_pydantic_import_are_not_refused(tmp_path: Path, clean_imports: None) -> None:
    """Both modules load in the audit, so the module check sees them. Both live under library entries."""
    import pydantic  # noqa: F401

    for name in ("zipapp", "pydantic.deprecated.parse"):
        sys.modules.pop(name, None)
    reads = run(workspace(tmp_path, "import zipapp\nimport pydantic.deprecated.parse\n"))
    assert "zipapp" in sys.modules
    assert "pydantic.deprecated.parse" in sys.modules
    assert reads.refusals() == []
    assert reads.result()["files"] == {}


def test_an_entry_of_sys_path_inside_the_workspace_does_not_hide_its_files(tmp_path: Path, clean_imports: None) -> None:
    entry = workspace(tmp_path, "import audit_vendored\nopen('vendor/data.txt').read()\n")
    (entry.parent / "vendor").mkdir()
    (entry.parent / "vendor" / "audit_vendored.py").write_text("VALUE = 1\n")
    (entry.parent / "vendor" / "data.txt").write_text("d")
    sys.path.append(str(entry.parent / "vendor"))
    reads = run(entry)
    assert sorted(reads.result()["files"]) == ["vendor/audit_vendored.py", "vendor/data.txt"]
    assert reads.refusals() == []


def test_the_generated_packages_folder_inside_the_workspace_stays_exempt(tmp_path: Path, clean_imports: None) -> None:
    entry = workspace(tmp_path, "import audit_generated\n")
    packages = entry.parent / ".basix" / "pynix"
    packages.mkdir(parents=True)
    (packages / "audit_generated.py").write_text("VALUE = 1\n")
    sys.path.append(str(packages))
    reads = run(entry)
    assert reads.result()["files"] == {}
    assert reads.refusals() == []


def test_a_caller_can_name_another_folder_inside_the_workspace_as_library_code(
    tmp_path: Path, clean_imports: None
) -> None:
    entry = workspace(tmp_path, "import audit_named\n")
    (entry.parent / "lib").mkdir()
    (entry.parent / "lib" / "audit_named.py").write_text("VALUE = 1\n")
    sys.path.append(str(entry.parent / "lib"))
    with Reads(entry, inside_libs=["lib"]) as reads:
        exec(compile(entry.read_text(), str(entry), "exec"), {})
    assert reads.result()["files"] == {}


def test_an_ancestor_of_the_workspace_on_sys_path_does_not_hide_a_read(tmp_path: Path, clean_imports: None) -> None:
    entry = workspace(tmp_path, "open('data.txt').read()\nopen('../note.txt').read()\n")
    (entry.parent / "data.txt").write_text("d")
    (tmp_path / "note.txt").write_text("n")
    sys.path.append(str(tmp_path))
    reads = run(entry)
    assert list(reads.result()["files"]) == ["data.txt"]
    assert reads.refusals() == [
        f"home.py:2:1: reads {tmp_path / 'note.txt'}, which is outside the workspace. "
        "Copy the file into the folder of home.py and read the copy."
    ]
