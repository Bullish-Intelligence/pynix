# The option walk: the three module sets that the generator reads, one manifest each.
# Copy of 008 S10 `generator/evaluate.nix`, with two changes:
#   - The sources are flake inputs, not `builtins.getFlake` of fixed revisions.
#   - Home Manager evaluates with the nixpkgs of this flake (owner decision L126), not with the nixpkgs of its own
#     lock. So `pynix_hm` pairs with the nixpkgs that minix evaluates with.
#   - The walk settings that S9 passed in the environment are arguments (`nixosWalk`, `homeWalk`, `partsWalk`).
#     The defaults are the settings of the stored S9 manifests: the NixOS walk forces example values of submodule
#     types (`S9_SUBMODULES=1`) and skips the ten examples that stop the evaluator (S9 `results/skip-nixos.txt`).
#     The Home Manager walk forces them too, as the stored S9 manifest does: with `submodules = false` the `deep`
#     field of 2 submodule examples reads "not run", and the gate `s9-values` counts them as outside the gaps.
{ nixpkgs, home-manager, flake-parts, system ? "x86_64-linux"
, nixosWalk ? {
    submodules = true;
    skip = [
      "__nixdantic_placeholder__.flowQueuePIEConfig:example"
      "__nixdantic_placeholder__.pfifoConfig:example"
      "__nixdantic_placeholder__.pfifoHeadDropConfig:example"
      "__nixdantic_placeholder__.pieConfig:example"
      "__nixdantic_placeholder__.stochasticFairBlueConfig:example"
      "__nixdantic_placeholder__.inclexcl:example"
      "__nixdantic_placeholder__.locks:example"
      "__nixdantic_placeholder__.settings:example"
      "services.restic.backups:example"
      "__nixdantic_placeholder__.services.restic.backups:example"
    ];
  }
, homeWalk ? { submodules = true; }
, partsWalk ? { }
}:
let
  lib = nixpkgs.lib;
  shimLib = import ./shim.nix lib;
  # `lib.nixosSystem` is bound to the original lib. Call eval-config with the shimmed lib (008 A1b).
  nixos = import (nixpkgs + "/nixos/lib/eval-config.nix") {
    lib = shimLib;
    system = null;
    modules = [ ({ ... }: { nixpkgs.hostPlatform = system; }) ];
  };
  home = home-manager.lib.homeManagerConfiguration {
    pkgs = import nixpkgs { inherit system; };
    modules = [ ({ ... }: {
      home.username = "n1";
      home.homeDirectory = "/home/n1";
      home.stateVersion = "24.11";
    }) ];
  };
  parts = flake-parts.lib.evalFlakeModule { inputs = { inherit nixpkgs flake-parts; homeManager = home-manager; flakeParts = flake-parts; }; } {
    systems = [ system ];
    perSystem = { ... }: { };
  };
  extract = settings: import ./extractor.nix ({ inherit lib; pool = true; } // settings);
  source = revs: m: m // { source = revs; };
in {
  nixos = source { nixpkgs = nixpkgs.rev; } (extract nixosWalk nixos);
  home-manager = source { home-manager = home-manager.rev; nixpkgs = nixpkgs.rev; } (extract homeWalk home);
  flake-parts = source { flake-parts = flake-parts.rev; nixpkgs-lib = nixpkgs.rev; } (extract partsWalk parts);
}
