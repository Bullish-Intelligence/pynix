# The generated libraries as one deterministic derivation.
# Copy of 008 S15 `template/generator/default.nix` (itself a copy of S10 `generator/default.nix`).
# Input: the three pooled option manifests of `evaluate.nix`, the runtime, and the generator.
# Output: `nixdantic/`, `decoder.nix`, `pynix_os/`, `pynix_hm/`, `pynix_flake_parts/` (formatted with ruff), and the
# gap and field summaries of each library. The repository keeps the same tree in `src/`.
{ pkgs, python, ruff, manifests, runtime, decoder, generator, name ? "pynix-libraries" }:
pkgs.runCommand name { nativeBuildInputs = [ python ruff ]; } ''
  export PYTHONDONTWRITEBYTECODE=1
  export RUFF_CACHE_DIR="$TMPDIR/ruff"
  mkdir -p "$out"
  python ${generator} ${manifests}/nixos.json "$out" pynix_os --label "pynix-os (NixOS)"
  python ${generator} ${manifests}/home-manager.json "$out" pynix_hm --label "pynix-hm (Home Manager)"
  python ${generator} ${manifests}/flake-parts.json "$out" pynix_flake_parts --label "pynix-flake-parts (flake-parts)"
  cp -r ${runtime} "$out/nixdantic"
  cp ${decoder} "$out/decoder.nix"
  chmod -R u+w "$out"
  ruff format --quiet --line-length 120 "$out"
''
