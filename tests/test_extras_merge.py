"""A typed field and an extra key in one section: the emitted value holds both.

A freeform section such as `systemd.user.services.NAME` has typed fields (`Service_ExecStart` is
`Service.ExecStart`) and extra keys (`Service = {"Restart": ...}`). The runtime joins them key by key.
The tests need no Nix.
"""

import importlib
import inspect
import pkgutil
from typing import Any, ClassVar

import pytest
from pydantic import ValidationError

import pynix_flake_parts
import pynix_hm
import pynix_os
from nixdantic import Force, Model, Text, _merge, supplied
from pynix_hm.systemd.user import User_Services_Value as HmService


class Section(Model):
    """A minimal freeform class with one typed field below a section."""

    __nix_paths__: ClassVar[dict[str, tuple[str, ...]]] = {"Service_ExecStart": ("Service", "ExecStart")}
    model_config = Model.model_config | {"extra": "allow"}
    Service_ExecStart: str | None = None


def test_typed_field_and_dict_extra_join() -> None:
    value = Section(Service_ExecStart="/bin/x", Service={"Restart": "on-failure"})
    assert supplied(value) == {"Service": {"ExecStart": "/bin/x", "Restart": "on-failure"}}


def test_typed_path_moves_out_of_the_dict_and_back() -> None:
    value = Section(Service={"ExecStart": "/bin/x", "Restart": "on-failure"})
    assert supplied(value) == {"Service": {"ExecStart": "/bin/x", "Restart": "on-failure"}}


def test_two_sections_are_kept() -> None:
    value = Section(Service_ExecStart="/bin/x", Unit={"Description": "d"}, Service={"Restart": "no"})
    assert supplied(value) == {"Service": {"ExecStart": "/bin/x", "Restart": "no"}, "Unit": {"Description": "d"}}


def test_a_priority_wrapper_in_an_extra_key_is_kept() -> None:
    wire = supplied(Section(Service={"Restart": Force("no")}))
    assert wire == {"Service": {"Restart": {"__nixdantic_ref__": {"kind": "priority", "level": 50, "value": "no"}}}}


def test_service_unit_with_typed_and_extra_keys() -> None:
    """The home unit of agentman (011 P3): a `Unit` and a `Service` dict with a typed `Text` and an extra key."""
    value = HmService(
        Unit={"Description": "agentman daemon", "Requires": ["agentman.socket"], "After": ["agentman.socket"]},
        Service={
            "ExecStartPre": Text("/bin/agentman", " migrate"),
            "ExecStart": Text("/bin/agentman", " serve --systemd-socket"),
            "Environment": ["A=1"],
            "Restart": "on-failure",
        },
    )
    wire = supplied(value)
    assert isinstance(wire, dict)
    assert wire["Unit"] == {
        "Description": "agentman daemon",
        "Requires": ["agentman.socket"],
        "After": ["agentman.socket"],
    }
    service = wire["Service"]
    assert isinstance(service, dict)
    assert set(service) == {"ExecStartPre", "ExecStart", "Environment", "Restart"}
    typed = HmService(
        Unit_Description="d", Service_ExecStart="/bin/x", Unit={"After": ["a"]}, Service={"Restart": "no"}
    )
    assert supplied(typed) == {
        "Unit": {"Description": "d", "After": ["a"]},
        "Service": {"ExecStart": "/bin/x", "Restart": "no"},
    }


def _freeform_classes() -> list[type[Model]]:
    found: list[type[Model]] = []
    for root in (pynix_hm, pynix_os, pynix_flake_parts):
        for info in pkgutil.walk_packages(root.__path__, root.__name__ + "."):
            module = importlib.import_module(info.name)
            for _, cls in inspect.getmembers(module, inspect.isclass):
                if (
                    issubclass(cls, Model)
                    and cls.__module__ == module.__name__
                    and cls.__nix_paths__
                    and cls.model_config.get("extra") == "allow"
                ):
                    found.append(cls)
    return found


def test_every_freeform_class_with_typed_paths_joins() -> None:
    """Each generated class that has typed paths and extra keys keeps both in one section."""
    classes = _freeform_classes()
    assert len(classes) > 100
    for cls in classes:
        field, path = sorted(cls.__nix_paths__.items())[0]
        fields: dict[str, Any] = {field: "typed", path[0]: {"ExtraKey": "extra"}}
        wire: Any = supplied(cls.model_construct(**fields))
        assert wire[path[0]]["ExtraKey"] == "extra", cls
        node: Any = wire
        for part in path:
            node = node[part]
        assert node == "typed", cls


def test_a_leaf_set_twice_with_unequal_values_raises() -> None:
    with pytest.raises(ValidationError, match=r"Service\.Environment is set twice: once as the typed field"):
        HmService(Service_Environment=["A=1"], Service={"Restart": "always", "Environment": ["B=2"]})


def test_a_leaf_set_twice_after_validation_raises() -> None:
    value = HmService.model_construct(Service_Environment=["A=1"], Service={"Environment": ["B=2"]})
    with pytest.raises(ValueError, match=r"Service\.Environment is set twice: once as the typed field"):
        supplied(value)


def test_a_leaf_set_twice_with_equal_values_joins() -> None:
    value = HmService(Service_Environment=["A=1"], Service={"Restart": "always", "Environment": ["A=1"]})
    assert supplied(value) == {"Service": {"Environment": ["A=1"], "Restart": "always"}}


def test_a_conflict_in_a_nested_dict_names_the_nested_path() -> None:
    result: dict[str, Any] = {"Service": {"Limits": {"Nofile": 1, "Nproc": 2}}}
    with pytest.raises(ValueError, match=r"Service\.Limits\.Nofile is set twice"):
        _merge(result, "Service", {"Limits": {"Nproc": 2, "Nofile": 3}})


def test_two_nested_dicts_join_key_by_key() -> None:
    result: dict[str, Any] = {"Service": {"Limits": {"Nofile": 1}}}
    _merge(result, "Service", {"Limits": {"Nproc": 2}, "Restart": "no"})
    assert result == {"Service": {"Limits": {"Nofile": 1, "Nproc": 2}, "Restart": "no"}}


def test_a_reference_leaf_against_a_plain_leaf_raises() -> None:
    value = Section.model_construct(Service_ExecStart=Text("/bin/x"), Service={"ExecStart": "/bin/y"})
    with pytest.raises(ValueError, match=r"Service\.ExecStart is set twice"):
        supplied(value)
