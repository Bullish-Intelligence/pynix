# The package-name list of ONE pinned nixpkgs (a `NixpkgsPin(name, commit)` of an entry, 009-D54).
# Pure: the caller fetches the nixpkgs by its lock node and passes its `legacyPackages` (for example
# `inputs.nixpkgs.legacyPackages.${system}`, or `import src { inherit system; }` for a source from `fetchTree`).
# `source` is the lock node `locked` of `nixpkgs-NAME`: `{ rev; narHash; lastModified; }`.
# Output: `{ source = { commit; narHash; lastModified; }; packages = { ATTR = { kind; main; desc; }; }; }`.
# The generator `src/pynix/gen_nixpkgs.py` reads it. Each name that throws gets the kind `fail` (see `pkgs-meta.nix`).
{
  legacyPackages,
  source,
  names ? builtins.attrNames legacyPackages,
}:
{
  source = {
    commit = source.rev;
    inherit (source) narHash;
    lastModified = source.lastModified or null;
  };
  packages = import ./pkgs-meta.nix {
    pkgs = legacyPackages;
    inherit names;
  };
}
