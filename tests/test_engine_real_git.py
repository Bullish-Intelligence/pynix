"""The engine with real git: stage, refuse, commit, and undo in a git repository on disk. Nix and the switch are fake.

The other engine tests model git with `FakeGit`. These tests check the git commands themselves.
"""

import fcntl
import os
import subprocess
from collections.abc import Callable, Sequence
from pathlib import Path

import pytest
from test_engine_support import GOOD_UNITS, HEALTH, HEALTH_USER, TOP_NEW, World, basix_layer, minix_layer

from pynix_engine import Engine, Layer, Result, Session, SubprocessRunner
from pynix_engine.testing import FakeClock, FakeRunner

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.org",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.org",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


class GitThenFake:
    """Send `git` to a real process and every other command to a fake runner."""

    def __init__(self, fake: FakeRunner) -> None:
        self.fake = fake
        self.real = SubprocessRunner()
        self.git_calls: list[tuple[str, ...]] = []

    def run(
        self, argv: Sequence[str], *, cwd: Path | None = None, on_line: Callable[[str], None] | None = None
    ) -> Result:
        if tuple(argv[:1]) == ("git",):
            self.git_calls.append(tuple(argv))
            return self.real.run(argv, cwd=cwd, on_line=on_line)
        return self.fake.run(argv, cwd=cwd, on_line=on_line)


def git(ws: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=ws, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def ws(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    # The test repository gets its own identity: no outer git setting (a devenv persona, a GIT_* variable) reaches it.
    for key in [k for k in os.environ if k.startswith("GIT_")]:
        monkeypatch.delenv(key)
    for key, value in GIT_ENV.items():
        monkeypatch.setenv(key, value)
    git(tmp_path, "init", "-q", "-b", "main")
    git(tmp_path, "config", "user.name", "test")
    git(tmp_path, "config", "user.email", "test@example.org")
    (tmp_path / "system.py").write_text("machine = 1\n")
    git(tmp_path, "add", "-A")
    git(tmp_path, "commit", "-q", "-m", "first")
    return tmp_path


def engine(ws: Path, lines: list[str], layer: Layer | None = None) -> tuple[Engine, GitThenFake]:
    fake = FakeRunner()
    fake.on(("nix", "build"), Result(0, TOP_NEW + "\n"))
    fake.on(HEALTH, Result(0, GOOD_UNITS))
    fake.on(HEALTH_USER, Result(0, GOOD_UNITS))
    runner = GitThenFake(fake)
    return Engine(layer or basix_layer(World()), ws, runner=runner, clock=FakeClock(), say=lines.append, env={}), runner


def test_apply_stages_and_commits_a_new_file(ws: Path) -> None:
    (ws / "system.py").write_text("machine = 2\n")
    (ws / "notes.txt").write_text("a new file\n")
    lines: list[str] = []
    assert engine(ws, lines)[0].apply() == 0, lines
    assert git(ws, "status", "--porcelain") == ""
    assert sorted(git(ws, "show", "--name-only", "--format=", "HEAD").split()) == [
        "notes.txt",
        "system.json",
        "system.py",
    ]
    assert lines[-1].startswith("saved")


def test_apply_refuses_a_secret_and_a_symlink_out(ws: Path) -> None:
    (ws / "key.pem").write_text("-----BEGIN-----\n")
    lines: list[str] = []
    assert engine(ws, lines)[0].apply() != 0
    assert any("key.pem" in line and "secret" in line for line in lines), lines
    assert git(ws, "log", "--format=%s") == "first\n"
    (ws / "key.pem").unlink()
    (ws / "out").symlink_to("/etc/hostname")
    lines.clear()
    assert engine(ws, lines)[0].apply() != 0
    assert any("out" in line for line in lines)
    assert git(ws, "log", "--format=%s") == "first\n"


def test_undo_drops_an_edit_and_restores_the_earlier_save(ws: Path) -> None:
    (ws / "system.py").write_text("machine = 2\n")
    assert engine(ws, [])[0].apply() == 0
    (ws / "system.py").write_text("machine = 3\n")
    lines: list[str] = []
    # A dirty tree: undo drops the edit, keeps it at a ref, and commits nothing.
    assert engine(ws, lines)[0].undo() == 0
    assert (ws / "system.py").read_text() == "machine = 2\n"
    assert git(ws, "rev-parse", "--verify", "-q", "refs/basix/dropped").strip()
    # A clean tree: undo restores the files of the save before the last one and commits them.
    assert engine(ws, [])[0].undo() == 0
    assert (ws / "system.py").read_text() == "machine = 1\n"
    assert git(ws, "status", "--porcelain") == ""
    assert git(ws, "log", "-1", "--format=%s").startswith("undo to ")


# --- a refusal leaves the index and the output clean (010-D11, 009-D15) --------------------------------
LAYERS = {
    "basix": (basix_layer, "apply stopped", "~/basix"),
    "minix": (minix_layer, "apply stopped", "~/minix"),
}


def plant_secret(ws: Path) -> str:
    (ws / "key.pem").write_text("-----BEGIN-----\n")
    return "key.pem looks like a secret; move it out of {folder}"


def plant_nested_repository(ws: Path) -> str:
    inner = ws / "modules" / "sub"
    inner.mkdir(parents=True)
    git(inner, "init", "-q", "-b", "main")
    (inner / "a.txt").write_text("a\n")
    git(inner, "add", "-A")
    git(inner, "commit", "-q", "-m", "inner")
    return "modules/sub holds its own repository, so its files stay hidden; move it out of {folder}"


def plant_symlink_out(ws: Path) -> str:
    (ws / "out").symlink_to("/etc/hostname")
    return "out is a link that leaves {folder}; put the file inside {folder}"


PLANTS = {"secret": plant_secret, "nested repository": plant_nested_repository, "symlink out": plant_symlink_out}


@pytest.mark.parametrize("kind", PLANTS)
@pytest.mark.parametrize("layer_name", LAYERS)
def test_a_refusal_prints_one_line_and_leaves_the_index_alone(ws: Path, layer_name: str, kind: str) -> None:
    make, stopped, folder = LAYERS[layer_name]
    # A new file that passes stays out of the output too: the refusal is one plain line.
    (ws / "notes.txt").write_text("fine\n")
    # A file that the learner staged on purpose stays staged: the index returns to its state before the stage.
    (ws / "wanted.txt").write_text("wanted\n")
    git(ws, "add", "wanted.txt")
    index_before = git(ws, "ls-files", "-s")
    head_before = git(ws, "rev-parse", "HEAD")
    text = PLANTS[kind](ws)
    lines: list[str] = []
    assert engine(ws, lines, make(World()))[0].apply() == 2, lines
    assert lines == [f"{stopped}: " + text.format(folder=folder)]
    assert git(ws, "ls-files", "-s") == index_before
    assert git(ws, "diff", "--cached", "--name-only") == "wanted.txt\n"
    assert git(ws, "rev-parse", "HEAD") == head_before


@pytest.mark.parametrize("kind", PLANTS)
def test_a_raw_commit_after_a_refusal_saves_no_refused_file(ws: Path, kind: str) -> None:
    text = PLANTS[kind](ws)
    refused = text.split(" ")[0]
    assert engine(ws, [])[0].apply() == 2
    (ws / "system.py").write_text("machine = 9\n")
    git(ws, "add", "system.py")
    git(ws, "commit", "-q", "-m", "raw commit")
    assert git(ws, "show", "--name-only", "--format=", "HEAD") == "system.py\n"
    assert refused not in git(ws, "ls-tree", "-r", "--name-only", "HEAD").split()


def test_a_refusal_restores_a_path_that_the_stage_removed(ws: Path) -> None:
    """`git add -A` drops a deleted file from the index. A refusal puts it back."""
    (ws / "system.py").unlink()
    plant_secret(ws)
    index_before = git(ws, "ls-files", "-s")
    lines: list[str] = []
    assert engine(ws, lines)[0].apply() == 2, lines
    assert git(ws, "ls-files", "-s") == index_before


def test_a_late_refusal_restores_the_index_of_the_earlier_stage(ws: Path) -> None:
    """A secret that appears during the build is refused at a later stage. The index keeps the earlier stage."""
    lines: list[str] = []
    eng, runner = engine(ws, lines)

    def plant(argv: Sequence[str]) -> Result:
        (ws / "late.key").write_text("x\n")
        return Result(0, TOP_NEW + "\n")

    runner.fake.on(("nix", "build"), plant)
    assert eng.apply() == 2
    assert lines[-1] == "apply stopped: late.key looks like a secret; move it out of ~/basix"
    assert git(ws, "diff", "--cached", "--name-only") == "system.json\n"  # the compile output of the earlier stage
    assert git(ws, "status", "--porcelain").splitlines() == ["A  system.json", "?? late.key"]


def test_apply_names_the_new_files_after_the_stage(ws: Path) -> None:
    (ws / "notes.txt").write_text("fine\n")
    lines: list[str] = []
    assert engine(ws, lines)[0].apply() == 0, lines
    assert lines[0] == "new files that basix will save: notes.txt"


# --- the git folder of a linked worktree (Gap B) ------------------------------------------------------------
def make_session(ws: Path) -> Session:
    return Session(basix_layer(World()), ws, FakeRunner(), FakeClock(), lambda line: None, {})


@pytest.fixture
def worktrees(ws: Path, tmp_path_factory: pytest.TempPathFactory) -> tuple[Path, Path]:
    """The main checkout and a linked worktree of the same repository."""
    wt = tmp_path_factory.mktemp("linked") / "wt"
    git(ws, "worktree", "add", "-q", "--detach", str(wt))
    return ws, wt


def test_a_clone_keeps_its_state_and_lock_in_the_git_folder(ws: Path) -> None:
    session = make_session(ws)
    assert session.state == ws / ".git" / "basix"
    assert session.lock_path == ws / ".git" / "basix" / "lock"
    assert session.state.is_dir()


def test_two_worktrees_have_two_states_and_one_lock(worktrees: tuple[Path, Path]) -> None:
    main, wt = worktrees
    first, second = make_session(main), make_session(wt)
    assert first.state != second.state
    assert second.state == main / ".git" / "worktrees" / "wt" / "basix"
    assert first.lock_path == second.lock_path == main / ".git" / "basix" / "lock"
    assert first.log_path != second.log_path


def test_one_worktree_holds_the_lock_against_the_other(worktrees: tuple[Path, Path]) -> None:
    main, wt = worktrees
    first, second = make_session(main), make_session(wt)
    handle = first.try_lock()
    assert handle is not None
    assert second.try_lock() is None
    lines: list[str] = []
    assert engine(wt, lines)[0].apply() == 1
    assert lines == [second.word("busy")]
    handle.close()
    again = second.try_lock()
    assert again is not None
    again.close()


def test_try_lock_gives_the_lock_back_when_the_handle_closes(ws: Path) -> None:
    session = make_session(ws)
    handle = session.try_lock()
    assert handle is not None
    handle.close()
    with session.lock_path.open("w") as other:
        fcntl.flock(other, fcntl.LOCK_EX | fcntl.LOCK_NB)


def test_apply_runs_in_a_linked_worktree(worktrees: tuple[Path, Path]) -> None:
    _, wt = worktrees
    (wt / "system.py").write_text("machine = 2\n")
    lines: list[str] = []
    assert engine(wt, lines)[0].apply() == 0, lines
    assert not any("not a basix workspace" in line for line in lines)
    assert lines[-1].startswith("saved")
    assert git(wt, "log", "-1", "--format=%s") != "first\n"
    assert (wt / ".git").is_file()


def test_undo_runs_in_a_linked_worktree(worktrees: tuple[Path, Path]) -> None:
    _, wt = worktrees
    (wt / "system.py").write_text("machine = 2\n")
    assert engine(wt, [])[0].apply() == 0
    (wt / "system.py").write_text("machine = 3\n")
    lines: list[str] = []
    assert engine(wt, lines)[0].undo() == 0, lines
    assert not any("not a basix workspace" in line for line in lines)
    assert (wt / "system.py").read_text() == "machine = 2\n"


def test_the_log_of_a_worktree_lies_in_its_own_git_folder(worktrees: tuple[Path, Path]) -> None:
    main, wt = worktrees
    (wt / "system.py").write_text("machine = 2\n")
    assert engine(wt, [])[0].apply() == 0
    assert (main / ".git" / "worktrees" / "wt" / "basix" / "last.log").is_file()
    assert not (main / ".git" / "basix" / "last.log").exists()


def test_a_bad_dot_git_file_prints_the_plain_line(tmp_path: Path) -> None:
    (tmp_path / ".git").write_text("this is not a pointer\n")
    lines: list[str] = []
    eng, runner = engine(tmp_path, lines)
    assert eng.apply() == 1
    assert eng.undo() == 1
    assert lines == [f"{tmp_path} is not a basix workspace. Go to ~/basix first."] * 2
    assert runner.git_calls == []
    assert runner.fake.calls == []
