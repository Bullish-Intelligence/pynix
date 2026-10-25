"""Every class of pynix_hm in one flat namespace. Generated; do not edit.

`from pynix_hm import all as nixos`, then `nixos.Loader(efi=nixos.Loader_Efi(...))`. Python loads the module of a name at its first use.
"""

from importlib import import_module as _import_module
from typing import TYPE_CHECKING as _TYPE_CHECKING, Any as _Any

if _TYPE_CHECKING:  # the type checker reads these lines; Python skips them
    from pynix_hm.accounts.calendar import (
        Calendar as Calendar,
        Calendar_Accounts_Value as Calendar_Accounts_Value,
        Calendar_Accounts_Value_Local as Calendar_Accounts_Value_Local,
        Calendar_Accounts_Value_Remote as Calendar_Accounts_Value_Remote,
        Calendar_Accounts_Value_VdirsyncerTimeRange as Calendar_Accounts_Value_VdirsyncerTimeRange,
    )
    from pynix_hm.accounts.contact import (
        Contact as Contact,
        Contact_Accounts_Value as Contact_Accounts_Value,
        Contact_Accounts_Value_Local as Contact_Accounts_Value_Local,
        Contact_Accounts_Value_Remote as Contact_Accounts_Value_Remote,
        Contact_Accounts_Value_VdirsyncerTimeRange as Contact_Accounts_Value_VdirsyncerTimeRange,
    )
    from pynix_hm.accounts.email import (
        Email as Email,
        Email_Accounts_Value as Email_Accounts_Value,
        Email_Accounts_Value_AercImapOauth2Params as Email_Accounts_Value_AercImapOauth2Params,
        Email_Accounts_Value_Aliases_Item_Or as Email_Accounts_Value_Aliases_Item_Or,
        Email_Accounts_Value_Aliases_Item_Or_Gpg as Email_Accounts_Value_Aliases_Item_Or_Gpg,
        Email_Accounts_Value_Aliases_Item_Or_Signature as Email_Accounts_Value_Aliases_Item_Or_Signature,
        Email_Accounts_Value_Aliases_Item_Or_Smtp as Email_Accounts_Value_Aliases_Item_Or_Smtp,
        Email_Accounts_Value_Aliases_Item_Or_Smtp_Tls as Email_Accounts_Value_Aliases_Item_Or_Smtp_Tls,
        Email_Accounts_Value_Ews as Email_Accounts_Value_Ews,
        Email_Accounts_Value_Ews_Tls as Email_Accounts_Value_Ews_Tls,
        Email_Accounts_Value_Folders as Email_Accounts_Value_Folders,
        Email_Accounts_Value_Gpg as Email_Accounts_Value_Gpg,
        Email_Accounts_Value_HimalayaSettings as Email_Accounts_Value_HimalayaSettings,
        Email_Accounts_Value_Imap as Email_Accounts_Value_Imap,
        Email_Accounts_Value_Jmap as Email_Accounts_Value_Jmap,
        Email_Accounts_Value_LieerSettings as Email_Accounts_Value_LieerSettings,
        Email_Accounts_Value_Maildir as Email_Accounts_Value_Maildir,
        Email_Accounts_Value_MbsyncGroups_Value as Email_Accounts_Value_MbsyncGroups_Value,
        Email_Accounts_Value_MbsyncGroups_Value_Channels_Value as Email_Accounts_Value_MbsyncGroups_Value_Channels_Value,
        Email_Accounts_Value_MeliSettings as Email_Accounts_Value_MeliSettings,
        Email_Accounts_Value_MujmapSettings as Email_Accounts_Value_MujmapSettings,
        Email_Accounts_Value_MujmapSettings_Tags as Email_Accounts_Value_MujmapSettings_Tags,
        Email_Accounts_Value_NeomuttExtraMailboxes_Item_Or as Email_Accounts_Value_NeomuttExtraMailboxes_Item_Or,
        Email_Accounts_Value_NotmuchNeomuttVirtualMailboxes_Item as Email_Accounts_Value_NotmuchNeomuttVirtualMailboxes_Item,
        Email_Accounts_Value_Signature as Email_Accounts_Value_Signature,
        Email_Accounts_Value_Smtp as Email_Accounts_Value_Smtp,
        Email_Accounts_Value_ThunderbirdMessageFilters_Item as Email_Accounts_Value_ThunderbirdMessageFilters_Item,
    )
    from pynix_hm.dbus.__options__ import Dbus as Dbus
    from pynix_hm.dconf.__options__ import Dconf as Dconf
    from pynix_hm.editorconfig.__options__ import Editorconfig as Editorconfig
    from pynix_hm.fonts.fontconfig import (
        Fontconfig as Fontconfig,
        Fontconfig_ConfigFile_Value as Fontconfig_ConfigFile_Value,
        Fontconfig_DefaultFonts as Fontconfig_DefaultFonts,
    )
    from pynix_hm.gtk.__options__ import (
        Gtk as Gtk,
        Gtk_CursorTheme as Gtk_CursorTheme,
        Gtk_Font as Gtk_Font,
        Gtk_IconTheme as Gtk_IconTheme,
        Gtk_Theme as Gtk_Theme,
    )
    from pynix_hm.gtk.gtk2 import (
        Gtk2 as Gtk2,
        Gtk2_CursorTheme as Gtk2_CursorTheme,
        Gtk2_Font as Gtk2_Font,
        Gtk2_IconTheme as Gtk2_IconTheme,
        Gtk2_Theme as Gtk2_Theme,
    )
    from pynix_hm.gtk.gtk3 import (
        Gtk3 as Gtk3,
        Gtk3_CursorTheme as Gtk3_CursorTheme,
        Gtk3_Font as Gtk3_Font,
        Gtk3_IconTheme as Gtk3_IconTheme,
        Gtk3_Theme as Gtk3_Theme,
    )
    from pynix_hm.gtk.gtk4 import (
        Gtk4 as Gtk4,
        Gtk4_CursorTheme as Gtk4_CursorTheme,
        Gtk4_Font as Gtk4_Font,
        Gtk4_IconTheme as Gtk4_IconTheme,
        Gtk4_Theme as Gtk4_Theme,
    )
    from pynix_hm.home.__options__ import (
        Home as Home,
        Home_File_Value as Home_File_Value,
        Home_Keyboard as Home_Keyboard,
        Home_Language as Home_Language,
        Home_PointerCursor as Home_PointerCursor,
        Home_Services_Value as Home_Services_Value,
        Home_Services_Value_ConfigData_Value as Home_Services_Value_ConfigData_Value,
        Home_Services_Value_NotificationProtocol as Home_Services_Value_NotificationProtocol,
        Home_Services_Value_Services_Value as Home_Services_Value_Services_Value,
        Home_Services_Value_SystemdService as Home_Services_Value_SystemdService,
        Home_Services_Value_SystemdServices_Value as Home_Services_Value_SystemdServices_Value,
    )
    from pynix_hm.home.internal import Internal as Internal
    from pynix_hm.home.shell import Shell as Shell
    from pynix_hm.home.version import Version as Version
    from pynix_hm.i18n.__options__ import I18n as I18n
    from pynix_hm.launchd.__options__ import (
        Launchd as Launchd,
        Launchd_Agents_Value as Launchd_Agents_Value,
        Launchd_Agents_Value_Config as Launchd_Agents_Value_Config,
        Launchd_Agents_Value_Config_HardResourceLimits as Launchd_Agents_Value_Config_HardResourceLimits,
        Launchd_Agents_Value_Config_InetdCompatibility as Launchd_Agents_Value_Config_InetdCompatibility,
        Launchd_Agents_Value_Config_KeepAlive_Or as Launchd_Agents_Value_Config_KeepAlive_Or,
        Launchd_Agents_Value_Config_MachServices_Value_Or as Launchd_Agents_Value_Config_MachServices_Value_Or,
        Launchd_Agents_Value_Config_Sockets_Value as Launchd_Agents_Value_Config_Sockets_Value,
        Launchd_Agents_Value_Config_SoftResourceLimits as Launchd_Agents_Value_Config_SoftResourceLimits,
        Launchd_Agents_Value_Config_StartCalendarInterval as Launchd_Agents_Value_Config_StartCalendarInterval,
    )
    from pynix_hm.manual.html import Html as Html
    from pynix_hm.manual.json_ import Json as Manual_Json
    from pynix_hm.manual.manpages import Manpages as Manpages
    from pynix_hm.meta.__options__ import Meta as Meta
    from pynix_hm.mozilla.__options__ import Mozilla as Mozilla
    from pynix_hm.news.__options__ import News as News, News_Entries_Item as News_Entries_Item
    from pynix_hm.news.json_ import Json as News_Json
    from pynix_hm.nix.__options__ import (
        Nix as Nix,
        Nix_BuildMachines_Item as Nix_BuildMachines_Item,
        Nix_Registry_Value as Nix_Registry_Value,
        Nix_Settings as Nix_Settings,
    )
    from pynix_hm.nix.gc import Gc as Gc
    from pynix_hm.nixpkgs.__options__ import Nixpkgs as Nixpkgs
    from pynix_hm.pam.__options__ import Pam as Pam
    from pynix_hm.pam.yubico import Yubico as Yubico, Yubico_AuthorizedYubiKeys as Yubico_AuthorizedYubiKeys
    from pynix_hm.programs.abaddon import Abaddon as Abaddon
    from pynix_hm.programs.abook import Abook as Abook
    from pynix_hm.programs.acd_cli import AcdCli as AcdCli
    from pynix_hm.programs.aerc import Aerc as Aerc
    from pynix_hm.programs.aerospace import Aerospace as Aerospace, Aerospace_Launchd as Aerospace_Launchd
    from pynix_hm.programs.afew import Afew as Afew
    from pynix_hm.programs.ahoviewer import Ahoviewer as Ahoviewer
    from pynix_hm.programs.aiac import Aiac as Aiac
    from pynix_hm.programs.aichat import Aichat as Aichat
    from pynix_hm.programs.aider_chat import AiderChat as AiderChat
    from pynix_hm.programs.airlift import Airlift as Airlift
    from pynix_hm.programs.alacritty import Alacritty as Alacritty
    from pynix_hm.programs.algia import Algia as Algia
    from pynix_hm.programs.aliae import Aliae as Aliae
    from pynix_hm.programs.alistral import Alistral as Alistral
    from pynix_hm.programs.alot import Alot as Alot, Alot_Bindings as Alot_Bindings, Alot_Tags_Value as Alot_Tags_Value
    from pynix_hm.programs.am2rlauncher import Am2rlauncher as Am2rlauncher
    from pynix_hm.programs.amber import Amber as Amber
    from pynix_hm.programs.amfora import Amfora as Amfora
    from pynix_hm.programs.amoco import Amoco as Amoco
    from pynix_hm.programs.amp import Amp as Amp
    from pynix_hm.programs.andcli import Andcli as Andcli
    from pynix_hm.programs.anime_downloader import AnimeDownloader as AnimeDownloader
    from pynix_hm.programs.anki import (
        Anki as Anki,
        Anki_AnswerKeys_Item as Anki_AnswerKeys_Item,
        Anki_Profiles_Value as Anki_Profiles_Value,
    )
    from pynix_hm.programs.antigravity import (
        Antigravity as Antigravity,
        Antigravity_Profiles_Value as Antigravity_Profiles_Value,
        Antigravity_Profiles_Value_Keybindings_Or_Item as Antigravity_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.antigravity_cli import (
        AntigravityCli as AntigravityCli,
        AntigravityCli_Commands_Value as AntigravityCli_Commands_Value,
        AntigravityCli_Permissions as AntigravityCli_Permissions,
    )
    from pynix_hm.programs.anup import Anup as Anup
    from pynix_hm.programs.anvil_editor import AnvilEditor as AnvilEditor
    from pynix_hm.programs.anyrun import (
        Anyrun as Anyrun,
        Anyrun_Config as Anyrun_Config,
        Anyrun_Config_Height as Anyrun_Config_Height,
        Anyrun_Config_Keybinds_Item as Anyrun_Config_Keybinds_Item,
        Anyrun_Daemon as Anyrun_Daemon,
    )
    from pynix_hm.programs.aperture import Aperture as Aperture
    from pynix_hm.programs.aphorme import Aphorme as Aphorme
    from pynix_hm.programs.aria2 import Aria2 as Aria2, Aria2_Systemd as Aria2_Systemd
    from pynix_hm.programs.aria2p import Aria2p as Aria2p
    from pynix_hm.programs.asciinema import Asciinema as Asciinema
    from pynix_hm.programs.ashell import Ashell as Ashell, Ashell_Systemd as Ashell_Systemd
    from pynix_hm.programs.astroid import Astroid as Astroid
    from pynix_hm.programs.atool import Atool as Atool
    from pynix_hm.programs.attic_client import AtticClient as AtticClient
    from pynix_hm.programs.atuin import Atuin as Atuin, Atuin_Daemon as Atuin_Daemon
    from pynix_hm.programs.autojump import Autojump as Autojump
    from pynix_hm.programs.autorandr import (
        Autorandr_Hooks as Autorandr_Hooks,
        Autorandr_Profiles_Value as Autorandr_Profiles_Value,
        Autorandr_Profiles_Value_Config_Value as Autorandr_Profiles_Value_Config_Value,
        Autorandr_Profiles_Value_Config_Value_Scale as Autorandr_Profiles_Value_Config_Value_Scale,
        Autorandr_Profiles_Value_Hooks as Autorandr_Profiles_Value_Hooks,
        Autorandr as Programs_Autorandr,
    )
    from pynix_hm.programs.awscli import (
        Awscli as Awscli,
        Awscli_Credentials as Awscli_Credentials,
        Awscli_Settings as Awscli_Settings,
    )
    from pynix_hm.programs.b4 import B4 as B4, B4_AgentReview as B4_AgentReview
    from pynix_hm.programs.bacon import Bacon as Bacon
    from pynix_hm.programs.bash import Bash as Bash
    from pynix_hm.programs.bashmount import Bashmount as Bashmount
    from pynix_hm.programs.bat import (
        Bat as Bat,
        Bat_Syntaxes_Value_Or as Bat_Syntaxes_Value_Or,
        Bat_Themes_Value_Or as Bat_Themes_Value_Or,
    )
    from pynix_hm.programs.beets import Beets as Beets, Beets_MpdIntegration as Beets_MpdIntegration
    from pynix_hm.programs.bemenu import Bemenu as Bemenu
    from pynix_hm.programs.bluetuith import Bluetuith as Bluetuith
    from pynix_hm.programs.borgmatic import (
        Borgmatic_Backups_Value as Borgmatic_Backups_Value,
        Borgmatic_Backups_Value_ConsistencyChecks_Item as Borgmatic_Backups_Value_ConsistencyChecks_Item,
        Borgmatic_Backups_Value_LocationRepositories_Item_Or as Borgmatic_Backups_Value_LocationRepositories_Item_Or,
        Borgmatic_Backups_Value_Settings as Borgmatic_Backups_Value_Settings,
        Borgmatic as Programs_Borgmatic,
    )
    from pynix_hm.programs.bottom import Bottom as Bottom
    from pynix_hm.programs.boxxy import Boxxy as Boxxy, Boxxy_Rules_Item as Boxxy_Rules_Item
    from pynix_hm.programs.brave import Brave as Brave, Brave_Extensions_Item as Brave_Extensions_Item
    from pynix_hm.programs.brave_origin import (
        BraveOrigin as BraveOrigin,
        BraveOrigin_Extensions_Item as BraveOrigin_Extensions_Item,
    )
    from pynix_hm.programs.broot import Broot as Broot, Broot_Settings as Broot_Settings
    from pynix_hm.programs.browserpass import Browserpass as Browserpass
    from pynix_hm.programs.btop import Btop as Btop
    from pynix_hm.programs.bun import Bun as Bun
    from pynix_hm.programs.calibre import Calibre as Calibre
    from pynix_hm.programs.carapace import Carapace as Carapace
    from pynix_hm.programs.cargo import Cargo as Cargo
    from pynix_hm.programs.cava import Cava as Cava
    from pynix_hm.programs.cavalier import Cavalier as Cavalier, Cavalier_Settings as Cavalier_Settings
    from pynix_hm.programs.chawan import Chawan as Chawan
    from pynix_hm.programs.chromium import Chromium as Chromium, Chromium_Extensions_Item as Chromium_Extensions_Item
    from pynix_hm.programs.claude_code import ClaudeCode as ClaudeCode
    from pynix_hm.programs.clock_rs import ClockRs as ClockRs
    from pynix_hm.programs.cmus import Cmus as Cmus
    from pynix_hm.programs.codex import Codex as Codex
    from pynix_hm.programs.command_not_found import CommandNotFound as CommandNotFound
    from pynix_hm.programs.comodoro import Comodoro_Settings as Comodoro_Settings, Comodoro as Programs_Comodoro
    from pynix_hm.programs.concord import (
        Concord as Concord,
        Concord_KeymapSettings as Concord_KeymapSettings,
        Concord_Settings as Concord_Settings,
        Concord_ThemeSettings as Concord_ThemeSettings,
    )
    from pynix_hm.programs.crush import Crush as Crush
    from pynix_hm.programs.cudatext import Cudatext as Cudatext
    from pynix_hm.programs.cursor import (
        Cursor as Cursor,
        Cursor_Profiles_Value as Cursor_Profiles_Value,
        Cursor_Profiles_Value_Keybindings_Or_Item as Cursor_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.darcs import Darcs as Darcs
    from pynix_hm.programs.dbeaver import Dbeaver as Dbeaver
    from pynix_hm.programs.delta import Delta as Delta
    from pynix_hm.programs.desktoppr import Desktoppr as Desktoppr, Desktoppr_Settings as Desktoppr_Settings
    from pynix_hm.programs.devenv import Devenv as Devenv
    from pynix_hm.programs.diff_highlight import DiffHighlight as DiffHighlight
    from pynix_hm.programs.diff_so_fancy import DiffSoFancy as DiffSoFancy
    from pynix_hm.programs.difftastic import (
        Difftastic as Difftastic,
        Difftastic_Git as Difftastic_Git,
        Difftastic_Jujutsu as Difftastic_Jujutsu,
    )
    from pynix_hm.programs.dircolors import Dircolors as Dircolors
    from pynix_hm.programs.direnv import (
        Direnv as Direnv,
        Direnv_Mise as Direnv_Mise,
        Direnv_NixDirenv as Direnv_NixDirenv,
    )
    from pynix_hm.programs.discocss import Discocss as Discocss
    from pynix_hm.programs.discord import Discord as Discord, Discord_Settings as Discord_Settings
    from pynix_hm.programs.distrobox import Distrobox as Distrobox
    from pynix_hm.programs.docker_cli import (
        DockerCli as DockerCli,
        DockerCli_Contexts_Value as DockerCli_Contexts_Value,
    )
    from pynix_hm.programs.dprint import Dprint as Dprint
    from pynix_hm.programs.earthly import Earthly as Earthly
    from pynix_hm.programs.ec import Ec as Ec
    from pynix_hm.programs.eclipse import Eclipse as Eclipse
    from pynix_hm.programs.eilmeldung import Eilmeldung as Eilmeldung
    from pynix_hm.programs.element_desktop import ElementDesktop as ElementDesktop
    from pynix_hm.programs.emacs import Emacs as Programs_Emacs
    from pynix_hm.programs.equibop import Equibop as Equibop, Equibop_Equicord as Equibop_Equicord
    from pynix_hm.programs.eww import Eww as Eww, Eww_Systemd as Eww_Systemd
    from pynix_hm.programs.eza import Eza as Eza
    from pynix_hm.programs.fabric_ai import FabricAi as FabricAi
    from pynix_hm.programs.fastfetch import Fastfetch as Fastfetch
    from pynix_hm.programs.fd import Fd as Fd
    from pynix_hm.programs.feedr import Feedr as Feedr
    from pynix_hm.programs.feh import Feh as Feh
    from pynix_hm.programs.firefox import (
        Firefox as Firefox,
        Firefox_GlobalExtensions_Item_Or as Firefox_GlobalExtensions_Item_Or,
        Firefox_Profiles_Value as Firefox_Profiles_Value,
        Firefox_Profiles_Value_Bookmarks as Firefox_Profiles_Value_Bookmarks,
        Firefox_Profiles_Value_Bookmarks_From_Item as Firefox_Profiles_Value_Bookmarks_From_Item,
        Firefox_Profiles_Value_Bookmarks_From_Item_Or as Firefox_Profiles_Value_Bookmarks_From_Item_Or,
        Firefox_Profiles_Value_Containers_Value as Firefox_Profiles_Value_Containers_Value,
        Firefox_Profiles_Value_Extensions as Firefox_Profiles_Value_Extensions,
        Firefox_Profiles_Value_Extensions_Settings_Value as Firefox_Profiles_Value_Extensions_Settings_Value,
        Firefox_Profiles_Value_Handlers as Firefox_Profiles_Value_Handlers,
        Firefox_Profiles_Value_Handlers_MimeTypes_Value as Firefox_Profiles_Value_Handlers_MimeTypes_Value,
        Firefox_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item as Firefox_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item,
        Firefox_Profiles_Value_Handlers_Schemes_Value as Firefox_Profiles_Value_Handlers_Schemes_Value,
        Firefox_Profiles_Value_Search as Firefox_Profiles_Value_Search,
    )
    from pynix_hm.programs.firefoxpwa import (
        Firefoxpwa as Firefoxpwa,
        Firefoxpwa_Profiles_Value as Firefoxpwa_Profiles_Value,
        Firefoxpwa_Profiles_Value_Sites_Value as Firefoxpwa_Profiles_Value_Sites_Value,
    )
    from pynix_hm.programs.fish import (
        Fish as Fish,
        Fish_Binds_Value as Fish_Binds_Value,
        Fish_Completions_Value_Or as Fish_Completions_Value_Or,
        Fish_Functions_Value_Or as Fish_Functions_Value_Or,
        Fish_Plugins_Item as Fish_Plugins_Item,
        Fish_ShellAbbrs_Value_Or as Fish_ShellAbbrs_Value_Or,
    )
    from pynix_hm.programs.flake_edit import FlakeEdit as FlakeEdit
    from pynix_hm.programs.flashspace import Flashspace as Flashspace
    from pynix_hm.programs.floorp import (
        Floorp as Floorp,
        Floorp_GlobalExtensions_Item_Or as Floorp_GlobalExtensions_Item_Or,
        Floorp_Profiles_Value as Floorp_Profiles_Value,
        Floorp_Profiles_Value_Bookmarks as Floorp_Profiles_Value_Bookmarks,
        Floorp_Profiles_Value_Bookmarks_From_Item as Floorp_Profiles_Value_Bookmarks_From_Item,
        Floorp_Profiles_Value_Bookmarks_From_Item_Or as Floorp_Profiles_Value_Bookmarks_From_Item_Or,
        Floorp_Profiles_Value_Containers_Value as Floorp_Profiles_Value_Containers_Value,
        Floorp_Profiles_Value_Extensions as Floorp_Profiles_Value_Extensions,
        Floorp_Profiles_Value_Extensions_Settings_Value as Floorp_Profiles_Value_Extensions_Settings_Value,
        Floorp_Profiles_Value_Handlers as Floorp_Profiles_Value_Handlers,
        Floorp_Profiles_Value_Handlers_MimeTypes_Value as Floorp_Profiles_Value_Handlers_MimeTypes_Value,
        Floorp_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item as Floorp_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item,
        Floorp_Profiles_Value_Handlers_Schemes_Value as Floorp_Profiles_Value_Handlers_Schemes_Value,
        Floorp_Profiles_Value_Search as Floorp_Profiles_Value_Search,
    )
    from pynix_hm.programs.fnox import Fnox as Fnox
    from pynix_hm.programs.foliate import Foliate as Foliate
    from pynix_hm.programs.foot import Foot as Foot, Foot_Server as Foot_Server
    from pynix_hm.programs.formiko import Formiko as Formiko
    from pynix_hm.programs.freetube import Freetube as Freetube
    from pynix_hm.programs.fresh_editor import FreshEditor as FreshEditor
    from pynix_hm.programs.fuzzel import Fuzzel as Fuzzel
    from pynix_hm.programs.fzf import (
        Fzf as Fzf,
        Fzf_ChangeDirWidget as Fzf_ChangeDirWidget,
        Fzf_ChangeDirWidget_Bash as Fzf_ChangeDirWidget_Bash,
        Fzf_ChangeDirWidget_Fish as Fzf_ChangeDirWidget_Fish,
        Fzf_ChangeDirWidget_Nushell as Fzf_ChangeDirWidget_Nushell,
        Fzf_ChangeDirWidget_Zsh as Fzf_ChangeDirWidget_Zsh,
        Fzf_FileWidget as Fzf_FileWidget,
        Fzf_FileWidget_Bash as Fzf_FileWidget_Bash,
        Fzf_FileWidget_Fish as Fzf_FileWidget_Fish,
        Fzf_FileWidget_Nushell as Fzf_FileWidget_Nushell,
        Fzf_FileWidget_Zsh as Fzf_FileWidget_Zsh,
        Fzf_HistoryWidget as Fzf_HistoryWidget,
        Fzf_HistoryWidget_Bash as Fzf_HistoryWidget_Bash,
        Fzf_HistoryWidget_Fish as Fzf_HistoryWidget_Fish,
        Fzf_HistoryWidget_Nushell as Fzf_HistoryWidget_Nushell,
        Fzf_HistoryWidget_Zsh as Fzf_HistoryWidget_Zsh,
        Fzf_Tmux as Fzf_Tmux,
    )
    from pynix_hm.programs.gallery_dl import GalleryDl as GalleryDl
    from pynix_hm.programs.gcc import Gcc as Gcc
    from pynix_hm.programs.gh import (
        Gh as Gh,
        Gh_GitCredentialHelper as Gh_GitCredentialHelper,
        Gh_Settings as Gh_Settings,
    )
    from pynix_hm.programs.gh_dash import GhDash as GhDash
    from pynix_hm.programs.ghostty import Ghostty as Ghostty, Ghostty_Systemd as Ghostty_Systemd
    from pynix_hm.programs.git import (
        Git as Git,
        Git_Includes_Item as Git_Includes_Item,
        Git_Lfs as Git_Lfs,
        Git_Maintenance as Git_Maintenance,
        Git_Signing as Git_Signing,
    )
    from pynix_hm.programs.git_cliff import GitCliff as GitCliff
    from pynix_hm.programs.git_credential_keepassxc import GitCredentialKeepassxc as GitCredentialKeepassxc
    from pynix_hm.programs.git_credential_oauth import GitCredentialOauth as GitCredentialOauth
    from pynix_hm.programs.git_worktree_switcher import GitWorktreeSwitcher as GitWorktreeSwitcher
    from pynix_hm.programs.github_copilot_cli import GithubCopilotCli as GithubCopilotCli
    from pynix_hm.programs.gitui import Gitui as Gitui
    from pynix_hm.programs.gnome_shell import (
        GnomeShell as GnomeShell,
        GnomeShell_Extensions_Item as GnomeShell_Extensions_Item,
        GnomeShell_Theme as GnomeShell_Theme,
    )
    from pynix_hm.programs.gnome_terminal import (
        GnomeTerminal as GnomeTerminal,
        GnomeTerminal_Profile_Value as GnomeTerminal_Profile_Value,
        GnomeTerminal_Profile_Value_Colors as GnomeTerminal_Profile_Value_Colors,
        GnomeTerminal_Profile_Value_Colors_Cursor as GnomeTerminal_Profile_Value_Colors_Cursor,
    )
    from pynix_hm.programs.go import Go as Go, Go_Env as Go_Env, Go_Telemetry as Go_Telemetry
    from pynix_hm.programs.google_chrome import (
        GoogleChrome as GoogleChrome,
        GoogleChrome_Extensions_Item as GoogleChrome_Extensions_Item,
    )
    from pynix_hm.programs.google_chrome_beta import (
        GoogleChromeBeta as GoogleChromeBeta,
        GoogleChromeBeta_Extensions_Item as GoogleChromeBeta_Extensions_Item,
    )
    from pynix_hm.programs.google_chrome_dev import (
        GoogleChromeDev as GoogleChromeDev,
        GoogleChromeDev_Extensions_Item as GoogleChromeDev_Extensions_Item,
    )
    from pynix_hm.programs.goto import Goto as Goto
    from pynix_hm.programs.gpg import Gpg as Gpg, Gpg_PublicKeys_Item as Gpg_PublicKeys_Item
    from pynix_hm.programs.gradle import (
        Gradle as Gradle,
        Gradle_InitScripts_Value as Gradle_InitScripts_Value,
        Gradle_Settings as Gradle_Settings,
    )
    from pynix_hm.programs.gram import Gram as Gram
    from pynix_hm.programs.granted import Granted as Granted
    from pynix_hm.programs.grep import Grep as Grep
    from pynix_hm.programs.grype import Grype as Grype
    from pynix_hm.programs.gurk_rs import GurkRs as GurkRs
    from pynix_hm.programs.halloy import Halloy as Halloy
    from pynix_hm.programs.havoc import Havoc as Havoc
    from pynix_hm.programs.helix import Helix as Helix
    from pynix_hm.programs.herdr import Herdr as Herdr
    from pynix_hm.programs.himalaya import (
        Himalaya as Himalaya,
        Himalaya_Mblaze as Himalaya_Mblaze,
        Himalaya_Settings as Himalaya_Settings,
    )
    from pynix_hm.programs.home_manager import HomeManager as Programs_HomeManager
    from pynix_hm.programs.hstr import Hstr as Hstr
    from pynix_hm.programs.htop import Htop as Htop
    from pynix_hm.programs.hwatch import Hwatch as Hwatch
    from pynix_hm.programs.hyfetch import Hyfetch as Hyfetch
    from pynix_hm.programs.hyprland_qt_support import HyprlandQtSupport as HyprlandQtSupport
    from pynix_hm.programs.hyprlock import Hyprlock as Hyprlock
    from pynix_hm.programs.hyprpanel import Hyprpanel as Hyprpanel, Hyprpanel_Systemd as Hyprpanel_Systemd
    from pynix_hm.programs.hyprshot import Hyprshot as Hyprshot
    from pynix_hm.programs.hyprtoolkit import Hyprtoolkit as Hyprtoolkit
    from pynix_hm.programs.i3bar_river import I3barRiver as I3barRiver
    from pynix_hm.programs.i3blocks import I3blocks as I3blocks
    from pynix_hm.programs.i3status import I3status as I3status, I3status_Modules_Value as I3status_Modules_Value
    from pynix_hm.programs.i3status_rust import (
        I3statusRust as I3statusRust,
        I3statusRust_Bars_Value as I3statusRust_Bars_Value,
    )
    from pynix_hm.programs.iamb import Iamb as Iamb
    from pynix_hm.programs.impala import Impala as Impala
    from pynix_hm.programs.imv import Imv as Imv
    from pynix_hm.programs.infat import Infat as Infat, Infat_AutoActivate as Infat_AutoActivate
    from pynix_hm.programs.info import Info as Info
    from pynix_hm.programs.inori import Inori as Inori
    from pynix_hm.programs.intelli_shell import IntelliShell as IntelliShell
    from pynix_hm.programs.ion import Ion as Ion
    from pynix_hm.programs.irssi import (
        Irssi as Irssi,
        Irssi_Networks_Value as Irssi_Networks_Value,
        Irssi_Networks_Value_Channels_Value as Irssi_Networks_Value_Channels_Value,
    )
    from pynix_hm.programs.java import Java as Java
    from pynix_hm.programs.jetbrains_remote import JetbrainsRemote as JetbrainsRemote
    from pynix_hm.programs.jjui import Jjui as Jjui
    from pynix_hm.programs.joplin_desktop import (
        JoplinDesktop as JoplinDesktop,
        JoplinDesktop_General as JoplinDesktop_General,
    )
    from pynix_hm.programs.joshuto import Joshuto as Joshuto
    from pynix_hm.programs.jq import Jq as Jq, Jq_Colors as Jq_Colors
    from pynix_hm.programs.jqp import Jqp as Jqp
    from pynix_hm.programs.jrnl import Jrnl as Jrnl
    from pynix_hm.programs.jujutsu import Jujutsu as Jujutsu
    from pynix_hm.programs.k9s import K9s as K9s
    from pynix_hm.programs.kakoune import (
        Kakoune as Kakoune,
        Kakoune_Config as Kakoune_Config,
        Kakoune_Config_Hooks_Item as Kakoune_Config_Hooks_Item,
        Kakoune_Config_KeyMappings_Item as Kakoune_Config_KeyMappings_Item,
        Kakoune_Config_NumberLines as Kakoune_Config_NumberLines,
        Kakoune_Config_ScrollOff as Kakoune_Config_ScrollOff,
        Kakoune_Config_ShowWhitespace as Kakoune_Config_ShowWhitespace,
        Kakoune_Config_Ui as Kakoune_Config_Ui,
        Kakoune_Config_WrapLines as Kakoune_Config_WrapLines,
    )
    from pynix_hm.programs.keepassxc import Keepassxc as Keepassxc
    from pynix_hm.programs.keychain import Keychain as Keychain
    from pynix_hm.programs.khal import Khal as Khal, Khal_Locale as Khal_Locale
    from pynix_hm.programs.khard import Khard as Khard, Khard_Settings as Khard_Settings
    from pynix_hm.programs.kickoff import Kickoff as Kickoff
    from pynix_hm.programs.kiro import (
        Kiro as Kiro,
        Kiro_Profiles_Value as Kiro_Profiles_Value,
        Kiro_Profiles_Value_Keybindings_Or_Item as Kiro_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.kiro_cli import KiroCli as KiroCli
    from pynix_hm.programs.kitty import (
        Kitty as Kitty,
        Kitty_AutoThemeFiles as Kitty_AutoThemeFiles,
        Kitty_DiffConfig as Kitty_DiffConfig,
        Kitty_Font as Kitty_Font,
        Kitty_ShellIntegration as Kitty_ShellIntegration,
    )
    from pynix_hm.programs.kodi import Kodi as Kodi
    from pynix_hm.programs.kraftkit import Kraftkit as Kraftkit
    from pynix_hm.programs.kubecolor import Kubecolor as Kubecolor
    from pynix_hm.programs.kubeswitch import Kubeswitch as Kubeswitch
    from pynix_hm.programs.lapce import Lapce as Lapce, Lapce_Plugins_Item as Lapce_Plugins_Item
    from pynix_hm.programs.lazydocker import Lazydocker as Lazydocker
    from pynix_hm.programs.lazygit import Lazygit as Lazygit
    from pynix_hm.programs.lazysql import Lazysql as Lazysql
    from pynix_hm.programs.lazyworktree import Lazyworktree as Lazyworktree
    from pynix_hm.programs.ledger import Ledger as Ledger
    from pynix_hm.programs.less import Less as Less
    from pynix_hm.programs.lesspipe import Lesspipe as Lesspipe
    from pynix_hm.programs.lf import Lf as Lf, Lf_Previewer as Lf_Previewer
    from pynix_hm.programs.libreoffice import Libreoffice as Libreoffice
    from pynix_hm.programs.librewolf import (
        Librewolf as Librewolf,
        Librewolf_GlobalExtensions_Item_Or as Librewolf_GlobalExtensions_Item_Or,
        Librewolf_Profiles_Value as Librewolf_Profiles_Value,
        Librewolf_Profiles_Value_Bookmarks as Librewolf_Profiles_Value_Bookmarks,
        Librewolf_Profiles_Value_Bookmarks_From_Item as Librewolf_Profiles_Value_Bookmarks_From_Item,
        Librewolf_Profiles_Value_Bookmarks_From_Item_Or as Librewolf_Profiles_Value_Bookmarks_From_Item_Or,
        Librewolf_Profiles_Value_Containers_Value as Librewolf_Profiles_Value_Containers_Value,
        Librewolf_Profiles_Value_Extensions as Librewolf_Profiles_Value_Extensions,
        Librewolf_Profiles_Value_Extensions_Settings_Value as Librewolf_Profiles_Value_Extensions_Settings_Value,
        Librewolf_Profiles_Value_Handlers as Librewolf_Profiles_Value_Handlers,
        Librewolf_Profiles_Value_Handlers_MimeTypes_Value as Librewolf_Profiles_Value_Handlers_MimeTypes_Value,
        Librewolf_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item as Librewolf_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item,
        Librewolf_Profiles_Value_Handlers_Schemes_Value as Librewolf_Profiles_Value_Handlers_Schemes_Value,
        Librewolf_Profiles_Value_Search as Librewolf_Profiles_Value_Search,
    )
    from pynix_hm.programs.lieer import Lieer as Programs_Lieer
    from pynix_hm.programs.looking_glass_client import LookingGlassClient as LookingGlassClient
    from pynix_hm.programs.lsd import Lsd as Lsd
    from pynix_hm.programs.lutris import (
        Lutris as Lutris,
        Lutris_Runners_Value as Lutris_Runners_Value,
        Lutris_Runners_Value_Settings as Lutris_Runners_Value_Settings,
        Lutris_Runners_Value_Settings_Runner as Lutris_Runners_Value_Settings_Runner,
        Lutris_Runners_Value_Settings_System as Lutris_Runners_Value_Settings_System,
    )
    from pynix_hm.programs.macchina import (
        Macchina as Macchina,
        Macchina_Settings as Macchina_Settings,
        Macchina_Themes_Value as Macchina_Themes_Value,
        Macchina_Themes_Value_Bar as Macchina_Themes_Value_Bar,
        Macchina_Themes_Value_Box as Macchina_Themes_Value_Box,
        Macchina_Themes_Value_Box_InnerMargin as Macchina_Themes_Value_Box_InnerMargin,
        Macchina_Themes_Value_CustomAscii as Macchina_Themes_Value_CustomAscii,
        Macchina_Themes_Value_Keys as Macchina_Themes_Value_Keys,
        Macchina_Themes_Value_Palette as Macchina_Themes_Value_Palette,
        Macchina_Themes_Value_Randomize as Macchina_Themes_Value_Randomize,
    )
    from pynix_hm.programs.macos_terminal import (
        MacosTerminal as MacosTerminal,
        MacosTerminal_Preferences as MacosTerminal_Preferences,
        MacosTerminal_Profiles_Value as MacosTerminal_Profiles_Value,
    )
    from pynix_hm.programs.man import Man as Man, Man_ManDb as Man_ManDb, Man_Mandoc as Man_Mandoc
    from pynix_hm.programs.mangohud import Mangohud as Mangohud
    from pynix_hm.programs.matplotlib import Matplotlib as Matplotlib
    from pynix_hm.programs.mblaze import Mblaze as Mblaze
    from pynix_hm.programs.mbsync import Mbsync as Programs_Mbsync
    from pynix_hm.programs.mc import Mc as Mc
    from pynix_hm.programs.mcfly import Mcfly as Mcfly, Mcfly_Fzf as Mcfly_Fzf
    from pynix_hm.programs.mcp import (
        Mcp as Mcp,
        Mcp_Servers_Value as Mcp_Servers_Value,
        Mcp_Servers_Value_Env_Value_Or as Mcp_Servers_Value_Env_Value_Or,
    )
    from pynix_hm.programs.meli import Meli as Meli, Meli_Settings as Meli_Settings
    from pynix_hm.programs.mercurial import Mercurial as Mercurial
    from pynix_hm.programs.mergiraf import Mergiraf as Mergiraf
    from pynix_hm.programs.micro import Micro as Micro
    from pynix_hm.programs.microsoft_edge import (
        MicrosoftEdge as MicrosoftEdge,
        MicrosoftEdge_Extensions_Item as MicrosoftEdge_Extensions_Item,
    )
    from pynix_hm.programs.mise import Mise as Mise
    from pynix_hm.programs.mistral_vibe import MistralVibe as MistralVibe
    from pynix_hm.programs.mods import Mods as Mods
    from pynix_hm.programs.moor import Moor as Moor
    from pynix_hm.programs.mpv import Mpv as Mpv
    from pynix_hm.programs.mpvpaper import Mpvpaper as Mpvpaper
    from pynix_hm.programs.mr import Mr as Mr
    from pynix_hm.programs.msmtp import Msmtp as Msmtp
    from pynix_hm.programs.mu import Mu as Mu
    from pynix_hm.programs.mujmap import Mujmap as Mujmap
    from pynix_hm.programs.mullvad_vpn import MullvadVpn as MullvadVpn
    from pynix_hm.programs.mypy import Mypy as Mypy
    from pynix_hm.programs.navi import Navi as Navi
    from pynix_hm.programs.ncmpcpp import Ncmpcpp as Ncmpcpp, Ncmpcpp_Bindings_Item as Ncmpcpp_Bindings_Item
    from pynix_hm.programs.ncspot import Ncspot as Ncspot
    from pynix_hm.programs.ne import Ne as Ne
    from pynix_hm.programs.neomutt import (
        Neomutt as Neomutt,
        Neomutt_Binds_Item as Neomutt_Binds_Item,
        Neomutt_Sidebar as Neomutt_Sidebar,
    )
    from pynix_hm.programs.neovide import Neovide as Neovide
    from pynix_hm.programs.neovim import (
        Neovim as Neovim,
        Neovim_Coc as Neovim_Coc,
        Neovim_Plugins_Item_Or as Neovim_Plugins_Item_Or,
        Neovim_Plugins_Item_Or_Runtime_Value as Neovim_Plugins_Item_Or_Runtime_Value,
    )
    from pynix_hm.programs.newsboat import (
        Newsboat as Newsboat,
        Newsboat_AutoFetchArticles as Newsboat_AutoFetchArticles,
        Newsboat_AutoVacuum as Newsboat_AutoVacuum,
        Newsboat_Urls_Item as Newsboat_Urls_Item,
    )
    from pynix_hm.programs.nh import Nh as Nh, Nh_Clean as Nh_Clean
    from pynix_hm.programs.nheko import Nheko as Nheko
    from pynix_hm.programs.ninjabrain_bot import NinjabrainBot as NinjabrainBot
    from pynix_hm.programs.nix_index import NixIndex as NixIndex
    from pynix_hm.programs.nix_init import NixInit as NixInit
    from pynix_hm.programs.nix_search_tv import NixSearchTv as NixSearchTv
    from pynix_hm.programs.nix_your_shell import (
        NixYourShell as NixYourShell,
        NixYourShell_NixOutputMonitor as NixYourShell_NixOutputMonitor,
    )
    from pynix_hm.programs.nnn import Nnn as Nnn, Nnn_Plugins as Nnn_Plugins
    from pynix_hm.programs.noctalia import Noctalia as Noctalia, Noctalia_Systemd as Noctalia_Systemd
    from pynix_hm.programs.nom import Nom as Nom
    from pynix_hm.programs.noti import Noti as Noti
    from pynix_hm.programs.notmuch import Notmuch as Notmuch, Notmuch_Hooks as Notmuch_Hooks
    from pynix_hm.programs.npm import Npm as Npm
    from pynix_hm.programs.numbat import Numbat as Numbat
    from pynix_hm.programs.nushell import (
        Nushell as Nushell,
        Nushell_ConfigFile as Nushell_ConfigFile,
        Nushell_EnvFile as Nushell_EnvFile,
        Nushell_LoginFile as Nushell_LoginFile,
    )
    from pynix_hm.programs.nvchecker import (
        Nvchecker as Nvchecker,
        Nvchecker_Settings as Nvchecker_Settings,
        Nvchecker_Settings_NConfig as Nvchecker_Settings_NConfig,
    )
    from pynix_hm.programs.nyxt import Nyxt as Nyxt
    from pynix_hm.programs.obs_studio import ObsStudio as ObsStudio
    from pynix_hm.programs.obsidian import (
        Obsidian as Obsidian,
        Obsidian_Cli as Obsidian_Cli,
        Obsidian_DefaultSettings as Obsidian_DefaultSettings,
        Obsidian_DefaultSettings_CommunityPlugins_Item as Obsidian_DefaultSettings_CommunityPlugins_Item,
        Obsidian_DefaultSettings_CorePlugins_Item as Obsidian_DefaultSettings_CorePlugins_Item,
        Obsidian_DefaultSettings_CssSnippets_Item as Obsidian_DefaultSettings_CssSnippets_Item,
        Obsidian_DefaultSettings_ExtraFiles_Value as Obsidian_DefaultSettings_ExtraFiles_Value,
        Obsidian_DefaultSettings_Hotkeys_Value_Item as Obsidian_DefaultSettings_Hotkeys_Value_Item,
        Obsidian_DefaultSettings_Themes_Item as Obsidian_DefaultSettings_Themes_Item,
        Obsidian_Vaults_Value as Obsidian_Vaults_Value,
    )
    from pynix_hm.programs.offlineimap import (
        Offlineimap as Offlineimap,
        Offlineimap_ExtraConfig as Offlineimap_ExtraConfig,
    )
    from pynix_hm.programs.oh_my_posh import OhMyPosh as OhMyPosh
    from pynix_hm.programs.omniwm import Omniwm as Omniwm, Omniwm_Launchd as Omniwm_Launchd
    from pynix_hm.programs.onagre import Onagre as Onagre
    from pynix_hm.programs.onedrive import Onedrive as Onedrive
    from pynix_hm.programs.onlyoffice import Onlyoffice as Onlyoffice
    from pynix_hm.programs.opam import Opam as Opam
    from pynix_hm.programs.opencode import (
        Opencode as Opencode,
        Opencode_ValidateFiles as Opencode_ValidateFiles,
        Opencode_Web as Opencode_Web,
    )
    from pynix_hm.programs.openstackclient import (
        Openstackclient as Openstackclient,
        Openstackclient_CloudsPublicSettings_Value_Or as Openstackclient_CloudsPublicSettings_Value_Or,
    )
    from pynix_hm.programs.opkssh import Opkssh as Opkssh
    from pynix_hm.programs.pandoc import Pandoc as Pandoc
    from pynix_hm.programs.papis import Papis as Papis, Papis_Libraries_Value as Papis_Libraries_Value
    from pynix_hm.programs.parallel import Parallel as Parallel
    from pynix_hm.programs.password_store import PasswordStore as PasswordStore
    from pynix_hm.programs.patdiff import Patdiff as Patdiff
    from pynix_hm.programs.pay_respects import PayRespects as PayRespects
    from pynix_hm.programs.pazi import Pazi as Pazi
    from pynix_hm.programs.pet import Pet as Pet, Pet_Snippets_Item as Pet_Snippets_Item
    from pynix_hm.programs.pgcli import Pgcli as Pgcli
    from pynix_hm.programs.pi_coding_agent import PiCodingAgent as PiCodingAgent
    from pynix_hm.programs.pianobar import Pianobar as Pianobar, Pianobar_Settings as Pianobar_Settings
    from pynix_hm.programs.pidgin import Pidgin as Pidgin
    from pynix_hm.programs.pimsync import Pimsync as Programs_Pimsync
    from pynix_hm.programs.pistol import Pistol as Pistol, Pistol_Associations_Item as Pistol_Associations_Item
    from pynix_hm.programs.piston_cli import PistonCli as PistonCli
    from pynix_hm.programs.pls import Pls as Pls
    from pynix_hm.programs.pnpm import Pnpm as Pnpm
    from pynix_hm.programs.poetry import Poetry as Poetry
    from pynix_hm.programs.pomo import Pomo as Pomo
    from pynix_hm.programs.positron import (
        Positron as Positron,
        Positron_Profiles_Value as Positron_Profiles_Value,
        Positron_Profiles_Value_Keybindings_Or_Item as Positron_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.posting import Posting as Posting
    from pynix_hm.programs.powerline_go import PowerlineGo as PowerlineGo
    from pynix_hm.programs.pqiv import Pqiv as Pqiv
    from pynix_hm.programs.prismlauncher import (
        Prismlauncher as Prismlauncher,
        Prismlauncher_Themes_Value_Or as Prismlauncher_Themes_Value_Or,
    )
    from pynix_hm.programs.ptyxis import Ptyxis as Ptyxis
    from pynix_hm.programs.pubs import Pubs as Pubs
    from pynix_hm.programs.pyenv import Pyenv as Pyenv
    from pynix_hm.programs.pylint import Pylint as Pylint
    from pynix_hm.programs.pyradio import (
        Pyradio as Pyradio,
        Pyradio_Stations_Item as Pyradio_Stations_Item,
        Pyradio_Stations_Item_Buffering as Pyradio_Stations_Item_Buffering,
    )
    from pynix_hm.programs.pywal import Pywal as Pywal
    from pynix_hm.programs.qalculate import Qalculate as Qalculate
    from pynix_hm.programs.qcal import Qcal as Qcal
    from pynix_hm.programs.quickshell import Quickshell as Quickshell, Quickshell_Systemd as Quickshell_Systemd
    from pynix_hm.programs.qutebrowser import Qutebrowser as Qutebrowser
    from pynix_hm.programs.radicle import (
        Radicle as Programs_Radicle,
        Radicle_Cli as Radicle_Cli,
        Radicle_Settings as Radicle_Settings,
        Radicle_Uri as Radicle_Uri,
        Radicle_Uri_Rad as Radicle_Uri_Rad,
        Radicle_Uri_Rad_Browser as Radicle_Uri_Rad_Browser,
        Radicle_Uri_Rad_Vscode as Radicle_Uri_Rad_Vscode,
        Radicle_Uri_WebRad as Radicle_Uri_WebRad,
    )
    from pynix_hm.programs.radio_active import RadioActive as RadioActive
    from pynix_hm.programs.radio_cli import RadioCli as RadioCli
    from pynix_hm.programs.ranger import (
        Ranger as Ranger,
        Ranger_Plugins_Item as Ranger_Plugins_Item,
        Ranger_Rifle_Item as Ranger_Rifle_Item,
    )
    from pynix_hm.programs.rbenv import Rbenv as Rbenv, Rbenv_Plugins_Item as Rbenv_Plugins_Item
    from pynix_hm.programs.rbw import Rbw as Rbw, Rbw_Settings as Rbw_Settings
    from pynix_hm.programs.rclone import (
        Rclone as Rclone,
        Rclone_Remotes_Value as Rclone_Remotes_Value,
        Rclone_Remotes_Value_Mounts_Value as Rclone_Remotes_Value_Mounts_Value,
        Rclone_Remotes_Value_Serve_Value as Rclone_Remotes_Value_Serve_Value,
    )
    from pynix_hm.programs.readest import Readest as Readest
    from pynix_hm.programs.readline import Readline as Readline
    from pynix_hm.programs.rectangle import (
        Rectangle as Rectangle,
        Rectangle_Shortcuts_Value as Rectangle_Shortcuts_Value,
    )
    from pynix_hm.programs.retext import Retext as Retext
    from pynix_hm.programs.retroarch import Retroarch as Retroarch, Retroarch_Cores_Value as Retroarch_Cores_Value
    from pynix_hm.programs.riff import Riff as Riff
    from pynix_hm.programs.rio import Rio as Rio
    from pynix_hm.programs.ripasso import Ripasso as Ripasso
    from pynix_hm.programs.ripgrep import Ripgrep as Ripgrep
    from pynix_hm.programs.ripgrep_all import (
        RipgrepAll as RipgrepAll,
        RipgrepAll_CustomAdapters_Item as RipgrepAll_CustomAdapters_Item,
    )
    from pynix_hm.programs.rizin import Rizin as Rizin
    from pynix_hm.programs.rmpc import Rmpc as Rmpc
    from pynix_hm.programs.rofi import (
        Rofi as Rofi,
        Rofi_Modes_Item_Or as Rofi_Modes_Item_Or,
        Rofi_Settings_Value_Value_Or as Rofi_Settings_Value_Value_Or,
    )
    from pynix_hm.programs.rtorrent import Rtorrent as Rtorrent
    from pynix_hm.programs.ruff import Ruff as Ruff
    from pynix_hm.programs.sagemath import Sagemath as Sagemath
    from pynix_hm.programs.sapling import Sapling as Sapling
    from pynix_hm.programs.satty import Satty as Satty
    from pynix_hm.programs.sbt import (
        Sbt as Sbt,
        Sbt_Credentials_Item as Sbt_Credentials_Item,
        Sbt_Plugins_Item as Sbt_Plugins_Item,
    )
    from pynix_hm.programs.scmpuff import Scmpuff as Scmpuff
    from pynix_hm.programs.screen import Screen as Screen
    from pynix_hm.programs.script_directory import ScriptDirectory as ScriptDirectory
    from pynix_hm.programs.secretspec import Secretspec as Secretspec
    from pynix_hm.programs.senpai import Senpai as Senpai, Senpai_Config as Senpai_Config
    from pynix_hm.programs.sesh import Sesh as Sesh, Sesh_Settings as Sesh_Settings
    from pynix_hm.programs.sftpman import Sftpman as Sftpman, Sftpman_Mounts_Value as Sftpman_Mounts_Value
    from pynix_hm.programs.sheldon import Sheldon as Sheldon
    from pynix_hm.programs.sherlock import Sherlock as Sherlock, Sherlock_Systemd as Sherlock_Systemd
    from pynix_hm.programs.sioyek import Sioyek as Sioyek, Sioyek_Config as Sioyek_Config
    from pynix_hm.programs.sketchybar import (
        Sketchybar as Sketchybar,
        Sketchybar_Config_Or as Sketchybar_Config_Or,
        Sketchybar_Service as Sketchybar_Service,
    )
    from pynix_hm.programs.skim import Skim as Skim
    from pynix_hm.programs.sm64ex import Sm64ex as Sm64ex
    from pynix_hm.programs.smug import (
        Smug as Smug,
        Smug_Projects_Value as Smug_Projects_Value,
        Smug_Projects_Value_Windows_Item as Smug_Projects_Value_Windows_Item,
        Smug_Projects_Value_Windows_Item_Panes_Item as Smug_Projects_Value_Windows_Item_Panes_Item,
    )
    from pynix_hm.programs.spotify_player import SpotifyPlayer as SpotifyPlayer
    from pynix_hm.programs.sqls import Sqls as Sqls
    from pynix_hm.programs.ssh import Ssh as Ssh
    from pynix_hm.programs.starship import Starship as Starship, Starship_ValidateFiles as Starship_ValidateFiles
    from pynix_hm.programs.streamlink import (
        Streamlink as Streamlink,
        Streamlink_Plugins_Value as Streamlink_Plugins_Value,
    )
    from pynix_hm.programs.stylua import Stylua as Stylua
    from pynix_hm.programs.superfile import (
        Superfile as Superfile,
        Superfile_PinnedFolders_Item as Superfile_PinnedFolders_Item,
    )
    from pynix_hm.programs.swappy import Swappy as Swappy
    from pynix_hm.programs.sway_easyfocus import SwayEasyfocus as SwayEasyfocus
    from pynix_hm.programs.swayimg import Swayimg as Swayimg
    from pynix_hm.programs.swaylock import Swaylock as Swaylock
    from pynix_hm.programs.swayr import Swayr as Swayr, Swayr_Systemd as Swayr_Systemd
    from pynix_hm.programs.t3code import T3code as T3code
    from pynix_hm.programs.taskwarrior import Taskwarrior as Taskwarrior
    from pynix_hm.programs.tealdeer import (
        Tealdeer as Tealdeer,
        Tealdeer_Settings as Tealdeer_Settings,
        Tealdeer_Settings_Updates as Tealdeer_Settings_Updates,
    )
    from pynix_hm.programs.television import Television as Television
    from pynix_hm.programs.terminator import Terminator as Terminator
    from pynix_hm.programs.termite import Termite as Termite
    from pynix_hm.programs.tex_fmt import TexFmt as TexFmt
    from pynix_hm.programs.texlive import Texlive as Texlive
    from pynix_hm.programs.thunderbird import (
        Thunderbird as Thunderbird,
        Thunderbird_Profiles_Value as Thunderbird_Profiles_Value,
        Thunderbird_Profiles_Value_FeedAccounts_Value as Thunderbird_Profiles_Value_FeedAccounts_Value,
        Thunderbird_Profiles_Value_Search as Thunderbird_Profiles_Value_Search,
    )
    from pynix_hm.programs.timidity import Timidity as Timidity
    from pynix_hm.programs.tint2 import Tint2 as Tint2
    from pynix_hm.programs.tiny import Tiny as Tiny
    from pynix_hm.programs.tirith import Tirith as Tirith
    from pynix_hm.programs.tmate import Tmate as Tmate
    from pynix_hm.programs.tmux import (
        Tmux as Tmux,
        Tmux_Plugins_Item_Or as Tmux_Plugins_Item_Or,
        Tmux_Tmuxinator as Tmux_Tmuxinator,
        Tmux_Tmuxp as Tmux_Tmuxp,
    )
    from pynix_hm.programs.todoman import Todoman as Todoman
    from pynix_hm.programs.tofi import Tofi as Tofi
    from pynix_hm.programs.topgrade import Topgrade as Topgrade
    from pynix_hm.programs.translate_shell import TranslateShell as TranslateShell
    from pynix_hm.programs.tray_tui import TrayTui as TrayTui
    from pynix_hm.programs.trippy import Trippy as Trippy
    from pynix_hm.programs.ttyper import Ttyper as Ttyper
    from pynix_hm.programs.twitch_tui import TwitchTui as TwitchTui
    from pynix_hm.programs.ty import Ty as Ty
    from pynix_hm.programs.urxvt import (
        Urxvt as Urxvt,
        Urxvt_Scroll as Urxvt_Scroll,
        Urxvt_Scroll_Bar as Urxvt_Scroll_Bar,
    )
    from pynix_hm.programs.uv import Uv as Uv, Uv_Python as Uv_Python, Uv_Tool as Uv_Tool
    from pynix_hm.programs.vdirsyncer import Vdirsyncer as Programs_Vdirsyncer
    from pynix_hm.programs.vesktop import Vesktop as Vesktop, Vesktop_Vencord as Vesktop_Vencord
    from pynix_hm.programs.vicinae import Vicinae as Vicinae, Vicinae_Systemd as Vicinae_Systemd
    from pynix_hm.programs.vifm import Vifm as Vifm
    from pynix_hm.programs.vim import Vim as Vim, Vim_Settings as Vim_Settings
    from pynix_hm.programs.vim_vint import VimVint as VimVint
    from pynix_hm.programs.vinegar import Vinegar as Vinegar
    from pynix_hm.programs.visidata import Visidata as Visidata
    from pynix_hm.programs.vivaldi import Vivaldi as Vivaldi, Vivaldi_Extensions_Item as Vivaldi_Extensions_Item
    from pynix_hm.programs.vivid import Vivid as Vivid
    from pynix_hm.programs.vscode import (
        Vscode as Vscode,
        Vscode_Haskell as Vscode_Haskell,
        Vscode_Haskell_Hie as Vscode_Haskell_Hie,
        Vscode_Profiles_Value as Vscode_Profiles_Value,
        Vscode_Profiles_Value_Keybindings_Or_Item as Vscode_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.vscodium import (
        Vscodium as Vscodium,
        Vscodium_Profiles_Value as Vscodium_Profiles_Value,
        Vscodium_Profiles_Value_Keybindings_Or_Item as Vscodium_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.w3m import (
        W3m as W3m,
        W3m_Bookmarks as W3m_Bookmarks,
        W3m_Bookmarks_Marks_Value_Item as W3m_Bookmarks_Marks_Value_Item,
        W3m_CgiBin_Value as W3m_CgiBin_Value,
        W3m_Siteconf_Item as W3m_Siteconf_Item,
    )
    from pynix_hm.programs.wallust import Wallust as Wallust
    from pynix_hm.programs.watson import Watson as Watson
    from pynix_hm.programs.waveterm import Waveterm as Waveterm
    from pynix_hm.programs.waybar import (
        Waybar as Waybar,
        Waybar_Settings_Item as Waybar_Settings_Item,
        Waybar_Systemd as Waybar_Systemd,
    )
    from pynix_hm.programs.waylogout import Waylogout as Waylogout
    from pynix_hm.programs.wayprompt import Wayprompt as Wayprompt
    from pynix_hm.programs.wezterm import Wezterm as Wezterm
    from pynix_hm.programs.windsurf import (
        Windsurf as Windsurf,
        Windsurf_Profiles_Value as Windsurf_Profiles_Value,
        Windsurf_Profiles_Value_Keybindings_Or_Item as Windsurf_Profiles_Value_Keybindings_Or_Item,
    )
    from pynix_hm.programs.wiremix import Wiremix as Wiremix
    from pynix_hm.programs.wleave import Wleave as Wleave
    from pynix_hm.programs.wlogout import Wlogout as Wlogout, Wlogout_Layout_Item as Wlogout_Layout_Item
    from pynix_hm.programs.wlr_which_key import WlrWhichKey as WlrWhichKey
    from pynix_hm.programs.wofi import Wofi as Wofi
    from pynix_hm.programs.workstyle import Workstyle as Workstyle, Workstyle_Systemd as Workstyle_Systemd
    from pynix_hm.programs.worktrunk import (
        Worktrunk as Worktrunk,
        Worktrunk_ClaudeCodeIntegration as Worktrunk_ClaudeCodeIntegration,
    )
    from pynix_hm.programs.xmobar import Xmobar as Xmobar
    from pynix_hm.programs.xplr import Xplr as Xplr
    from pynix_hm.programs.yambar import Yambar as Yambar, Yambar_Systemd as Yambar_Systemd
    from pynix_hm.programs.yarn import Yarn as Yarn
    from pynix_hm.programs.yazi import Yazi as Yazi, Yazi_Plugins_Value as Yazi_Plugins_Value
    from pynix_hm.programs.yofi import Yofi as Yofi
    from pynix_hm.programs.yopass import Yopass as Yopass
    from pynix_hm.programs.yt_dlp import YtDlp as YtDlp
    from pynix_hm.programs.z_lua import ZLua as ZLua
    from pynix_hm.programs.zapzap import Zapzap as Zapzap
    from pynix_hm.programs.zathura import Zathura as Zathura
    from pynix_hm.programs.zed_editor import ZedEditor as ZedEditor
    from pynix_hm.programs.zellij import Zellij as Zellij
    from pynix_hm.programs.zk import Zk as Zk
    from pynix_hm.programs.zoxide import Zoxide as Zoxide
    from pynix_hm.programs.zsh import (
        Zsh as Zsh,
        Zsh_Antidote as Zsh_Antidote,
        Zsh_Autosuggestion as Zsh_Autosuggestion,
        Zsh_FastSyntaxHighlighting as Zsh_FastSyntaxHighlighting,
        Zsh_History as Zsh_History,
        Zsh_HistorySubstringSearch as Zsh_HistorySubstringSearch,
        Zsh_OhMyZsh as Zsh_OhMyZsh,
        Zsh_Plugins_Item as Zsh_Plugins_Item,
        Zsh_Prezto as Zsh_Prezto,
        Zsh_SyntaxHighlighting as Zsh_SyntaxHighlighting,
        Zsh_Zplug as Zsh_Zplug,
        Zsh_Zplug_Plugins_Item as Zsh_Zplug_Plugins_Item,
        Zsh_Zprof as Zsh_Zprof,
        Zsh_ZshAbbr as Zsh_ZshAbbr,
    )
    from pynix_hm.qt.__options__ import Qt as Qt, Qt_PlatformTheme_Or as Qt_PlatformTheme_Or
    from pynix_hm.qt.kde import Kde as Kde
    from pynix_hm.qt.kvantum import (
        Kvantum as Kvantum,
        Kvantum_Settings as Kvantum_Settings,
        Kvantum_Settings_General as Kvantum_Settings_General,
    )
    from pynix_hm.qt.style import Style as Style
    from pynix_hm.services.activitywatch import (
        Activitywatch as Activitywatch,
        Activitywatch_Watchers_Value as Activitywatch_Watchers_Value,
    )
    from pynix_hm.services.amberol import Amberol as Amberol
    from pynix_hm.services.arrpc import Arrpc as Arrpc
    from pynix_hm.services.autorandr import Autorandr as Services_Autorandr
    from pynix_hm.services.autotiling import Autotiling as Autotiling
    from pynix_hm.services.avizo import Avizo as Avizo
    from pynix_hm.services.awww import Awww as Awww
    from pynix_hm.services.batsignal import Batsignal as Batsignal
    from pynix_hm.services.betterlockscreen import Betterlockscreen as Betterlockscreen
    from pynix_hm.services.blanket import Blanket as Blanket
    from pynix_hm.services.blueman_applet import BluemanApplet as BluemanApplet
    from pynix_hm.services.borgmatic import Borgmatic as Services_Borgmatic
    from pynix_hm.services.cachix_agent import CachixAgent as CachixAgent
    from pynix_hm.services.caffeine import Caffeine as Caffeine
    from pynix_hm.services.cbatticon import Cbatticon as Cbatticon
    from pynix_hm.services.clipcat import Clipcat as Clipcat
    from pynix_hm.services.cliphist import Cliphist as Cliphist
    from pynix_hm.services.clipman import Clipman as Clipman
    from pynix_hm.services.clipmenu import Clipmenu as Clipmenu
    from pynix_hm.services.clipse import Clipse as Clipse
    from pynix_hm.services.colima import Colima as Colima, Colima_Profiles_Value as Colima_Profiles_Value
    from pynix_hm.services.comodoro import Comodoro as Services_Comodoro
    from pynix_hm.services.conky import Conky as Conky
    from pynix_hm.services.copyq import Copyq as Copyq
    from pynix_hm.services.darkman import Darkman as Darkman, Darkman_Settings as Darkman_Settings
    from pynix_hm.services.davmail import Davmail as Davmail
    from pynix_hm.services.devilspie2 import Devilspie2 as Devilspie2
    from pynix_hm.services.dropbox import Dropbox as Dropbox
    from pynix_hm.services.dunst import Dunst as Dunst, Dunst_IconTheme as Dunst_IconTheme
    from pynix_hm.services.dwm_status import DwmStatus as DwmStatus
    from pynix_hm.services.easyeffects import Easyeffects as Easyeffects, Easyeffects_Preset_Or as Easyeffects_Preset_Or
    from pynix_hm.services.elephant import Elephant as Elephant
    from pynix_hm.services.emacs import (
        Emacs_Client as Emacs_Client,
        Emacs_SocketActivation as Emacs_SocketActivation,
        Emacs as Services_Emacs,
    )
    from pynix_hm.services.espanso import Espanso as Espanso
    from pynix_hm.services.etesync_dav import EtesyncDav as EtesyncDav
    from pynix_hm.services.exo import Exo as Exo
    from pynix_hm.services.flameshot import Flameshot as Flameshot
    from pynix_hm.services.fluidsynth import Fluidsynth as Fluidsynth
    from pynix_hm.services.fnott import Fnott as Fnott
    from pynix_hm.services.fusuma import Fusuma as Fusuma
    from pynix_hm.services.gammastep import (
        Gammastep as Gammastep,
        Gammastep_Settings as Gammastep_Settings,
        Gammastep_Temperature as Gammastep_Temperature,
    )
    from pynix_hm.services.getmail import Getmail as Getmail
    from pynix_hm.services.git_sync import GitSync as GitSync, GitSync_Repositories_Value as GitSync_Repositories_Value
    from pynix_hm.services.glance import Glance as Glance
    from pynix_hm.services.gnome_keyring import GnomeKeyring as GnomeKeyring
    from pynix_hm.services.gpg_agent import GpgAgent as GpgAgent, GpgAgent_Pinentry as GpgAgent_Pinentry
    from pynix_hm.services.grobi import Grobi as Grobi, Grobi_Settings as Grobi_Settings
    from pynix_hm.services.gromit_mpx import GromitMpx as GromitMpx, GromitMpx_Tools_Item as GromitMpx_Tools_Item
    from pynix_hm.services.home_manager import (
        HomeManager_AutoExpire as HomeManager_AutoExpire,
        HomeManager_AutoExpire_Store as HomeManager_AutoExpire_Store,
        HomeManager_AutoUpgrade as HomeManager_AutoUpgrade,
        HomeManager as Services_HomeManager,
    )
    from pynix_hm.services.hound import Hound as Hound
    from pynix_hm.services.hypridle import Hypridle as Hypridle
    from pynix_hm.services.hyprlauncher import Hyprlauncher as Hyprlauncher
    from pynix_hm.services.hyprpaper import Hyprpaper as Hyprpaper
    from pynix_hm.services.hyprpolkitagent import Hyprpolkitagent as Hyprpolkitagent
    from pynix_hm.services.hyprscratch import Hyprscratch as Hyprscratch
    from pynix_hm.services.hyprshell import Hyprshell as Hyprshell, Hyprshell_Systemd as Hyprshell_Systemd
    from pynix_hm.services.hyprsunset import (
        Hyprsunset as Hyprsunset,
        Hyprsunset_Transitions_Value as Hyprsunset_Transitions_Value,
    )
    from pynix_hm.services.imapnotify import Imapnotify as Imapnotify
    from pynix_hm.services.jankyborders import Jankyborders as Jankyborders
    from pynix_hm.services.jellyfin_mpv_shim import JellyfinMpvShim as JellyfinMpvShim
    from pynix_hm.services.kanshi import (
        Kanshi as Kanshi,
        Kanshi_Profiles_Value as Kanshi_Profiles_Value,
        Kanshi_Profiles_Value_Outputs_Item as Kanshi_Profiles_Value_Outputs_Item,
    )
    from pynix_hm.services.kbfs import Kbfs as Kbfs
    from pynix_hm.services.kdeconnect import Kdeconnect as Kdeconnect
    from pynix_hm.services.keybase import Keybase as Keybase
    from pynix_hm.services.keynav import Keynav as Keynav
    from pynix_hm.services.librespot import Librespot as Librespot, Librespot_Settings as Librespot_Settings
    from pynix_hm.services.lieer import Lieer as Services_Lieer
    from pynix_hm.services.linux_wallpaperengine import (
        LinuxWallpaperengine as LinuxWallpaperengine,
        LinuxWallpaperengine_Audio as LinuxWallpaperengine_Audio,
        LinuxWallpaperengine_Wallpapers_Item as LinuxWallpaperengine_Wallpapers_Item,
    )
    from pynix_hm.services.listenbrainz_mpd import ListenbrainzMpd as ListenbrainzMpd
    from pynix_hm.services.local_ai import LocalAi as LocalAi
    from pynix_hm.services.lorri import Lorri as Lorri
    from pynix_hm.services.ludusavi import Ludusavi as Ludusavi
    from pynix_hm.services.lxqt_policykit_agent import LxqtPolicykitAgent as LxqtPolicykitAgent
    from pynix_hm.services.macos_remap_keys import MacosRemapKeys as MacosRemapKeys
    from pynix_hm.services.mako import Mako as Mako
    from pynix_hm.services.mbsync import Mbsync as Services_Mbsync
    from pynix_hm.services.megasync import Megasync as Megasync
    from pynix_hm.services.mopidy import Mopidy as Mopidy
    from pynix_hm.services.mpd import Mpd as Mpd, Mpd_Network as Mpd_Network
    from pynix_hm.services.mpd_discord_rpc import MpdDiscordRpc as MpdDiscordRpc
    from pynix_hm.services.mpd_mpris import MpdMpris as MpdMpris, MpdMpris_Settings as MpdMpris_Settings
    from pynix_hm.services.mpdris2 import Mpdris2 as Mpdris2, Mpdris2_Mpd as Mpdris2_Mpd
    from pynix_hm.services.mpdris2_rs import Mpdris2Rs as Mpdris2Rs, Mpdris2Rs_Notifications as Mpdris2Rs_Notifications
    from pynix_hm.services.mpdscribble import (
        Mpdscribble as Mpdscribble,
        Mpdscribble_Endpoints_Value as Mpdscribble_Endpoints_Value,
    )
    from pynix_hm.services.mpris_proxy import MprisProxy as MprisProxy
    from pynix_hm.services.muchsync import Muchsync as Muchsync, Muchsync_Remotes_Value as Muchsync_Remotes_Value
    from pynix_hm.services.network_manager_applet import NetworkManagerApplet as NetworkManagerApplet
    from pynix_hm.services.nextcloud_client import NextcloudClient as NextcloudClient
    from pynix_hm.services.notify_osd import NotifyOsd as NotifyOsd
    from pynix_hm.services.nvibrant import Nvibrant as Nvibrant
    from pynix_hm.services.ollama import Ollama as Ollama
    from pynix_hm.services.openlinkhub import (
        Openlinkhub as Openlinkhub,
        Openlinkhub_Dashboard as Openlinkhub_Dashboard,
        Openlinkhub_ExtraConfigs as Openlinkhub_ExtraConfigs,
        Openlinkhub_Settings as Openlinkhub_Settings,
    )
    from pynix_hm.services.opensnitch_ui import OpensnitchUi as OpensnitchUi
    from pynix_hm.services.osmscout_server import (
        OsmscoutServer as OsmscoutServer,
        OsmscoutServer_Network as OsmscoutServer_Network,
    )
    from pynix_hm.services.owncloud_client import OwncloudClient as OwncloudClient
    from pynix_hm.services.pantalaimon import Pantalaimon as Pantalaimon
    from pynix_hm.services.parcellite import Parcellite as Parcellite
    from pynix_hm.services.pass_secret_service import PassSecretService as PassSecretService
    from pynix_hm.services.pasystray import Pasystray as Pasystray
    from pynix_hm.services.pbgopy import Pbgopy as Pbgopy, Pbgopy_Cache as Pbgopy_Cache
    from pynix_hm.services.picom import Picom as Picom
    from pynix_hm.services.pimsync import Pimsync as Services_Pimsync
    from pynix_hm.services.pipewire import Pipewire as Pipewire, Pipewire_Wireplumber as Pipewire_Wireplumber
    from pynix_hm.services.pizauth import Pizauth as Pizauth, Pizauth_Accounts_Value as Pizauth_Accounts_Value
    from pynix_hm.services.plan9port import (
        Plan9port as Plan9port,
        Plan9port_Fontsrv as Plan9port_Fontsrv,
        Plan9port_Plumber as Plan9port_Plumber,
    )
    from pynix_hm.services.playerctld import Playerctld as Playerctld
    from pynix_hm.services.plex_mpv_shim import PlexMpvShim as PlexMpvShim
    from pynix_hm.services.podman import (
        Podman as Podman,
        Podman_AutoUpdate as Podman_AutoUpdate,
        Podman_Builds_Value as Podman_Builds_Value,
        Podman_Containers_Value as Podman_Containers_Value,
        Podman_Images_Value as Podman_Images_Value,
        Podman_Internal as Podman_Internal,
        Podman_Internal_QuadletDefinitions_Item as Podman_Internal_QuadletDefinitions_Item,
        Podman_Machines_Value as Podman_Machines_Value,
        Podman_Networks_Value as Podman_Networks_Value,
        Podman_Settings as Podman_Settings,
        Podman_Settings_Registries as Podman_Settings_Registries,
        Podman_Settings_Registries_Registry_Item as Podman_Settings_Registries_Registry_Item,
        Podman_Volumes_Value as Podman_Volumes_Value,
    )
    from pynix_hm.services.polkit_gnome import PolkitGnome as PolkitGnome
    from pynix_hm.services.polybar import Polybar as Polybar
    from pynix_hm.services.poweralertd import Poweralertd as Poweralertd
    from pynix_hm.services.proton_pass_agent import ProtonPassAgent as ProtonPassAgent
    from pynix_hm.services.protonmail_bridge import ProtonmailBridge as ProtonmailBridge
    from pynix_hm.services.psd import Psd as Psd
    from pynix_hm.services.pueue import Pueue as Pueue
    from pynix_hm.services.pulseeffects import Pulseeffects as Pulseeffects
    from pynix_hm.services.radicle import (
        Radicle_Node as Radicle_Node,
        Radicle_Node_Lazy as Radicle_Node_Lazy,
        Radicle as Services_Radicle,
    )
    from pynix_hm.services.random_background import RandomBackground as RandomBackground
    from pynix_hm.services.recoll import Recoll as Recoll
    from pynix_hm.services.redshift import (
        Redshift as Redshift,
        Redshift_Settings as Redshift_Settings,
        Redshift_Temperature as Redshift_Temperature,
    )
    from pynix_hm.services.remmina import Remmina as Remmina, Remmina_SystemdService as Remmina_SystemdService
    from pynix_hm.services.rescrobbled import Rescrobbled as Rescrobbled
    from pynix_hm.services.restic import Restic as Restic, Restic_Backups_Value as Restic_Backups_Value
    from pynix_hm.services.rsibreak import Rsibreak as Rsibreak
    from pynix_hm.services.safeeyes import Safeeyes as Safeeyes
    from pynix_hm.services.screen_locker import (
        ScreenLocker as ScreenLocker,
        ScreenLocker_Xautolock as ScreenLocker_Xautolock,
        ScreenLocker_XssLock as ScreenLocker_XssLock,
    )
    from pynix_hm.services.sctd import Sctd as Sctd
    from pynix_hm.services.shikane import Shikane as Shikane
    from pynix_hm.services.shpool import Shpool as Shpool
    from pynix_hm.services.signaturepdf import Signaturepdf as Signaturepdf
    from pynix_hm.services.skhd import Skhd as Skhd
    from pynix_hm.services.snixembed import Snixembed as Snixembed
    from pynix_hm.services.spotifyd import Spotifyd as Spotifyd
    from pynix_hm.services.ssh_agent import SshAgent as SshAgent
    from pynix_hm.services.ssh_tpm_agent import SshTpmAgent as SshTpmAgent
    from pynix_hm.services.stalonetray import Stalonetray as Stalonetray
    from pynix_hm.services.status_notifier_watcher import StatusNotifierWatcher as StatusNotifierWatcher
    from pynix_hm.services.swayidle import (
        Swayidle as Swayidle,
        Swayidle_Events as Swayidle_Events,
        Swayidle_Timeouts_Item as Swayidle_Timeouts_Item,
    )
    from pynix_hm.services.swaync import Swaync as Swaync
    from pynix_hm.services.swayosd import Swayosd as Swayosd
    from pynix_hm.services.sxhkd import Sxhkd as Sxhkd
    from pynix_hm.services.syncthing import (
        Syncthing as Syncthing,
        Syncthing_GuiCredentials as Syncthing_GuiCredentials,
        Syncthing_Settings as Syncthing_Settings,
        Syncthing_Settings_Devices_Value as Syncthing_Settings_Devices_Value,
        Syncthing_Settings_Folders_Value as Syncthing_Settings_Folders_Value,
        Syncthing_Settings_Folders_Value_Devices_Item_Or as Syncthing_Settings_Folders_Value_Devices_Item_Or,
        Syncthing_Settings_Folders_Value_Versioning as Syncthing_Settings_Folders_Value_Versioning,
        Syncthing_Settings_Options as Syncthing_Settings_Options,
        Syncthing_Tray as Syncthing_Tray,
    )
    from pynix_hm.services.syshud import Syshud as Syshud
    from pynix_hm.services.systembus_notify import SystembusNotify as SystembusNotify
    from pynix_hm.services.taffybar import Taffybar as Taffybar
    from pynix_hm.services.tahoe_lafs import TahoeLafs as TahoeLafs
    from pynix_hm.services.tailscale_systray import TailscaleSystray as TailscaleSystray
    from pynix_hm.services.taskwarrior_sync import TaskwarriorSync as TaskwarriorSync
    from pynix_hm.services.tldr_update import TldrUpdate as TldrUpdate
    from pynix_hm.services.tomat import Tomat as Tomat, Tomat_Settings as Tomat_Settings
    from pynix_hm.services.trayer import Trayer as Trayer
    from pynix_hm.services.trayscale import Trayscale as Trayscale
    from pynix_hm.services.twmn import (
        Twmn as Twmn,
        Twmn_Text as Twmn_Text,
        Twmn_Text_Font as Twmn_Text_Font,
        Twmn_Window as Twmn_Window,
        Twmn_Window_Animation as Twmn_Window_Animation,
        Twmn_Window_Animation_EaseIn_Or as Twmn_Window_Animation_EaseIn_Or,
    )
    from pynix_hm.services.udiskie import Udiskie as Udiskie
    from pynix_hm.services.unclutter import Unclutter as Unclutter
    from pynix_hm.services.unison import Unison as Unison, Unison_Pairs_Value as Unison_Pairs_Value
    from pynix_hm.services.vdirsyncer import Vdirsyncer as Services_Vdirsyncer
    from pynix_hm.services.volnoti import Volnoti as Volnoti
    from pynix_hm.services.voxtype import (
        Voxtype as Voxtype,
        Voxtype_Wayland as Voxtype_Wayland,
        Voxtype_X11 as Voxtype_X11,
    )
    from pynix_hm.services.walker import (
        Walker as Walker,
        Walker_Systemd as Walker_Systemd,
        Walker_Theme as Walker_Theme,
    )
    from pynix_hm.services.way_displays import WayDisplays as WayDisplays
    from pynix_hm.services.wayle import Wayle as Wayle
    from pynix_hm.services.wayvnc import Wayvnc as Wayvnc, Wayvnc_Settings as Wayvnc_Settings
    from pynix_hm.services.wbg import Wbg as Wbg
    from pynix_hm.services.wl_clip_persist import WlClipPersist as WlClipPersist
    from pynix_hm.services.wlsunset import Wlsunset as Wlsunset, Wlsunset_Temperature as Wlsunset_Temperature
    from pynix_hm.services.wluma import Wluma as Wluma, Wluma_Systemd as Wluma_Systemd
    from pynix_hm.services.wob import Wob as Wob
    from pynix_hm.services.wpaperd import Wpaperd as Wpaperd
    from pynix_hm.services.xcape import Xcape as Xcape
    from pynix_hm.services.xembed_sni_proxy import XembedSniProxy as XembedSniProxy
    from pynix_hm.services.xidlehook import Xidlehook as Xidlehook, Xidlehook_Timers_Item as Xidlehook_Timers_Item
    from pynix_hm.services.xscreensaver import Xscreensaver as Xscreensaver
    from pynix_hm.services.xsettingsd import Xsettingsd as Xsettingsd
    from pynix_hm.services.xsuspender import (
        Xsuspender as Xsuspender,
        Xsuspender_Settings_Value as Xsuspender_Settings_Value,
    )
    from pynix_hm.services.yubikey_agent import YubikeyAgent as YubikeyAgent
    from pynix_hm.sshAuthSock.__options__ import SshAuthSock as SshAuthSock
    from pynix_hm.sshAuthSock.initialization import Initialization as Initialization
    from pynix_hm.sshAuthSock.systemd import Systemd as SshAuthSock_Systemd
    from pynix_hm.submoduleSupport.__options__ import SubmoduleSupport as SubmoduleSupport
    from pynix_hm.systemd.user import (
        User as User,
        User_Automounts_Value as User_Automounts_Value,
        User_Services_Value as User_Services_Value,
        User_Settings as User_Settings,
        User_Tmpfiles as User_Tmpfiles,
    )
    from pynix_hm.targets.darwin import (
        Darwin as Darwin,
        Darwin_CopyApps as Darwin_CopyApps,
        Darwin_CurrentHostDefaults as Darwin_CurrentHostDefaults,
        Darwin_Defaults as Darwin_Defaults,
        Darwin_LinkApps as Darwin_LinkApps,
    )
    from pynix_hm.targets.genericLinux import (
        GenericLinux as GenericLinux,
        GenericLinux_Gpu as GenericLinux_Gpu,
        GenericLinux_Gpu_Nvidia as GenericLinux_Gpu_Nvidia,
        GenericLinux_NixGL as GenericLinux_NixGL,
        GenericLinux_NixGL_Prime as GenericLinux_NixGL_Prime,
        GenericLinux_NixGL_Vulkan as GenericLinux_NixGL_Vulkan,
    )
    from pynix_hm.top import Top as Top, Top_Specialisation_Value as Top_Specialisation_Value
    from pynix_hm.vdirsyncer.__options__ import Vdirsyncer as Vdirsyncer, Vdirsyncer_TimeRange as Vdirsyncer_TimeRange
    from pynix_hm.wayland.systemd import Systemd as Wayland_Systemd
    from pynix_hm.wayland.windowManager import (
        WindowManager as Wayland_WindowManager,
        WindowManager_Hyprland as WindowManager_Hyprland,
        WindowManager_Hyprland_ExtraLuaFiles_Value as WindowManager_Hyprland_ExtraLuaFiles_Value,
        WindowManager_Hyprland_Submaps_Value as WindowManager_Hyprland_Submaps_Value,
        WindowManager_Hyprland_Systemd as WindowManager_Hyprland_Systemd,
        WindowManager_Hyprland_Xdph as WindowManager_Hyprland_Xdph,
        WindowManager_Hyprland_Xdph_Settings as WindowManager_Hyprland_Xdph_Settings,
        WindowManager_Hyprland_Xdph_Settings_General as WindowManager_Hyprland_Xdph_Settings_General,
        WindowManager_Hyprland_Xdph_Settings_Screencopy as WindowManager_Hyprland_Xdph_Settings_Screencopy,
        WindowManager_Hyprland_Xwayland as WindowManager_Hyprland_Xwayland,
        WindowManager_Labwc as WindowManager_Labwc,
        WindowManager_Labwc_Rc as WindowManager_Labwc_Rc,
        WindowManager_Labwc_Systemd as WindowManager_Labwc_Systemd,
        WindowManager_Labwc_Xwayland as WindowManager_Labwc_Xwayland,
        WindowManager_Niri as WindowManager_Niri,
        WindowManager_Niri_Systemd as WindowManager_Niri_Systemd,
        WindowManager_River as WindowManager_River,
        WindowManager_River_Systemd as WindowManager_River_Systemd,
        WindowManager_River_Xwayland as WindowManager_River_Xwayland,
        WindowManager_Sway as WindowManager_Sway,
        WindowManager_Sway_Config as WindowManager_Sway_Config,
        WindowManager_Sway_Config_Bars_Item as WindowManager_Sway_Config_Bars_Item,
        WindowManager_Sway_Config_Bars_Item_Colors as WindowManager_Sway_Config_Bars_Item_Colors,
        WindowManager_Sway_Config_Bars_Item_Colors_ActiveWorkspace as WindowManager_Sway_Config_Bars_Item_Colors_ActiveWorkspace,
        WindowManager_Sway_Config_Bindswitches_Value as WindowManager_Sway_Config_Bindswitches_Value,
        WindowManager_Sway_Config_Colors as WindowManager_Sway_Config_Colors,
        WindowManager_Sway_Config_Colors_Focused as WindowManager_Sway_Config_Colors_Focused,
        WindowManager_Sway_Config_Floating as WindowManager_Sway_Config_Floating,
        WindowManager_Sway_Config_Focus as WindowManager_Sway_Config_Focus,
        WindowManager_Sway_Config_Fonts_Or as WindowManager_Sway_Config_Fonts_Or,
        WindowManager_Sway_Config_Gaps as WindowManager_Sway_Config_Gaps,
        WindowManager_Sway_Config_Startup_Item as WindowManager_Sway_Config_Startup_Item,
        WindowManager_Sway_Config_Window as WindowManager_Sway_Config_Window,
        WindowManager_Sway_Config_Window_Commands_Item as WindowManager_Sway_Config_Window_Commands_Item,
        WindowManager_Sway_Config_WorkspaceOutputAssign_Item as WindowManager_Sway_Config_WorkspaceOutputAssign_Item,
        WindowManager_Sway_Swaynag as WindowManager_Sway_Swaynag,
        WindowManager_Sway_Systemd as WindowManager_Sway_Systemd,
        WindowManager_Sway_WrapperFeatures as WindowManager_Sway_WrapperFeatures,
        WindowManager_Wayfire as WindowManager_Wayfire,
        WindowManager_Wayfire_Settings as WindowManager_Wayfire_Settings,
        WindowManager_Wayfire_Systemd as WindowManager_Wayfire_Systemd,
        WindowManager_Wayfire_WfShell as WindowManager_Wayfire_WfShell,
        WindowManager_Wayfire_Xwayland as WindowManager_Wayfire_Xwayland,
    )
    from pynix_hm.xdg.__options__ import (
        Xdg as Xdg,
        Xdg_CacheFile_Value as Xdg_CacheFile_Value,
        Xdg_ConfigFile_Value as Xdg_ConfigFile_Value,
        Xdg_DataFile_Value as Xdg_DataFile_Value,
        Xdg_DesktopEntries_Value as Xdg_DesktopEntries_Value,
        Xdg_DesktopEntries_Value_Actions_Value as Xdg_DesktopEntries_Value_Actions_Value,
        Xdg_StateFile_Value as Xdg_StateFile_Value,
    )
    from pynix_hm.xdg.autostart import Autostart as Autostart
    from pynix_hm.xdg.mime import Mime as Mime
    from pynix_hm.xdg.mimeApps import MimeApps as MimeApps, MimeApps_Associations as MimeApps_Associations
    from pynix_hm.xdg.portal import Portal as Portal
    from pynix_hm.xdg.systemDirs import SystemDirs as SystemDirs
    from pynix_hm.xdg.terminal_exec import TerminalExec as TerminalExec
    from pynix_hm.xdg.userDirs import UserDirs as UserDirs
    from pynix_hm.xfconf.__options__ import (
        Xfconf as Xfconf,
        Xfconf_Settings_Value_Value_Or as Xfconf_Settings_Value_Value_Or,
    )
    from pynix_hm.xresources.__options__ import Xresources as Xresources
    from pynix_hm.xsession.__options__ import Xsession as Xsession
    from pynix_hm.xsession.numlock import Numlock as Numlock
    from pynix_hm.xsession.windowManager import (
        WindowManager_Awesome as WindowManager_Awesome,
        WindowManager_Bspwm as WindowManager_Bspwm,
        WindowManager_Bspwm_Rules_Value as WindowManager_Bspwm_Rules_Value,
        WindowManager_Exwm as WindowManager_Exwm,
        WindowManager_Fluxbox as WindowManager_Fluxbox,
        WindowManager_Herbstluftwm as WindowManager_Herbstluftwm,
        WindowManager_I3 as WindowManager_I3,
        WindowManager_I3_Config as WindowManager_I3_Config,
        WindowManager_I3_Config_Bars_Item as WindowManager_I3_Config_Bars_Item,
        WindowManager_I3_Config_Bars_Item_Colors as WindowManager_I3_Config_Bars_Item_Colors,
        WindowManager_I3_Config_Bars_Item_Colors_ActiveWorkspace as WindowManager_I3_Config_Bars_Item_Colors_ActiveWorkspace,
        WindowManager_I3_Config_Colors as WindowManager_I3_Config_Colors,
        WindowManager_I3_Config_Colors_Focused as WindowManager_I3_Config_Colors_Focused,
        WindowManager_I3_Config_Floating as WindowManager_I3_Config_Floating,
        WindowManager_I3_Config_Focus as WindowManager_I3_Config_Focus,
        WindowManager_I3_Config_Fonts_Or as WindowManager_I3_Config_Fonts_Or,
        WindowManager_I3_Config_Gaps as WindowManager_I3_Config_Gaps,
        WindowManager_I3_Config_Startup_Item as WindowManager_I3_Config_Startup_Item,
        WindowManager_I3_Config_Window as WindowManager_I3_Config_Window,
        WindowManager_I3_Config_Window_Commands_Item as WindowManager_I3_Config_Window_Commands_Item,
        WindowManager_I3_Config_WorkspaceOutputAssign_Item as WindowManager_I3_Config_WorkspaceOutputAssign_Item,
        WindowManager_Spectrwm as WindowManager_Spectrwm,
        WindowManager_Xmonad as WindowManager_Xmonad,
        WindowManager as Xsession_WindowManager,
    )
else:
    _INDEX = {
        "Abaddon": "pynix_hm.programs.abaddon:Abaddon",
        "Abook": "pynix_hm.programs.abook:Abook",
        "AcdCli": "pynix_hm.programs.acd_cli:AcdCli",
        "Activitywatch": "pynix_hm.services.activitywatch:Activitywatch",
        "Activitywatch_Watchers_Value": "pynix_hm.services.activitywatch:Activitywatch_Watchers_Value",
        "Aerc": "pynix_hm.programs.aerc:Aerc",
        "Aerospace": "pynix_hm.programs.aerospace:Aerospace",
        "Aerospace_Launchd": "pynix_hm.programs.aerospace:Aerospace_Launchd",
        "Afew": "pynix_hm.programs.afew:Afew",
        "Ahoviewer": "pynix_hm.programs.ahoviewer:Ahoviewer",
        "Aiac": "pynix_hm.programs.aiac:Aiac",
        "Aichat": "pynix_hm.programs.aichat:Aichat",
        "AiderChat": "pynix_hm.programs.aider_chat:AiderChat",
        "Airlift": "pynix_hm.programs.airlift:Airlift",
        "Alacritty": "pynix_hm.programs.alacritty:Alacritty",
        "Algia": "pynix_hm.programs.algia:Algia",
        "Aliae": "pynix_hm.programs.aliae:Aliae",
        "Alistral": "pynix_hm.programs.alistral:Alistral",
        "Alot": "pynix_hm.programs.alot:Alot",
        "Alot_Bindings": "pynix_hm.programs.alot:Alot_Bindings",
        "Alot_Tags_Value": "pynix_hm.programs.alot:Alot_Tags_Value",
        "Am2rlauncher": "pynix_hm.programs.am2rlauncher:Am2rlauncher",
        "Amber": "pynix_hm.programs.amber:Amber",
        "Amberol": "pynix_hm.services.amberol:Amberol",
        "Amfora": "pynix_hm.programs.amfora:Amfora",
        "Amoco": "pynix_hm.programs.amoco:Amoco",
        "Amp": "pynix_hm.programs.amp:Amp",
        "Andcli": "pynix_hm.programs.andcli:Andcli",
        "AnimeDownloader": "pynix_hm.programs.anime_downloader:AnimeDownloader",
        "Anki": "pynix_hm.programs.anki:Anki",
        "Anki_AnswerKeys_Item": "pynix_hm.programs.anki:Anki_AnswerKeys_Item",
        "Anki_Profiles_Value": "pynix_hm.programs.anki:Anki_Profiles_Value",
        "Antigravity": "pynix_hm.programs.antigravity:Antigravity",
        "AntigravityCli": "pynix_hm.programs.antigravity_cli:AntigravityCli",
        "AntigravityCli_Commands_Value": "pynix_hm.programs.antigravity_cli:AntigravityCli_Commands_Value",
        "AntigravityCli_Permissions": "pynix_hm.programs.antigravity_cli:AntigravityCli_Permissions",
        "Antigravity_Profiles_Value": "pynix_hm.programs.antigravity:Antigravity_Profiles_Value",
        "Antigravity_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.antigravity:Antigravity_Profiles_Value_Keybindings_Or_Item",
        "Anup": "pynix_hm.programs.anup:Anup",
        "AnvilEditor": "pynix_hm.programs.anvil_editor:AnvilEditor",
        "Anyrun": "pynix_hm.programs.anyrun:Anyrun",
        "Anyrun_Config": "pynix_hm.programs.anyrun:Anyrun_Config",
        "Anyrun_Config_Height": "pynix_hm.programs.anyrun:Anyrun_Config_Height",
        "Anyrun_Config_Keybinds_Item": "pynix_hm.programs.anyrun:Anyrun_Config_Keybinds_Item",
        "Anyrun_Daemon": "pynix_hm.programs.anyrun:Anyrun_Daemon",
        "Aperture": "pynix_hm.programs.aperture:Aperture",
        "Aphorme": "pynix_hm.programs.aphorme:Aphorme",
        "Aria2": "pynix_hm.programs.aria2:Aria2",
        "Aria2_Systemd": "pynix_hm.programs.aria2:Aria2_Systemd",
        "Aria2p": "pynix_hm.programs.aria2p:Aria2p",
        "Arrpc": "pynix_hm.services.arrpc:Arrpc",
        "Asciinema": "pynix_hm.programs.asciinema:Asciinema",
        "Ashell": "pynix_hm.programs.ashell:Ashell",
        "Ashell_Systemd": "pynix_hm.programs.ashell:Ashell_Systemd",
        "Astroid": "pynix_hm.programs.astroid:Astroid",
        "Atool": "pynix_hm.programs.atool:Atool",
        "AtticClient": "pynix_hm.programs.attic_client:AtticClient",
        "Atuin": "pynix_hm.programs.atuin:Atuin",
        "Atuin_Daemon": "pynix_hm.programs.atuin:Atuin_Daemon",
        "Autojump": "pynix_hm.programs.autojump:Autojump",
        "Programs_Autorandr": "pynix_hm.programs.autorandr:Autorandr",
        "Services_Autorandr": "pynix_hm.services.autorandr:Autorandr",
        "Autorandr_Hooks": "pynix_hm.programs.autorandr:Autorandr_Hooks",
        "Autorandr_Profiles_Value": "pynix_hm.programs.autorandr:Autorandr_Profiles_Value",
        "Autorandr_Profiles_Value_Config_Value": "pynix_hm.programs.autorandr:Autorandr_Profiles_Value_Config_Value",
        "Autorandr_Profiles_Value_Config_Value_Scale": "pynix_hm.programs.autorandr:Autorandr_Profiles_Value_Config_Value_Scale",
        "Autorandr_Profiles_Value_Hooks": "pynix_hm.programs.autorandr:Autorandr_Profiles_Value_Hooks",
        "Autostart": "pynix_hm.xdg.autostart:Autostart",
        "Autotiling": "pynix_hm.services.autotiling:Autotiling",
        "Avizo": "pynix_hm.services.avizo:Avizo",
        "Awscli": "pynix_hm.programs.awscli:Awscli",
        "Awscli_Credentials": "pynix_hm.programs.awscli:Awscli_Credentials",
        "Awscli_Settings": "pynix_hm.programs.awscli:Awscli_Settings",
        "Awww": "pynix_hm.services.awww:Awww",
        "B4": "pynix_hm.programs.b4:B4",
        "B4_AgentReview": "pynix_hm.programs.b4:B4_AgentReview",
        "Bacon": "pynix_hm.programs.bacon:Bacon",
        "Bash": "pynix_hm.programs.bash:Bash",
        "Bashmount": "pynix_hm.programs.bashmount:Bashmount",
        "Bat": "pynix_hm.programs.bat:Bat",
        "Bat_Syntaxes_Value_Or": "pynix_hm.programs.bat:Bat_Syntaxes_Value_Or",
        "Bat_Themes_Value_Or": "pynix_hm.programs.bat:Bat_Themes_Value_Or",
        "Batsignal": "pynix_hm.services.batsignal:Batsignal",
        "Beets": "pynix_hm.programs.beets:Beets",
        "Beets_MpdIntegration": "pynix_hm.programs.beets:Beets_MpdIntegration",
        "Bemenu": "pynix_hm.programs.bemenu:Bemenu",
        "Betterlockscreen": "pynix_hm.services.betterlockscreen:Betterlockscreen",
        "Blanket": "pynix_hm.services.blanket:Blanket",
        "BluemanApplet": "pynix_hm.services.blueman_applet:BluemanApplet",
        "Bluetuith": "pynix_hm.programs.bluetuith:Bluetuith",
        "Programs_Borgmatic": "pynix_hm.programs.borgmatic:Borgmatic",
        "Services_Borgmatic": "pynix_hm.services.borgmatic:Borgmatic",
        "Borgmatic_Backups_Value": "pynix_hm.programs.borgmatic:Borgmatic_Backups_Value",
        "Borgmatic_Backups_Value_ConsistencyChecks_Item": "pynix_hm.programs.borgmatic:Borgmatic_Backups_Value_ConsistencyChecks_Item",
        "Borgmatic_Backups_Value_LocationRepositories_Item_Or": "pynix_hm.programs.borgmatic:Borgmatic_Backups_Value_LocationRepositories_Item_Or",
        "Borgmatic_Backups_Value_Settings": "pynix_hm.programs.borgmatic:Borgmatic_Backups_Value_Settings",
        "Bottom": "pynix_hm.programs.bottom:Bottom",
        "Boxxy": "pynix_hm.programs.boxxy:Boxxy",
        "Boxxy_Rules_Item": "pynix_hm.programs.boxxy:Boxxy_Rules_Item",
        "Brave": "pynix_hm.programs.brave:Brave",
        "BraveOrigin": "pynix_hm.programs.brave_origin:BraveOrigin",
        "BraveOrigin_Extensions_Item": "pynix_hm.programs.brave_origin:BraveOrigin_Extensions_Item",
        "Brave_Extensions_Item": "pynix_hm.programs.brave:Brave_Extensions_Item",
        "Broot": "pynix_hm.programs.broot:Broot",
        "Broot_Settings": "pynix_hm.programs.broot:Broot_Settings",
        "Browserpass": "pynix_hm.programs.browserpass:Browserpass",
        "Btop": "pynix_hm.programs.btop:Btop",
        "Bun": "pynix_hm.programs.bun:Bun",
        "CachixAgent": "pynix_hm.services.cachix_agent:CachixAgent",
        "Caffeine": "pynix_hm.services.caffeine:Caffeine",
        "Calendar": "pynix_hm.accounts.calendar:Calendar",
        "Calendar_Accounts_Value": "pynix_hm.accounts.calendar:Calendar_Accounts_Value",
        "Calendar_Accounts_Value_Local": "pynix_hm.accounts.calendar:Calendar_Accounts_Value_Local",
        "Calendar_Accounts_Value_Remote": "pynix_hm.accounts.calendar:Calendar_Accounts_Value_Remote",
        "Calendar_Accounts_Value_VdirsyncerTimeRange": "pynix_hm.accounts.calendar:Calendar_Accounts_Value_VdirsyncerTimeRange",
        "Calibre": "pynix_hm.programs.calibre:Calibre",
        "Carapace": "pynix_hm.programs.carapace:Carapace",
        "Cargo": "pynix_hm.programs.cargo:Cargo",
        "Cava": "pynix_hm.programs.cava:Cava",
        "Cavalier": "pynix_hm.programs.cavalier:Cavalier",
        "Cavalier_Settings": "pynix_hm.programs.cavalier:Cavalier_Settings",
        "Cbatticon": "pynix_hm.services.cbatticon:Cbatticon",
        "Chawan": "pynix_hm.programs.chawan:Chawan",
        "Chromium": "pynix_hm.programs.chromium:Chromium",
        "Chromium_Extensions_Item": "pynix_hm.programs.chromium:Chromium_Extensions_Item",
        "ClaudeCode": "pynix_hm.programs.claude_code:ClaudeCode",
        "Clipcat": "pynix_hm.services.clipcat:Clipcat",
        "Cliphist": "pynix_hm.services.cliphist:Cliphist",
        "Clipman": "pynix_hm.services.clipman:Clipman",
        "Clipmenu": "pynix_hm.services.clipmenu:Clipmenu",
        "Clipse": "pynix_hm.services.clipse:Clipse",
        "ClockRs": "pynix_hm.programs.clock_rs:ClockRs",
        "Cmus": "pynix_hm.programs.cmus:Cmus",
        "Codex": "pynix_hm.programs.codex:Codex",
        "Colima": "pynix_hm.services.colima:Colima",
        "Colima_Profiles_Value": "pynix_hm.services.colima:Colima_Profiles_Value",
        "CommandNotFound": "pynix_hm.programs.command_not_found:CommandNotFound",
        "Programs_Comodoro": "pynix_hm.programs.comodoro:Comodoro",
        "Services_Comodoro": "pynix_hm.services.comodoro:Comodoro",
        "Comodoro_Settings": "pynix_hm.programs.comodoro:Comodoro_Settings",
        "Concord": "pynix_hm.programs.concord:Concord",
        "Concord_KeymapSettings": "pynix_hm.programs.concord:Concord_KeymapSettings",
        "Concord_Settings": "pynix_hm.programs.concord:Concord_Settings",
        "Concord_ThemeSettings": "pynix_hm.programs.concord:Concord_ThemeSettings",
        "Conky": "pynix_hm.services.conky:Conky",
        "Contact": "pynix_hm.accounts.contact:Contact",
        "Contact_Accounts_Value": "pynix_hm.accounts.contact:Contact_Accounts_Value",
        "Contact_Accounts_Value_Local": "pynix_hm.accounts.contact:Contact_Accounts_Value_Local",
        "Contact_Accounts_Value_Remote": "pynix_hm.accounts.contact:Contact_Accounts_Value_Remote",
        "Contact_Accounts_Value_VdirsyncerTimeRange": "pynix_hm.accounts.contact:Contact_Accounts_Value_VdirsyncerTimeRange",
        "Copyq": "pynix_hm.services.copyq:Copyq",
        "Crush": "pynix_hm.programs.crush:Crush",
        "Cudatext": "pynix_hm.programs.cudatext:Cudatext",
        "Cursor": "pynix_hm.programs.cursor:Cursor",
        "Cursor_Profiles_Value": "pynix_hm.programs.cursor:Cursor_Profiles_Value",
        "Cursor_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.cursor:Cursor_Profiles_Value_Keybindings_Or_Item",
        "Darcs": "pynix_hm.programs.darcs:Darcs",
        "Darkman": "pynix_hm.services.darkman:Darkman",
        "Darkman_Settings": "pynix_hm.services.darkman:Darkman_Settings",
        "Darwin": "pynix_hm.targets.darwin:Darwin",
        "Darwin_CopyApps": "pynix_hm.targets.darwin:Darwin_CopyApps",
        "Darwin_CurrentHostDefaults": "pynix_hm.targets.darwin:Darwin_CurrentHostDefaults",
        "Darwin_Defaults": "pynix_hm.targets.darwin:Darwin_Defaults",
        "Darwin_LinkApps": "pynix_hm.targets.darwin:Darwin_LinkApps",
        "Davmail": "pynix_hm.services.davmail:Davmail",
        "Dbeaver": "pynix_hm.programs.dbeaver:Dbeaver",
        "Dbus": "pynix_hm.dbus.__options__:Dbus",
        "Dconf": "pynix_hm.dconf.__options__:Dconf",
        "Delta": "pynix_hm.programs.delta:Delta",
        "Desktoppr": "pynix_hm.programs.desktoppr:Desktoppr",
        "Desktoppr_Settings": "pynix_hm.programs.desktoppr:Desktoppr_Settings",
        "Devenv": "pynix_hm.programs.devenv:Devenv",
        "Devilspie2": "pynix_hm.services.devilspie2:Devilspie2",
        "DiffHighlight": "pynix_hm.programs.diff_highlight:DiffHighlight",
        "DiffSoFancy": "pynix_hm.programs.diff_so_fancy:DiffSoFancy",
        "Difftastic": "pynix_hm.programs.difftastic:Difftastic",
        "Difftastic_Git": "pynix_hm.programs.difftastic:Difftastic_Git",
        "Difftastic_Jujutsu": "pynix_hm.programs.difftastic:Difftastic_Jujutsu",
        "Dircolors": "pynix_hm.programs.dircolors:Dircolors",
        "Direnv": "pynix_hm.programs.direnv:Direnv",
        "Direnv_Mise": "pynix_hm.programs.direnv:Direnv_Mise",
        "Direnv_NixDirenv": "pynix_hm.programs.direnv:Direnv_NixDirenv",
        "Discocss": "pynix_hm.programs.discocss:Discocss",
        "Discord": "pynix_hm.programs.discord:Discord",
        "Discord_Settings": "pynix_hm.programs.discord:Discord_Settings",
        "Distrobox": "pynix_hm.programs.distrobox:Distrobox",
        "DockerCli": "pynix_hm.programs.docker_cli:DockerCli",
        "DockerCli_Contexts_Value": "pynix_hm.programs.docker_cli:DockerCli_Contexts_Value",
        "Dprint": "pynix_hm.programs.dprint:Dprint",
        "Dropbox": "pynix_hm.services.dropbox:Dropbox",
        "Dunst": "pynix_hm.services.dunst:Dunst",
        "Dunst_IconTheme": "pynix_hm.services.dunst:Dunst_IconTheme",
        "DwmStatus": "pynix_hm.services.dwm_status:DwmStatus",
        "Earthly": "pynix_hm.programs.earthly:Earthly",
        "Easyeffects": "pynix_hm.services.easyeffects:Easyeffects",
        "Easyeffects_Preset_Or": "pynix_hm.services.easyeffects:Easyeffects_Preset_Or",
        "Ec": "pynix_hm.programs.ec:Ec",
        "Eclipse": "pynix_hm.programs.eclipse:Eclipse",
        "Editorconfig": "pynix_hm.editorconfig.__options__:Editorconfig",
        "Eilmeldung": "pynix_hm.programs.eilmeldung:Eilmeldung",
        "ElementDesktop": "pynix_hm.programs.element_desktop:ElementDesktop",
        "Elephant": "pynix_hm.services.elephant:Elephant",
        "Programs_Emacs": "pynix_hm.programs.emacs:Emacs",
        "Services_Emacs": "pynix_hm.services.emacs:Emacs",
        "Emacs_Client": "pynix_hm.services.emacs:Emacs_Client",
        "Emacs_SocketActivation": "pynix_hm.services.emacs:Emacs_SocketActivation",
        "Email": "pynix_hm.accounts.email:Email",
        "Email_Accounts_Value": "pynix_hm.accounts.email:Email_Accounts_Value",
        "Email_Accounts_Value_AercImapOauth2Params": "pynix_hm.accounts.email:Email_Accounts_Value_AercImapOauth2Params",
        "Email_Accounts_Value_Aliases_Item_Or": "pynix_hm.accounts.email:Email_Accounts_Value_Aliases_Item_Or",
        "Email_Accounts_Value_Aliases_Item_Or_Gpg": "pynix_hm.accounts.email:Email_Accounts_Value_Aliases_Item_Or_Gpg",
        "Email_Accounts_Value_Aliases_Item_Or_Signature": "pynix_hm.accounts.email:Email_Accounts_Value_Aliases_Item_Or_Signature",
        "Email_Accounts_Value_Aliases_Item_Or_Smtp": "pynix_hm.accounts.email:Email_Accounts_Value_Aliases_Item_Or_Smtp",
        "Email_Accounts_Value_Aliases_Item_Or_Smtp_Tls": "pynix_hm.accounts.email:Email_Accounts_Value_Aliases_Item_Or_Smtp_Tls",
        "Email_Accounts_Value_Ews": "pynix_hm.accounts.email:Email_Accounts_Value_Ews",
        "Email_Accounts_Value_Ews_Tls": "pynix_hm.accounts.email:Email_Accounts_Value_Ews_Tls",
        "Email_Accounts_Value_Folders": "pynix_hm.accounts.email:Email_Accounts_Value_Folders",
        "Email_Accounts_Value_Gpg": "pynix_hm.accounts.email:Email_Accounts_Value_Gpg",
        "Email_Accounts_Value_HimalayaSettings": "pynix_hm.accounts.email:Email_Accounts_Value_HimalayaSettings",
        "Email_Accounts_Value_Imap": "pynix_hm.accounts.email:Email_Accounts_Value_Imap",
        "Email_Accounts_Value_Jmap": "pynix_hm.accounts.email:Email_Accounts_Value_Jmap",
        "Email_Accounts_Value_LieerSettings": "pynix_hm.accounts.email:Email_Accounts_Value_LieerSettings",
        "Email_Accounts_Value_Maildir": "pynix_hm.accounts.email:Email_Accounts_Value_Maildir",
        "Email_Accounts_Value_MbsyncGroups_Value": "pynix_hm.accounts.email:Email_Accounts_Value_MbsyncGroups_Value",
        "Email_Accounts_Value_MbsyncGroups_Value_Channels_Value": "pynix_hm.accounts.email:Email_Accounts_Value_MbsyncGroups_Value_Channels_Value",
        "Email_Accounts_Value_MeliSettings": "pynix_hm.accounts.email:Email_Accounts_Value_MeliSettings",
        "Email_Accounts_Value_MujmapSettings": "pynix_hm.accounts.email:Email_Accounts_Value_MujmapSettings",
        "Email_Accounts_Value_MujmapSettings_Tags": "pynix_hm.accounts.email:Email_Accounts_Value_MujmapSettings_Tags",
        "Email_Accounts_Value_NeomuttExtraMailboxes_Item_Or": "pynix_hm.accounts.email:Email_Accounts_Value_NeomuttExtraMailboxes_Item_Or",
        "Email_Accounts_Value_NotmuchNeomuttVirtualMailboxes_Item": "pynix_hm.accounts.email:Email_Accounts_Value_NotmuchNeomuttVirtualMailboxes_Item",
        "Email_Accounts_Value_Signature": "pynix_hm.accounts.email:Email_Accounts_Value_Signature",
        "Email_Accounts_Value_Smtp": "pynix_hm.accounts.email:Email_Accounts_Value_Smtp",
        "Email_Accounts_Value_ThunderbirdMessageFilters_Item": "pynix_hm.accounts.email:Email_Accounts_Value_ThunderbirdMessageFilters_Item",
        "Equibop": "pynix_hm.programs.equibop:Equibop",
        "Equibop_Equicord": "pynix_hm.programs.equibop:Equibop_Equicord",
        "Espanso": "pynix_hm.services.espanso:Espanso",
        "EtesyncDav": "pynix_hm.services.etesync_dav:EtesyncDav",
        "Eww": "pynix_hm.programs.eww:Eww",
        "Eww_Systemd": "pynix_hm.programs.eww:Eww_Systemd",
        "Exo": "pynix_hm.services.exo:Exo",
        "Eza": "pynix_hm.programs.eza:Eza",
        "FabricAi": "pynix_hm.programs.fabric_ai:FabricAi",
        "Fastfetch": "pynix_hm.programs.fastfetch:Fastfetch",
        "Fd": "pynix_hm.programs.fd:Fd",
        "Feedr": "pynix_hm.programs.feedr:Feedr",
        "Feh": "pynix_hm.programs.feh:Feh",
        "Firefox": "pynix_hm.programs.firefox:Firefox",
        "Firefox_GlobalExtensions_Item_Or": "pynix_hm.programs.firefox:Firefox_GlobalExtensions_Item_Or",
        "Firefox_Profiles_Value": "pynix_hm.programs.firefox:Firefox_Profiles_Value",
        "Firefox_Profiles_Value_Bookmarks": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Bookmarks",
        "Firefox_Profiles_Value_Bookmarks_From_Item": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Bookmarks_From_Item",
        "Firefox_Profiles_Value_Bookmarks_From_Item_Or": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Bookmarks_From_Item_Or",
        "Firefox_Profiles_Value_Containers_Value": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Containers_Value",
        "Firefox_Profiles_Value_Extensions": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Extensions",
        "Firefox_Profiles_Value_Extensions_Settings_Value": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Extensions_Settings_Value",
        "Firefox_Profiles_Value_Handlers": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Handlers",
        "Firefox_Profiles_Value_Handlers_MimeTypes_Value": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Handlers_MimeTypes_Value",
        "Firefox_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item",
        "Firefox_Profiles_Value_Handlers_Schemes_Value": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Handlers_Schemes_Value",
        "Firefox_Profiles_Value_Search": "pynix_hm.programs.firefox:Firefox_Profiles_Value_Search",
        "Firefoxpwa": "pynix_hm.programs.firefoxpwa:Firefoxpwa",
        "Firefoxpwa_Profiles_Value": "pynix_hm.programs.firefoxpwa:Firefoxpwa_Profiles_Value",
        "Firefoxpwa_Profiles_Value_Sites_Value": "pynix_hm.programs.firefoxpwa:Firefoxpwa_Profiles_Value_Sites_Value",
        "Fish": "pynix_hm.programs.fish:Fish",
        "Fish_Binds_Value": "pynix_hm.programs.fish:Fish_Binds_Value",
        "Fish_Completions_Value_Or": "pynix_hm.programs.fish:Fish_Completions_Value_Or",
        "Fish_Functions_Value_Or": "pynix_hm.programs.fish:Fish_Functions_Value_Or",
        "Fish_Plugins_Item": "pynix_hm.programs.fish:Fish_Plugins_Item",
        "Fish_ShellAbbrs_Value_Or": "pynix_hm.programs.fish:Fish_ShellAbbrs_Value_Or",
        "FlakeEdit": "pynix_hm.programs.flake_edit:FlakeEdit",
        "Flameshot": "pynix_hm.services.flameshot:Flameshot",
        "Flashspace": "pynix_hm.programs.flashspace:Flashspace",
        "Floorp": "pynix_hm.programs.floorp:Floorp",
        "Floorp_GlobalExtensions_Item_Or": "pynix_hm.programs.floorp:Floorp_GlobalExtensions_Item_Or",
        "Floorp_Profiles_Value": "pynix_hm.programs.floorp:Floorp_Profiles_Value",
        "Floorp_Profiles_Value_Bookmarks": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Bookmarks",
        "Floorp_Profiles_Value_Bookmarks_From_Item": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Bookmarks_From_Item",
        "Floorp_Profiles_Value_Bookmarks_From_Item_Or": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Bookmarks_From_Item_Or",
        "Floorp_Profiles_Value_Containers_Value": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Containers_Value",
        "Floorp_Profiles_Value_Extensions": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Extensions",
        "Floorp_Profiles_Value_Extensions_Settings_Value": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Extensions_Settings_Value",
        "Floorp_Profiles_Value_Handlers": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Handlers",
        "Floorp_Profiles_Value_Handlers_MimeTypes_Value": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Handlers_MimeTypes_Value",
        "Floorp_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item",
        "Floorp_Profiles_Value_Handlers_Schemes_Value": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Handlers_Schemes_Value",
        "Floorp_Profiles_Value_Search": "pynix_hm.programs.floorp:Floorp_Profiles_Value_Search",
        "Fluidsynth": "pynix_hm.services.fluidsynth:Fluidsynth",
        "Fnott": "pynix_hm.services.fnott:Fnott",
        "Fnox": "pynix_hm.programs.fnox:Fnox",
        "Foliate": "pynix_hm.programs.foliate:Foliate",
        "Fontconfig": "pynix_hm.fonts.fontconfig:Fontconfig",
        "Fontconfig_ConfigFile_Value": "pynix_hm.fonts.fontconfig:Fontconfig_ConfigFile_Value",
        "Fontconfig_DefaultFonts": "pynix_hm.fonts.fontconfig:Fontconfig_DefaultFonts",
        "Foot": "pynix_hm.programs.foot:Foot",
        "Foot_Server": "pynix_hm.programs.foot:Foot_Server",
        "Formiko": "pynix_hm.programs.formiko:Formiko",
        "Freetube": "pynix_hm.programs.freetube:Freetube",
        "FreshEditor": "pynix_hm.programs.fresh_editor:FreshEditor",
        "Fusuma": "pynix_hm.services.fusuma:Fusuma",
        "Fuzzel": "pynix_hm.programs.fuzzel:Fuzzel",
        "Fzf": "pynix_hm.programs.fzf:Fzf",
        "Fzf_ChangeDirWidget": "pynix_hm.programs.fzf:Fzf_ChangeDirWidget",
        "Fzf_ChangeDirWidget_Bash": "pynix_hm.programs.fzf:Fzf_ChangeDirWidget_Bash",
        "Fzf_ChangeDirWidget_Fish": "pynix_hm.programs.fzf:Fzf_ChangeDirWidget_Fish",
        "Fzf_ChangeDirWidget_Nushell": "pynix_hm.programs.fzf:Fzf_ChangeDirWidget_Nushell",
        "Fzf_ChangeDirWidget_Zsh": "pynix_hm.programs.fzf:Fzf_ChangeDirWidget_Zsh",
        "Fzf_FileWidget": "pynix_hm.programs.fzf:Fzf_FileWidget",
        "Fzf_FileWidget_Bash": "pynix_hm.programs.fzf:Fzf_FileWidget_Bash",
        "Fzf_FileWidget_Fish": "pynix_hm.programs.fzf:Fzf_FileWidget_Fish",
        "Fzf_FileWidget_Nushell": "pynix_hm.programs.fzf:Fzf_FileWidget_Nushell",
        "Fzf_FileWidget_Zsh": "pynix_hm.programs.fzf:Fzf_FileWidget_Zsh",
        "Fzf_HistoryWidget": "pynix_hm.programs.fzf:Fzf_HistoryWidget",
        "Fzf_HistoryWidget_Bash": "pynix_hm.programs.fzf:Fzf_HistoryWidget_Bash",
        "Fzf_HistoryWidget_Fish": "pynix_hm.programs.fzf:Fzf_HistoryWidget_Fish",
        "Fzf_HistoryWidget_Nushell": "pynix_hm.programs.fzf:Fzf_HistoryWidget_Nushell",
        "Fzf_HistoryWidget_Zsh": "pynix_hm.programs.fzf:Fzf_HistoryWidget_Zsh",
        "Fzf_Tmux": "pynix_hm.programs.fzf:Fzf_Tmux",
        "GalleryDl": "pynix_hm.programs.gallery_dl:GalleryDl",
        "Gammastep": "pynix_hm.services.gammastep:Gammastep",
        "Gammastep_Settings": "pynix_hm.services.gammastep:Gammastep_Settings",
        "Gammastep_Temperature": "pynix_hm.services.gammastep:Gammastep_Temperature",
        "Gc": "pynix_hm.nix.gc:Gc",
        "Gcc": "pynix_hm.programs.gcc:Gcc",
        "GenericLinux": "pynix_hm.targets.genericLinux:GenericLinux",
        "GenericLinux_Gpu": "pynix_hm.targets.genericLinux:GenericLinux_Gpu",
        "GenericLinux_Gpu_Nvidia": "pynix_hm.targets.genericLinux:GenericLinux_Gpu_Nvidia",
        "GenericLinux_NixGL": "pynix_hm.targets.genericLinux:GenericLinux_NixGL",
        "GenericLinux_NixGL_Prime": "pynix_hm.targets.genericLinux:GenericLinux_NixGL_Prime",
        "GenericLinux_NixGL_Vulkan": "pynix_hm.targets.genericLinux:GenericLinux_NixGL_Vulkan",
        "Getmail": "pynix_hm.services.getmail:Getmail",
        "Gh": "pynix_hm.programs.gh:Gh",
        "GhDash": "pynix_hm.programs.gh_dash:GhDash",
        "Gh_GitCredentialHelper": "pynix_hm.programs.gh:Gh_GitCredentialHelper",
        "Gh_Settings": "pynix_hm.programs.gh:Gh_Settings",
        "Ghostty": "pynix_hm.programs.ghostty:Ghostty",
        "Ghostty_Systemd": "pynix_hm.programs.ghostty:Ghostty_Systemd",
        "Git": "pynix_hm.programs.git:Git",
        "GitCliff": "pynix_hm.programs.git_cliff:GitCliff",
        "GitCredentialKeepassxc": "pynix_hm.programs.git_credential_keepassxc:GitCredentialKeepassxc",
        "GitCredentialOauth": "pynix_hm.programs.git_credential_oauth:GitCredentialOauth",
        "GitSync": "pynix_hm.services.git_sync:GitSync",
        "GitSync_Repositories_Value": "pynix_hm.services.git_sync:GitSync_Repositories_Value",
        "GitWorktreeSwitcher": "pynix_hm.programs.git_worktree_switcher:GitWorktreeSwitcher",
        "Git_Includes_Item": "pynix_hm.programs.git:Git_Includes_Item",
        "Git_Lfs": "pynix_hm.programs.git:Git_Lfs",
        "Git_Maintenance": "pynix_hm.programs.git:Git_Maintenance",
        "Git_Signing": "pynix_hm.programs.git:Git_Signing",
        "GithubCopilotCli": "pynix_hm.programs.github_copilot_cli:GithubCopilotCli",
        "Gitui": "pynix_hm.programs.gitui:Gitui",
        "Glance": "pynix_hm.services.glance:Glance",
        "GnomeKeyring": "pynix_hm.services.gnome_keyring:GnomeKeyring",
        "GnomeShell": "pynix_hm.programs.gnome_shell:GnomeShell",
        "GnomeShell_Extensions_Item": "pynix_hm.programs.gnome_shell:GnomeShell_Extensions_Item",
        "GnomeShell_Theme": "pynix_hm.programs.gnome_shell:GnomeShell_Theme",
        "GnomeTerminal": "pynix_hm.programs.gnome_terminal:GnomeTerminal",
        "GnomeTerminal_Profile_Value": "pynix_hm.programs.gnome_terminal:GnomeTerminal_Profile_Value",
        "GnomeTerminal_Profile_Value_Colors": "pynix_hm.programs.gnome_terminal:GnomeTerminal_Profile_Value_Colors",
        "GnomeTerminal_Profile_Value_Colors_Cursor": "pynix_hm.programs.gnome_terminal:GnomeTerminal_Profile_Value_Colors_Cursor",
        "Go": "pynix_hm.programs.go:Go",
        "Go_Env": "pynix_hm.programs.go:Go_Env",
        "Go_Telemetry": "pynix_hm.programs.go:Go_Telemetry",
        "GoogleChrome": "pynix_hm.programs.google_chrome:GoogleChrome",
        "GoogleChromeBeta": "pynix_hm.programs.google_chrome_beta:GoogleChromeBeta",
        "GoogleChromeBeta_Extensions_Item": "pynix_hm.programs.google_chrome_beta:GoogleChromeBeta_Extensions_Item",
        "GoogleChromeDev": "pynix_hm.programs.google_chrome_dev:GoogleChromeDev",
        "GoogleChromeDev_Extensions_Item": "pynix_hm.programs.google_chrome_dev:GoogleChromeDev_Extensions_Item",
        "GoogleChrome_Extensions_Item": "pynix_hm.programs.google_chrome:GoogleChrome_Extensions_Item",
        "Goto": "pynix_hm.programs.goto:Goto",
        "Gpg": "pynix_hm.programs.gpg:Gpg",
        "GpgAgent": "pynix_hm.services.gpg_agent:GpgAgent",
        "GpgAgent_Pinentry": "pynix_hm.services.gpg_agent:GpgAgent_Pinentry",
        "Gpg_PublicKeys_Item": "pynix_hm.programs.gpg:Gpg_PublicKeys_Item",
        "Gradle": "pynix_hm.programs.gradle:Gradle",
        "Gradle_InitScripts_Value": "pynix_hm.programs.gradle:Gradle_InitScripts_Value",
        "Gradle_Settings": "pynix_hm.programs.gradle:Gradle_Settings",
        "Gram": "pynix_hm.programs.gram:Gram",
        "Granted": "pynix_hm.programs.granted:Granted",
        "Grep": "pynix_hm.programs.grep:Grep",
        "Grobi": "pynix_hm.services.grobi:Grobi",
        "Grobi_Settings": "pynix_hm.services.grobi:Grobi_Settings",
        "GromitMpx": "pynix_hm.services.gromit_mpx:GromitMpx",
        "GromitMpx_Tools_Item": "pynix_hm.services.gromit_mpx:GromitMpx_Tools_Item",
        "Grype": "pynix_hm.programs.grype:Grype",
        "Gtk": "pynix_hm.gtk.__options__:Gtk",
        "Gtk2": "pynix_hm.gtk.gtk2:Gtk2",
        "Gtk2_CursorTheme": "pynix_hm.gtk.gtk2:Gtk2_CursorTheme",
        "Gtk2_Font": "pynix_hm.gtk.gtk2:Gtk2_Font",
        "Gtk2_IconTheme": "pynix_hm.gtk.gtk2:Gtk2_IconTheme",
        "Gtk2_Theme": "pynix_hm.gtk.gtk2:Gtk2_Theme",
        "Gtk3": "pynix_hm.gtk.gtk3:Gtk3",
        "Gtk3_CursorTheme": "pynix_hm.gtk.gtk3:Gtk3_CursorTheme",
        "Gtk3_Font": "pynix_hm.gtk.gtk3:Gtk3_Font",
        "Gtk3_IconTheme": "pynix_hm.gtk.gtk3:Gtk3_IconTheme",
        "Gtk3_Theme": "pynix_hm.gtk.gtk3:Gtk3_Theme",
        "Gtk4": "pynix_hm.gtk.gtk4:Gtk4",
        "Gtk4_CursorTheme": "pynix_hm.gtk.gtk4:Gtk4_CursorTheme",
        "Gtk4_Font": "pynix_hm.gtk.gtk4:Gtk4_Font",
        "Gtk4_IconTheme": "pynix_hm.gtk.gtk4:Gtk4_IconTheme",
        "Gtk4_Theme": "pynix_hm.gtk.gtk4:Gtk4_Theme",
        "Gtk_CursorTheme": "pynix_hm.gtk.__options__:Gtk_CursorTheme",
        "Gtk_Font": "pynix_hm.gtk.__options__:Gtk_Font",
        "Gtk_IconTheme": "pynix_hm.gtk.__options__:Gtk_IconTheme",
        "Gtk_Theme": "pynix_hm.gtk.__options__:Gtk_Theme",
        "GurkRs": "pynix_hm.programs.gurk_rs:GurkRs",
        "Halloy": "pynix_hm.programs.halloy:Halloy",
        "Havoc": "pynix_hm.programs.havoc:Havoc",
        "Helix": "pynix_hm.programs.helix:Helix",
        "Herdr": "pynix_hm.programs.herdr:Herdr",
        "Himalaya": "pynix_hm.programs.himalaya:Himalaya",
        "Himalaya_Mblaze": "pynix_hm.programs.himalaya:Himalaya_Mblaze",
        "Himalaya_Settings": "pynix_hm.programs.himalaya:Himalaya_Settings",
        "Home": "pynix_hm.home.__options__:Home",
        "Programs_HomeManager": "pynix_hm.programs.home_manager:HomeManager",
        "Services_HomeManager": "pynix_hm.services.home_manager:HomeManager",
        "HomeManager_AutoExpire": "pynix_hm.services.home_manager:HomeManager_AutoExpire",
        "HomeManager_AutoExpire_Store": "pynix_hm.services.home_manager:HomeManager_AutoExpire_Store",
        "HomeManager_AutoUpgrade": "pynix_hm.services.home_manager:HomeManager_AutoUpgrade",
        "Home_File_Value": "pynix_hm.home.__options__:Home_File_Value",
        "Home_Keyboard": "pynix_hm.home.__options__:Home_Keyboard",
        "Home_Language": "pynix_hm.home.__options__:Home_Language",
        "Home_PointerCursor": "pynix_hm.home.__options__:Home_PointerCursor",
        "Home_Services_Value": "pynix_hm.home.__options__:Home_Services_Value",
        "Home_Services_Value_ConfigData_Value": "pynix_hm.home.__options__:Home_Services_Value_ConfigData_Value",
        "Home_Services_Value_NotificationProtocol": "pynix_hm.home.__options__:Home_Services_Value_NotificationProtocol",
        "Home_Services_Value_Services_Value": "pynix_hm.home.__options__:Home_Services_Value_Services_Value",
        "Home_Services_Value_SystemdService": "pynix_hm.home.__options__:Home_Services_Value_SystemdService",
        "Home_Services_Value_SystemdServices_Value": "pynix_hm.home.__options__:Home_Services_Value_SystemdServices_Value",
        "Hound": "pynix_hm.services.hound:Hound",
        "Hstr": "pynix_hm.programs.hstr:Hstr",
        "Html": "pynix_hm.manual.html:Html",
        "Htop": "pynix_hm.programs.htop:Htop",
        "Hwatch": "pynix_hm.programs.hwatch:Hwatch",
        "Hyfetch": "pynix_hm.programs.hyfetch:Hyfetch",
        "Hypridle": "pynix_hm.services.hypridle:Hypridle",
        "HyprlandQtSupport": "pynix_hm.programs.hyprland_qt_support:HyprlandQtSupport",
        "Hyprlauncher": "pynix_hm.services.hyprlauncher:Hyprlauncher",
        "Hyprlock": "pynix_hm.programs.hyprlock:Hyprlock",
        "Hyprpanel": "pynix_hm.programs.hyprpanel:Hyprpanel",
        "Hyprpanel_Systemd": "pynix_hm.programs.hyprpanel:Hyprpanel_Systemd",
        "Hyprpaper": "pynix_hm.services.hyprpaper:Hyprpaper",
        "Hyprpolkitagent": "pynix_hm.services.hyprpolkitagent:Hyprpolkitagent",
        "Hyprscratch": "pynix_hm.services.hyprscratch:Hyprscratch",
        "Hyprshell": "pynix_hm.services.hyprshell:Hyprshell",
        "Hyprshell_Systemd": "pynix_hm.services.hyprshell:Hyprshell_Systemd",
        "Hyprshot": "pynix_hm.programs.hyprshot:Hyprshot",
        "Hyprsunset": "pynix_hm.services.hyprsunset:Hyprsunset",
        "Hyprsunset_Transitions_Value": "pynix_hm.services.hyprsunset:Hyprsunset_Transitions_Value",
        "Hyprtoolkit": "pynix_hm.programs.hyprtoolkit:Hyprtoolkit",
        "I18n": "pynix_hm.i18n.__options__:I18n",
        "I3barRiver": "pynix_hm.programs.i3bar_river:I3barRiver",
        "I3blocks": "pynix_hm.programs.i3blocks:I3blocks",
        "I3status": "pynix_hm.programs.i3status:I3status",
        "I3statusRust": "pynix_hm.programs.i3status_rust:I3statusRust",
        "I3statusRust_Bars_Value": "pynix_hm.programs.i3status_rust:I3statusRust_Bars_Value",
        "I3status_Modules_Value": "pynix_hm.programs.i3status:I3status_Modules_Value",
        "Iamb": "pynix_hm.programs.iamb:Iamb",
        "Imapnotify": "pynix_hm.services.imapnotify:Imapnotify",
        "Impala": "pynix_hm.programs.impala:Impala",
        "Imv": "pynix_hm.programs.imv:Imv",
        "Infat": "pynix_hm.programs.infat:Infat",
        "Infat_AutoActivate": "pynix_hm.programs.infat:Infat_AutoActivate",
        "Info": "pynix_hm.programs.info:Info",
        "Initialization": "pynix_hm.sshAuthSock.initialization:Initialization",
        "Inori": "pynix_hm.programs.inori:Inori",
        "IntelliShell": "pynix_hm.programs.intelli_shell:IntelliShell",
        "Internal": "pynix_hm.home.internal:Internal",
        "Ion": "pynix_hm.programs.ion:Ion",
        "Irssi": "pynix_hm.programs.irssi:Irssi",
        "Irssi_Networks_Value": "pynix_hm.programs.irssi:Irssi_Networks_Value",
        "Irssi_Networks_Value_Channels_Value": "pynix_hm.programs.irssi:Irssi_Networks_Value_Channels_Value",
        "Jankyborders": "pynix_hm.services.jankyborders:Jankyborders",
        "Java": "pynix_hm.programs.java:Java",
        "JellyfinMpvShim": "pynix_hm.services.jellyfin_mpv_shim:JellyfinMpvShim",
        "JetbrainsRemote": "pynix_hm.programs.jetbrains_remote:JetbrainsRemote",
        "Jjui": "pynix_hm.programs.jjui:Jjui",
        "JoplinDesktop": "pynix_hm.programs.joplin_desktop:JoplinDesktop",
        "JoplinDesktop_General": "pynix_hm.programs.joplin_desktop:JoplinDesktop_General",
        "Joshuto": "pynix_hm.programs.joshuto:Joshuto",
        "Jq": "pynix_hm.programs.jq:Jq",
        "Jq_Colors": "pynix_hm.programs.jq:Jq_Colors",
        "Jqp": "pynix_hm.programs.jqp:Jqp",
        "Jrnl": "pynix_hm.programs.jrnl:Jrnl",
        "Manual_Json": "pynix_hm.manual.json_:Json",
        "News_Json": "pynix_hm.news.json_:Json",
        "Jujutsu": "pynix_hm.programs.jujutsu:Jujutsu",
        "K9s": "pynix_hm.programs.k9s:K9s",
        "Kakoune": "pynix_hm.programs.kakoune:Kakoune",
        "Kakoune_Config": "pynix_hm.programs.kakoune:Kakoune_Config",
        "Kakoune_Config_Hooks_Item": "pynix_hm.programs.kakoune:Kakoune_Config_Hooks_Item",
        "Kakoune_Config_KeyMappings_Item": "pynix_hm.programs.kakoune:Kakoune_Config_KeyMappings_Item",
        "Kakoune_Config_NumberLines": "pynix_hm.programs.kakoune:Kakoune_Config_NumberLines",
        "Kakoune_Config_ScrollOff": "pynix_hm.programs.kakoune:Kakoune_Config_ScrollOff",
        "Kakoune_Config_ShowWhitespace": "pynix_hm.programs.kakoune:Kakoune_Config_ShowWhitespace",
        "Kakoune_Config_Ui": "pynix_hm.programs.kakoune:Kakoune_Config_Ui",
        "Kakoune_Config_WrapLines": "pynix_hm.programs.kakoune:Kakoune_Config_WrapLines",
        "Kanshi": "pynix_hm.services.kanshi:Kanshi",
        "Kanshi_Profiles_Value": "pynix_hm.services.kanshi:Kanshi_Profiles_Value",
        "Kanshi_Profiles_Value_Outputs_Item": "pynix_hm.services.kanshi:Kanshi_Profiles_Value_Outputs_Item",
        "Kbfs": "pynix_hm.services.kbfs:Kbfs",
        "Kde": "pynix_hm.qt.kde:Kde",
        "Kdeconnect": "pynix_hm.services.kdeconnect:Kdeconnect",
        "Keepassxc": "pynix_hm.programs.keepassxc:Keepassxc",
        "Keybase": "pynix_hm.services.keybase:Keybase",
        "Keychain": "pynix_hm.programs.keychain:Keychain",
        "Keynav": "pynix_hm.services.keynav:Keynav",
        "Khal": "pynix_hm.programs.khal:Khal",
        "Khal_Locale": "pynix_hm.programs.khal:Khal_Locale",
        "Khard": "pynix_hm.programs.khard:Khard",
        "Khard_Settings": "pynix_hm.programs.khard:Khard_Settings",
        "Kickoff": "pynix_hm.programs.kickoff:Kickoff",
        "Kiro": "pynix_hm.programs.kiro:Kiro",
        "KiroCli": "pynix_hm.programs.kiro_cli:KiroCli",
        "Kiro_Profiles_Value": "pynix_hm.programs.kiro:Kiro_Profiles_Value",
        "Kiro_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.kiro:Kiro_Profiles_Value_Keybindings_Or_Item",
        "Kitty": "pynix_hm.programs.kitty:Kitty",
        "Kitty_AutoThemeFiles": "pynix_hm.programs.kitty:Kitty_AutoThemeFiles",
        "Kitty_DiffConfig": "pynix_hm.programs.kitty:Kitty_DiffConfig",
        "Kitty_Font": "pynix_hm.programs.kitty:Kitty_Font",
        "Kitty_ShellIntegration": "pynix_hm.programs.kitty:Kitty_ShellIntegration",
        "Kodi": "pynix_hm.programs.kodi:Kodi",
        "Kraftkit": "pynix_hm.programs.kraftkit:Kraftkit",
        "Kubecolor": "pynix_hm.programs.kubecolor:Kubecolor",
        "Kubeswitch": "pynix_hm.programs.kubeswitch:Kubeswitch",
        "Kvantum": "pynix_hm.qt.kvantum:Kvantum",
        "Kvantum_Settings": "pynix_hm.qt.kvantum:Kvantum_Settings",
        "Kvantum_Settings_General": "pynix_hm.qt.kvantum:Kvantum_Settings_General",
        "Lapce": "pynix_hm.programs.lapce:Lapce",
        "Lapce_Plugins_Item": "pynix_hm.programs.lapce:Lapce_Plugins_Item",
        "Launchd": "pynix_hm.launchd.__options__:Launchd",
        "Launchd_Agents_Value": "pynix_hm.launchd.__options__:Launchd_Agents_Value",
        "Launchd_Agents_Value_Config": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config",
        "Launchd_Agents_Value_Config_HardResourceLimits": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_HardResourceLimits",
        "Launchd_Agents_Value_Config_InetdCompatibility": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_InetdCompatibility",
        "Launchd_Agents_Value_Config_KeepAlive_Or": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_KeepAlive_Or",
        "Launchd_Agents_Value_Config_MachServices_Value_Or": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_MachServices_Value_Or",
        "Launchd_Agents_Value_Config_Sockets_Value": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_Sockets_Value",
        "Launchd_Agents_Value_Config_SoftResourceLimits": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_SoftResourceLimits",
        "Launchd_Agents_Value_Config_StartCalendarInterval": "pynix_hm.launchd.__options__:Launchd_Agents_Value_Config_StartCalendarInterval",
        "Lazydocker": "pynix_hm.programs.lazydocker:Lazydocker",
        "Lazygit": "pynix_hm.programs.lazygit:Lazygit",
        "Lazysql": "pynix_hm.programs.lazysql:Lazysql",
        "Lazyworktree": "pynix_hm.programs.lazyworktree:Lazyworktree",
        "Ledger": "pynix_hm.programs.ledger:Ledger",
        "Less": "pynix_hm.programs.less:Less",
        "Lesspipe": "pynix_hm.programs.lesspipe:Lesspipe",
        "Lf": "pynix_hm.programs.lf:Lf",
        "Lf_Previewer": "pynix_hm.programs.lf:Lf_Previewer",
        "Libreoffice": "pynix_hm.programs.libreoffice:Libreoffice",
        "Librespot": "pynix_hm.services.librespot:Librespot",
        "Librespot_Settings": "pynix_hm.services.librespot:Librespot_Settings",
        "Librewolf": "pynix_hm.programs.librewolf:Librewolf",
        "Librewolf_GlobalExtensions_Item_Or": "pynix_hm.programs.librewolf:Librewolf_GlobalExtensions_Item_Or",
        "Librewolf_Profiles_Value": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value",
        "Librewolf_Profiles_Value_Bookmarks": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Bookmarks",
        "Librewolf_Profiles_Value_Bookmarks_From_Item": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Bookmarks_From_Item",
        "Librewolf_Profiles_Value_Bookmarks_From_Item_Or": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Bookmarks_From_Item_Or",
        "Librewolf_Profiles_Value_Containers_Value": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Containers_Value",
        "Librewolf_Profiles_Value_Extensions": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Extensions",
        "Librewolf_Profiles_Value_Extensions_Settings_Value": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Extensions_Settings_Value",
        "Librewolf_Profiles_Value_Handlers": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Handlers",
        "Librewolf_Profiles_Value_Handlers_MimeTypes_Value": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Handlers_MimeTypes_Value",
        "Librewolf_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Handlers_MimeTypes_Value_Handlers_Item",
        "Librewolf_Profiles_Value_Handlers_Schemes_Value": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Handlers_Schemes_Value",
        "Librewolf_Profiles_Value_Search": "pynix_hm.programs.librewolf:Librewolf_Profiles_Value_Search",
        "Programs_Lieer": "pynix_hm.programs.lieer:Lieer",
        "Services_Lieer": "pynix_hm.services.lieer:Lieer",
        "LinuxWallpaperengine": "pynix_hm.services.linux_wallpaperengine:LinuxWallpaperengine",
        "LinuxWallpaperengine_Audio": "pynix_hm.services.linux_wallpaperengine:LinuxWallpaperengine_Audio",
        "LinuxWallpaperengine_Wallpapers_Item": "pynix_hm.services.linux_wallpaperengine:LinuxWallpaperengine_Wallpapers_Item",
        "ListenbrainzMpd": "pynix_hm.services.listenbrainz_mpd:ListenbrainzMpd",
        "LocalAi": "pynix_hm.services.local_ai:LocalAi",
        "LookingGlassClient": "pynix_hm.programs.looking_glass_client:LookingGlassClient",
        "Lorri": "pynix_hm.services.lorri:Lorri",
        "Lsd": "pynix_hm.programs.lsd:Lsd",
        "Ludusavi": "pynix_hm.services.ludusavi:Ludusavi",
        "Lutris": "pynix_hm.programs.lutris:Lutris",
        "Lutris_Runners_Value": "pynix_hm.programs.lutris:Lutris_Runners_Value",
        "Lutris_Runners_Value_Settings": "pynix_hm.programs.lutris:Lutris_Runners_Value_Settings",
        "Lutris_Runners_Value_Settings_Runner": "pynix_hm.programs.lutris:Lutris_Runners_Value_Settings_Runner",
        "Lutris_Runners_Value_Settings_System": "pynix_hm.programs.lutris:Lutris_Runners_Value_Settings_System",
        "LxqtPolicykitAgent": "pynix_hm.services.lxqt_policykit_agent:LxqtPolicykitAgent",
        "Macchina": "pynix_hm.programs.macchina:Macchina",
        "Macchina_Settings": "pynix_hm.programs.macchina:Macchina_Settings",
        "Macchina_Themes_Value": "pynix_hm.programs.macchina:Macchina_Themes_Value",
        "Macchina_Themes_Value_Bar": "pynix_hm.programs.macchina:Macchina_Themes_Value_Bar",
        "Macchina_Themes_Value_Box": "pynix_hm.programs.macchina:Macchina_Themes_Value_Box",
        "Macchina_Themes_Value_Box_InnerMargin": "pynix_hm.programs.macchina:Macchina_Themes_Value_Box_InnerMargin",
        "Macchina_Themes_Value_CustomAscii": "pynix_hm.programs.macchina:Macchina_Themes_Value_CustomAscii",
        "Macchina_Themes_Value_Keys": "pynix_hm.programs.macchina:Macchina_Themes_Value_Keys",
        "Macchina_Themes_Value_Palette": "pynix_hm.programs.macchina:Macchina_Themes_Value_Palette",
        "Macchina_Themes_Value_Randomize": "pynix_hm.programs.macchina:Macchina_Themes_Value_Randomize",
        "MacosRemapKeys": "pynix_hm.services.macos_remap_keys:MacosRemapKeys",
        "MacosTerminal": "pynix_hm.programs.macos_terminal:MacosTerminal",
        "MacosTerminal_Preferences": "pynix_hm.programs.macos_terminal:MacosTerminal_Preferences",
        "MacosTerminal_Profiles_Value": "pynix_hm.programs.macos_terminal:MacosTerminal_Profiles_Value",
        "Mako": "pynix_hm.services.mako:Mako",
        "Man": "pynix_hm.programs.man:Man",
        "Man_ManDb": "pynix_hm.programs.man:Man_ManDb",
        "Man_Mandoc": "pynix_hm.programs.man:Man_Mandoc",
        "Mangohud": "pynix_hm.programs.mangohud:Mangohud",
        "Manpages": "pynix_hm.manual.manpages:Manpages",
        "Matplotlib": "pynix_hm.programs.matplotlib:Matplotlib",
        "Mblaze": "pynix_hm.programs.mblaze:Mblaze",
        "Programs_Mbsync": "pynix_hm.programs.mbsync:Mbsync",
        "Services_Mbsync": "pynix_hm.services.mbsync:Mbsync",
        "Mc": "pynix_hm.programs.mc:Mc",
        "Mcfly": "pynix_hm.programs.mcfly:Mcfly",
        "Mcfly_Fzf": "pynix_hm.programs.mcfly:Mcfly_Fzf",
        "Mcp": "pynix_hm.programs.mcp:Mcp",
        "Mcp_Servers_Value": "pynix_hm.programs.mcp:Mcp_Servers_Value",
        "Mcp_Servers_Value_Env_Value_Or": "pynix_hm.programs.mcp:Mcp_Servers_Value_Env_Value_Or",
        "Megasync": "pynix_hm.services.megasync:Megasync",
        "Meli": "pynix_hm.programs.meli:Meli",
        "Meli_Settings": "pynix_hm.programs.meli:Meli_Settings",
        "Mercurial": "pynix_hm.programs.mercurial:Mercurial",
        "Mergiraf": "pynix_hm.programs.mergiraf:Mergiraf",
        "Meta": "pynix_hm.meta.__options__:Meta",
        "Micro": "pynix_hm.programs.micro:Micro",
        "MicrosoftEdge": "pynix_hm.programs.microsoft_edge:MicrosoftEdge",
        "MicrosoftEdge_Extensions_Item": "pynix_hm.programs.microsoft_edge:MicrosoftEdge_Extensions_Item",
        "Mime": "pynix_hm.xdg.mime:Mime",
        "MimeApps": "pynix_hm.xdg.mimeApps:MimeApps",
        "MimeApps_Associations": "pynix_hm.xdg.mimeApps:MimeApps_Associations",
        "Mise": "pynix_hm.programs.mise:Mise",
        "MistralVibe": "pynix_hm.programs.mistral_vibe:MistralVibe",
        "Mods": "pynix_hm.programs.mods:Mods",
        "Moor": "pynix_hm.programs.moor:Moor",
        "Mopidy": "pynix_hm.services.mopidy:Mopidy",
        "Mozilla": "pynix_hm.mozilla.__options__:Mozilla",
        "Mpd": "pynix_hm.services.mpd:Mpd",
        "MpdDiscordRpc": "pynix_hm.services.mpd_discord_rpc:MpdDiscordRpc",
        "MpdMpris": "pynix_hm.services.mpd_mpris:MpdMpris",
        "MpdMpris_Settings": "pynix_hm.services.mpd_mpris:MpdMpris_Settings",
        "Mpd_Network": "pynix_hm.services.mpd:Mpd_Network",
        "Mpdris2": "pynix_hm.services.mpdris2:Mpdris2",
        "Mpdris2Rs": "pynix_hm.services.mpdris2_rs:Mpdris2Rs",
        "Mpdris2Rs_Notifications": "pynix_hm.services.mpdris2_rs:Mpdris2Rs_Notifications",
        "Mpdris2_Mpd": "pynix_hm.services.mpdris2:Mpdris2_Mpd",
        "Mpdscribble": "pynix_hm.services.mpdscribble:Mpdscribble",
        "Mpdscribble_Endpoints_Value": "pynix_hm.services.mpdscribble:Mpdscribble_Endpoints_Value",
        "MprisProxy": "pynix_hm.services.mpris_proxy:MprisProxy",
        "Mpv": "pynix_hm.programs.mpv:Mpv",
        "Mpvpaper": "pynix_hm.programs.mpvpaper:Mpvpaper",
        "Mr": "pynix_hm.programs.mr:Mr",
        "Msmtp": "pynix_hm.programs.msmtp:Msmtp",
        "Mu": "pynix_hm.programs.mu:Mu",
        "Muchsync": "pynix_hm.services.muchsync:Muchsync",
        "Muchsync_Remotes_Value": "pynix_hm.services.muchsync:Muchsync_Remotes_Value",
        "Mujmap": "pynix_hm.programs.mujmap:Mujmap",
        "MullvadVpn": "pynix_hm.programs.mullvad_vpn:MullvadVpn",
        "Mypy": "pynix_hm.programs.mypy:Mypy",
        "Navi": "pynix_hm.programs.navi:Navi",
        "Ncmpcpp": "pynix_hm.programs.ncmpcpp:Ncmpcpp",
        "Ncmpcpp_Bindings_Item": "pynix_hm.programs.ncmpcpp:Ncmpcpp_Bindings_Item",
        "Ncspot": "pynix_hm.programs.ncspot:Ncspot",
        "Ne": "pynix_hm.programs.ne:Ne",
        "Neomutt": "pynix_hm.programs.neomutt:Neomutt",
        "Neomutt_Binds_Item": "pynix_hm.programs.neomutt:Neomutt_Binds_Item",
        "Neomutt_Sidebar": "pynix_hm.programs.neomutt:Neomutt_Sidebar",
        "Neovide": "pynix_hm.programs.neovide:Neovide",
        "Neovim": "pynix_hm.programs.neovim:Neovim",
        "Neovim_Coc": "pynix_hm.programs.neovim:Neovim_Coc",
        "Neovim_Plugins_Item_Or": "pynix_hm.programs.neovim:Neovim_Plugins_Item_Or",
        "Neovim_Plugins_Item_Or_Runtime_Value": "pynix_hm.programs.neovim:Neovim_Plugins_Item_Or_Runtime_Value",
        "NetworkManagerApplet": "pynix_hm.services.network_manager_applet:NetworkManagerApplet",
        "News": "pynix_hm.news.__options__:News",
        "News_Entries_Item": "pynix_hm.news.__options__:News_Entries_Item",
        "Newsboat": "pynix_hm.programs.newsboat:Newsboat",
        "Newsboat_AutoFetchArticles": "pynix_hm.programs.newsboat:Newsboat_AutoFetchArticles",
        "Newsboat_AutoVacuum": "pynix_hm.programs.newsboat:Newsboat_AutoVacuum",
        "Newsboat_Urls_Item": "pynix_hm.programs.newsboat:Newsboat_Urls_Item",
        "NextcloudClient": "pynix_hm.services.nextcloud_client:NextcloudClient",
        "Nh": "pynix_hm.programs.nh:Nh",
        "Nh_Clean": "pynix_hm.programs.nh:Nh_Clean",
        "Nheko": "pynix_hm.programs.nheko:Nheko",
        "NinjabrainBot": "pynix_hm.programs.ninjabrain_bot:NinjabrainBot",
        "Nix": "pynix_hm.nix.__options__:Nix",
        "NixIndex": "pynix_hm.programs.nix_index:NixIndex",
        "NixInit": "pynix_hm.programs.nix_init:NixInit",
        "NixSearchTv": "pynix_hm.programs.nix_search_tv:NixSearchTv",
        "NixYourShell": "pynix_hm.programs.nix_your_shell:NixYourShell",
        "NixYourShell_NixOutputMonitor": "pynix_hm.programs.nix_your_shell:NixYourShell_NixOutputMonitor",
        "Nix_BuildMachines_Item": "pynix_hm.nix.__options__:Nix_BuildMachines_Item",
        "Nix_Registry_Value": "pynix_hm.nix.__options__:Nix_Registry_Value",
        "Nix_Settings": "pynix_hm.nix.__options__:Nix_Settings",
        "Nixpkgs": "pynix_hm.nixpkgs.__options__:Nixpkgs",
        "Nnn": "pynix_hm.programs.nnn:Nnn",
        "Nnn_Plugins": "pynix_hm.programs.nnn:Nnn_Plugins",
        "Noctalia": "pynix_hm.programs.noctalia:Noctalia",
        "Noctalia_Systemd": "pynix_hm.programs.noctalia:Noctalia_Systemd",
        "Nom": "pynix_hm.programs.nom:Nom",
        "Noti": "pynix_hm.programs.noti:Noti",
        "NotifyOsd": "pynix_hm.services.notify_osd:NotifyOsd",
        "Notmuch": "pynix_hm.programs.notmuch:Notmuch",
        "Notmuch_Hooks": "pynix_hm.programs.notmuch:Notmuch_Hooks",
        "Npm": "pynix_hm.programs.npm:Npm",
        "Numbat": "pynix_hm.programs.numbat:Numbat",
        "Numlock": "pynix_hm.xsession.numlock:Numlock",
        "Nushell": "pynix_hm.programs.nushell:Nushell",
        "Nushell_ConfigFile": "pynix_hm.programs.nushell:Nushell_ConfigFile",
        "Nushell_EnvFile": "pynix_hm.programs.nushell:Nushell_EnvFile",
        "Nushell_LoginFile": "pynix_hm.programs.nushell:Nushell_LoginFile",
        "Nvchecker": "pynix_hm.programs.nvchecker:Nvchecker",
        "Nvchecker_Settings": "pynix_hm.programs.nvchecker:Nvchecker_Settings",
        "Nvchecker_Settings_NConfig": "pynix_hm.programs.nvchecker:Nvchecker_Settings_NConfig",
        "Nvibrant": "pynix_hm.services.nvibrant:Nvibrant",
        "Nyxt": "pynix_hm.programs.nyxt:Nyxt",
        "ObsStudio": "pynix_hm.programs.obs_studio:ObsStudio",
        "Obsidian": "pynix_hm.programs.obsidian:Obsidian",
        "Obsidian_Cli": "pynix_hm.programs.obsidian:Obsidian_Cli",
        "Obsidian_DefaultSettings": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings",
        "Obsidian_DefaultSettings_CommunityPlugins_Item": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings_CommunityPlugins_Item",
        "Obsidian_DefaultSettings_CorePlugins_Item": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings_CorePlugins_Item",
        "Obsidian_DefaultSettings_CssSnippets_Item": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings_CssSnippets_Item",
        "Obsidian_DefaultSettings_ExtraFiles_Value": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings_ExtraFiles_Value",
        "Obsidian_DefaultSettings_Hotkeys_Value_Item": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings_Hotkeys_Value_Item",
        "Obsidian_DefaultSettings_Themes_Item": "pynix_hm.programs.obsidian:Obsidian_DefaultSettings_Themes_Item",
        "Obsidian_Vaults_Value": "pynix_hm.programs.obsidian:Obsidian_Vaults_Value",
        "Offlineimap": "pynix_hm.programs.offlineimap:Offlineimap",
        "Offlineimap_ExtraConfig": "pynix_hm.programs.offlineimap:Offlineimap_ExtraConfig",
        "OhMyPosh": "pynix_hm.programs.oh_my_posh:OhMyPosh",
        "Ollama": "pynix_hm.services.ollama:Ollama",
        "Omniwm": "pynix_hm.programs.omniwm:Omniwm",
        "Omniwm_Launchd": "pynix_hm.programs.omniwm:Omniwm_Launchd",
        "Onagre": "pynix_hm.programs.onagre:Onagre",
        "Onedrive": "pynix_hm.programs.onedrive:Onedrive",
        "Onlyoffice": "pynix_hm.programs.onlyoffice:Onlyoffice",
        "Opam": "pynix_hm.programs.opam:Opam",
        "Opencode": "pynix_hm.programs.opencode:Opencode",
        "Opencode_ValidateFiles": "pynix_hm.programs.opencode:Opencode_ValidateFiles",
        "Opencode_Web": "pynix_hm.programs.opencode:Opencode_Web",
        "Openlinkhub": "pynix_hm.services.openlinkhub:Openlinkhub",
        "Openlinkhub_Dashboard": "pynix_hm.services.openlinkhub:Openlinkhub_Dashboard",
        "Openlinkhub_ExtraConfigs": "pynix_hm.services.openlinkhub:Openlinkhub_ExtraConfigs",
        "Openlinkhub_Settings": "pynix_hm.services.openlinkhub:Openlinkhub_Settings",
        "OpensnitchUi": "pynix_hm.services.opensnitch_ui:OpensnitchUi",
        "Openstackclient": "pynix_hm.programs.openstackclient:Openstackclient",
        "Openstackclient_CloudsPublicSettings_Value_Or": "pynix_hm.programs.openstackclient:Openstackclient_CloudsPublicSettings_Value_Or",
        "Opkssh": "pynix_hm.programs.opkssh:Opkssh",
        "OsmscoutServer": "pynix_hm.services.osmscout_server:OsmscoutServer",
        "OsmscoutServer_Network": "pynix_hm.services.osmscout_server:OsmscoutServer_Network",
        "OwncloudClient": "pynix_hm.services.owncloud_client:OwncloudClient",
        "Pam": "pynix_hm.pam.__options__:Pam",
        "Pandoc": "pynix_hm.programs.pandoc:Pandoc",
        "Pantalaimon": "pynix_hm.services.pantalaimon:Pantalaimon",
        "Papis": "pynix_hm.programs.papis:Papis",
        "Papis_Libraries_Value": "pynix_hm.programs.papis:Papis_Libraries_Value",
        "Parallel": "pynix_hm.programs.parallel:Parallel",
        "Parcellite": "pynix_hm.services.parcellite:Parcellite",
        "PassSecretService": "pynix_hm.services.pass_secret_service:PassSecretService",
        "PasswordStore": "pynix_hm.programs.password_store:PasswordStore",
        "Pasystray": "pynix_hm.services.pasystray:Pasystray",
        "Patdiff": "pynix_hm.programs.patdiff:Patdiff",
        "PayRespects": "pynix_hm.programs.pay_respects:PayRespects",
        "Pazi": "pynix_hm.programs.pazi:Pazi",
        "Pbgopy": "pynix_hm.services.pbgopy:Pbgopy",
        "Pbgopy_Cache": "pynix_hm.services.pbgopy:Pbgopy_Cache",
        "Pet": "pynix_hm.programs.pet:Pet",
        "Pet_Snippets_Item": "pynix_hm.programs.pet:Pet_Snippets_Item",
        "Pgcli": "pynix_hm.programs.pgcli:Pgcli",
        "PiCodingAgent": "pynix_hm.programs.pi_coding_agent:PiCodingAgent",
        "Pianobar": "pynix_hm.programs.pianobar:Pianobar",
        "Pianobar_Settings": "pynix_hm.programs.pianobar:Pianobar_Settings",
        "Picom": "pynix_hm.services.picom:Picom",
        "Pidgin": "pynix_hm.programs.pidgin:Pidgin",
        "Programs_Pimsync": "pynix_hm.programs.pimsync:Pimsync",
        "Services_Pimsync": "pynix_hm.services.pimsync:Pimsync",
        "Pipewire": "pynix_hm.services.pipewire:Pipewire",
        "Pipewire_Wireplumber": "pynix_hm.services.pipewire:Pipewire_Wireplumber",
        "Pistol": "pynix_hm.programs.pistol:Pistol",
        "Pistol_Associations_Item": "pynix_hm.programs.pistol:Pistol_Associations_Item",
        "PistonCli": "pynix_hm.programs.piston_cli:PistonCli",
        "Pizauth": "pynix_hm.services.pizauth:Pizauth",
        "Pizauth_Accounts_Value": "pynix_hm.services.pizauth:Pizauth_Accounts_Value",
        "Plan9port": "pynix_hm.services.plan9port:Plan9port",
        "Plan9port_Fontsrv": "pynix_hm.services.plan9port:Plan9port_Fontsrv",
        "Plan9port_Plumber": "pynix_hm.services.plan9port:Plan9port_Plumber",
        "Playerctld": "pynix_hm.services.playerctld:Playerctld",
        "PlexMpvShim": "pynix_hm.services.plex_mpv_shim:PlexMpvShim",
        "Pls": "pynix_hm.programs.pls:Pls",
        "Pnpm": "pynix_hm.programs.pnpm:Pnpm",
        "Podman": "pynix_hm.services.podman:Podman",
        "Podman_AutoUpdate": "pynix_hm.services.podman:Podman_AutoUpdate",
        "Podman_Builds_Value": "pynix_hm.services.podman:Podman_Builds_Value",
        "Podman_Containers_Value": "pynix_hm.services.podman:Podman_Containers_Value",
        "Podman_Images_Value": "pynix_hm.services.podman:Podman_Images_Value",
        "Podman_Internal": "pynix_hm.services.podman:Podman_Internal",
        "Podman_Internal_QuadletDefinitions_Item": "pynix_hm.services.podman:Podman_Internal_QuadletDefinitions_Item",
        "Podman_Machines_Value": "pynix_hm.services.podman:Podman_Machines_Value",
        "Podman_Networks_Value": "pynix_hm.services.podman:Podman_Networks_Value",
        "Podman_Settings": "pynix_hm.services.podman:Podman_Settings",
        "Podman_Settings_Registries": "pynix_hm.services.podman:Podman_Settings_Registries",
        "Podman_Settings_Registries_Registry_Item": "pynix_hm.services.podman:Podman_Settings_Registries_Registry_Item",
        "Podman_Volumes_Value": "pynix_hm.services.podman:Podman_Volumes_Value",
        "Poetry": "pynix_hm.programs.poetry:Poetry",
        "PolkitGnome": "pynix_hm.services.polkit_gnome:PolkitGnome",
        "Polybar": "pynix_hm.services.polybar:Polybar",
        "Pomo": "pynix_hm.programs.pomo:Pomo",
        "Portal": "pynix_hm.xdg.portal:Portal",
        "Positron": "pynix_hm.programs.positron:Positron",
        "Positron_Profiles_Value": "pynix_hm.programs.positron:Positron_Profiles_Value",
        "Positron_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.positron:Positron_Profiles_Value_Keybindings_Or_Item",
        "Posting": "pynix_hm.programs.posting:Posting",
        "Poweralertd": "pynix_hm.services.poweralertd:Poweralertd",
        "PowerlineGo": "pynix_hm.programs.powerline_go:PowerlineGo",
        "Pqiv": "pynix_hm.programs.pqiv:Pqiv",
        "Prismlauncher": "pynix_hm.programs.prismlauncher:Prismlauncher",
        "Prismlauncher_Themes_Value_Or": "pynix_hm.programs.prismlauncher:Prismlauncher_Themes_Value_Or",
        "ProtonPassAgent": "pynix_hm.services.proton_pass_agent:ProtonPassAgent",
        "ProtonmailBridge": "pynix_hm.services.protonmail_bridge:ProtonmailBridge",
        "Psd": "pynix_hm.services.psd:Psd",
        "Ptyxis": "pynix_hm.programs.ptyxis:Ptyxis",
        "Pubs": "pynix_hm.programs.pubs:Pubs",
        "Pueue": "pynix_hm.services.pueue:Pueue",
        "Pulseeffects": "pynix_hm.services.pulseeffects:Pulseeffects",
        "Pyenv": "pynix_hm.programs.pyenv:Pyenv",
        "Pylint": "pynix_hm.programs.pylint:Pylint",
        "Pyradio": "pynix_hm.programs.pyradio:Pyradio",
        "Pyradio_Stations_Item": "pynix_hm.programs.pyradio:Pyradio_Stations_Item",
        "Pyradio_Stations_Item_Buffering": "pynix_hm.programs.pyradio:Pyradio_Stations_Item_Buffering",
        "Pywal": "pynix_hm.programs.pywal:Pywal",
        "Qalculate": "pynix_hm.programs.qalculate:Qalculate",
        "Qcal": "pynix_hm.programs.qcal:Qcal",
        "Qt": "pynix_hm.qt.__options__:Qt",
        "Qt_PlatformTheme_Or": "pynix_hm.qt.__options__:Qt_PlatformTheme_Or",
        "Quickshell": "pynix_hm.programs.quickshell:Quickshell",
        "Quickshell_Systemd": "pynix_hm.programs.quickshell:Quickshell_Systemd",
        "Qutebrowser": "pynix_hm.programs.qutebrowser:Qutebrowser",
        "Programs_Radicle": "pynix_hm.programs.radicle:Radicle",
        "Services_Radicle": "pynix_hm.services.radicle:Radicle",
        "Radicle_Cli": "pynix_hm.programs.radicle:Radicle_Cli",
        "Radicle_Node": "pynix_hm.services.radicle:Radicle_Node",
        "Radicle_Node_Lazy": "pynix_hm.services.radicle:Radicle_Node_Lazy",
        "Radicle_Settings": "pynix_hm.programs.radicle:Radicle_Settings",
        "Radicle_Uri": "pynix_hm.programs.radicle:Radicle_Uri",
        "Radicle_Uri_Rad": "pynix_hm.programs.radicle:Radicle_Uri_Rad",
        "Radicle_Uri_Rad_Browser": "pynix_hm.programs.radicle:Radicle_Uri_Rad_Browser",
        "Radicle_Uri_Rad_Vscode": "pynix_hm.programs.radicle:Radicle_Uri_Rad_Vscode",
        "Radicle_Uri_WebRad": "pynix_hm.programs.radicle:Radicle_Uri_WebRad",
        "RadioActive": "pynix_hm.programs.radio_active:RadioActive",
        "RadioCli": "pynix_hm.programs.radio_cli:RadioCli",
        "RandomBackground": "pynix_hm.services.random_background:RandomBackground",
        "Ranger": "pynix_hm.programs.ranger:Ranger",
        "Ranger_Plugins_Item": "pynix_hm.programs.ranger:Ranger_Plugins_Item",
        "Ranger_Rifle_Item": "pynix_hm.programs.ranger:Ranger_Rifle_Item",
        "Rbenv": "pynix_hm.programs.rbenv:Rbenv",
        "Rbenv_Plugins_Item": "pynix_hm.programs.rbenv:Rbenv_Plugins_Item",
        "Rbw": "pynix_hm.programs.rbw:Rbw",
        "Rbw_Settings": "pynix_hm.programs.rbw:Rbw_Settings",
        "Rclone": "pynix_hm.programs.rclone:Rclone",
        "Rclone_Remotes_Value": "pynix_hm.programs.rclone:Rclone_Remotes_Value",
        "Rclone_Remotes_Value_Mounts_Value": "pynix_hm.programs.rclone:Rclone_Remotes_Value_Mounts_Value",
        "Rclone_Remotes_Value_Serve_Value": "pynix_hm.programs.rclone:Rclone_Remotes_Value_Serve_Value",
        "Readest": "pynix_hm.programs.readest:Readest",
        "Readline": "pynix_hm.programs.readline:Readline",
        "Recoll": "pynix_hm.services.recoll:Recoll",
        "Rectangle": "pynix_hm.programs.rectangle:Rectangle",
        "Rectangle_Shortcuts_Value": "pynix_hm.programs.rectangle:Rectangle_Shortcuts_Value",
        "Redshift": "pynix_hm.services.redshift:Redshift",
        "Redshift_Settings": "pynix_hm.services.redshift:Redshift_Settings",
        "Redshift_Temperature": "pynix_hm.services.redshift:Redshift_Temperature",
        "Remmina": "pynix_hm.services.remmina:Remmina",
        "Remmina_SystemdService": "pynix_hm.services.remmina:Remmina_SystemdService",
        "Rescrobbled": "pynix_hm.services.rescrobbled:Rescrobbled",
        "Restic": "pynix_hm.services.restic:Restic",
        "Restic_Backups_Value": "pynix_hm.services.restic:Restic_Backups_Value",
        "Retext": "pynix_hm.programs.retext:Retext",
        "Retroarch": "pynix_hm.programs.retroarch:Retroarch",
        "Retroarch_Cores_Value": "pynix_hm.programs.retroarch:Retroarch_Cores_Value",
        "Riff": "pynix_hm.programs.riff:Riff",
        "Rio": "pynix_hm.programs.rio:Rio",
        "Ripasso": "pynix_hm.programs.ripasso:Ripasso",
        "Ripgrep": "pynix_hm.programs.ripgrep:Ripgrep",
        "RipgrepAll": "pynix_hm.programs.ripgrep_all:RipgrepAll",
        "RipgrepAll_CustomAdapters_Item": "pynix_hm.programs.ripgrep_all:RipgrepAll_CustomAdapters_Item",
        "Rizin": "pynix_hm.programs.rizin:Rizin",
        "Rmpc": "pynix_hm.programs.rmpc:Rmpc",
        "Rofi": "pynix_hm.programs.rofi:Rofi",
        "Rofi_Modes_Item_Or": "pynix_hm.programs.rofi:Rofi_Modes_Item_Or",
        "Rofi_Settings_Value_Value_Or": "pynix_hm.programs.rofi:Rofi_Settings_Value_Value_Or",
        "Rsibreak": "pynix_hm.services.rsibreak:Rsibreak",
        "Rtorrent": "pynix_hm.programs.rtorrent:Rtorrent",
        "Ruff": "pynix_hm.programs.ruff:Ruff",
        "Safeeyes": "pynix_hm.services.safeeyes:Safeeyes",
        "Sagemath": "pynix_hm.programs.sagemath:Sagemath",
        "Sapling": "pynix_hm.programs.sapling:Sapling",
        "Satty": "pynix_hm.programs.satty:Satty",
        "Sbt": "pynix_hm.programs.sbt:Sbt",
        "Sbt_Credentials_Item": "pynix_hm.programs.sbt:Sbt_Credentials_Item",
        "Sbt_Plugins_Item": "pynix_hm.programs.sbt:Sbt_Plugins_Item",
        "Scmpuff": "pynix_hm.programs.scmpuff:Scmpuff",
        "Screen": "pynix_hm.programs.screen:Screen",
        "ScreenLocker": "pynix_hm.services.screen_locker:ScreenLocker",
        "ScreenLocker_Xautolock": "pynix_hm.services.screen_locker:ScreenLocker_Xautolock",
        "ScreenLocker_XssLock": "pynix_hm.services.screen_locker:ScreenLocker_XssLock",
        "ScriptDirectory": "pynix_hm.programs.script_directory:ScriptDirectory",
        "Sctd": "pynix_hm.services.sctd:Sctd",
        "Secretspec": "pynix_hm.programs.secretspec:Secretspec",
        "Senpai": "pynix_hm.programs.senpai:Senpai",
        "Senpai_Config": "pynix_hm.programs.senpai:Senpai_Config",
        "Sesh": "pynix_hm.programs.sesh:Sesh",
        "Sesh_Settings": "pynix_hm.programs.sesh:Sesh_Settings",
        "Sftpman": "pynix_hm.programs.sftpman:Sftpman",
        "Sftpman_Mounts_Value": "pynix_hm.programs.sftpman:Sftpman_Mounts_Value",
        "Sheldon": "pynix_hm.programs.sheldon:Sheldon",
        "Shell": "pynix_hm.home.shell:Shell",
        "Sherlock": "pynix_hm.programs.sherlock:Sherlock",
        "Sherlock_Systemd": "pynix_hm.programs.sherlock:Sherlock_Systemd",
        "Shikane": "pynix_hm.services.shikane:Shikane",
        "Shpool": "pynix_hm.services.shpool:Shpool",
        "Signaturepdf": "pynix_hm.services.signaturepdf:Signaturepdf",
        "Sioyek": "pynix_hm.programs.sioyek:Sioyek",
        "Sioyek_Config": "pynix_hm.programs.sioyek:Sioyek_Config",
        "Sketchybar": "pynix_hm.programs.sketchybar:Sketchybar",
        "Sketchybar_Config_Or": "pynix_hm.programs.sketchybar:Sketchybar_Config_Or",
        "Sketchybar_Service": "pynix_hm.programs.sketchybar:Sketchybar_Service",
        "Skhd": "pynix_hm.services.skhd:Skhd",
        "Skim": "pynix_hm.programs.skim:Skim",
        "Sm64ex": "pynix_hm.programs.sm64ex:Sm64ex",
        "Smug": "pynix_hm.programs.smug:Smug",
        "Smug_Projects_Value": "pynix_hm.programs.smug:Smug_Projects_Value",
        "Smug_Projects_Value_Windows_Item": "pynix_hm.programs.smug:Smug_Projects_Value_Windows_Item",
        "Smug_Projects_Value_Windows_Item_Panes_Item": "pynix_hm.programs.smug:Smug_Projects_Value_Windows_Item_Panes_Item",
        "Snixembed": "pynix_hm.services.snixembed:Snixembed",
        "SpotifyPlayer": "pynix_hm.programs.spotify_player:SpotifyPlayer",
        "Spotifyd": "pynix_hm.services.spotifyd:Spotifyd",
        "Sqls": "pynix_hm.programs.sqls:Sqls",
        "Ssh": "pynix_hm.programs.ssh:Ssh",
        "SshAgent": "pynix_hm.services.ssh_agent:SshAgent",
        "SshAuthSock": "pynix_hm.sshAuthSock.__options__:SshAuthSock",
        "SshTpmAgent": "pynix_hm.services.ssh_tpm_agent:SshTpmAgent",
        "Stalonetray": "pynix_hm.services.stalonetray:Stalonetray",
        "Starship": "pynix_hm.programs.starship:Starship",
        "Starship_ValidateFiles": "pynix_hm.programs.starship:Starship_ValidateFiles",
        "StatusNotifierWatcher": "pynix_hm.services.status_notifier_watcher:StatusNotifierWatcher",
        "Streamlink": "pynix_hm.programs.streamlink:Streamlink",
        "Streamlink_Plugins_Value": "pynix_hm.programs.streamlink:Streamlink_Plugins_Value",
        "Style": "pynix_hm.qt.style:Style",
        "Stylua": "pynix_hm.programs.stylua:Stylua",
        "SubmoduleSupport": "pynix_hm.submoduleSupport.__options__:SubmoduleSupport",
        "Superfile": "pynix_hm.programs.superfile:Superfile",
        "Superfile_PinnedFolders_Item": "pynix_hm.programs.superfile:Superfile_PinnedFolders_Item",
        "Swappy": "pynix_hm.programs.swappy:Swappy",
        "SwayEasyfocus": "pynix_hm.programs.sway_easyfocus:SwayEasyfocus",
        "Swayidle": "pynix_hm.services.swayidle:Swayidle",
        "Swayidle_Events": "pynix_hm.services.swayidle:Swayidle_Events",
        "Swayidle_Timeouts_Item": "pynix_hm.services.swayidle:Swayidle_Timeouts_Item",
        "Swayimg": "pynix_hm.programs.swayimg:Swayimg",
        "Swaylock": "pynix_hm.programs.swaylock:Swaylock",
        "Swaync": "pynix_hm.services.swaync:Swaync",
        "Swayosd": "pynix_hm.services.swayosd:Swayosd",
        "Swayr": "pynix_hm.programs.swayr:Swayr",
        "Swayr_Systemd": "pynix_hm.programs.swayr:Swayr_Systemd",
        "Sxhkd": "pynix_hm.services.sxhkd:Sxhkd",
        "Syncthing": "pynix_hm.services.syncthing:Syncthing",
        "Syncthing_GuiCredentials": "pynix_hm.services.syncthing:Syncthing_GuiCredentials",
        "Syncthing_Settings": "pynix_hm.services.syncthing:Syncthing_Settings",
        "Syncthing_Settings_Devices_Value": "pynix_hm.services.syncthing:Syncthing_Settings_Devices_Value",
        "Syncthing_Settings_Folders_Value": "pynix_hm.services.syncthing:Syncthing_Settings_Folders_Value",
        "Syncthing_Settings_Folders_Value_Devices_Item_Or": "pynix_hm.services.syncthing:Syncthing_Settings_Folders_Value_Devices_Item_Or",
        "Syncthing_Settings_Folders_Value_Versioning": "pynix_hm.services.syncthing:Syncthing_Settings_Folders_Value_Versioning",
        "Syncthing_Settings_Options": "pynix_hm.services.syncthing:Syncthing_Settings_Options",
        "Syncthing_Tray": "pynix_hm.services.syncthing:Syncthing_Tray",
        "Syshud": "pynix_hm.services.syshud:Syshud",
        "SystemDirs": "pynix_hm.xdg.systemDirs:SystemDirs",
        "SystembusNotify": "pynix_hm.services.systembus_notify:SystembusNotify",
        "SshAuthSock_Systemd": "pynix_hm.sshAuthSock.systemd:Systemd",
        "Wayland_Systemd": "pynix_hm.wayland.systemd:Systemd",
        "T3code": "pynix_hm.programs.t3code:T3code",
        "Taffybar": "pynix_hm.services.taffybar:Taffybar",
        "TahoeLafs": "pynix_hm.services.tahoe_lafs:TahoeLafs",
        "TailscaleSystray": "pynix_hm.services.tailscale_systray:TailscaleSystray",
        "Taskwarrior": "pynix_hm.programs.taskwarrior:Taskwarrior",
        "TaskwarriorSync": "pynix_hm.services.taskwarrior_sync:TaskwarriorSync",
        "Tealdeer": "pynix_hm.programs.tealdeer:Tealdeer",
        "Tealdeer_Settings": "pynix_hm.programs.tealdeer:Tealdeer_Settings",
        "Tealdeer_Settings_Updates": "pynix_hm.programs.tealdeer:Tealdeer_Settings_Updates",
        "Television": "pynix_hm.programs.television:Television",
        "TerminalExec": "pynix_hm.xdg.terminal_exec:TerminalExec",
        "Terminator": "pynix_hm.programs.terminator:Terminator",
        "Termite": "pynix_hm.programs.termite:Termite",
        "TexFmt": "pynix_hm.programs.tex_fmt:TexFmt",
        "Texlive": "pynix_hm.programs.texlive:Texlive",
        "Thunderbird": "pynix_hm.programs.thunderbird:Thunderbird",
        "Thunderbird_Profiles_Value": "pynix_hm.programs.thunderbird:Thunderbird_Profiles_Value",
        "Thunderbird_Profiles_Value_FeedAccounts_Value": "pynix_hm.programs.thunderbird:Thunderbird_Profiles_Value_FeedAccounts_Value",
        "Thunderbird_Profiles_Value_Search": "pynix_hm.programs.thunderbird:Thunderbird_Profiles_Value_Search",
        "Timidity": "pynix_hm.programs.timidity:Timidity",
        "Tint2": "pynix_hm.programs.tint2:Tint2",
        "Tiny": "pynix_hm.programs.tiny:Tiny",
        "Tirith": "pynix_hm.programs.tirith:Tirith",
        "TldrUpdate": "pynix_hm.services.tldr_update:TldrUpdate",
        "Tmate": "pynix_hm.programs.tmate:Tmate",
        "Tmux": "pynix_hm.programs.tmux:Tmux",
        "Tmux_Plugins_Item_Or": "pynix_hm.programs.tmux:Tmux_Plugins_Item_Or",
        "Tmux_Tmuxinator": "pynix_hm.programs.tmux:Tmux_Tmuxinator",
        "Tmux_Tmuxp": "pynix_hm.programs.tmux:Tmux_Tmuxp",
        "Todoman": "pynix_hm.programs.todoman:Todoman",
        "Tofi": "pynix_hm.programs.tofi:Tofi",
        "Tomat": "pynix_hm.services.tomat:Tomat",
        "Tomat_Settings": "pynix_hm.services.tomat:Tomat_Settings",
        "Top": "pynix_hm.top:Top",
        "Top_Specialisation_Value": "pynix_hm.top:Top_Specialisation_Value",
        "Topgrade": "pynix_hm.programs.topgrade:Topgrade",
        "TranslateShell": "pynix_hm.programs.translate_shell:TranslateShell",
        "TrayTui": "pynix_hm.programs.tray_tui:TrayTui",
        "Trayer": "pynix_hm.services.trayer:Trayer",
        "Trayscale": "pynix_hm.services.trayscale:Trayscale",
        "Trippy": "pynix_hm.programs.trippy:Trippy",
        "Ttyper": "pynix_hm.programs.ttyper:Ttyper",
        "TwitchTui": "pynix_hm.programs.twitch_tui:TwitchTui",
        "Twmn": "pynix_hm.services.twmn:Twmn",
        "Twmn_Text": "pynix_hm.services.twmn:Twmn_Text",
        "Twmn_Text_Font": "pynix_hm.services.twmn:Twmn_Text_Font",
        "Twmn_Window": "pynix_hm.services.twmn:Twmn_Window",
        "Twmn_Window_Animation": "pynix_hm.services.twmn:Twmn_Window_Animation",
        "Twmn_Window_Animation_EaseIn_Or": "pynix_hm.services.twmn:Twmn_Window_Animation_EaseIn_Or",
        "Ty": "pynix_hm.programs.ty:Ty",
        "Udiskie": "pynix_hm.services.udiskie:Udiskie",
        "Unclutter": "pynix_hm.services.unclutter:Unclutter",
        "Unison": "pynix_hm.services.unison:Unison",
        "Unison_Pairs_Value": "pynix_hm.services.unison:Unison_Pairs_Value",
        "Urxvt": "pynix_hm.programs.urxvt:Urxvt",
        "Urxvt_Scroll": "pynix_hm.programs.urxvt:Urxvt_Scroll",
        "Urxvt_Scroll_Bar": "pynix_hm.programs.urxvt:Urxvt_Scroll_Bar",
        "User": "pynix_hm.systemd.user:User",
        "UserDirs": "pynix_hm.xdg.userDirs:UserDirs",
        "User_Automounts_Value": "pynix_hm.systemd.user:User_Automounts_Value",
        "User_Services_Value": "pynix_hm.systemd.user:User_Services_Value",
        "User_Settings": "pynix_hm.systemd.user:User_Settings",
        "User_Tmpfiles": "pynix_hm.systemd.user:User_Tmpfiles",
        "Uv": "pynix_hm.programs.uv:Uv",
        "Uv_Python": "pynix_hm.programs.uv:Uv_Python",
        "Uv_Tool": "pynix_hm.programs.uv:Uv_Tool",
        "Programs_Vdirsyncer": "pynix_hm.programs.vdirsyncer:Vdirsyncer",
        "Services_Vdirsyncer": "pynix_hm.services.vdirsyncer:Vdirsyncer",
        "Vdirsyncer": "pynix_hm.vdirsyncer.__options__:Vdirsyncer",
        "Vdirsyncer_TimeRange": "pynix_hm.vdirsyncer.__options__:Vdirsyncer_TimeRange",
        "Version": "pynix_hm.home.version:Version",
        "Vesktop": "pynix_hm.programs.vesktop:Vesktop",
        "Vesktop_Vencord": "pynix_hm.programs.vesktop:Vesktop_Vencord",
        "Vicinae": "pynix_hm.programs.vicinae:Vicinae",
        "Vicinae_Systemd": "pynix_hm.programs.vicinae:Vicinae_Systemd",
        "Vifm": "pynix_hm.programs.vifm:Vifm",
        "Vim": "pynix_hm.programs.vim:Vim",
        "VimVint": "pynix_hm.programs.vim_vint:VimVint",
        "Vim_Settings": "pynix_hm.programs.vim:Vim_Settings",
        "Vinegar": "pynix_hm.programs.vinegar:Vinegar",
        "Visidata": "pynix_hm.programs.visidata:Visidata",
        "Vivaldi": "pynix_hm.programs.vivaldi:Vivaldi",
        "Vivaldi_Extensions_Item": "pynix_hm.programs.vivaldi:Vivaldi_Extensions_Item",
        "Vivid": "pynix_hm.programs.vivid:Vivid",
        "Volnoti": "pynix_hm.services.volnoti:Volnoti",
        "Voxtype": "pynix_hm.services.voxtype:Voxtype",
        "Voxtype_Wayland": "pynix_hm.services.voxtype:Voxtype_Wayland",
        "Voxtype_X11": "pynix_hm.services.voxtype:Voxtype_X11",
        "Vscode": "pynix_hm.programs.vscode:Vscode",
        "Vscode_Haskell": "pynix_hm.programs.vscode:Vscode_Haskell",
        "Vscode_Haskell_Hie": "pynix_hm.programs.vscode:Vscode_Haskell_Hie",
        "Vscode_Profiles_Value": "pynix_hm.programs.vscode:Vscode_Profiles_Value",
        "Vscode_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.vscode:Vscode_Profiles_Value_Keybindings_Or_Item",
        "Vscodium": "pynix_hm.programs.vscodium:Vscodium",
        "Vscodium_Profiles_Value": "pynix_hm.programs.vscodium:Vscodium_Profiles_Value",
        "Vscodium_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.vscodium:Vscodium_Profiles_Value_Keybindings_Or_Item",
        "W3m": "pynix_hm.programs.w3m:W3m",
        "W3m_Bookmarks": "pynix_hm.programs.w3m:W3m_Bookmarks",
        "W3m_Bookmarks_Marks_Value_Item": "pynix_hm.programs.w3m:W3m_Bookmarks_Marks_Value_Item",
        "W3m_CgiBin_Value": "pynix_hm.programs.w3m:W3m_CgiBin_Value",
        "W3m_Siteconf_Item": "pynix_hm.programs.w3m:W3m_Siteconf_Item",
        "Walker": "pynix_hm.services.walker:Walker",
        "Walker_Systemd": "pynix_hm.services.walker:Walker_Systemd",
        "Walker_Theme": "pynix_hm.services.walker:Walker_Theme",
        "Wallust": "pynix_hm.programs.wallust:Wallust",
        "Watson": "pynix_hm.programs.watson:Watson",
        "Waveterm": "pynix_hm.programs.waveterm:Waveterm",
        "WayDisplays": "pynix_hm.services.way_displays:WayDisplays",
        "Waybar": "pynix_hm.programs.waybar:Waybar",
        "Waybar_Settings_Item": "pynix_hm.programs.waybar:Waybar_Settings_Item",
        "Waybar_Systemd": "pynix_hm.programs.waybar:Waybar_Systemd",
        "Wayle": "pynix_hm.services.wayle:Wayle",
        "Waylogout": "pynix_hm.programs.waylogout:Waylogout",
        "Wayprompt": "pynix_hm.programs.wayprompt:Wayprompt",
        "Wayvnc": "pynix_hm.services.wayvnc:Wayvnc",
        "Wayvnc_Settings": "pynix_hm.services.wayvnc:Wayvnc_Settings",
        "Wbg": "pynix_hm.services.wbg:Wbg",
        "Wezterm": "pynix_hm.programs.wezterm:Wezterm",
        "Wayland_WindowManager": "pynix_hm.wayland.windowManager:WindowManager",
        "Xsession_WindowManager": "pynix_hm.xsession.windowManager:WindowManager",
        "WindowManager_Awesome": "pynix_hm.xsession.windowManager:WindowManager_Awesome",
        "WindowManager_Bspwm": "pynix_hm.xsession.windowManager:WindowManager_Bspwm",
        "WindowManager_Bspwm_Rules_Value": "pynix_hm.xsession.windowManager:WindowManager_Bspwm_Rules_Value",
        "WindowManager_Exwm": "pynix_hm.xsession.windowManager:WindowManager_Exwm",
        "WindowManager_Fluxbox": "pynix_hm.xsession.windowManager:WindowManager_Fluxbox",
        "WindowManager_Herbstluftwm": "pynix_hm.xsession.windowManager:WindowManager_Herbstluftwm",
        "WindowManager_Hyprland": "pynix_hm.wayland.windowManager:WindowManager_Hyprland",
        "WindowManager_Hyprland_ExtraLuaFiles_Value": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_ExtraLuaFiles_Value",
        "WindowManager_Hyprland_Submaps_Value": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Submaps_Value",
        "WindowManager_Hyprland_Systemd": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Systemd",
        "WindowManager_Hyprland_Xdph": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Xdph",
        "WindowManager_Hyprland_Xdph_Settings": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Xdph_Settings",
        "WindowManager_Hyprland_Xdph_Settings_General": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Xdph_Settings_General",
        "WindowManager_Hyprland_Xdph_Settings_Screencopy": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Xdph_Settings_Screencopy",
        "WindowManager_Hyprland_Xwayland": "pynix_hm.wayland.windowManager:WindowManager_Hyprland_Xwayland",
        "WindowManager_I3": "pynix_hm.xsession.windowManager:WindowManager_I3",
        "WindowManager_I3_Config": "pynix_hm.xsession.windowManager:WindowManager_I3_Config",
        "WindowManager_I3_Config_Bars_Item": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Bars_Item",
        "WindowManager_I3_Config_Bars_Item_Colors": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Bars_Item_Colors",
        "WindowManager_I3_Config_Bars_Item_Colors_ActiveWorkspace": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Bars_Item_Colors_ActiveWorkspace",
        "WindowManager_I3_Config_Colors": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Colors",
        "WindowManager_I3_Config_Colors_Focused": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Colors_Focused",
        "WindowManager_I3_Config_Floating": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Floating",
        "WindowManager_I3_Config_Focus": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Focus",
        "WindowManager_I3_Config_Fonts_Or": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Fonts_Or",
        "WindowManager_I3_Config_Gaps": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Gaps",
        "WindowManager_I3_Config_Startup_Item": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Startup_Item",
        "WindowManager_I3_Config_Window": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Window",
        "WindowManager_I3_Config_Window_Commands_Item": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_Window_Commands_Item",
        "WindowManager_I3_Config_WorkspaceOutputAssign_Item": "pynix_hm.xsession.windowManager:WindowManager_I3_Config_WorkspaceOutputAssign_Item",
        "WindowManager_Labwc": "pynix_hm.wayland.windowManager:WindowManager_Labwc",
        "WindowManager_Labwc_Rc": "pynix_hm.wayland.windowManager:WindowManager_Labwc_Rc",
        "WindowManager_Labwc_Systemd": "pynix_hm.wayland.windowManager:WindowManager_Labwc_Systemd",
        "WindowManager_Labwc_Xwayland": "pynix_hm.wayland.windowManager:WindowManager_Labwc_Xwayland",
        "WindowManager_Niri": "pynix_hm.wayland.windowManager:WindowManager_Niri",
        "WindowManager_Niri_Systemd": "pynix_hm.wayland.windowManager:WindowManager_Niri_Systemd",
        "WindowManager_River": "pynix_hm.wayland.windowManager:WindowManager_River",
        "WindowManager_River_Systemd": "pynix_hm.wayland.windowManager:WindowManager_River_Systemd",
        "WindowManager_River_Xwayland": "pynix_hm.wayland.windowManager:WindowManager_River_Xwayland",
        "WindowManager_Spectrwm": "pynix_hm.xsession.windowManager:WindowManager_Spectrwm",
        "WindowManager_Sway": "pynix_hm.wayland.windowManager:WindowManager_Sway",
        "WindowManager_Sway_Config": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config",
        "WindowManager_Sway_Config_Bars_Item": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Bars_Item",
        "WindowManager_Sway_Config_Bars_Item_Colors": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Bars_Item_Colors",
        "WindowManager_Sway_Config_Bars_Item_Colors_ActiveWorkspace": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Bars_Item_Colors_ActiveWorkspace",
        "WindowManager_Sway_Config_Bindswitches_Value": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Bindswitches_Value",
        "WindowManager_Sway_Config_Colors": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Colors",
        "WindowManager_Sway_Config_Colors_Focused": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Colors_Focused",
        "WindowManager_Sway_Config_Floating": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Floating",
        "WindowManager_Sway_Config_Focus": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Focus",
        "WindowManager_Sway_Config_Fonts_Or": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Fonts_Or",
        "WindowManager_Sway_Config_Gaps": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Gaps",
        "WindowManager_Sway_Config_Startup_Item": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Startup_Item",
        "WindowManager_Sway_Config_Window": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Window",
        "WindowManager_Sway_Config_Window_Commands_Item": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_Window_Commands_Item",
        "WindowManager_Sway_Config_WorkspaceOutputAssign_Item": "pynix_hm.wayland.windowManager:WindowManager_Sway_Config_WorkspaceOutputAssign_Item",
        "WindowManager_Sway_Swaynag": "pynix_hm.wayland.windowManager:WindowManager_Sway_Swaynag",
        "WindowManager_Sway_Systemd": "pynix_hm.wayland.windowManager:WindowManager_Sway_Systemd",
        "WindowManager_Sway_WrapperFeatures": "pynix_hm.wayland.windowManager:WindowManager_Sway_WrapperFeatures",
        "WindowManager_Wayfire": "pynix_hm.wayland.windowManager:WindowManager_Wayfire",
        "WindowManager_Wayfire_Settings": "pynix_hm.wayland.windowManager:WindowManager_Wayfire_Settings",
        "WindowManager_Wayfire_Systemd": "pynix_hm.wayland.windowManager:WindowManager_Wayfire_Systemd",
        "WindowManager_Wayfire_WfShell": "pynix_hm.wayland.windowManager:WindowManager_Wayfire_WfShell",
        "WindowManager_Wayfire_Xwayland": "pynix_hm.wayland.windowManager:WindowManager_Wayfire_Xwayland",
        "WindowManager_Xmonad": "pynix_hm.xsession.windowManager:WindowManager_Xmonad",
        "Windsurf": "pynix_hm.programs.windsurf:Windsurf",
        "Windsurf_Profiles_Value": "pynix_hm.programs.windsurf:Windsurf_Profiles_Value",
        "Windsurf_Profiles_Value_Keybindings_Or_Item": "pynix_hm.programs.windsurf:Windsurf_Profiles_Value_Keybindings_Or_Item",
        "Wiremix": "pynix_hm.programs.wiremix:Wiremix",
        "WlClipPersist": "pynix_hm.services.wl_clip_persist:WlClipPersist",
        "Wleave": "pynix_hm.programs.wleave:Wleave",
        "Wlogout": "pynix_hm.programs.wlogout:Wlogout",
        "Wlogout_Layout_Item": "pynix_hm.programs.wlogout:Wlogout_Layout_Item",
        "WlrWhichKey": "pynix_hm.programs.wlr_which_key:WlrWhichKey",
        "Wlsunset": "pynix_hm.services.wlsunset:Wlsunset",
        "Wlsunset_Temperature": "pynix_hm.services.wlsunset:Wlsunset_Temperature",
        "Wluma": "pynix_hm.services.wluma:Wluma",
        "Wluma_Systemd": "pynix_hm.services.wluma:Wluma_Systemd",
        "Wob": "pynix_hm.services.wob:Wob",
        "Wofi": "pynix_hm.programs.wofi:Wofi",
        "Workstyle": "pynix_hm.programs.workstyle:Workstyle",
        "Workstyle_Systemd": "pynix_hm.programs.workstyle:Workstyle_Systemd",
        "Worktrunk": "pynix_hm.programs.worktrunk:Worktrunk",
        "Worktrunk_ClaudeCodeIntegration": "pynix_hm.programs.worktrunk:Worktrunk_ClaudeCodeIntegration",
        "Wpaperd": "pynix_hm.services.wpaperd:Wpaperd",
        "Xcape": "pynix_hm.services.xcape:Xcape",
        "Xdg": "pynix_hm.xdg.__options__:Xdg",
        "Xdg_CacheFile_Value": "pynix_hm.xdg.__options__:Xdg_CacheFile_Value",
        "Xdg_ConfigFile_Value": "pynix_hm.xdg.__options__:Xdg_ConfigFile_Value",
        "Xdg_DataFile_Value": "pynix_hm.xdg.__options__:Xdg_DataFile_Value",
        "Xdg_DesktopEntries_Value": "pynix_hm.xdg.__options__:Xdg_DesktopEntries_Value",
        "Xdg_DesktopEntries_Value_Actions_Value": "pynix_hm.xdg.__options__:Xdg_DesktopEntries_Value_Actions_Value",
        "Xdg_StateFile_Value": "pynix_hm.xdg.__options__:Xdg_StateFile_Value",
        "XembedSniProxy": "pynix_hm.services.xembed_sni_proxy:XembedSniProxy",
        "Xfconf": "pynix_hm.xfconf.__options__:Xfconf",
        "Xfconf_Settings_Value_Value_Or": "pynix_hm.xfconf.__options__:Xfconf_Settings_Value_Value_Or",
        "Xidlehook": "pynix_hm.services.xidlehook:Xidlehook",
        "Xidlehook_Timers_Item": "pynix_hm.services.xidlehook:Xidlehook_Timers_Item",
        "Xmobar": "pynix_hm.programs.xmobar:Xmobar",
        "Xplr": "pynix_hm.programs.xplr:Xplr",
        "Xresources": "pynix_hm.xresources.__options__:Xresources",
        "Xscreensaver": "pynix_hm.services.xscreensaver:Xscreensaver",
        "Xsession": "pynix_hm.xsession.__options__:Xsession",
        "Xsettingsd": "pynix_hm.services.xsettingsd:Xsettingsd",
        "Xsuspender": "pynix_hm.services.xsuspender:Xsuspender",
        "Xsuspender_Settings_Value": "pynix_hm.services.xsuspender:Xsuspender_Settings_Value",
        "Yambar": "pynix_hm.programs.yambar:Yambar",
        "Yambar_Systemd": "pynix_hm.programs.yambar:Yambar_Systemd",
        "Yarn": "pynix_hm.programs.yarn:Yarn",
        "Yazi": "pynix_hm.programs.yazi:Yazi",
        "Yazi_Plugins_Value": "pynix_hm.programs.yazi:Yazi_Plugins_Value",
        "Yofi": "pynix_hm.programs.yofi:Yofi",
        "Yopass": "pynix_hm.programs.yopass:Yopass",
        "YtDlp": "pynix_hm.programs.yt_dlp:YtDlp",
        "Yubico": "pynix_hm.pam.yubico:Yubico",
        "Yubico_AuthorizedYubiKeys": "pynix_hm.pam.yubico:Yubico_AuthorizedYubiKeys",
        "YubikeyAgent": "pynix_hm.services.yubikey_agent:YubikeyAgent",
        "ZLua": "pynix_hm.programs.z_lua:ZLua",
        "Zapzap": "pynix_hm.programs.zapzap:Zapzap",
        "Zathura": "pynix_hm.programs.zathura:Zathura",
        "ZedEditor": "pynix_hm.programs.zed_editor:ZedEditor",
        "Zellij": "pynix_hm.programs.zellij:Zellij",
        "Zk": "pynix_hm.programs.zk:Zk",
        "Zoxide": "pynix_hm.programs.zoxide:Zoxide",
        "Zsh": "pynix_hm.programs.zsh:Zsh",
        "Zsh_Antidote": "pynix_hm.programs.zsh:Zsh_Antidote",
        "Zsh_Autosuggestion": "pynix_hm.programs.zsh:Zsh_Autosuggestion",
        "Zsh_FastSyntaxHighlighting": "pynix_hm.programs.zsh:Zsh_FastSyntaxHighlighting",
        "Zsh_History": "pynix_hm.programs.zsh:Zsh_History",
        "Zsh_HistorySubstringSearch": "pynix_hm.programs.zsh:Zsh_HistorySubstringSearch",
        "Zsh_OhMyZsh": "pynix_hm.programs.zsh:Zsh_OhMyZsh",
        "Zsh_Plugins_Item": "pynix_hm.programs.zsh:Zsh_Plugins_Item",
        "Zsh_Prezto": "pynix_hm.programs.zsh:Zsh_Prezto",
        "Zsh_SyntaxHighlighting": "pynix_hm.programs.zsh:Zsh_SyntaxHighlighting",
        "Zsh_Zplug": "pynix_hm.programs.zsh:Zsh_Zplug",
        "Zsh_Zplug_Plugins_Item": "pynix_hm.programs.zsh:Zsh_Zplug_Plugins_Item",
        "Zsh_Zprof": "pynix_hm.programs.zsh:Zsh_Zprof",
        "Zsh_ZshAbbr": "pynix_hm.programs.zsh:Zsh_ZshAbbr",
    }

    def __getattr__(name: str) -> _Any:
        try:
            target = _INDEX[name]
        except KeyError:
            close = [n for n, t in _INDEX.items() if t.endswith(":" + name) and n != name]
            hint = f" Two classes have this name. Write one of: {', '.join(close)}." if close else ""
            raise AttributeError(f"The flat list of {__name__.split('.')[0]} has no class {name}.{hint}") from None
        module, _, real = target.partition(":")
        value = getattr(_import_module(module), real)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(_INDEX)
