"""Shared set-up for the engine tests: a Basix-like layer, a minix-like layer, and a workspace on disk.

The layers here are test values. They show what a command passes in (the sudo words, the switch command, the
health query). The engine itself names neither layer.
"""

from dataclasses import dataclass, field, replace
from pathlib import Path

from pynix_engine import Command, Engine, Layer, Plan, Result, Session
from pynix_engine.testing import FakeClock, FakeGit, FakeRunner

TOP_NEW = "/nix/store/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-nixos-system-new"
TOP_OLD = "/nix/store/bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb-nixos-system-old"
COMPILER = "/nix/store/cccccccccccccccccccccccccccccccc-basix-compiler"
SUDO = "/run/wrappers/bin/sudo"
HEALTH = ("systemctl", "list-units", "--all", "--no-legend", "--plain", "--no-pager")
HEALTH_USER = ("systemctl", "--user", "list-units", "--all", "--no-legend", "--plain", "--no-pager")
GOOD_UNITS = "sshd.service loaded active running OpenSSH\n"
BAD_UNITS = GOOD_UNITS + "web.service loaded failed failed Web\n"


@dataclass
class World:
    """The fake machine behind a layer: the running system, and the boot default."""

    running: str = TOP_OLD
    boot_default: str = TOP_OLD
    plan_calls: list[str] = field(default_factory=list)


def basix_plan(world: World, built: str) -> Plan:
    """The Basix plan of L123: reset, `test`, the check, then the profile and `boot`."""
    world.plan_calls.append(built)
    switch = f"{built}/bin/switch-to-configuration"
    old = f"{world.running}/bin/switch-to-configuration"
    return Plan(
        unchanged=built == world.running and built == world.boot_default,
        reset=[[SUDO, "systemctl", "reset-failed"]],
        activate=[[SUDO, switch, "test"]],
        finish=[[SUDO, "nix-env", "-p", "/nix/var/nix/profiles/system", "--set", built], [SUDO, switch, "boot"]],
        restore=lambda: [[SUDO, old, "test"]],
        notice="Basix needs your password to change the machine",
    )


def minix_plan(world: World, built: str) -> Plan:
    """The minix plan: no sudo, an activation, and the last good activation on a failure."""
    old: list[Command] = [[f"{world.running}/activate"]] if world.running else []
    return Plan(
        unchanged=built == world.running,
        reset=[["systemctl", "--user", "reset-failed"]],
        activate=[[f"{built}/activate"]],
        restore=lambda: old,
    )


def write_json(session: Session) -> None:
    """A stand-in for the compile callable of a layer: write the JSON file."""
    (session.ws / session.layer.json_file).write_text("{}\n")


def basix_layer(world: World, **changes: object) -> Layer:
    layer = Layer(
        name="basix",
        entry="system.py",
        json_file="system.json",
        folder="~/basix",
        noun="system",
        compiler_bin="basix-compile",
        build_attr=".#nixosConfigurations.basix.config.system.build.toplevel",
        health_command=HEALTH,
        unit_suffixes=(".service", ".mount", ".socket", ".timer", ".path"),
        plan=lambda session, built: basix_plan(world, built),
        on_fail_env="BASIX_ON_FAIL",
        compile=write_json,
    )
    return replace(layer, **changes)


def minix_layer(world: World, **changes: object) -> Layer:
    layer = Layer(
        name="minix",
        entry="home.py",
        json_file="home.json",
        folder="~/minix",
        noun="home",
        compiler_bin="minix-compile",
        build_attr=".#homeConfigurations.ada.activationPackage",
        health_command=HEALTH_USER,
        unit_suffixes=(".service", ".socket", ".timer", ".path"),
        plan=lambda session, built: minix_plan(world, built),
        on_fail_env="MINIX_ON_FAIL",
        compile=write_json,
        fallback_identity=("minix", "minix@localhost"),
    )
    return replace(layer, **changes)


@dataclass
class Setup:
    ws: Path
    runner: FakeRunner
    git: FakeGit
    clock: FakeClock
    world: World
    lines: list[str]

    def engine(self, layer: Layer | None = None, env: dict[str, str] | None = None, verbose: bool = False) -> Engine:
        return Engine(
            layer or basix_layer(self.world),
            self.ws,
            runner=self.runner,
            clock=self.clock,
            say=self.lines.append,
            env=env or {},
            verbose=verbose,
        )

    def log(self, name: str = "basix") -> str:
        return (self.ws / ".git" / name / "last.log").read_text()

    def trace(self) -> list[str]:
        """The calls that matter, in order, as short labels. Repeated health polls count once."""
        labels: list[str] = []
        for call in self.runner.calls:
            label = _label(call)
            if label and (label != "health" or not labels or labels[-1] != "health"):
                labels.append(label)
        return labels


def _label(call: tuple[str, ...]) -> str | None:
    words = [word for word in call if word != SUDO]
    if call[:2] == ("nix", "build"):
        return "compiler" if call[-1].endswith("#compiler") else "build"
    if call[:3] == ("nix", "flake", "lock"):
        return "lock"
    if call[:1] == ("git",) and "commit" in call:
        return "commit"
    if call[:2] == ("git", "restore"):
        return "restore"
    if call[-5:] == HEALTH[-5:]:
        return "health"
    if "reset-failed" in words:
        return "reset"
    if words[:1] == ["nix-env"]:
        return "profile"
    if words and words[0].endswith(("switch-to-configuration", "/activate")):
        return words[-1] if words[0].endswith("switch-to-configuration") else "activate"
    return None


def make_setup(tmp_path: Path) -> Setup:
    (tmp_path / ".git").mkdir()
    runner = FakeRunner()
    git = FakeGit(runner)
    world = World()
    # The default build gives the new system. The default health query gives healthy units.
    runner.on(("nix", "build"), Result(0, TOP_NEW + "\n"))
    runner.on(HEALTH, Result(0, GOOD_UNITS))
    runner.on(HEALTH_USER, Result(0, GOOD_UNITS))
    return Setup(tmp_path, runner, git, FakeClock(), world, [])
