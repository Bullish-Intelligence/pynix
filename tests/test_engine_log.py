"""The log file, the plain lines (009-D15), the Nix error trim, the runner seam, and the layer-neutral rule."""

import ast
import re
import sys
from pathlib import Path

import pytest
from test_engine_support import BAD_UNITS, COMPILER, HEALTH, TOP_NEW, Setup, basix_layer, make_setup, minix_layer

import pynix_engine
from pynix_engine import Fail, Result, Session, SubprocessRunner, Words, trim_nix_error
from pynix_engine.steps import plain


@pytest.fixture
def s(tmp_path: Path) -> Setup:
    return make_setup(tmp_path)


# --- the log file ------------------------------------------------------------------------------------
def test_the_full_log_is_in_the_state_folder(s: Setup) -> None:
    s.runner.on(("nix", "build"), Result(0, f"warning: Git tree is dirty\n{TOP_NEW}\n"))
    s.engine().apply()
    log = (s.ws / ".git" / "basix" / "last.log").read_text()
    assert "$ nix build --out-link" in log
    assert "    warning: Git tree is dirty" in log
    assert f"    {TOP_NEW}" in log
    assert "$ git commit -q -m apply: system.py" in log
    assert "(exit 0)" in log
    assert "saved: system.py" in log  # the plain lines are in the log too


def test_each_run_starts_a_new_log(s: Setup) -> None:
    s.engine().apply()
    s.engine().apply()
    assert s.log().count("$ nix build") == 1


def test_a_stopped_run_still_has_its_log(s: Setup) -> None:
    s.runner.on(("nix", "build"), Result(1, "error: nope\n"))
    s.engine().apply()
    assert "    error: nope" in s.log()


def test_the_state_folder_is_named_by_the_layer(s: Setup) -> None:
    s.engine(minix_layer(s.world)).apply()
    assert (s.ws / ".git" / "minix" / "last.log").exists()
    assert not (s.ws / ".git" / "basix").exists()


def test_verbose_prints_the_log_lines(s: Setup) -> None:
    s.engine(verbose=True).apply()
    assert any(line.startswith("$ nix build") for line in s.lines)
    assert f"    {TOP_NEW}" in s.lines


def test_quiet_runs_print_no_command(s: Setup) -> None:
    s.engine().apply()
    assert not any(line.startswith("    ") or line.startswith("$") for line in s.lines)


# --- the plain lines ---------------------------------------------------------------------------------
GIT_WORDS = re.compile(r"\bgit\b|stash|jj\b|refs/|HEAD|commit", re.IGNORECASE)


LOG_PATH = re.compile(r"\.git/\w+/last\.log")


def assert_plain(lines: list[str]) -> None:
    for line in lines:
        assert "/nix/store" not in line, line
        # The path of the log is the one thing that D15 names: `.git/NAME/last.log`.
        assert not GIT_WORDS.search(LOG_PATH.sub("", line)), line


def test_a_clean_apply_prints_plain_lines_only(s: Setup) -> None:
    s.engine().apply()
    assert s.lines == [
        "checked: system.py",
        "building the system",
        "built the system",
        "Basix needs your password to change the machine",
        "checking the units for 8 s",
        "applied: the system runs, and its units are healthy",
        "saved: system.py",
    ]
    assert_plain(s.lines)


def test_a_failed_apply_prints_plain_lines_only(s: Setup) -> None:
    s.runner.on(HEALTH, Result(0, BAD_UNITS))
    s.engine().apply()
    assert_plain(s.lines)


def test_undo_prints_plain_lines_only(s: Setup) -> None:
    s.git.tree = s.git.head_tree = "tree-head"
    s.git.restored_staged = ["system.py"]
    s.engine().undo()
    assert_plain(s.lines)
    s.git.tree, s.git.head_tree = "tree-edit", "tree-head"
    s.lines.clear()
    s.engine().undo()
    assert_plain(s.lines)


def test_a_build_error_loses_the_hash_of_every_store_path(s: Setup) -> None:
    error = "error: Cannot build '/nix/store/dddddddddddddddddddddddddddddddd-web.drv'.\n       Reason: failed.\n"
    s.runner.on(("nix", "build"), Result(1, error))
    s.engine().apply()
    assert_plain(s.lines)
    assert "web.drv" in s.lines[-1]
    assert "/nix/store" in s.log()  # the log keeps everything


def test_the_layer_can_give_its_own_words(s: Setup) -> None:
    words = Words(nothing="all is as it was", saved="done: {summary}")
    s.world.running = s.world.boot_default = TOP_NEW
    s.git.staged = []
    s.engine(basix_layer(s.world, words=words)).apply()
    assert s.lines[-1] == "all is as it was"


def test_plain_drops_only_the_hash() -> None:
    assert plain("see /nix/store/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-foo-1.0/bin/foo") == "see foo-1.0/bin/foo"


# --- the trim of a Nix error (from the S12 script) ----------------------------------------------------
NIX_ERROR = """warning: Git tree '/home/ada/basix' is dirty
error: builder for '/nix/store/aaaa-web.drv' failed with exit code 1;
       last 3 log lines:
       > what
       For full logs, run 'nix log /nix/store/aaaa-web.drv'.
error: Cannot build '/nix/store/aaaa-system.drv'.
       Reason: 1 dependency failed.
error: Cannot build '/nix/store/aaaa-web.drv'.
       Reason: builder failed with exit code 1.
       Output paths: /nix/store/bbbb-web
"""


def test_trim_keeps_the_cause_and_drops_the_follow_up() -> None:
    text = trim_nix_error(NIX_ERROR)
    assert "Cannot build '/nix/store/aaaa-web.drv'." in text
    assert "Reason: builder failed with exit code 1." in text
    assert "dependency failed" not in text
    assert "warning:" not in text


def test_trim_drops_source_snippets_and_the_bare_error_line() -> None:
    text = trim_nix_error(
        "error:\n       at /x/a.nix:3:5:\n          3|   foo = bar;\n           |   ^\n       undefined variable 'bar'\n"
    )
    assert "undefined variable 'bar'" in text
    assert "|" not in text


def test_trim_shortens_a_long_error() -> None:
    body = "error: big\n" + "".join(f"line {n}\n" for n in range(100))
    out = trim_nix_error(body).splitlines()
    assert len(out) <= 30
    assert "    ..." in out


def test_trim_without_an_error_block_keeps_the_last_lines() -> None:
    assert trim_nix_error("a\nb\nc\n", limit=2) == "b\nc"


# --- the runner seam ---------------------------------------------------------------------------------
def test_subprocess_runner_merges_stderr_and_streams_lines() -> None:
    code = "import sys; print('a', flush=True); sys.stderr.write('b\\n'); sys.stderr.flush(); sys.exit(3)"
    seen: list[str] = []
    result = SubprocessRunner().run([sys.executable, "-I", "-c", code], on_line=seen.append)
    assert result.code == 3
    assert result.out == "a\nb\n"
    assert seen == ["a", "b"]


def test_subprocess_runner_reports_a_missing_program() -> None:
    result = SubprocessRunner().run(["pynix-engine-no-such-program"])
    assert result.code == 127
    assert "command not found" in result.out


def test_every_subprocess_goes_through_the_runner() -> None:
    """The package calls no subprocess itself, apart from the one real runner."""
    package = Path(pynix_engine.__file__).parent
    users = [
        path.name
        for path in package.glob("*.py")
        if re.search(r"import subprocess|\bsubprocess\.|os\.system|os\.popen", path.read_text())
    ]
    assert users == ["runner.py"]


def test_the_session_tells_the_runner_the_workspace(s: Setup) -> None:
    s.engine().apply()
    assert all(cwd == s.ws for cwd in s.runner.cwds)


# --- the engine names no layer -----------------------------------------------------------------------
LAYER_WORDS = ("basix", "minix", "sudo", "systemctl", "switch-to-configuration", "nix-env", "home-manager")


def string_constants(path: Path) -> list[str]:
    """Every string constant of a module, apart from docstrings."""
    tree = ast.parse(path.read_text())
    docstrings = {
        id(node.body[0].value)
        for node in ast.walk(tree)
        if isinstance(node, ast.Module | ast.ClassDef | ast.FunctionDef)
        and node.body
        and isinstance(node.body[0], ast.Expr)
        and isinstance(node.body[0].value, ast.Constant)
    }
    return [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docstrings
    ]


def test_no_layer_word_in_the_code_of_the_engine() -> None:
    package = Path(pynix_engine.__file__).parent
    for path in package.glob("*.py"):
        if path.name == "testing.py":
            continue
        for text in string_constants(path):
            for word in LAYER_WORDS:
                assert word not in text.lower(), f"{path.name}: {text!r} names {word}"


def test_session_and_fail_are_public() -> None:
    assert issubclass(Fail, Exception)
    assert Session.__name__ == "Session"


def test_the_compiler_path_constant_is_a_store_path() -> None:
    assert COMPILER.startswith("/nix/store/")
