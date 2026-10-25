"""What a command passes to the engine: the `Layer` description, the plain words, and the plan of a switch (009-D26).

The engine names no layer. `basix` and `minix` each build one `Layer` value. The layer decides `sudo`, the switch
commands, and the health query. The engine only runs the command words that the layer gives it.
"""

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .session import Session

# 009-D4: one settle time for both commands. The check ends early at the first failed unit.
SETTLE_SECONDS = 8.0

# 007 V2-D7, V2-D30, and the S5 guard: a staged path with one of these names is refused.
# A public key (`id_ed25519.pub`) is not a secret: the `id_` rule skips a name that ends in `.pub` (010-D11).
SECRET_PATTERN = r"(\.key|\.pem)$|(^|/)id_(?![^/]*\.pub$)|(^|/)\.env|secret|password|token"

# A command: the words of one program call. The runner runs it with no shell.
Command = Sequence[str]

# Exit codes (the S16 table). 0 is done or nothing to change.
EXIT_FAILED = 1
EXIT_STOPPED = 2  # stopped before any switch: a compile error or a build error
EXIT_UNHEALTHY = 3  # the new state did not start cleanly
EXIT_CHANGED = 4  # a file changed during the run


def _no_steps() -> Sequence[Command]:
    return ()


@dataclass(frozen=True)
class Plan:
    """How the layer changes the running state to the built result, and how it goes back (L123).

    `reset`, `activate`, and `finish` run in this order. The health check runs between `activate` and `finish`.
    For Basix: `reset` is reset-failed, `activate` is `test`, `finish` sets the profile and runs `boot`.
    A command that exits with a code other than 0 fails the apply. `restore` is called only after a failure.
    """

    unchanged: bool  # the running state already is the built result
    reset: Sequence[Command] = ()
    activate: Sequence[Command] = ()
    finish: Sequence[Command] = ()
    restore: Callable[[], Sequence[Command]] = _no_steps  # empty: there is no earlier state to return to
    notice: str | None = None  # a line to print before the first command (for example why sudo asks)


@dataclass(frozen=True)
class Words:
    """The plain lines (009-D15). A template may use {name}, {entry}, {noun}, {folder}, {stopped}, and its own keys."""

    stopped: str = "apply stopped"
    refuse_secret: str = "{stopped}: {path} looks like a secret; move it out of {folder}"
    refuse_gitlink: str = (
        "{stopped}: {path} holds its own repository, so its files stay hidden; move it out of {folder}"
    )
    refuse_symlink: str = "{stopped}: {path} is a link that leaves {folder}; put the file inside {folder}"
    no_identity: str = (
        'git does not know your name. Run: git config --global user.name "Your Name"; '
        "git config --global user.email you@example.org"
    )
    not_a_workspace: str = "{path} is not a {name} workspace. Go to {folder} first."
    busy: str = "Another {name} command runs in this workspace. Wait for it."
    bad_on_fail: str = "{env} must be rollback or keep, found {value}."
    new_files: str = "new files that {name} will save: {names}"
    checked: str = "checked: {entry}"
    compiler_old: str = "the compiler could not be built, so {name} uses the compiler of the last good build"
    compiler_failed: str = "The compiler could not be built. Nothing was built, switched, or saved.\n{detail}"
    compile_failed: str = "{entry} has an error."
    building: str = "building the {noun}"
    built: str = "built the {noun}"
    build_failed: str = (
        "The build failed. Nothing was switched or saved. The {noun} did not change.\n{detail}\n(full log: {log})"
    )
    no_output: str = "The build gave no result. Nothing was switched or saved. (full log: {log})"
    changed_build: str = (
        "A file changed while {name} built the {noun}. Nothing was switched or saved. Run {name} apply again."
    )
    changed_switch: str = (
        "A file changed while {name} switched the {noun}. The running {noun} matches the files from before "
        "that change. Nothing was saved. Run {name} apply again."
    )
    nothing: str = "nothing to change"
    files_only: str = "the {noun} is the same; only files changed"
    watching: str = "checking the units for {settle:g} s"
    applied: str = "applied: the {noun} runs, and its units are healthy"
    problem: str = "problem: {reason}"
    step_failed: str = "the {noun} did not switch (exit {code})"
    units_failed: str = "failed units: {units}"
    health_failed: str = "the health check could not run"
    rolled_back: str = "the earlier {noun} is back"
    roll_failed: str = "tried to roll back, but that also failed (exit {code})"
    no_earlier: str = "found no earlier {noun} to return to, so the new {noun} stays"
    failed_rollback: str = (
        "failed: {what}. Nothing was saved.\nYour edited files are still in the folder. "
        "Fix them and run {name} apply, or run {name} undo to drop the edit."
    )
    failed_keep: str = (
        "failed: the new {noun} is running, but it did not start cleanly. Nothing was saved.\n"
        "The files, the last save, and the running {noun} differ. "
        "Fix the files and run {name} apply, or run {name} undo to return to the last save."
    )
    saved: str = "saved: {summary}"
    undo_dropped: str = "undo: dropped the edit that {name} did not apply (a copy stays in the workspace history)"
    undo_restored: str = "undo: restoring the files of the save before the last one"
    undo_nothing: str = "There is nothing to go back to. Run {name} apply first."
    undo_only_one: str = "There is only one save. There is nothing to undo."
    undone: str = "the files of the earlier save are back"


@dataclass(frozen=True)
class Layer:
    """One layer, as a command passes it to the engine."""

    name: str  # "basix" or "minix": the state folder `.git/NAME/`, the lock, and the dropped-edit ref
    entry: str  # "system.py" or "home.py"
    json_file: str  # "system.json" or "home.json"
    folder: str  # the workspace folder in plain words, for example "~/basix"
    noun: str  # the plain word for the thing that changes: "system" or "home"
    compiler_bin: str  # the program name under `bin/` of the compiler package
    build_attr: str  # the flake attribute that one `nix build` builds (never an eval first, L21)
    health_command: Command  # prints one unit per line: `UNIT LOAD ACTIVE SUB` (`systemctl list-units`)
    unit_suffixes: tuple[str, ...]  # the unit kinds that the check reads
    plan: Callable[["Session", str], Plan]  # (session, built result) -> how to switch to it
    on_fail_env: str  # "BASIX_ON_FAIL" or "MINIX_ON_FAIL": rollback (default) or keep
    compile: Callable[["Session"], None] | None = None  # None: `steps.default_compile`
    compiler_attr: str = ".#compiler"
    build_command: Callable[[Sequence[str]], Sequence[str]] | None = None  # adapt the build command (L134: root)
    preflight: Callable[["Session"], None] | None = None  # a check before any change, for example sudo (raise Fail)
    fallback_identity: tuple[str, str] | None = None  # (name, email) for a commit when git knows none
    settle: float = SETTLE_SECONDS
    poll: float = 0.5
    secret_pattern: str = SECRET_PATTERN
    words: Words = field(default_factory=Words)

    def text(self, key: str, **values: object) -> str:
        """Format the word template `key`."""
        template: str = getattr(self.words, key)
        base: Mapping[str, object] = {
            "name": self.name,
            "entry": self.entry,
            "noun": self.noun,
            "folder": self.folder,
            "stopped": self.words.stopped,
        }
        return template.format(**{**base, **values})
