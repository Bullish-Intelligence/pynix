"""Find the git folders of a workspace. The code reads files and starts no other process.

A normal clone has a `.git` folder. A linked worktree, a submodule, and a repository made with
`--separate-git-dir` have a `.git` file instead. That file holds one line: `gitdir: PATH`.
"""

from pathlib import Path

_PREFIX = "gitdir:"


def git_dirs(ws: Path) -> tuple[Path, Path] | None:
    """Return `(git_dir, common_dir)` as absolute paths, or None when `ws` is not a git workspace.

    `git_dir` belongs to this checkout. `common_dir` is shared by all worktrees of one repository.
    In a normal clone both are `ws/.git`.
    """
    dot_git = ws / ".git"
    if dot_git.is_dir():
        folder = dot_git.absolute()
        return folder, folder
    if not dot_git.is_file():
        return None
    git_dir = _read_gitdir(dot_git, ws)
    if git_dir is None:
        return None
    return git_dir, _read_commondir(git_dir)


def _read_gitdir(dot_git: Path, ws: Path) -> Path | None:
    try:
        text = dot_git.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    for line in text.splitlines():
        if not line.startswith(_PREFIX):
            continue
        value = line[len(_PREFIX) :].strip()
        if not value:
            return None
        target = (ws.absolute() / value).resolve()
        return target if target.is_dir() else None
    return None


def _read_commondir(git_dir: Path) -> Path:
    try:
        value = (git_dir / "commondir").read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError):
        return git_dir
    if not value:
        return git_dir
    return (git_dir / value).resolve()
