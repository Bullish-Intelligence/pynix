# pynix — Python project configuration.
#
# Testee 0.8.1 runs `setup:*` tasks once before selected tasks. It then runs the
# five standard tasks below. `check:lint` also runs `uv lock --check` and `scripts/check_public.py`.
{ pkgs, ... }:

{
  # Python toolchain. The venv hosts the app and the dev group (pytest, ruff, ty).
  # Python 3.13: the interpreter of the Nix package and of the compilers that read this library.
  languages.python = {
    enable = true;
    package = pkgs.python313;
    venv.enable = true;
    uv.enable = true;
  };

  tasks = {
    # Testee runs setup once before selected checks. Clone tasks use it too.
    "setup:sync".exec = ''
      uv sync --locked
    '';

    "check:lint".exec = ''
      set -o pipefail
      # A stale `uv.lock` fails here, before the Nix package build does.
      uv lock --check
      # No tracked file names an owner fact; NOTICE holds the upstream MIT notices.
      python3 -I scripts/check_public.py . --require-notice
      python3 -I scripts/check_public.py --selftest
      out="''${TESTEE_RUN_DIR:-.devenv/state}"
      mkdir -p "$out"
      uv run --no-sync ruff check src tests --output-format json | tee "$out/check:lint.ruff.json"
    '';

    "check:format".exec = ''
      set -o pipefail
      uv run --no-sync ruff format --check src tests
    '';

    "check:types".exec = ''
      set -o pipefail
      uv run --no-sync ty check src tests
    '';

    # The unit tests only: no option walk and no gate (seconds).
    "test:quick".exec = ''
      set -o pipefail
      uv run --no-sync pytest tests
    '';

    # The tests, then the check that `src/` equals the output of the generators (the option walk), then the 11 gates of
    # the generated libraries with the canaries (`gates/README.md`).
    # The full task takes about 5 minutes (the option walk, the libraries, the canaries). The limit is about twice
    # that, so a hang or a slip fails soon. Run `testee verify --profile quick` first: it takes seconds.
    "test:full".input.testee.timeout_s = 600;
    "test:full".exec = ''
      set -o pipefail
      out="''${TESTEE_RUN_DIR:-.devenv/state}"
      mkdir -p "$out"
      uv run --no-sync pytest tests --junitxml="$out/test:full.junit.xml"
      # One build of the three outputs, so Nix evaluates the option walk once for both checks below.
      # Each output is found by its content, not by the order of the lines.
      for path in $(nix build --no-link --print-out-paths \
        "path:$PWD#libraries" "path:$PWD#packageNames" "path:$PWD#manifests"); do
        if [ -d "$path/pynix_os" ]; then export PYNIX_LIBRARIES=$path; fi
        if [ -f "$path/pkgs.pyi" ]; then export PYNIX_PACKAGE_NAMES=$path; fi
        if [ -f "$path/nixos.json" ]; then export MANIFEST_DIR=$path; fi
      done
      bash scripts/check_generated.sh
      bash gates/run_gates.sh src "$out/gates"
    '';

    # Clone entrypoints. Setup finishes before they invoke the standard tasks.
    # Never name a task in `after` that does not exist: devenv then fails every task and the shell.
    "base:check" = {
      after = [ "setup:sync" ];
      exec = ''
        set -e
        devenv --no-tui tasks run --show-output check:lint
        devenv --no-tui tasks run --show-output check:format
        devenv --no-tui tasks run --show-output check:types
      '';
    };
    "base:test" = {
      after = [ "setup:sync" ];
      exec = ''
        set -e
        devenv --no-tui tasks run --show-output test:full
      '';
    };
  };
}