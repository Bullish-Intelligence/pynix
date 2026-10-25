"""The package-name stub `pynix_pkgs` (009 SV4, 009-D31)."""

import pytest

from pynix_pkgs import Pkg, Prog, UnknownPackage, pkgs


def test_known_package_with_a_main_program() -> None:
    assert isinstance(pkgs.ripgrep, Prog)
    assert pkgs.ripgrep.attr == "ripgrep"


def test_dashed_name() -> None:
    assert pkgs["ripgrep-all"].attr == "ripgrep-all"
    assert isinstance(pkgs.zlib, Pkg)


def test_unknown_package_says_did_you_mean() -> None:
    typo = "ripgrp"  # ty flags `pkgs.ripgrp` in a file; the runtime check is the second line of defence
    with pytest.raises(UnknownPackage) as caught:
        getattr(pkgs, typo)
    assert str(caught.value) == "The package list has no package `ripgrp`. Did you mean `ripgrep`?"
