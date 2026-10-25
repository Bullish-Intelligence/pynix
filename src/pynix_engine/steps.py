"""The steps of an apply. Each step is a function of the session (009-D26).

The behaviour comes from the proven scripts: the S12 `basix_apply.py` and the S16 `minix_apply.py`. The stage
refusals come from 007 V2-D7 and the S5 report (GAPS G11).
"""

import os
import re
import textwrap
from pathlib import Path

from .layer import EXIT_STOPPED, Plan
from .session import Fail, Session

NIX_STORE_HASH = re.compile(r"/nix/store/[0-9a-z]{32}-")
MODE_SYMLINK = "120000"
MODE_GITLINK = "160000"
RESTORE_BATCH = 200  # paths per `git update-index` call


# --- text -------------------------------------------------------------------------------------------
def plain(text: str) -> str:
    """Drop the hash of every store path (009-D15: no store path in the output)."""
    return NIX_STORE_HASH.sub("", text)


def trim_nix_error(text: str, limit: int = 30) -> str:
    """Keep the cause of a Nix error. Drop source snippets, trace notes, and 'dependency failed' follow-ups."""
    lines = [line for line in text.splitlines() if not line.startswith("warning:")]
    blocks: list[list[str]] = []
    for line in lines:
        if re.match(r"\s*error:", line):
            blocks.append([line])
        elif blocks:
            blocks[-1].append(line)
    if not blocks:
        return "\n".join(lines[-limit:])
    built = [b for b in blocks if any("Cannot build" in x for x in b) and not any("dependency failed" in x for x in b)]
    chosen = built[0] if built else blocks[-1]
    body = [x for x in chosen if not re.match(r"\s*(\d+)?\s*\|", x) and "stack trace truncated" not in x]
    if len(body) > 1 and body[0].strip() == "error:":
        body = body[1:]
    cleaned = re.sub(r"\n{2,}", "\n", textwrap.dedent("\n".join(body)).strip())
    out = cleaned.splitlines()
    if len(out) > limit:
        out = [*out[:6], "    ...", *out[-(limit - 7) :]]
    return "\n".join(out)


def store_paths(output: str) -> list[str]:
    """The lines of a `--print-out-paths` output that are paths."""
    return [line.strip() for line in output.splitlines() if line.startswith("/")]


# --- stage ------------------------------------------------------------------------------------------
def new_files(session: Session) -> list[str]:
    """The files that git does not track yet."""
    out = session.git("ls-files", "--others", "--exclude-standard", check=False).out
    return [name for name in out.splitlines() if name]


def staged_names(session: Session) -> list[str]:
    out = session.git("diff", "--cached", "--name-only", check=False).out
    return [name for name in out.splitlines() if name]


def index_records(session: Session) -> dict[str, tuple[str, str]]:
    """Every entry of the index at stage 0 as {path: (mode, object id)}. An unmerged entry is left out."""
    out = session.git("ls-files", "-s", "-z").out
    records: dict[str, tuple[str, str]] = {}
    for record in out.split("\0"):
        meta, _, path = record.partition("\t")
        fields = meta.split()
        if path and len(fields) == 3 and fields[2] == "0":
            records[path] = (fields[0], fields[1])
    return records


def leaves_workspace(session: Session, path: str) -> bool:
    """True when the symlink `path` points outside the workspace."""
    target = (session.ws / path).resolve()
    return not target.is_relative_to(session.ws.resolve())


def refuse_unsafe(session: Session, entries: dict[str, tuple[str, str]]) -> None:
    """Stop with one plain line for a secret, a nested repository, or a symlink that leaves the workspace."""
    pattern = re.compile(session.layer.secret_pattern, re.IGNORECASE)
    for path in entries:
        if pattern.search(path):
            raise Fail(session.word("refuse_secret", path=path), EXIT_STOPPED)
    for path, (mode, _) in entries.items():
        if mode == MODE_GITLINK:
            raise Fail(session.word("refuse_gitlink", path=path), EXIT_STOPPED)
    for path, (mode, _) in entries.items():
        if mode == MODE_SYMLINK and leaves_workspace(session, path):
            raise Fail(session.word("refuse_symlink", path=path), EXIT_STOPPED)


def restore_index(session: Session, before: dict[str, tuple[str, str]]) -> None:
    """Put the index back to `before`: drop what the stage added, and restore what it changed or removed."""
    now = index_records(session)
    gone = [path for path in now if path not in before]
    back = [f"{mode},{oid},{path}" for path, (mode, oid) in before.items() if now.get(path) != (mode, oid)]
    for start in range(0, len(gone), RESTORE_BATCH):
        session.git("update-index", "--force-remove", "--", *gone[start : start + RESTORE_BATCH])
    for start in range(0, len(back), RESTORE_BATCH):
        argv = [word for info in back[start : start + RESTORE_BATCH] for word in ("--cacheinfo", info)]
        session.git("update-index", "--add", *argv)


def stage(session: Session) -> str:
    """Stage every file (the flake sees tracked files only), refuse unsafe paths, and return the tree id.

    A refusal leaves the index as it was before the stage: a later `git commit` must not save a refused file.
    """
    before = index_records(session)
    session.git("add", "-A")
    entries = index_records(session)
    try:
        refuse_unsafe(session, entries)
    except Fail:
        restore_index(session, before)
        raise
    return session.git("write-tree").out.strip()


# --- compile ----------------------------------------------------------------------------------------
def build_compiler(session: Session) -> Path:
    """Build the compiler of the workspace lock. `--out-link` under `.git/NAME/` is its garbage-collector root.

    When the build fails and an earlier root still holds a compiler (offline, after a garbage collection),
    use that compiler and say so.
    """
    layer = session.layer
    root = session.state / "compiler"
    result = session.run(
        ["nix", "build", "--out-link", str(root), "--print-out-paths", "--no-warn-dirty", layer.compiler_attr]
    )
    paths = store_paths(result.out)
    if result.code == 0 and paths:
        return Path(paths[-1]) / "bin" / layer.compiler_bin
    old = root / "bin" / layer.compiler_bin
    if old.exists():
        session.say(session.word("compiler_old"))
        return old
    detail = plain(trim_nix_error(result.out))
    raise Fail(session.word("compiler_failed", detail=detail), EXIT_STOPPED)


def run_compiler(session: Session, tool: Path) -> None:
    """Run the compiler on the entry. Write the JSON file. Stop with the plain text of the compiler on an error."""
    layer = session.layer
    tmp = session.ws / (layer.json_file + ".new")
    result = session.run([str(tool), layer.entry, str(tmp)])
    if result.code != 0:
        tmp.unlink(missing_ok=True)
        raise Fail(result.out.strip() or session.word("compile_failed"), EXIT_STOPPED)
    os.replace(tmp, session.ws / layer.json_file)


def default_compile(session: Session) -> None:
    """Lock the flake, build the compiler of the lock, and run it. A layer may wrap this in its own compile."""
    session.run(["nix", "flake", "lock", "--no-warn-dirty"])  # a new lock must not look like an edit
    stage(session)  # a file that git does not track is invisible to the flake
    run_compiler(session, build_compiler(session))


# --- build ------------------------------------------------------------------------------------------
def build(session: Session) -> str:
    """One `nix build` of the layer's attribute. The out-link `.git/NAME/result` keeps the result until the switch."""
    layer = session.layer
    argv = ["nix", "build", "--out-link", str(session.state / "result"), "--print-out-paths", "--no-warn-dirty"]
    argv.append(layer.build_attr)
    if layer.build_command:
        argv = list(layer.build_command(argv))
    result = session.run(argv)
    log = session.display(session.log_path)
    if result.code != 0:
        detail = plain(trim_nix_error(result.out))
        raise Fail(session.word("build_failed", detail=detail, log=log), EXIT_STOPPED)
    paths = store_paths(result.out)
    if not paths:
        raise Fail(session.word("no_output", log=log), EXIT_STOPPED)
    return paths[-1]


# --- switch and health ------------------------------------------------------------------------------
def parse_bad_units(output: str, suffixes: tuple[str, ...]) -> list[str]:
    """Units that failed, or restart in a loop after a failure. The input is `systemctl list-units` output."""
    bad: list[str] = []
    for line in output.splitlines():
        fields = line.split()
        if len(fields) >= 4 and fields[0].endswith(suffixes):
            if fields[2] == "failed" or (fields[2] == "activating" and fields[3] == "auto-restart"):
                bad.append(fields[0])
    return bad


def watch(session: Session) -> list[str] | None:
    """Watch the units for the settle time. Return at the first failure. Success needs the whole settle time.

    Return the failed units. Return None when the query itself fails (010-D9): a health check that cannot run is a
    failed health check.
    """
    layer = session.layer
    end = session.clock.now() + layer.settle
    polls = 0
    while True:
        polls += 1
        result = session.run(layer.health_command, quiet=True)
        if result.code != 0:
            session.log(f"health: {polls} polls; the query failed (exit {result.code})")
            return None
        bad = parse_bad_units(result.out, layer.unit_suffixes)
        if bad or session.clock.now() >= end:
            session.log(f"health: {polls} polls; failed units: {', '.join(bad) or 'none'}")
            return bad
        session.clock.sleep(layer.poll)


def switch_and_check(session: Session, plan: Plan) -> str | None:
    """Run the plan: reset, activate, the health check, then finish. Return None, or the reason of a failure."""
    if plan.notice:
        session.say(plan.notice)
    for command in plan.reset:
        session.run(command)  # an old failed unit must not fail the new state; the result does not matter
    for command in plan.activate:
        result = session.run(command)
        if result.code != 0:
            return session.word("step_failed", code=result.code)
    session.say(session.word("watching", settle=session.layer.settle))
    bad = watch(session)
    if bad is None:
        return session.word("health_failed")
    if bad:
        return session.word("units_failed", units=", ".join(bad))
    for command in plan.finish:
        result = session.run(command)
        if result.code != 0:
            return session.word("step_failed", code=result.code)
    return None


def roll_back(session: Session, plan: Plan) -> str:
    """Return to the earlier state. Return the plain text about the result."""
    commands = plan.restore()
    if not commands:
        return session.word("no_earlier")
    for command in commands:
        result = session.run(command)
        if result.code != 0:
            return session.word("roll_failed", code=result.code)
    return session.word("rolled_back")


# --- commit and undo --------------------------------------------------------------------------------
def check_identity(session: Session) -> None:
    """Find out whether git knows the author. Stop early when it does not and the layer has no fallback."""
    known = (
        session.git("config", "user.name", check=False).code == 0
        and session.git("config", "user.email", check=False).code == 0
    )
    session.identity_known = known
    if not known and session.layer.fallback_identity is None:
        raise Fail(session.word("no_identity"))


def commit(session: Session, message: str, summary: str) -> None:
    fallback = session.layer.fallback_identity
    ident: list[str] = []
    if not session.identity_known and fallback:
        ident = ["-c", f"user.name={fallback[0]}", "-c", f"user.email={fallback[1]}"]
    session.git(*ident, "commit", "-q", "-m", message)
    session.say(session.word("saved", summary=summary))


def commit_message(names: list[str]) -> str:
    return "apply: " + ", ".join(names[:5]) + (f" and {len(names) - 5} more" if len(names) > 5 else "")


def restore_for_undo(session: Session) -> str | None:
    """Put the files of the last good save back. Return the commit message for a clean tree, else None.

    A dirty tree goes back to HEAD, and the dropped edit stays at `refs/NAME/dropped`.
    A clean tree goes back to the files of HEAD~1.
    """
    tree = stage(session)
    if session.git("rev-parse", "--verify", "-q", "HEAD", check=False).code != 0:
        raise Fail(session.word("undo_nothing"))
    message = None
    if tree != session.git("rev-parse", "HEAD^{tree}").out.strip():
        saved = session.git("stash", "create").out.strip()
        session.say(session.word("undo_dropped"))
        if saved:
            session.git("update-ref", f"refs/{session.layer.name}/dropped", saved)
        source = "HEAD"
    else:
        if session.git("rev-parse", "--verify", "-q", "HEAD~1", check=False).code != 0:
            raise Fail(session.word("undo_only_one"))
        source = "HEAD~1"
        message = "undo to " + session.git("rev-parse", "--short", source).out.strip()
        session.say(session.word("undo_restored"))
    session.git("restore", f"--source={source}", "--staged", "--worktree", ":/")
    return message
