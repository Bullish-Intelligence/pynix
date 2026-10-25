"""The read audit (`nixdantic.reads`, 009-D45): which files an entry reads while it runs."""

import hashlib
import importlib
import os
import sys
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
