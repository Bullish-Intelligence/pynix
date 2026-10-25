"""The layer-compare script: equal locks, differences, a missing node, a folder, and an unreadable file."""

import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "compare_layers.py"
_spec = importlib.util.spec_from_file_location("compare_layers", SCRIPT)
assert _spec is not None and _spec.loader is not None
compare_layers = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(compare_layers)

NIXPKGS_REV = "e7439b6b14ad3cc35d05608ebca9bce01a25f5f8"
OTHER_REV = "1234567890abcdef1234567890abcdef12345678"
PYNIX_REV = "cb0489516a87fe5c219ab97f3fba07cd4343002d"
OCTOBER_8 = 1791456040  # 2026-10-08


def lock(
    nixpkgs: tuple[str, int] | None = (NIXPKGS_REV, OCTOBER_8),
    pynix: tuple[str, str] | None = ("pynix-v0.1.0-rc.3", PYNIX_REV),
    home_manager: bool = False,
) -> dict:
    nodes: dict = {}
    inputs: dict = {}
    if nixpkgs:
        rev, modified = nixpkgs
        nodes["nixpkgs"] = {
            "locked": {"lastModified": modified, "rev": rev, "type": "github"},
            "original": {"owner": "NixOS", "repo": "nixpkgs", "rev": rev, "type": "github"},
        }
        inputs["nixpkgs"] = "nixpkgs"
    if pynix:
        tag, rev = pynix
        ref = f"refs/tags/{tag}"
        nodes["pynix"] = {
            "flake": False,
            "locked": {"lastModified": 1792594113, "ref": ref, "rev": rev, "type": "git"},
            "original": {"ref": ref, "type": "git", "url": "https://example.invalid/pynix"},
        }
        inputs["pynix"] = "pynix"
    if home_manager:
        nodes["home-manager"] = {
            "locked": {"lastModified": 1791306979, "rev": "fae6e9e42c3b762ab47635cddcfaf6f52374a61b", "type": "github"},
            "original": {"type": "github"},
        }
        inputs["home-manager"] = "home-manager"
    nodes["root"] = {"inputs": inputs}
    return {"nodes": nodes, "root": "root", "version": 7}


def write(path: Path, data: dict) -> Path:
    path.write_text(json.dumps(data))
    return path


def run(capsys: pytest.CaptureFixture[str], *args: str) -> tuple[int, str, str]:
    code = compare_layers.main(list(args))
    out = capsys.readouterr()
    return code, out.out, out.err


def test_equal_locks(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    two = write(tmp_path / "two.lock", lock(home_manager=True))
    code, out, _ = run(capsys, str(one), str(two), "--names", "basix,minix")
    assert code == 0
    assert "nixpkgs: basix e7439b6 (2026-10-08), minix e7439b6 (2026-10-08): equal" in out
    assert "pynix: basix pynix-v0.1.0-rc.3 cb04895, minix pynix-v0.1.0-rc.3 cb04895: equal" in out
    assert "home-manager: minix fae6e9e (2026-10-06); basix has none: no compare" in out
    assert "warning:" not in out


def test_default_names(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    code, out, _ = run(capsys, str(one), str(one))
    assert code == 0
    assert "nixpkgs: first e7439b6 (2026-10-08), second e7439b6 (2026-10-08): equal" in out
    assert "home-manager: no pin in either lock: no compare" in out


def test_nixpkgs_difference(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    two = write(tmp_path / "two.lock", lock(nixpkgs=(OTHER_REV, OCTOBER_8 - 86400 * 3)))
    code, out, _ = run(capsys, str(one), str(two), "--names", "basix,minix")
    assert code == 0
    assert "nixpkgs: basix e7439b6 (2026-10-08), minix 1234567 (2026-10-05): differ" in out
    assert "warning: nixpkgs differs" in out
    assert "minix has the older nixpkgs. Update the nixpkgs pin of minix." in out
    assert "pynix:" in out and "equal" in out


def test_pynix_tag_difference_names_the_newer_tag(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock(pynix=("pynix-v0.1.0-rc.3", PYNIX_REV)))
    two = write(tmp_path / "two.lock", lock(pynix=("pynix-v0.1.0-rc.10", OTHER_REV)))
    code, out, _ = run(capsys, str(one), str(two), "--names", "basix,minix")
    assert code == 0
    assert "warning: pynix tags differ: basix pynix-v0.1.0-rc.3, minix pynix-v0.1.0-rc.10." in out
    # rc.10 is newer than rc.3: the order is numeric.
    assert "minix has the newer tag. Release basix again with pynix-v0.1.0-rc.10." in out


def test_release_is_newer_than_its_candidate(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock(pynix=("pynix-v0.1.0", OTHER_REV)))
    two = write(tmp_path / "two.lock", lock(pynix=("pynix-v0.1.0-rc.3", PYNIX_REV)))
    _, out, _ = run(capsys, str(one), str(two), "--names", "basix,minix")
    assert "basix has the newer tag. Release minix again with pynix-v0.1.0." in out


def test_same_tag_with_another_rev(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    two = write(tmp_path / "two.lock", lock(pynix=("pynix-v0.1.0-rc.3", OTHER_REV)))
    code, out, _ = run(capsys, str(one), str(two))
    assert code == 0
    assert "both layers pin the tag pynix-v0.1.0-rc.3 with different revisions" in out


def test_missing_node(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    two = write(tmp_path / "two.lock", lock(nixpkgs=None, pynix=None))
    code, out, _ = run(capsys, str(one), str(two), "--names", "basix,minix")
    assert code == 0
    assert "nixpkgs: basix e7439b6 (2026-10-08), minix has no pin: missing" in out
    assert "warning: nixpkgs: the lock of minix has no nixpkgs pin" in out
    assert "warning: pynix: the lock of minix has no pynix pin" in out


def test_follows_list_leads_to_the_node(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    data = lock()
    data["nodes"]["root"]["inputs"]["nixpkgs"] = ["other", "nixpkgs"]
    data["nodes"]["root"]["inputs"]["other"] = "other"
    data["nodes"]["other"] = {"inputs": {"nixpkgs": "nixpkgs"}}
    one = write(tmp_path / "one.lock", data)
    code, out, _ = run(capsys, str(one), str(one))
    assert code == 0
    assert "nixpkgs: first e7439b6 (2026-10-08), second e7439b6 (2026-10-08): equal" in out


def test_folder_argument(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    folder = tmp_path / "layer"
    folder.mkdir()
    write(folder / "flake.lock", lock())
    other = write(tmp_path / "other.lock", lock())
    code, out, _ = run(capsys, str(folder), str(other))
    assert code == 0
    assert "equal" in out


def test_unreadable_file_exits_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    good = write(tmp_path / "good.lock", lock())
    for bad in (tmp_path / "missing.lock", tmp_path / "empty-folder"):
        bad.mkdir() if bad.name == "empty-folder" else None
        code, out, err = run(capsys, str(good), str(bad))
        assert code == 2
        assert out == ""
        assert err.startswith("compare_layers: cannot read the lock")
    broken = tmp_path / "broken.lock"
    broken.write_text("not json")
    code, _, err = run(capsys, str(broken), str(good))
    assert code == 2
    assert err.count("\n") == 1
    other = write(tmp_path / "other.json", {"hello": 1})
    code, _, err = run(capsys, str(other), str(good))
    assert code == 2
    assert "is not a flake.lock file" in err


def test_wrong_names_exit_2(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    for names in ("only", "a,a", "a,", "a,b,c"):
        code, _, err = run(capsys, str(one), str(one), "--names", names)
        assert code == 2
        assert "--names needs two different names" in err


def test_wrong_use_exits_2(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as stop:
        compare_layers.main(["only-one-argument"])
    assert stop.value.code == 2
    capsys.readouterr()


def test_json_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    one = write(tmp_path / "one.lock", lock())
    two = write(tmp_path / "two.lock", lock(pynix=("pynix-v0.1.0-rc.4", OTHER_REV)))
    code, out, _ = run(capsys, str(one), str(two), "--names", "basix,minix", "--json")
    assert code == 0
    result = json.loads(out)
    assert result["names"] == ["basix", "minix"]
    assert result["pins"]["pynix"]["minix"]["tag"] == "pynix-v0.1.0-rc.4"
    assert result["pins"]["nixpkgs"]["basix"]["date"] == "2026-10-08"
    assert result["pins"]["home-manager"]["basix"] is None
    assert len(result["warnings"]) == 1
