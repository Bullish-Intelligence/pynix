"""`NativeModule`: a native Nix module file of the workspace (009-D40)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, ClassVar

from pydantic import AfterValidator, BaseModel, ConfigDict
from pydantic_core import PydanticCustomError

__all__ = ["NativeModule"]


def _module_file(value: str) -> str:
    if value.startswith("/") or ".." in value.split("/") or not value.endswith(".nix"):
        raise PydanticCustomError(
            "native_file", 'must be a .nix file below the workspace folder, for example "fans.nix"'
        )
    return value


class NativeModule(BaseModel):
    """A native module file: `NativeModule("fans.nix")`. The path is relative to the workspace folder."""

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)
    _positional: ClassVar[tuple[str, ...]] = ("file",)
    file: Annotated[str, AfterValidator(_module_file)]
    """The path of the file, relative to the workspace folder, for example "fans.nix"."""

    if TYPE_CHECKING:

        def __init__(self, file: str, /) -> None:
            """A native module file.

            Args:
                file: The path of the file, relative to the workspace folder, for example "fans.nix".
            """
            ...

    else:

        def __init__(self, file: str) -> None:
            super().__init__(file=file)

        __init__.__pydantic_base_init__ = True
