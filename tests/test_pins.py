"""The pin compare (021-D3): URL identity, the manifest, `from_workspace`, the compare, and the text."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from pynix_native import pins
from pynix_native.pins import Manifest, Mismatch, Pin, compare, format_mismatch, normalize_url, parse

R1, R2 = "a" * 40, "b" * 40
AT = "@"  # a url with a user name and a password; the public check refuses a literal e-mail shape
ROOT = Path(__file__).resolve().parent.parent


def got(manifest: Manifest | None) -> Manifest:
    assert manifest is not None
    return manifest


def pin(name, url, rev=R1, nar="sha256-AAAA", flake=True):
    return Pin(name, url, rev, nar, flake, "src")


def man(*ps):
    return Manifest(tuple(ps))


def row(name, url, rev=R1, nar="sha256-AAAA", flake=True):
    return {"name": name, "url": url, "flake": flake, "python": "src", "rev": rev, "narHash": nar}


# --- the identity of an input ---------------------------------------------------------------------------------------
def test_normalize_forms_of_one_repository():
    forms = [
        "git+https://github.com/Owner/Repo.git?ref=main&rev=" + R1,
        "github:owner/repo",
        "github:owner/repo/" + R2,
        "git@github.com:owner/repo.git",
        "git+ssh://git@github.com/owner/repo",
        f"https://user:token{AT}github.com/owner/repo/",
        "git+https://GitHub.com/owner/repo",
    ]
    assert {normalize_url(f) for f in forms} == {"github.com/owner/repo"}


def test_normalize_keeps_what_differs():
    assert normalize_url("git+file:///srv/a/p/pytuin?ref=main") == "file:///srv/a/p/pytuin"
    assert normalize_url("path:/srv/a/x/") == "path:/srv/a/x"
    assert normalize_url("git+https://git.example.org/a/b?dir=sub") == "git.example.org/a/b#sub"
    assert normalize_url("git+https://git.example.org/A/b") != normalize_url("git+https://git.example.org/a/b")
    assert normalize_url("github:o/r") != normalize_url("github:o/r2")
    assert normalize_url("github:o/r?dir=a") != normalize_url("github:o/r?dir=b")


def test_normalize_other_hosts():
    assert (
        normalize_url("gitlab:Group/Proj")
        == normalize_url("git+https://gitlab.com/group/proj.git")
        == "gitlab.com/group/proj"
    )
    assert normalize_url("sourcehut:~o/r") == "git.sr.ht/~o/r"
    assert normalize_url("git+https://Git.Example.org:8443/a/b.git") == "git.example.org:8443/a/b"


# --- the compare ----------------------------------------------------------------------------------------------------
def test_one_layer_only_gives_nothing():
    assert compare(man(pin("a", "github:o/a")), man(pin("b", "github:o/b"))) == []
    assert compare(man(pin("a", "github:o/a")), None) == []
    assert compare(None, man()) == []


def test_same_revision_gives_nothing():
    a = man(pin("tool", "github:o/t"))
    b = man(pin("tool", "git+https://github.com/o/t.git?ref=main"))
    assert compare(a, b) == []


def test_different_revision_gives_a_mismatch():
    a = man(pin("tool", "github:o/t", rev=R1))
    b = man(pin("tool", "github:o/t", rev=R2))
    assert compare(a, b) == [Mismatch("tool", "tool", "github:o/t", R1, R2)]
    assert compare(b, a) == [Mismatch("tool", "tool", "github:o/t", R2, R1)]


def test_same_url_other_name_is_the_same_input():
    a = man(pin("tool", "github:o/t", rev=R1))
    b = man(pin("tools", "github:o/t", rev=R2))
    [m] = compare(a, b)
    assert (m.local_name, m.other_name) == ("tool", "tools")
    line = format_mismatch(m, here="home", there="system")
    assert "`tool` (`tools` in system)" in line


def test_same_name_other_url_is_another_input():
    a = man(pin("tool", "github:o/t", rev=R1))
    b = man(pin("tool", "github:fork/t", rev=R2))
    assert compare(a, b) == []


def test_flake_false_input_compares_like_any_other():
    a = man(pin("src", "git+file:///p/agentman", rev=R1, flake=False))
    b = man(pin("src", "git+file:///p/agentman", rev=R2, flake=False))
    assert len(compare(a, b)) == 1


def test_path_input_without_revision_compares_the_nar_hash():
    a = man(pin("loc", "path:/x/y", rev=None, nar="sha256-ONE"))
    same = man(pin("loc", "path:/x/y/", rev=None, nar="sha256-ONE"))
    other = man(pin("loc", "path:/x/y", rev=None, nar="sha256-TWO"))
    assert compare(a, same) == []
    assert [(m.local_rev, m.other_rev) for m in compare(a, other)] == [("sha256-ONE", "sha256-TWO")]


def test_same_repository_twice_in_the_other_layer_with_one_match_is_quiet():
    a = man(pin("t", "github:o/t", rev=R1))
    b = man(pin("t1", "github:o/t", rev=R1), pin("t2", "github:o/t", rev=R2))
    assert compare(a, b) == []


def test_a_pin_with_no_version_gives_nothing():
    a = man(pin("t", "github:o/t", rev=None, nar=None))
    assert compare(a, man(pin("t", "github:o/t"))) == []
    assert compare(man(pin("t", "github:o/t")), a) == []


# --- the manifest ---------------------------------------------------------------------------------------------------
def test_parse_refuses_what_is_not_this_version():
    good = {"version": 1, "pins": [row("t", "github:o/t")]}
    assert got(parse(json.dumps(good))).pins[0].rev == R1
    for bad in ({**good, "version": 2}, {"pins": good["pins"]}, {"version": 1}, {"version": 1, "pins": {}}, []):
        assert parse(json.dumps(bad)) is None
    assert parse("{") is None
    assert parse("") is None
    assert parse("[" * 100000) is None


def test_parse_drops_a_damaged_row_and_ignores_unknown_fields():
    rows = [row("ok", "github:o/ok"), {"name": "x"}, "text", {"name": 1, "url": "u"}]
    m = got(parse(json.dumps({"version": 1, "pins": rows, "extra": 1})))
    assert [p.name for p in m.pins] == ["ok"]


def test_load_is_tolerant(tmp_path: Path):
    good = tmp_path / "m.json"
    good.write_text(json.dumps({"version": 1, "pins": [row("t", "github:o/t")]}))
    assert got(pins.load(good)).pins[0].name == "t"
    assert pins.load(tmp_path / "missing.json") is None
    assert pins.load(tmp_path) is None  # a folder
    empty = tmp_path / "empty.json"
    empty.write_text("")
    assert pins.load(empty) is None
    binary = tmp_path / "bin.json"
    binary.write_bytes(b"\xff\xfe\x00")
    assert pins.load(binary) is None


# --- the own workspace ----------------------------------------------------------------------------------------------
def lock(**nodes):
    inputs = {n: n for n in nodes}
    return {"version": 7, "root": "root", "nodes": {"root": {"inputs": inputs}, **nodes}}


def test_from_data_reads_the_compiled_json_and_the_lock():
    compiled = {
        "inputs": [
            {"name": "zed", "url": "github:o/zed", "python": "."},
            {"name": "tool", "url": f"https://u:tok{AT}host.org/o/tool", "python": "src", "flake": False},
            {"name": "mods", "url": "github:o/mods", "modules": ["m"]},  # no python: out of scope
        ]
    }
    lk = lock(
        zed={"locked": {"rev": R1, "narHash": "sha256-Z"}},
        tool={"locked": {"rev": R2, "narHash": "sha256-T"}},
        mods={"locked": {"rev": R1, "narHash": "sha256-M"}},
    )
    m = pins.from_data(compiled, lk)
    assert [(p.name, p.url, p.rev, p.nar_hash, p.flake, p.python) for p in m.pins] == [
        ("tool", "https://host.org/o/tool", R2, "sha256-T", False, "src"),
        ("zed", "github:o/zed", R1, "sha256-Z", True, "."),
    ]


def test_from_data_follows_a_follows_path():
    lk = {
        "root": "root",
        "nodes": {
            "root": {"inputs": {"tool": ["other", "tool"], "other": "other"}},
            "other": {"inputs": {"tool": "tool_2"}},
            "tool_2": {"locked": {"rev": R1, "narHash": "sha256-T"}},
        },
    }
    m = pins.from_data({"inputs": [{"name": "tool", "url": "github:o/t", "python": "src"}]}, lk)
    assert m.pins[0].rev == R1


def test_from_workspace_gives_none_for_a_bad_workspace(tmp_path: Path):
    assert pins.from_workspace(tmp_path, "home.json") is None
    (tmp_path / "home.json").write_text('{"inputs": [{"name": "t", "url": "github:o/t", "python": "src"}]}')
    assert pins.from_workspace(tmp_path, "home.json") is None  # no lock
    (tmp_path / "flake.lock").write_text(json.dumps(lock(t={"locked": {"rev": R1, "narHash": "sha256-T"}})))
    assert got(pins.from_workspace(tmp_path, "home.json")).pins[0].rev == R1
    (tmp_path / "home.json").write_text("[]")
    assert pins.from_workspace(tmp_path, "home.json") is None


@pytest.mark.skipif(shutil.which("nix-instantiate") is None, reason="nix is not installed")
def test_nix_manifest_equals_the_manifest_of_the_workspace():
    """`nix/pins.nix` and `from_data` give the same rows; the Nix result is a `version` 1 manifest that `parse` reads."""
    declared = [
        {"name": "b", "url": f"https://u:tok{AT}host.org/o/b", "python": "src", "flake": False},
        {"name": "a", "url": "github:o/a", "python": "."},
        {"name": "z", "url": "github:o/z"},
    ]
    objects = {
        "a": {"rev": R1, "narHash": "sha256-A"},
        "b": {"narHash": "sha256-B"},
        "z": {"rev": R2, "narHash": "sha256-Z"},
    }
    expr = f"import {ROOT}/nix/pins.nix {{ declared = builtins.fromJSON ''{json.dumps(declared)}''; inputs = builtins.fromJSON ''{json.dumps(objects)}''; }}"
    done = subprocess.run(
        ["nix-instantiate", "--eval", "--strict", "--json", "--expr", expr], capture_output=True, text=True
    )
    assert done.returncode == 0, done.stderr
    from_nix = got(parse(done.stdout))
    assert json.loads(done.stdout)["version"] == pins.VERSION
    lk = lock(
        a={"locked": {"rev": R1, "narHash": "sha256-A"}},
        b={"locked": {"narHash": "sha256-B"}},
        z={"locked": {"rev": R2, "narHash": "sha256-Z"}},
    )
    assert from_nix == pins.from_data({"inputs": declared}, lk)
    assert [p.name for p in from_nix.pins] == ["a", "b"]


# --- the text -------------------------------------------------------------------------------------------------------
def test_default_line_is_one_plain_line_with_short_revs():
    m = Mismatch("tool", "tool", "github:o/t", R1, R2)
    line = format_mismatch(m, here="your home", there="the system")
    assert line == (
        "warning: the input `tool` is at aaaaaaa in your home, but the system has bbbbbbb. "
        "The Python code of the two pins can differ."
    )
    assert "\n" not in line and "/nix/store" not in line and "git " not in line


def test_short_form_of_a_nar_hash_drops_the_algorithm():
    assert pins.short("sha256-ABCDEFGHIJ=") == "ABCDEFG"


def test_the_layer_gives_its_own_text():
    m = Mismatch("tool", "tool", "github:o/t", R1, R2)
    out = format_mismatch(
        m, here="H", there="T", text="note: {local_name} {url} {local_rev}/{other_rev}\nin {here}, {there}"
    )
    assert out == "note: tool github:o/t aaaaaaa/bbbbbbb in H, T"


def test_lines_never_raise():
    a = man(pin("tool", "github:o/t", rev=R1))
    b = man(pin("tool", "github:o/t", rev=R2))
    assert len(pins.lines(a, b, here="h", there="t")) == 1
    assert pins.lines(a, b, here="h", there="t", text="{nope}") == []
    assert pins.lines(None, b, here="h", there="t") == []
