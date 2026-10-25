# pynix: copy of 008 S10 (the S9 extractor). One change: the three settings that S9 read from the environment
# (`S9_DEEP`, `S9_SKIP`, `S9_SUBMODULES`) are arguments (`deepCheck`, `skip`, `submodules`), so the walk is pure.
# S9: copy of the S1 extractor. Each option record also holds `values`: the default and the example value
# when it is plain JSON data (see `valueInfo`). Nix checks each plain value against the type of the option.
#
# S1: the A1b expand-once type table, plus payload data for the generator (see `payloadData`).
#
# A1b: expand-once type table.
#
# Based on the A1 extractors (evidence/A1/extractor-constructor.nix, itself a copy of
# evidence/N1/extractor.nix). The walk differs in three ways:
#
# 1. Every distinct type is a node of a graph. `builtins.genericClosure` visits each node once.
#    A node is a type; its edges are the types it refers to (`nestedTypes`, and for a submodule
#    the types of its sub-options). The closure ends on its own, so no depth limit is needed.
#    A reference to a node that is already in progress is only an ID, so cycles end.
# 2. A submodule type is expanded one time. Its entry in `types` holds its sub-option records.
#    An option holds the ID of its type. A wrapper (attrsOf, listOf, nullOr, ...) is an entry that
#    refers to the type inside it by ID (`nested`).
# 3. The key of a node is a string made from the constructor, the description, and the keys of the
#    nested types (cut at `keyDepth`), or, for a submodule, a hash of the identity of its modules
#    (see `moduleIdent`). The ID in the manifest is the position of the node in the closure.
{ lib, keyDepth ? 6, fingerprint ? true, pool ? false, deepCheck ? true, skip ? [ ], submodules ? false }:
evalResult:
let
  inherit (builtins)
    attrNames concatMap concatStringsSep elem filter foldl' genericClosure hashString head
    isAttrs isBool isFunction isInt isList isPath isString length listToAttrs mapAttrs
    substring toJSON toString tryEval unsafeGetAttrPos functionArgs deepSeq;

  tryDeep = f: tryEval (deepSeq f f);
  safe = f: let r = tryEval (deepSeq f f); in
    if r.success then { ok = true; value = r.value; }
    else { ok = false; error = "evaluation failed"; };

  # ---- type classification -------------------------------------------------------------------
  functorOf = t: t.functor or { };
  payloadOf = t: let p = (functorOf t).payload or null; in if isAttrs p then p else { };
  # The constructor key: functor.name, with type.name as fallback.
  ctorOf = t:
    let n = (functorOf t).name or "";
    in if isString n && n != "" then n else t.name or "Native";
  # A type is a submodule type when its functor payload carries a list of modules.
  isModuleType = t:
    let p = payloadOf t;
    in (p ? modules || p ? staticModules) && (t.getSubModules or null) != null;
  isOptionType = v: isAttrs v && (v._type or null) == "option-type";
  isOpt = v: isAttrs v && v ? type && isAttrs v.type;

  # The types inside a type. `attrTag` keeps options in `nestedTypes`; take their `type`.
  childType = v:
    if isOptionType v then v
    else if isOpt v && isOptionType v.type then v.type
    else null;
  kidsOf = t:
    let
      raw = t.nestedTypes or { };
      typed = mapAttrs (_: childType) (if isAttrs raw then raw else { });
    in lib.filterAttrs (_: v: v != null) typed;

  # ---- identity of a submodule type ----------------------------------------------------------
  posOf = n: v:
    let p = unsafeGetAttrPos n v;
    in if p == null then "" else "${p.file}:${toString p.line}:${toString p.column}";
  attrNamesSafe = v:
    let r = tryDeep (attrNames v); in if r.success then r.value else [ "?" ];
  # Identity of one module value. A path or string names itself. An attribute set is named by the
  # source position and the name of each of its attributes, and by the option names. A function is
  # named by its argument names only: the extractor never calls a module function, because the
  # body can fail on a made-up argument in a way that `tryEval` does not catch (observed on
  # Home Manager: `lib.hm...` on a null `lib`). The fingerprint of the sub-options separates types
  # that this identity cannot.
  modIdent = d: m:
    if isPath m then toString m
    else if isString m then m
    else if d > 3 then "deep"
    else if isFunction m then "fn(${concatStringsSep "," (attrNames (functionArgs m))})"
    else if isAttrs m then modAttrs d m
    else "?";
  modAttrs = d: v:
    let
      names = filter (n: n != "_file") (attrNamesSafe v);
      one = n:
        if n == "imports" && d == 0 then
          # Only the wrapper that the module system adds (d = 0) names its imports.
          let r = tryDeep (if isList v.imports then map (modIdent (d + 1)) v.imports else [ "?" ]);
          in "imports=[${concatStringsSep ";" (if r.success then r.value else [ "?" ])}]"
        else if n == "options" then
          "options@${posOf n v}=${toJSON (attrNamesSafe (v.options or { }))}"
        else "${n}@${posOf n v}";
      file = let f = v._file or null; in if f == null then "" else toString f;
    in "{${file}|${concatStringsSep "," (map one names)}}";
  # The file of a module for the reader of the manifest.
  modFile = m:
    if isPath m || isString m then toString m
    else if isAttrs m && (isPath (m._file or null) || isString (m._file or null)) then toString m._file
    else if isFunction m then "<function>"
    else "<module>";
  moduleIdent = t:
    let
      p = payloadOf t;
      mods = t.getSubModules;
      r = tryEval (toJSON {
        # A set, not a list: a type that holds itself (vmVariant in vmVariant) adds the same
        # module again at each level, and the list would never repeat.
        mods = lib.unique (lib.sort (a: b: a < b) (map (modIdent 0) mods));
        class = p.class or null;
        shorthand = p.shorthandOnlyDefinesConfig or null;
        specialArgs = if isAttrs (p.specialArgs or null) then attrNames p.specialArgs else [ ];
        description = if isString (p.description or null) then p.description else null;
        ctor = ctorOf t;
      });
    in if r.success then r.value else "unidentified:${ctorOf t}";

  # ---- node key ------------------------------------------------------------------------------
  # The description of a type that has nested types can recurse without end (a recursive JSON
  # type, for example), and `tryEval` does not catch that. Read a description only from a leaf type.
  descOf = t:
    if kidsOf t != { } then ""
    else
      let r = tryEval (let d = t.description or t.name or ""; in if isString d then d else "");
      in if r.success then r.value else "";
  labelOf = t:
    let
      name = t.name or "Native";
      d = descOf t;
    in if d == name || d == "" then name else "${name}|${d}";

  # ---- option records ------------------------------------------------------------------------
  flatten = prefix: tree:
    concatMap (name:
      let value = tree.${name}; path = prefix ++ [ name ];
      in if name == "_freeformOptions" then [ ]  # the freeform type expands these itself
         else if isOpt value then [ { inherit path; opt = value; } ]
         else if isAttrs value then flatten path value
         else [ ]) (attrNames tree);

  metaOf = value:
    safe {
      description = value.description or null;
      declarations = map toString (value.declarations or [ ]);
      declarationPositions = map (p: "${toString p.file}:${toString p.line}:${toString p.column}")
        (value.declarationPositions or [ ]);
      hasDefault = value ? default;
      hasDefaultText = value ? defaultText;
      defaultText = value.defaultText or null;
      readOnly = value.readOnly or false;
      visible = value.visible or true;
      internal = value.internal or false;
    };

  # ---- the closure ---------------------------------------------------------------------------
  # One `item` per place where a type occurs. The item holds its key (computed once), the items
  # of the types inside it, and, for a submodule type, the items of the types of its sub-options.
  # The key of a submodule type has two parts: the identity of its modules, and (when `fingerprint`
  # is true) a hash of its sub-option names, descriptions, and type labels. A helper that makes
  # many submodule types from one source position gives the same module identity, but not the
  # same sub-option descriptions.
  descString = d:
    if isString d then d
    else if isAttrs d && isString (d.text or null) then d.text
    else "";
  mkItem = t:
    let
      kidsT = kidsOf t;
      isMod = isModuleType t;
      self = {
        type = t;
        inherit isMod;
        kidItems = mapAttrs (_: mkItem) kidsT;
        # Sub-options of a submodule type, flattened with paths relative to the submodule.
        exp =
          let l = flatten [ ] (t.getSubOptions [ "__nixdantic_placeholder__" ]);
              r = tryEval (deepSeq (map (x: x.path) l) l);
          in r // { items = if r.success then map (x: x // { item = mkItem x.opt.type; }) r.value else [ ]; };
        fp =
          if !fingerprint then ""
          else if !self.exp.success then "err"
          else substring 0 20 (hashString "sha256" (toJSON {
            options = map (x: [
              x.path
              (descString (x.opt.description or null))
              (descString (x.opt.defaultText or null))
              (x.opt ? default)
              (x.opt.readOnly or false)
              (x.opt.visible or true)
              (x.opt.internal or false)
              (labelOf x.opt.type)
            ]) self.exp.value;
            kids = mapAttrs (_: labelOf) kidsT;
          }));
        modKey = "S:${substring 0 20 (hashString "sha256" (moduleIdent t))}:${self.fp}";
        keyD = d:
          if isMod then self.modKey
          else if kidsT == { } then labelOf t
          else if d >= keyDepth then "${labelOf t}<cut>"
          else "${labelOf t}<${concatStringsSep "," (lib.mapAttrsToList (k: i: "${k}=${i.keyD (d + 1)}") self.kidItems)}>";
        key = self.keyD 0;
      };
    in self;

  rootTree = if evalResult ? options then evalResult.options else { };
  rootRecords = map (x: x // { item = mkItem x.opt.type; }) (flatten [ ] rootTree);

  operator = item:
    (lib.attrValues item.kidItems)
    ++ (if item.isMod && item.exp.success then map (x: x.item) item.exp.items else [ ]);

  closure = genericClosure {
    startSet = map (x: x.item) rootRecords;
    inherit operator;
  };

  ids = listToAttrs (lib.imap0 (i: item: { name = item.key; value = i; }) closure);
  idOf = item: ids.${item.key};

  # ---- manifest ------------------------------------------------------------------------------
  functorSummary = t:
    let
      functor = functorOf t;
      fields = mapAttrs (key: field:
        if isFunction field then "<function>"
        else if isString field || isBool field || isInt field then field
        else if isAttrs field then { name = field.name or null; fields = attrNames field; }
        else "<structured>") functor;
    in {
      name = if functor ? name && isString functor.name then functor.name else "";
      fields = attrNames functor;
      values = fields;
    };

  # S1: plain payload data of a leaf type. A value that is not plain JSON data is left out.
  plainScalar = v: isString v || isInt v || isBool v || builtins.isFloat v || v == null;
  payloadData = t:
    let
      p = (functorOf t).payload or null;
      r = tryDeep (
        if !isAttrs p then { }
        else lib.filterAttrs (_: v: v != null) {
          values = if isList (p.values or null) && builtins.all plainScalar p.values then p.values else null;
          pattern = if isString (p.pattern or null) then p.pattern else null;
          sep = if isString (p.sep or null) then p.sep else null;
          inStore = if isBool (p.inStore or null) then p.inStore else null;
          absolute = if isBool (p.absolute or null) then p.absolute else null;
        });
    in if r.success then r.value else { };

  # ---- S9: default and example values ---------------------------------------------------------
  # A value is plain when it holds only null, bool, int, float, and string, in lists and attribute sets.
  # Any other value is skipped, and its kind is the state: path, function, derivation, `typed:NAME`
  # (a literalExpression, literalMD, mkIf, ...), outPath, too deep, eval error.
  unwrap = v: if isAttrs v && (v._type or null) == "override" then v.content else v;
  firstBad = ks: let bad = filter (k: k != "plain") ks; in if bad == [ ] then "plain" else head bad;
  kindOf = d: v:
    let t = builtins.typeOf v;
    in if elem t [ "null" "bool" "int" "float" "string" ] then "plain"
    else if t == "path" then "path"
    else if t == "lambda" then "function"
    else if d > 12 then "too deep"
    else if t == "list" then firstBad (map (kindOf (d + 1)) v)
    else if t == "set" then
      (if (v.type or null) == "derivation" then "derivation"
       else if v ? _type then "typed:${toString v._type}"
       else if v ? outPath then "outPath"
       else firstBad (map (kindOf (d + 1)) (lib.attrValues v)))
    else "other:${t}";
  # `check` is `type.check` (shallow for a container). `deep` is the full check: the module system merges
  # the value as the one definition of the option, and the result is forced (nested types included).
  # True when the type may hold a submodule (or when the walk cannot tell at depth 6). The full check forces
  # the merged value, and a submodule value holds a whole module configuration: the evaluator overflows its
  # stack on it (observed on Home Manager). So the full check runs only on types with no submodule.
  mayHoldSubmodule = d: item:
    item.isMod || (if d > 6 then true else lib.any (mayHoldSubmodule (d + 1)) (lib.attrValues item.kidItems));
  # Forces a merged value to the leaves, but not through a derivation, and not through `_module` (the module
  # arguments hold `pkgs`: `deepSeq` on a whole submodule configuration overflows the stack).
  forceSafe = d: v:
    if d > 40 then true
    else if isAttrs v then
      (if (v.type or null) == "derivation" then true
       else lib.all (n: forceSafe (d + 1) v.${n}) (filter (n: n != "_module") (attrNames v)))
    else if isList v then lib.all (forceSafe (d + 1)) v
    else builtins.seq v true;
  valueInfo = name: item: opt: raw:
    let
      # S9_SKIP: `OPTION.PATH:default` or `OPTION.PATH:example`, separated by spaces. An evaluation error that
      # `tryEval` does not catch (a failed comparison inside a custom check) stops the whole walk; the
      # option is listed here and the value counts as "check stops the evaluator".
      key = "${concatStringsSep "." opt.loc}:${name}";
      skipped = elem key skip;
      # Only examples get the forced check on a type with a submodule: a default `{}` of a submodule type would
      # force the whole nested configuration, whose options read the system `config` (observed: uncatchable errors).
      forceSub = submodules && name == "example";
      rawT = tryEval (builtins.addErrorContext "S9OPT ${key}" raw);
      v = unwrap raw;
      k = tryEval (kindOf 0 v);
      kind = if !rawT.success || !k.success then "eval error" else k.value;
      js = tryEval (deepSeq (toJSON v) (toJSON v));
      shallow = tryEval (builtins.addErrorContext "S9OPT ${key}" (opt.type.check v));
      merged = (lib.modules.mergeDefinitions opt.loc opt.type [ { file = "s9"; value = v; } ]).mergedValue;
      hasSub = mayHoldSubmodule 0 item;
      deepRun = deepCheck && (!hasSub || forceSub);
      deep = if deepRun then tryEval (builtins.addErrorContext "S9OPT ${key}" (if hasSub then forceSafe 0 merged else deepSeq merged true)) else { success = false; };
    in
    if skipped then { state = "evaluator-stop"; }
    else if kind != "plain" then { state = kind; }
    else if !js.success then { state = "eval error"; }
    else {
      state = "plain";
      json = builtins.unsafeDiscardStringContext js.value;
      ctx = builtins.hasContext js.value;
      wrapped = isAttrs raw && (raw._type or null) == "override";
      check = shallow.success && shallow.value == true;
      deep = if deepRun then (if deep.success then "ok" else "fail") else "not run";
      sub = hasSub;
    };
  valuesOf = item: opt:
    # An option with `defaultText` has a computed default (often a package, or a read of `config`).
    # Forcing it can stop the evaluation with an error that `tryEval` does not catch (a missing attribute).
    (if opt ? defaultText then { default = { state = "defaultText"; }; }
     else if opt ? default then { default = valueInfo "default" item opt opt.default; } else { })
    // (if opt ? example then { example = valueInfo "example" item opt opt.example; } else { });

  # ---- S9: the true limits of an integer type, and a probe list for float and number types ---------
  # `check` of a numeric leaf type is cheap and total on numbers. For an integer type, the search looks
  # for the least and the greatest accepted integer (the accepted set is an interval), from a seed that
  # the type accepts. `lo = null` means that the type accepts down to the least Nix integer.
  maxInt = 9223372036854775807;
  minInt = -9223372036854775807 - 1;
  midOf = a: b:
    let m = a / 2 + b / 2;
    in if m <= a then a + 1 else if m >= b then b - 1 else m;
  numericProbe = t:
    let
      ctor = ctorOf t;
      leaf = kidsOf t == { };
      acc = n: let r = tryEval (t.check n); in r.success && r.value == true;
      # The numbers of the description only seed the search; the limits come from `check`.
      inDesc = map (x: lib.toInt (head x)) (builtins.filter isList (builtins.split "(-?[0-9]+)" (descOf t)));
      seeds = [ 0 1 (-1) 10 100 1000 65535 (-20) (-128) ] ++ inDesc;
      seed = lib.findFirst acc null seeds;
      lower = a: b: if b == a + 1 then b else let m = midOf a b; in if acc m then lower a m else lower m b;
      upper = a: b: if b == a + 1 then a else let m = midOf a b; in if acc m then upper m b else upper a m;
      lo = if acc minInt then null else lower minInt seed;
      hi = if acc maxInt then null else upper seed maxInt;
      floats = [ 0.0 1.0 (-1.0) 0.5 1.5 1.0e10 ];
    in
    if !leaf then null
    else if ctor == "int" then (if seed == null then { kind = "int"; seed = null; } else { kind = "int"; inherit seed lo hi; })
    else if ctor == "float" || ctor == "number" then { kind = ctor; floats = map acc floats; ints = map acc [ 0 1 (-1) 100 ]; }
    else null;

  optionRecord = x:
    let m = metaOf x.opt;
    in {
      inherit (x) path;
      type = idOf x.item;
      metadata = if m.ok then m.value else { error = m.error; };
      error = !m.ok;
      values = valuesOf x.item x.opt;
    };

  entryOf = i: item:
    let
      t = item.type;
      kids = kidsOf t;
      base = {
        id = i;
        name = t.name or "Native";
        ctor = ctorOf t;
        description = descOf t;
        functor = functorSummary t;
        nested = mapAttrs (_: idOf) item.kidItems;
        # Types inside this type that give it sub-options: the ID to follow to find them.
        expandsTo = lib.mapAttrsToList (_: idOf)
          (lib.filterAttrs (k: _: (kids.${k}.getSubModules or null) != null) item.kidItems);
        # S1: the payload data that the Python generator needs (enum values, the pattern of
        # strMatching, the separator of separatedString, the path flags). Plain data only.
        payload = payloadData t;
        # S9: the true limits of a numeric leaf type, found by calls of its own `check`.
        numeric = numericProbe t;
      };
    in
    if item.isMod then
      base // {
        submodule = true;
        freeform = kids ? freeformType;
        modules = let r = tryDeep (map modFile t.getSubModules);
                  in if r.success then r.value else [ ];
        expandError = !item.exp.success;
        options = if item.exp.success then map optionRecord item.exp.items else [ ];
      }
    else base // { submodule = false; };

  entries = lib.imap0 entryOf closure;
  rootOptions = map optionRecord rootRecords;

  # ---- optional pool of option records -------------------------------------------------------
  # Two submodule types that hold the same options (the root of NixOS and `vmVariant`, for
  # example) write the same option records. With `pool = true` each distinct record is written
  # once in `optionPool`, and `options` lists indexes into the pool.
  poolKey = r: hashString "sha256" (toJSON r);
  withKey = r: { key = poolKey r; record = r; };
  keyedRoots = map withKey rootOptions;
  keyedEntryOptions = map (e: map withKey (e.options or [ ])) entries;
  poolItems = genericClosure {
    startSet = keyedRoots ++ lib.concatLists keyedEntryOptions;
    operator = _: [ ];
  };
  poolIds = listToAttrs (lib.imap0 (i: it: { name = it.key; value = i; }) poolItems);
  pooledEntries = lib.zipListsWith (e: keyed: if e ? options then e // { options = map (k: poolIds.${k.key}) keyed; } else e)
    entries keyedEntryOptions;
in {
  format = if pool then "nixdantic-option-manifest-v4-type-table-once-pool" else "nixdantic-option-manifest-v4-type-table-once";
  count = length rootRecords;
  typeCount = length closure;
  types = if pool then pooledEntries else entries;
  options = if pool then map (k: poolIds.${k.key}) keyedRoots else rootOptions;
} // (if pool then { optionPool = map (it: it.record) poolItems; } else { })
