"""The engine: `apply` and `undo` for one layer in one workspace (009-D26, CONCEPT section 4).

Order of an apply: lock, stage, compile, stage, build, switch, health check, finish, commit.
Order of an undo: lock, restore the files, then the apply above.
"""

from collections.abc import Callable, Mapping
from pathlib import Path
from typing import TextIO

from . import steps
from .gitdir import git_dirs
from .layer import EXIT_CHANGED, EXIT_FAILED, EXIT_UNHEALTHY, Layer, Plan
from .runner import Clock, Runner, SubprocessRunner, SystemClock
from .session import Fail, Session, default_env, print_flush


class Engine:
    def __init__(
        self,
        layer: Layer,
        ws: Path,
        *,
        runner: Runner | None = None,
        clock: Clock | None = None,
        say: Callable[[str], None] = print_flush,
        env: Mapping[str, str] | None = None,
        verbose: bool = False,
    ) -> None:
        self.layer = layer
        self.ws = ws
        self.runner = runner or SubprocessRunner()
        self.clock = clock or SystemClock()
        self.say = say
        self.env = default_env() if env is None else env
        self.verbose = verbose

    def apply(self) -> int:
        """Build the machine (or home) from the files, switch to it, check it, then save the files. Return the exit code."""
        return self._run(lambda session, on_fail: self._apply(session, on_fail, None))

    def undo(self) -> int:
        """Drop an edit that was not applied; else go back to the save before the last one. Then apply."""
        return self._run(self._undo)

    # --- the run ------------------------------------------------------------------------------
    def _run(self, body: Callable[[Session, str], int]) -> int:
        if git_dirs(self.ws) is None:
            self.say(self.layer.text("not_a_workspace", path=str(self.ws)))
            return EXIT_FAILED
        session = Session(self.layer, self.ws, self.runner, self.clock, self.say, self.env, self.verbose)
        lock = self._lock(session)
        if lock is None:
            self.say(session.word("busy"))
            return EXIT_FAILED
        try:
            session.open_log()
            on_fail = self._on_fail(session)
            if self.layer.preflight:
                self.layer.preflight(session)
            steps.check_identity(session)
            return body(session, on_fail)
        except Fail as failure:
            session.say(str(failure))
            return failure.code
        finally:
            lock.close()
            session.close()

    def _on_fail(self, session: Session) -> str:
        """What to do after a failed switch or check: `rollback` (default) or `keep`."""
        value = self.env.get(self.layer.on_fail_env, "rollback")
        if value not in ("rollback", "keep"):
            raise Fail(session.word("bad_on_fail", env=self.layer.on_fail_env, value=value))
        return value

    def _lock(self, session: Session) -> TextIO | None:
        """Take the lock of the repository: one apply at a time. Return None when another run holds it."""
        return session.try_lock()

    # --- apply --------------------------------------------------------------------------------
    def _apply(self, session: Session, on_fail: str, message: str | None) -> int:
        layer = self.layer
        fresh = steps.new_files(session)
        steps.stage(session)  # the refusals run before Nix reads any file
        if fresh:  # a refusal is one plain line, so name the files only after the stage passes
            session.say(session.word("new_files", names=", ".join(fresh)))
        (layer.compile or steps.default_compile)(session)
        session.say(session.word("checked"))
        tree = steps.stage(session)

        session.say(session.word("building"))
        built = steps.build(session)
        session.say(session.word("built"))
        if steps.stage(session) != tree:
            raise Fail(session.word("changed_build"), EXIT_CHANGED)

        self._pin_check(session, built)
        plan = layer.plan(session, built)
        if plan.unchanged and not steps.staged_names(session):
            session.say(session.word("nothing"))
            return 0
        if plan.unchanged:
            session.say(session.word("files_only"))
        else:
            self._switch(session, plan, on_fail)

        if steps.stage(session) != tree:
            raise Fail(session.word("changed_switch"), EXIT_CHANGED)
        names = steps.staged_names(session)
        if not names:
            session.say(session.word("nothing"))
            return 0
        if message:
            steps.commit(session, message, session.word("undone"))
        else:
            steps.commit(session, steps.commit_message(names), ", ".join(names[:5]))
        return 0

    def _pin_check(self, session: Session, built: str) -> None:
        """Say the warning lines of `Layer.pin_check`. A warning never stops the apply, so no error leaves this method."""
        check = self.layer.pin_check
        if check is None:
            return
        try:
            lines = [str(line) for line in check(session, built)]
        except Exception as error:  # noqa: BLE001 - a warning must never break an apply
            session.log(f"the pin check failed and was skipped: {type(error).__name__}: {error}")
            return
        for line in lines:
            session.say(line)

    def _switch(self, session: Session, plan: Plan, on_fail: str) -> None:
        reason = steps.switch_and_check(session, plan)
        if reason is None:
            session.say(session.word("applied"))
            return
        session.say(session.word("problem", reason=reason))
        if on_fail == "keep":
            raise Fail(session.word("failed_keep"), EXIT_UNHEALTHY)
        raise Fail(session.word("failed_rollback", what=steps.roll_back(session, plan)), EXIT_UNHEALTHY)

    # --- undo ---------------------------------------------------------------------------------
    def _undo(self, session: Session, on_fail: str) -> int:
        message = steps.restore_for_undo(session)
        return self._apply(session, on_fail, message)
