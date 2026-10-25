# A tiny flake input for the tests of `nix/input-packages.nix`. It has no inputs, so it evaluates offline.
{
  description = "pynix test fixture: one NixOS module, one Home Manager module, two packages";

  outputs =
    { self }:
    let
      # A package without nixpkgs: a plain derivation with `meta` set by hand.
      mkPackage =
        name: meta:
        (derivation {
          inherit name;
          system = "x86_64-linux";
          builder = "/bin/sh";
          args = [ "-c" "echo ${name} > $out" ];
        })
        // {
          inherit meta;
        };
    in
    {
      # A path module: its options are declared in a file below the store path of the input.
      nixosModules.fixture = ./nixos.nix;
      nixosModules.default = self.nixosModules.fixture;
      # A function value: the module system has no file for it, so the position of the option names the file.
      nixosModules.inline =
        { lib, ... }:
        {
          options.services.fixtureInline.enable = lib.mkEnableOption "the inline fixture";
        };
      homeManagerModules.fixture = ./home.nix;

      packages.x86_64-linux = {
        fixture = mkPackage "fixture" {
          description = "The fixture program";
          mainProgram = "fixture";
        };
        # No main program and no description.
        fixture-data = mkPackage "fixture-data" { };
        # Not a derivation: the name list leaves it out.
        notes = "text";
      };
    };
}
