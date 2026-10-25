"""The runtime and the generated libraries: the proven 008 S10 behaviour, from the installed package."""

import pytest
from pydantic import ValidationError

from nixdantic import Package, Text, fragment
from pynix_hm import _generation as hm_generation
from pynix_os import _generation as os_generation
from pynix_os.services.openssh import Openssh


def test_error_names_the_option_path() -> None:
    with pytest.raises(ValidationError) as caught:
        Openssh(ports=[70000])
    (error,) = caught.value.errors()
    assert error["ctx"]["option"] == "services.openssh.ports"
    assert error["msg"] == "must be 16 bit unsigned integer; between 0 and 65535 (both inclusive)"


def test_fragment_of_a_root_class() -> None:
    frag = fragment(Openssh(enable=True, ports=[2222]))
    assert frag["path"] == ["services", "openssh"]
    assert frag["value"] == {"enable": True, "ports": [2222]}


def test_text_keeps_references() -> None:
    value = Text(Package(attr="hello"), "/bin/hello")
    assert value.parts[1] == "/bin/hello"


def test_libraries_pair_with_one_nixpkgs() -> None:
    # Owner decision L126: Home Manager is generated against the nixpkgs of pynix_os.
    assert hm_generation.SOURCE["nixpkgs"] == os_generation.SOURCE["nixpkgs"]
