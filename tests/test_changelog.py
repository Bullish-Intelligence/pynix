"""The changelog of a release: the manifest reader, the option diff, and the renderer."""

import json
from pathlib import Path

import pytest

from pynix import changelog
from pynix.manifest import PLACEHOLDER, aliases, option_types, type_text

TYPES = [
    {"name": "bool", "ctor": "bool", "description": "boolean", "nested": {}},
    {"name": "str", "ctor": "str", "description": "string", "nested": {}},
    {"name": "nullOr", "ctor": "nullOr", "description": "", "nested": {"elemType": 1}},
    {"name": "listOf", "ctor": "listOf", "description": "", "nested": {"elemType": 2}},
    {"name": "attrsOf", "ctor": "attrsWith", "description": "", "nested": {"elemType": 0}},
    {"name": "coercedTo", "ctor": "coercedTo", "description": "", "nested": {"a": 0, "b": 1}},
]


def manifest(options: dict[str, int]) -> dict:
    return {"types": TYPES, "optionPool": [{"path": name.split("."), "type": tid} for name, tid in options.items()]}


def inputs(version: str, rev: str, modified: int) -> dict:
    sources = {
        "nixpkgs": {"rev": rev * 40, "lastModified": modified},
        "home-manager": {"rev": "b" * 40, "lastModified": modified},
        "flake-parts": {"rev": "c" * 40, "lastModified": modified},
    }
    return {"version": version, "sources": sources}


def test_type_text_builds_container_names() -> None:
    assert type_text(TYPES, 0) == "boolean"
    assert type_text(TYPES, 2) == "null or string"
    assert type_text(TYPES, 3) == "list of null or string"
    assert type_text(TYPES, 4) == "attribute set of boolean"
    assert type_text(TYPES, 5) == "coercedTo of (boolean, string)"


def test_option_types_names_and_placeholders() -> None:
    m = manifest({"a.b": 0, f"a.{PLACEHOLDER}.c": 1})
    m["optionPool"].append({"path": ["a", "b"], "type": 1})
    assert option_types(m) == {"a.<name>.c": "string", "a.b": "boolean | string"}


def test_aliases_reads_literal_pairs(tmp_path: Path) -> None:
    (tmp_path / "m").mkdir()
    (tmp_path / "m" / "x.nix").write_text(
        '{ imports = [ (lib.mkRenamedOptionModule [ "services" "old" ] [ "services" "new" "port" ]) ]; }'
    )
    assert aliases(tmp_path, "m") == {("services.old", "services.new.port")}


def test_diff_options() -> None:
    old = {"a.x": "boolean", "a.old": "string", "b.y": "string"}
    cur = {"a.x": "null or boolean", "a.new": "string", "b.y": "string", "c.z": "string"}
    d = changelog.diff_options(old, cur, {("a.old", "a.new"), ("q.r", "q.s")})
    assert d["added"] == ["a.new", "c.z"]
    assert d["removed"] == ["a.old"]
    assert d["type_changed"] == [("a.x", "boolean", "null or boolean")]
    assert d["renamed"] == [("a.old", "a.new")]


def test_type_change_short_and_long() -> None:
    assert changelog.type_change("string", "null or string") == "string -> null or string"
    old = "one of " + ", ".join(f'"v{i}"' for i in range(20))
    new = old + " or extra"
    assert changelog.type_change(old, new) == "adds or extra"


def test_render_first_release() -> None:
    lines = changelog.render_first(
        inputs("0.1.0-rc.1", "a", 1_791_456_040), {"nixos": 10, "home-manager": 5, "flake-parts": 2}, 99
    )
    assert "Initial release" in lines[1]
    assert lines[2] == "Options: NixOS 10, Home Manager 5, flake-parts 2."
    assert lines[3] == "Package names: 99."


def test_render_fits_max_lines_and_shows_counts() -> None:
    cur_inputs = inputs("0.2.0", "a", 1_791_456_040 + 17 * 86400)
    prev_inputs = inputs("0.1.0", "d", 1_791_456_040)
    big = {
        "added": [f"services.s{i}.opt{j}" for i in range(60) for j in range(3)],
        "removed": [f"programs.p{i}.opt" for i in range(30)],
        "type_changed": [(f"t.o{i}", "string", "null or string") for i in range(50)],
        "renamed": [(f"r.old{i}", f"r.new{i}") for i in range(30)],
    }
    empty = {"added": [], "removed": [], "type_changed": [], "renamed": []}
    diffs = {"nixos": big, "home-manager": empty, "flake-parts": empty}
    names = {"added": [f"pkg{i}" for i in range(100)], "removed": ["gone"]}
    lines = changelog.render(
        cur_inputs,
        prev_inputs,
        ({"nixos": 1, "home-manager": 2, "flake-parts": 3}, {"nixos": 4, "home-manager": 2, "flake-parts": 3}),
        diffs,
        names,
        (10, 109),
    )
    assert len(lines) <= changelog.MAX_LINES
    text = "\n".join(lines)
    assert "Gap: 17 d 0 h." in text
    assert "Added 180, removed 30, type changed 50, renamed 30." in text
    assert "Package names added (100)" in text


def test_render_refuses_a_text_that_cannot_fit() -> None:
    diffs = {
        k: {"added": ["a.b"], "removed": [], "type_changed": [], "renamed": []}
        for k in ("nixos", "home-manager", "flake-parts")
    }
    with pytest.raises(ValueError):
        changelog.render(
            inputs("2", "a", 2),
            inputs("1", "d", 1),
            ({"nixos": 0, "home-manager": 0, "flake-parts": 0}, {"nixos": 0, "home-manager": 0, "flake-parts": 0}),
            diffs,
            {"added": [], "removed": []},
            (0, 0),
            max_lines=3,
        )


def write_side(root: Path, options: dict[str, int]) -> Path:
    root.mkdir(parents=True)
    for key in ("nixos", "home-manager", "flake-parts"):
        (root / f"{key}.json").write_text(json.dumps(manifest(options)))
    return root


def test_main_first_and_later_release(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    first = write_side(tmp_path / "m1", {"a.x": 0})
    second = write_side(tmp_path / "m2", {"a.x": 2, "a.y": 1})
    (tmp_path / "i1.json").write_text(json.dumps(inputs("0.1.0-rc.1", "a", 1_791_456_040)))
    (tmp_path / "i2.json").write_text(json.dumps(inputs("0.1.0-rc.2", "b", 1_791_456_040 + 3600)))
    (tmp_path / "n1.json").write_text(json.dumps({"hello": []}))
    (tmp_path / "n2.json").write_text(json.dumps({"hello": [], "git": []}))
    assert (
        changelog.main(
            ["--inputs", str(tmp_path / "i1.json"), "--manifests", str(first), "--names", str(tmp_path / "n1.json")]
        )
        == 0
    )
    assert "Initial release" in capsys.readouterr().out
    diff_json = tmp_path / "diff.json"
    args = [
        "--inputs",
        str(tmp_path / "i2.json"),
        "--manifests",
        str(second),
        "--names",
        str(tmp_path / "n2.json"),
        "--prev-inputs",
        str(tmp_path / "i1.json"),
        "--prev-manifests",
        str(first),
        "--prev-names",
        str(tmp_path / "n1.json"),
        "--diff-json",
        str(diff_json),
    ]
    assert changelog.main(args) == 0
    out = capsys.readouterr().out
    assert "NixOS options: 1 -> 2. Added 1, removed 0, type changed 1, renamed 0." in out
    assert "a.x: boolean -> null or string" in out
    assert "Package names added (1): git" in out
    assert json.loads(diff_json.read_text())["libraries"]["nixos"]["added"] == ["a.y"]
