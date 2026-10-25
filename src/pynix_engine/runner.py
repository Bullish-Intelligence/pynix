"""The seam for every outside effect: one runner for commands, one clock for time (009-D26).

The engine calls `Runner.run` for every subprocess. Tests pass a fake runner. Real use passes `SubprocessRunner`.
"""

import subprocess
import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class Result:
    """The exit code of a command, and its output (stdout and stderr together)."""

    code: int
    out: str = ""


class Runner(Protocol):
    def run(
        self, argv: Sequence[str], *, cwd: Path | None = None, on_line: Callable[[str], None] | None = None
    ) -> Result:
        """Run a command. Call `on_line` with each output line (no newline) while the command runs."""
        ...


class Clock(Protocol):
    def now(self) -> float: ...

    def sleep(self, seconds: float) -> None: ...


class SubprocessRunner:
    """Run real commands. A missing program gives exit code 127."""

    def run(
        self, argv: Sequence[str], *, cwd: Path | None = None, on_line: Callable[[str], None] | None = None
    ) -> Result:
        try:
            proc = subprocess.Popen(
                list(argv), cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, errors="replace"
            )
        except FileNotFoundError:
            line = f"{argv[0]}: command not found"
            if on_line:
                on_line(line)
            return Result(127, line + "\n")
        lines: list[str] = []
        assert proc.stdout is not None
        for raw in proc.stdout:
            lines.append(raw)
            if on_line:
                on_line(raw.rstrip("\n"))
        return Result(proc.wait(), "".join(lines))


class SystemClock:
    """The real clock. `now` is monotonic."""

    def now(self) -> float:
        return time.monotonic()

    def sleep(self, seconds: float) -> None:
        time.sleep(seconds)
