# The Home Manager module of the fixture. Its default reads a base option (`config.xdg.dataHome`).
{ config, lib, ... }:
{
  options.programs.fixture = {
    enable = lib.mkEnableOption "the fixture program";
    dataDir = lib.mkOption {
      type = lib.types.str;
      default = "${config.xdg.dataHome}/fixture";
      description = "Where the program keeps its data.";
    };
    theme = lib.mkOption {
      type = lib.types.enum [ "light" "dark" ];
      default = "dark";
      description = "The colour theme.";
    };
  };
}
