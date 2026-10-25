"""The health check: one settle time, an early stop at the first failed unit (009-D4), and a fake clock."""

from pathlib import Path

import pytest
from test_engine_support import (
    BAD_UNITS,
    GOOD_UNITS,
    HEALTH,
    HEALTH_USER,
    Setup,
    basix_layer,
    make_setup,
    minix_layer,
)

from pynix_engine import SETTLE_SECONDS, Result, parse_bad_units

SUFFIXES = (".service", ".mount", ".socket", ".timer", ".path")


@pytest.fixture
def s(tmp_path: Path) -> Setup:
    return make_setup(tmp_path)


def test_the_settle_constant_is_eight_seconds() -> None:
    assert SETTLE_SECONDS == 8.0


def test_success_needs_the_whole_settle_time(s: Setup) -> None:
    assert s.engine().apply() == 0
    assert s.runner.count(*HEALTH) == 17  # one poll at 0 s, then one every 0.5 s until 8 s
    assert s.clock.time == 8.0
    assert "checking the units for 8 s" in s.lines


def test_the_check_stops_at_the_first_failed_unit(s: Setup) -> None:
    ok, bad = Result(0, GOOD_UNITS), Result(0, BAD_UNITS)
    s.runner.on_turns(HEALTH, ok, ok, bad)
    assert s.engine().apply() == 3
    assert s.runner.count(*HEALTH) == 3
    assert s.clock.slept == [0.5, 0.5]
    assert s.clock.time < SETTLE_SECONDS  # it did not wait for the end of the settle time
    assert "problem: failed units: web.service" in s.lines


def test_a_failure_at_the_first_poll_does_not_sleep(s: Setup) -> None:
    s.runner.on(HEALTH, Result(0, BAD_UNITS))
    assert s.engine().apply() == 3
    assert s.clock.slept == []


def test_a_unit_that_fails_late_in_the_settle_time_still_counts(s: Setup) -> None:
    ok = Result(0, GOOD_UNITS)
    s.runner.on_turns(HEALTH, *([ok] * 15), Result(0, BAD_UNITS))
    assert s.engine().apply() == 3
    assert s.runner.count(*HEALTH) == 16


def test_the_layer_sets_the_settle_time(s: Setup) -> None:
    assert s.engine(basix_layer(s.world, settle=2.0, poll=1.0)).apply() == 0
    assert s.runner.count(*HEALTH) == 3
    assert s.clock.time == 2.0


def test_the_health_polls_stay_out_of_the_log(s: Setup) -> None:
    s.engine().apply()
    assert "list-units" not in s.log()
    assert "health: 17 polls; failed units: none" in s.log()


# --- a health query that fails (010-D9) --------------------------------------------------------------
def test_a_failed_query_is_a_failed_health_check(s: Setup) -> None:
    s.runner.on(HEALTH, Result(1, "Failed to connect to bus\n"))
    assert s.engine().apply() == 3
    assert s.runner.count(*HEALTH) == 1
    assert s.clock.slept == []
    assert "problem: the health check could not run" in s.lines
    assert s.lines[-1].startswith("failed: the earlier system is back. Nothing was saved.")
    assert s.git.commits == []
    assert "health: 1 polls; the query failed (exit 1)" in s.log()


def test_a_failed_query_with_keep_leaves_the_new_state(s: Setup) -> None:
    s.runner.on(HEALTH, Result(1, ""))
    assert s.engine(env={"BASIX_ON_FAIL": "keep"}).apply() == 3
    assert s.trace() == ["build", "reset", "test", "health"]
    assert s.lines[-1].startswith("failed: the new system is running, but it did not start cleanly.")
    assert s.git.commits == []


def test_a_query_that_fails_late_in_the_settle_time_still_counts(s: Setup) -> None:
    s.runner.on_turns(HEALTH, *([Result(0, GOOD_UNITS)] * 5), Result(2, "boom\n"))
    assert s.engine().apply() == 3
    assert s.runner.count(*HEALTH) == 6
    assert "problem: the health check could not run" in s.lines
    assert s.git.commits == []


def test_a_failed_query_rolls_back_a_minix_home(s: Setup) -> None:
    s.runner.on(HEALTH_USER, Result(1, ""))
    assert s.engine(minix_layer(s.world)).apply() == 3
    assert "problem: the health check could not run" in s.lines
    assert s.lines[-1].startswith("failed: the earlier home is back.")
    assert s.git.commits == []


def test_a_query_that_answers_with_output_but_a_bad_code_still_fails(s: Setup) -> None:
    s.runner.on(HEALTH, Result(1, GOOD_UNITS))
    assert s.engine().apply() == 3
    assert s.git.commits == []


# --- reading the unit list ---------------------------------------------------------------------------
def test_parse_finds_failed_units() -> None:
    out = "a.service loaded active running A\nb.service loaded failed failed B\nc.mount loaded failed failed C\n"
    assert parse_bad_units(out, SUFFIXES) == ["b.service", "c.mount"]


def test_parse_finds_a_restart_loop() -> None:
    out = "loop.service loaded activating auto-restart Loop\nstart.service loaded activating start Start\n"
    assert parse_bad_units(out, SUFFIXES) == ["loop.service"]


def test_parse_reads_only_the_unit_kinds_of_the_layer() -> None:
    out = "x.slice loaded failed failed X\ny.service loaded failed failed Y\n"
    assert parse_bad_units(out, (".service",)) == ["y.service"]
    assert parse_bad_units(out, (".slice",)) == ["x.slice"]


def test_parse_skips_short_lines() -> None:
    assert parse_bad_units("\nfoo.service\n", SUFFIXES) == []
