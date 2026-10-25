# The package-name list of one nixpkgs: kind, main program, and description of each top-level name.
# Copy of 009 SV4 `src/meta.nix`, with `pkgs` as an argument (it read a fixed `builtins.getFlake`).
# A name whose value throws (an alias, a broken package) gets the kind `fail`.
{ pkgs, names ? builtins.attrNames pkgs }:
let
  one = n:
    let
      r = builtins.tryEval (
        let p = pkgs.${n}; in
        if p ? type && p.type == "derivation" then
          { kind = "drv";
            main = (p.meta or {}).mainProgram or null;
            desc = (p.meta or {}).description or null; }
        else { kind = if builtins.isAttrs p then "set" else builtins.typeOf p; });
    in if r.success then r.value else { kind = "fail"; };
in builtins.listToAttrs (map (n: { name = n; value = one n; }) names)
