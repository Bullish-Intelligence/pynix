# The NixOS module of the fixture: `services.fixture.{enable,port,settings}`. The `config` part writes a base option.
{ config, lib, ... }:
let
  cfg = config.services.fixture;
in
{
  options.services.fixture = {
    enable = lib.mkEnableOption "the fixture service";
    port = lib.mkOption {
      type = lib.types.port;
      default = 8080;
      description = "The port of the fixture service.";
    };
    settings = lib.mkOption {
      type = lib.types.submodule {
        freeformType = lib.types.attrsOf lib.types.str;
        options.level = lib.mkOption {
          type = lib.types.enum [ "low" "high" ];
          default = "low";
          description = "How much the service logs.";
        };
      };
      default = { };
      description = "Settings of the fixture service.";
    };
  };

  config = lib.mkIf cfg.enable {
    systemd.services.fixture.serviceConfig.ExecStart = "fixture --port ${toString cfg.port}";
  };
}
