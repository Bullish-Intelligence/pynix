{ pkgs, inputs, ... }: { tool = "${pkgs.hello}/bin/hello"; marker = inputs.marker; }
