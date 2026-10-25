#!/usr/bin/env bash
# Check that `src/` holds exactly what the generators make from the pinned inputs.
# It builds `.#libraries` (the option walk, then the generator) and `.#packageNames` (the package-name list and the
# package sets), and compares each generated file with `src/`. The libraries hold the flat
# namespace `all.py` too. A difference fails: regenerate with `scripts/regenerate.sh`.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
out=${TESTEE_RUN_DIR:-$root/.devenv/state}/check-generated
mkdir -p "$out"
# A caller that built the outputs already passes them in, so the option walk runs once.
libs=${PYNIX_LIBRARIES:-$(nix build --no-link --print-out-paths "path:$root#libraries" 2>"$out/libraries.log")}
names=${PYNIX_PACKAGE_NAMES:-$(nix build --no-link --print-out-paths "path:$root#packageNames" 2>"$out/package-names.log")}
fail=0
for part in nixdantic decoder.nix pynix_os pynix_hm pynix_flake_parts \
  pynix_os-gaps.json pynix_os-fields.json pynix_hm-gaps.json pynix_hm-fields.json \
  pynix_flake_parts-gaps.json pynix_flake_parts-fields.json; do
  if ! diff -r -x __pycache__ "$libs/$part" "$root/src/$part" >"$out/diff-$part.txt" 2>&1; then
    echo "check_generated: src/$part differs from $libs/$part (see $out/diff-$part.txt)"
    fail=1
  fi
done
# The stub files, the name list of the top level, the index of the package sets, and the stub and name list of each set.
for part in pkgs.pyi names.json sets.json sets; do
  if ! diff -r "$names/$part" "$root/src/pynix_pkgs/$part" >"$out/diff-pkgs-$part.txt" 2>&1; then
    echo "check_generated: src/pynix_pkgs/$part differs from $names/$part (see $out/diff-pkgs-$part.txt)"
    fail=1
  fi
done
[ "$fail" = 0 ] && echo "check_generated: src/ equals $libs and $names"
exit "$fail"
