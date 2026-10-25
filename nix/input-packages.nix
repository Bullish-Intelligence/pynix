# The input packages (009-D47, 009-D48, 009-D51): the typed Python package `pynix_NAME` of each extra flake input.
#
# One derivation holds a folder `pynix_NAME/` for each input. The learner's tool (Basix or minix) builds it to the
# out-link `.basix/pynix`; the compiler and ty read that folder. The store path follows `flake.lock`: the options come
# from the real, locked input object, so a moved input, a moved nixpkgs, or a new generator gives another store path.
#
# Per input the function
#   1. evaluates the named modules of the input (`nixosModules.M` or `homeManagerModules.M`) together with the base
#      options of the layer, so a module that reads `config.xdg.dataHome` or `config.users` still evaluates;
#   2. keeps only the options that the input declares (`declarations` and `declarationPositions` below the store path
#      of the input), so no base option leaks into the package;
#   3. walks the kept options with `extractor.nix` and runs `src/pynix/gen_input.py` (the generator with
#      `--init-nested`, the input named in each class docstring, and the name stub of `packages.<system>`).
# `_generation.py` holds `SOURCE = {input, narHash, rev, nixpkgs, generator, modules}` for the pair check (the keys
# `input`, `narHash`, `rev`, `nixpkgs`, and `generator` are the ones that `pynix_native.pair` reads). `nixpkgs` is the
# commit of the nixpkgs that the input uses after `follows`. `generator` is a hash of the generator files, so a changed
# generator gives a new store path and the pair check says `regenerate` (010-D5).
#
# Call (from a flake that has pynix as an input):
#   pynix.lib.inputPackages { pkgs = ...; layer = "nixos"; nixpkgs = inputs.nixpkgs; inputs = { inherit nirinit; };
#                             modules.nirinit = [ "nirinit" ]; }
# Call (pynix with `flake = false`): the same arguments to `import "${pynix}/nix/input-packages.nix"`.
#
# A named nixpkgs (`NixpkgsPin(name, commit)`, 009-D53, 009-D54) is not an input with options. The argument `nixpkgsInputs`
# gives it a name list `pynix_nixpkgs_NAME` (`src/pynix/gen_nixpkgs.py`), so `NAME.pkgs.PACKAGE` finds its packages.
#
# An input that is not a flake (`flake = false`) gets no package. An input with no module in `modules` (or with an
# empty list) declares no option: its package holds the name stub only (SG44).
{
  # The pkgs of the layer. The modules evaluate with it, as the machine does.
  pkgs,
  # "nixos" or "home-manager".
  layer,
  # { NAME = <flake input object>; }: the extra inputs of the entry (`Input(...)`), with `follows` applied.
  inputs,
  # { NAME = [ "module" ... ]; }: the modules of each input to import (`Input(modules=[...])`).
  modules ? { },
  # { NAME = <flake input object of `nixpkgs-NAME`>; }: the nixpkgs pins of the entry (`NixpkgsPin(name, commit)`), keyed by
  # the name without the prefix `nixpkgs-`. Each gets the package-name list `pynix_nixpkgs_NAME`. Not an input of `inputs`.
  nixpkgsInputs ? { },
  # The nixpkgs flake input of the layer. It gives the `nixpkgs` commit of an input that has no nixpkgs input.
  nixpkgs ? null,
  # The home-manager flake input (needed for layer "home-manager"; its `lib.homeManagerConfiguration` is the base).
  homeManager ? null,
  # A module list that replaces the base of the layer (for example `[ ]` for no base, or stub modules of your own).
  # The default `null` gives the full base of the layer: NixOS `eval-config.nix`, or `homeManagerConfiguration`.
  baseModules ? null,
  # Passed to the modules as `specialArgs` (NixOS) or `extraSpecialArgs` (Home Manager). The machine passes `inputs`.
  specialArgs ? { inherit inputs; },
  # The pynix source tree (`src/`). A consumer with `flake = false` can leave it out: it is the tree next to this file.
  src ? ../src,
  # The Python of the build. The generator needs the standard library only.
  python ? pkgs.python3,
  # Set to `pkgs.ruff` to format the generated files (line length 120). The default writes them unformatted:
  # the type checker gives the same result and the build needs no ruff.
  ruff ? null,
  lib ? pkgs.lib,
  system ? pkgs.stdenv.hostPlatform.system,
}:
let
  inherit (builtins) hashFile hashString substring;

  # ---- the generator ---------------------------------------------------------------------------------------------
  # The Python files of the generator in one small tree: `pynix/{__init__,generate,gen_pkgs,gen_input,gen_nixpkgs}.py`.
  generatorTree = builtins.path {
    path = src;
    name = "pynix-input-generator";
    filter =
      path: type:
      let
        rel = lib.removePrefix (toString src) path;
      in
      rel == ""
      || rel == "/pynix"
      || lib.elem rel (map (f: "/pynix/${f}.py") [ "__init__" "generate" "gen_pkgs" "gen_input" "gen_nixpkgs" ]);
  };
  extractor = ./extractor.nix;
  # The generator version: a hash of every file that decides the output. A change gives another store path.
  generatorId =
    "input-gen-"
    + substring 0 12 (
      hashString "sha256" (
        lib.concatMapStringsSep "," (hashFile "sha256") (
          map (f: src + "/pynix/${f}.py") [ "generate" "gen_pkgs" "gen_input" ] ++ [ extractor ./input-packages.nix ]
        )
      )
    );
  extract = import extractor {
    inherit lib;
    pool = true;
  };

  # ---- the layer ---------------------------------------------------------------------------------------------------
  moduleOutput =
    {
      nixos = "nixosModules";
      home-manager = "homeManagerModules";
    }
    .${layer};

  # The option tree of the layer with the given modules. Only `options` is read, never `config`.
  evalOptions =
    mods:
    if baseModules != null then
      (lib.evalModules {
        modules = baseModules ++ mods ++ [
          {
            _module.args.pkgs = lib.mkDefault pkgs;
            _module.check = false;
          }
        ];
        inherit specialArgs;
      }).options
    else if layer == "nixos" then
      (import (pkgs.path + "/nixos/lib/eval-config.nix") {
        system = null;
        inherit specialArgs;
        # `stateVersion` has a default that warns when unset; the walk reads defaults, so set it.
        modules = [
          {
            nixpkgs.pkgs = pkgs;
            system.stateVersion = lib.mkDefault lib.trivial.release;
          }
        ] ++ mods;
      }).options
    else
      (homeManager.lib.homeManagerConfiguration {
        inherit pkgs;
        extraSpecialArgs = specialArgs;
        modules = [
          {
            home.username = "n1";
            home.homeDirectory = "/home/n1";
            home.stateVersion = "24.11";
          }
        ] ++ mods;
      }).options;

  # ---- the filter --------------------------------------------------------------------------------------------------
  # Keep an option when a file of the input declares it. A module that is a plain value of the flake (not a file) has
  # the declaration `<unknown-file>`, so the position of the option names the file (SG42a, SG42c).
  isOption = v: builtins.isAttrs v && (v._type or null) == "option";
  filterTree =
    root: tree:
    let
      prefix = root + "/";
      declaredHere =
        o:
        lib.any (d: lib.hasPrefix prefix (toString d)) (o.declarations or [ ])
        || lib.any (p: lib.hasPrefix prefix (toString p.file)) (o.declarationPositions or [ ]);
      walk =
        t:
        lib.filterAttrs (_: v: v != null && v != { }) (
          lib.mapAttrs (
            _: v:
            if isOption v then
              (if declaredHere v then v else null)
            else if builtins.isAttrs v && !(v ? _type) then
              walk v
            else
              null
          ) t
        );
    in
    walk tree;

  # ---- one input ---------------------------------------------------------------------------------------------------
  nixpkgsCommit =
    name: input:
    let
      n = input.inputs.nixpkgs or nixpkgs;
    in
    if n == null then
      throw "pynix input packages: the input `${name}` has no nixpkgs input, so the argument `nixpkgs` is needed"
    else
      n.rev or null;

  one =
    name: input:
    let
      available = input.${moduleOutput} or { };
      wanted = modules.${name} or [ ];
      pick =
        m:
        available.${m} or (throw ''
          pynix input packages: the input `${name}` has no ${moduleOutput}.${m}. It has: ${
            lib.concatStringsSep ", " (builtins.attrNames available)
          }.'');
      kept = if wanted == [ ] then { } else filterTree (toString input.outPath) (evalOptions (map pick wanted));
      source =
        {
          input = name;
          inherit (input) narHash;
          modules = lib.concatStringsSep "," wanted;
          generator = generatorId;
        }
        // lib.optionalAttrs (input ? rev) { inherit (input) rev; }
        // lib.optionalAttrs (nixpkgsCommit name input != null) { nixpkgs = nixpkgsCommit name input; };
      manifest = (extract { options = kept; }) // {
        inherit source;
      };

      # The package-name stub: the names of `packages.<system>` with kind, main program, and description.
      pkgSet = input.packages.${system} or { };
      # A set that throws when it lists its names gives no names, not a failed build.
      pkgNames =
        let
          r = builtins.tryEval (builtins.attrNames pkgSet);
        in
        if r.success then r.value else [ ];
      meta =
        n:
        let
          r = builtins.tryEval (
            let
              p = pkgSet.${n};
            in
            if p ? type && p.type == "derivation" then
              {
                kind = "drv";
                main = (p.meta or { }).mainProgram or null;
                desc = (p.meta or { }).description or null;
              }
            else
              { kind = "other"; }
          );
        in
        if r.success then r.value else { kind = "fail"; };
      json = n: v: pkgs.writeText "${n}-${name}.json" (builtins.unsafeDiscardStringContext (builtins.toJSON v));
    in
    pkgs.runCommand "pynix-${name}"
      {
        nativeBuildInputs = [ python ] ++ lib.optional (ruff != null) ruff;
        passthru = { inherit manifest source; };
      }
      ''
        export PYTHONDONTWRITEBYTECODE=1 PYTHONSAFEPATH=1 PYTHONPATH=${generatorTree}
        mkdir -p "$out"
        python -m pynix.gen_input ${json "manifest" manifest} ${json "packages" (lib.genAttrs pkgNames meta)} \
          "$out" ${lib.escapeShellArg name} > "$TMPDIR/summary.json"
        cat "$TMPDIR/summary.json"
        ${lib.optionalString (ruff != null) ''
          export RUFF_CACHE_DIR="$TMPDIR/ruff"
          ruff format --quiet --line-length 120 --no-cache "$out"
        ''}
      '';

  # ---- one named nixpkgs ---------------------------------------------------------------------------------------------
  # The package-name list of a pinned nixpkgs. `nixpkgs-names.nix` reads `legacyPackages` and the lock node of the input.
  oneNixpkgs =
    name: input:
    let
      list = import ./nixpkgs-names.nix {
        legacyPackages = input.legacyPackages.${system};
        source = {
          inherit (input) narHash;
          rev = input.rev or (throw "pynix input packages: the nixpkgs `${name}` has no rev; pin it by commit");
          lastModified = input.lastModified or null;
        };
      };
    in
    pkgs.runCommand "pynix-nixpkgs-${name}"
      {
        nativeBuildInputs = [ python ];
        passthru = { inherit (list) source; };
      }
      ''
        export PYTHONDONTWRITEBYTECODE=1 PYTHONSAFEPATH=1 PYTHONPATH=${generatorTree}
        mkdir -p "$out"
        python -m pynix.gen_nixpkgs ${pkgs.writeText "nixpkgs-${name}.json" (builtins.unsafeDiscardStringContext (builtins.toJSON list))} \
          "$out" ${lib.escapeShellArg name} > "$TMPDIR/summary.json"
        cat "$TMPDIR/summary.json"
      '';

  # An input that is not a flake has no module to type (009-D52).
  flakes = lib.filterAttrs (_: v: (v._type or null) == "flake") inputs;
  # The key of a name list cannot meet the key of an input: the prefix `nixpkgs-` is not a valid input name (it is taken).
  parts = lib.mapAttrs one flakes // lib.mapAttrs' (n: v: lib.nameValuePair "nixpkgs-${n}" (oneNixpkgs n v)) nixpkgsInputs;
in
if !(lib.elem layer [ "nixos" "home-manager" ]) then
  throw ''pynix input packages: layer must be "nixos" or "home-manager", found "${layer}"''
else if layer == "home-manager" && baseModules == null && homeManager == null then
  throw ''pynix input packages: layer "home-manager" needs the argument `homeManager` (the home-manager flake)''
else
  pkgs.symlinkJoin {
    name = "pynix-inputs";
    paths = lib.attrValues parts;
    passthru = {
      generator = generatorId;
      inherit parts;
    };
  }
