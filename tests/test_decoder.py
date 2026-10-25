"""The decoder (`src/decoder.nix`): one test for each reference kind that a Python class writes.

The tests run the decoder with `lib.evalModules` of the pinned nixpkgs (`flake.lock`, in the store, no network) and a
small fake package set. A missing `nix` skips them.
"""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from nixdantic import Native, Package, Text, supplied
from pynix_pkgs._pkgref import Exe

ROOT = Path(__file__).resolve().parents[1]
NIX = ["nix", "--extra-experimental-features", "nix-command flakes", "--offline"]

EVAL = """
let
  root = @ROOT@;
  lock = (builtins.fromJSON (builtins.readFile (root + "/flake.lock"))).nodes;
  nixpkgs = builtins.fetchTree (builtins.removeAttrs lock.nixpkgs.locked [ "dir" ]);
  lib = import (nixpkgs + "/lib");
  decoder = import (root + "/src/decoder.nix");
  package = name: main: {
    type = "derivation";
    inherit name;
    outPath = "/nix/store/00000000000000000000000000000000-" + name;
    meta = lib.optionalAttrs (main != null) { mainProgram = main; };
  };
  pkgs = { hello = package "hello" "hello"; ripgrep = package "ripgrep" "rg"; };
  result = lib.evalModules {
    specialArgs = { inherit pkgs; inputs = { marker = "from-inputs"; }; };
    modules = [
      { options.fixture.value = lib.mkOption { type = lib.types.raw; }; }
      (decoder { fragment = builtins.fromJSON ''@FRAGMENT@''; nativeRoot = @NATIVE@; })
    ];
  };
in (@THEN@) result.config.fixture.value
"""


def decode(value: object, native_root: Path = ROOT, then: str = "x: x") -> str:
    """Decode one value at `fixture.value` and give the result as a string (a store path or an error line).

    `native_root` is the folder of the native value files. `then` is a Nix function that turns the decoded value into
    the string to print (it is the identity by default).
    """
    fragment = {"version": 1, "source": "test.py:1", "path": ["fixture", "value"], "value": supplied(value)}
    expr = (
        EVAL.replace("@ROOT@", str(ROOT))
        .replace("@NATIVE@", str(native_root))
        .replace("@THEN@", then)
        .replace("@FRAGMENT@", json.dumps(fragment))
    )
    done = subprocess.run([*NIX, "eval", "--impure", "--raw", "--expr", expr], capture_output=True, text=True)
    return done.stdout if done.returncode == 0 else done.stderr


needs_nix = pytest.mark.skipif(shutil.which("nix") is None, reason="nix is not installed")


@needs_nix
def test_the_decoder_gives_the_exe_of_a_package() -> None:
    assert Exe("ripgrep").model_dump() == {"kind": "exe", "attr": "ripgrep"}
    assert decode(Exe("ripgrep")) == "/nix/store/00000000000000000000000000000000-ripgrep/bin/rg"


@needs_nix
def test_the_exe_is_a_part_of_a_text() -> None:
    assert decode(Text(Exe("hello"), " --flag")) == "/nix/store/00000000000000000000000000000000-hello/bin/hello --flag"


@needs_nix
def test_the_decoder_gives_a_package_as_the_package() -> None:
    assert decode(Text(Package("hello"), "/bin/hello")) == "/nix/store/00000000000000000000000000000000-hello/bin/hello"


@needs_nix
def test_the_decoder_names_the_source_of_an_unknown_exe() -> None:
    assert "nixdantic: test.py:1: unknown package `nothing`: pkgs has no attribute `nothing`" in decode(Exe("nothing"))


@needs_nix
def test_the_decoder_refuses_an_unknown_kind() -> None:
    class Odd(Package):
        kind: str = "odd"  # type: ignore[assignment]

    assert "Unknown nixdantic reference: odd" in decode(Odd("hello"))


@needs_nix
def test_a_native_value_file_that_is_an_attribute_set_works(tmp_path: Path) -> None:
    (tmp_path / "plain.nix").write_text('{ tool = "plain-tool"; }')
    assert decode(Native("plain.nix", ["tool"]), tmp_path) == "plain-tool"


@needs_nix
def test_a_native_value_file_that_is_a_function_gets_pkgs_and_inputs(tmp_path: Path) -> None:
    (tmp_path / "fn.nix").write_text(
        '{ pkgs, inputs, ... }: { tool = "${pkgs.hello}/bin/hello"; marker = inputs.marker; }'
    )
    hello = "/nix/store/00000000000000000000000000000000-hello/bin/hello"
    assert decode(Native("fn.nix", ["tool"]), tmp_path) == hello
    assert decode(Native("fn.nix", ["marker"]), tmp_path) == "from-inputs"


@needs_nix
def test_a_native_value_file_function_gets_only_the_arguments_it_names(tmp_path: Path) -> None:
    (tmp_path / "pkgs-only.nix").write_text("{ pkgs }: { name = pkgs.hello.name; }")
    assert decode(Native("pkgs-only.nix", ["name"]), tmp_path) == "hello"


@needs_nix
def test_a_whole_value_overlay_stays_a_function(tmp_path: Path) -> None:
    """PF-8: `Native("overlay.nix")` with no `attr` is an overlay. The decoder must not call it with `{ }`."""
    (tmp_path / "overlay.nix").write_text('final: prev: { marker = "overlay-marker"; }')
    assert decode(Native("overlay.nix"), tmp_path, "o: (o { } { }).marker") == "overlay-marker"


@needs_nix
def test_a_whole_value_file_that_names_an_argument_gets_the_module_arguments(tmp_path: Path) -> None:
    (tmp_path / "named.nix").write_text("{ pkgs, inputs, ... }: { tool = pkgs.hello.name; marker = inputs.marker; }")
    assert decode(Native("named.nix"), tmp_path, "v: v.tool + v.marker") == "hellofrom-inputs"


@needs_nix
def test_a_whole_value_attribute_set_file_stays_as_it_is(tmp_path: Path) -> None:
    (tmp_path / "plain.nix").write_text('{ tool = "plain-tool"; }')
    assert decode(Native("plain.nix"), tmp_path, "v: v.tool") == "plain-tool"


@needs_nix
def test_a_whole_value_file_without_named_arguments_is_returned_as_a_function(tmp_path: Path) -> None:
    """The edge of PF-8: `{ ... }:` names no argument, so a whole-value reference does not call it."""
    (tmp_path / "bare.nix").write_text('{ ... }: { bare = "bare"; }')
    assert decode(Native("bare.nix"), tmp_path, "v: builtins.typeOf v") == "lambda"


@needs_nix
def test_a_file_without_named_arguments_is_called_when_the_reference_has_an_attribute_path(tmp_path: Path) -> None:
    (tmp_path / "bare.nix").write_text('{ ... }: { bare = "bare"; }')
    assert decode(Native("bare.nix", ["bare"]), tmp_path) == "bare"
