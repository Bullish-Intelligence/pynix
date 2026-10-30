"""`git_dirs` against real git: a clone, a linked worktree, a separate git folder, and a submodule.

Each case compares the answer with `git rev-parse`. The None cases cover a missing, broken, or unreadable `.git`.
"""

import os
import subprocess
from pathlib import Path

import pytest

from pynix_engine import git_dirs

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.org",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.org",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


@pytest.fixture(autouse=True)
def clean_git_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """Give the test repositories their own identity: no outer GIT_* variable reaches them."""
    for key in [k for k in os.environ if k.startswith("GIT_")]:
        monkeypatch.delenv(key)
    for key, value in GIT_ENV.items():
        monkeypatch.setenv(key, value)


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def make_repo(path: Path) -> Path:
    path.mkdir(parents=True)
    git(path, "init", "-q", "-b", "main")
    (path / "a.txt").write_text("a\n")
    git(path, "add", "-A")
    git(path, "commit", "-q", "-m", "first")
    return path


def expected(ws: Path) -> tuple[Path, Path]:
    """What git itself says: the git folder and the common folder, both resolved."""
    git_dir = Path(git(ws, "rev-parse", "--absolute-git-dir")).resolve()
    common = Path(git(ws, "rev-parse", "--git-common-dir"))
    return git_dir, (ws / common).resolve()


def test_a_clone_has_one_folder(tmp_path: Path) -> None:
    ws = make_repo(tmp_path / "repo")
    assert git_dirs(ws) == (ws / ".git", ws / ".git")
    assert git_dirs(ws) == expected(ws)


def test_a_linked_worktree_has_its_own_git_folder_and_the_common_one(tmp_path: Path) -> None:
    main = make_repo(tmp_path / "main")
    wt = tmp_path / "wt"
    git(main, "worktree", "add", "-q", "--detach", str(wt))
    assert (wt / ".git").is_file()
    found = git_dirs(wt)
    assert found == expected(wt)
    assert found == (main / ".git" / "worktrees" / "wt", main / ".git")


def test_a_relative_gitdir_line_counts_from_the_workspace(tmp_path: Path) -> None:
    main = make_repo(tmp_path / "main")
    wt = tmp_path / "wt"
    git(main, "worktree", "add", "-q", "--detach", str(wt))
    (wt / ".git").write_text("gitdir: ../main/.git/worktrees/wt\n")
    assert git_dirs(wt) == expected(wt)


def test_a_separate_git_dir(tmp_path: Path) -> None:
    ws = tmp_path / "ws"
    ws.mkdir()
    store = tmp_path / "store.git"
    git(ws, "init", "-q", "-b", "main", "--separate-git-dir", str(store))
    assert (ws / ".git").is_file()
    assert git_dirs(ws) == (store, store)
    assert git_dirs(ws) == expected(ws)


def test_a_submodule(tmp_path: Path) -> None:
    inner = make_repo(tmp_path / "inner")
    outer = make_repo(tmp_path / "outer")
    git(outer, "-c", "protocol.file.allow=always", "submodule", "add", "-q", str(inner), "sub")
    sub = outer / "sub"
    assert (sub / ".git").is_file()
    found = git_dirs(sub)
    assert found == expected(sub)
    assert found is not None
    assert found[0] == found[1] == outer / ".git" / "modules" / "sub"


@pytest.mark.parametrize(
    "content",
    [None, "", "no marker here\n", "gitdir:\n", "gitdir: missing/folder\n", "GITDIR: x\n"],
)
def test_a_bad_dot_git_file_gives_none(tmp_path: Path, content: str | None) -> None:
    ws = tmp_path / "ws"
    ws.mkdir()
    if content is not None:
        (ws / ".git").write_text(content)
    assert git_dirs(ws) is None


def test_a_gitdir_that_names_a_file_gives_none(tmp_path: Path) -> None:
    ws = tmp_path / "ws"
    ws.mkdir()
    (tmp_path / "plain").write_text("x\n")
    (ws / ".git").write_text("gitdir: ../plain\n")
    assert git_dirs(ws) is None


def test_a_missing_workspace_gives_none(tmp_path: Path) -> None:
    assert git_dirs(tmp_path / "nowhere") is None


def test_a_commondir_file_may_hold_a_relative_path(tmp_path: Path) -> None:
    git_dir = tmp_path / "gd"
    git_dir.mkdir()
    (tmp_path / "common").mkdir()
    (git_dir / "commondir").write_text("../common\n")
    ws = tmp_path / "ws"
    ws.mkdir()
    (ws / ".git").write_text(f"gitdir: {git_dir}\n")
    assert git_dirs(ws) == (git_dir, tmp_path / "common")
