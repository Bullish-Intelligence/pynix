# nix-unit tests of the S8 decoder (the reference kind "text"), and of the old kinds that it must keep.
# Run: nix-unit --impure --expr 'import ./unit/tests.nix {}'   (from the S8 directory)
# Copy of 008 S10 `unit/tests.nix` (S8). The decoder under test is a parameter: env NIXDANTIC_DECODER (an absolute
# path; `run_gates.sh` sets it to `src/decoder.nix`). The nixpkgs source is env GATES_NIXPKGS (the lock of the
# repository). The S1 decoder copy is `decoder-s1.nix`.
{ decoder ? /. + builtins.getEnv "NIXDANTIC_DECODER"
, oldDecoder ? ./decoder-s1.nix }:
let
  pkgs = import (/. + builtins.getEnv "GATES_NIXPKGS") { system = "x86_64-linux"; };
  lib = pkgs.lib;
  decodeWith = d: fragment: import d { inherit fragment; nativeRoot = ./.; };
  evalValue = d: type: source: value: lib.evalModules {
    specialArgs = { inherit pkgs; inputs = { marker = "input-marker"; }; };
    modules = [
      {
        options.fixture.value = lib.mkOption { inherit type; };
        options.fixture.count = lib.mkOption { type = lib.types.int; default = 7; };
        options.networking.hostName = lib.mkOption { type = lib.types.str; default = "n2"; };
      }
      (decodeWith d {
        version = 1;
        inherit source;
        path = [ "fixture" "value" ];
        inherit value;
      })
    ];
  };
  ref = r: { __nixdantic_ref__ = r; };
  package = attr: ref { kind = "package"; inherit attr; };
  text = parts: ref { kind = "text"; inherit parts; };
  run = type: source: value: (evalValue decoder type source value).config.fixture.value;
  str = lib.types.str;
  hello = text [ (package "hello") "/bin/hello" ];
  helloValue = run str "test.py:1 (Hello)" hello;
  anything = lib.types.attrsOf lib.types.anything;
in {
  "test: text decodes to the store path of the package, then the literal" = {
    expr = helloValue;
    expected = "${pkgs.hello}/bin/hello";
  };
  "test: text value starts with the store directory and ends with the literal" = {
    expr = lib.hasPrefix "/nix/store/" helloValue && lib.hasSuffix "-hello-${pkgs.hello.version}/bin/hello" helloValue;
    expected = true;
  };
  "test: text keeps the string context" = {
    expr = builtins.hasContext helloValue;
    expected = true;
  };
  "test: the context names the derivation of the package" = {
    expr = builtins.attrNames (builtins.getContext helloValue);
    expected = [ pkgs.hello.drvPath ];
  };
  "test: the context asks for the output of the package" = {
    expr = (builtins.getContext helloValue).${builtins.unsafeDiscardStringContext pkgs.hello.drvPath}.outputs;
    expected = [ "out" ];
  };
  "test: a text of literals only has no context" = {
    expr = builtins.hasContext (run str "test.py:2" (text [ "echo " "hi" ]));
    expected = false;
  };
  "test: a string part is literal, so dollar-brace in it stays text and gains no context" = {
    expr = let v = run str "test.py:3" (text [ "echo \${pkgs.hello} \${HOME}" ]); in [ v (builtins.hasContext v) ];
    expected = [ "echo \${pkgs.hello} \${HOME}" false ];
  };
  "test: a literal string with the tag name is data in a part" = {
    expr = run str "test.py:4" (text [ "__nixdantic_ref__" ]);
    expected = "__nixdantic_ref__";
  };
  "test: a literal attribute set in a free-form value stays data" = {
    expr = (run anything "test.py:5" { __nixdantic_literal__ = ref { kind = "text"; parts = [ "x" ]; }; }).__nixdantic_ref__;
    expected = { kind = "text"; parts = [ "x" ]; };
  };
  "test: text with a package, an argument, and a second package" = {
    expr = run str "test.py:6" (text [ (package "hello") "/bin/hello --path " (package "coreutils") "/bin" ]);
    expected = "${pkgs.hello}/bin/hello --path ${pkgs.coreutils}/bin";
  };
  "test: the context of a text with two packages holds both derivations" = {
    expr = builtins.attrNames (builtins.getContext (run str "test.py:6" (text [ (package "hello") " " (package "coreutils") ])));
    expected = lib.sort (a: b: a < b) [ pkgs.hello.drvPath pkgs.coreutils.drvPath ];
  };
  "test: a nested text works" = {
    expr = run str "test.py:7" (text [ "a=" (text [ (package "hello") "/bin" ]) ]);
    expected = "a=${pkgs.hello}/bin";
  };
  "test: a config reference is a part" = {
    expr = run str "test.py:8" (text [ "host=" (ref { kind = "config"; path = [ "networking" "hostName" ]; }) ]);
    expected = "host=n2";
  };
  "test: a native reference is a part" = {
    expr = run str "test.py:9" (text [ "user=" (ref { kind = "native"; file = "native.nix"; attr = [ "user" ]; }) ]);
    expected = "user=native-user";
  };
  "test: a native file that is a function gets pkgs and inputs" = {
    expr = run anything "test.py:9"
      { tool = ref { kind = "native"; file = "native-fn.nix"; attr = [ "tool" ]; };
        marker = ref { kind = "native"; file = "native-fn.nix"; attr = [ "marker" ]; }; };
    expected = { tool = "${pkgs.hello}/bin/hello"; marker = "input-marker"; };
  };
  # PF-8: a reference with an empty `attr` takes the whole value. A function that names no argument stays a function.
  "test: a whole-value overlay final: prev: stays a function and works in an overlay list" = {
    expr =
      let
        overlayType = lib.types.listOf (lib.mkOptionType { name = "overlay"; check = lib.isFunction; merge = lib.mergeOneOption; });
        overlays = run overlayType "test.py:9" [ (ref { kind = "native"; file = "overlay.nix"; attr = [ ]; }) ];
      in (builtins.head overlays) { } { };
    expected = { marker = "overlay-marker"; };
  };
  "test: a whole-value file that names an argument gets the module arguments" = {
    expr = run lib.types.raw "test.py:9" (ref { kind = "native"; file = "native-whole-fn.nix"; attr = [ ]; });
    expected = { tool = "${pkgs.hello}/bin/hello"; };
  };
  "test: a whole-value attribute set file stays as it is" = {
    expr = run lib.types.raw "test.py:9" (ref { kind = "native"; file = "native.nix"; attr = [ ]; });
    expected = { user = "native-user"; };
  };
  "test: a whole-value file { ... }: names no argument and stays a function (the edge)" = {
    expr = builtins.isFunction (run lib.types.raw "test.py:9" (ref { kind = "native"; file = "native-bare.nix"; attr = [ ]; }));
    expected = true;
  };
  "test: a file { ... }: with an attribute path is called" = {
    expr = run str "test.py:9" (ref { kind = "native"; file = "native-bare.nix"; attr = [ "bare" ]; });
    expected = "bare";
  };
  "test: text inside free-form data resolves at depth, and the context stays" = {
    expr =
      let v = run anything "test.py:10" { ExecStart = hello; Type = "oneshot"; Nest.List = [ hello ]; };
      in [ v.ExecStart (v.Type) (builtins.hasContext v.ExecStart) (builtins.hasContext (builtins.head v.Nest.List)) ];
    expected = [ "${pkgs.hello}/bin/hello" "oneshot" true true ];
  };
  "test: text is a valid value of the option type path" = {
    expr = run lib.types.path "test.py:11" hello;
    expected = "${pkgs.hello}/bin/hello";
  };
  "test: the old package reference still decodes" = {
    expr = (run lib.types.package "test.py:12" (package "git")).drvPath;
    expected = pkgs.git.drvPath;
  };
  "test: the old config reference still decodes" = {
    expr = run str "test.py:13" (ref { kind = "config"; path = [ "networking" "hostName" ]; });
    expected = "n2";
  };
  "test: an unknown package in a text names the line and the attribute" = {
    expr = run str "test.py:14 (Hello)" (text [ (package "hellp") "/bin/hello" ]);
    expectedError = { type = "ThrownError"; msg = "nixdantic: test.py:14 \\(Hello\\): unknown package `hellp`: pkgs has no attribute `hellp`"; };
  };
  "test: an unknown package reference alone names the line and the attribute" = {
    expr = (run lib.types.package "test.py:15 (Hello)" (package "hellp")).drvPath;
    expectedError = { type = "ThrownError"; msg = "nixdantic: test.py:15 \\(Hello\\): unknown package `hellp`"; };
  };
  "test: a text part that is an integer fails with the position" = {
    expr = run str "test.py:16 (Hello)" (text [ "n=" (ref { kind = "config"; path = [ "fixture" "count" ]; }) ]);
    expectedError = { type = "ThrownError"; msg = "nixdantic: test.py:16 \\(Hello\\): part 1 of a text has type int, not a string or a path"; };
  };
  "test: the S1 decoder refuses the kind text with a clear message" = {
    expr = (evalValue oldDecoder str "test.py:17" hello).config.fixture.value;
    expectedError = { type = "ThrownError"; msg = "Unknown nixdantic reference: text"; };
  };
  "test: the S1 decoder and the S8 decoder agree on a fragment with no text" = {
    expr = (evalValue oldDecoder lib.types.package "test.py:18" (package "git")).config.fixture.value.drvPath;
    expected = (run lib.types.package "test.py:18" (package "git")).drvPath;
  };
}
