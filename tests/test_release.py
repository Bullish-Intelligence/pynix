"""The release script refuses a wrong call before it changes anything."""

import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "release.sh"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["bash", str(SCRIPT), *args], capture_output=True, text=True, check=False)


@pytest.mark.parametrize(
    "tag",
    [
        "v0.1.0",
        "pynix-v0.1",
        "pynix-v0.1.0-beta.1",
        "pynix-v0.1.0-manifests",
        "manifests/pynix-v0.1.0",
        "pynix-v1.0.0-rc.",
    ],
)
def test_wrong_tag_name_exits_2(tag: str) -> None:
    done = run(tag)
    assert done.returncode == 2
    assert "pynix-vX.Y.Z" in done.stderr


def test_no_tag_exits_2() -> None:
    assert run().returncode == 2
    assert run("--skip-status").returncode == 2


def test_unknown_option_exits_2() -> None:
    done = run("--force", "pynix-v0.1.0")
    assert done.returncode == 2
    assert "unknown option" in done.stderr
