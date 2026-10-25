"""The apply of the engine, with the fake runner: the order of the calls, the stops, and the failures.

Case names follow the S12 (Basix) and S16 (minix) runs where they fit.
"""

import fcntl
import os
from pathlib import Path

import pytest
from test_engine_support import (
    BAD_UNITS,
    COMPILER,
    HEALTH,
    HEALTH_USER,
    SUDO,
    TOP_NEW,
    TOP_OLD,
    Setup,
    basix_layer,
    make_setup,
    minix_layer,
)

from pynix_engine import Fail, Result, Session, SubprocessRunner, default_compile
from pynix_engine.engine import Engine


@pytest.fixture
def s(tmp_path: Path) -> Setup:
    return make_setup(tmp_path)


# --- the clean apply (S12 1a, 1b; S16 1, 3) ----------------------------------------------------------
def test_clean_apply_order_for_basix(s: Setup) -> None:
    """L123: reset, build, `test`, the check, the profile, `boot`, then the commit."""
    assert s.engine().apply() == 0
    assert s.trace() == ["build", "reset", "test", "health", "profile", "boot", "commit"]
    assert s.git.commits == ["apply: system.py"]
    assert s.lines[-1] == "saved: system.py"
    assert "Basix needs your password to change the machine" in s.lines
    # The new system is the boot default only after the check passed.
    words = s.runner.words()
    boot = words.index(f"{SUDO} {TOP_NEW}/bin/switch-to-configuration boot")
    assert words.index(" ".join(HEALTH)) < boot


def test_clean_apply_order_for_minix(s: Setup) -> None:
    s.world.running = TOP_OLD
    assert s.engine(minix_layer(s.world)).apply() == 0
    assert s.trace() == ["build", "reset", "activate", "health", "commit"]
    assert s.runner.ran(f"{TOP_NEW}/activate")
    assert not any(call[0] == SUDO for call in s.runner.calls)


def test_stage_runs_first_and_the_compile_runs_before_the_build(s: Setup) -> None:
    s.engine().apply()
    first_add = s.runner.index("git", "add", "-A")
    assert first_add is not None
    assert first_add < (s.runner.index("nix", "build") or 0)
    assert (s.ws / "system.json").read_text() == "{}\n"


def test_build_is_one_nix_build_with_an_out_link_and_no_eval(s: Setup) -> None:
    s.engine().apply()
    builds = [call for call in s.runner.calls if call[:2] == ("nix", "build")]
    assert len(builds) == 1
    assert builds[0][-1] == ".#nixosConfigurations.basix.config.system.build.toplevel"
    assert builds[0][builds[0].index("--out-link") + 1] == str(s.ws / ".git" / "basix" / "result")
    assert not s.runner.ran("nix", "eval")


def test_build_command_wraps_the_build_for_root(s: Setup) -> None:
    """L134: the layer runs the build as root with `--option` values."""
    layer = basix_layer(
        s.world, build_command=lambda argv: [SUDO, *argv, "--option", "extra-substituters", "https://c"]
    )
    s.engine(layer).apply()
    build = next(call for call in s.runner.calls if "build" in call[:3] and call[0] == SUDO)
    assert build[-3:] == ("--option", "extra-substituters", "https://c")


def test_the_layer_gets_the_built_result(s: Setup) -> None:
    s.engine().apply()
    assert s.world.plan_calls == [TOP_NEW]


# --- nothing to change (S12 "No change", S16 case 2) -------------------------------------------------
def test_nothing_to_change(s: Setup) -> None:
    s.world.running = s.world.boot_default = TOP_NEW
    s.git.staged = []
    assert s.engine().apply() == 0
    assert s.lines[-1] == "nothing to change"
    assert s.trace() == ["build"]
    assert s.git.commits == []


def test_same_system_but_new_files_are_saved_without_a_switch(s: Setup) -> None:
    s.world.running = s.world.boot_default = TOP_NEW
    s.git.staged = ["system.json"]
    assert s.engine().apply() == 0
    assert s.trace() == ["build", "commit"]
    assert "the system is the same; only files changed" in s.lines


def test_switch_and_check_run_when_only_the_boot_default_differs(s: Setup) -> None:
    s.world.running = TOP_NEW
    s.world.boot_default = TOP_OLD
    s.git.staged = []
    assert s.engine().apply() == 0
    assert s.trace() == ["build", "reset", "test", "health", "profile", "boot"]
    assert s.lines[-1] == "nothing to change"


def test_nothing_to_commit_after_a_switch(s: Setup) -> None:
    s.git.staged = []
    assert s.engine().apply() == 0
    assert s.lines[-1] == "nothing to change"
    assert s.git.commits == []


def test_new_files_are_named_before_they_are_saved(s: Setup) -> None:
    s.git.new_files = ["notes.txt", "extra.nix"]
    s.engine().apply()
    assert "new files that basix will save: notes.txt, extra.nix" in s.lines


# --- a compile error (S12 2; S16 4, 9) ---------------------------------------------------------------
def test_compile_error_stops_before_any_build(s: Setup) -> None:
    line = "system.py:5:10: Machine.user must be an account name (a lower case letter), found 42."

    def compile_fails(session: Session) -> None:
        raise Fail(line, 2)

    assert s.engine(basix_layer(s.world, compile=compile_fails)).apply() == 2
    assert s.lines[-1] == line
    assert s.trace() == []
    assert s.git.commits == []


# --- the default compile -----------------------------------------------------------------------------
def compiler_answers(s: Setup, *, builds: bool = True, run: Result | None = None) -> None:
    tool = f"{COMPILER}/bin/basix-compile"

    def compiler_build(argv: tuple[str, ...]) -> Result:
        if argv[-1] == ".#compiler":
            return Result(0, COMPILER + "\n") if builds else Result(1, "error: cannot build the compiler\n")
        return Result(0, TOP_NEW + "\n")

    def run_tool(argv: tuple[str, ...]) -> Result:
        if run is not None:
            return run
        Path(argv[2]).write_text('{"source_sha256": "x"}\n')
        return Result(0)

    s.runner.on(("nix", "build"), compiler_build)
    s.runner.on((tool,), run_tool)


def test_default_compile_roots_the_compiler_and_writes_the_json(s: Setup) -> None:
    compiler_answers(s)
    assert s.engine(basix_layer(s.world, compile=None)).apply() == 0
    assert s.trace()[:3] == ["lock", "compiler", "build"]
    compile_call = next(call for call in s.runner.calls if call[-1] == ".#compiler")
    assert compile_call[compile_call.index("--out-link") + 1] == str(s.ws / ".git" / "basix" / "compiler")
    assert (s.ws / "system.json").read_text() == '{"source_sha256": "x"}\n'
    assert not (s.ws / "system.json.new").exists()
    assert "checked: system.py" in s.lines


def test_default_compile_prints_the_one_line_of_the_compiler(s: Setup) -> None:
    line = "system.py:4:10: syntax error: invalid syntax. Perhaps you forgot a comma?"
    compiler_answers(s, run=Result(1, line + "\n"))
    (s.ws / "system.json").write_text("old\n")
    assert s.engine(basix_layer(s.world, compile=None)).apply() == 2
    assert s.lines[-1] == line
    assert (s.ws / "system.json").read_text() == "old\n"
    assert not (s.ws / "system.json.new").exists()
    assert "build" not in s.trace()


def test_default_compile_uses_the_rooted_compiler_when_the_build_fails(s: Setup) -> None:
    compiler_answers(s, builds=False)
    old = s.ws / ".git" / "basix" / "compiler" / "bin" / "basix-compile"
    old.parent.mkdir(parents=True)
    old.write_text("")
    s.runner.on((str(old),), lambda argv: _write_json(argv))
    assert s.engine(basix_layer(s.world, compile=None)).apply() == 0
    assert "the compiler could not be built, so basix uses the compiler of the last good build" in s.lines


def _write_json(argv: tuple[str, ...]) -> Result:
    Path(argv[2]).write_text("{}\n")
    return Result(0)


def test_default_compile_stops_when_no_compiler_exists(s: Setup) -> None:
    compiler_answers(s, builds=False)
    assert s.engine(basix_layer(s.world, compile=None)).apply() == 2
    assert s.lines[-1].startswith("The compiler could not be built. Nothing was built, switched, or saved.")
    assert "build" not in s.trace()


def test_default_compile_is_the_function_that_the_engine_uses_for_none(s: Setup) -> None:
    assert basix_layer(s.world, compile=None).compile is None
    assert callable(default_compile)


# --- a failed build (the earlier state stays) --------------------------------------------------------
def test_failed_build_changes_nothing(s: Setup) -> None:
    error = (
        "error: builder for '/nix/store/dddddddddddddddddddddddddddddddd-web.drv' failed with exit code 1\n"
        "error: Cannot build '/nix/store/dddddddddddddddddddddddddddddddd-web.drv'.\n"
        "       Reason: builder failed with exit code 1.\n"
    )
    s.runner.on(("nix", "build"), Result(1, error))
    assert s.engine().apply() == 2
    assert s.trace() == ["build"]  # no reset, no switch, no profile change
    assert s.git.commits == []
    assert s.world.running == TOP_OLD
    message = s.lines[-1]
    assert message.startswith("The build failed. Nothing was switched or saved. The system did not change.")
    assert "/nix/store" not in message
    assert "(full log: .git/basix/last.log)" in message


def test_a_build_with_no_result_path_stops(s: Setup) -> None:
    s.runner.on(("nix", "build"), Result(0, ""))
    assert s.engine().apply() == 2
    assert s.trace() == ["build"]


# --- a file changes during the run -------------------------------------------------------------------
def test_file_changed_during_build(s: Setup) -> None:
    s.runner.on_turns(("git", "write-tree"), Result(0, "t1\n"), Result(0, "t1\n"), Result(0, "t2\n"))
    assert s.engine().apply() == 4
    assert s.trace() == ["build"]
    assert "A file changed while basix built the system" in s.lines[-1]


def test_file_changed_during_switch(s: Setup) -> None:
    s.runner.on_turns(("git", "write-tree"), Result(0, "t1\n"), Result(0, "t1\n"), Result(0, "t1\n"), Result(0, "t2\n"))
    assert s.engine().apply() == 4
    assert s.git.commits == []
    assert "Nothing was saved. Run basix apply again." in s.lines[-1]


# --- a failed switch or check (S12 L123; S16 case 5) --------------------------------------------------
def test_failed_health_check_rolls_back_and_commits_nothing(s: Setup) -> None:
    s.runner.on(HEALTH, Result(0, BAD_UNITS))
    assert s.engine().apply() == 3
    # `test` again with the old system; no profile change, no `boot`, no commit.
    assert s.trace() == ["build", "reset", "test", "health", "test"]
    assert s.runner.words(f"{SUDO} {TOP_OLD}/bin/switch-to-configuration test")
    assert not s.runner.ran(SUDO, "nix-env")
    assert s.git.commits == []
    assert "problem: failed units: web.service" in s.lines
    assert s.lines[-1].startswith("failed: the earlier system is back. Nothing was saved.")
    assert "run basix undo to drop the edit" in s.lines[-1]


def test_failed_health_check_with_keep_leaves_the_new_state(s: Setup) -> None:
    s.runner.on(HEALTH, Result(0, BAD_UNITS))
    assert s.engine(env={"BASIX_ON_FAIL": "keep"}).apply() == 3
    assert s.trace() == ["build", "reset", "test", "health"]
    assert s.git.commits == []
    assert s.lines[-1].startswith("failed: the new system is running, but it did not start cleanly.")


def test_failed_switch_command_rolls_back_without_a_check(s: Setup) -> None:
    s.runner.on((SUDO, f"{TOP_NEW}/bin/switch-to-configuration", "test"), Result(1, "boom\n"))
    assert s.engine().apply() == 3
    assert s.trace() == ["build", "reset", "test", "test"]
    assert "problem: the system did not switch (exit 1)" in s.lines


def test_failed_boot_step_rolls_back(s: Setup) -> None:
    s.runner.on((SUDO, f"{TOP_NEW}/bin/switch-to-configuration", "boot"), Result(1, ""))
    assert s.engine().apply() == 3
    assert s.git.commits == []
    assert s.trace()[-1] == "test"


def test_minix_rolls_back_to_the_last_good_activation(s: Setup) -> None:
    s.runner.on(HEALTH_USER, Result(0, BAD_UNITS))
    assert s.engine(minix_layer(s.world)).apply() == 3
    assert s.trace() == ["build", "reset", "activate", "health", "activate"]
    assert s.runner.calls[-1] == (f"{TOP_OLD}/activate",)
    assert s.lines[-1].startswith("failed: the earlier home is back.")
    assert s.git.commits == []


def test_minix_keep(s: Setup) -> None:
    s.runner.on(HEALTH_USER, Result(0, BAD_UNITS))
    assert s.engine(minix_layer(s.world), env={"MINIX_ON_FAIL": "keep"}).apply() == 3
    assert s.trace() == ["build", "reset", "activate", "health"]


def test_no_earlier_state_to_return_to(s: Setup) -> None:
    s.world.running = ""
    s.runner.on(HEALTH_USER, Result(0, BAD_UNITS))
    assert s.engine(minix_layer(s.world)).apply() == 3
    assert "found no earlier home to return to, so the new home stays" in s.lines[-1]


def test_a_failed_roll_back_is_said(s: Setup) -> None:
    s.runner.on(HEALTH, Result(0, BAD_UNITS))
    s.runner.on((SUDO, f"{TOP_OLD}/bin/switch-to-configuration", "test"), Result(1, ""))
    assert s.engine().apply() == 3
    assert "tried to roll back, but that also failed (exit 1)" in s.lines[-1]


def test_a_wrong_on_fail_value_stops_before_any_call(s: Setup) -> None:
    assert s.engine(env={"BASIX_ON_FAIL": "maybe"}).apply() == 1
    assert s.lines == ["BASIX_ON_FAIL must be rollback or keep, found maybe."]
    assert s.runner.calls == []


# --- the guards of the run ----------------------------------------------------------------------------
def test_preflight_stops_before_a_change(s: Setup) -> None:
    def no_terminal(session: Session) -> None:
        raise Fail("sudo needs your password and there is no terminal. Run basix in a terminal window.")

    assert s.engine(basix_layer(s.world, preflight=no_terminal)).apply() == 1
    assert s.lines == ["sudo needs your password and there is no terminal. Run basix in a terminal window."]
    assert s.runner.calls == []


def test_unknown_author_stops_when_the_layer_has_no_fallback(s: Setup) -> None:
    s.git.identity = False
    assert s.engine().apply() == 1
    assert s.lines[-1].startswith("git does not know your name.")
    assert not s.runner.ran("nix")


def test_unknown_author_uses_the_fallback_of_the_layer(s: Setup) -> None:
    s.git.identity = False
    assert s.engine(minix_layer(s.world)).apply() == 0
    commit = s.git.commit_calls[0]
    assert commit[:5] == ("git", "-c", "user.name=minix", "-c", "user.email=minix@localhost")


def test_a_second_run_waits_and_keeps_the_log_of_the_first(s: Setup) -> None:
    state = s.ws / ".git" / "basix"
    state.mkdir()
    (state / "last.log").write_text("first run\n")
    with (state / "lock").open("w") as holder:
        fcntl.flock(holder, fcntl.LOCK_EX)
        assert s.engine().apply() == 1
    assert s.lines == ["Another basix command runs in this workspace. Wait for it."]
    assert (state / "last.log").read_text() == "first run\n"
    assert s.runner.calls == []


def test_the_lock_is_free_after_a_run(s: Setup) -> None:
    s.engine().apply()
    with (s.ws / ".git" / "basix" / "lock").open("w") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)


def test_not_a_workspace(s: Setup) -> None:
    plain = s.ws / "plain"
    plain.mkdir()
    engine = Engine(basix_layer(s.world), plain, runner=s.runner, clock=s.clock, say=s.lines.append)
    assert engine.apply() == 1
    assert s.lines[0].endswith("plain is not a basix workspace. Go to ~/basix first.")
    assert s.runner.calls == []


def test_the_default_runner_is_the_subprocess_runner(s: Setup) -> None:
    engine = Engine(basix_layer(s.world), s.ws)
    assert isinstance(engine.runner, SubprocessRunner)
    assert engine.env is os.environ
