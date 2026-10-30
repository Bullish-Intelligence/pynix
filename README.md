# pynix

pynix turns typed Python values into Nix definitions. A release is a tag. Basix and minix each pin one tag
and read `"${input}/src"` with `flake = false` (or use `lib.src`).

`src/` holds the release tree:

| Package | Holds | Written by |
| --- | --- | --- |
| `nixdantic` | the runtime: the base classes, the references (`Package`, `Text`, `ConfigRef`, `Native`), the error text | hand |
| `decoder.nix` | the Nix side of the references | hand |
| `pynix` | the generators (`generate.py`, `gen_pkgs.py`) | hand |
| `pynix_os`, `pynix_hm`, `pynix_flake_parts` | one class per option set of NixOS, Home Manager, flake-parts | `.#libraries` |
| `pynix_pkgs` | `pkgs.NAME` and the package-name list (`names.json`) of the pinned nixpkgs | `.#packageNames` (`pkgs.pyi`, `names.json`) |

A `Native(file, attr)` reference reads a Nix file of the workspace. The file can be a function of the module
arguments (`{ pkgs, inputs, ... }:`). When `attr` is not empty, the file must give an attribute set, and the decoder
calls a function with the module arguments that it names. When `attr` is empty, the reference takes the whole value
(an overlay `final: prev: { ... }`, for example). The decoder then calls a function only when it names an argument
(`{ pkgs, ... }:`) and returns any other value as it is. Nix cannot tell `{ ... }:` from `final: prev:`, so the
decoder returns a whole-value file `{ ... }:` as a function and does not call it.

## Python code of an input

`Input("tools", "github:me/tools", python="src")` makes the Python code of an input importable in the entry file
(`system.py` or `home.py`). The input can be a flake or not (`flake=False`). `python` names a folder of the input.
Use `"."` for the root of the input. The folder must not start with `/` and must not contain `..`.

Pynix imports two kinds of entry from that folder:

- a package: a folder with an `__init__.py`;
- a module: a file `NAME.py`.

NAME must be a Python identifier and must not start with `_`. Pynix ignores all other files, and a folder with no
`__init__.py` (a folder of tests, for example). If `src` holds `tools/__init__.py`, the entry writes
`from tools import thing`.

The compile stops, with one line that names the input and the name, when:

- two inputs give the same name, or one input gives it twice (`x/` and `x.py`);
- a name is reserved: `pynix`, any `pynix_*`, `nixdantic`, `pydantic`, `pydantic_core`, `annotated_types`,
  `typing_extensions`, `typing_inspection`, `minix`, `minix_config`, `basix`, `basix_config`;
- a name is in the standard library of the build Python (`sys.stdlib_module_names`);
- the folder does not exist in the input;
- the folder holds no package and no module.

The code can import the standard library, `pydantic`, `nixdantic`, `pynix_pkgs`, `pynix_native`, and the libraries
of its layer (minix: `minix_config`, `pynix_hm`; Basix: `basix_config`, `pynix_os`). Other third-party packages are
not available. `flake.lock` pins the code. It changes only after an update of the input.

`nix/input-packages.nix` does the work. Its argument `pythonDirs = { NAME = "src"; }` links each entry into the
output next to `pynix_NAME`. An input with `flake=False` and `python` also gets a `pynix_NAME` folder. That folder
holds the record that the pair check compares with `flake.lock`. An input with `flake=False` and no `python` gets
no package.

The option walk (`nix/evaluate.nix`) reads the pinned inputs of `flake.nix`: nixpkgs, Home Manager (it follows
nixpkgs), and flake-parts. `scripts/check_generated.sh` (in `test:full`) fails when `src/` differs from the
output of the generators. `scripts/regenerate.sh` writes that output into `src/`.

`scripts/compare_layers.py LOCK_A LOCK_B [--names A,B] [--json]` compares the `nixpkgs` and `pynix` pins of two
`flake.lock` files (or folders that hold one). It prints one line per item and a `warning:` line for each
difference. It blocks nothing: it exits 0 with or without differences, and 2 on wrong use or an unreadable lock.

A [devenv](https://devenv.sh) **Python** project. This repository defines five
Testee tasks in `devenv.nix`.
The machine supplies the `testee` command. This project pins no Testee input.

## Getting started

```bash
devenv shell          # enter the project environment
uv sync --all-extras  # app deps + the dev group (pytest/ruff/ty)
```

The first sync creates `uv.lock`. After you commit it, Testee runs `setup:sync`
once before selected tasks. The `base:check` and `base:test` tasks wait for
`setup:sync`, then run their checks in sequence for cloners.

## Verify

The five tasks in `devenv.nix` are `check:lint`, `check:format`, `check:types`, `test:quick` and
`test:full`. `check:lint` also runs `uv lock --check`, so a stale `uv.lock` fails the gate.

Run these commands from the repository root. Testee checks the commit in its
own workspace, so untracked and ignored files cannot change a verdict.

```bash
testee doctor                    # check the runner and the tasks
testee verify                    # the four required tasks: check:lint, check:format, check:types, test:full
testee verify --profile quick    # check:lint, check:format and test:quick
testee status                    # the verdict for the current commit
```

Exit codes: `0` green, `1` a check failed, `2` no verdict (never verified, not set up, incomplete, or a
refusal with a reason code). A placeholder gives no verdict until you replace it. Keep `uv.lock` and
`devenv.lock` in Git. Testee has no fix command: run `ruff format src tests` in the devenv shell, then
rerun `testee verify`.

## Layout

```
src/            # the release tree (see the table above)
nix/            # the option walk, the extractor, the library build, the package-name walk
scripts/        # check_generated.sh, regenerate.sh
tests/          # pytest tests (the `test:full` task)
devenv.nix      # shell, toolchain, and the Testee tasks
pyproject.toml  # metadata, pins (pydantic, ruff, ty equal to the pinned nixpkgs), ruff and pytest config
```

## Project configuration

defines the Testee tasks.

For Gitman, Devman, and CopyRoom workflows, use the corresponding
skills linked under `.agents/skills/`.

## Staying current with the template

This project is managed by CopyRoom. Use the central CopyRoom skill linked at
`.agents/skills/copyroom/SKILL.md` for the update workflow.

## Contributing

Pull requests are welcome, but the author does not promise a review.

## Author

Bullish-Intelligence <242310653+Bullish-Intelligence@users.noreply.github.com>