"""The stage step and its refusals (007 V2-D7, V2-D30, S5; GAPS G11): a secret, a nested repository, a bad symlink."""

from pathlib import Path

import pytest
from test_engine_support import Setup, basix_layer, make_setup

from pynix_engine import Result


@pytest.fixture
def s(tmp_path: Path) -> Setup:
    return make_setup(tmp_path)


def refused(s: Setup) -> None:
    """The run stopped at the stage: exit 2, no Nix call, no switch, no commit."""
    assert s.runner.count("nix") == 0
    assert s.git.commits == []
    assert s.trace() == []


def test_secret_is_refused_with_one_plain_line(s: Setup) -> None:
    s.git.entries = [("100644", "system.py"), ("100644", "key.pem")]
    assert s.engine().apply() == 2
    assert s.lines[-1] == "apply stopped: key.pem looks like a secret; move it out of ~/basix"
    refused(s)


def test_a_refusal_prints_no_new_files_line(s: Setup) -> None:
    """009-D15: a refusal is one plain line. The new-files line waits until the stage checks pass."""
    s.git.new_files = ["key.pem", "notes.txt"]
    s.git.entries = [("100644", "system.py"), ("100644", "key.pem"), ("100644", "notes.txt")]
    assert s.engine().apply() == 2
    assert s.lines == ["apply stopped: key.pem looks like a secret; move it out of ~/basix"]


def test_new_files_line_comes_after_the_stage_passes(s: Setup) -> None:
    s.git.new_files = ["notes.txt"]
    assert s.engine().apply() == 0
    assert s.lines[0] == "new files that basix will save: notes.txt"


@pytest.mark.parametrize(
    "path",
    [
        ".env",
        ".env.local",
        "id_ed25519",
        "keys/id_rsa",
        "keys/id_rsa.pub.key",
        "my.key",
        "cert.pem",
        "notes/Secret.txt",
        "password.txt",
        "api-token.json",
    ],
)
def test_names_that_look_like_a_secret(s: Setup, path: str) -> None:
    s.git.entries = [("100644", path)]
    assert s.engine().apply() == 2
    assert s.lines[-1].startswith(f"apply stopped: {path} looks like a secret")


@pytest.mark.parametrize(
    "path",
    [
        "system.py",
        "system.json",
        "flake.nix",
        "flake.lock",
        "facter.json",
        ".gitignore",
        "keyboard.py",
        "dotfiles/zshrc",
        "id_ed25519.pub",  # a public key is not a secret (010-D11)
        "keys/id_rsa.pub",
    ],
)
def test_ordinary_names_pass(s: Setup, path: str) -> None:
    s.git.entries = [("100644", path)]
    assert s.engine().apply() == 0


def test_a_tracked_secret_is_refused_too(s: Setup) -> None:
    """V2-D30: `.gitignore` does not untrack a file, so the guard reads the whole index, not only new files."""
    s.git.entries = [("100644", "system.py"), ("100644", "old.key")]
    s.git.staged = []
    assert s.engine().apply() == 2


def test_gitlink_is_refused(s: Setup) -> None:
    s.git.entries = [("100644", "system.py"), ("160000", "modules/sub")]
    assert s.engine().apply() == 2
    assert s.lines[-1] == (
        "apply stopped: modules/sub holds its own repository, so its files stay hidden; move it out of ~/basix"
    )
    refused(s)


def test_symlink_to_an_absolute_path_outside_is_refused(s: Setup) -> None:
    (s.ws / "result").symlink_to("/nix/store/eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee-out")
    s.git.entries = [("100644", "system.py"), ("120000", "result")]
    assert s.engine().apply() == 2
    assert s.lines[-1] == "apply stopped: result is a link that leaves ~/basix; put the file inside ~/basix"
    refused(s)


def test_symlink_with_a_relative_path_outside_is_refused(s: Setup) -> None:
    (s.ws / "up").symlink_to("../outside.txt")
    s.git.entries = [("120000", "up")]
    assert s.engine().apply() == 2
    assert s.lines[-1].startswith("apply stopped: up is a link that leaves")


def test_symlink_inside_the_workspace_passes(s: Setup) -> None:
    (s.ws / "system.py").write_text("")
    (s.ws / "link-in").symlink_to("system.py")
    (s.ws / "deep").mkdir()
    (s.ws / "deep" / "back").symlink_to("../system.py")
    s.git.entries = [("100644", "system.py"), ("120000", "link-in"), ("120000", "deep/back")]
    assert s.engine().apply() == 0


def test_the_stage_runs_every_time_the_tree_is_read(s: Setup) -> None:
    """A secret that appears during the build is caught at the next stage, before the switch."""
    s.runner.on(("nix", "build"), lambda argv: _plant_secret(s))
    assert s.engine().apply() == 2
    assert s.trace() == ["build"]
    assert s.lines[-1].startswith("apply stopped: late.key looks like a secret")


def _plant_secret(s: Setup) -> Result:
    s.git.entries = [("100644", "late.key")]
    return Result(0, "/nix/store/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-new\n")


def test_the_layer_can_change_the_secret_pattern(s: Setup) -> None:
    s.git.entries = [("100644", "token-list.txt")]
    assert s.engine(basix_layer(s.world, secret_pattern=r"\.pem$")).apply() == 0
