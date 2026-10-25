"""`pynix_native.discover`: the reader of `Input(...)` and `NixpkgsPin(...)` in an entry file (009-D49, 009-D53)."""

from pathlib import Path

import pytest

from pynix_native import (
    OWN,
    DiscoveryError,
    Input,
    NixpkgsPin,
    discover,
    discover_source,
    input_json,
)

FIXTURES = Path(__file__).parent / "fixtures" / "native"
OLD = "d233902339c02a9c334e7e593de68855ad26c4cb"
NIRINIT = "github:amaanq/nirinit/0e43f61069f81bba1114475cae2e84aa0965a1a3"


def read(name: str):
    return discover(FIXTURES / f"{name}.txt", "system.py")


def test_w3_has_three_inputs_and_one_nixpkgs() -> None:
    found = read("W3-system")
    assert [i.name for i in found.inputs] == ["nirinit", "pytuin", "nirinitold"]
    assert [i.nixpkgs for i in found.inputs[:2]] == [None, "own"]
    old = found.inputs[2].nixpkgs
    assert getattr(old, "name", None) == "old"
    assert [(n.name, n.commit, n.source) for n in found.nixpkgs] == [("old", OLD, "system.py:7")]


def test_w3_sources_are_the_lines_of_the_calls() -> None:
    found = read("W3-system")
    assert {i.source for i in found.inputs} == {"system.py:17"}


def test_f1_reads_a_name_own_and_none() -> None:
    found = read("F1")
    assert [i.name for i in found.inputs] == ["modonly", "modonly2", "modonly3"]
    assert [i.source for i in found.inputs] == ["system.py:12", "system.py:13", "system.py:14"]
    assert getattr(found.inputs[0].nixpkgs, "commit", None) == OLD
    assert found.inputs[1].nixpkgs is None
    assert found.inputs[2].nixpkgs == "own"


def test_f2_reads_modules() -> None:
    found = read("F2")
    assert found.inputs[0].modules == ("default",)


def test_h1_reads_a_home_entry() -> None:
    found = read("H1")
    assert [i.name for i in found.inputs] == ["example-tool"]
    assert [n.name for n in found.nixpkgs] == ["old"]


def test_an_entry_with_no_input_gives_empty_json() -> None:
    assert discover_source("machine = Machine()\n").to_json() == {"inputs": []}


def test_json_has_nixpkgs_only_when_the_entry_has_one() -> None:
    assert "nixpkgs" not in discover_source('x = Input("a", "github:a/b")\n').to_json()
    assert "nixpkgs" in read("W3-system").to_json()


def test_nixpkgs_option_calls_do_not_declare_pins() -> None:
    text = f'Nixpkgs(config={{"allowUnfree": True}})\nNixpkgs(overlays=[])\nold = NixpkgsPin("old", "{OLD}")\n'
    assert [pin.name for pin in discover_source(text).nixpkgs] == ["old"]


def test_a_pin_call_with_no_argument_stops_the_reader() -> None:
    assert fails("old = NixpkgsPin()\n") == "system.py:1:7: NixpkgsPin(...) needs name and commit, as plain text"


def test_json_equals_the_json_of_the_objects() -> None:
    """The stub writer reads the discovery JSON; the compiler writes the object JSON. They agree, apart from `source`."""
    old = NixpkgsPin("old", OLD)
    made = [
        Input("nirinit", NIRINIT),
        Input("pytuin", "path:/srv/example/inputs/pytuin", nixpkgs=OWN),
        Input("nirinitold", NIRINIT, nixpkgs=old),
    ]
    want = [{k: v for k, v in input_json(i, "x").items() if k != "source"} for i in made]
    have = [{k: v for k, v in i.items() if k != "source"} for i in read("W3-system").to_json()["inputs"]]
    assert have == want


def test_inline_nixpkgs_and_flake_false() -> None:
    text = f'Input("src", "github:a/b", flake=False, nixpkgs=NixpkgsPin("old", "{OLD}"))\n'
    found = discover_source(text)
    assert found.inputs[0].flake is False
    assert [n.name for n in found.nixpkgs] == ["old"]
    assert found.to_json()["inputs"][0]["nixpkgs"] == {"name": "old", "commit": OLD}


def test_attribute_calls_are_read() -> None:
    text = f'import m\nold = m.NixpkgsPin("old", "{OLD}")\nm.Input("a", "github:a/b", nixpkgs=old)\nm.Input("b", "github:a/b", nixpkgs=m.OWN)\n'
    found = discover_source(text)
    assert [i.nixpkgs == "own" for i in found.inputs] == [False, True]


def test_keywords_in_any_order() -> None:
    found = discover_source(f'old = NixpkgsPin(commit="{OLD}", name="old")\nInput(url="github:a/b", name="a")\n')
    assert found.nixpkgs[0].name == "old"
    assert found.inputs[0].name == "a"


def test_a_nixpkgs_used_by_no_input_is_still_found() -> None:
    assert [n.name for n in discover_source(f'old = NixpkgsPin("old", "{OLD}")\n').nixpkgs] == ["old"]


def test_the_same_nixpkgs_twice_is_one_item() -> None:
    text = f'a = NixpkgsPin("old", "{OLD}")\nb = NixpkgsPin("old", "{OLD}")\n'
    assert len(discover_source(text).nixpkgs) == 1


def fails(text: str) -> str:
    with pytest.raises(DiscoveryError) as caught:
        discover_source(text)
    return str(caught.value)


def test_a_computed_argument_names_file_line_and_column() -> None:
    assert fails('x = 1\nname = "a"\nInput(name, "github:a/b")\n') == (
        "system.py:3:1: Input(...) takes plain text and True or False only"
    )
    assert fails('machine = Machine(inputs=[Input("a", "github:" + "a/b")])\n') == (
        "system.py:1:27: Input(...) takes plain text and True or False only"
    )


def test_a_computed_nixpkgs_argument_is_refused() -> None:
    assert fails('c = "x"\nold = NixpkgsPin("old", c)\n') == (
        "system.py:2:7: NixpkgsPin(...) takes plain text and True or False only"
    )


def test_a_starred_argument_is_refused() -> None:
    assert fails('args = ["a", "github:a/b"]\nInput(*args)\n') == (
        "system.py:2:1: Input(...) takes plain text and True or False only"
    )
    assert fails("Input(**kw)\n") == "system.py:1:1: Input(...) takes plain text and True or False only"


def test_a_computed_modules_list_is_refused() -> None:
    assert fails('Input("a", "github:a/b", modules=names)\n') == (
        "system.py:1:1: Input(...) takes plain text and True or False only"
    )


def test_a_short_commit_is_refused_with_the_position_of_the_argument() -> None:
    assert fails('x = 1\n\n\n\n\n\nold = NixpkgsPin("old", "d2339023")\n') == (
        "system.py:7:25: NixpkgsPin.commit must be a full commit of nixpkgs: 40 lower case hex digits "
        '(a branch name or a short commit does not pin), found "d2339023".'
    )


def test_a_reserved_nixpkgs_name_is_refused() -> None:
    assert fails(f'NixpkgsPin("own", "{OLD}")\n') == (
        "system.py:1:12: NixpkgsPin.name must be a new name: lower case letters, digits, and '-' "
        "('layer' and 'own' are taken), found \"own\"."
    )


def test_an_input_name_with_the_nixpkgs_prefix_is_refused() -> None:
    assert "Input.name must be a new name" in fails('Input("nixpkgs-old", "github:a/b")\n')


def test_a_bad_url_is_refused() -> None:
    assert "Input.url must be a flake reference" in fails('Input("a", "github a/b")\n')


def test_a_url_that_is_not_text_is_refused() -> None:
    assert fails('Input("a", 5)\n') == "system.py:1:12: Input.url must be text, found 5."


def test_flake_must_be_a_bool() -> None:
    assert (
        fails('Input("a", "github:a/b", flake="no")\n')
        == "system.py:1:32: Input.flake must be True or False, found 'no'."
    )


def test_a_bad_module_name_is_refused() -> None:
    assert "Input.modules must be the name of a module" in fails('Input("a", "github:a/b", modules=["a b"])\n')


def test_nixpkgs_equals_a_string_is_refused() -> None:
    assert fails(f'NixpkgsPin("old", "{OLD}")\nInput("a", "github:a/b", nixpkgs="old")\n') == (
        "system.py:2:34: nixpkgs= takes OWN, or a name that you set to NixpkgsPin(...) in this file"
    )


def test_nixpkgs_with_an_unknown_variable_is_refused() -> None:
    assert "nixpkgs= takes OWN" in fails('Input("a", "github:a/b", nixpkgs=older)\n')


def test_an_unknown_argument_is_named() -> None:
    assert fails('Input("a", "github:a/b", follow_nixpkgs=True)\n') == (
        "system.py:1:41: Input(...) has no argument `follow_nixpkgs`"
    )


def test_a_missing_argument_is_named() -> None:
    assert fails('Input("a")\n') == "system.py:1:1: Input(...) needs url, as plain text"


def test_an_input_twice_is_refused() -> None:
    assert fails('Input("a", "github:a/b")\nInput("a", "github:c/d")\n') == (
        "system.py:2:1: the input `a` is already set at line 1"
    )


def test_a_nixpkgs_twice_with_two_commits_is_refused() -> None:
    assert fails(f'NixpkgsPin("old", "{OLD}")\nNixpkgsPin("old", "{"0" * 40}")\n') == (
        "system.py:2: the nixpkgs `old` is already set to another commit at line 1"
    )


def test_the_ty_m_entry_stops_at_its_short_commit() -> None:
    with pytest.raises(DiscoveryError) as caught:
        read("ty-m")
    assert str(caught.value).startswith("system.py:12:25: NixpkgsPin.commit must be a full commit of nixpkgs")


def test_a_syntax_error_is_one_line() -> None:
    assert fails("Input(\n").startswith("system.py:1:")
