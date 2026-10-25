# AGENTS.md — project instructions

This repository is a Python package. `AGENTS.md` holds its contributor
instructions, and `CLAUDE.md` is a symlink to this file.

## Checks

- Run Python commands in the `devenv` shell.
- `devenv.nix` defines five tasks: `check:lint`, `check:format`, `check:types`, `test:quick` and `test:full`.
  Each task starts as a placeholder. A placeholder prints `TESTEE_NOT_SET_UP <task>` and exits 78.
  Replace it with a real command, or with `echo "n/a: <reason>"; exit 0`.
- `testee doctor` lists the tasks that are not set up.
- `testee verify` runs the four required tasks: `check:lint`, `check:format`, `check:types` and `test:full`.
- `testee verify --profile quick` runs `check:lint`, `check:format` and `test:quick`.
- `setup:sync` runs `uv sync --locked` once before selected checks. Do not list it in a standard task's `after` attribute.
- The `base:check` and `base:test` tasks wait for setup, then run their checks in sequence for cloners.
- `testee status` gives the verdict for the commit. Integrate only on GREEN.
- If formatting fails, run `ruff format src tests`, then rerun the checks.
- Keep `uv.lock` and `devenv.lock` in Git. The machine supplies the `testee` command.
  This project pins no Testee input and sets no `testee.*` option.

## Project configuration

- `pyproject.toml` declares the package and its development dependencies.
- `devenv.nix` declares the shell and the Testee tasks.
- For tool workflows, use the skills linked under `.agents/skills/`.
