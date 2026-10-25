#!/usr/bin/env bash
# Usage: run_gates.sh [--no-canaries] LIBRARY OUTDIR [CHECK...]
#
# Runs the 11 gate checks on a generated library and writes OUTDIR/summary.txt and OUTDIR/summary.json.
# LIBRARY holds nixdantic, decoder.nix, pynix_os, pynix_hm, pynix_flake_parts (with their -gaps.json and -fields.json
# files). In the repository it is `src/`. Run it from the repository root: `bash gates/run_gates.sh src OUTDIR`.
# CHECK names (default: all): s5-ty-check s5-ty-probe s5-runtime s9-values s9-patterns s9-limits s9-cases
#                             s8-nix-unit s8-runtime s7-lsp s5-canaries
# Exit 0 only when every check that ran passes. A failure with a known cause prints "FAIL (expected: ...)" and still fails.
#
# Parameters (environment). Each default comes from the repository; the README lists them:
#   PY                 the Python of the uv environment (`uv run --no-sync python`)
#   GATES_TY           ty of the same environment (pinned in uv.lock)
#   GATES_NIXPKGS      the nixpkgs source of flake.lock (a store path)
#   NIX_UNIT           nix-unit of the pinned nixpkgs (`nix build .#nix-unit`)
#   MANIFEST_DIR       nixos.json, home-manager.json, flake-parts.json (`nix build .#manifests`)
#   GENERATOR          src/pynix/generate.py
#   NIXDANTIC_DECODER  decoder.nix for the nix-unit tests (LIBRARY/decoder.nix)
#   S7_MACHINE, S7_OPENSSH, S7_CURATED, S7_EXTRA_PATHS   the LSP probe; see s7_probe.py
#   CANARY_JOBS, LOGDIR (raw logs; default OUTDIR/logs), SCRATCH (default OUTDIR/scratch)
set -u
export PYTHONDONTWRITEBYTECODE=1
here=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
root=$(cd "$here/.." && pwd)

canaries=1
args=()
for a in "$@"; do
  case "$a" in
    --no-canaries) canaries=0 ;;
    --canaries) canaries=1 ;;
    *) args+=("$a") ;;
  esac
done
[ "${#args[@]}" -ge 2 ] || { sed -n 2,3p "$0"; exit 2; }
export LIBRARY=$(readlink -f "${args[0]}")
mkdir -p "${args[1]}"
export OUTDIR=$(readlink -f "${args[1]}")
requested=("${args[@]:2}")
[ -d "$LIBRARY" ] || { echo "no library: $LIBRARY" >&2; exit 2; }

# Clear the old scratch first: a `path:` flake copies the whole tree, and OUTDIR may sit inside it.
export SCRATCH=${SCRATCH:-$OUTDIR/scratch}
rm -rf "$OUTDIR/checks" "$SCRATCH"
export LOGDIR=${LOGDIR:-$OUTDIR/logs}
mkdir -p "$OUTDIR/checks" "$LOGDIR"

die() { echo "run_gates: $*" >&2; exit 2; }

# The Python and ty of the uv environment. A virtual environment keeps its own path, so do not resolve the link.
if [ -z "${PY:-}" ]; then
  PY=$(cd "$root" && uv run --no-sync python -c 'import sys; print(sys.executable)') || die "no uv environment: run uv sync"
fi
export PY
export GATES_TY=${GATES_TY:-$(dirname "$PY")/ty}
[ -x "$GATES_TY" ] || die "no ty at $GATES_TY"
export GATES_SITE=${GATES_SITE:-$("$PY" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')}
export GATES_PATH=${GATES_PATH:-$(dirname "$PY"):/usr/bin:/bin}

# The nixpkgs source of the lock (no network when the store holds it).
if [ -z "${GATES_NIXPKGS:-}" ]; then
  GATES_NIXPKGS=$(nix eval --raw --impure --expr \
    'let l = (builtins.fromJSON (builtins.readFile '"$root"'/flake.lock)).nodes.nixpkgs.locked; in (builtins.fetchTree l).outPath' 2>>"$LOGDIR/nix.txt") \
    || die "cannot read the nixpkgs source from flake.lock (see $LOGDIR/nix.txt)"
fi
export GATES_NIXPKGS

# nix-unit and the manifests are flake outputs of the repository.
if [ -z "${NIX_UNIT:-}" ]; then
  NIX_UNIT=$(nix build --no-link --print-out-paths "path:$root#nix-unit" 2>>"$LOGDIR/nix.txt")/bin/nix-unit || die "cannot build nix-unit (see $LOGDIR/nix.txt)"
fi
export NIX_UNIT
if [ -z "${MANIFEST_DIR:-}" ]; then
  MANIFEST_DIR=$(nix build --no-link --print-out-paths "path:$root#manifests" 2>>"$LOGDIR/nix.txt") || die "cannot build the manifests (see $LOGDIR/nix.txt)"
fi
export MANIFEST_DIR

export GENERATOR=${GENERATOR:-$root/src/pynix/generate.py}
export NIXDANTIC_DECODER=${NIXDANTIC_DECODER:-$LIBRARY/decoder.nix}

run() { "$PY" -I "$here/gates.py" "$1" 2>&1 | tee -a "$LOGDIR/run.txt" | tail -1; }

check_s5_ty_check()  { run s5-ty-check; }
check_s5_ty_probe()  { run s5-ty-probe; }
check_s5_runtime()   { run s5-runtime; }
check_s9_values()    { run s9-values; }
check_s9_patterns()  { run s9-patterns; }
check_s9_limits()    { run s9-limits; }
check_s9_cases()     { run s9-cases; }
check_s8_nix_unit()  { run s8-nix-unit; }
check_s8_runtime()   { run s8-runtime; }
check_s7_lsp()       { run s7-lsp; }
check_s5_canaries()  { run s5-canaries; }

all=(s5-ty-check s5-ty-probe s5-runtime s9-values s9-patterns s9-limits s9-cases s8-nix-unit s8-runtime s7-lsp)
[ "$canaries" = 1 ] && all+=(s5-canaries)
if [ "${#requested[@]}" -gt 0 ]; then selected=("${requested[@]}"); else selected=("${all[@]}"); fi

for c in "${selected[@]}"; do
  fn=check_${c//-/_}
  if ! declare -F "$fn" >/dev/null; then echo "unknown check: $c" >&2; exit 2; fi
  rm -f "$OUTDIR/checks/$c.json"
  echo "== $c"
  "$fn"
done

exec "$PY" -I "$here/summary.py" "$OUTDIR" "$LIBRARY" "${selected[@]}"
