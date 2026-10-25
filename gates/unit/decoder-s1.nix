# Each fragment enters lib.evalModules as one independent module.
{ fragment, nativeRoot ? ./. }:
{ lib, config, pkgs, ... }:
let
  input = if builtins.isPath fragment then builtins.fromJSON (builtins.readFile fragment) else fragment;
  decode = value:
    if builtins.isList value then map decode value
    else if !builtins.isAttrs value then value
    else if value ? __nixdantic_literal__ then lib.mapAttrs (_: decode) value.__nixdantic_literal__
    else if value ? __nixdantic_ref__ then
      let ref = value.__nixdantic_ref__;
      in if ref.kind == "package" then lib.getAttrFromPath (lib.splitString "." ref.attr) pkgs
         else if ref.kind == "config" then lib.getAttrFromPath ref.path config
         else if ref.kind == "native" then lib.getAttrFromPath ref.attr (import (nativeRoot + "/${ref.file}"))
         else throw "Unknown nixdantic reference: ${ref.kind}"
    else lib.mapAttrs (_: decode) value;
in {
  _file = input.source;
  config = assert input.version == 1; lib.setAttrByPath input.path (decode input.value);
}
