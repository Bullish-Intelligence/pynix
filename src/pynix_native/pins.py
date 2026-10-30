"""Compare the pins of the Python inputs of two workspaces (021-D3). A warning only: nothing here stops a command.

Two layers can pin the same input (`Input(..., python="src")`) at different revisions. A layer publishes its pins as a
manifest file. The other layer reads that file and warns when the pins differ. This module is layer-neutral: the layer
chooses the file, the paths, and the words.

The manifest is JSON from `nix/pins.nix` (`pynix.lib.pythonPins`):

    {"version": 1, "pins": [{"name", "url", "flake", "python", "rev", "narHash"}, ...]}

`rev` is null for an input that has none (a `path:` input). The locked `rev` and `narHash` come from `flake.lock`, not
from the text of the url.

Rules (021-D8):

- Two pins are the same input when `normalize_url` gives the same text. The name is a local alias.
- Two pins have the same version when the `rev` is equal, or the `narHash` when there is no `rev`.
- A missing, empty, or damaged manifest gives no warning. A pin with no `rev` and no `narHash` gives none either.
- Only inputs with `python=` are in a manifest.

Use:

    here = pins.from_workspace(ws, "home.json")      # `update`: no build, so read the own lock and the generated JSON
    here = pins.load(built / "path/of/the/file")     # `apply`: read the file of the new build
    other = pins.load(path_of_the_other_file)
    lines = pins.lines(here, other, here="your home", there="the system")
"""

from __future__ import annotations

import json
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit

from .lock import LockError, follow, read_lock

__all__ = [
    "DEFAULT_TEXT",
    "VERSION",
    "Manifest",
    "Mismatch",
    "Pin",
    "compare",
    "format_mismatch",
    "from_data",
    "from_workspace",
    "lines",
    "load",
    "normalize_url",
    "parse",
    "short",
]

VERSION = 1
SHORT = 7
DEFAULT_TEXT = (
    "warning: the input {input} is at {local_rev} in {here}, but {there} has {other_rev}. "
    "The Python code of the two pins can differ."
)

_HOSTED = {"github": "github.com", "gitlab": "gitlab.com", "sourcehut": "git.sr.ht"}
_HOSTED_URL = re.compile(r"^(github|gitlab|sourcehut):([^/?]+)/([^/?]+)(?:/[^?]*)?(\?.*)?$")
_SCP = re.compile(r"^(?:[^@/\s]+@)?([^:/\s]+):(?!//)(.+)$")  # git@host:owner/repo.git
_SECRET = re.compile(r"^([A-Za-z+.-]+://)[^/@]*@")


@dataclass(frozen=True)
class Pin:
    """One `Input(..., python=...)` as a manifest row."""

    name: str
    url: str
    rev: str | None
    nar_hash: str | None
    flake: bool = True
    python: str | None = None

    @property
    def key(self) -> str:
        """The identity of the input: the normalized url."""
        return normalize_url(self.url)

    @property
    def version(self) -> str | None:
        """The locked `rev`, else the `narHash` (a `path:` input has no `rev`)."""
        return self.rev or self.nar_hash


@dataclass(frozen=True)
class Manifest:
    pins: tuple[Pin, ...]


@dataclass(frozen=True)
class Mismatch:
    """One input that both sides pin at a different version. `local_rev` and `other_rev` are the full `rev` or `narHash`."""

    local_name: str
    other_name: str
    url: str  # the url of the local pin, without credentials
    local_rev: str
    other_rev: str


def short(version: str) -> str:
    """A short form of a `rev` or a `narHash` for a plain line."""
    return version.removeprefix("sha256-")[:SHORT]


def normalize_url(url: str) -> str:
    """The identity of the repository that a flake url names. The ref and the revision are not part of it.

    `git+https://github.com/Owner/Repo.git?ref=main&rev=abc`, `github:owner/repo/abc`, `git@github.com:owner/repo`, and
    `git+ssh://git@github.com/owner/repo` all give `github.com/owner/repo`. A `dir=` stays: it names another flake.
    """
    text = url.strip()
    for prefix in ("git+", "tarball+", "file+"):
        if text.startswith(prefix) and "://" in text:
            text = text[len(prefix) :]
    hosted = _HOSTED_URL.match(text)
    if hosted:
        kind, owner, repo, query = hosted.groups()
        return _join(_HOSTED[kind], f"{owner}/{repo}", query)
    if text.startswith("path:"):
        return "path:" + (text[5:].partition("?")[0].rstrip("/") or "/")
    scp = _SCP.match(text)
    if scp and "://" not in text:
        return _join(scp.group(1), scp.group(2), None)
    parts = urlsplit(text)
    if parts.scheme == "file":
        return "file://" + _join("", parts.path, parts.query)
    if parts.hostname:
        host = parts.hostname + (f":{parts.port}" if parts.port else "")
        return _join(host, parts.path, parts.query)
    return text.rstrip("/")


def _join(host: str, path: str, query: str | None) -> str:
    host = host.lower()
    path = path.strip("/").removesuffix(".git") if host else path.rstrip("/")
    if host.split(":")[0] in _HOSTED.values():
        path = path.lower()  # these hosts ignore case in an owner or a repository
    key = f"{host}/{path}" if host else path
    directory = parse_qs((query or "").lstrip("?")).get("dir")
    return f"{key}#{directory[0]}" if directory else key


def scrub(url: str) -> str:
    """Remove a user name and a password from a url, as `pins.nix` does."""
    return _SECRET.sub(r"\1", url)


# --- the manifest --------------------------------------------------------------------------------------------------
def _text(value: object) -> str | None:
    return value if isinstance(value, str) and value else None


def _row(row: object) -> Pin | None:
    if not isinstance(row, dict):
        return None
    name, url = _text(row.get("name")), _text(row.get("url"))
    if name is None or url is None:
        return None
    return Pin(
        name,
        url,
        _text(row.get("rev")),
        _text(row.get("narHash")),
        row.get("flake") is not False,
        _text(row.get("python")),
    )


def parse(text: str) -> Manifest | None:
    """The manifest in `text`, or None for a text that is not a manifest of this version. A damaged row is dropped."""
    try:
        data = json.loads(text)
        if not isinstance(data, dict) or data.get("version") != VERSION or not isinstance(data.get("pins"), list):
            return None
        return Manifest(tuple(pin for pin in map(_row, data["pins"]) if pin is not None))
    except (ValueError, RecursionError):
        return None


def load(path: Path | str) -> Manifest | None:
    """The manifest in a file. A file that is missing, empty, unreadable, or damaged gives None. It never raises."""
    try:
        return parse(Path(path).read_text())
    except (OSError, ValueError):  # ValueError: not UTF-8
        return None


def from_data(compiled: Mapping[str, Any], lock: Mapping[str, Any]) -> Manifest:
    """The manifest that `pins.nix` writes, made from the generated JSON and the lock of the own workspace.

    `compiled` is the JSON of the entry (`inputs` holds `name`, `url`, `flake`, and `python` when set). `lock` is `flake.lock`.
    """
    nodes = lock.get("nodes", {})
    refs = nodes.get(lock.get("root", "root"), {}).get("inputs", {})
    out: list[Pin] = []
    for item in sorted(compiled.get("inputs", []), key=lambda i: i["name"]):
        if not _text(item.get("python")):
            continue
        locked: Mapping[str, Any] = {}
        if item["name"] in refs:
            try:
                locked = nodes[follow(lock, refs[item["name"]])].get("locked", {})
            except (KeyError, LockError):
                locked = {}
        out.append(
            Pin(
                item["name"],
                scrub(item["url"]),
                _text(locked.get("rev")),
                _text(locked.get("narHash")),
                item.get("flake", True) is not False,
                item["python"],
            )
        )
    return Manifest(tuple(out))


def from_workspace(ws: Path, json_file: str) -> Manifest | None:
    """The pins of the own workspace: the generated JSON `ws/json_file` and `ws/flake.lock`. Any failure gives None.

    A command without a build (`update`) uses this. The result equals the manifest of a build.
    """
    try:
        compiled = json.loads((ws / json_file).read_text())
        return from_data(compiled, read_lock(ws / "flake.lock"))
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return None


# --- the compare ---------------------------------------------------------------------------------------------------
def compare(local: Manifest | None, other: Manifest | None) -> list[Mismatch]:
    """The pins of `local` that `other` pins at another version, in the order of `local`.

    A side that is None gives nothing. An input that only one side has gives nothing. If `other` pins the same input
    twice and one pin equals ours, nothing differs.
    """
    if local is None or other is None:
        return []
    peers: dict[str, list[Pin]] = {}
    for pin in other.pins:
        if pin.version is not None:
            peers.setdefault(pin.key, []).append(pin)
    found: list[Mismatch] = []
    for pin in local.pins:
        theirs = peers.get(pin.key, [])
        if pin.version is None or not theirs or any(p.version == pin.version for p in theirs):
            continue
        found.append(Mismatch(pin.name, theirs[0].name, scrub(pin.url), pin.version, theirs[0].version or ""))
    return found


def format_mismatch(mismatch: Mismatch, *, here: str, there: str, text: str = DEFAULT_TEXT) -> str:
    """One plain line. `here` and `there` are the layer's words for the two sides, for example "your home" and "the system".

    `text` is a `str.format` template. Its fields: `input`, `local_name`, `other_name`, `url`, `local_rev`, `other_rev`,
    `here`, and `there`. `local_rev` and `other_rev` are short. `input` is the name in backticks; when the other side
    uses another name, it adds that name. The result has no line break.
    """
    name = f"`{mismatch.local_name}`"
    if mismatch.other_name != mismatch.local_name:
        name += f" (`{mismatch.other_name}` in {there})"
    line = text.format(
        input=name,
        local_name=mismatch.local_name,
        other_name=mismatch.other_name,
        url=mismatch.url,
        local_rev=short(mismatch.local_rev),
        other_rev=short(mismatch.other_rev),
        here=here,
        there=there,
    )
    return " ".join(line.split())


def lines(
    local: Manifest | None, other: Manifest | None, *, here: str, there: str, text: str = DEFAULT_TEXT
) -> Sequence[str]:
    """The warning lines for two manifests: one for each mismatch. It never raises; a failure gives no line."""
    try:
        return [format_mismatch(m, here=here, there=there, text=text) for m in compare(local, other)]
    except Exception:  # noqa: BLE001 - a warning must never break a command
        return []
