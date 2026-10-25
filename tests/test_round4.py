"""Round 4 of the 009 concept: `Root` and `RootOnly`, positional references, `PathRef`, references in free-form values,
and the flat namespaces `pynix_os.all` and `pynix_hm.all`. Ported from the SG33 gate and the SG35 probes."""

from typing import Annotated

import pytest
from pydantic import ValidationError

from nixdantic import (
    ConfigRef,
    Model,
    Native,
    Package,
    PathRef,
    Root,
    RootOnly,
    Text,
    fragment,
    is_root,
    nested_class_text,
)
from pynix import generate
from pynix_hm import all as hm
from pynix_os import all as nixos
from pynix_os.top import Top


class Holder(Model):
    """A small stand-in for `Machine` and `Home`: `options` takes root classes only."""

    options: list[Annotated[Model, RootOnly]]


def refusal(item: Model) -> str:
    with pytest.raises(ValidationError) as caught:
        Holder(options=[item])
    (error,) = caught.value.errors()
    assert error["loc"] == ("options", 0)
    return error["msg"]


# --- 009-D41: a nested class in `options` ----------------------------------------------------------------------


def test_nested_class_is_refused_with_its_parent() -> None:
    assert refusal(nixos.Loader_Efi(canTouchEfiVariables=True)) == (
        "Loader_Efi is a part of Loader; write Loader(efi=Loader_Efi(...))"
    )


def test_nested_class_of_home_manager_is_refused() -> None:
    assert refusal(hm.Git_Lfs(enable=True)) == "Git_Lfs is a part of Git; write Git(lfs=Git_Lfs(...))"


def test_deep_class_names_the_chain_up_to_three_levels() -> None:
    item = nixos.Loader_GenericExtlinuxCompatible_MirroredBoots_Item(path="/x")
    assert refusal(item) == (
        "Loader_GenericExtlinuxCompatible_MirroredBoots_Item is a part of Loader_GenericExtlinuxCompatible, "
        "which is a part of Loader; write Loader(generic_extlinux_compatible="
        "Loader_GenericExtlinuxCompatible(mirroredBoots=[Loader_GenericExtlinuxCompatible_MirroredBoots_Item(...)]))"
    )


def test_parent_form_is_accepted() -> None:
    loader = nixos.Loader(efi=nixos.Loader_Efi(canTouchEfiVariables=True))
    assert Holder(options=[loader]).options == [loader]


def test_fragment_refuses_a_part_class() -> None:
    with pytest.raises(ValueError, match=r"Loader_Efi is a part of Loader; write Loader\(efi=Loader_Efi\(\.\.\.\)\)"):
        fragment(nixos.Loader_Efi(canTouchEfiVariables=True))


def test_fragment_of_the_parent_has_its_path() -> None:
    frag = fragment(nixos.Loader(efi=nixos.Loader_Efi(canTouchEfiVariables=True)))
    assert frag["path"] == ["boot", "loader"]
    assert frag["value"] == {"efi": {"canTouchEfiVariables": True}}


def test_root_marks_a_class_with_its_own_path() -> None:
    assert issubclass(nixos.Loader, Root) and is_root(nixos.Loader)
    assert not issubclass(nixos.Loader_Efi, Root) and not is_root(nixos.Loader_Efi)
    assert is_root(Top) and Top.__nix_path__ == ()  # the empty path still counts as a path of its own
    assert nested_class_text(nixos.Loader_Efi).startswith("Loader_Efi is a part of Loader")


# --- 009-D42: references take their main value by position ------------------------------------------------------


def test_positional_and_keyword_references_are_equal() -> None:
    positional = [
        Package("htop"),
        ConfigRef(["networking", "hostName"]),
        Native("x.nix"),
        Native("x.nix", ["a", "b"]),
        Text(Package("hello"), "/bin/hello"),
    ]
    keyword = [
        Package(attr="htop"),
        ConfigRef(path=["networking", "hostName"]),
        Native(file="x.nix"),
        Native(file="x.nix", attr=["a", "b"]),
        Text(Package(attr="hello"), "/bin/hello"),
    ]
    assert positional == keyword


def test_wrong_positional_calls_say_what_is_wrong() -> None:
    with pytest.raises(TypeError, match=r"Package\(\) takes 1 positional arguments but 2 were given"):
        Package("a", "b")  # ty: ignore[too-many-positional-arguments]
    with pytest.raises(TypeError, match=r"Package\(\) got multiple values for argument 'attr'"):
        Package("a", attr="b")  # ty: ignore[parameter-already-assigned]


def test_a_reference_validates_inside_a_model_from_a_dict() -> None:
    # Pydantic must not call the positional `__init__` with the keys of a dict.
    assert nixos.Atticd.model_validate({"settings": {"a": Package("hello")}}).settings == {"a": Package("hello")}


# --- 009-D44: references and paths in free-form values ----------------------------------------------------------


def test_path_ref_reaches_the_wire_format() -> None:
    frag = fragment(nixos.Boot(kernelPatches=[{"name": "x", "patch": PathRef(file="fix.patch")}]))
    assert frag["value"] == {
        "kernelPatches": [{"name": "x", "patch": {"__nixdantic_ref__": {"kind": "path", "file": "fix.patch"}}}]
    }


def test_free_form_values_hold_references() -> None:
    package = fragment(nixos.Atticd(settings={"a": Package("hello")}))
    assert package["value"] == {"settings": {"a": {"__nixdantic_ref__": {"kind": "package", "attr": "hello"}}}}
    path = ["boot", "binfmt", "emulatedSystems"]
    typed = fragment(nixos.Nix(settings=nixos.Nix_Settings(**{"extra-platforms": ConfigRef(path)})))
    assert typed["value"] == {"settings": {"extra-platforms": {"__nixdantic_ref__": {"kind": "config", "path": path}}}}
    service = nixos.Systemd_Services_Value(serviceConfig={"X": ConfigRef(["a"])})
    wire = fragment(nixos.Systemd(services={"x": service}))["value"]
    assert wire == {
        "services": {"x": {"serviceConfig": {"X": {"__nixdantic_ref__": {"kind": "config", "path": ["a"]}}}}}
    }


def test_free_form_values_refuse_an_arbitrary_object() -> None:
    with pytest.raises(ValidationError):
        nixos.Atticd(settings={"a": object()})  # ty: ignore[invalid-argument-type]


def test_free_form_containers_take_a_nested_constant() -> None:
    value = nixos.Atticd(settings={"a": {"b": [1, "two", None, {"c": 1.5}]}})
    assert fragment(value)["value"] == {"settings": {"a": {"b": [1, "two", None, {"c": 1.5}]}}}


def test_text_takes_a_path_part() -> None:
    assert Text("a", PathRef(file="x")).parts == ["a", PathRef(file="x")]


# --- 009-D42: the flat namespaces ------------------------------------------------------------------------------


def test_namespace_gives_the_class() -> None:
    from pynix_os.boot.loader import Loader, Loader_Efi

    assert nixos.Loader is Loader and nixos.Loader_Efi is Loader_Efi


def test_colliding_plain_name_goes_to_none_of_its_classes() -> None:
    with pytest.raises(AttributeError) as caught:
        _ = nixos.Firewall  # ty: ignore[unresolved-attribute]
    assert str(caught.value) == (
        "The flat list of pynix_os has no class Firewall. Two classes have this name. "
        "Write one of: Networking_Firewall, Nix_Firewall."
    )
    assert nixos.Networking_Firewall is not nixos.Nix_Firewall


def test_class_named_after_its_own_path_keeps_the_plain_name() -> None:
    assert nixos.Boot.__nix_path__ == ("boot",)  # `Boot` is in the collision list, and it keeps its name


def test_home_manager_collision_has_the_same_rule() -> None:
    assert "Programs_Autorandr" in dir(hm) and "Services_Autorandr" in dir(hm)
    with pytest.raises(
        AttributeError, match="Two classes have this name. Write one of: Programs_Autorandr, Services_Autorandr."
    ):
        _ = hm.Autorandr  # ty: ignore[unresolved-attribute]


def test_unknown_name_has_no_collision_hint() -> None:
    with pytest.raises(AttributeError) as caught:
        _ = nixos.Loaderr  # ty: ignore[unresolved-attribute]
    assert str(caught.value) == "The flat list of pynix_os has no class Loaderr."


def test_namespace_lists_every_class() -> None:
    assert len(dir(nixos)) == 4733 and len(dir(hm)) == 1226


def test_generator_rule_on_a_small_package(tmp_path) -> None:
    package = tmp_path / "toy"
    (package / "net").mkdir(parents=True)
    (package / "services").mkdir()
    (package / "net" / "__options__.py").write_text(
        'class Net(Root):\n    __nix_path__: ClassVar[tuple[str, ...]] = ("net",)\n\n\n'
        'class Firewall(Root):\n    __nix_path__: ClassVar[tuple[str, ...]] = ("net", "firewall")\n'
    )
    (package / "services" / "fw.py").write_text(
        'class Firewall(Root):\n    __nix_path__: ClassVar[tuple[str, ...]] = ("services", "fw")\n\n\n'
        "class Firewall_Rule(Model):\n    pass\n"
    )
    generate.write_namespace(tmp_path, "toy")
    scope: dict[str, object] = {"__name__": "toy.all"}
    exec(compile((package / "all.py").read_text(), "all.py", "exec"), scope)
    assert scope["_INDEX"] == {
        "Net": "toy.net.__options__:Net",
        "Net_Firewall": "toy.net.__options__:Firewall",
        "Services_Fw_Firewall": "toy.services.fw:Firewall",
        "Firewall_Rule": "toy.services.fw:Firewall_Rule",
    }
