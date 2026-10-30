"""The layer-neutral engine of `basix apply` and `minix apply`: stage, build, health check, commit, undo (009-D26).

A command builds a `Layer`, makes an `Engine`, and calls `apply` or `undo`. The engine imports no layer and no
`nixdantic` class. Every subprocess goes through a `Runner`, so tests use the fake runner in `pynix_engine.testing`.
"""

from .engine import Engine
from .gitdir import git_dirs
from .layer import (
    EXIT_CHANGED,
    EXIT_FAILED,
    EXIT_STOPPED,
    EXIT_UNHEALTHY,
    SECRET_PATTERN,
    SETTLE_SECONDS,
    Command,
    Layer,
    Plan,
    Words,
)
from .runner import Clock, Result, Runner, SubprocessRunner, SystemClock
from .session import Fail, Session
from .steps import (
    build,
    build_compiler,
    default_compile,
    parse_bad_units,
    run_compiler,
    stage,
    trim_nix_error,
)

__all__ = [
    "EXIT_CHANGED",
    "EXIT_FAILED",
    "EXIT_STOPPED",
    "EXIT_UNHEALTHY",
    "SECRET_PATTERN",
    "SETTLE_SECONDS",
    "Clock",
    "Command",
    "Engine",
    "Fail",
    "Layer",
    "Plan",
    "Result",
    "Runner",
    "Session",
    "SubprocessRunner",
    "SystemClock",
    "Words",
    "build",
    "build_compiler",
    "default_compile",
    "git_dirs",
    "parse_bad_units",
    "run_compiler",
    "stage",
    "trim_nix_error",
]
