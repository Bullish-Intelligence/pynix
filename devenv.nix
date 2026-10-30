# pynix — Python project configuration.
#
# Testee 0.8.1 runs `setup:*` tasks once before selected tasks. It then runs the
# five standard tasks below. `check:lint` also runs `uv lock --check` and `scripts/check_public.py`.
{ pkgs, ... }:

let
  # Files that no standard check reads: records, notes, and the files of the release job. A change to only these files
  # reuses a verdict (Testee). `README.md` is read by `uv sync` only (`pyproject.toml` names it), and `NOTICE` by
  # `scripts/check_public.py` only. Before you add a path, grep for it in the task commands and in the files that they run.
  notes = [ "CHANGELOG.md" "provenance/**" "AGENTS.md" "CLAUDE.md" "NOTICE" "README.md" "gates/README.md" ];
  # `check:lint` alone runs these files. No test imports them.
  lintScripts = [ "scripts/check_public.py" "scripts/public_allow.toml" ];
  # No task runs this script. The owner runs it to refresh `src/`.
  ownerScripts = [ "scripts/regenerate.sh" ];
  # `test:full` alone runs the gates and the generated-files check. The format, type, and unit-test tasks do not read them.
  fullOnly = [ "gates/**" "scripts/check_generated.sh" ];
  # `tests/test_release.py` runs `scripts/release.sh`, and `tests/test_compare_layers.py` loads `scripts/compare_layers.py`.
  # So only the tasks that run `pytest` read these two scripts.
  testScripts = [ "scripts/release.sh" "scripts/compare_layers.py" ];
  unread = notes ++ lintScripts ++ ownerScripts;
in
{
  # Python toolchain. The venv hosts the app and the dev group (pytest, ruff, ty).
  # Python 3.13: the interpreter of the Nix package and of the compilers that read this library.
  languages.python = {
    enable = true;
    package = pkgs.python313;
    venv.enable = true;
    uv.enable = true;
  };

  # Every task declares `input.testee`, so Testee can reuse a verdict when a commit changes none of its inputs.
  # After an edit of this table, run `testee doctor`: it must show reuse on for every task.
  tasks = {
    # Testee runs setup once before selected checks. Clone tasks use it too.
    # `uv sync` reads the lock, the project file, the readme (`pyproject.toml` names it), and the `.gitignore` of the build.
    "setup:sync".input.testee.reads = [ "uv.lock" "pyproject.toml" "README.md" ".gitignore" ];
    "setup:sync".exec = ''
      uv sync --locked
    '';

    # `check_public.py` reads every tracked file, so this task ignores no tracked file. `.devenv/**` is state, not source.
    "check:lint".input.testee.ignores = [ ".devenv/**" ];
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

    "check:format".input.testee.ignores = unread ++ fullOnly ++ testScripts;
    "check:format".exec = ''
      set -o pipefail
      uv run --no-sync ruff format --check src tests
    '';

    "check:types".input.testee.ignores = unread ++ fullOnly ++ testScripts;
    "check:types".exec = ''
      set -o pipefail
      uv run --no-sync ty check src tests
    '';

    # The unit tests only: no option walk and no gate (seconds).
    "test:quick".input.testee.ignores = unread ++ fullOnly;
    "test:quick".exec = ''
      set -o pipefail
      uv run --no-sync pytest tests
    '';

    # The tests, then the check that `src/` equals the output of the generators (the option walk), then the 11 gates of
    # the generated libraries with the canaries (`gates/README.md`).
    # The full task takes about 6 minutes (347 s and 370 s measured, 2026-10-30: the option walk, the libraries, the
    # canaries). The limit is about twice that, so a hang or a slip fails soon. Run `testee verify --profile quick`
    # first: it takes seconds.
    "test:full".input.testee = {
      timeout_s = 720;
      ignores = unread;
    };
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
    # They run the standard tasks, so they read what those tasks read: they ignore only the folder of the devenv state.
    # Never name a task in `after` that does not exist: devenv then fails every task and the shell.
    "base:check" = {
      after = [ "setup:sync" ];
      input.testee.ignores = [ ".devenv/**" ];
      exec = ''
        set -e
        devenv --no-tui tasks run --show-output check:lint
        devenv --no-tui tasks run --show-output check:format
        devenv --no-tui tasks run --show-output check:types
      '';
    };
    "base:test" = {
      after = [ "setup:sync" ];
      input.testee.ignores = [ ".devenv/**" ];
      exec = ''
        set -e
        devenv --no-tui tasks run --show-output test:full
      '';
    };
  };
}