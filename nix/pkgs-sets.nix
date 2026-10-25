# The package sets of one nixpkgs: the packages of each set, for the nested names `pkgs.nerd_fonts.fira_code` (009-D43).
# Copy of 009 SG36 `meta-set.nix` (the members of one set) and `sets.nix` (the walk over the sets), in one pure
# expression. A package set is a top-level name of kind "set" that is not on the skip list.
# Output: `{ SET = { MEMBER = { main?, desc? }; }; }` for each set that holds at least one package.
# `desc` is present only for a curated set, because only a curated set has a stub with docstrings.
# A member whose value throws (an alias, a broken package) is left out, as `pkgs-meta.nix` gives it the kind `fail`.
{ pkgs, topMeta, curated }:
let
  lib = pkgs.lib;
  # Not package sets: they evaluate nixpkgs again (`pkgs*`, `buildPackages`, ...), or hold tests, or are not a set of
  # packages (`lib`, `config`, `haskell`, `darwin`, ...). The three `pypy` sets throw "infinite recursion", which
  # `tryEval` does not catch.
  skip = [
    "__splicedPackages" "buildPackages" "config" "cygwin" "darwin" "driversi686Linux" "freebsd" "haskell" "lib"
    "linuxKernel" "minimal-bootstrap" "minimal-bootstrap-sources" "netbsd" "nixosTests" "openbsd" "pkgs" "pkgsArocc"
    "pkgsBuildBuild" "pkgsBuildHost" "pkgsBuildTarget" "pkgsChecked" "pkgsCross" "pkgsCuda" "pkgsExtraHardening"
    "pkgsForCudaArch" "pkgsHostHost" "pkgsHostTarget" "pkgsLLVM" "pkgsLinux" "pkgsMusl" "pkgsParallel" "pkgsRocm"
    "pkgsStatic" "pkgsStrict" "pkgsStructured" "pkgsTargetTarget" "pkgsZig" "pkgsi686Linux" "stdenvAdapters"
    "targetPackages" "tests" "webos" "windows"
    "pypy27Packages" "pypy2Packages" "pypyPackages"
  ];
  candidates = lib.filter (n: topMeta.${n}.kind == "set" && !(builtins.elem n skip)) (builtins.attrNames topMeta);
  # One member: `null` when it is not a package or its value throws. `deepSeq` makes `tryEval` see every field.
  member = withDesc: set: n:
    let
      r = builtins.tryEval (
        let
          p = set.${n};
          meta = p.meta or { };
          value =
            lib.optionalAttrs (builtins.isString (meta.mainProgram or null)) { main = meta.mainProgram; }
            // lib.optionalAttrs (withDesc && builtins.isString (meta.description or null)) { desc = meta.description; };
        in
        if builtins.isAttrs p && (p.type or "") == "derivation" then builtins.deepSeq value value else null
      );
    in
    if r.success then r.value else null;
  one = n:
    let
      r = builtins.tryEval (
        let
          set = pkgs.${n};
          members = builtins.attrNames set;
          rows = map (m: { name = m; value = member (builtins.elem n curated) set m; }) members;
          kept = builtins.filter (row: row.value != null) rows;
        in
        if builtins.isAttrs set && (set.type or "") != "derivation" then builtins.listToAttrs kept else { }
      );
    in
    if r.success then r.value else { };
  all = map (n: { name = n; value = one n; }) candidates;
in
builtins.listToAttrs (builtins.filter (row: row.value != { }) all)
