"""Generated: the packages of the package list. Do not edit."""

from builtins import str as _str

from .._pkgref import Pkg as _Pkg
from .._pkgref import Prog as _Prog

class PackageSet_nushellPlugins:
    def __getitem__(self, attr: _str) -> _Pkg: ...
    bson: _Prog
    """Nushell plugin for BSON (Binary JSON) format `from bson` and `to bson`. Runs as `nu_plugin_bson`."""
    dbus: _Prog
    """Nushell plugin for communicating with D-Bus. Runs as `nu_plugin_dbus`."""
    desktop_notifications: _Prog
    """Nushell plugin for sending desktop notifications. Runs as `nu_plugin_desktop_notifications`."""
    formats: _Prog
    """Formats plugin for Nushell. Runs as `nu_plugin_formats`."""
    gstat: _Prog
    """Git status plugin for Nushell. Runs as `nu_plugin_gstat`."""
    hcl: _Prog
    """Nushell plugin for parsing Hashicorp Configuration Language files. Runs as `nu_plugin_hcl`."""
    highlight: _Prog
    """`nushell` plugin for syntax highlighting. Runs as `nu_plugin_highlight`."""
    net: _Prog
    """Nushell plugin to list system network interfaces. Runs as `nu_plugin_net`."""
    polars: _Prog
    """Nushell dataframe plugin commands based on polars. Runs as `nu_plugin_polars`."""
    query: _Prog
    """Nushell plugin to query JSON, XML, and various web data. Runs as `nu_plugin_query`."""
    skim: _Prog
    """Nushell plugin that adds integrates the skim fuzzy finder. Runs as `nu_plugin_skim`."""
    units: _Prog
    """Nushell plugin for easily converting between common units. Runs as `nu_plugin_units`."""
