# Each fragment enters lib.evalModules as one independent module.
# S8 copy of the S1 decoder. Wire format version 1 stays readable. Additions:
#   - the reference kind "text": a string made of literal parts and references (it keeps the string context);
#   - an unknown package attribute throws a message that names the learner line (`input.source`);
#   - the reference kind "path" (009-D44): a file of the workspace as a Nix path;
#   - the reference kind "with_packages" (009-D43): a Python with libraries;
#   - the reference kinds "input_package" (SG42a) and "nixpkgs_package" (SG44): a package of a flake input, and a
#     package of a nixpkgs pinned by commit. Both read `inputs` from the special arguments.
#   - the reference kind "exe": the main program of a package, `lib.getExe pkgs.ATTR` (`Exe`, `pynix_pkgs`);
#   - the reference kind "native" (PF-5, PF-8): a function gets the module arguments that it names. A whole-value
#     reference (empty `attr`) calls only a function that names an argument, so an overlay `final: prev:` stays a function.
#   - the reference kinds "priority" and "order" (L128): `Force(v)` is `lib.mkOverride 50`, `Before(v)` is `lib.mkOrder 500`.
{ fragment, nativeRoot ? ./. }:
args@{ lib, config, pkgs, inputs ? { }, ... }:
let
  input = if builtins.isPath fragment then builtins.fromJSON (builtins.readFile fragment) else fragment;
  fail = message: throw "nixdantic: ${input.source}: ${message}";
  package = attr:
    let path = lib.splitString "." attr;
    in if lib.hasAttrByPath path pkgs then lib.getAttrFromPath path pkgs
       else fail "unknown package `${attr}`: pkgs has no attribute `${attr}`";
  # SG36: `python3.withPackages (ps: [ ps.requests ])`. `attr` is the interpreter; `packages` are attribute paths
  # below its package set (`ps`).
  withPackages = ref:
    let
      interp = package ref.attr;
      pick = ps: name:
        let path = lib.splitString "." name;
        in if lib.hasAttrByPath path ps then lib.getAttrFromPath path ps
           else fail "unknown package `${name}`: `${ref.attr}` has no package set member `${name}`";
    in if interp ? withPackages then interp.withPackages (ps: map (pick ps) ref.packages)
       else fail "package `${ref.attr}` has no withPackages";
  # SG42a: `InputPkg(input, attr)` is `inputs.INPUT.packages.<system>.ATTR` (the typed package of a flake input).
  inputPackage = ref:
    let p = lib.attrByPath [ ref.input "packages" pkgs.stdenv.hostPlatform.system ref.attr ] null inputs;
    in if p != null then p else fail "unknown package `${ref.attr}`: the input `${ref.input}` has no such package";
  # SG44: `NixpkgsPkg(nixpkgs, attr)` is `inputs.nixpkgs-NAME.legacyPackages.<system>.ATTR` (a package of a nixpkgs pinned by commit).
  nixpkgsPackage = ref:
    let p = lib.attrByPath [ "nixpkgs-${ref.nixpkgs}" "legacyPackages" pkgs.stdenv.hostPlatform.system ref.attr ] null inputs;
    in if p != null then p else fail "unknown package `${ref.attr}`: the nixpkgs `${ref.nixpkgs}` has no such package (is it in flake.nix? run `basix apply`)";
  # One part of a text: a string stays as it is, a package or a path becomes its store path. Other values fail.
  textPart = index: value:
    if builtins.isString value then value
    else if builtins.isPath value || (builtins.isAttrs value && value ? outPath) then "${value}"
    else fail "part ${toString index} of a text has type ${builtins.typeOf value}, not a string or a path";
  # PF-5, PF-8: a native value file is a value, or a function of module arguments (`{ pkgs, inputs, ... }:`).
  # Nix cannot tell `{ ... }:` from `final: prev:`: `builtins.functionArgs` gives `{ }` for both. So the rule
  # depends on how the reference reads the file:
  #   - `attr` is not empty: the file must give an attribute set. A function receives the module arguments that it
  #     names, as the module system does (`{ }` for `{ ... }:`). `inputs` is `{ }` when empty.
  #   - `attr` is empty: the reference takes the whole value, for example an overlay `final: prev: ...`. A function
  #     that names arguments (`{ pkgs, ... }:`) gets the module arguments. Any other value stays as it is.
  # The edge: a whole-value file `{ ... }:` names no argument. The decoder returns it as a function.
  nativeValue = ref:
    let
      value = import (nativeRoot + "/${ref.file}");
      moduleArgs = args // { inherit inputs; };
      names = builtins.functionArgs value;
      call = value (builtins.intersectAttrs names moduleArgs);
    in if !builtins.isFunction value then value
       else if ref.attr != [ ] || names != { } then call
       else value;
  decode = value:
    if builtins.isList value then map decode value
    else if !builtins.isAttrs value then value
    else if value ? __nixdantic_literal__ then lib.mapAttrs (_: decode) value.__nixdantic_literal__
    else if value ? __nixdantic_ref__ then
      let ref = value.__nixdantic_ref__;
      in if ref.kind == "package" then package ref.attr
         else if ref.kind == "exe" then lib.getExe (package ref.attr)
         else if ref.kind == "with_packages" then withPackages ref
         else if ref.kind == "input_package" then inputPackage ref
         else if ref.kind == "nixpkgs_package" then nixpkgsPackage ref
         else if ref.kind == "config" then lib.getAttrFromPath ref.path config
         else if ref.kind == "path" then builtins.path { path = (let p = nativeRoot + "/${ref.file}"; in if builtins.isPath p then p else builtins.unsafeDiscardStringContext p); name = baseNameOf ref.file; }  # the file alone, copied to the store as `./file` is
         else if ref.kind == "native" then lib.getAttrFromPath ref.attr (nativeValue ref)
         else if ref.kind == "priority" then lib.mkOverride ref.level (decode ref.value)
         else if ref.kind == "order" then lib.mkOrder ref.level (decode ref.value)
         else if ref.kind == "text" then lib.concatStrings (lib.imap0 (i: part: textPart i (decode part)) ref.parts)
         else throw "Unknown nixdantic reference: ${ref.kind}"
    else lib.mapAttrs (_: decode) value;
in {
  _file = input.source;
  config = assert input.version == 1; lib.setAttrByPath input.path (decode input.value);
}
