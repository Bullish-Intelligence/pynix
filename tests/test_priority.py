"""The merge priority and order wrappers (L128; SG34 form a): `Force`, `Default`, `Before`, `After`, `Order`.

The runtime tests need no Nix. The evaluation test runs the decoder with `lib.evalModules` of the pinned nixpkgs
(`flake.lock`, in the store, no network). A missing `nix` skips it.
"""

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from nixdantic import (
    After,
    Before,
    Default,
    Force,
    Order,
    PriorityError,
    Root,
    Unset,
    UnsetType,
    fragment,
)
from pynix_os.services.openssh import Openssh

ROOT = Path(__file__).resolve().parents[1]


class Fixture(Root):
    """A small root class with a flag, a text, and a list."""

    __nix_path__ = ("fixture",)
    flag: bool | UnsetType = Unset
    text: str | UnsetType = Unset
    names: list[str] | UnsetType = Unset


def value_of(item: Root) -> Any:
    return fragment(item, source="test.py:1")["value"]


def tag(kind: str, level: int, value: Any) -> dict[str, Any]:
    return {"__nixdantic_ref__": {"kind": kind, "level": level, "value": value}}


# --- run time ---------------------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("wrapper", "kind", "level"),
    [(Force, "priority", 50), (Default, "priority", 1000), (Before, "order", 500), (After, "order", 1500)],
)
def test_a_wrapper_writes_its_kind_and_level_at_emission(wrapper: Any, kind: str, level: int) -> None:
    assert value_of(Fixture(text=wrapper("x"))) == {"text": tag(kind, level, "x")}


def test_order_takes_a_level() -> None:
    assert value_of(Fixture(text=Order(2000, "x"))) == {"text": tag("order", 2000, "x")}


def test_a_value_with_no_wrapper_is_unchanged() -> None:
    assert value_of(Fixture(flag=True, text="x")) == {"flag": True, "text": "x"}


def test_the_wrapper_marks_one_field_only() -> None:
    assert value_of(Fixture(flag=Force(False), text="x")) == {"flag": tag("priority", 50, False), "text": "x"}


def test_a_list_is_one_value() -> None:
    assert value_of(Fixture(names=Before(["a", "b"]))) == {"names": tag("order", 500, ["a", "b"])}


def test_the_inner_value_gets_the_normal_check() -> None:
    with pytest.raises(ValidationError) as caught:
        Fixture(flag=Force("yes"))  # ty: ignore[invalid-argument-type]
    (error,) = caught.value.errors()
    assert error["loc"] == ("flag",)
    assert error["msg"] == "must be true or false"


def test_the_check_of_a_generated_class_reads_through_the_wrapper() -> None:
    with pytest.raises(ValidationError) as caught:
        Openssh(ports=Force([70000]))
    (error,) = caught.value.errors()
    assert error["ctx"]["option"] == "services.openssh.ports"


def test_a_wrapper_works_in_a_generated_class() -> None:
    assert value_of(Openssh(enable=Force(True), ports=Default([22]))) == {
        "enable": tag("priority", 50, True),
        "ports": tag("priority", 1000, [22]),
    }


def test_a_wrapper_inside_a_wrapper_is_refused() -> None:
    with pytest.raises(PriorityError) as caught:
        Force(Default(True))
    assert str(caught.value) == "Force(...) cannot hold Default(...): use one wrapper for one value."


@pytest.mark.parametrize("level", [1.5, "late", True, None])
def test_a_level_that_is_not_a_whole_number_is_refused(level: Any) -> None:
    with pytest.raises(PriorityError) as caught:
        Order(level, "x")
    assert str(caught.value) == f"Order: the level must be a whole number, found {level!r}."


def test_a_wrapper_on_one_item_of_a_list_is_refused() -> None:
    with pytest.raises(PriorityError) as caught:
        Fixture(names=["a", Force("b")])
    assert str(caught.value) == "Force(...) works on a whole value, not on one item of a list."


def test_a_wrapper_inside_a_free_form_set_is_marked_at_its_key() -> None:
    class Free(Root):
        __nix_path__ = ("free",)
        data: dict[str, str] | UnsetType = Unset

    assert value_of(Free(data={"a": Force("x"), "b": "y"})) == {"data": {"a": tag("priority", 50, "x"), "b": "y"}}


def test_a_wrapper_does_not_leak_into_the_next_value() -> None:
    first = Fixture(text=Force("x"))
    second = Fixture(text="x")
    assert value_of(first) == {"text": tag("priority", 50, "x")}
    assert value_of(second) == {"text": "x"}


# --- the decoder (Nix) ------------------------------------------------------------------------------------------

NIX = ["nix", "--extra-experimental-features", "nix-command flakes", "--offline"]

#: A plain module sets each option at normal priority. The decoder turns each fragment into one more module.
EVAL = """
let
  root = @ROOT@;
  lock = (builtins.fromJSON (builtins.readFile (root + "/flake.lock"))).nodes;
  nixpkgs = builtins.fetchTree (builtins.removeAttrs lock.nixpkgs.locked [ "dir" ]);
  lib = import (nixpkgs + "/lib");
  decoder = import (root + "/src/decoder.nix");
  fragments = builtins.fromJSON ''@FRAGMENTS@'';
  result = lib.evalModules {
    specialArgs = { pkgs = null; };
    modules = [
      {
        options.fixture.flag = lib.mkOption { type = lib.types.bool; };
        options.fixture.text = lib.mkOption { type = lib.types.lines; };
        options.fixture.names = lib.mkOption { type = lib.types.listOf lib.types.str; };
      }
      { fixture = { flag = true; text = "normal"; names = [ "normal" ]; }; }
    ] ++ map (fragment: decoder { inherit fragment; }) fragments;
  };
in result.config.fixture
"""


@pytest.mark.skipif(shutil.which("nix") is None, reason="nix is not installed")
def test_the_decoder_gives_the_priority_and_the_order() -> None:
    fragments = [
        fragment(Fixture(flag=Force(False)), source="test.py:1"),
        fragment(Fixture(text=Before("first"), names=Before(["first"])), source="test.py:2"),
        fragment(Fixture(text=After("last"), names=Order(2000, ["last"])), source="test.py:3"),
    ]
    expr = EVAL.replace("@ROOT@", str(ROOT)).replace("@FRAGMENTS@", json.dumps(fragments))
    done = subprocess.run([*NIX, "eval", "--impure", "--json", "--expr", expr], capture_output=True, text=True)
    assert done.returncode == 0, done.stderr
    config = json.loads(done.stdout)
    assert config["flag"] is False  # Force beats the normal `true`
    assert config["text"] == "first\nnormal\nlast"  # Before 500, normal 1000, After 1500
    assert config["names"] == ["first", "normal", "last"]  # Order 2000 comes last
