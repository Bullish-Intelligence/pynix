"""Test fixture for the `s7-lsp` check: a curated class with the hand-written `__init__` block.

The class `Machine` keeps the shape that the 008 S10 probe used for the Basix `Machine`: the fields `name` and `user`,
each with an attribute docstring, and an `__init__` under `TYPE_CHECKING` that repeats the docstrings in `Args`. It holds
no Basix code. The check proves that ty shows the field description in hover, completion, and signature help for a
curated class of this shape.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import ConfigDict, StringConstraints

from nixdantic import Expect, Plain

Name = Annotated[
    str,
    StringConstraints(pattern=r"^[a-z][a-z0-9-]*$"),
    Expect("a machine name (a lower case letter, then lower case letters, digits, or '-')"),
]
Account = Annotated[
    str,
    StringConstraints(pattern=r"^[a-z][a-z0-9-]{0,31}$"),
    Expect("an account name (a lower case letter, then up to 31 lower case letters, digits, or '-')"),
]


class Machine(Plain):
    """One machine."""

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True, use_attribute_docstrings=True)

    name: Name
    """The machine name. It is the host name, and other computers reach the machine as NAME.local."""
    user: Account
    """Your account name: lower-case letters, digits, and '-', at most 32 characters."""

    if TYPE_CHECKING:  # help while you type `Machine(...)`; the editor reads it, Python never runs it

        def __init__(self, *, name: Name, user: Account) -> None:
            """One machine.

            Args:
                name: The machine name. It is the host name, and other computers reach the machine as NAME.local.
                user: Your account name: lower-case letters, digits, and '-', at most 32 characters.
            """
            ...
