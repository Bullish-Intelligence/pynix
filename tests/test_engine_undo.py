"""Undo: restore the files of the last good save, keep the dropped edit at a ref, then apply (CONCEPT 4.2)."""

import fcntl
from pathlib import Path

import pytest
from test_engine_support import TOP_NEW, TOP_OLD, Setup, basix_layer, make_setup, minix_layer

from pynix_engine import Result, Session


@pytest.fixture
def s(tmp_path: Path) -> Setup:
    return make_setup(tmp_path)


def test_undo_with_a_dirty_tree_drops_the_edit_and_commits_nothing(s: Setup) -> None:
    """S12 3a, S16 6a."""
    s.git.tree, s.git.head_tree = "tree-edit", "tree-head"
    s.git.staged = []  # after the restore, the tree equals HEAD
    assert s.engine().undo() == 0
    assert s.git.refs == {"refs/basix/dropped": "deadbeefcafe0000"}
    assert s.runner.words("git restore --source=HEAD --staged --worktree :/")
    assert s.git.commits == []
    assert s.lines[0] == "undo: dropped the edit that basix did not apply (a copy stays in the workspace history)"
    assert s.lines[-1] == "nothing to change"


def test_undo_with_a_clean_tree_restores_the_files_of_the_save_before(s: Setup) -> None:
    """S12 3b, S16 6b: the files of HEAD~1, an apply of them, and a new commit."""
    s.git.tree = s.git.head_tree = "tree-head"
    s.git.restored_staged = ["system.py", "system.json"]
    assert s.engine().undo() == 0
    assert s.runner.words("git restore --source=HEAD~1 --staged --worktree :/")
    assert s.git.refs == {}
    assert s.git.commits == ["undo to abc1234"]
    assert "undo: restoring the files of the save before the last one" in s.lines
    assert s.lines[-1] == "saved: the files of the earlier save are back"
    assert s.trace() == ["restore", "build", "reset", "test", "health", "profile", "boot", "commit"]


def test_undo_applies_with_the_same_rules(s: Setup) -> None:
    """A failed check after an undo rolls back, as for any apply."""
    s.git.tree = s.git.head_tree = "tree-head"
    s.git.restored_staged = ["system.py"]
    s.runner.on(("systemctl",), Result(0, "web.service loaded failed failed Web\n"))
    assert s.engine().undo() == 3
    assert s.git.commits == []


def test_undo_refuses_when_there_is_one_commit(s: Setup) -> None:
    s.git.tree = s.git.head_tree = "tree-head"
    s.git.has_parent = False
    assert s.engine().undo() == 1
    assert s.lines[-1] == "There is only one save. There is nothing to undo."
    assert not s.runner.words("git restore")
    assert s.runner.count("nix") == 0


def test_undo_refuses_with_no_commit(s: Setup) -> None:
    s.git.has_head = False
    assert s.engine().undo() == 1
    assert s.lines[-1] == "There is nothing to go back to. Run basix apply first."
    assert not s.runner.words("git restore")


def test_undo_takes_the_lock_before_it_touches_the_files(s: Setup) -> None:
    state = s.ws / ".git" / "basix"
    state.mkdir()
    with (state / "lock").open("w") as holder:
        fcntl.flock(holder, fcntl.LOCK_EX)
        assert s.engine().undo() == 1
    assert s.runner.calls == []


def test_undo_for_minix_uses_its_own_ref_and_words(s: Setup) -> None:
    s.world.running = TOP_OLD
    s.git.tree, s.git.head_tree = "tree-edit", "tree-head"
    s.git.staged = []
    assert s.engine(minix_layer(s.world)).undo() == 0
    assert list(s.git.refs) == ["refs/minix/dropped"]
    assert "minix did not apply" in s.lines[0]
    assert "refs/minix/dropped" in s.log("minix")


def test_undo_runs_the_pin_check_after_the_build(s: Setup) -> None:
    s.git.tree = s.git.head_tree = "tree-head"
    s.git.restored_staged = ["system.py", "system.json"]
    seen: list[tuple[str, list[str]]] = []

    def check(session: Session, built: str) -> list[str]:
        seen.append((built, s.trace()))
        return ["warning: pins differ"]

    assert s.engine(basix_layer(s.world, pin_check=check)).undo() == 0
    assert seen == [(TOP_NEW, ["restore", "build"])]
    assert "warning: pins differ" in s.lines
