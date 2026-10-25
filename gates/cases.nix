# S9 step 3: one option per hand case, typed with the real `lib.types` of the pinned nixpkgs.
#   .manifest  the S9 extractor over the options (the generator reads it, like a real manifest)
#   .verdicts  for each case and label: does `lib.evalModules` accept the JSON text as the value of a
#              one-option module? The texts come from the file in $S9_CASE_VALUES: { CASE = { LABEL = TEXT; }; }
let
  nixpkgs = /. + builtins.getEnv "GATES_NIXPKGS";
  lib = import (nixpkgs + "/lib");
  inherit (lib) types mkOption;
  T = {
    float_t = types.float;
    number_t = types.number;
    number_between_t = types.numbers.between 0 1;
    number_nonneg_t = types.numbers.nonnegative;
    int_t = types.int;
    u8_t = types.ints.u8;
    s8_t = types.ints.s8;
    u16_port_t = types.port;
    u32_t = types.ints.u32;
    s32_t = types.ints.s32;
    positive_t = types.ints.positive;
    unsigned_t = types.ints.unsigned;
    between_neg_t = types.ints.between (-20) 19;
    bool_t = types.bool;
    enum_str_t = types.enum [ "a" "b" ];
    enum_int_t = types.enum [ 1 2 3 ];
    enum_bool_t = types.enum [ true false ];
    enum_null_t = types.enum [ null "a" ];
    enum_float_t = types.enum [ 0.5 1.5 ];
    enum_mixed_t = types.enum [ "a" 1 true ];
    match_posix_t = types.strMatching "[[:alnum:]_-]+";
    match_dot_t = types.strMatching "a.*b";
    match_upper_t = types.strMatching "(BTN|KEY)_[[:upper:][:digit:]_]+";
    match_space_t = types.strMatching "[^[:space:]]{1,64}";
    match_caret_t = types.strMatching "^[a-z]+$";
    match_bracket_t = types.strMatching "[a\\]]+";
    either_int_str_t = types.either types.int types.str;
    oneof_t = types.oneOf [ types.int types.str types.bool ];
    either_list_str_t = types.either (types.listOf types.str) types.str;
    either_int_float_t = types.either types.int types.float;
    coerced_t = types.coercedTo types.int toString types.str;
    nullor_int_t = types.nullOr types.int;
    nullor_float_t = types.nullOr types.float;
    list_str_t = types.listOf types.str;
    list_float_t = types.listOf types.float;
    attrs_int_t = types.attrsOf types.int;
    attrs_t = types.attrs;
    anything_t = types.anything;
    sub_t = types.submodule { options.a = mkOption { type = types.int; default = 1; }; options.b = mkOption { type = types.str; default = "x"; }; };
    list_sub_t = types.listOf (types.submodule { options.a = mkOption { type = types.int; default = 1; }; });
    attrs_sub_t = types.attrsOf (types.submodule { options.a = mkOption { type = types.int; default = 1; }; });
    ns_sub_t = types.attrsOf (types.submodule { options.name = mkOption { type = types.str; default = "n"; }; options.ipv4.addresses = mkOption { type = types.listOf types.str; default = [ ]; }; });
    rename_t = types.listOf (types.submodule { options.type = mkOption { type = types.str; default = "t"; }; options.match = mkOption { type = types.str; default = "m"; }; });
    unspec_t = types.unspecified;
    raw_t = types.raw;
    elixir_tuple_t = types.mkOptionType { name = "elixirTuple"; description = "elixir tuple"; check = x: (x._elixirType or "") == "tuple"; };
    elixir_raw_t = types.mkOptionType { name = "rawElixir"; description = "raw elixir"; check = x: (x._elixirType or "") == "raw"; };
    path_t = types.path;
    path_any_t = types.pathWith { };
    path_nostore_t = types.pathWith { inStore = false; };
    path_rel_t = types.pathWith { absolute = false; };
    path_instore_t = types.pathInStore;
    str_t = types.str;
    nonempty_t = types.nonEmptyStr;
    addcheck_str_t = types.addCheck types.str (s: builtins.stringLength s < 5);
    addcheck_int_t = types.addCheck types.int (x: x != 5);
    addcheck_sub_t = types.addCheck (types.attrsOf types.int) (x: x ? a);
  };
  evaluated = lib.evalModules { modules = [ { options = lib.mapAttrs (_: t: mkOption { type = t; }) T; } ]; };
  extract = import ../nix/extractor.nix { inherit lib; pool = true; deepCheck = false; };
  texts = builtins.fromJSON (builtins.readFile (builtins.getEnv "S9_CASE_VALUES"));
  verdict = id: text:
    let
      r = builtins.tryEval (builtins.deepSeq
        (lib.evalModules { modules = [ { options.v = mkOption { type = T.${id}; }; config.v = builtins.fromJSON text; } ]; }).config.v
        true);
    in r.success;
in {
  manifest = extract evaluated // { source = { nixpkgs = "e7439b6b14ad3cc35d05608ebca9bce01a25f5f8"; }; };
  verdicts = lib.mapAttrs (id: labels: lib.mapAttrs (_: verdict id) labels) texts;
}
