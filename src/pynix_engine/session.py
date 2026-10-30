"""One run of a command: the workspace, the runner, the clock, and the log (009-D15).

Every plain line and every command goes into `NAME/last.log` in the git folder of the workspace. With `verbose` the
session also prints them.

The git folder is `ws/.git` in a normal clone. In a linked worktree it is the folder that the `.git` file names.
`state` belongs to one checkout: the log, the compiler, the result, and the inputs. `lock_path` lies in the common
git folder, so all worktrees of one repository share one lock. In a normal clone both lie in `ws/.git/NAME`.
"""

import fcntl
import os
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import TextIO

from .gitdir import git_dirs
from .layer import EXIT_FAILED, Layer
from .runner import Clock, Result, Runner


class Fail(Exception):
    """A run that stops. The message is the plain text for the learner. `code` is the exit code."""

    def __init__(self, message: str, code: int = EXIT_FAILED) -> None:
        super().__init__(message)
        self.code = code


class Session:
    def __init__(
        self,
        layer: Layer,
        ws: Path,
        runner: Runner,
        clock: Clock,
        say: Callable[[str], None],
        env: Mapping[str, str],
        verbose: bool = False,
    ) -> None:
        self.layer = layer
        self.ws = ws
        self.runner = runner
        self.clock = clock
        self.env = env
        self.verbose = verbose
        self._say = say
        dirs = git_dirs(ws)
        if dirs is None:
            raise Fail(layer.text("not_a_workspace", path=str(ws)))
        git_dir, common_dir = dirs
        self.state = git_dir / layer.name
        self.lock_path = common_dir / layer.name / "lock"
        self.state.mkdir(parents=True, exist_ok=True)
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        self.log_path = self.state / "last.log"
        self._log: TextIO | None = None
        self.identity_known = True

    def try_lock(self) -> TextIO | None:
        """Take the lock of the repository: one run at a time. Return the open handle, or None when another run holds it."""
        handle = self.lock_path.open("w")
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            handle.close()
            return None
        return handle

    def open_log(self) -> None:
        """Start a fresh log. Call it only while you hold the lock, so a busy run keeps the log of the first run."""
        self._log = self.log_path.open("w", encoding="utf-8")

    def close(self) -> None:
        if self._log:
            self._log.close()
            self._log = None

    def _write(self, line: str) -> None:
        if self._log:
            self._log.write(line + "\n")
            self._log.flush()

    def log(self, line: str) -> None:
        self._write(line)
        if self.verbose:
            self._say(line)

    def say(self, text: str = "") -> None:
        """Print a plain line. The log gets it too."""
        self._write(text)
        self._say(text)

    def word(self, key: str, **values: object) -> str:
        return self.layer.text(key, **values)

    def run(self, argv: Sequence[str], *, cwd: Path | None = None, quiet: bool = False) -> Result:
        """Run a command in the workspace (or `cwd`). `quiet` leaves the command out of the log (the health polls)."""
        where = cwd or self.ws
        if quiet:
            return self.runner.run(argv, cwd=where)
        self.log("$ " + " ".join(argv))
        result = self.runner.run(argv, cwd=where, on_line=lambda line: self.log("    " + line))
        self.log(f"(exit {result.code})")
        return result

    def git(self, *args: str, check: bool = True) -> Result:
        result = self.run(["git", *args])
        if check and result.code != 0:
            raise Fail(f"git {' '.join(args[:2])} failed (exit {result.code}):\n{result.out.strip()}")
        return result

    def display(self, path: Path) -> str:
        """A path for the learner: relative to the workspace when it lies inside."""
        try:
            return str(path.relative_to(self.ws))
        except ValueError:
            return str(path)


def print_flush(text: str) -> None:
    print(text, flush=True)


def default_env() -> Mapping[str, str]:
    return os.environ
