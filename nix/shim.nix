# pynix: copy of 008 S10. Unchanged below this line.
# A1b: compatibility shim for one defect of the pinned nixpkgs.
# `nixos/modules/services/misc/autorandr.nix` (matrixOf) calls `lib.types.elemTypeFunctor`.
# That attribute does not exist at the pin, and `builtins.tryEval` cannot catch the error
# ("attribute 'elemTypeFunctor' missing"). Reading `functor` of that type ends the whole walk.
# This file adds the helper with the same body as the local `elemTypeFunctor` of lib/types.nix.
lib:
lib.extend (final: prev: {
  types = prev.types // {
    elemTypeFunctor = name: { elemType, ... }@payload: {
      inherit name payload;
      type = final.types.${name};
      binOp = a: b:
        let merged = a.elemType.typeMerge b.elemType.functor;
        in if merged == null then null else { elemType = merged; };
    };
  };
})
