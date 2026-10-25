"""Shared fixtures for the tests."""

import pytest

from pynix_native import reset_nixpkgs


@pytest.fixture(autouse=True)
def _fresh_nixpkgs_registry():
    """`NixpkgsPin(...)` keeps a registry for the process. Each test starts with an empty one."""
    reset_nixpkgs()
    yield
    reset_nixpkgs()
