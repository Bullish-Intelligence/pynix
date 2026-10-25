# gates: 11 checks of the generated libraries

The harness is a copy of the 008 S10 harness (`evidence/S10/gates/`), moved into `pynix`. The checks, the pass rules,
and the canaries are the S10 ones. Only the fixed paths changed (see "Parameters"). `testee verify` runs it in `test:full`.
`scripts/release.sh` runs it with the canaries before a release.

## Run

```sh
devenv shell -- bash gates/run_gates.sh [--no-canaries] LIBRARY OUTDIR [CHECK...]
devenv shell -- bash gates/run_gates.sh src /tmp/gates-out   # all 11 checks on src/
```

- Run it from the repository root, through the devenv (`uv` and the pinned tools).
- LIBRARY: a directory with `nixdantic/`, `decoder.nix`, `pynix_os`, `pynix_hm`, `pynix_flake_parts`, and their
  `-gaps.json` and `-fields.json` files. In the repository it is `src/`.
- OUTDIR: receives `summary.txt`, `summary.json` (one line per check: name, PASS or FAIL, key numbers, seconds),
  `checks/NAME.json`, `results/`, `logs/` (raw logs), and `scratch/`. Keep OUTDIR out of the repository: write to
  `$TESTEE_RUN_DIR` or `.devenv/state` (`test:full` does).
- Exit 0 only when every check that ran passes. A failure with a known cause prints `FAIL (expected: ...)`. It still fails.
- CHECK names pick a subset. `--no-canaries` skips `s5-canaries`.
- Time: about 5 minutes with the canaries (the canaries take about 2 minutes), plus the build of the manifests when
  the Nix store does not hold them yet.

## Checks

| Check | What it runs | Proves | Pass when |
| --- | --- | --- | --- |
| `s5-ty-check` | `ty check` on each package (`gate_ty_check.py`) | ty accepts every generated module | 0 diagnostics |
| `s5-ty-probe` | `gate_ty_probe.py`: reveal the type of every field | an editor sees an exact type for every option; the `Native` escapes are the counted ones | every field exact; the `Native` count equals the gap file |
| `s5-runtime` | `gate_runtime.py`: import, rebuild, walk every annotation | every class imports and every annotation resolves at run time | 0 failures; the `Native` count equals the gap file |
| `s9-values` | `check_values.py` on the manifests, then `values_gate.py` | every default and example value that Nix accepts, the model accepts too | every refusal is a counted `Native` gap or an unproven example |
| `s9-patterns` | `patterns.py`: Nix `builtins.match` against `matching` | the Python check of each `strMatching` pattern is not stricter than Nix | 0 false rejections |
| `s9-limits` | `bounds.py`: integer limits (NixOS, Home Manager) | the integer ranges equal the ranges of the Nix types | 0 false rejections |
| `s9-cases` | `cases.py` + `cases.nix`: 165 hand values, Nix proved by `lib.evalModules` | the generator maps each hand-made Nix type to a model that accepts what Nix accepts | 0 false rejections in JSON mode; in Python mode only the two `tuple` rows |
| `s8-nix-unit` | `unit/tests.nix` (23 tests) and a planted-bug decoder as control | the decoder turns references and text into the right Nix values | 23 of 23 pass; the planted decoder fails some |
| `s8-runtime` | `runtime_checks.py`: `Text` and `NixValue` at run time | the runtime types behave as specified | all checks pass |
| `s7-lsp` | `s7_probe.py`: the ty language server: hover, completion, signature help | the description of a field shows in an editor, for a generated class and for a curated class | the description of two keywords of `Machine` and of `Openssh` shows in all three |
| `s5-canaries` | `canaries.py`: plant the defects D0 to D5 in a copy of the library; run ty check, ty probe, runtime | the gates can fail: each gate catches the same defects as in S5 (`s5/matrix-expected.json`) | D0 passes; every other defect is caught by the same gates as in S5 |

The S5 gates (`s5lib.py`, `gate_ty_probe.py`, `gate_runtime.py`) are one unified copy. They count `NixValue` and
`JsonValue`, use the S9 `NOT_NATIVE_GAPS` set, and accept a library with or without `Text`. The probe flattens
`Annotated[A | B, Expect(...)]` as ty does.

### Refusal rule of `s9-values`

The check counts the refusals (JSON and Python mode) of the Nix-accepted default and example values. A refusal is allowed
in three cases. First, the tier is `unresolved` (Nix acceptance not proven). Second, the option type holds a constructor
that the gap file maps to `Native` (a walk of the type tree, submodule options and free-form types included). Third, the
generated field takes only `Native`. Any other refusal is "outside": the check fails and lists it in
`results/values-PKG.json`. Result on `src/`: 32 refusals = 22 counted gaps + 10 unproven examples + 0 outside.

The unproven examples depend on the option walk. The walk must run the deep check on the examples of submodule types for
NixOS and for Home Manager (`nixosWalk` and `homeWalk` in `nix/evaluate.nix`). Without it two Home Manager examples that
upstream wrote wrongly count as outside.

## Parameters

`run_gates.sh` sets each one. Set a variable before the call to use another value.

| Variable | Default | Meaning |
| --- | --- | --- |
| `PY` | `uv run --no-sync python` of the repository | the Python (pydantic 2.13.4 from `uv.lock`) that runs the gates |
| `GATES_TY` | `ty` beside `PY` | ty 0.0.84 from `uv.lock` |
| `GATES_SITE`, `GATES_PATH` | the `purelib` of `PY`; its `bin` directory | the environment of the ty language server |
| `GATES_NIXPKGS` | the nixpkgs source of `flake.lock` (`fetchTree`) | the nixpkgs for `unit/tests.nix` and `cases.nix` |
| `NIX_UNIT` | `nix build .#nix-unit` (nix-unit of the pinned nixpkgs) | the Nix test runner |
| `MANIFEST_DIR` | `nix build .#manifests` | `nixos.json`, `home-manager.json`, `flake-parts.json` |
| `GENERATOR` | `src/pynix/generate.py` | the generator that built LIBRARY (for `s9-limits` and `s9-cases`) |
| `NIXDANTIC_DECODER` | `LIBRARY/decoder.nix` | the decoder for the nix-unit tests; the control decoder is made from it |
| `S7_MACHINE`, `S7_OPENSSH` | `curated_fixture:Machine`, `pynix_os.services.openssh:Openssh` | the classes of the LSP probe |
| `S7_CURATED`, `S7_EXTRA_PATHS` | `gates/fixtures/curated_fixture`; none | the package of the curated class; more search paths |
| `CANARY_JOBS`, `LOGDIR`, `SCRATCH` | 3; `OUTDIR/logs`; `OUTDIR/scratch` | parallel canary runs; raw logs; scratch |

## Changes from the S10 harness

- Paths: the S1 Python, ty, nix-unit, the nixpkgs source, the manifests, and the generator come from the repository (see
  the table). The fixed absolute paths are gone.
- `cases.nix` imports `nix/extractor.nix` of the repository. The S10 copy of the extractor and the shim are not part of
  `gates/`.
- The decoder under test is `LIBRARY/decoder.nix`. The control decoder of `s8-nix-unit` is that file with one planted
  defect (the text kind drops the string context). The check fails when the line to plant into is not there.
  `unit/decoder-s1.nix` stays: it is the old wire format that the decoder must keep reading.
- `s7-lsp` takes its curated class from `fixtures/curated_fixture` (below).
- `results/` of the S10 evidence is not part of `gates/`.

## The curated fixture

The `s7-lsp` check needs a curated class with the hand-written `__init__` block under `TYPE_CHECKING`. S10 used the
Basix `Machine` (`evidence/S10/basix_config`). That is Basix code and does not belong in `pynix`.
`fixtures/curated_fixture/__init__.py` is a test fixture. Its class `Machine` keeps the shape that S10 probed: the fields
`name` and `user` with their attribute docstrings, and the `__init__` block with `Args`. It holds nothing else of
Basix. It proves that ty shows the description in a curated class of this shape. It does not prove the Basix class.
Basix runs its own probe on its own `Machine` (`S7_MACHINE`, `S7_CURATED`, and `S7_EXTRA_PATHS` select another class).

## Limits

- `s7-lsp` tests two keywords per class and one ty version (0.0.84, from `uv.lock`).
- The `s9-values` "counted gap" rule is a type-tree walk. A refusal below an unrelated `Native` in a large submodule would
  count as a gap. The gap file has no sites, so a per-site proof is not possible yet.
- Canaries plant in `pynix_os/services/a2boot.py` (field `enable`) only, as in S5. Gate (d) `--verifytypes` is not part of
  the harness.
- `s8-nix-unit` tests the decoder file, not the library.
- The gates run on the Python of the devenv (3.14.7 at the time of the move). S10 ran on Python 3.13. The numbers equal.
