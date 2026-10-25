#!/usr/bin/env bash
# Write the output of the generators into `src/`: the libraries of `.#libraries` and the stubs and name lists of
# `.#packageNames` (the top level and the package sets).
# Run it after a change of the generator, the runtime, or a pinned input. Then run `testee verify`.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
libs=$(nix build --no-link --print-out-paths "path:$root#libraries")
names=$(nix build --no-link --print-out-paths "path:$root#packageNames")
for part in pynix_os pynix_hm pynix_flake_parts; do
  rm -rf "$root/src/$part"
  cp -r --no-preserve=mode "$libs/$part" "$root/src/$part"
  cp --no-preserve=mode "$libs/$part-gaps.json" "$libs/$part-fields.json" "$root/src/"
done
rm -rf "$root/src/pynix_pkgs/sets"
cp --no-preserve=mode "$names/pkgs.pyi" "$names/names.json" "$names/sets.json" "$root/src/pynix_pkgs/"
cp -r --no-preserve=mode "$names/sets" "$root/src/pynix_pkgs/sets"
echo "regenerate: src/ now holds $libs and $names"
