{
  description = "pynix: typed Python values to Nix definitions.";

  inputs = {
    # The option source and the tool source. Basix pins the same revision.
    nixpkgs.url = "github:NixOS/nixpkgs/e7439b6b14ad3cc35d05608ebca9bce01a25f5f8";
    # Home Manager follows nixpkgs, so `pynix_hm` pairs with the nixpkgs that minix evaluates with (L126).
    home-manager = {
      url = "github:nix-community/home-manager/fae6e9e42c3b762ab47635cddcfaf6f52374a61b";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    # flake-parts assembles the outputs (009-D1), and its options are the source of `pynix_flake_parts`.
    flake-parts = {
      url = "github:hercules-ci/flake-parts/024633cd702b10285db5cb19b40ad48d2399ba60";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };
    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
    };
    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
    };
  };

  outputs = inputs@{ nixpkgs, flake-parts, pyproject-nix, uv2nix, pyproject-build-systems, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" ];

      flake = {
        # The checked-in tree. A consumer that sets `flake = false` reads `"${input}/src"` instead.
        lib.src = ./src;
        lib.version = (builtins.fromTOML (builtins.readFile ./pyproject.toml)).project.version;
        # The input packages (009-D47): one derivation with `pynix_NAME/` for each extra flake input. Basix and minix call
        # it from their flakes. A consumer with `flake = false` calls `import "${pynix}/nix/input-packages.nix"` instead.
        lib.inputPackages = args: import ./nix/input-packages.nix args;
      };

      perSystem = { pkgs, system, ... }:
        let
          inherit (nixpkgs) lib;
          workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
          lockedOverlay = workspace.mkPyprojectOverlay { sourcePreference = "wheel"; };
          pythonSet =
            (pkgs.callPackage pyproject-nix.build.packages { python = pkgs.python313; }).overrideScope (
              lib.composeManyExtensions [
                pyproject-build-systems.overlays.wheel
                lockedOverlay
                (final: prev: {
                  pynix = prev.pynix.overrideAttrs (old: {
                    nativeBuildInputs = (old.nativeBuildInputs or [ ]) ++ final.resolveBuildSystem {
                      hatchling = [ ];
                    };
                  });
                })
              ]
            );
          venv = pythonSet.mkVirtualEnv "pynix-env" workspace.deps.default;

          # The option walk. Nix evaluates it once and writes one JSON file per module set.
          walk = import ./nix/evaluate.nix {
            inherit system;
            inherit (inputs) nixpkgs home-manager flake-parts;
          };
          manifests = pkgs.runCommand "pynix-manifests" { } ''
            mkdir -p "$out"
            cp ${pkgs.writeText "nixos.json" (builtins.toJSON walk.nixos)} "$out/nixos.json"
            cp ${pkgs.writeText "home-manager.json" (builtins.toJSON walk.home-manager)} "$out/home-manager.json"
            cp ${pkgs.writeText "flake-parts.json" (builtins.toJSON walk.flake-parts)} "$out/flake-parts.json"
          '';
          # The generator needs only the standard library. ruff comes from `uv.lock`, so the format is fixed.
          librariesFrom = manifestDir: import ./nix/libraries.nix {
            inherit pkgs;
            python = pkgs.python313;
            ruff = pythonSet.ruff;
            manifests = manifestDir;
            # A local `__pycache__` must not enter the build: a clean checkout has none.
            runtime = builtins.path {
              path = ./src/nixdantic;
              name = "nixdantic-runtime";
              filter = path: type: baseNameOf path != "__pycache__";
            };
            decoder = ./src/decoder.nix;
            generator = ./src/pynix/generate.py;
          };
          # The package-name list of the pinned nixpkgs (009-D31) and the package sets in it (009-D43): `pkgs.pyi`,
          # `names.json`, `sets.json`, `sets/` of `pynix_pkgs`. Pure evaluation of the pinned `legacyPackages`.
          nixpkgsPackages = inputs.nixpkgs.legacyPackages.${system};
          curatedSets = ./src/pynix/curated-sets.txt;
          topMeta = import ./nix/pkgs-meta.nix { pkgs = nixpkgsPackages; };
          setMeta = import ./nix/pkgs-sets.nix {
            pkgs = nixpkgsPackages;
            inherit topMeta;
            curated = lib.filter (line: line != "") (lib.splitString "\n" (builtins.readFile curatedSets));
          };
          packageNames = pkgs.runCommand "pynix-package-names" { nativeBuildInputs = [ pkgs.python313 ]; } ''
            export PYTHONDONTWRITEBYTECODE=1
            python -I ${./src/pynix/gen_pkgs.py} ${pkgs.writeText "pynix-package-meta.json" (builtins.toJSON topMeta)} \
              ${pkgs.writeText "pynix-package-sets.json" (builtins.toJSON setMeta)} ${curatedSets} "$out" > "$TMPDIR/stats.json"
            cp "$TMPDIR/stats.json" "$out/stats.json"
          '';
        in
        {
          packages = {
            default = venv;
            pynix = venv;
            inherit manifests packageNames;
            # The test runner of the decoder gate (`gates/`): the version of the pinned nixpkgs.
            nix-unit = pkgs.nix-unit;
            # The generated libraries from the walk of this flake's inputs: the tree that `src/` holds.
            libraries = librariesFrom manifests;
          };
          # The same derivation from another manifest directory, for example a stored walk.
          legacyPackages = { inherit librariesFrom; };
          checks.pynix = venv;
        };
    };
}
