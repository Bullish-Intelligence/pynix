"""Fakes for the tests of the engine and of the commands that use it: a fake runner, a fake clock, and a fake git.

`FakeRunner` records every call and answers from rules. A later rule beats an earlier one. `FakeGit` answers the
git calls of the engine from a few plain fields, so a test sets the state and reads the commits.
"""

from collections.abc import Callable, Sequence
from pathlib import Path

from .runner import Result

Argv = tuple[str, ...]
Responder = Callable[[Argv], Result]
Handler = Callable[[Argv], Result | None]


def _fixed(result: Result) -> Responder:
    def respond(argv: Argv) -> Result:
        return result

    return respond


def _in_turn(queue: list[Result]) -> Responder:
    def respond(argv: Argv) -> Result:
        return queue.pop(0) if len(queue) > 1 else queue[0]

    return respond


class FakeClock:
    """A clock that moves only when the code sleeps. The tests never wait for real."""

    def __init__(self, start: float = 0.0) -> None:
        self.time = start
        self.slept: list[float] = []

    def now(self) -> float:
        return self.time

    def sleep(self, seconds: float) -> None:
        self.slept.append(seconds)
        self.time += seconds


class FakeRunner:
    def __init__(self) -> None:
        self.calls: list[Argv] = []
        self.cwds: list[Path | None] = []
        self._handlers: list[Handler] = []

    def add(self, handler: Handler) -> None:
        """Add a handler that beats all earlier ones. It returns None to pass the call on."""
        self._handlers.insert(0, handler)

    def on(self, prefix: Sequence[str], answer: Result | Responder) -> None:
        """Answer every call that starts with `prefix`."""
        start = tuple(prefix)
        respond = _fixed(answer) if isinstance(answer, Result) else answer

        def handler(argv: Argv) -> Result | None:
            return respond(argv) if argv[: len(start)] == start else None

        self.add(handler)

    def on_turns(self, prefix: Sequence[str], *answers: Result) -> None:
        """Answer the calls that start with `prefix` one result at a time. The last result repeats."""
        self.on(prefix, _in_turn(list(answers)))

    def run(
        self, argv: Sequence[str], *, cwd: Path | None = None, on_line: Callable[[str], None] | None = None
    ) -> Result:
        call = tuple(argv)
        self.calls.append(call)
        self.cwds.append(cwd)
        result = Result(0, "")
        for handler in self._handlers:
            answered = handler(call)
            if answered is not None:
                result = answered
                break
        if on_line:
            for line in result.out.splitlines():
                on_line(line)
        return result

    # --- reading the record -------------------------------------------------------------------
    def ran(self, *prefix: str) -> bool:
        return self.index(*prefix) is not None

    def index(self, *prefix: str) -> int | None:
        """The position of the first call that starts with `prefix`."""
        for position, call in enumerate(self.calls):
            if call[: len(prefix)] == prefix:
                return position
        return None

    def count(self, *prefix: str) -> int:
        return sum(1 for call in self.calls if call[: len(prefix)] == prefix)

    def words(self, prefix: str = "") -> list[str]:
        """Every call as one line of text, filtered by the start of the line."""
        return [line for line in (" ".join(call) for call in self.calls) if line.startswith(prefix)]


class FakeGit:
    """The git state that the engine reads. Set the fields, run the engine, read `commits` and `refs`."""

    def __init__(self, runner: FakeRunner) -> None:
        self.entries: list[tuple[str, str]] = [("100644", "system.py")]
        self.new_files: list[str] = []
        self.staged: list[str] = ["system.py"]
        self.tree = "tree-new"
        self.head_tree = "tree-head"
        self.has_head = True
        self.has_parent = True
        self.identity = True
        self.restored_staged: list[str] = []
        self.commits: list[str] = []
        self.commit_calls: list[Argv] = []
        self.refs: dict[str, str] = {}
        runner.add(self._handle)

    def _handle(self, argv: Argv) -> Result | None:
        if not argv or argv[0] != "git":
            return None
        args = list(argv[1:])
        while args[:1] == ["-c"]:
            args = args[2:]
        head = " ".join(args[:2])
        if head == "add -A":
            return Result(0)
        if args[:1] == ["write-tree"]:
            return Result(0, self.tree + "\n")
        if args[:3] == ["ls-files", "-s", "-z"]:
            return Result(0, "".join(f"{mode} 0000 0\t{path}\0" for mode, path in self.entries))
        if args[:2] == ["ls-files", "--others"]:
            return Result(0, "\n".join(self.new_files))
        if args[:2] == ["diff", "--cached"]:
            return Result(0, "\n".join(self.staged))
        if args[:1] == ["config"]:
            return Result(0 if self.identity else 1)
        if args[:1] == ["rev-parse"]:
            return self._rev_parse(args[1:])
        if head == "stash create":
            return Result(0, "deadbeefcafe0000\n")
        if args[:1] == ["update-ref"]:
            self.refs[args[1]] = args[2]
            return Result(0)
        if args[:1] == ["restore"]:
            self.tree = self.head_tree if args[1] == "--source=HEAD" else "tree-parent"
            self.staged = list(self.restored_staged)
            return Result(0)
        if args[:3] == ["commit", "-q", "-m"]:
            self.commits.append(args[3])
            self.commit_calls.append(argv)
            self.head_tree = self.tree
            self.staged = []
            return Result(0)
        return Result(0)

    def _rev_parse(self, args: list[str]) -> Result:
        if args == ["--verify", "-q", "HEAD"]:
            return Result(0 if self.has_head else 1)
        if args == ["--verify", "-q", "HEAD~1"]:
            return Result(0 if self.has_parent else 1)
        if args == ["HEAD^{tree}"]:
            return Result(0, self.head_tree + "\n")
        if args[:1] == ["--short"]:
            return Result(0, "abc1234\n")
        return Result(0)
