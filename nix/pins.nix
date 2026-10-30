# The pins of the Python inputs of a workspace (021-D3): one row for each `Input(..., python=...)`.
#
# A layer writes the result into its own build output with `builtins.toJSON`. The other layer reads that file from the
# activated state, and never reads this workspace. Pynix names no layer and no path: the layer chooses both.
#
# The rows come from the same data as `input-packages.nix`: the declared inputs of the compiled entry (`name`, `url`,
# `flake`, `python`) and the flake input objects that the stub passes (`rev`, `narHash` from `flake.lock`). The locked
# value counts, not the text of the url: a `rev=` in the url can differ from the lock.
#
# Call (from a flake that has pynix as an input):
#   pynix.lib.pythonPins { declared = compiled.inputs; inputs = extraInputs; }
# Result:
#   { version = 1; pins = [ { name; url; flake; python; rev; narHash; } ... ]; }   # sorted by name; `rev` is null for a `path:` input
#
# The file `pynix_native/pins.py` reads this shape (`pins.parse`). Raise `version` when a field changes meaning.
# The function needs no `lib`: it uses `builtins` only.
{
  # The `inputs` list of the compiled entry: attribute sets with `name`, `url`, and optionally `flake` and `python`.
  declared,
  # { NAME = <flake input object>; }: the extra inputs of the stub. An input that is missing gives null `rev` and `narHash`.
  inputs ? { },
}:
let
  # `https://user:token@host/x` -> `https://host/x`. A secret in a url must never reach a world-readable file.
  scrub =
    url:
    let
      m = builtins.match "([A-Za-z+.-]+://)[^/@]*@(.*)" url;
    in
    if m == null then url else (builtins.elemAt m 0) + (builtins.elemAt m 1);

  python = builtins.filter (i: (i.python or null) != null) declared;

  row =
    i:
    let
      locked = inputs.${i.name} or { };
    in
    {
      inherit (i) name python;
      url = scrub i.url;
      flake = i.flake or true;
      rev = locked.rev or null;
      narHash = locked.narHash or null;
    };
in
{
  version = 1;
  pins = map row (builtins.sort (a: b: a.name < b.name) python);
}
