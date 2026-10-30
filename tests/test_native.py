"""`pynix_native`: the entry objects, their refusals, and their JSON (009-D40, 009-D49, 009-D52, 009-D53)."""

from typing import Any

import pytest
from pydantic import ValidationError

from pynix_native import (
    OWN,
    Input,
    NativeModule,
    NixpkgsPin,
    input_json,
    input_package_name,
    module_attr,
    nixpkgs_package_name,
    registered_nixpkgs,
    set_module_attr,
)

OLD = "d233902339c02a9c334e7e593de68855ad26c4cb"


def first_error(call) -> Any:
    with pytest.raises(ValidationError) as caught:
        call()
    return caught.value.errors()[0]


def test_native_module_keeps_a_workspace_path() -> None:
    assert NativeModule("fans.nix").file == "fans.nix"
    assert NativeModule("hw/fans.nix").file == "hw/fans.nix"


@pytest.mark.parametrize("bad", ["../x.nix", "/etc/x.nix", "fans.txt", "a/../../x.nix"])
def test_native_module_refuses_a_bad_path(bad: str) -> None:
    error = first_error(lambda: NativeModule(bad))
    assert error["msg"] == 'must be a .nix file below the workspace folder, for example "fans.nix"'


def test_nixpkgs_takes_a_full_commit() -> None:
    old = NixpkgsPin("old", OLD)
    assert (old.name, old.commit) == ("old", OLD)
    assert old.to_json() == {"name": "old", "commit": OLD}


@pytest.mark.parametrize("bad", ["d2339023", "master", OLD.upper(), OLD[:-1], OLD + "0"])
def test_nixpkgs_refuses_a_commit_that_does_not_pin(bad: str) -> None:
    error = first_error(lambda: NixpkgsPin("old", bad))
    assert error["loc"] == ("commit",)
    assert error["msg"] == (
        "must be a full commit of nixpkgs: 40 lower case hex digits (a branch name or a short commit does not pin)"
    )


@pytest.mark.parametrize("name", ["layer", "own", "Old", "1old", "", "has space", "a" * 33])
def test_nixpkgs_refuses_a_name(name: str) -> None:
    error = first_error(lambda: NixpkgsPin(name, OLD))
    assert error["loc"] == ("name",)
    assert error["msg"] == "must be a new name: lower case letters, digits, and '-' ('layer' and 'own' are taken)"


def test_nixpkgs_twice_with_one_commit_is_fine() -> None:
    NixpkgsPin("old", OLD)
    NixpkgsPin("old", OLD)
    assert registered_nixpkgs() == [{"name": "old", "commit": OLD}]


def test_nixpkgs_twice_with_two_commits_is_refused() -> None:
    NixpkgsPin("old", OLD)
    error = first_error(lambda: NixpkgsPin("old", "0" * 40))
    assert error["msg"] == "the nixpkgs `old` is already set to another commit"


def test_registered_nixpkgs_is_sorted_by_name() -> None:
    NixpkgsPin("zed", "1" * 40)
    NixpkgsPin("abc", "2" * 40)
    assert [n["name"] for n in registered_nixpkgs()] == ["abc", "zed"]


@pytest.mark.parametrize("name", ["self", "basix", "minix", "nixpkgs", "ext", "nixpkgs-old", "Bad", "1x", "a_b"])
def test_input_refuses_a_name(name: str) -> None:
    error = first_error(lambda: Input(name, "github:a/b"))
    assert error["loc"] == ("name",)
    assert error["msg"] == (
        "must be a new name: lower case letters, digits, and '-' ('basix', 'minix', 'nixpkgs', and 'self' are taken)"
    )


@pytest.mark.parametrize("url", ["github a/b", "github:a/b'", 'github:"x"', "noscheme", ""])
def test_input_refuses_a_url(url: str) -> None:
    error = first_error(lambda: Input("x", url))
    assert error["msg"] == (
        "must be a flake reference such as github:OWNER/REPO or git+file:///path (no spaces or quotes)"
    )


def test_input_refuses_a_module_name() -> None:
    error = first_error(lambda: Input("x", "github:a/b", modules=["bad name"]))
    assert error["msg"] == 'must be the name of a module in `nixosModules` of the input, for example "default"'


def test_input_refuses_a_nixpkgs_that_is_not_a_choice() -> None:
    first_error(lambda: Input("x", "github:a/b", nixpkgs="old"))  # ty: ignore[invalid-argument-type]


def test_input_has_no_follow_nixpkgs_field() -> None:
    with pytest.raises(ValidationError):
        Input("x", "github:a/b", follow_nixpkgs=True)  # ty: ignore[unknown-argument]


def test_input_json_without_nixpkgs_has_no_key() -> None:
    out = input_json(Input("nirinit", "github:amaanq/nirinit"), "system.py:5")
    assert out == {
        "name": "nirinit",
        "url": "github:amaanq/nirinit",
        "flake": True,
        "modules": [],
        "source": "system.py:5",
    }


def test_input_json_with_own() -> None:
    assert input_json(Input("x", "github:a/b", nixpkgs=OWN), "system.py:5")["nixpkgs"] == "own"


def test_input_json_with_a_nixpkgs() -> None:
    old = NixpkgsPin("old", OLD)
    out = input_json(Input("x", "github:a/b", modules=["default"], flake=False, nixpkgs=old), "system.py:5")
    assert out["nixpkgs"] == {"name": "old", "commit": OLD}
    assert out["modules"] == ["default"]
    assert out["flake"] is False


@pytest.mark.parametrize("folder", ["src", ".", "python", "lib/py", "a-b/c.d", "_x/y_z"])
def test_input_takes_a_python_folder(folder: str) -> None:
    assert Input("x", "github:a/b", python=folder).python == folder


def test_input_has_no_python_folder_by_default() -> None:
    assert Input("x", "github:a/b").python is None
    assert Input("x", "github:a/b", python=None).python is None


@pytest.mark.parametrize(
    "folder", ["", "/src", "/", "..", "../src", "src/..", "a/../b", "a//b", "src/", "./src", ".hidden", "a b", "a'b"]
)
def test_input_refuses_a_python_folder(folder: str) -> None:
    error = first_error(lambda: Input("x", "github:a/b", python=folder))
    assert error["loc"] == ("python",)
    assert error["msg"] == (
        'must be a folder below the input, such as "src" or "." for the input root (no leading "/", no "..")'
    )


def test_input_json_has_python_only_when_it_is_set() -> None:
    assert "python" not in input_json(Input("x", "github:a/b"), "system.py:5")
    assert input_json(Input("x", "github:a/b", python="src"), "system.py:5")["python"] == "src"
    assert input_json(Input("x", "github:a/b", flake=False, python="."), "system.py:5")["python"] == "."


def test_own_is_one_value() -> None:
    assert repr(OWN) == "OWN"


def test_package_names() -> None:
    assert input_package_name("nix-terminal") == "pynix_nix_terminal"
    assert nixpkgs_package_name("old-2") == "pynix_nixpkgs_old_2"


def test_the_module_word_is_nixos_modules_until_the_layer_sets_another() -> None:
    assert module_attr() == "nixosModules"
    try:
        set_module_attr("homeManagerModules")
        assert module_attr() == "homeManagerModules"
        error = first_error(lambda: Input("x", "github:a/b", modules=["bad name"]))
        assert (
            error["msg"] == 'must be the name of a module in `homeManagerModules` of the input, for example "default"'
        )
    finally:
        set_module_attr("nixosModules")
    error = first_error(lambda: Input("x", "github:a/b", modules=["bad name"]))
    assert "`nixosModules`" in error["msg"]


def test_the_module_word_must_be_a_plain_name() -> None:
    with pytest.raises(ValueError, match="plain name"):
        set_module_attr("not a name")
    assert module_attr() == "nixosModules"
