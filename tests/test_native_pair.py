"""`pynix_native.pair`: the pair check of a generated package against `flake.lock` (009-D48)."""

import copy
import json
from pathlib import Path

import pytest

from pynix_native import (
    NAMES_GENERATOR,
    Found,
    FoundInput,
    Pair,
    check_input,
    check_nixpkgs,
    check_pairs,
    discover,
    error_lines,
    follow,
    input_cache_key,
    input_lock,
    names_cache_key,
    nixpkgs_lock,
    read_lock,
    read_source,
    to_regenerate,
)

FIXTURES = Path(__file__).parent / "fixtures" / "native"
GEN = "input-gen-1"
LAYER = "e7439b6b14ad3cc35d05608ebca9bce01a25f5f8"
OLD = "d233902339c02a9c334e7e593de68855ad26c4cb"
NEWER = "0bb7ec54c8483066ec9d7720e780a5caa71f8612"
OWN_NIXPKGS = "18b9261cb3294b6d2a06d03f96872827b8fe2698"
NIRINIT_HASH = "sha256-jpSYhiJNI5u/1CJ1RY+9BkSQtvishCfm5n+l9r7hdEk="
NIRINIT_REV = "0e43f61069f81bba1114475cae2e84aa0965a1a3"
PYTUIN_HASH = "sha256-I3a3onXGZDzPtXCAJmyUPDPcB9GYtaaSs/7HRpjkprU="
OLD_HASH = "sha256-30sZNZoA1cqF5JNO9fVX+wgiQYjB7HJqqJ4ztCDeBZE="


@pytest.fixture
def w3() -> dict:
    return read_lock(FIXTURES / "W3-flake.lock")


@pytest.fixture
def found():
    return discover(FIXTURES / "W3-system.txt", "system.py")


def write(folder: Path, module: str, record: dict) -> None:
    (folder / module).mkdir(parents=True, exist_ok=True)
    body = "".join(f"    {json.dumps(k)}: {json.dumps(v)},\n" for k, v in sorted(record.items()))
    (folder / module / "_generation.py").write_text(
        f'"""The source of this generated package."""\n\nSOURCE: dict[str, str] = {{\n{body}}}\n'
    )


def make_all(folder: Path, generator: str = GEN, names_generator: str = NAMES_GENERATOR) -> None:
    """The three input packages and the name list of W3, as apply would make them from `W3-flake.lock`."""
    write(
        folder, "pynix_nirinit", {"narHash": NIRINIT_HASH, "rev": NIRINIT_REV, "nixpkgs": LAYER, "generator": generator}
    )
    write(folder, "pynix_pytuin", {"narHash": PYTUIN_HASH, "nixpkgs": OWN_NIXPKGS, "generator": generator})
    write(
        folder,
        "pynix_nirinitold",
        {"narHash": NIRINIT_HASH, "rev": NIRINIT_REV, "nixpkgs": OLD, "generator": generator},
    )
    write(
        folder, "pynix_nixpkgs_old", {"commit": OLD, "narHash": OLD_HASH, "generator": names_generator, "name": "old"}
    )


def statuses(pairs: list[Pair]) -> dict[str, str]:
    return {f"{p.kind}:{p.name}": p.status for p in pairs}


def test_follows_reach_the_nixpkgs_of_each_input(w3: dict) -> None:
    assert input_lock(w3, "nirinit").nixpkgs_commit == LAYER  # root nixpkgs follows basix/nixpkgs
    assert input_lock(w3, "nirinitold").nixpkgs_commit == OLD  # follows nixpkgs-old
    assert input_lock(w3, "pytuin").nixpkgs_commit == OWN_NIXPKGS  # its own lock
    assert input_lock(w3, "nirinit").narHash == NIRINIT_HASH
    assert input_lock(w3, "pytuin").rev is None


def test_follow_walks_a_path_from_the_root(w3: dict) -> None:
    assert follow(w3, ["basix", "nixpkgs"]) == "nixpkgs"
    assert follow(w3, "nirinit") == "nirinit"


def test_nixpkgs_lock(w3: dict) -> None:
    pin = nixpkgs_lock(w3, "old")
    assert (pin.commit, pin.narHash) == (OLD, OLD_HASH)


def test_everything_matches(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path)
    pairs = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert statuses(pairs) == {
        "nixpkgs:old": "ok",
        "input:nirinit": "ok",
        "input:pytuin": "ok",
        "input:nirinitold": "ok",
    }
    assert error_lines(pairs) == []
    assert to_regenerate(pairs) == []


def test_narhash_moved(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path)
    w3 = copy.deepcopy(w3)
    w3["nodes"]["nirinit"]["locked"]["narHash"] = "sha256-moved"
    pairs = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert error_lines(pairs) == [
        "system.py:17: the package `pynix_nirinit` was made from another version of `nirinit` than flake.lock holds; "
        "run `basix apply` to make it again"
    ]
    assert statuses(pairs)["input:nirinit"] == "stale"
    assert [p.name for p in to_regenerate(pairs)] == ["nirinit"]


def test_the_command_is_the_caller_choice(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path)
    w3 = copy.deepcopy(w3)
    w3["nodes"]["pytuin"]["locked"]["narHash"] = "sha256-moved"
    line = error_lines(check_pairs(found, w3, tmp_path, "minix apply", generator=GEN))[0]
    assert line.endswith("run `minix apply` to make it again")


def test_a_moved_revision_with_one_narhash_is_stale(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path)
    w3 = copy.deepcopy(w3)
    w3["nodes"]["nirinit"]["locked"]["rev"] = "1" * 40
    assert statuses(check_pairs(found, w3, tmp_path, "basix apply", generator=GEN))["input:nirinit"] == "stale"


def test_the_nixpkgs_moved_is_found_with_a_silent_narhash() -> None:
    """SG44 P5: the commit of `old` moves. The narHash of `nirinitold` stays, so a narHash check alone says nothing."""
    p5 = read_lock(FIXTURES / "P5-flake.lock")
    found = discover(FIXTURES / "W3-system.txt", "system.py")
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        make_all(Path(tmp))
        pairs = check_pairs(found, p5, Path(tmp), "basix apply", generator=GEN)
    assert error_lines(pairs) == [
        "system.py:7: the package list `old` was made from another commit than flake.lock holds "
        f"({OLD[:12]} against {NEWER[:12]}); run `basix apply` to make it again",
        f"system.py:17: the package `pynix_nirinitold` was made with another nixpkgs ({OLD[:12]}) "
        f"than flake.lock gives `nirinitold` now ({NEWER[:12]}); run `basix apply` to make it again",
    ]
    ok = {p.name for p in pairs if p.status == "ok"}
    assert ok == {"nirinit", "pytuin"}


def test_the_generator_moved_is_no_error(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path, generator="input-gen-0", names_generator="nixpkgs-names-0")
    pairs = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert set(statuses(pairs).values()) == {"regenerate"}
    assert error_lines(pairs) == []
    assert all(p.line is None for p in pairs)
    assert len(to_regenerate(pairs)) == 4


def test_no_generator_for_inputs_skips_that_comparison(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path, generator="anything")
    pairs = check_pairs(found, w3, tmp_path, "basix apply")
    assert {p.status for p in pairs if p.kind == "input"} == {"ok"}


def test_a_narhash_difference_wins_over_a_generator_difference(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path, generator="input-gen-0")
    w3 = copy.deepcopy(w3)
    w3["nodes"]["nirinit"]["locked"]["narHash"] = "sha256-moved"
    assert statuses(check_pairs(found, w3, tmp_path, "basix apply", generator=GEN))["input:nirinit"] == "stale"


def test_a_package_that_is_not_made(tmp_path: Path, w3: dict, found) -> None:
    pairs = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert {p.status for p in pairs} == {"missing"}
    assert error_lines(pairs)[0] == (
        "system.py:7: the package list `old` is not made yet; run `basix apply` to make it"
    )
    assert "system.py:17: the package `pynix_nirinit` is not made yet; run `basix apply` to make it" in error_lines(
        pairs
    )


def test_an_input_that_the_lock_lacks(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path)
    w3 = copy.deepcopy(w3)
    del w3["nodes"]["root"]["inputs"]["pytuin"]
    pairs = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert statuses(pairs)["input:pytuin"] == "unlocked"
    assert "system.py:17: flake.lock holds no input `pytuin` yet; run `basix apply` to lock it" in error_lines(pairs)
    assert "pytuin" not in [p.name for p in to_regenerate(pairs)]


def test_a_nixpkgs_that_the_lock_lacks(tmp_path: Path, w3: dict, found) -> None:
    make_all(tmp_path)
    w3 = copy.deepcopy(w3)
    del w3["nodes"]["root"]["inputs"]["nixpkgs-old"]
    pairs = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert statuses(pairs)["nixpkgs:old"] == "unlocked"
    assert statuses(pairs)["input:nirinitold"] == "unlocked"  # its follows path is gone


def test_an_input_with_flake_false_has_no_package(tmp_path: Path, w3: dict) -> None:
    found = Found((FoundInput("src", "github:a/b", False, (), None, "system.py", 3),), ())
    assert check_pairs(found, w3, tmp_path, "basix apply") == []


def test_an_input_with_flake_false_and_python_is_checked(tmp_path: Path, w3: dict) -> None:
    found = Found(
        (FoundInput("pytuin", "path:/srv/example/inputs/pytuin", False, (), None, "system.py", 3, "src"),), ()
    )
    missing = check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)
    assert statuses(missing) == {"input:pytuin": "missing"}
    make_all(tmp_path)
    assert statuses(check_pairs(found, w3, tmp_path, "basix apply", generator=GEN)) == {"input:pytuin": "ok"}
    assert statuses(check_pairs(found, w3, tmp_path, "basix apply", generator="input-gen-2")) == {
        "input:pytuin": "regenerate"
    }
    moved = copy.deepcopy(w3)
    moved["nodes"]["pytuin"]["locked"]["narHash"] = "sha256-moved"
    stale = check_pairs(found, moved, tmp_path, "basix apply", generator=GEN)
    assert statuses(stale) == {"input:pytuin": "stale"}
    assert error_lines(stale) == [
        "system.py:3: the package `pynix_pytuin` was made from another version of `pytuin` than flake.lock holds; "
        "run `basix apply` to make it again"
    ]


def test_check_input_alone(tmp_path: Path, w3: dict, found) -> None:
    write(tmp_path, "pynix_nirinit", {"narHash": NIRINIT_HASH, "nixpkgs": OLD})
    pair = check_input(found.inputs[0], w3, tmp_path, "basix apply")
    assert pair.status == "stale"
    assert pair.line is not None and "another nixpkgs" in pair.line


def test_check_nixpkgs_alone(tmp_path: Path, w3: dict, found) -> None:
    write(tmp_path, "pynix_nixpkgs_old", {"commit": OLD, "narHash": OLD_HASH, "generator": NAMES_GENERATOR})
    assert check_nixpkgs(found.nixpkgs[0], w3, tmp_path, "basix apply").status == "ok"


def test_read_source_reads_text_and_runs_nothing(tmp_path: Path) -> None:
    file = tmp_path / "_generation.py"
    file.write_text('raise SystemExit("run")\nSOURCE: dict[str, str] = {"narHash": "x"}\nFORMAT: str = "f"\n')
    assert read_source(file) == {"narHash": "x"}


def test_read_source_of_a_missing_or_broken_file(tmp_path: Path) -> None:
    assert read_source(tmp_path / "none.py") is None
    (tmp_path / "bad.py").write_text("SOURCE = (\n")
    assert read_source(tmp_path / "bad.py") is None
    (tmp_path / "other.py").write_text("X = 1\n")
    assert read_source(tmp_path / "other.py") is None


def test_the_names_cache_key_follows_the_narhash_and_the_generator(w3: dict) -> None:
    node = w3["nodes"]["nixpkgs-old"]
    key = names_cache_key(node, NAMES_GENERATOR)
    assert key == names_cache_key(node["locked"], NAMES_GENERATOR)  # a node or its `locked` part
    assert len(key) == 12
    assert key != names_cache_key(node, "nixpkgs-names-0")
    assert key != names_cache_key(w3["nodes"]["nixpkgs"], NAMES_GENERATOR)
    other = copy.deepcopy(node)
    other["locked"]["rev"] = "f" * 40  # the key reads the narHash, not the revision
    assert key == names_cache_key(other, NAMES_GENERATOR)


def test_the_input_cache_key_follows_the_source_the_nixpkgs_and_the_generator(w3: dict) -> None:
    key = input_cache_key(w3, "nirinit", GEN)
    assert key != input_cache_key(w3, "nirinitold", GEN)  # same source, another nixpkgs
    assert key != input_cache_key(w3, "nirinit", "input-gen-2")
    assert key == input_cache_key(copy.deepcopy(w3), "nirinit", GEN)
