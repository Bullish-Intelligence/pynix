"""Every class of pynix_os in one flat namespace. Generated; do not edit.

`from pynix_os import all as nixos`, then `nixos.Loader(efi=nixos.Loader_Efi(...))`. Python loads the module of a name at its first use.
"""

from importlib import import_module as _import_module
from typing import TYPE_CHECKING as _TYPE_CHECKING, Any as _Any

if _TYPE_CHECKING:  # the type checker reads these lines; Python skips them
    from pynix_os.appstream.__options__ import Appstream as Appstream
    from pynix_os.boot.__options__ import Boot as Boot, Boot_SpecialFileSystems_Value as Boot_SpecialFileSystems_Value
    from pynix_os.boot.bcache import Bcache as Bcache
    from pynix_os.boot.bcachefs import Bcachefs as Boot_Bcachefs
    from pynix_os.boot.binfmt import Binfmt as Binfmt, Binfmt_Registrations_Value as Binfmt_Registrations_Value
    from pynix_os.boot.bootspec import Bootspec as Bootspec
    from pynix_os.boot.crashDump import CrashDump as CrashDump
    from pynix_os.boot.initrd import (
        Initrd as Initrd,
        Initrd_Clevis as Initrd_Clevis,
        Initrd_ClevisLuksAskpass as Initrd_ClevisLuksAskpass,
        Initrd_Clevis_Devices_Value as Initrd_Clevis_Devices_Value,
        Initrd_ExtraFiles_Value as Initrd_ExtraFiles_Value,
        Initrd_Luks as Initrd_Luks,
        Initrd_Luks_Devices_Value as Initrd_Luks_Devices_Value,
        Initrd_Luks_Devices_Value_GpgCard as Initrd_Luks_Devices_Value_GpgCard,
        Initrd_Luks_Devices_Value_Yubikey as Initrd_Luks_Devices_Value_Yubikey,
        Initrd_Network as Initrd_Network,
        Initrd_Network_Ifstate as Initrd_Network_Ifstate,
        Initrd_Network_Openvpn as Initrd_Network_Openvpn,
        Initrd_Network_Ssh as Initrd_Network_Ssh,
        Initrd_Network_Udhcpc as Initrd_Network_Udhcpc,
        Initrd_NixStoreVeritysetup as Initrd_NixStoreVeritysetup,
        Initrd_Services as Initrd_Services,
        Initrd_Services_Bcache as Initrd_Services_Bcache,
        Initrd_Services_Lvm as Initrd_Services_Lvm,
        Initrd_Services_Resolved as Initrd_Services_Resolved,
        Initrd_Services_Udev as Initrd_Services_Udev,
        Initrd_Systemd as Initrd_Systemd,
        Initrd_Systemd_Automounts_Item as Initrd_Systemd_Automounts_Item,
        Initrd_Systemd_Contents_Value as Initrd_Systemd_Contents_Value,
        Initrd_Systemd_Dbus as Initrd_Systemd_Dbus,
        Initrd_Systemd_DmVerity as Initrd_Systemd_DmVerity,
        Initrd_Systemd_Fido2 as Initrd_Systemd_Fido2,
        Initrd_Systemd_Groups_Value as Initrd_Systemd_Groups_Value,
        Initrd_Systemd_Mounts_Item as Initrd_Systemd_Mounts_Item,
        Initrd_Systemd_Network as Initrd_Systemd_Network,
        Initrd_Systemd_Network_Config as Initrd_Systemd_Network_Config,
        Initrd_Systemd_Network_Links_Value as Initrd_Systemd_Network_Links_Value,
        Initrd_Systemd_Network_Netdevs_Value as Initrd_Systemd_Network_Netdevs_Value,
        Initrd_Systemd_Network_Networks_Value as Initrd_Systemd_Network_Networks_Value,
        Initrd_Systemd_Network_Units_Value as Initrd_Systemd_Network_Units_Value,
        Initrd_Systemd_Network_WaitOnline as Initrd_Systemd_Network_WaitOnline,
        Initrd_Systemd_Paths_Value as Initrd_Systemd_Paths_Value,
        Initrd_Systemd_Repart as Initrd_Systemd_Repart,
        Initrd_Systemd_Services_Value as Initrd_Systemd_Services_Value,
        Initrd_Systemd_Settings as Initrd_Systemd_Settings,
        Initrd_Systemd_Settings_Manager as Initrd_Systemd_Settings_Manager,
        Initrd_Systemd_Shell as Initrd_Systemd_Shell,
        Initrd_Systemd_Slices_Value as Initrd_Systemd_Slices_Value,
        Initrd_Systemd_Sockets_Value as Initrd_Systemd_Sockets_Value,
        Initrd_Systemd_StorePaths_Item as Initrd_Systemd_StorePaths_Item,
        Initrd_Systemd_Targets_Value as Initrd_Systemd_Targets_Value,
        Initrd_Systemd_Timers_Value as Initrd_Systemd_Timers_Value,
        Initrd_Systemd_Tmpfiles as Initrd_Systemd_Tmpfiles,
        Initrd_Systemd_Tmpfiles_Settings_Value_Value_Value as Initrd_Systemd_Tmpfiles_Settings_Value_Value_Value,
        Initrd_Systemd_Tpm2 as Initrd_Systemd_Tpm2,
        Initrd_Systemd_Tpm2_Pcrosseparator as Initrd_Systemd_Tpm2_Pcrosseparator,
        Initrd_Systemd_Tpm2_Pcrphases as Initrd_Systemd_Tpm2_Pcrphases,
        Initrd_Systemd_Units_Value as Initrd_Systemd_Units_Value,
        Initrd_Systemd_Users_Value as Initrd_Systemd_Users_Value,
        Initrd_Unl0kr as Initrd_Unl0kr,
        Initrd_Unl0kr_Settings as Initrd_Unl0kr_Settings,
    )
    from pynix_os.boot.iscsi_initiator import IscsiInitiator as IscsiInitiator
    from pynix_os.boot.kernel import Kernel as Kernel, Kernel_Sysctl as Kernel_Sysctl, Kernel_Sysfs as Kernel_Sysfs
    from pynix_os.boot.kexec import Kexec as Kexec
    from pynix_os.boot.loader import (
        Loader as Loader,
        Loader_Efi as Loader_Efi,
        Loader_External as Loader_External,
        Loader_GenerationsDir as Loader_GenerationsDir,
        Loader_GenericExtlinuxCompatible as Loader_GenericExtlinuxCompatible,
        Loader_GenericExtlinuxCompatible_MirroredBoots_Item as Loader_GenericExtlinuxCompatible_MirroredBoots_Item,
        Loader_Grub as Loader_Grub,
        Loader_Grub_Memtest86 as Loader_Grub_Memtest86,
        Loader_Grub_MirroredBoots_Item as Loader_Grub_MirroredBoots_Item,
        Loader_Grub_Users_Value as Loader_Grub_Users_Value,
        Loader_InitScript as Loader_InitScript,
        Loader_Limine as Loader_Limine,
        Loader_Limine_SecureBoot as Loader_Limine_SecureBoot,
        Loader_Limine_SecureBoot_AutoEnrollKeys as Loader_Limine_SecureBoot_AutoEnrollKeys,
        Loader_Limine_Style as Loader_Limine_Style,
        Loader_Limine_Style_GraphicalTerminal as Loader_Limine_Style_GraphicalTerminal,
        Loader_Limine_Style_GraphicalTerminal_Font as Loader_Limine_Style_GraphicalTerminal_Font,
        Loader_Limine_Style_Interface as Loader_Limine_Style_Interface,
        Loader_Refind as Loader_Refind,
        Loader_SystemdBoot as Loader_SystemdBoot,
        Loader_SystemdBoot_BootCounting as Loader_SystemdBoot_BootCounting,
        Loader_SystemdBoot_Edk2UefiShell as Loader_SystemdBoot_Edk2UefiShell,
        Loader_SystemdBoot_Memtest86 as Loader_SystemdBoot_Memtest86,
        Loader_SystemdBoot_Netbootxyz as Loader_SystemdBoot_Netbootxyz,
        Loader_SystemdBoot_Windows_Value as Loader_SystemdBoot_Windows_Value,
    )
    from pynix_os.boot.modprobeConfig import ModprobeConfig as ModprobeConfig
    from pynix_os.boot.plymouth import Plymouth as Plymouth, Plymouth_Tpm2Totp as Plymouth_Tpm2Totp
    from pynix_os.boot.swraid import Swraid as Swraid
    from pynix_os.boot.tmp import Tmp as Tmp, Tmp_ZramSettings as Tmp_ZramSettings
    from pynix_os.boot.uki import Uki as Uki
    from pynix_os.boot.uvesafb import Uvesafb as Uvesafb, Uvesafb_V86d as Uvesafb_V86d
    from pynix_os.boot.zfs import Zfs as Boot_Zfs, Zfs_Pools_Value as Zfs_Pools_Value, Zfs_Tzpfms as Zfs_Tzpfms
    from pynix_os.boot.zswap import Zswap as Zswap
    from pynix_os.console.__options__ import Console as Console
    from pynix_os.documentation.__options__ import Documentation as Documentation
    from pynix_os.documentation.dev import Dev as Dev
    from pynix_os.documentation.doc import Doc as Doc
    from pynix_os.documentation.info import Info as Info
    from pynix_os.documentation.man import (
        Man as Man,
        Man_Cache as Man_Cache,
        Man_ManDb as Man_ManDb,
        Man_Mandoc as Man_Mandoc,
        Man_Mandoc_Settings as Man_Mandoc_Settings,
    )
    from pynix_os.documentation.nixos import Nixos as Documentation_Nixos, Nixos_Options as Nixos_Options
    from pynix_os.ec2.__options__ import Ec2 as Ec2
    from pynix_os.ec2.zfs import Zfs as Ec2_Zfs, Zfs_Datasets_Value as Ec2_Zfs_Zfs_Datasets_Value
    from pynix_os.environment.__options__ import (
        Environment as Environment,
        Environment_Etc_Value as Environment_Etc_Value,
    )
    from pynix_os.environment.budgie import Budgie as Budgie
    from pynix_os.environment.cinnamon import Cinnamon as Environment_Cinnamon
    from pynix_os.environment.cosmic import Cosmic as Cosmic
    from pynix_os.environment.enlightenment import Enlightenment as Enlightenment
    from pynix_os.environment.gnome import Gnome as Environment_Gnome
    from pynix_os.environment.lxqt import Lxqt as Lxqt
    from pynix_os.environment.mate import Mate as Mate
    from pynix_os.environment.memoryAllocator import MemoryAllocator as MemoryAllocator
    from pynix_os.environment.pantheon import Pantheon as Environment_Pantheon
    from pynix_os.environment.plasma6 import Plasma6 as Plasma6
    from pynix_os.environment.shell import Shell as Shell
    from pynix_os.environment.stub_ld import StubLd as StubLd
    from pynix_os.environment.wordlist import Wordlist as Wordlist
    from pynix_os.environment.wvdial import Wvdial as Wvdial
    from pynix_os.environment.xfce import Xfce as Xfce
    from pynix_os.fonts.__options__ import Fonts as Fonts
    from pynix_os.fonts.fontDir import FontDir as FontDir
    from pynix_os.fonts.fontconfig import (
        Fontconfig as Fontconfig,
        Fontconfig_Aliases_Value as Fontconfig_Aliases_Value,
        Fontconfig_DefaultFonts as Fontconfig_DefaultFonts,
        Fontconfig_Hinting as Fontconfig_Hinting,
        Fontconfig_Subpixel as Fontconfig_Subpixel,
    )
    from pynix_os.gtk.iconCache import IconCache as IconCache
    from pynix_os.hardware.__options__ import Hardware as Hardware
    from pynix_os.hardware.acpilight import Acpilight as Acpilight
    from pynix_os.hardware.alsa import (
        Alsa as Alsa,
        Alsa_CardAliases_Value as Alsa_CardAliases_Value,
        Alsa_Controls_Value as Alsa_Controls_Value,
        Alsa_DefaultDevice as Alsa_DefaultDevice,
    )
    from pynix_os.hardware.amdgpu import (
        Amdgpu as Amdgpu,
        Amdgpu_Initrd as Amdgpu_Initrd,
        Amdgpu_LegacySupport as Amdgpu_LegacySupport,
        Amdgpu_Opencl as Amdgpu_Opencl,
        Amdgpu_Overdrive as Amdgpu_Overdrive,
        Amdgpu_Zluda as Amdgpu_Zluda,
    )
    from pynix_os.hardware.apple import Apple as Apple, Apple_TouchBar as Apple_TouchBar
    from pynix_os.hardware.bladeRF import BladeRF as BladeRF
    from pynix_os.hardware.block import Block as Block
    from pynix_os.hardware.bluetooth import Bluetooth as Bluetooth, Bluetooth_Hsphfpd as Bluetooth_Hsphfpd
    from pynix_os.hardware.brillo import Brillo as Brillo
    from pynix_os.hardware.bumblebee import Bumblebee as Bumblebee
    from pynix_os.hardware.ckb_next import CkbNext as CkbNext
    from pynix_os.hardware.coral import Coral as Coral, Coral_Pcie as Coral_Pcie, Coral_Usb as Coral_Usb
    from pynix_os.hardware.cpu import (
        Cpu as Cpu,
        Cpu_Amd as Cpu_Amd,
        Cpu_Amd_RyzenSmu as Cpu_Amd_RyzenSmu,
        Cpu_Amd_Sev as Cpu_Amd_Sev,
        Cpu_Amd_SevGuest as Cpu_Amd_SevGuest,
        Cpu_Intel as Cpu_Intel,
        Cpu_Intel_Npu as Cpu_Intel_Npu,
        Cpu_Intel_Sgx as Cpu_Intel_Sgx,
        Cpu_Intel_Sgx_Provision as Cpu_Intel_Sgx_Provision,
        Cpu_X86 as Cpu_X86,
        Cpu_X86_Msr as Cpu_X86_Msr,
        Cpu_X86_Msr_Settings as Cpu_X86_Msr_Settings,
    )
    from pynix_os.hardware.decklink import Decklink as Decklink
    from pynix_os.hardware.deviceTree import (
        DeviceTree as DeviceTree,
        DeviceTree_Overlays_Item as DeviceTree_Overlays_Item,
    )
    from pynix_os.hardware.digitalbitbox import Digitalbitbox as Hardware_Digitalbitbox
    from pynix_os.hardware.display import (
        Display as Display,
        Display_Edid as Display_Edid,
        Display_Outputs_Value as Display_Outputs_Value,
    )
    from pynix_os.hardware.facetimehd import Facetimehd as Facetimehd
    from pynix_os.hardware.facter import (
        Facter as Facter,
        Facter_Debug as Facter_Debug,
        Facter_Detected as Facter_Detected,
        Facter_Detected_Bluetooth as Facter_Detected_Bluetooth,
        Facter_Detected_Boot as Facter_Detected_Boot,
        Facter_Detected_Boot_Disk as Facter_Detected_Boot_Disk,
        Facter_Detected_Boot_Graphics as Facter_Detected_Boot_Graphics,
        Facter_Detected_Boot_Initrd as Facter_Detected_Boot_Initrd,
        Facter_Detected_Boot_Initrd_Networking as Facter_Detected_Boot_Initrd_Networking,
        Facter_Detected_Boot_Keyboard as Facter_Detected_Boot_Keyboard,
        Facter_Detected_Camera as Facter_Detected_Camera,
        Facter_Detected_Camera_Ipu6 as Facter_Detected_Camera_Ipu6,
        Facter_Detected_Dhcp as Facter_Detected_Dhcp,
        Facter_Detected_Fingerprint as Facter_Detected_Fingerprint,
        Facter_Detected_Graphics as Facter_Detected_Graphics,
        Facter_Detected_Graphics_Amd as Facter_Detected_Graphics_Amd,
        Facter_Detected_Networking as Facter_Detected_Networking,
        Facter_Detected_Networking_Intel as Facter_Detected_Networking_Intel,
        Facter_Detected_Networking_Intel_N2200BG as Facter_Detected_Networking_Intel_N2200BG,
        Facter_Detected_Networking_Intel_N3945ABG as Facter_Detected_Networking_Intel_N3945ABG,
        Facter_Detected_Uefi as Facter_Detected_Uefi,
        Facter_Detected_Virtualisation as Facter_Detected_Virtualisation,
        Facter_Detected_Virtualisation_Hyperv as Facter_Detected_Virtualisation_Hyperv,
        Facter_Detected_Virtualisation_None as Facter_Detected_Virtualisation_None,
        Facter_Detected_Virtualisation_Oracle as Facter_Detected_Virtualisation_Oracle,
        Facter_Detected_Virtualisation_Parallels as Facter_Detected_Virtualisation_Parallels,
        Facter_Detected_Virtualisation_Qemu as Facter_Detected_Virtualisation_Qemu,
        Facter_Detected_Virtualisation_VirtioScsi as Facter_Detected_Virtualisation_VirtioScsi,
    )
    from pynix_os.hardware.fancontrol import Fancontrol as Fancontrol
    from pynix_os.hardware.flipperzero import Flipperzero as Flipperzero
    from pynix_os.hardware.flirc import Flirc as Flirc
    from pynix_os.hardware.fw_fanctrl import (
        FwFanctrl as FwFanctrl,
        FwFanctrl_Config as FwFanctrl_Config,
        FwFanctrl_Config_Strategies_Value as FwFanctrl_Config_Strategies_Value,
        FwFanctrl_Config_Strategies_Value_SpeedCurve_Item as FwFanctrl_Config_Strategies_Value_SpeedCurve_Item,
    )
    from pynix_os.hardware.glasgow import Glasgow as Glasgow
    from pynix_os.hardware.gpgSmartcards import GpgSmartcards as GpgSmartcards
    from pynix_os.hardware.graphics import Graphics as Graphics
    from pynix_os.hardware.hackrf import Hackrf as Hackrf
    from pynix_os.hardware.hid_fanatecff import HidFanatecff as HidFanatecff
    from pynix_os.hardware.i2c import I2c as I2c
    from pynix_os.hardware.infiniband import Infiniband as Infiniband
    from pynix_os.hardware.inputmodule import Inputmodule as Inputmodule
    from pynix_os.hardware.intel_gpu_tools import IntelGpuTools as IntelGpuTools
    from pynix_os.hardware.ipu6 import Ipu6 as Ipu6
    from pynix_os.hardware.ipu7 import Ipu7 as Ipu7
    from pynix_os.hardware.keyboard import (
        Keyboard as Keyboard,
        Keyboard_Qmk as Keyboard_Qmk,
        Keyboard_Teck as Keyboard_Teck,
        Keyboard_Uhk as Keyboard_Uhk,
        Keyboard_Zsa as Keyboard_Zsa,
    )
    from pynix_os.hardware.kryoflux import Kryoflux as Kryoflux
    from pynix_os.hardware.ksm import Ksm as Ksm
    from pynix_os.hardware.ledger import Ledger as Ledger
    from pynix_os.hardware.libftdi import Libftdi as Libftdi
    from pynix_os.hardware.libjaylink import Libjaylink as Libjaylink
    from pynix_os.hardware.logitech import (
        Logitech as Logitech,
        Logitech_Lcd as Logitech_Lcd,
        Logitech_Wireless as Logitech_Wireless,
    )
    from pynix_os.hardware.mcelog import Mcelog as Mcelog
    from pynix_os.hardware.mwProCapture import MwProCapture as MwProCapture
    from pynix_os.hardware.new_lg4ff import NewLg4ff as NewLg4ff
    from pynix_os.hardware.nfc_nci import NfcNci as NfcNci
    from pynix_os.hardware.nitrokey import Nitrokey as Nitrokey
    from pynix_os.hardware.nvidia import (
        Nvidia as Nvidia,
        Nvidia_Datacenter as Nvidia_Datacenter,
        Nvidia_DynamicBoost as Nvidia_DynamicBoost,
        Nvidia_Gsp as Nvidia_Gsp,
        Nvidia_Modesetting as Nvidia_Modesetting,
        Nvidia_PowerManagement as Nvidia_PowerManagement,
        Nvidia_Prime as Nvidia_Prime,
        Nvidia_Prime_Offload as Nvidia_Prime_Offload,
        Nvidia_Prime_ReverseSync as Nvidia_Prime_ReverseSync,
        Nvidia_Prime_ReverseSync_SetupCommands as Nvidia_Prime_ReverseSync_SetupCommands,
        Nvidia_Prime_Sync as Nvidia_Prime_Sync,
    )
    from pynix_os.hardware.nvidiaOptimus import NvidiaOptimus as NvidiaOptimus
    from pynix_os.hardware.nvidia_container_toolkit import (
        NvidiaContainerToolkit as NvidiaContainerToolkit,
        NvidiaContainerToolkit_Mounts_Item as NvidiaContainerToolkit_Mounts_Item,
    )
    from pynix_os.hardware.onlykey import Onlykey as Onlykey
    from pynix_os.hardware.openrazer import (
        Openrazer as Openrazer,
        Openrazer_BatteryNotifier as Openrazer_BatteryNotifier,
        Openrazer_Packages as Openrazer_Packages,
    )
    from pynix_os.hardware.opentabletdriver import (
        Opentabletdriver as Opentabletdriver,
        Opentabletdriver_Daemon as Opentabletdriver_Daemon,
    )
    from pynix_os.hardware.parallels import Parallels as Parallels
    from pynix_os.hardware.pcmcia import Pcmcia as Pcmcia
    from pynix_os.hardware.printers import (
        Printers as Printers,
        Printers_EnsureClasses_Value as Printers_EnsureClasses_Value,
        Printers_EnsurePrinters_Item as Printers_EnsurePrinters_Item,
    )
    from pynix_os.hardware.raid import Raid as Raid, Raid_HPSmartArray as Raid_HPSmartArray
    from pynix_os.hardware.rasdaemon import Rasdaemon as Rasdaemon
    from pynix_os.hardware.rtl_sdr import RtlSdr as RtlSdr
    from pynix_os.hardware.saleae_logic import SaleaeLogic as SaleaeLogic
    from pynix_os.hardware.sane import (
        Sane as Sane,
        Sane_Brscan4 as Sane_Brscan4,
        Sane_Brscan4_NetDevices_Value as Sane_Brscan4_NetDevices_Value,
        Sane_Brscan5 as Sane_Brscan5,
        Sane_Brscan5_NetDevices_Value as Sane_Brscan5_NetDevices_Value,
        Sane_Drivers as Sane_Drivers,
        Sane_Drivers_ScanSnap as Sane_Drivers_ScanSnap,
        Sane_Dsseries as Sane_Dsseries,
    )
    from pynix_os.hardware.sata import (
        Sata as Sata,
        Sata_Timeout as Sata_Timeout,
        Sata_Timeout_Drives_Item as Sata_Timeout_Drives_Item,
    )
    from pynix_os.hardware.sensor import Sensor as Sensor, Sensor_Hddtemp as Sensor_Hddtemp, Sensor_Iio as Sensor_Iio
    from pynix_os.hardware.sheep_net import SheepNet as SheepNet
    from pynix_os.hardware.spacenavd import Spacenavd as Spacenavd
    from pynix_os.hardware.steam_hardware import SteamHardware as SteamHardware
    from pynix_os.hardware.system76 import (
        System76 as System76,
        System76_FirmwareDaemon as System76_FirmwareDaemon,
        System76_KernelModules as System76_KernelModules,
        System76_PowerDaemon as System76_PowerDaemon,
    )
    from pynix_os.hardware.tenstorrent import Tenstorrent as Tenstorrent
    from pynix_os.hardware.trackpoint import Trackpoint as Trackpoint
    from pynix_os.hardware.tuxedo_drivers import (
        TuxedoDrivers as TuxedoDrivers,
        TuxedoDrivers_Settings as TuxedoDrivers_Settings,
    )
    from pynix_os.hardware.tuxedo_rs import TuxedoRs as TuxedoRs, TuxedoRs_TailorGui as TuxedoRs_TailorGui
    from pynix_os.hardware.ubertooth import Ubertooth as Ubertooth
    from pynix_os.hardware.uinput import Uinput as Uinput
    from pynix_os.hardware.uni_sync import (
        UniSync as UniSync,
        UniSync_Devices_Item as UniSync_Devices_Item,
        UniSync_Devices_Item_Channels_Item as UniSync_Devices_Item_Channels_Item,
    )
    from pynix_os.hardware.usbStorage import UsbStorage as UsbStorage
    from pynix_os.hardware.usb_modeswitch import UsbModeswitch as UsbModeswitch
    from pynix_os.hardware.wooting import Wooting as Wooting
    from pynix_os.hardware.xone import Xone as Xone
    from pynix_os.hardware.xpad_noone import XpadNoone as XpadNoone
    from pynix_os.hardware.xpadneo import Xpadneo as Xpadneo, Xpadneo_RumbleAttenuation as Xpadneo_RumbleAttenuation
    from pynix_os.i18n.__options__ import I18n as I18n
    from pynix_os.ids.__options__ import Ids as Ids
    from pynix_os.image.__options__ import Image as Image, Image_Modules_Value as Image_Modules_Value
    from pynix_os.lix.__options__ import (
        Lix as Lix,
        Lix_BuildMachines as Lix_BuildMachines,
        Lix_BuildMachines_Machines_Value as Lix_BuildMachines_Machines_Value,
    )
    from pynix_os.location.__options__ import Location as Location
    from pynix_os.meta.__options__ import Meta as Meta
    from pynix_os.networking.__options__ import (
        Networking as Networking,
        Networking_Bonds_Value as Networking_Bonds_Value,
        Networking_Bridges_Value as Networking_Bridges_Value,
        Networking_DefaultGateway as Networking_DefaultGateway,
        Networking_FooOverUDP_Value as Networking_FooOverUDP_Value,
        Networking_FooOverUDP_Value_Local as Networking_FooOverUDP_Value_Local,
        Networking_GreTunnels_Value as Networking_GreTunnels_Value,
        Networking_Interfaces_Value as Networking_Interfaces_Value,
        Networking_Interfaces_Value_Ipv4Addresses_Item as Networking_Interfaces_Value_Ipv4Addresses_Item,
        Networking_Interfaces_Value_Ipv4Routes_Item as Networking_Interfaces_Value_Ipv4Routes_Item,
        Networking_Interfaces_Value_Ipv6Addresses_Item as Networking_Interfaces_Value_Ipv6Addresses_Item,
        Networking_Interfaces_Value_Ipv6Routes_Item as Networking_Interfaces_Value_Ipv6Routes_Item,
        Networking_Ipips_Value as Networking_Ipips_Value,
        Networking_Ipvlans_Value as Networking_Ipvlans_Value,
        Networking_Macvlans_Value as Networking_Macvlans_Value,
        Networking_Sits_Value as Networking_Sits_Value,
        Networking_Sits_Value_Encapsulation as Networking_Sits_Value_Encapsulation,
        Networking_Supplicant_Value as Networking_Supplicant_Value,
        Networking_Vlans_Value as Networking_Vlans_Value,
        Networking_Vswitches_Value as Networking_Vswitches_Value,
        Networking_Vswitches_Value_Interfaces_Value as Networking_Vswitches_Value_Interfaces_Value,
        Networking_WlanInterfaces_Value as Networking_WlanInterfaces_Value,
    )
    from pynix_os.networking.dhcpcd import Dhcpcd as Dhcpcd
    from pynix_os.networking.firewall import (
        Firewall_Interfaces_Value as Firewall_Interfaces_Value,
        Firewall as Networking_Firewall,
    )
    from pynix_os.networking.getaddrinfo import Getaddrinfo as Getaddrinfo
    from pynix_os.networking.ifstate import Ifstate as Ifstate
    from pynix_os.networking.iproute2 import Iproute2 as Iproute2
    from pynix_os.networking.jool import (
        Jool as Jool,
        Jool_Nat64_Value as Jool_Nat64_Value,
        Jool_Siit_Value as Jool_Siit_Value,
    )
    from pynix_os.networking.modemmanager import (
        Modemmanager as Modemmanager,
        Modemmanager_FccUnlockScripts_Item as Modemmanager_FccUnlockScripts_Item,
    )
    from pynix_os.networking.nat import Nat as Nat, Nat_ForwardPorts_Item as Nat_ForwardPorts_Item
    from pynix_os.networking.netplan import Netplan as Netplan
    from pynix_os.networking.networkmanager import (
        Networkmanager as Networkmanager,
        Networkmanager_DispatcherScripts_Item as Networkmanager_DispatcherScripts_Item,
        Networkmanager_EnsureProfiles as Networkmanager_EnsureProfiles,
        Networkmanager_EnsureProfiles_Profiles_Value as Networkmanager_EnsureProfiles_Profiles_Value,
        Networkmanager_EnsureProfiles_Secrets as Networkmanager_EnsureProfiles_Secrets,
        Networkmanager_EnsureProfiles_Secrets_Entries_Item as Networkmanager_EnsureProfiles_Secrets_Entries_Item,
        Networkmanager_Ethernet as Networkmanager_Ethernet,
        Networkmanager_Wifi as Networkmanager_Wifi,
    )
    from pynix_os.networking.nftables import Nftables as Nftables, Nftables_Tables_Value as Nftables_Tables_Value
    from pynix_os.networking.openconnect import (
        Openconnect as Openconnect,
        Openconnect_Interfaces_Value as Openconnect_Interfaces_Value,
    )
    from pynix_os.networking.proxy import Proxy as Proxy
    from pynix_os.networking.resolvconf import Resolvconf as Resolvconf
    from pynix_os.networking.rxe import Rxe as Rxe
    from pynix_os.networking.stevenblack import Stevenblack as Stevenblack
    from pynix_os.networking.tcpcrypt import Tcpcrypt as Tcpcrypt
    from pynix_os.networking.ucarp import Ucarp as Ucarp
    from pynix_os.networking.wg_quick import (
        WgQuick as WgQuick,
        WgQuick_Interfaces_Value as WgQuick_Interfaces_Value,
        WgQuick_Interfaces_Value_Peers_Item as WgQuick_Interfaces_Value_Peers_Item,
    )
    from pynix_os.networking.wireguard import (
        Wireguard as Wireguard,
        Wireguard_Interfaces_Value as Wireguard_Interfaces_Value,
        Wireguard_Interfaces_Value_Peers_Item as Wireguard_Interfaces_Value_Peers_Item,
    )
    from pynix_os.networking.wireless import (
        Wireless as Wireless,
        Wireless_Iwd as Wireless_Iwd,
        Wireless_Networks_Value as Wireless_Networks_Value,
        Wireless_Pkcs11 as Wireless_Pkcs11,
    )
    from pynix_os.nix.__options__ import (
        Nix as Nix,
        Nix_BuildMachines_Item as Nix_BuildMachines_Item,
        Nix_Registry_Value as Nix_Registry_Value,
        Nix_Settings as Nix_Settings,
    )
    from pynix_os.nix.channel import Channel as Channel
    from pynix_os.nix.daemon import Daemon as Daemon
    from pynix_os.nix.firewall import Firewall as Nix_Firewall
    from pynix_os.nix.gc import Gc as Gc
    from pynix_os.nix.optimise import Optimise as Optimise
    from pynix_os.nix.sshServe import SshServe as SshServe
    from pynix_os.nixops.__options__ import Nixops as Nixops
    from pynix_os.nixpkgs.__options__ import Nixpkgs as Nixpkgs
    from pynix_os.nixpkgs.flake import Flake as Flake
    from pynix_os.oci.__options__ import Oci as Oci
    from pynix_os.openstack.__options__ import Openstack as Openstack
    from pynix_os.openstack.zfs import Zfs as Openstack_Zfs, Zfs_Datasets_Value as Openstack_Zfs_Zfs_Datasets_Value
    from pynix_os.power.ups import (
        Ups as Ups,
        Ups_Ups_Value as Ups_Ups_Value,
        Ups_Upsd as Ups_Upsd,
        Ups_Upsd_Listen_Item as Ups_Upsd_Listen_Item,
        Ups_Upsmon as Ups_Upsmon,
        Ups_Upsmon_Monitor_Value as Ups_Upsmon_Monitor_Value,
        Ups_Users_Value as Ups_Users_Value,
    )
    from pynix_os.powerManagement.__options__ import PowerManagement as PowerManagement
    from pynix_os.powerManagement.cpufreq import Cpufreq as Cpufreq
    from pynix_os.powerManagement.powertop import Powertop as Powertop
    from pynix_os.programs.alvr import Alvr as Alvr
    from pynix_os.programs.amnezia_vpn import AmneziaVpn as AmneziaVpn
    from pynix_os.programs.appgate_sdp import AppgateSdp as AppgateSdp
    from pynix_os.programs.appimage import Appimage as Appimage
    from pynix_os.programs.arp_scan import ArpScan as ArpScan
    from pynix_os.programs.atop import (
        Atop as Atop,
        Atop_AtopRotateTimer as Atop_AtopRotateTimer,
        Atop_AtopService as Atop_AtopService,
        Atop_AtopacctService as Atop_AtopacctService,
        Atop_Atopgpu as Atop_Atopgpu,
        Atop_Netatop as Atop_Netatop,
        Atop_SetuidWrapper as Atop_SetuidWrapper,
    )
    from pynix_os.programs.atuin import Atuin_Daemon as Atuin_Daemon, Atuin as Programs_Atuin
    from pynix_os.programs.ausweisapp import Ausweisapp as Ausweisapp
    from pynix_os.programs.autoenv import Autoenv as Autoenv
    from pynix_os.programs.autojump import Autojump as Autojump
    from pynix_os.programs.bandwhich import Bandwhich as Bandwhich
    from pynix_os.programs.bash import (
        Bash as Bash,
        Bash_Blesh as Bash_Blesh,
        Bash_Completion as Bash_Completion,
        Bash_UndistractMe as Bash_UndistractMe,
    )
    from pynix_os.programs.bash_my_aws import BashMyAws as BashMyAws
    from pynix_os.programs.bat import Bat as Bat
    from pynix_os.programs.bazecor import Bazecor as Bazecor
    from pynix_os.programs.bcc import Bcc as Bcc
    from pynix_os.programs.benchexec import Benchexec as Benchexec
    from pynix_os.programs.browserpass import Browserpass as Browserpass
    from pynix_os.programs.btrfs_heatmap import BtrfsHeatmap as BtrfsHeatmap
    from pynix_os.programs.calls import Calls as Calls
    from pynix_os.programs.captive_browser import CaptiveBrowser as CaptiveBrowser
    from pynix_os.programs.ccache import Ccache as Ccache
    from pynix_os.programs.cdemu import Cdemu as Cdemu
    from pynix_os.programs.cfs_zen_tweaks import CfsZenTweaks as CfsZenTweaks
    from pynix_os.programs.chromium import Chromium as Chromium
    from pynix_os.programs.chrysalis import Chrysalis as Chrysalis
    from pynix_os.programs.clash_verge import ClashVerge as ClashVerge
    from pynix_os.programs.cnping import Cnping as Cnping
    from pynix_os.programs.comma import Comma as Comma
    from pynix_os.programs.command_not_found import CommandNotFound as CommandNotFound
    from pynix_os.programs.compsize import Compsize as Compsize
    from pynix_os.programs.coolercontrol import Coolercontrol as Coolercontrol
    from pynix_os.programs.corectrl import Corectrl as Corectrl
    from pynix_os.programs.corefreq import Corefreq as Corefreq
    from pynix_os.programs.cpu_energy_meter import CpuEnergyMeter as CpuEnergyMeter
    from pynix_os.programs.criu import Criu as Criu
    from pynix_os.programs.dconf import (
        Dconf as Dconf,
        Dconf_Profiles_Value_Or as Dconf_Profiles_Value_Or,
        Dconf_Profiles_Value_Or_Databases_Item_Or as Dconf_Profiles_Value_Or_Databases_Item_Or,
    )
    from pynix_os.programs.digitalbitbox import Digitalbitbox as Programs_Digitalbitbox
    from pynix_os.programs.direnv import (
        Direnv as Direnv,
        Direnv_Angrr as Direnv_Angrr,
        Direnv_NixDirenv as Direnv_NixDirenv,
    )
    from pynix_os.programs.dmrconfig import Dmrconfig as Dmrconfig
    from pynix_os.programs.dms_shell import (
        DmsShell as DmsShell,
        DmsShell_Plugins_Value as DmsShell_Plugins_Value,
        DmsShell_Quickshell as DmsShell_Quickshell,
        DmsShell_Systemd as DmsShell_Systemd,
    )
    from pynix_os.programs.droidcam import Droidcam as Droidcam
    from pynix_os.programs.dsearch import Dsearch as Dsearch, Dsearch_Systemd as Dsearch_Systemd
    from pynix_os.programs.dublin_traceroute import DublinTraceroute as DublinTraceroute
    from pynix_os.programs.dwl import Dwl as Dwl
    from pynix_os.programs.ente_auth import EnteAuth as EnteAuth
    from pynix_os.programs.entropy import Entropy as Entropy
    from pynix_os.programs.envision import Envision as Envision
    from pynix_os.programs.evince import Evince as Evince
    from pynix_os.programs.evolution import Evolution as Evolution
    from pynix_os.programs.extra_container import ExtraContainer as ExtraContainer
    from pynix_os.programs.fcast_receiver import FcastReceiver as FcastReceiver
    from pynix_os.programs.feedbackd import Feedbackd as Feedbackd
    from pynix_os.programs.firefox import (
        Firefox as Firefox,
        Firefox_NativeMessagingHosts as Firefox_NativeMessagingHosts,
    )
    from pynix_os.programs.firejail import (
        Firejail as Firejail,
        Firejail_WrappedBinaries_Value_Or as Firejail_WrappedBinaries_Value_Or,
    )
    from pynix_os.programs.fish import (
        Fish as Fish,
        Fish_ShellFunctions_Value as Fish_ShellFunctions_Value,
        Fish_Vendor as Fish_Vendor,
        Fish_Vendor_Completions as Fish_Vendor_Completions,
        Fish_Vendor_Config as Fish_Vendor_Config,
        Fish_Vendor_Functions as Fish_Vendor_Functions,
    )
    from pynix_os.programs.flashprog import Flashprog as Flashprog
    from pynix_os.programs.flashrom import Flashrom as Flashrom
    from pynix_os.programs.flexoptix_app import FlexoptixApp as FlexoptixApp
    from pynix_os.programs.foot import Foot as Foot, Foot_Xdg as Foot_Xdg
    from pynix_os.programs.fuse import Fuse as Fuse
    from pynix_os.programs.fzf import Fzf as Fzf
    from pynix_os.programs.gamemode import Gamemode as Gamemode
    from pynix_os.programs.gamescope import Gamescope as Gamescope
    from pynix_os.programs.gdk_pixbuf import GdkPixbuf as GdkPixbuf
    from pynix_os.programs.geary import Geary as Geary
    from pynix_os.programs.ghidra import Ghidra as Ghidra
    from pynix_os.programs.git import Git as Git, Git_Lfs as Git_Lfs, Git_Prompt as Git_Prompt
    from pynix_os.programs.git_worktree_switcher import GitWorktreeSwitcher as GitWorktreeSwitcher
    from pynix_os.programs.gnome_disks import GnomeDisks as GnomeDisks
    from pynix_os.programs.gnome_terminal import GnomeTerminal as GnomeTerminal
    from pynix_os.programs.gnupg import Gnupg as Gnupg, Gnupg_Agent as Gnupg_Agent, Gnupg_Dirmngr as Gnupg_Dirmngr
    from pynix_os.programs.google_chrome import GoogleChrome as GoogleChrome
    from pynix_os.programs.gpaste import Gpaste as Gpaste
    from pynix_os.programs.gphoto2 import Gphoto2 as Gphoto2
    from pynix_os.programs.gpu_screen_recorder import (
        GpuScreenRecorder as GpuScreenRecorder,
        GpuScreenRecorder_Ui as GpuScreenRecorder_Ui,
    )
    from pynix_os.programs.gtklock import Gtklock as Gtklock
    from pynix_os.programs.haguichi import Haguichi as Haguichi
    from pynix_os.programs.hamster import Hamster as Hamster
    from pynix_os.programs.htop import Htop as Htop
    from pynix_os.programs.hyprland import (
        Hyprland as Hyprland,
        Hyprland_Systemd as Hyprland_Systemd,
        Hyprland_Systemd_SetPath as Hyprland_Systemd_SetPath,
        Hyprland_Xwayland as Hyprland_Xwayland,
    )
    from pynix_os.programs.hyprlock import Hyprlock as Hyprlock
    from pynix_os.programs.i3lock import I3lock as I3lock
    from pynix_os.programs.iay import Iay as Iay
    from pynix_os.programs.idescriptor import Idescriptor as Idescriptor
    from pynix_os.programs.iftop import Iftop as Iftop
    from pynix_os.programs.iio_hyprland import IioHyprland as IioHyprland
    from pynix_os.programs.immersed import Immersed as Immersed
    from pynix_os.programs.ioquake3 import Ioquake3 as Ioquake3
    from pynix_os.programs.iotop import Iotop as Iotop
    from pynix_os.programs.jai_jail import JaiJail as JaiJail
    from pynix_os.programs.java import Java as Java
    from pynix_os.programs.joycond_cemuhook import JoycondCemuhook as JoycondCemuhook
    from pynix_os.programs.k3b import K3b as K3b
    from pynix_os.programs.k40_whisperer import K40Whisperer as K40Whisperer
    from pynix_os.programs.kbdlight import Kbdlight as Kbdlight
    from pynix_os.programs.kclock import Kclock as Kclock
    from pynix_os.programs.kde_pim import KdePim as KdePim
    from pynix_os.programs.kdeconnect import Kdeconnect as Kdeconnect
    from pynix_os.programs.kubeswitch import Kubeswitch as Kubeswitch
    from pynix_os.programs.labwc import Labwc as Labwc
    from pynix_os.programs.ladybird import Ladybird as Ladybird
    from pynix_os.programs.lazygit import Lazygit as Lazygit
    from pynix_os.programs.less import Less as Less
    from pynix_os.programs.liboping import Liboping as Liboping
    from pynix_os.programs.librepods import Librepods as Librepods
    from pynix_os.programs.localsend import Localsend as Localsend
    from pynix_os.programs.mango import Mango as Mango
    from pynix_os.programs.mdevctl import Mdevctl as Mdevctl
    from pynix_os.programs.mepo import Mepo as Mepo, Mepo_LocationBackends as Mepo_LocationBackends
    from pynix_os.programs.mininet import Mininet as Mininet
    from pynix_os.programs.minipro import Minipro as Minipro
    from pynix_os.programs.miriway import Miriway as Miriway
    from pynix_os.programs.moonlight_qt import MoonlightQt as MoonlightQt
    from pynix_os.programs.mosh import Mosh as Mosh
    from pynix_os.programs.mouse_actions import MouseActions as MouseActions
    from pynix_os.programs.msmtp import Msmtp as Msmtp
    from pynix_os.programs.mtr import Mtr as Mtr
    from pynix_os.programs.n__1password import N1password as N1password
    from pynix_os.programs.n__1password_gui import N1passwordGui as N1passwordGui
    from pynix_os.programs.nano import Nano as Nano
    from pynix_os.programs.nautilus_open_any_terminal import NautilusOpenAnyTerminal as NautilusOpenAnyTerminal
    from pynix_os.programs.nbd import Nbd as Programs_Nbd
    from pynix_os.programs.neovim import Neovim as Neovim, Neovim_Runtime_Value as Neovim_Runtime_Value
    from pynix_os.programs.nethoscope import Nethoscope as Nethoscope
    from pynix_os.programs.nexttrace import Nexttrace as Nexttrace
    from pynix_os.programs.nh import Nh as Nh, Nh_Clean as Nh_Clean
    from pynix_os.programs.niri import Niri as Niri
    from pynix_os.programs.nix_index import NixIndex as NixIndex
    from pynix_os.programs.nix_ld import NixLd as NixLd
    from pynix_os.programs.nix_required_mounts import (
        NixRequiredMounts as NixRequiredMounts,
        NixRequiredMounts_AllowedPatterns_Value as NixRequiredMounts_AllowedPatterns_Value,
        NixRequiredMounts_AllowedPatterns_Value_Paths_Item_Or as NixRequiredMounts_AllowedPatterns_Value_Paths_Item_Or,
        NixRequiredMounts_Presets as NixRequiredMounts_Presets,
        NixRequiredMounts_Presets_NvidiaGpu as NixRequiredMounts_Presets_NvidiaGpu,
        NixRequiredMounts_Presets_Zluda as NixRequiredMounts_Presets_Zluda,
    )
    from pynix_os.programs.nixbit import Nixbit as Nixbit
    from pynix_os.programs.nm_applet import NmApplet as NmApplet
    from pynix_os.programs.nncp import Nncp as Programs_Nncp
    from pynix_os.programs.noctalia import (
        Noctalia as Noctalia,
        Noctalia_RecommendedServices as Noctalia_RecommendedServices,
        Noctalia_Systemd as Noctalia_Systemd,
    )
    from pynix_os.programs.noisetorch import Noisetorch as Noisetorch
    from pynix_os.programs.npm import Npm as Npm
    from pynix_os.programs.ns_usbloader import NsUsbloader as NsUsbloader
    from pynix_os.programs.nushell import Nushell as Nushell
    from pynix_os.programs.nvrs import Nvrs as Nvrs, Nvrs_Settings as Nvrs_Settings
    from pynix_os.programs.nxdumpclient import Nxdumpclient as Nxdumpclient
    from pynix_os.programs.obs_studio import ObsStudio as ObsStudio
    from pynix_os.programs.oddjobd import Oddjobd as Oddjobd
    from pynix_os.programs.opengamepadui import (
        Opengamepadui as Opengamepadui,
        Opengamepadui_GamescopeSession as Opengamepadui_GamescopeSession,
        Opengamepadui_Inputplumber as Opengamepadui_Inputplumber,
        Opengamepadui_Powerstation as Opengamepadui_Powerstation,
    )
    from pynix_os.programs.openvpn3 import (
        Openvpn3 as Openvpn3,
        Openvpn3_LogService as Openvpn3_LogService,
        Openvpn3_LogService_Settings as Openvpn3_LogService_Settings,
        Openvpn3_Netcfg as Openvpn3_Netcfg,
        Openvpn3_Netcfg_Settings as Openvpn3_Netcfg_Settings,
    )
    from pynix_os.programs.partition_manager import PartitionManager as PartitionManager
    from pynix_os.programs.passless import Passless as Passless
    from pynix_os.programs.pay_respects import (
        PayRespects as PayRespects,
        PayRespects_AiIntegration_Or as PayRespects_AiIntegration_Or,
    )
    from pynix_os.programs.pinnacle import Pinnacle as Pinnacle, Pinnacle_XdgPortals as Pinnacle_XdgPortals
    from pynix_os.programs.plotinus import Plotinus as Plotinus
    from pynix_os.programs.pmount import Pmount as Pmount
    from pynix_os.programs.projecteur import Projecteur as Projecteur
    from pynix_os.programs.proxychains import (
        Proxychains as Proxychains,
        Proxychains_Proxies_Value as Proxychains_Proxies_Value,
    )
    from pynix_os.programs.pulseview import Pulseview as Pulseview
    from pynix_os.programs.qdmr import Qdmr as Qdmr
    from pynix_os.programs.qgroundcontrol import Qgroundcontrol as Qgroundcontrol
    from pynix_os.programs.quark_goldleaf import QuarkGoldleaf as QuarkGoldleaf
    from pynix_os.programs.renderdoc import Renderdoc as Renderdoc
    from pynix_os.programs.river_classic import (
        RiverClassic as RiverClassic,
        RiverClassic_Xwayland as RiverClassic_Xwayland,
    )
    from pynix_os.programs.rog_control_center import RogControlCenter as RogControlCenter
    from pynix_os.programs.rush import Rush as Rush
    from pynix_os.programs.rust_motd import RustMotd as RustMotd
    from pynix_os.programs.ryzen_monitor_ng import RyzenMonitorNg as RyzenMonitorNg
    from pynix_os.programs.schroot import Schroot as Schroot, Schroot_Profiles_Value as Schroot_Profiles_Value
    from pynix_os.programs.screen import Screen as Screen
    from pynix_os.programs.seahorse import Seahorse as Seahorse
    from pynix_os.programs.sedutil import Sedutil as Sedutil
    from pynix_os.programs.sharing import Sharing as Sharing
    from pynix_os.programs.singularity import Singularity as Singularity
    from pynix_os.programs.skim import Skim as Skim
    from pynix_os.programs.slock import Slock as Slock
    from pynix_os.programs.sniffnet import Sniffnet as Sniffnet
    from pynix_os.programs.solaar import Solaar as Solaar, Solaar_UserService as Solaar_UserService
    from pynix_os.programs.soundmodem import Soundmodem as Soundmodem
    from pynix_os.programs.ssh import (
        Ssh as Ssh,
        Ssh_KnownHosts_Value as Ssh_KnownHosts_Value,
        Ssh_SystemdSshProxy as Ssh_SystemdSshProxy,
    )
    from pynix_os.programs.starship import Starship as Starship, Starship_TransientPrompt as Starship_TransientPrompt
    from pynix_os.programs.steam import (
        Steam as Steam,
        Steam_DedicatedServer as Steam_DedicatedServer,
        Steam_Extest as Steam_Extest,
        Steam_GamescopeSession as Steam_GamescopeSession,
        Steam_LocalNetworkGameTransfers as Steam_LocalNetworkGameTransfers,
        Steam_Protontricks as Steam_Protontricks,
        Steam_RemotePlay as Steam_RemotePlay,
    )
    from pynix_os.programs.streamcontroller import Streamcontroller as Streamcontroller
    from pynix_os.programs.streamdeck_ui import StreamdeckUi as StreamdeckUi
    from pynix_os.programs.sway import (
        Sway as Sway,
        Sway_WrapperFeatures as Sway_WrapperFeatures,
        Sway_Xwayland as Sway_Xwayland,
    )
    from pynix_os.programs.sysdig import Sysdig as Sysdig
    from pynix_os.programs.system_config_printer import SystemConfigPrinter as Programs_SystemConfigPrinter
    from pynix_os.programs.systemtap import Systemtap as Systemtap
    from pynix_os.programs.tack import Tack as Tack
    from pynix_os.programs.tcpdump import Tcpdump as Tcpdump
    from pynix_os.programs.television import Television as Television
    from pynix_os.programs.throne import Throne as Throne, Throne_TunMode as Throne_TunMode
    from pynix_os.programs.thunar import Thunar as Thunar
    from pynix_os.programs.thunderbird import Thunderbird as Thunderbird
    from pynix_os.programs.tmux import Tmux as Tmux
    from pynix_os.programs.traceroute import Traceroute as Traceroute
    from pynix_os.programs.trippy import Trippy as Trippy
    from pynix_os.programs.tsmClient import TsmClient as TsmClient, TsmClient_Servers_Value as TsmClient_Servers_Value
    from pynix_os.programs.turbovnc import Turbovnc as Turbovnc
    from pynix_os.programs.tuxclocker import Tuxclocker as Tuxclocker
    from pynix_os.programs.udevil import Udevil as Udevil
    from pynix_os.programs.umbriel import Umbriel as Umbriel
    from pynix_os.programs.usbtop import Usbtop as Usbtop
    from pynix_os.programs.uwsm import Uwsm as Uwsm, Uwsm_WaylandCompositors_Value as Uwsm_WaylandCompositors_Value
    from pynix_os.programs.vellum import Vellum as Vellum
    from pynix_os.programs.vim import Vim as Vim
    from pynix_os.programs.virt_manager import VirtManager as VirtManager
    from pynix_os.programs.vivid import Vivid as Vivid
    from pynix_os.programs.vscode import Vscode as Vscode
    from pynix_os.programs.wavemon import Wavemon as Wavemon
    from pynix_os.programs.waybar import Waybar as Waybar, Waybar_Systemd as Waybar_Systemd
    from pynix_os.programs.wayfire import Wayfire as Wayfire, Wayfire_Xwayland as Wayfire_Xwayland
    from pynix_os.programs.wayland import Wayland as Wayland, Wayland_MiracleWm as Wayland_MiracleWm
    from pynix_os.programs.wayvnc import Wayvnc as Wayvnc
    from pynix_os.programs.weylus import Weylus as Weylus
    from pynix_os.programs.whois import Whois as Whois, Whois_Settings_Item as Whois_Settings_Item
    from pynix_os.programs.winbox import Winbox as Winbox
    from pynix_os.programs.wireshark import (
        Wireshark as Wireshark,
        Wireshark_Dumpcap as Wireshark_Dumpcap,
        Wireshark_Usbmon as Wireshark_Usbmon,
    )
    from pynix_os.programs.wshowkeys import Wshowkeys as Wshowkeys
    from pynix_os.programs.xastir import Xastir as Xastir
    from pynix_os.programs.xfconf import Xfconf as Xfconf
    from pynix_os.programs.xfs_quota import XfsQuota as XfsQuota, XfsQuota_Projects_Value as XfsQuota_Projects_Value
    from pynix_os.programs.xonsh import Xonsh as Xonsh, Xonsh_BashCompletion as Xonsh_BashCompletion
    from pynix_os.programs.xppen import Xppen as Xppen
    from pynix_os.programs.xscreensaver import (
        Xscreensaver as Programs_Xscreensaver,
        Xscreensaver_Sonar as Xscreensaver_Sonar,
    )
    from pynix_os.programs.xss_lock import XssLock as XssLock
    from pynix_os.programs.xwayland import Xwayland as Xwayland
    from pynix_os.programs.yazi import Yazi as Yazi, Yazi_Settings as Yazi_Settings
    from pynix_os.programs.ydotool import Ydotool as Ydotool
    from pynix_os.programs.yubikey_manager import YubikeyManager as YubikeyManager
    from pynix_os.programs.yubikey_touch_detector import YubikeyTouchDetector as YubikeyTouchDetector
    from pynix_os.programs.zmap import Zmap as Zmap
    from pynix_os.programs.zoom_us import ZoomUs as ZoomUs
    from pynix_os.programs.zoxide import Zoxide as Zoxide
    from pynix_os.programs.zsh import (
        Zsh as Zsh,
        Zsh_Autosuggestions as Zsh_Autosuggestions,
        Zsh_OhMyZsh as Zsh_OhMyZsh,
        Zsh_SyntaxHighlighting as Zsh_SyntaxHighlighting,
        Zsh_ZshAutoenv as Zsh_ZshAutoenv,
    )
    from pynix_os.qt.__options__ import Qt as Qt
    from pynix_os.security.__options__ import Security as Security, Security_Wrappers_Value as Security_Wrappers_Value
    from pynix_os.security.account_utils import (
        AccountUtils as AccountUtils,
        AccountUtils_Pwaccessd as AccountUtils_Pwaccessd,
        AccountUtils_Pwaccessd_Settings as AccountUtils_Pwaccessd_Settings,
    )
    from pynix_os.security.acme import (
        Acme as Acme,
        Acme_Certs_Value as Acme_Certs_Value,
        Acme_Defaults as Acme_Defaults,
    )
    from pynix_os.security.agnos import (
        Agnos as Agnos,
        Agnos_GenerateKeys as Agnos_GenerateKeys,
        Agnos_Settings as Agnos_Settings,
        Agnos_Settings_Accounts_Item as Agnos_Settings_Accounts_Item,
        Agnos_Settings_Accounts_Item_Certificates_Item as Agnos_Settings_Accounts_Item_Certificates_Item,
    )
    from pynix_os.security.apparmor import Apparmor as Apparmor, Apparmor_Policies_Value as Apparmor_Policies_Value
    from pynix_os.security.audit import Audit as Audit
    from pynix_os.security.auditd import (
        Auditd as Auditd,
        Auditd_Plugins_Value as Auditd_Plugins_Value,
        Auditd_Plugins_Value_Settings as Auditd_Plugins_Value_Settings,
        Auditd_Settings as Auditd_Settings,
    )
    from pynix_os.security.chromiumSuidSandbox import ChromiumSuidSandbox as ChromiumSuidSandbox
    from pynix_os.security.doas import Doas as Doas, Doas_ExtraRules_Item as Doas_ExtraRules_Item
    from pynix_os.security.duosec import Duosec as Duosec, Duosec_Pam as Duosec_Pam, Duosec_Ssh as Duosec_Ssh
    from pynix_os.security.googleOsLogin import GoogleOsLogin as GoogleOsLogin
    from pynix_os.security.ipa import Ipa as Ipa, Ipa_Dyndns as Ipa_Dyndns
    from pynix_os.security.isolate import Isolate as Isolate
    from pynix_os.security.krb5 import Krb5 as Krb5, Krb5_Settings as Krb5_Settings
    from pynix_os.security.loginDefs import LoginDefs as LoginDefs, LoginDefs_Settings as LoginDefs_Settings
    from pynix_os.security.pam import (
        Pam as Pam,
        Pam_Dp9ik as Pam_Dp9ik,
        Pam_Howdy as Pam_Howdy,
        Pam_Krb5 as Pam_Krb5,
        Pam_LoginLimits_Item as Pam_LoginLimits_Item,
        Pam_MakeHomeDir as Pam_MakeHomeDir,
        Pam_Mount as Pam_Mount,
        Pam_Oath as Pam_Oath,
        Pam_P11 as Pam_P11,
        Pam_Rssh as Pam_Rssh,
        Pam_Rssh_Settings as Pam_Rssh_Settings,
        Pam_Services_Value as Pam_Services_Value,
        Pam_Services_Value_Rules as Pam_Services_Value_Rules,
        Pam_Services_Value_Rules_Account_Value as Pam_Services_Value_Rules_Account_Value,
        Pam_Services_Value_SlurmAdoptSettings as Pam_Services_Value_SlurmAdoptSettings,
        Pam_SshAgentAuth as Pam_SshAgentAuth,
        Pam_U2f as Pam_U2f,
        Pam_U2f_Settings as Pam_U2f_Settings,
        Pam_Ussh as Pam_Ussh,
        Pam_Yubico as Pam_Yubico,
        Pam_Zfs as Pam_Zfs,
    )
    from pynix_os.security.pki import Pki as Pki
    from pynix_os.security.please import Please as Please
    from pynix_os.security.polkit import Polkit as Polkit, Polkit_Settings as Polkit_Settings
    from pynix_os.security.rtkit import Rtkit as Rtkit
    from pynix_os.security.run0 import (
        Run0 as Run0,
        Run0_PersistentAuth as Run0_PersistentAuth,
        Run0_SudoShim as Run0_SudoShim,
    )
    from pynix_os.security.shadow import Shadow as Shadow, Shadow_Su as Shadow_Su
    from pynix_os.security.soteria import Soteria as Soteria
    from pynix_os.security.sudo import (
        Sudo as Sudo,
        Sudo_ExtraRules_Item as Sudo_ExtraRules_Item,
        Sudo_ExtraRules_Item_Commands_Item_Or as Sudo_ExtraRules_Item_Commands_Item_Or,
    )
    from pynix_os.security.sudo_rs import (
        SudoRs as SudoRs,
        SudoRs_ExtraRules_Item as SudoRs_ExtraRules_Item,
        SudoRs_ExtraRules_Item_Commands_Item_Or as SudoRs_ExtraRules_Item_Commands_Item_Or,
    )
    from pynix_os.security.tpm2 import (
        Tpm2 as Security_Tpm2,
        Tpm2_Abrmd as Tpm2_Abrmd,
        Tpm2_Fapi as Tpm2_Fapi,
        Tpm2_Pkcs11 as Tpm2_Pkcs11,
        Tpm2_TctiEnvironment as Tpm2_TctiEnvironment,
    )
    from pynix_os.security.virtualisation import Virtualisation as Security_Virtualisation
    from pynix_os.services.SystemdJournal2Gelf import SystemdJournal2Gelf as SystemdJournal2Gelf
    from pynix_os.services.__options__ import (
        Services as Services,
        Services_Bitcoind_Value as Services_Bitcoind_Value,
        Services_Bitcoind_Value_RpcUsers_Value as Services_Bitcoind_Value_RpcUsers_Value,
        Services_BlockbookFrontend_Value as Services_BlockbookFrontend_Value,
        Services_BuildkiteAgents_Value as Services_BuildkiteAgents_Value,
        Services_Cgit_Value as Services_Cgit_Value,
        Services_Compton as Services_Compton,
        Services_Fedimintd_Value as Services_Fedimintd_Value,
        Services_Fedimintd_Value_NginxConfig as Services_Fedimintd_Value_NginxConfig,
        Services_Fedimintd_Value_NginxConfig_Listen_Item as Services_Fedimintd_Value_NginxConfig_Listen_Item,
        Services_Fedimintd_Value_NginxConfig_Locations_Value as Services_Fedimintd_Value_NginxConfig_Locations_Value,
        Services_Geth_Value as Services_Geth_Value,
        Services_GithubRunners_Value as Services_GithubRunners_Value,
        Services_GithubRunners_Value_GithubApp as Services_GithubRunners_Value_GithubApp,
        Services_GithubRunners_Value_Orgs_Value as Services_GithubRunners_Value_Orgs_Value,
        Services_Gitwatch_Value as Services_Gitwatch_Value,
        Services_Invoiceplane as Services_Invoiceplane,
        Services_Invoiceplane_Sites_Value as Services_Invoiceplane_Sites_Value,
        Services_NixStoreGcsProxy_Value as Services_NixStoreGcsProxy_Value,
        Services_Nylon_Value as Services_Nylon_Value,
        Services_Quicktun_Value as Services_Quicktun_Value,
        Services_Uhub_Value as Services_Uhub_Value,
        Services_Uhub_Value_Plugins_Item as Services_Uhub_Value_Plugins_Item,
    )
    from pynix_os.services.a2boot import A2boot as A2boot
    from pynix_os.services.accounts_daemon import AccountsDaemon as AccountsDaemon
    from pynix_os.services.acme_dns import AcmeDns as AcmeDns, AcmeDns_Settings as AcmeDns_Settings
    from pynix_os.services.acpid import Acpid as Acpid, Acpid_Handlers_Value as Acpid_Handlers_Value
    from pynix_os.services.activemq import Activemq as Activemq
    from pynix_os.services.actkbd import Actkbd as Actkbd, Actkbd_Bindings_Item as Actkbd_Bindings_Item
    from pynix_os.services.actual import Actual as Actual, Actual_Settings as Actual_Settings
    from pynix_os.services.adguardhome import Adguardhome as Adguardhome, Adguardhome_Settings as Adguardhome_Settings
    from pynix_os.services.adw_bluetooth import AdwBluetooth as AdwBluetooth
    from pynix_os.services.aerospike import Aerospike as Aerospike
    from pynix_os.services.aesmd import Aesmd as Aesmd, Aesmd_Settings as Aesmd_Settings
    from pynix_os.services.agate import Agate as Agate
    from pynix_os.services.agorakit import (
        Agorakit as Agorakit,
        Agorakit_Config_Value_Or as Agorakit_Config_Value_Or,
        Agorakit_Database as Agorakit_Database,
        Agorakit_Mail as Agorakit_Mail,
        Agorakit_Nginx as Agorakit_Nginx,
        Agorakit_Nginx_Listen_Item as Agorakit_Nginx_Listen_Item,
        Agorakit_Nginx_Locations_Value as Agorakit_Nginx_Locations_Value,
    )
    from pynix_os.services.airsonic import Airsonic as Airsonic
    from pynix_os.services.akkoma import (
        Akkoma as Akkoma,
        Akkoma_Config as Akkoma_Config,
        Akkoma_Config_NWebPushEncryption as Akkoma_Config_NWebPushEncryption,
        Akkoma_Dist as Akkoma_Dist,
        Akkoma_Frontends_Value as Akkoma_Frontends_Value,
        Akkoma_InitDb as Akkoma_InitDb,
        Akkoma_Nginx as Akkoma_Nginx,
        Akkoma_Nginx_Listen_Item as Akkoma_Nginx_Listen_Item,
        Akkoma_Nginx_Locations_Value as Akkoma_Nginx_Locations_Value,
    )
    from pynix_os.services.alerta import Alerta as Alerta
    from pynix_os.services.alice_lg import AliceLg as AliceLg
    from pynix_os.services.alloy import Alloy as Alloy
    from pynix_os.services.alps import Alps as Alps, Alps_Settings as Alps_Settings
    from pynix_os.services.amazon_cloudwatch_agent import AmazonCloudwatchAgent as AmazonCloudwatchAgent
    from pynix_os.services.amazon_ssm_agent import AmazonSsmAgent as AmazonSsmAgent
    from pynix_os.services.amule import Amule as Amule, Amule_Settings as Amule_Settings
    from pynix_os.services.ananicy import Ananicy as Ananicy
    from pynix_os.services.angrr import (
        Angrr as Angrr,
        Angrr_Settings as Angrr_Settings,
        Angrr_Settings_ProfilePolicies_Value as Angrr_Settings_ProfilePolicies_Value,
        Angrr_Settings_ProfilePolicies_Value_KeepNPerBucket_Item as Angrr_Settings_ProfilePolicies_Value_KeepNPerBucket_Item,
        Angrr_Settings_TemporaryRootPolicies_Value as Angrr_Settings_TemporaryRootPolicies_Value,
        Angrr_Settings_TemporaryRootPolicies_Value_Filter as Angrr_Settings_TemporaryRootPolicies_Value_Filter,
        Angrr_Timer as Angrr_Timer,
    )
    from pynix_os.services.anki_sync_server import (
        AnkiSyncServer as AnkiSyncServer,
        AnkiSyncServer_Users_Item as AnkiSyncServer_Users_Item,
    )
    from pynix_os.services.anubis import (
        Anubis as Anubis,
        Anubis_DefaultOptions as Anubis_DefaultOptions,
        Anubis_DefaultOptions_Policy as Anubis_DefaultOptions_Policy,
        Anubis_DefaultOptions_Settings as Anubis_DefaultOptions_Settings,
        Anubis_Instances_Value as Anubis_Instances_Value,
        Anubis_Instances_Value_Policy as Anubis_Instances_Value_Policy,
        Anubis_Instances_Value_Settings as Anubis_Instances_Value_Settings,
    )
    from pynix_os.services.anuko_time_tracker import (
        AnukoTimeTracker as AnukoTimeTracker,
        AnukoTimeTracker_Database as AnukoTimeTracker_Database,
        AnukoTimeTracker_Nginx as AnukoTimeTracker_Nginx,
        AnukoTimeTracker_Nginx_Listen_Item as AnukoTimeTracker_Nginx_Listen_Item,
        AnukoTimeTracker_Nginx_Locations_Value as AnukoTimeTracker_Nginx_Locations_Value,
        AnukoTimeTracker_Settings as AnukoTimeTracker_Settings,
        AnukoTimeTracker_Settings_Email as AnukoTimeTracker_Settings_Email,
    )
    from pynix_os.services.apache_kafka import (
        ApacheKafka as ApacheKafka,
        ApacheKafka_ConfigFiles as ApacheKafka_ConfigFiles,
        ApacheKafka_Settings as ApacheKafka_Settings,
    )
    from pynix_os.services.apcupsd import Apcupsd as Apcupsd
    from pynix_os.services.arbtt import Arbtt as Arbtt
    from pynix_os.services.archisteamfarm import (
        Archisteamfarm as Archisteamfarm,
        Archisteamfarm_Bots_Value as Archisteamfarm_Bots_Value,
        Archisteamfarm_WebUi as Archisteamfarm_WebUi,
    )
    from pynix_os.services.aria2 import Aria2 as Aria2, Aria2_Settings as Aria2_Settings
    from pynix_os.services.armagetronad import (
        Armagetronad as Armagetronad,
        Armagetronad_Servers_Value as Armagetronad_Servers_Value,
    )
    from pynix_os.services.arsenik import Arsenik as Arsenik
    from pynix_os.services.artalk import Artalk as Artalk, Artalk_Settings as Artalk_Settings
    from pynix_os.services.asterisk import Asterisk as Asterisk
    from pynix_os.services.asusd import Asusd as Asusd, Asusd_AnimeConfig as Asusd_AnimeConfig
    from pynix_os.services.atalkd import Atalkd as Atalkd, Atalkd_Interfaces_Value as Atalkd_Interfaces_Value
    from pynix_os.services.atd import Atd as Atd
    from pynix_os.services.atftpd import Atftpd as Atftpd
    from pynix_os.services.athens import (
        Athens as Athens,
        Athens_Index as Athens_Index,
        Athens_Index_Mysql as Athens_Index_Mysql,
        Athens_Index_Mysql_Params as Athens_Index_Mysql_Params,
        Athens_Index_Postgres as Athens_Index_Postgres,
        Athens_Index_Postgres_Params as Athens_Index_Postgres_Params,
        Athens_SingleFlight as Athens_SingleFlight,
        Athens_SingleFlight_Etcd as Athens_SingleFlight_Etcd,
        Athens_SingleFlight_Redis as Athens_SingleFlight_Redis,
        Athens_SingleFlight_RedisSentinel as Athens_SingleFlight_RedisSentinel,
        Athens_SingleFlight_RedisSentinel_LockConfig as Athens_SingleFlight_RedisSentinel_LockConfig,
        Athens_SingleFlight_Redis_LockConfig as Athens_SingleFlight_Redis_LockConfig,
        Athens_Storage as Athens_Storage,
        Athens_Storage_Azureblob as Athens_Storage_Azureblob,
        Athens_Storage_Cdn as Athens_Storage_Cdn,
        Athens_Storage_Disk as Athens_Storage_Disk,
        Athens_Storage_External as Athens_Storage_External,
        Athens_Storage_Gcp as Athens_Storage_Gcp,
        Athens_Storage_Mongo as Athens_Storage_Mongo,
        Athens_Storage_S3 as Athens_Storage_S3,
    )
    from pynix_os.services.atticd import Atticd as Atticd
    from pynix_os.services.atuin import Atuin_Database as Atuin_Database, Atuin as Services_Atuin
    from pynix_os.services.audiobookshelf import Audiobookshelf as Audiobookshelf
    from pynix_os.services.aurral import Aurral as Aurral
    from pynix_os.services.authelia import (
        Authelia as Authelia,
        Authelia_Instances_Value as Authelia_Instances_Value,
        Authelia_Instances_Value_Secrets as Authelia_Instances_Value_Secrets,
        Authelia_Instances_Value_Settings as Authelia_Instances_Value_Settings,
    )
    from pynix_os.services.auto_cpufreq import AutoCpufreq as AutoCpufreq, AutoCpufreq_Settings as AutoCpufreq_Settings
    from pynix_os.services.auto_epp import AutoEpp as AutoEpp, AutoEpp_Settings as AutoEpp_Settings
    from pynix_os.services.autobrr import Autobrr as Autobrr, Autobrr_Settings as Autobrr_Settings
    from pynix_os.services.autofs import Autofs as Autofs
    from pynix_os.services.automatic_timezoned import AutomaticTimezoned as AutomaticTimezoned
    from pynix_os.services.automx2 import Automx2 as Automx2
    from pynix_os.services.automysqlbackup import Automysqlbackup as Automysqlbackup
    from pynix_os.services.autorandr import (
        Autorandr as Autorandr,
        Autorandr_Hooks as Autorandr_Hooks,
        Autorandr_Profiles_Value as Autorandr_Profiles_Value,
        Autorandr_Profiles_Value_Config_Value as Autorandr_Profiles_Value_Config_Value,
        Autorandr_Profiles_Value_Config_Value_Scale as Autorandr_Profiles_Value_Config_Value_Scale,
    )
    from pynix_os.services.autossh import Autossh as Autossh, Autossh_Sessions_Item as Autossh_Sessions_Item
    from pynix_os.services.autossh_ng import (
        AutosshNg as AutosshNg,
        AutosshNg_Sessions_Value as AutosshNg_Sessions_Value,
    )
    from pynix_os.services.autosuspend import (
        Autosuspend as Autosuspend,
        Autosuspend_Checks_Value as Autosuspend_Checks_Value,
        Autosuspend_Settings as Autosuspend_Settings,
        Autosuspend_Wakeups_Value as Autosuspend_Wakeups_Value,
    )
    from pynix_os.services.autotierfs import Autotierfs as Autotierfs, Autotierfs_Settings as Autotierfs_Settings
    from pynix_os.services.avahi import Avahi as Avahi, Avahi_Publish as Avahi_Publish
    from pynix_os.services.awstats import Awstats as Awstats, Awstats_Configs_Value as Awstats_Configs_Value
    from pynix_os.services.ax25 import (
        Ax25 as Ax25,
        Ax25_Axlisten as Ax25_Axlisten,
        Ax25_Axports_Value as Ax25_Axports_Value,
    )
    from pynix_os.services.ayatana_indicators import AyatanaIndicators as AyatanaIndicators
    from pynix_os.services.babeld import Babeld as Babeld
    from pynix_os.services.bacula_dir import BaculaDir as BaculaDir, BaculaDir_Tls as BaculaDir_Tls
    from pynix_os.services.bacula_fd import (
        BaculaFd as BaculaFd,
        BaculaFd_Director_Value as BaculaFd_Director_Value,
        BaculaFd_Director_Value_Tls as BaculaFd_Director_Value_Tls,
        BaculaFd_Tls as BaculaFd_Tls,
    )
    from pynix_os.services.bacula_sd import (
        BaculaSd as BaculaSd,
        BaculaSd_Autochanger_Value as BaculaSd_Autochanger_Value,
        BaculaSd_Device_Value as BaculaSd_Device_Value,
        BaculaSd_Director_Value as BaculaSd_Director_Value,
        BaculaSd_Director_Value_Tls as BaculaSd_Director_Value_Tls,
        BaculaSd_Tls as BaculaSd_Tls,
    )
    from pynix_os.services.baikal import Baikal as Baikal
    from pynix_os.services.bamf import Bamf as Bamf
    from pynix_os.services.bazarr import Bazarr as Bazarr, Bazarr_Settings as Bazarr_Settings
    from pynix_os.services.bcachefs import Bcachefs_AutoScrub as Bcachefs_AutoScrub, Bcachefs as Services_Bcachefs
    from pynix_os.services.bcg import Bcg as Bcg, Bcg_Mqtt as Bcg_Mqtt
    from pynix_os.services.beanstalkd import Beanstalkd as Beanstalkd, Beanstalkd_Listen as Beanstalkd_Listen
    from pynix_os.services.bee import Bee as Bee
    from pynix_os.services.beesd import Beesd as Beesd, Beesd_Filesystems_Value as Beesd_Filesystems_Value
    from pynix_os.services.below import (
        Below as Below,
        Below_Collect as Below_Collect,
        Below_Compression as Below_Compression,
        Below_Dirs as Below_Dirs,
        Below_Retention as Below_Retention,
    )
    from pynix_os.services.bentopdf import (
        Bentopdf as Bentopdf,
        Bentopdf_Caddy as Bentopdf_Caddy,
        Bentopdf_Caddy_VirtualHost as Bentopdf_Caddy_VirtualHost,
        Bentopdf_Nginx as Bentopdf_Nginx,
        Bentopdf_Nginx_VirtualHost as Bentopdf_Nginx_VirtualHost,
        Bentopdf_Nginx_VirtualHost_Listen_Item as Bentopdf_Nginx_VirtualHost_Listen_Item,
        Bentopdf_Nginx_VirtualHost_Locations_Value as Bentopdf_Nginx_VirtualHost_Locations_Value,
    )
    from pynix_os.services.bepasty import Bepasty as Bepasty, Bepasty_Servers_Value as Bepasty_Servers_Value
    from pynix_os.services.beszel import (
        Beszel as Beszel,
        Beszel_Agent as Beszel_Agent,
        Beszel_Agent_Environment as Beszel_Agent_Environment,
        Beszel_Agent_Smartmon as Beszel_Agent_Smartmon,
        Beszel_Hub as Beszel_Hub,
    )
    from pynix_os.services.biboumi import Biboumi as Biboumi, Biboumi_Settings as Biboumi_Settings
    from pynix_os.services.bind import Bind as Bind, Bind_Zones_Value as Bind_Zones_Value
    from pynix_os.services.bird import Bird as Bird
    from pynix_os.services.bird_lg import (
        BirdLg as BirdLg,
        BirdLg_Frontend as BirdLg_Frontend,
        BirdLg_Frontend_Navbar as BirdLg_Frontend_Navbar,
        BirdLg_Proxy as BirdLg_Proxy,
        BirdLg_Proxy_Traceroute as BirdLg_Proxy_Traceroute,
    )
    from pynix_os.services.birdwatcher import Birdwatcher as Birdwatcher
    from pynix_os.services.bitbox_bridge import BitboxBridge as BitboxBridge
    from pynix_os.services.bitlbee import Bitlbee as Bitlbee
    from pynix_os.services.bitmagnet import (
        Bitmagnet as Bitmagnet,
        Bitmagnet_Settings as Bitmagnet_Settings,
        Bitmagnet_Settings_DhtServer as Bitmagnet_Settings_DhtServer,
        Bitmagnet_Settings_HttpServer as Bitmagnet_Settings_HttpServer,
        Bitmagnet_Settings_Postgres as Bitmagnet_Settings_Postgres,
        Bitmagnet_Settings_Tmdb as Bitmagnet_Settings_Tmdb,
    )
    from pynix_os.services.bitwarden_directory_connector_cli import (
        BitwardenDirectoryConnectorCli as BitwardenDirectoryConnectorCli,
        BitwardenDirectoryConnectorCli_Ldap as BitwardenDirectoryConnectorCli_Ldap,
        BitwardenDirectoryConnectorCli_Secrets as BitwardenDirectoryConnectorCli_Secrets,
        BitwardenDirectoryConnectorCli_Secrets_Bitwarden as BitwardenDirectoryConnectorCli_Secrets_Bitwarden,
        BitwardenDirectoryConnectorCli_Sync as BitwardenDirectoryConnectorCli_Sync,
    )
    from pynix_os.services.blackfire_agent import (
        BlackfireAgent as BlackfireAgent,
        BlackfireAgent_Settings as BlackfireAgent_Settings,
    )
    from pynix_os.services.blendfarm import Blendfarm as Blendfarm, Blendfarm_ServerConfig as Blendfarm_ServerConfig
    from pynix_os.services.blocky import Blocky as Blocky
    from pynix_os.services.bloop import Bloop as Bloop
    from pynix_os.services.blueman import Blueman as Blueman
    from pynix_os.services.bluemap import (
        Bluemap as Bluemap,
        Bluemap_CoreSettings as Bluemap_CoreSettings,
        Bluemap_Maps_Value as Bluemap_Maps_Value,
        Bluemap_Storage_Value as Bluemap_Storage_Value,
        Bluemap_WebappSettings as Bluemap_WebappSettings,
        Bluemap_WebserverSettings as Bluemap_WebserverSettings,
    )
    from pynix_os.services.bluesky_pds import (
        BlueskyPds as BlueskyPds,
        BlueskyPds_Goat as BlueskyPds_Goat,
        BlueskyPds_Pdsadmin as BlueskyPds_Pdsadmin,
        BlueskyPds_Settings as BlueskyPds_Settings,
    )
    from pynix_os.services.boinc import Boinc as Boinc
    from pynix_os.services.bonsaid import Bonsaid as Bonsaid, Bonsaid_Settings_Item as Bonsaid_Settings_Item
    from pynix_os.services.bookorbit import Bookorbit as Bookorbit, Bookorbit_Environment as Bookorbit_Environment
    from pynix_os.services.bookstack import (
        Bookstack as Bookstack,
        Bookstack_Nginx as Bookstack_Nginx,
        Bookstack_Nginx_Listen_Item as Bookstack_Nginx_Listen_Item,
        Bookstack_Nginx_Locations_Value as Bookstack_Nginx_Locations_Value,
        Bookstack_Settings as Bookstack_Settings,
    )
    from pynix_os.services.borgbackup import (
        Borgbackup as Borgbackup,
        Borgbackup_Jobs_Value as Borgbackup_Jobs_Value,
        Borgbackup_Repos_Value as Borgbackup_Repos_Value,
    )
    from pynix_os.services.borgmatic import (
        Borgmatic as Borgmatic,
        Borgmatic_Configurations_Value as Borgmatic_Configurations_Value,
        Borgmatic_Configurations_Value_Repositories_Item as Borgmatic_Configurations_Value_Repositories_Item,
    )
    from pynix_os.services.bpftune import Bpftune as Bpftune
    from pynix_os.services.brltty import Brltty as Brltty
    from pynix_os.services.broadcast_box import (
        BroadcastBox as BroadcastBox,
        BroadcastBox_Settings as BroadcastBox_Settings,
        BroadcastBox_Web as BroadcastBox_Web,
    )
    from pynix_os.services.btrbk import (
        Btrbk as Btrbk,
        Btrbk_Instances_Value as Btrbk_Instances_Value,
        Btrbk_Instances_Value_Settings as Btrbk_Instances_Value_Settings,
        Btrbk_SshAccess_Item as Btrbk_SshAccess_Item,
    )
    from pynix_os.services.btrfs import Btrfs as Btrfs, Btrfs_AutoScrub as Btrfs_AutoScrub
    from pynix_os.services.buffyboard import Buffyboard as Buffyboard, Buffyboard_Settings as Buffyboard_Settings
    from pynix_os.services.buildbot_master import BuildbotMaster as BuildbotMaster
    from pynix_os.services.buildbot_worker import BuildbotWorker as BuildbotWorker
    from pynix_os.services.bulwark import (
        Bulwark as Bulwark,
        Bulwark_Admin as Bulwark_Admin,
        Bulwark_Plugins_Item as Bulwark_Plugins_Item,
        Bulwark_Plugins_Item_Config as Bulwark_Plugins_Item_Config,
        Bulwark_Policies as Bulwark_Policies,
        Bulwark_Policies_RestrictionsAnimationsEnabled as Bulwark_Policies_RestrictionsAnimationsEnabled,
        Bulwark_Settings as Bulwark_Settings,
        Bulwark_Settings_Branding as Bulwark_Settings_Branding,
        Bulwark_Settings_DomainBranding_Value as Bulwark_Settings_DomainBranding_Value,
        Bulwark_Settings_JmapServers_Value as Bulwark_Settings_JmapServers_Value,
        Bulwark_Settings_Oauth as Bulwark_Settings_Oauth,
        Bulwark_Telemetry as Bulwark_Telemetry,
        Bulwark_UpdateCheck as Bulwark_UpdateCheck,
    )
    from pynix_os.services.byedpi import Byedpi as Byedpi
    from pynix_os.services.c2fmzq_server import (
        C2fmzqServer as C2fmzqServer,
        C2fmzqServer_Settings as C2fmzqServer_Settings,
    )
    from pynix_os.services.cachefilesd import Cachefilesd as Cachefilesd
    from pynix_os.services.cachix_agent import CachixAgent as CachixAgent
    from pynix_os.services.cachix_watch_store import CachixWatchStore as CachixWatchStore
    from pynix_os.services.caddy import Caddy as Caddy, Caddy_VirtualHosts_Value as Caddy_VirtualHosts_Value
    from pynix_os.services.cadvisor import Cadvisor as Cadvisor
    from pynix_os.services.cage import Cage as Cage
    from pynix_os.services.calibre_server import (
        CalibreServer as CalibreServer,
        CalibreServer_Auth as CalibreServer_Auth,
    )
    from pynix_os.services.calibre_web import (
        CalibreWeb as CalibreWeb,
        CalibreWeb_Listen as CalibreWeb_Listen,
        CalibreWeb_Options as CalibreWeb_Options,
        CalibreWeb_Options_ReverseProxyAuth as CalibreWeb_Options_ReverseProxyAuth,
    )
    from pynix_os.services.canaille import (
        Canaille as Canaille,
        Canaille_Settings as Canaille_Settings,
        Canaille_Settings_CANAILLEACL as Canaille_Settings_CANAILLEACL,
        Canaille_Settings_CANAILLELDAP as Canaille_Settings_CANAILLELDAP,
        Canaille_Settings_CANAILLEOIDC as Canaille_Settings_CANAILLEOIDC,
        Canaille_Settings_CANAILLESMTP as Canaille_Settings_CANAILLESMTP,
    )
    from pynix_os.services.canto_daemon import CantoDaemon as CantoDaemon
    from pynix_os.services.cardwired import Cardwired as Cardwired, Cardwired_Settings as Cardwired_Settings
    from pynix_os.services.cassandra import Cassandra as Cassandra, Cassandra_JmxRoles_Item as Cassandra_JmxRoles_Item
    from pynix_os.services.castopod import Castopod as Castopod, Castopod_Database as Castopod_Database
    from pynix_os.services.castsponsorskip import Castsponsorskip as Castsponsorskip
    from pynix_os.services.cato_client import CatoClient as CatoClient
    from pynix_os.services.centrifugo import Centrifugo as Centrifugo
    from pynix_os.services.ceph import (
        Ceph as Ceph,
        Ceph_Client as Ceph_Client,
        Ceph_Global as Ceph_Global,
        Ceph_Mds as Ceph_Mds,
        Ceph_Mgr as Ceph_Mgr,
        Ceph_Mon as Ceph_Mon,
        Ceph_Osd as Ceph_Osd,
        Ceph_Rgw as Ceph_Rgw,
    )
    from pynix_os.services.certmgr import Certmgr as Certmgr, Certmgr_Specs_Value_Or as Certmgr_Specs_Value_Or
    from pynix_os.services.certspotter import Certspotter as Certspotter
    from pynix_os.services.cfdyndns import Cfdyndns as Cfdyndns
    from pynix_os.services.cfssl import Cfssl as Cfssl
    from pynix_os.services.cgminer import Cgminer as Cgminer
    from pynix_os.services.changedetection_io import ChangedetectionIo as ChangedetectionIo
    from pynix_os.services.chhoto_url import ChhotoUrl as ChhotoUrl, ChhotoUrl_Settings as ChhotoUrl_Settings
    from pynix_os.services.chisel_server import ChiselServer as ChiselServer
    from pynix_os.services.chromadb import Chromadb as Chromadb
    from pynix_os.services.chrony import (
        Chrony as Chrony,
        Chrony_Initstepslew as Chrony_Initstepslew,
        Chrony_Makestep as Chrony_Makestep,
    )
    from pynix_os.services.cinnamon import Cinnamon_Apps as Cinnamon_Apps, Cinnamon as Services_Cinnamon
    from pynix_os.services.cjdns import (
        Cjdns as Cjdns,
        Cjdns_Admin as Cjdns_Admin,
        Cjdns_ETHInterface as Cjdns_ETHInterface,
        Cjdns_ETHInterface_ConnectTo_Value as Cjdns_ETHInterface_ConnectTo_Value,
        Cjdns_UDPInterface as Cjdns_UDPInterface,
    )
    from pynix_os.services.clamav import (
        Clamav as Clamav,
        Clamav_Clamonacc as Clamav_Clamonacc,
        Clamav_Daemon as Clamav_Daemon,
        Clamav_Fangfrisch as Clamav_Fangfrisch,
        Clamav_Fangfrisch_Settings as Clamav_Fangfrisch_Settings,
        Clamav_Scanner as Clamav_Scanner,
        Clamav_Updater as Clamav_Updater,
    )
    from pynix_os.services.clatd import Clatd as Clatd, Clatd_Settings as Clatd_Settings
    from pynix_os.services.clickhouse import Clickhouse as Clickhouse
    from pynix_os.services.clight import Clight as Clight, Clight_Temperature as Clight_Temperature
    from pynix_os.services.clipcat import Clipcat as Clipcat
    from pynix_os.services.clipmenu import Clipmenu as Clipmenu
    from pynix_os.services.cliproxyapi import Cliproxyapi as Cliproxyapi, Cliproxyapi_Settings as Cliproxyapi_Settings
    from pynix_os.services.cloud_init import (
        CloudInit as CloudInit,
        CloudInit_Btrfs as CloudInit_Btrfs,
        CloudInit_Ext4 as CloudInit_Ext4,
        CloudInit_Network as CloudInit_Network,
        CloudInit_Settings as CloudInit_Settings,
        CloudInit_Xfs as CloudInit_Xfs,
    )
    from pynix_os.services.cloudflare_ddns import (
        CloudflareDdns as CloudflareDdns,
        CloudflareDdns_Provider as CloudflareDdns_Provider,
    )
    from pynix_os.services.cloudflare_dyndns import CloudflareDyndns as CloudflareDyndns
    from pynix_os.services.cloudflare_warp import CloudflareWarp as CloudflareWarp
    from pynix_os.services.cloudflared import (
        Cloudflared as Cloudflared,
        Cloudflared_Tunnels_Value as Cloudflared_Tunnels_Value,
        Cloudflared_Tunnels_Value_Ingress_Value_Or as Cloudflared_Tunnels_Value_Ingress_Value_Or,
    )
    from pynix_os.services.cloudlog import (
        Cloudlog as Cloudlog,
        Cloudlog_Database as Cloudlog_Database,
        Cloudlog_UpdateClublogScp as Cloudlog_UpdateClublogScp,
        Cloudlog_UpdateDok as Cloudlog_UpdateDok,
        Cloudlog_UpdateLotwUsers as Cloudlog_UpdateLotwUsers,
        Cloudlog_UpdateSota as Cloudlog_UpdateSota,
        Cloudlog_UpdateWwff as Cloudlog_UpdateWwff,
        Cloudlog_UploadClublog as Cloudlog_UploadClublog,
        Cloudlog_UploadLotw as Cloudlog_UploadLotw,
        Cloudlog_UploadQrz as Cloudlog_UploadQrz,
    )
    from pynix_os.services.cntlm import Cntlm as Cntlm
    from pynix_os.services.cockpit import Cockpit as Cockpit
    from pynix_os.services.cockroachdb import (
        Cockroachdb as Cockroachdb,
        Cockroachdb_Http as Cockroachdb_Http,
        Cockroachdb_Listen as Cockroachdb_Listen,
    )
    from pynix_os.services.cocoon import Cocoon as Cocoon, Cocoon_Settings as Cocoon_Settings
    from pynix_os.services.code_server import CodeServer as CodeServer
    from pynix_os.services.coder import (
        Coder as Coder,
        Coder_Database as Coder_Database,
        Coder_Environment as Coder_Environment,
    )
    from pynix_os.services.collabora_online import (
        CollaboraOnline as CollaboraOnline,
        CollaboraOnline_AliasGroups_Item as CollaboraOnline_AliasGroups_Item,
    )
    from pynix_os.services.collectd import Collectd as Collectd
    from pynix_os.services.colord import Colord as Colord
    from pynix_os.services.comfyui import Comfyui as Comfyui, Comfyui_Models_Item as Comfyui_Models_Item
    from pynix_os.services.commafeed import Commafeed as Commafeed
    from pynix_os.services.confd import Confd as Confd
    from pynix_os.services.conman import Conman as Conman
    from pynix_os.services.connman import Connman as Connman, Connman_Wifi as Connman_Wifi
    from pynix_os.services.consul import (
        Consul as Consul,
        Consul_Alerts as Consul_Alerts,
        Consul_Interface as Consul_Interface,
    )
    from pynix_os.services.consul_template import (
        ConsulTemplate as ConsulTemplate,
        ConsulTemplate_Instances_Value as ConsulTemplate_Instances_Value,
        ConsulTemplate_Instances_Value_Settings as ConsulTemplate_Instances_Value_Settings,
    )
    from pynix_os.services.convos import Convos as Convos
    from pynix_os.services.cook_cli import CookCli as CookCli
    from pynix_os.services.coredns import Coredns as Coredns
    from pynix_os.services.corerad import Corerad as Corerad
    from pynix_os.services.corosync import Corosync as Corosync, Corosync_Nodelist_Item as Corosync_Nodelist_Item
    from pynix_os.services.corteza import Corteza as Corteza, Corteza_Settings as Corteza_Settings
    from pynix_os.services.coturn import Coturn as Coturn
    from pynix_os.services.couchdb import Couchdb as Couchdb
    from pynix_os.services.cpuminer_cryptonight import CpuminerCryptonight as CpuminerCryptonight
    from pynix_os.services.cpupower_gui import CpupowerGui as CpupowerGui
    from pynix_os.services.crab_hole import CrabHole as CrabHole, CrabHole_Settings as CrabHole_Settings
    from pynix_os.services.create_ap import CreateAp as CreateAp
    from pynix_os.services.croc import Croc as Croc
    from pynix_os.services.cron import Cron as Cron
    from pynix_os.services.cross_seed import CrossSeed as CrossSeed, CrossSeed_Settings as CrossSeed_Settings
    from pynix_os.services.crossfire_server import CrossfireServer as CrossfireServer
    from pynix_os.services.crossmacro import Crossmacro as Crossmacro
    from pynix_os.services.crowdsec import (
        Crowdsec as Crowdsec,
        Crowdsec_Hub as Crowdsec_Hub,
        Crowdsec_LocalConfig as Crowdsec_LocalConfig,
        Crowdsec_LocalConfig_Parsers as Crowdsec_LocalConfig_Parsers,
        Crowdsec_LocalConfig_PostOverflows as Crowdsec_LocalConfig_PostOverflows,
        Crowdsec_Settings as Crowdsec_Settings,
        Crowdsec_Settings_Capi as Crowdsec_Settings_Capi,
        Crowdsec_Settings_Console as Crowdsec_Settings_Console,
        Crowdsec_Settings_Lapi as Crowdsec_Settings_Lapi,
    )
    from pynix_os.services.crowdsec_firewall_bouncer import (
        CrowdsecFirewallBouncer as CrowdsecFirewallBouncer,
        CrowdsecFirewallBouncer_RegisterBouncer as CrowdsecFirewallBouncer_RegisterBouncer,
        CrowdsecFirewallBouncer_Secrets as CrowdsecFirewallBouncer_Secrets,
        CrowdsecFirewallBouncer_Settings as CrowdsecFirewallBouncer_Settings,
    )
    from pynix_os.services.cryptpad import Cryptpad as Cryptpad, Cryptpad_Settings as Cryptpad_Settings
    from pynix_os.services.cyrus_imap import (
        CyrusImap as CyrusImap,
        CyrusImap_CyrusSettings as CyrusImap_CyrusSettings,
        CyrusImap_ImapdSettings as CyrusImap_ImapdSettings,
    )
    from pynix_os.services.dae import Dae as Dae, Dae_OpenFirewall as Dae_OpenFirewall
    from pynix_os.services.dante import Dante as Dante
    from pynix_os.services.darkhttpd import Darkhttpd as Darkhttpd
    from pynix_os.services.das_watchdog import DasWatchdog as DasWatchdog
    from pynix_os.services.dashy import Dashy as Dashy, Dashy_VirtualHost as Dashy_VirtualHost
    from pynix_os.services.datadog_agent import DatadogAgent as DatadogAgent
    from pynix_os.services.davfs2 import Davfs2 as Davfs2, Davfs2_Settings as Davfs2_Settings
    from pynix_os.services.davis import (
        Davis as Davis,
        Davis_Config_Value_Or as Davis_Config_Value_Or,
        Davis_Database as Davis_Database,
        Davis_Mail as Davis_Mail,
        Davis_Nginx as Davis_Nginx,
        Davis_Nginx_Listen_Item as Davis_Nginx_Listen_Item,
        Davis_Nginx_Locations_Value as Davis_Nginx_Locations_Value,
    )
    from pynix_os.services.davmail import Davmail as Davmail
    from pynix_os.services.dawarich import (
        Dawarich as Dawarich,
        Dawarich_Database as Dawarich_Database,
        Dawarich_Redis as Dawarich_Redis,
        Dawarich_SidekiqProcesses_Value as Dawarich_SidekiqProcesses_Value,
        Dawarich_Smtp as Dawarich_Smtp,
    )
    from pynix_os.services.db_rest import DbRest as DbRest, DbRest_Redis as DbRest_Redis
    from pynix_os.services.dbus import Dbus as Dbus
    from pynix_os.services.ddccontrol import Ddccontrol as Ddccontrol
    from pynix_os.services.ddclient import Ddclient as Ddclient
    from pynix_os.services.ddns_updater import DdnsUpdater as DdnsUpdater
    from pynix_os.services.deconz import Deconz as Deconz
    from pynix_os.services.deluge import Deluge as Deluge, Deluge_Web as Deluge_Web
    from pynix_os.services.dendrite import Dendrite as Dendrite, Dendrite_Settings as Dendrite_Settings
    from pynix_os.services.dependency_track import (
        DependencyTrack as DependencyTrack,
        DependencyTrack_Frontend as DependencyTrack_Frontend,
        DependencyTrack_Ldap as DependencyTrack_Ldap,
        DependencyTrack_Nginx as DependencyTrack_Nginx,
        DependencyTrack_Oidc as DependencyTrack_Oidc,
        DependencyTrack_Oidc_Teams as DependencyTrack_Oidc_Teams,
        DependencyTrack_Settings as DependencyTrack_Settings,
    )
    from pynix_os.services.desktopManager import (
        DesktopManager as DesktopManager,
        DesktopManager_Budgie as DesktopManager_Budgie,
        DesktopManager_Cosmic as DesktopManager_Cosmic,
        DesktopManager_Cosmic_Xwayland as DesktopManager_Cosmic_Xwayland,
        DesktopManager_Gnome as DesktopManager_Gnome,
        DesktopManager_Gnome_Flashback as DesktopManager_Gnome_Flashback,
        DesktopManager_Gnome_Flashback_CustomSessions_Item as DesktopManager_Gnome_Flashback_CustomSessions_Item,
        DesktopManager_Lomiri as DesktopManager_Lomiri,
        DesktopManager_Pantheon as DesktopManager_Pantheon,
        DesktopManager_Plasma6 as DesktopManager_Plasma6,
    )
    from pynix_os.services.devmon import Devmon as Devmon
    from pynix_os.services.devpi_server import DevpiServer as DevpiServer
    from pynix_os.services.dex import Dex as Dex
    from pynix_os.services.deye_dummycloud import DeyeDummycloud as DeyeDummycloud
    from pynix_os.services.dgraph import Dgraph as Dgraph, Dgraph_Alpha as Dgraph_Alpha, Dgraph_Zero as Dgraph_Zero
    from pynix_os.services.dictd import Dictd as Dictd
    from pynix_os.services.diod import Diod as Diod
    from pynix_os.services.discourse import (
        Discourse as Discourse,
        Discourse_Admin as Discourse_Admin,
        Discourse_Database as Discourse_Database,
        Discourse_Mail as Discourse_Mail,
        Discourse_Mail_Incoming as Discourse_Mail_Incoming,
        Discourse_Mail_Outgoing as Discourse_Mail_Outgoing,
        Discourse_Nginx as Discourse_Nginx,
        Discourse_Redis as Discourse_Redis,
    )
    from pynix_os.services.disnix import Disnix as Disnix
    from pynix_os.services.displayManager import (
        DisplayManager as DisplayManager,
        DisplayManager_Airlock as DisplayManager_Airlock,
        DisplayManager_Airlock_Compositor as DisplayManager_Airlock_Compositor,
        DisplayManager_Airlock_SyncDynamicScheme as DisplayManager_Airlock_SyncDynamicScheme,
        DisplayManager_AutoLogin as DisplayManager_AutoLogin,
        DisplayManager_CosmicGreeter as DisplayManager_CosmicGreeter,
        DisplayManager_DmsGreeter as DisplayManager_DmsGreeter,
        DisplayManager_DmsGreeter_Compositor as DisplayManager_DmsGreeter_Compositor,
        DisplayManager_DmsGreeter_Logs as DisplayManager_DmsGreeter_Logs,
        DisplayManager_DmsGreeter_Quickshell as DisplayManager_DmsGreeter_Quickshell,
        DisplayManager_Gdm as DisplayManager_Gdm,
        DisplayManager_Gdm_AutoLogin as DisplayManager_Gdm_AutoLogin,
        DisplayManager_Generic as DisplayManager_Generic,
        DisplayManager_Lemurs as DisplayManager_Lemurs,
        DisplayManager_Ly as DisplayManager_Ly,
        DisplayManager_NoctaliaGreeter as DisplayManager_NoctaliaGreeter,
        DisplayManager_NoctaliaGreeter_CursorTheme as DisplayManager_NoctaliaGreeter_CursorTheme,
        DisplayManager_PlasmaLoginManager as DisplayManager_PlasmaLoginManager,
        DisplayManager_Regreet as DisplayManager_Regreet,
        DisplayManager_Regreet_CursorTheme as DisplayManager_Regreet_CursorTheme,
        DisplayManager_Regreet_Font as DisplayManager_Regreet_Font,
        DisplayManager_Regreet_IconTheme as DisplayManager_Regreet_IconTheme,
        DisplayManager_Regreet_Theme as DisplayManager_Regreet_Theme,
        DisplayManager_Sddm as DisplayManager_Sddm,
        DisplayManager_Sddm_AutoLogin as DisplayManager_Sddm_AutoLogin,
        DisplayManager_Sddm_Wayland as DisplayManager_Sddm_Wayland,
    )
    from pynix_os.services.distccd import Distccd as Distccd, Distccd_Stats as Distccd_Stats
    from pynix_os.services.dkimproxy_out import DkimproxyOut as DkimproxyOut
    from pynix_os.services.dleyna import Dleyna as Dleyna
    from pynix_os.services.dnscache import Dnscache as Dnscache
    from pynix_os.services.dnscrypt_proxy import DnscryptProxy as DnscryptProxy
    from pynix_os.services.dnsdist import Dnsdist as Dnsdist, Dnsdist_Dnscrypt as Dnsdist_Dnscrypt
    from pynix_os.services.dnsmasq import Dnsmasq as Dnsmasq, Dnsmasq_Settings as Dnsmasq_Settings
    from pynix_os.services.dnsproxy import Dnsproxy as Dnsproxy
    from pynix_os.services.do_agent import DoAgent as DoAgent
    from pynix_os.services.dockerRegistry import DockerRegistry as DockerRegistry
    from pynix_os.services.docling_serve import DoclingServe as DoclingServe
    from pynix_os.services.documize import Documize as Documize
    from pynix_os.services.docuseal import Docuseal as Docuseal, Docuseal_Redis as Docuseal_Redis
    from pynix_os.services.docuum import Docuum as Docuum
    from pynix_os.services.doh_proxy_rust import DohProxyRust as DohProxyRust
    from pynix_os.services.doh_server import DohServer as DohServer, DohServer_Settings as DohServer_Settings
    from pynix_os.services.dokuwiki import (
        Dokuwiki as Dokuwiki,
        Dokuwiki_Sites_Value as Dokuwiki_Sites_Value,
        Dokuwiki_Sites_Value_Acl_Item as Dokuwiki_Sites_Value_Acl_Item,
    )
    from pynix_os.services.dolibarr import (
        Dolibarr as Dolibarr,
        Dolibarr_H2o as Dolibarr_H2o,
        Dolibarr_H2o_Acme as Dolibarr_H2o_Acme,
        Dolibarr_H2o_Http as Dolibarr_H2o_Http,
        Dolibarr_H2o_Tls as Dolibarr_H2o_Tls,
        Dolibarr_H2o_Tls_Identity_Item as Dolibarr_H2o_Tls_Identity_Item,
        Dolibarr_Nginx as Dolibarr_Nginx,
        Dolibarr_Nginx_Listen_Item as Dolibarr_Nginx_Listen_Item,
        Dolibarr_Nginx_Locations_Value as Dolibarr_Nginx_Locations_Value,
    )
    from pynix_os.services.domoticz import Domoticz as Domoticz
    from pynix_os.services.dovecot2 import (
        Dovecot2 as Dovecot2,
        Dovecot2_Imapsieve as Dovecot2_Imapsieve,
        Dovecot2_Imapsieve_Mailbox_Item as Dovecot2_Imapsieve_Mailbox_Item,
        Dovecot2_MailPlugins as Dovecot2_MailPlugins,
        Dovecot2_MailPlugins_Globally as Dovecot2_MailPlugins_Globally,
        Dovecot2_MailPlugins_PerProtocol_Value as Dovecot2_MailPlugins_PerProtocol_Value,
        Dovecot2_Settings as Dovecot2_Settings,
        Dovecot2_Settings_Extra_Or as Dovecot2_Settings_Extra_Or,
        Dovecot2_Settings_PassdbPam as Dovecot2_Settings_PassdbPam,
        Dovecot2_Settings_Plugin as Dovecot2_Settings_Plugin,
        Dovecot2_Settings_UserdbPasswd as Dovecot2_Settings_UserdbPasswd,
        Dovecot2_Sieve as Dovecot2_Sieve,
    )
    from pynix_os.services.dragonflydb import Dragonflydb as Dragonflydb
    from pynix_os.services.drasl import (
        Drasl as Drasl,
        Drasl_Settings as Drasl_Settings,
        Drasl_Settings_RegistrationOIDC_Item as Drasl_Settings_RegistrationOIDC_Item,
    )
    from pynix_os.services.draupnir import (
        Draupnir as Draupnir,
        Draupnir_Secrets as Draupnir_Secrets,
        Draupnir_Secrets_Pantalaimon as Draupnir_Secrets_Pantalaimon,
        Draupnir_Secrets_Web as Draupnir_Secrets_Web,
        Draupnir_Secrets_Web_SynapseHTTPAntispam as Draupnir_Secrets_Web_SynapseHTTPAntispam,
        Draupnir_Settings as Draupnir_Settings,
    )
    from pynix_os.services.drbd import Drbd as Drbd
    from pynix_os.services.druid import (
        Druid as Druid,
        Druid_Broker as Druid_Broker,
        Druid_Coordinator as Druid_Coordinator,
        Druid_Historical as Druid_Historical,
        Druid_Historical_SegmentLocations_Item as Druid_Historical_SegmentLocations_Item,
        Druid_MiddleManager as Druid_MiddleManager,
        Druid_Overlord as Druid_Overlord,
        Druid_Router as Druid_Router,
    )
    from pynix_os.services.drupal import (
        Drupal as Drupal,
        Drupal_Sites_Value as Drupal_Sites_Value,
        Drupal_Sites_Value_VirtualHost as Drupal_Sites_Value_VirtualHost,
        Drupal_Sites_Value_VirtualHost_Listen_Item as Drupal_Sites_Value_VirtualHost_Listen_Item,
        Drupal_Sites_Value_VirtualHost_Locations_Value as Drupal_Sites_Value_VirtualHost_Locations_Value,
    )
    from pynix_os.services.dsnet import Dsnet as Dsnet, Dsnet_Settings as Dsnet_Settings
    from pynix_os.services.dspam import Dspam as Dspam
    from pynix_os.services.duckdns import Duckdns as Duckdns
    from pynix_os.services.duckling import Duckling as Duckling
    from pynix_os.services.dump1090_fa import Dump1090Fa as Dump1090Fa
    from pynix_os.services.dunst import Dunst as Dunst
    from pynix_os.services.duplicati import Duplicati as Duplicati
    from pynix_os.services.duplicity import Duplicity as Duplicity, Duplicity_Cleanup as Duplicity_Cleanup
    from pynix_os.services.dwm_status import DwmStatus as DwmStatus, DwmStatus_Settings as DwmStatus_Settings
    from pynix_os.services.dysnomia import Dysnomia as Dysnomia
    from pynix_os.services.e_imzo import EImzo as EImzo
    from pynix_os.services.earlyoom import Earlyoom as Earlyoom
    from pynix_os.services.easytier import (
        Easytier as Easytier,
        Easytier_Instances_Value as Easytier_Instances_Value,
        Easytier_Instances_Value_Settings as Easytier_Instances_Value_Settings,
    )
    from pynix_os.services.ebusd import Ebusd as Ebusd, Ebusd_Logs as Ebusd_Logs, Ebusd_Mqtt as Ebusd_Mqtt
    from pynix_os.services.echoip import Echoip as Echoip
    from pynix_os.services.ecs_agent import EcsAgent as EcsAgent
    from pynix_os.services.eg25_manager import Eg25Manager as Eg25Manager
    from pynix_os.services.ejabberd import Ejabberd as Ejabberd
    from pynix_os.services.elasticsearch import Elasticsearch as Elasticsearch
    from pynix_os.services.elasticsearch_curator import ElasticsearchCurator as ElasticsearchCurator
    from pynix_os.services.elephant import Elephant as Elephant
    from pynix_os.services.elk import Elk as Elk, Elk_Settings as Elk_Settings
    from pynix_os.services.emacs import Emacs as Emacs
    from pynix_os.services.endlessh import Endlessh as Endlessh
    from pynix_os.services.endlessh_go import EndlesshGo as EndlesshGo, EndlesshGo_Prometheus as EndlesshGo_Prometheus
    from pynix_os.services.engelsystem import Engelsystem as Engelsystem
    from pynix_os.services.ente import (
        Ente as Ente,
        Ente_Api as Ente_Api,
        Ente_Api_Nginx as Ente_Api_Nginx,
        Ente_Api_Settings as Ente_Api_Settings,
        Ente_Web as Ente_Web,
        Ente_Web_Domains as Ente_Web_Domains,
    )
    from pynix_os.services.envfs import Envfs as Envfs
    from pynix_os.services.envoy import Envoy as Envoy
    from pynix_os.services.epgstation import (
        Epgstation as Epgstation,
        Epgstation_Database as Epgstation_Database,
        Epgstation_Settings as Epgstation_Settings,
    )
    from pynix_os.services.epmd import Epmd as Epmd
    from pynix_os.services.ergo import (
        Ergo as Ergo,
        Ergo_Api as Ergo_Api,
        Ergo_Api_Listen as Ergo_Api_Listen,
        Ergo_Listen as Ergo_Listen,
    )
    from pynix_os.services.ergochat import Ergochat as Ergochat
    from pynix_os.services.erigon import Erigon as Erigon
    from pynix_os.services.errbot import Errbot as Errbot, Errbot_Instances_Value as Errbot_Instances_Value
    from pynix_os.services.ersatztv import Ersatztv as Ersatztv
    from pynix_os.services.esdm import Esdm as Esdm
    from pynix_os.services.espanso import Espanso as Espanso
    from pynix_os.services.esphome import Esphome as Esphome
    from pynix_os.services.etcd import Etcd as Etcd
    from pynix_os.services.etebase_server import (
        EtebaseServer as EtebaseServer,
        EtebaseServer_Settings as EtebaseServer_Settings,
    )
    from pynix_os.services.eternal_terminal import EternalTerminal as EternalTerminal
    from pynix_os.services.etesync_dav import EtesyncDav as EtesyncDav
    from pynix_os.services.evcc import Evcc as Evcc
    from pynix_os.services.evdevremapkeys import Evdevremapkeys as Evdevremapkeys
    from pynix_os.services.evremap import (
        Evremap as Evremap,
        Evremap_Settings as Evremap_Settings,
        Evremap_Settings_DualRole_Item as Evremap_Settings_DualRole_Item,
        Evremap_Settings_Remap_Item as Evremap_Settings_Remap_Item,
    )
    from pynix_os.services.exim import Exim as Exim
    from pynix_os.services.expressvpn import Expressvpn as Expressvpn
    from pynix_os.services.factorio import Factorio as Factorio
    from pynix_os.services.fail2ban import (
        Fail2ban as Fail2ban,
        Fail2ban_BantimeIncrement as Fail2ban_BantimeIncrement,
        Fail2ban_Jails_Value_Or as Fail2ban_Jails_Value_Or,
    )
    from pynix_os.services.fakeroute import Fakeroute as Fakeroute
    from pynix_os.services.fanout import Fanout as Fanout
    from pynix_os.services.fastnetmon_advanced import (
        FastnetmonAdvanced as FastnetmonAdvanced,
        FastnetmonAdvanced_TrafficDb as FastnetmonAdvanced_TrafficDb,
    )
    from pynix_os.services.fcgiwrap import Fcgiwrap as Fcgiwrap, Fcgiwrap_Instances_Value as Fcgiwrap_Instances_Value
    from pynix_os.services.fcron import Fcron as Fcron
    from pynix_os.services.fediwall import (
        Fediwall as Fediwall,
        Fediwall_Nginx as Fediwall_Nginx,
        Fediwall_Nginx_Listen_Item as Fediwall_Nginx_Listen_Item,
        Fediwall_Nginx_Locations_Value as Fediwall_Nginx_Locations_Value,
        Fediwall_Settings as Fediwall_Settings,
    )
    from pynix_os.services.feishin import (
        Feishin as Feishin,
        Feishin_Caddy as Feishin_Caddy,
        Feishin_Caddy_VirtualHost as Feishin_Caddy_VirtualHost,
        Feishin_Nginx as Feishin_Nginx,
        Feishin_Nginx_VirtualHost as Feishin_Nginx_VirtualHost,
        Feishin_Nginx_VirtualHost_Listen_Item as Feishin_Nginx_VirtualHost_Listen_Item,
        Feishin_Nginx_VirtualHost_Locations_Value as Feishin_Nginx_VirtualHost_Locations_Value,
    )
    from pynix_os.services.felix import Felix as Felix
    from pynix_os.services.ferm import Ferm as Ferm
    from pynix_os.services.ferretdb import Ferretdb as Ferretdb, Ferretdb_Settings as Ferretdb_Settings
    from pynix_os.services.fider import Fider as Fider, Fider_Database as Fider_Database
    from pynix_os.services.filebeat import (
        Filebeat as Filebeat,
        Filebeat_Inputs_Value as Filebeat_Inputs_Value,
        Filebeat_Modules_Value as Filebeat_Modules_Value,
        Filebeat_Settings as Filebeat_Settings,
    )
    from pynix_os.services.filebrowser import Filebrowser as Filebrowser, Filebrowser_Settings as Filebrowser_Settings
    from pynix_os.services.firebird import Firebird as Firebird
    from pynix_os.services.firefly_iii import FireflyIii as FireflyIii, FireflyIii_Settings as FireflyIii_Settings
    from pynix_os.services.firefly_iii_data_importer import (
        FireflyIiiDataImporter as FireflyIiiDataImporter,
        FireflyIiiDataImporter_Settings as FireflyIiiDataImporter_Settings,
    )
    from pynix_os.services.firefox_syncserver import (
        FirefoxSyncserver as FirefoxSyncserver,
        FirefoxSyncserver_Settings as FirefoxSyncserver_Settings,
        FirefoxSyncserver_SingleNode as FirefoxSyncserver_SingleNode,
    )
    from pynix_os.services.fireqos import Fireqos as Fireqos
    from pynix_os.services.firewalld import (
        Firewalld as Firewalld,
        Firewalld_Services_Value as Firewalld_Services_Value,
        Firewalld_Services_Value_Destination as Firewalld_Services_Value_Destination,
        Firewalld_Services_Value_Ports_Item as Firewalld_Services_Value_Ports_Item,
        Firewalld_Services_Value_Ports_Item_Port_Or as Firewalld_Services_Value_Ports_Item_Port_Or,
        Firewalld_Settings as Firewalld_Settings,
        Firewalld_Zones_Value as Firewalld_Zones_Value,
        Firewalld_Zones_Value_ForwardPorts_Item as Firewalld_Zones_Value_ForwardPorts_Item,
        Firewalld_Zones_Value_Ports_Item as Firewalld_Zones_Value_Ports_Item,
    )
    from pynix_os.services.firezone import (
        Firezone as Firezone,
        Firezone_Gateway as Firezone_Gateway,
        Firezone_GuiClient as Firezone_GuiClient,
        Firezone_HeadlessClient as Firezone_HeadlessClient,
        Firezone_Relay as Firezone_Relay,
        Firezone_Server as Firezone_Server,
        Firezone_Server_Api as Firezone_Server_Api,
        Firezone_Server_Api_Settings as Firezone_Server_Api_Settings,
        Firezone_Server_Domain as Firezone_Server_Domain,
        Firezone_Server_Nginx as Firezone_Server_Nginx,
        Firezone_Server_Settings as Firezone_Server_Settings,
        Firezone_Server_SettingsSecret as Firezone_Server_SettingsSecret,
        Firezone_Server_Smtp as Firezone_Server_Smtp,
        Firezone_Server_Web as Firezone_Server_Web,
    )
    from pynix_os.services.flame import (
        Flame as Flame,
        Flame_Apps_Item as Flame_Apps_Item,
        Flame_Categories_Item as Flame_Categories_Item,
        Flame_Categories_Item_Bookmarks_Item as Flame_Categories_Item_Bookmarks_Item,
        Flame_Settings as Flame_Settings,
    )
    from pynix_os.services.flannel import Flannel as Flannel, Flannel_Etcd as Flannel_Etcd
    from pynix_os.services.flap_alerted import FlapAlerted as FlapAlerted, FlapAlerted_Settings as FlapAlerted_Settings
    from pynix_os.services.flaresolverr import Flaresolverr as Flaresolverr
    from pynix_os.services.flarum import Flarum as Flarum, Flarum_Database as Flarum_Database
    from pynix_os.services.flatpak import Flatpak as Flatpak
    from pynix_os.services.flexget import Flexget as Flexget
    from pynix_os.services.flood import Flood as Flood
    from pynix_os.services.fluent_bit import FluentBit as FluentBit
    from pynix_os.services.fluentd import Fluentd as Fluentd
    from pynix_os.services.fluidd import (
        Fluidd as Fluidd,
        Fluidd_Nginx as Fluidd_Nginx,
        Fluidd_Nginx_Listen_Item as Fluidd_Nginx_Listen_Item,
        Fluidd_Nginx_Locations_Value as Fluidd_Nginx_Locations_Value,
    )
    from pynix_os.services.foldingathome import Foldingathome as Foldingathome
    from pynix_os.services.forgejo import (
        Forgejo as Forgejo,
        Forgejo_Lfs as Forgejo_Lfs,
        Forgejo_Secrets as Forgejo_Secrets,
        Forgejo_Settings as Forgejo_Settings,
    )
    from pynix_os.services.forgejo_runner import (
        ForgejoRunner as ForgejoRunner,
        ForgejoRunner_Instances_Value as ForgejoRunner_Instances_Value,
        ForgejoRunner_Instances_Value_Settings as ForgejoRunner_Instances_Value_Settings,
        ForgejoRunner_Instances_Value_Settings_ServerConnections_Value as ForgejoRunner_Instances_Value_Settings_ServerConnections_Value,
    )
    from pynix_os.services.foundationdb import (
        Foundationdb as Foundationdb,
        Foundationdb_Locality as Foundationdb_Locality,
        Foundationdb_Tls as Foundationdb_Tls,
    )
    from pynix_os.services.fprintd import Fprintd as Fprintd, Fprintd_Tod as Fprintd_Tod
    from pynix_os.services.fractalart import Fractalart as Fractalart
    from pynix_os.services.framework_control import FrameworkControl as FrameworkControl
    from pynix_os.services.freeciv import Freeciv as Freeciv, Freeciv_Settings as Freeciv_Settings
    from pynix_os.services.freefall import Freefall as Freefall
    from pynix_os.services.freeradius import Freeradius as Freeradius
    from pynix_os.services.freescout import Freescout as Freescout, Freescout_DatabaseSetup as Freescout_DatabaseSetup
    from pynix_os.services.freeswitch import Freeswitch as Freeswitch
    from pynix_os.services.freshrss import Freshrss as Freshrss, Freshrss_Api as Freshrss_Api
    from pynix_os.services.frigate import (
        Frigate as Frigate,
        Frigate_Settings as Frigate_Settings,
        Frigate_Settings_Cameras_Value as Frigate_Settings_Cameras_Value,
        Frigate_Settings_Cameras_Value_FfmpegInputs_Item as Frigate_Settings_Cameras_Value_FfmpegInputs_Item,
    )
    from pynix_os.services.froide_govplan import (
        FroideGovplan as FroideGovplan,
        FroideGovplan_Settings as FroideGovplan_Settings,
    )
    from pynix_os.services.frp import Frp as Frp, Frp_Instances_Value as Frp_Instances_Value
    from pynix_os.services.frr import (
        Frr as Frr,
        Frr_Babeld as Frr_Babeld,
        Frr_Bfdd as Frr_Bfdd,
        Frr_Bgpd as Frr_Bgpd,
        Frr_Eigrpd as Frr_Eigrpd,
        Frr_Fabricd as Frr_Fabricd,
        Frr_Isisd as Frr_Isisd,
        Frr_Ldpd as Frr_Ldpd,
        Frr_Mgmtd as Frr_Mgmtd,
        Frr_Nhrpd as Frr_Nhrpd,
        Frr_Ospf6d as Frr_Ospf6d,
        Frr_Ospfd as Frr_Ospfd,
        Frr_Pathd as Frr_Pathd,
        Frr_Pbrd as Frr_Pbrd,
        Frr_Pim6d as Frr_Pim6d,
        Frr_Pimd as Frr_Pimd,
        Frr_Ripd as Frr_Ripd,
        Frr_Ripngd as Frr_Ripngd,
        Frr_Sharpd as Frr_Sharpd,
        Frr_Staticd as Frr_Staticd,
        Frr_Vrrpd as Frr_Vrrpd,
        Frr_Zebra as Frr_Zebra,
    )
    from pynix_os.services.fstrim import Fstrim as Fstrim
    from pynix_os.services.fusionInventory import FusionInventory as FusionInventory
    from pynix_os.services.fwupd import (
        Fwupd as Fwupd,
        Fwupd_DaemonSettings as Fwupd_DaemonSettings,
        Fwupd_UefiCapsuleSettings as Fwupd_UefiCapsuleSettings,
    )
    from pynix_os.services.g3proxy import G3proxy as G3proxy
    from pynix_os.services.g810_led import G810Led as G810Led
    from pynix_os.services.galene import Galene as Galene
    from pynix_os.services.gammu_smsd import (
        GammuSmsd as GammuSmsd,
        GammuSmsd_Backend as GammuSmsd_Backend,
        GammuSmsd_Backend_Files as GammuSmsd_Backend_Files,
        GammuSmsd_Backend_Sql as GammuSmsd_Backend_Sql,
        GammuSmsd_Device as GammuSmsd_Device,
        GammuSmsd_ExtraConfig as GammuSmsd_ExtraConfig,
        GammuSmsd_Log as GammuSmsd_Log,
    )
    from pynix_os.services.gancio import (
        Gancio as Gancio,
        Gancio_Nginx as Gancio_Nginx,
        Gancio_Nginx_Listen_Item as Gancio_Nginx_Listen_Item,
        Gancio_Nginx_Locations_Value as Gancio_Nginx_Locations_Value,
        Gancio_Settings as Gancio_Settings,
    )
    from pynix_os.services.garage import Garage as Garage, Garage_Settings as Garage_Settings
    from pynix_os.services.garm import Garm as Garm, Garm_Settings as Garm_Settings
    from pynix_os.services.gatus import Gatus as Gatus, Gatus_Settings as Gatus_Settings
    from pynix_os.services.gdomap import Gdomap as Gdomap
    from pynix_os.services.gemstash import Gemstash as Gemstash, Gemstash_Settings as Gemstash_Settings
    from pynix_os.services.geoclue2 import Geoclue2 as Geoclue2, Geoclue2_AppConfig_Value as Geoclue2_AppConfig_Value
    from pynix_os.services.geoipupdate import Geoipupdate as Geoipupdate, Geoipupdate_Settings as Geoipupdate_Settings
    from pynix_os.services.geoserver import Geoserver as Geoserver
    from pynix_os.services.geph import Geph as Geph
    from pynix_os.services.gerbil import Gerbil as Gerbil
    from pynix_os.services.gerrit import Gerrit as Gerrit
    from pynix_os.services.getty import Getty as Getty
    from pynix_os.services.ghostunnel import (
        Ghostunnel as Ghostunnel,
        Ghostunnel_Servers_Value as Ghostunnel_Servers_Value,
    )
    from pynix_os.services.gitDaemon import GitDaemon as GitDaemon
    from pynix_os.services.gitea import Gitea as Gitea, Gitea_Lfs as Gitea_Lfs, Gitea_Settings as Gitea_Settings
    from pynix_os.services.gitea_actions_runner import (
        GiteaActionsRunner as GiteaActionsRunner,
        GiteaActionsRunner_Instances_Value as GiteaActionsRunner_Instances_Value,
        GiteaActionsRunner_Instances_Value_Settings as GiteaActionsRunner_Instances_Value_Settings,
    )
    from pynix_os.services.gitlab import (
        Gitlab as Gitlab,
        Gitlab_Backup as Gitlab_Backup,
        Gitlab_Logrotate as Gitlab_Logrotate,
        Gitlab_Packages as Gitlab_Packages,
        Gitlab_Pages as Gitlab_Pages,
        Gitlab_Pages_Settings as Gitlab_Pages_Settings,
        Gitlab_Puma as Gitlab_Puma,
        Gitlab_Registry as Gitlab_Registry,
        Gitlab_Registry_GarbageCollection as Gitlab_Registry_GarbageCollection,
        Gitlab_Registry_Settings as Gitlab_Registry_Settings,
        Gitlab_Secrets as Gitlab_Secrets,
        Gitlab_Sidekiq as Gitlab_Sidekiq,
        Gitlab_Sidekiq_MemoryKiller as Gitlab_Sidekiq_MemoryKiller,
        Gitlab_Smtp as Gitlab_Smtp,
        Gitlab_Workhorse as Gitlab_Workhorse,
    )
    from pynix_os.services.gitlab_runner import (
        GitlabRunner as GitlabRunner,
        GitlabRunner_ClearDockerCache as GitlabRunner_ClearDockerCache,
        GitlabRunner_Services_Value as GitlabRunner_Services_Value,
        GitlabRunner_Settings as GitlabRunner_Settings,
    )
    from pynix_os.services.gitolite import Gitolite as Gitolite
    from pynix_os.services.gitweb import Gitweb as Gitweb, Gitweb_Nginx as Gitweb_Nginx
    from pynix_os.services.glance import Glance as Glance, Glance_Settings as Glance_Settings
    from pynix_os.services.glances import Glances as Glances
    from pynix_os.services.glitchtip import (
        Glitchtip as Glitchtip,
        Glitchtip_Database as Glitchtip_Database,
        Glitchtip_Nginx as Glitchtip_Nginx,
        Glitchtip_Redis as Glitchtip_Redis,
        Glitchtip_Settings as Glitchtip_Settings,
    )
    from pynix_os.services.glpiAgent import GlpiAgent as GlpiAgent
    from pynix_os.services.glusterfs import Glusterfs as Glusterfs, Glusterfs_TlsSettings as Glusterfs_TlsSettings
    from pynix_os.services.gmediarender import Gmediarender as Gmediarender
    from pynix_os.services.gnome import (
        Gnome_AtSpi2Core as Gnome_AtSpi2Core,
        Gnome_CoreApps as Gnome_CoreApps,
        Gnome_CoreDeveloperTools as Gnome_CoreDeveloperTools,
        Gnome_CoreOsServices as Gnome_CoreOsServices,
        Gnome_CoreShell as Gnome_CoreShell,
        Gnome_EvolutionDataServer as Gnome_EvolutionDataServer,
        Gnome_Games as Gnome_Games,
        Gnome_GcrSshAgent as Gnome_GcrSshAgent,
        Gnome_GlibNetworking as Gnome_GlibNetworking,
        Gnome_GnomeBrowserConnector as Gnome_GnomeBrowserConnector,
        Gnome_GnomeInitialSetup as Gnome_GnomeInitialSetup,
        Gnome_GnomeKeyring as Gnome_GnomeKeyring,
        Gnome_GnomeOnlineAccounts as Gnome_GnomeOnlineAccounts,
        Gnome_GnomeRemoteDesktop as Gnome_GnomeRemoteDesktop,
        Gnome_GnomeSettingsDaemon as Gnome_GnomeSettingsDaemon,
        Gnome_GnomeSoftware as Gnome_GnomeSoftware,
        Gnome_GnomeUserShare as Gnome_GnomeUserShare,
        Gnome_Localsearch as Gnome_Localsearch,
        Gnome_Rygel as Gnome_Rygel,
        Gnome_Sushi as Gnome_Sushi,
        Gnome_Tinysparql as Gnome_Tinysparql,
        Gnome as Services_Gnome,
    )
    from pynix_os.services.gns3_server import (
        Gns3Server as Gns3Server,
        Gns3Server_Auth as Gns3Server_Auth,
        Gns3Server_Dynamips as Gns3Server_Dynamips,
        Gns3Server_Log as Gns3Server_Log,
        Gns3Server_Settings as Gns3Server_Settings,
        Gns3Server_Ssl as Gns3Server_Ssl,
        Gns3Server_Ubridge as Gns3Server_Ubridge,
        Gns3Server_Vpcs as Gns3Server_Vpcs,
    )
    from pynix_os.services.gnunet import (
        Gnunet as Gnunet,
        Gnunet_FileSharing as Gnunet_FileSharing,
        Gnunet_Load as Gnunet_Load,
        Gnunet_Tcp as Gnunet_Tcp,
        Gnunet_Udp as Gnunet_Udp,
    )
    from pynix_os.services.go2rtc import Go2rtc as Go2rtc, Go2rtc_Settings as Go2rtc_Settings
    from pynix_os.services.go_autoconfig import (
        GoAutoconfig as GoAutoconfig,
        GoAutoconfig_Settings as GoAutoconfig_Settings,
    )
    from pynix_os.services.go_camo import GoCamo as GoCamo
    from pynix_os.services.go_csp_collector import (
        GoCspCollector as GoCspCollector,
        GoCspCollector_Settings as GoCspCollector_Settings,
    )
    from pynix_os.services.go_httpbin import GoHttpbin as GoHttpbin, GoHttpbin_Settings as GoHttpbin_Settings
    from pynix_os.services.go_shadowsocks2 import (
        GoShadowsocks2 as GoShadowsocks2,
        GoShadowsocks2_Server as GoShadowsocks2_Server,
    )
    from pynix_os.services.goatcounter import Goatcounter as Goatcounter
    from pynix_os.services.gobgpd import Gobgpd as Gobgpd
    from pynix_os.services.gocd_agent import GocdAgent as GocdAgent
    from pynix_os.services.gocd_server import GocdServer as GocdServer
    from pynix_os.services.gocron import Gocron as Gocron, Gocron_Hardening as Gocron_Hardening
    from pynix_os.services.godns import Godns as Godns, Godns_Settings as Godns_Settings
    from pynix_os.services.goeland import Goeland as Goeland
    from pynix_os.services.gokapi import (
        Gokapi as Gokapi,
        Gokapi_Environment as Gokapi_Environment,
        Gokapi_Settings as Gokapi_Settings,
    )
    from pynix_os.services.gollum import Gollum as Gollum
    from pynix_os.services.gonic import Gonic as Gonic
    from pynix_os.services.gophernicus import Gophernicus as Gophernicus
    from pynix_os.services.goss import Goss as Goss, Goss_Settings as Goss_Settings
    from pynix_os.services.gotenberg import (
        Gotenberg as Gotenberg,
        Gotenberg_Chromium as Gotenberg_Chromium,
        Gotenberg_DownloadFrom as Gotenberg_DownloadFrom,
        Gotenberg_Libreoffice as Gotenberg_Libreoffice,
        Gotenberg_PdfEngines as Gotenberg_PdfEngines,
    )
    from pynix_os.services.gotify import Gotify as Gotify
    from pynix_os.services.gotosocial import Gotosocial as Gotosocial
    from pynix_os.services.goupile import Goupile as Goupile, Goupile_Settings as Goupile_Settings
    from pynix_os.services.govee2mqtt import Govee2mqtt as Govee2mqtt
    from pynix_os.services.goxlr_utility import (
        GoxlrUtility as GoxlrUtility,
        GoxlrUtility_AutoStart as GoxlrUtility_AutoStart,
    )
    from pynix_os.services.gpm import Gpm as Gpm
    from pynix_os.services.gpsd import Gpsd as Gpsd
    from pynix_os.services.grafana import (
        Grafana as Grafana,
        Grafana_Provision as Grafana_Provision,
        Grafana_Provision_Alerting as Grafana_Provision_Alerting,
        Grafana_Provision_Alerting_ContactPoints as Grafana_Provision_Alerting_ContactPoints,
        Grafana_Provision_Alerting_ContactPoints_Settings as Grafana_Provision_Alerting_ContactPoints_Settings,
        Grafana_Provision_Alerting_ContactPoints_Settings_ContactPoints_Item as Grafana_Provision_Alerting_ContactPoints_Settings_ContactPoints_Item,
        Grafana_Provision_Alerting_ContactPoints_Settings_DeleteContactPoints_Item as Grafana_Provision_Alerting_ContactPoints_Settings_DeleteContactPoints_Item,
        Grafana_Provision_Alerting_MuteTimings as Grafana_Provision_Alerting_MuteTimings,
        Grafana_Provision_Alerting_MuteTimings_Settings as Grafana_Provision_Alerting_MuteTimings_Settings,
        Grafana_Provision_Alerting_MuteTimings_Settings_DeleteMuteTimes_Item as Grafana_Provision_Alerting_MuteTimings_Settings_DeleteMuteTimes_Item,
        Grafana_Provision_Alerting_MuteTimings_Settings_MuteTimes_Item as Grafana_Provision_Alerting_MuteTimings_Settings_MuteTimes_Item,
        Grafana_Provision_Alerting_Policies as Grafana_Provision_Alerting_Policies,
        Grafana_Provision_Alerting_Policies_Settings as Grafana_Provision_Alerting_Policies_Settings,
        Grafana_Provision_Alerting_Policies_Settings_Policies_Item as Grafana_Provision_Alerting_Policies_Settings_Policies_Item,
        Grafana_Provision_Alerting_Rules as Grafana_Provision_Alerting_Rules,
        Grafana_Provision_Alerting_Rules_Settings as Grafana_Provision_Alerting_Rules_Settings,
        Grafana_Provision_Alerting_Rules_Settings_DeleteRules_Item as Grafana_Provision_Alerting_Rules_Settings_DeleteRules_Item,
        Grafana_Provision_Alerting_Rules_Settings_Groups_Item as Grafana_Provision_Alerting_Rules_Settings_Groups_Item,
        Grafana_Provision_Alerting_Templates as Grafana_Provision_Alerting_Templates,
        Grafana_Provision_Alerting_Templates_Settings as Grafana_Provision_Alerting_Templates_Settings,
        Grafana_Provision_Alerting_Templates_Settings_DeleteTemplates_Item as Grafana_Provision_Alerting_Templates_Settings_DeleteTemplates_Item,
        Grafana_Provision_Alerting_Templates_Settings_Templates_Item as Grafana_Provision_Alerting_Templates_Settings_Templates_Item,
        Grafana_Provision_Dashboards as Grafana_Provision_Dashboards,
        Grafana_Provision_Dashboards_Settings as Grafana_Provision_Dashboards_Settings,
        Grafana_Provision_Dashboards_Settings_Providers_Item as Grafana_Provision_Dashboards_Settings_Providers_Item,
        Grafana_Provision_Datasources as Grafana_Provision_Datasources,
        Grafana_Provision_Datasources_Settings as Grafana_Provision_Datasources_Settings,
        Grafana_Provision_Datasources_Settings_Datasources_Item as Grafana_Provision_Datasources_Settings_Datasources_Item,
        Grafana_Provision_Datasources_Settings_DeleteDatasources_Item as Grafana_Provision_Datasources_Settings_DeleteDatasources_Item,
        Grafana_Settings as Grafana_Settings,
    )
    from pynix_os.services.grafana_image_renderer import (
        GrafanaImageRenderer as GrafanaImageRenderer,
        GrafanaImageRenderer_Settings as GrafanaImageRenderer_Settings,
    )
    from pynix_os.services.grafana_reporter import (
        GrafanaReporter as GrafanaReporter,
        GrafanaReporter_Grafana as GrafanaReporter_Grafana,
    )
    from pynix_os.services.grafana_to_ntfy import (
        GrafanaToNtfy as GrafanaToNtfy,
        GrafanaToNtfy_Settings as GrafanaToNtfy_Settings,
    )
    from pynix_os.services.graphical_desktop import GraphicalDesktop as GraphicalDesktop
    from pynix_os.services.graphite import (
        Graphite as Graphite,
        Graphite_Carbon as Graphite_Carbon,
        Graphite_Seyren as Graphite_Seyren,
        Graphite_Web as Graphite_Web,
    )
    from pynix_os.services.grav import Grav as Grav
    from pynix_os.services.graylog import Graylog as Graylog
    from pynix_os.services.greenclip import Greenclip as Greenclip
    from pynix_os.services.greenlight import (
        Greenlight as Greenlight,
        Greenlight_Database as Greenlight_Database,
        Greenlight_Redis as Greenlight_Redis,
        Greenlight_Settings as Greenlight_Settings,
    )
    from pynix_os.services.greetd import Greetd as Greetd
    from pynix_os.services.grist import Grist as Grist, Grist_Environment as Grist_Environment
    from pynix_os.services.grocy import (
        Grocy as Grocy,
        Grocy_Nginx as Grocy_Nginx,
        Grocy_Phpfpm as Grocy_Phpfpm,
        Grocy_Settings as Grocy_Settings,
        Grocy_Settings_Calendar as Grocy_Settings_Calendar,
    )
    from pynix_os.services.gs1200_exporter import Gs1200Exporter as Gs1200Exporter
    from pynix_os.services.guacamole_client import (
        GuacamoleClient as GuacamoleClient,
        GuacamoleClient_Settings as GuacamoleClient_Settings,
    )
    from pynix_os.services.guacamole_server import GuacamoleServer as GuacamoleServer
    from pynix_os.services.guix import (
        Guix as Guix,
        Guix_Gc as Guix_Gc,
        Guix_Publish as Guix_Publish,
        Guix_Substituters as Guix_Substituters,
    )
    from pynix_os.services.gvfs import Gvfs as Gvfs
    from pynix_os.services.gvpe import Gvpe as Gvpe
    from pynix_os.services.h2o import (
        H2o as H2o,
        H2o_Hosts_Value as H2o_Hosts_Value,
        H2o_Hosts_Value_Acme as H2o_Hosts_Value_Acme,
        H2o_Hosts_Value_Http as H2o_Hosts_Value_Http,
        H2o_Hosts_Value_Tls as H2o_Hosts_Value_Tls,
        H2o_Hosts_Value_Tls_Identity_Item as H2o_Hosts_Value_Tls_Identity_Item,
    )
    from pynix_os.services.hadoop import (
        Hadoop as Hadoop,
        Hadoop_GatewayRole as Hadoop_GatewayRole,
        Hadoop_Hbase as Hadoop_Hbase,
        Hadoop_Hbase_Master as Hadoop_Hbase_Master,
        Hadoop_Hbase_RegionServer as Hadoop_Hbase_RegionServer,
        Hadoop_Hbase_Rest as Hadoop_Hbase_Rest,
        Hadoop_Hbase_Thrift as Hadoop_Hbase_Thrift,
        Hadoop_Hdfs as Hadoop_Hdfs,
        Hadoop_Hdfs_Datanode as Hadoop_Hdfs_Datanode,
        Hadoop_Hdfs_Datanode_DataDirs_Item as Hadoop_Hdfs_Datanode_DataDirs_Item,
        Hadoop_Hdfs_Httpfs as Hadoop_Hdfs_Httpfs,
        Hadoop_Hdfs_Journalnode as Hadoop_Hdfs_Journalnode,
        Hadoop_Hdfs_Namenode as Hadoop_Hdfs_Namenode,
        Hadoop_Hdfs_Zkfc as Hadoop_Hdfs_Zkfc,
        Hadoop_Yarn as Hadoop_Yarn,
        Hadoop_Yarn_Nodemanager as Hadoop_Yarn_Nodemanager,
        Hadoop_Yarn_Nodemanager_Resource as Hadoop_Yarn_Nodemanager_Resource,
        Hadoop_Yarn_Resourcemanager as Hadoop_Yarn_Resourcemanager,
    )
    from pynix_os.services.handheld_daemon import (
        HandheldDaemon as HandheldDaemon,
        HandheldDaemon_Adjustor as HandheldDaemon_Adjustor,
        HandheldDaemon_Ui as HandheldDaemon_Ui,
    )
    from pynix_os.services.hans import (
        Hans as Hans,
        Hans_Clients_Value as Hans_Clients_Value,
        Hans_Server as Hans_Server,
    )
    from pynix_os.services.haproxy import Haproxy as Haproxy
    from pynix_os.services.hardware import (
        Hardware_Argonone as Hardware_Argonone,
        Hardware_Bolt as Hardware_Bolt,
        Hardware_DeepcoolDigitalLinux as Hardware_DeepcoolDigitalLinux,
        Hardware_DellBiosFanControl as Hardware_DellBiosFanControl,
        Hardware_Lcd as Hardware_Lcd,
        Hardware_Lcd_Client as Hardware_Lcd_Client,
        Hardware_Lcd_Server as Hardware_Lcd_Server,
        Hardware_Openrgb as Hardware_Openrgb,
        Hardware_Openrgb_Server as Hardware_Openrgb_Server,
        Hardware_Pommed as Hardware_Pommed,
        Hardware as Services_Hardware,
    )
    from pynix_os.services.harmonia import (
        Harmonia as Harmonia,
        Harmonia_Cache as Harmonia_Cache,
        Harmonia_Daemon as Harmonia_Daemon,
        Harmonia_Gc as Harmonia_Gc,
    )
    from pynix_os.services.haste_server import HasteServer as HasteServer
    from pynix_os.services.hatsu import Hatsu as Hatsu, Hatsu_Settings as Hatsu_Settings
    from pynix_os.services.haveged import Haveged as Haveged
    from pynix_os.services.haven import Haven as Haven
    from pynix_os.services.hbase_standalone import HbaseStandalone as HbaseStandalone
    from pynix_os.services.hdapsd import Hdapsd as Hdapsd
    from pynix_os.services.hddfancontrol import (
        Hddfancontrol as Hddfancontrol,
        Hddfancontrol_Settings_Value as Hddfancontrol_Settings_Value,
    )
    from pynix_os.services.headphones import Headphones as Headphones
    from pynix_os.services.headplane import (
        Headplane as Headplane,
        Headplane_Agent as Headplane_Agent,
        Headplane_Settings as Headplane_Settings,
        Headplane_Settings_Headscale as Headplane_Settings_Headscale,
        Headplane_Settings_Integration as Headplane_Settings_Integration,
        Headplane_Settings_Integration_Agent as Headplane_Settings_Integration_Agent,
        Headplane_Settings_Integration_Proc as Headplane_Settings_Integration_Proc,
        Headplane_Settings_Oidc as Headplane_Settings_Oidc,
        Headplane_Settings_Server as Headplane_Settings_Server,
        Headplane_Settings_Server_ProxyAuth as Headplane_Settings_Server_ProxyAuth,
    )
    from pynix_os.services.headscale import (
        Headscale as Headscale,
        Headscale_Settings as Headscale_Settings,
        Headscale_Settings_DnsExtraRecords_Item as Headscale_Settings_DnsExtraRecords_Item,
    )
    from pynix_os.services.healthchecks import (
        Healthchecks as Healthchecks,
        Healthchecks_Settings as Healthchecks_Settings,
    )
    from pynix_os.services.heapster import Heapster as Heapster
    from pynix_os.services.heartbeat import Heartbeat as Heartbeat
    from pynix_os.services.hebbot import Hebbot as Hebbot, Hebbot_Templates as Hebbot_Templates
    from pynix_os.services.hedgedoc import Hedgedoc as Hedgedoc, Hedgedoc_Settings as Hedgedoc_Settings
    from pynix_os.services.heisenbridge import (
        Heisenbridge as Heisenbridge,
        Heisenbridge_Identd as Heisenbridge_Identd,
        Heisenbridge_Namespaces as Heisenbridge_Namespaces,
    )
    from pynix_os.services.hercules_ci_agent import (
        HerculesCiAgent as HerculesCiAgent,
        HerculesCiAgent_Settings as HerculesCiAgent_Settings,
    )
    from pynix_os.services.hickory_dns import (
        HickoryDns as HickoryDns,
        HickoryDns_Settings as HickoryDns_Settings,
        HickoryDns_Settings_Zones_Item as HickoryDns_Settings_Zones_Item,
    )
    from pynix_os.services.hister import Hister as Hister
    from pynix_os.services.hitch import Hitch as Hitch, Hitch_OcspStapling as Hitch_OcspStapling
    from pynix_os.services.hledger_web import HledgerWeb as HledgerWeb
    from pynix_os.services.hockeypuck import Hockeypuck as Hockeypuck
    from pynix_os.services.hologram_agent import HologramAgent as HologramAgent
    from pynix_os.services.hologram_server import HologramServer as HologramServer
    from pynix_os.services.home_assistant import (
        HomeAssistant as HomeAssistant,
        HomeAssistant_Blueprints as HomeAssistant_Blueprints,
        HomeAssistant_Config as HomeAssistant_Config,
    )
    from pynix_os.services.home_assistant_matter_hub import (
        HomeAssistantMatterHub as HomeAssistantMatterHub,
        HomeAssistantMatterHub_Settings as HomeAssistantMatterHub_Settings,
    )
    from pynix_os.services.homebox import (
        Homebox as Homebox,
        Homebox_Database as Homebox_Database,
        Homebox_Secrets as Homebox_Secrets,
        Homebox_Settings as Homebox_Settings,
    )
    from pynix_os.services.homebridge import (
        Homebridge as Homebridge,
        Homebridge_Settings as Homebridge_Settings,
        Homebridge_Settings_Accessories_Item as Homebridge_Settings_Accessories_Item,
        Homebridge_Settings_Platforms_Item as Homebridge_Settings_Platforms_Item,
        Homebridge_UiSettings as Homebridge_UiSettings,
    )
    from pynix_os.services.homed import (
        Homed as Homed,
        Homed_Settings as Homed_Settings,
        Homed_Settings_Home as Homed_Settings_Home,
    )
    from pynix_os.services.homepage_dashboard import HomepageDashboard as HomepageDashboard
    from pynix_os.services.homer import (
        Homer as Homer,
        Homer_VirtualHost as Homer_VirtualHost,
        Homer_VirtualHost_Caddy as Homer_VirtualHost_Caddy,
        Homer_VirtualHost_Nginx as Homer_VirtualHost_Nginx,
    )
    from pynix_os.services.hoogle import Hoogle as Hoogle
    from pynix_os.services.hostapd import (
        Hostapd as Hostapd,
        Hostapd_Radios_Value as Hostapd_Radios_Value,
        Hostapd_Radios_Value_Networks_Value as Hostapd_Radios_Value_Networks_Value,
        Hostapd_Radios_Value_Networks_Value_AuthenticationSaePasswords_Item as Hostapd_Radios_Value_Networks_Value_AuthenticationSaePasswords_Item,
        Hostapd_Radios_Value_Networks_Value_Settings as Hostapd_Radios_Value_Networks_Value_Settings,
        Hostapd_Radios_Value_Settings as Hostapd_Radios_Value_Settings,
    )
    from pynix_os.services.hound import Hound as Hound
    from pynix_os.services.howdy import Howdy as Howdy
    from pynix_os.services.hqplayerd import Hqplayerd as Hqplayerd, Hqplayerd_Auth as Hqplayerd_Auth
    from pynix_os.services.htpdate import Htpdate as Htpdate
    from pynix_os.services.httpd import (
        Httpd as Httpd,
        Httpd_VirtualHosts_Value as Httpd_VirtualHosts_Value,
        Httpd_VirtualHosts_Value_Listen_Item as Httpd_VirtualHosts_Value_Listen_Item,
        Httpd_VirtualHosts_Value_Locations_Value as Httpd_VirtualHosts_Value_Locations_Value,
    )
    from pynix_os.services.https_dns_proxy import (
        HttpsDnsProxy as HttpsDnsProxy,
        HttpsDnsProxy_Provider as HttpsDnsProxy_Provider,
    )
    from pynix_os.services.hydra import (
        Hydra as Hydra,
        Hydra_AdHoc as Hydra_AdHoc,
        Hydra_AdHoc_Settings as Hydra_AdHoc_Settings,
        Hydra_EvaluatorSettings as Hydra_EvaluatorSettings,
        Hydra_QueueRunner as Hydra_QueueRunner,
        Hydra_QueueRunner_Grpc as Hydra_QueueRunner_Grpc,
        Hydra_QueueRunner_Mtls as Hydra_QueueRunner_Mtls,
        Hydra_QueueRunner_Rest as Hydra_QueueRunner_Rest,
        Hydra_QueueRunner_Settings as Hydra_QueueRunner_Settings,
        Hydra_QueueRunner_Settings_OverflowStore as Hydra_QueueRunner_Settings_OverflowStore,
        Hydra_Ws as Hydra_Ws,
        Hydra_Ws_Bind as Hydra_Ws_Bind,
        Hydra_Ws_Settings as Hydra_Ws_Settings,
    )
    from pynix_os.services.hydra_builder import (
        HydraBuilder as HydraBuilder,
        HydraBuilder_Mtls as HydraBuilder_Mtls,
        HydraBuilder_Settings as HydraBuilder_Settings,
    )
    from pynix_os.services.hylafax import (
        Hylafax as Hylafax,
        Hylafax_Faxcron as Hylafax_Faxcron,
        Hylafax_Faxcron_Enable as Hylafax_Faxcron_Enable,
        Hylafax_Faxqclean as Hylafax_Faxqclean,
        Hylafax_Faxqclean_Enable as Hylafax_Faxqclean_Enable,
        Hylafax_Modems_Value as Hylafax_Modems_Value,
    )
    from pynix_os.services.hyphanet import Hyphanet as Hyphanet
    from pynix_os.services.hypridle import Hypridle as Hypridle
    from pynix_os.services.hyprwhspr_rs import HyprwhsprRs as HyprwhsprRs
    from pynix_os.services.i2p import I2p as I2p
    from pynix_os.services.i2pd import (
        I2pd as I2pd,
        I2pd_ClientTunnels_Value as I2pd_ClientTunnels_Value,
        I2pd_ServerTunnels_Value as I2pd_ServerTunnels_Value,
        I2pd_Settings as I2pd_Settings,
    )
    from pynix_os.services.icecast import (
        Icecast as Icecast,
        Icecast_Admin as Icecast_Admin,
        Icecast_Listen as Icecast_Listen,
    )
    from pynix_os.services.icecream import (
        Icecream as Icecream,
        Icecream_Daemon as Icecream_Daemon,
        Icecream_Scheduler as Icecream_Scheduler,
    )
    from pynix_os.services.icingaweb2 import (
        Icingaweb2 as Icingaweb2,
        Icingaweb2_Modules as Icingaweb2_Modules,
        Icingaweb2_Modules_Doc as Icingaweb2_Modules_Doc,
        Icingaweb2_Modules_Migrate as Icingaweb2_Modules_Migrate,
        Icingaweb2_Modules_Monitoring as Icingaweb2_Modules_Monitoring,
        Icingaweb2_Modules_Monitoring_Backends_Value as Icingaweb2_Modules_Monitoring_Backends_Value,
        Icingaweb2_Modules_Monitoring_GeneralConfig as Icingaweb2_Modules_Monitoring_GeneralConfig,
        Icingaweb2_Modules_Monitoring_Transports_Value as Icingaweb2_Modules_Monitoring_Transports_Value,
        Icingaweb2_Modules_Setup as Icingaweb2_Modules_Setup,
        Icingaweb2_Modules_Test as Icingaweb2_Modules_Test,
        Icingaweb2_Modules_Translation as Icingaweb2_Modules_Translation,
    )
    from pynix_os.services.ifm import Ifm as Ifm
    from pynix_os.services.ihaskell import Ihaskell as Ihaskell
    from pynix_os.services.iio_niri import IioNiri as IioNiri
    from pynix_os.services.illum import Illum as Illum
    from pynix_os.services.imaginary import Imaginary as Imaginary, Imaginary_Settings as Imaginary_Settings
    from pynix_os.services.immich import (
        Immich as Immich,
        Immich_Database as Immich_Database,
        Immich_Environment as Immich_Environment,
        Immich_MachineLearning as Immich_MachineLearning,
        Immich_MachineLearning_Environment as Immich_MachineLearning_Environment,
        Immich_Redis as Immich_Redis,
        Immich_Settings as Immich_Settings,
    )
    from pynix_os.services.immich_kiosk import ImmichKiosk as ImmichKiosk, ImmichKiosk_Settings as ImmichKiosk_Settings
    from pynix_os.services.immich_public_proxy import (
        ImmichPublicProxy as ImmichPublicProxy,
        ImmichPublicProxy_Settings as ImmichPublicProxy_Settings,
    )
    from pynix_os.services.immichframe import (
        Immichframe as Immichframe,
        Immichframe_Settings as Immichframe_Settings,
        Immichframe_Settings_Accounts_Item as Immichframe_Settings_Accounts_Item,
    )
    from pynix_os.services.inadyn import (
        Inadyn as Inadyn,
        Inadyn_Settings as Inadyn_Settings,
        Inadyn_Settings_Custom_Value as Inadyn_Settings_Custom_Value,
        Inadyn_Settings_Provider_Value as Inadyn_Settings_Provider_Value,
    )
    from pynix_os.services.incron import Incron as Incron
    from pynix_os.services.infinoted import Infinoted as Infinoted
    from pynix_os.services.influxdb import Influxdb as Influxdb, Influxdb_Settings as Influxdb_Settings
    from pynix_os.services.influxdb2 import (
        Influxdb2 as Influxdb2,
        Influxdb2_Provision as Influxdb2_Provision,
        Influxdb2_Provision_InitialSetup as Influxdb2_Provision_InitialSetup,
        Influxdb2_Provision_Organizations_Value as Influxdb2_Provision_Organizations_Value,
        Influxdb2_Provision_Organizations_Value_Auths_Value as Influxdb2_Provision_Organizations_Value_Auths_Value,
        Influxdb2_Provision_Organizations_Value_Buckets_Value as Influxdb2_Provision_Organizations_Value_Buckets_Value,
        Influxdb2_Provision_Users_Value as Influxdb2_Provision_Users_Value,
    )
    from pynix_os.services.infnoise import Infnoise as Infnoise
    from pynix_os.services.input_remapper import InputRemapper as InputRemapper
    from pynix_os.services.inputplumber import Inputplumber as Inputplumber
    from pynix_os.services.inspircd import Inspircd as Inspircd
    from pynix_os.services.interception_tools import InterceptionTools as InterceptionTools
    from pynix_os.services.intune import Intune as Intune
    from pynix_os.services.inventree import Inventree as Inventree, Inventree_Database as Inventree_Database
    from pynix_os.services.invidious import (
        Invidious as Invidious,
        Invidious_Database as Invidious_Database,
        Invidious_Http3Ytproxy as Invidious_Http3Ytproxy,
        Invidious_Nginx as Invidious_Nginx,
        Invidious_SigHelper as Invidious_SigHelper,
    )
    from pynix_os.services.invidious_router import (
        InvidiousRouter as InvidiousRouter,
        InvidiousRouter_Nginx as InvidiousRouter_Nginx,
        InvidiousRouter_Settings as InvidiousRouter_Settings,
    )
    from pynix_os.services.iocaine import Iocaine as Iocaine, Iocaine_Settings as Iocaine_Settings
    from pynix_os.services.iodine import (
        Iodine as Iodine,
        Iodine_Clients_Value as Iodine_Clients_Value,
        Iodine_Server as Iodine_Server,
    )
    from pynix_os.services.iperf3 import Iperf3 as Iperf3
    from pynix_os.services.ipfs_cluster import IpfsCluster as IpfsCluster
    from pynix_os.services.ipp_usb import IppUsb as IppUsb
    from pynix_os.services.iptsd import Iptsd as Iptsd, Iptsd_Config as Iptsd_Config
    from pynix_os.services.ircdHybrid import IrcdHybrid as IrcdHybrid
    from pynix_os.services.irkerd import Irkerd as Irkerd
    from pynix_os.services.irqbalance import Irqbalance as Irqbalance
    from pynix_os.services.isso import Isso as Isso, Isso_Settings as Isso_Settings
    from pynix_os.services.ivpn import Ivpn as Ivpn
    from pynix_os.services.jack import (
        Jack as Jack,
        Jack_Alsa as Jack_Alsa,
        Jack_Jackd as Jack_Jackd,
        Jack_Loopback as Jack_Loopback,
    )
    from pynix_os.services.jackett import Jackett as Jackett
    from pynix_os.services.jboss import Jboss as Jboss
    from pynix_os.services.jellyfin import (
        Jellyfin as Jellyfin,
        Jellyfin_Transcoding as Jellyfin_Transcoding,
        Jellyfin_Transcoding_HardwareDecodingCodecs as Jellyfin_Transcoding_HardwareDecodingCodecs,
        Jellyfin_Transcoding_HardwareEncodingCodecs as Jellyfin_Transcoding_HardwareEncodingCodecs,
    )
    from pynix_os.services.jenkins import Jenkins as Jenkins, Jenkins_JobBuilder as Jenkins_JobBuilder
    from pynix_os.services.jenkinsSlave import JenkinsSlave as JenkinsSlave
    from pynix_os.services.jibri import Jibri as Jibri, Jibri_XmppEnvironments_Value as Jibri_XmppEnvironments_Value
    from pynix_os.services.jicofo import Jicofo as Jicofo
    from pynix_os.services.jigasi import Jigasi as Jigasi
    from pynix_os.services.jirafeau import (
        Jirafeau as Jirafeau,
        Jirafeau_NginxConfig as Jirafeau_NginxConfig,
        Jirafeau_NginxConfig_Listen_Item as Jirafeau_NginxConfig_Listen_Item,
        Jirafeau_NginxConfig_Locations_Value as Jirafeau_NginxConfig_Locations_Value,
    )
    from pynix_os.services.jitsi_meet import (
        JitsiMeet as JitsiMeet,
        JitsiMeet_Caddy as JitsiMeet_Caddy,
        JitsiMeet_Excalidraw as JitsiMeet_Excalidraw,
        JitsiMeet_Jibri as JitsiMeet_Jibri,
        JitsiMeet_Jicofo as JitsiMeet_Jicofo,
        JitsiMeet_Jigasi as JitsiMeet_Jigasi,
        JitsiMeet_Nginx as JitsiMeet_Nginx,
        JitsiMeet_Prosody as JitsiMeet_Prosody,
        JitsiMeet_SecureDomain as JitsiMeet_SecureDomain,
        JitsiMeet_Videobridge as JitsiMeet_Videobridge,
    )
    from pynix_os.services.jitsi_videobridge import (
        JitsiVideobridge as JitsiVideobridge,
        JitsiVideobridge_Nat as JitsiVideobridge_Nat,
        JitsiVideobridge_XmppConfigs_Value as JitsiVideobridge_XmppConfigs_Value,
    )
    from pynix_os.services.jitterentropy_rngd import JitterentropyRngd as JitterentropyRngd
    from pynix_os.services.jmusicbot import Jmusicbot as Jmusicbot
    from pynix_os.services.jotta_cli import JottaCli as JottaCli
    from pynix_os.services.journalbeat import Journalbeat as Journalbeat
    from pynix_os.services.journald import (
        Journald as Journald,
        Journald_Gateway as Journald_Gateway,
        Journald_Remote as Journald_Remote,
        Journald_Remote_Settings as Journald_Remote_Settings,
        Journald_Settings as Journald_Settings,
        Journald_Settings_Journal as Journald_Settings_Journal,
        Journald_Upload as Journald_Upload,
        Journald_Upload_Settings as Journald_Upload_Settings,
    )
    from pynix_os.services.journaldriver import Journaldriver as Journaldriver
    from pynix_os.services.journalwatch import (
        Journalwatch as Journalwatch,
        Journalwatch_FilterBlocks_Item as Journalwatch_FilterBlocks_Item,
    )
    from pynix_os.services.joycond import Joycond as Joycond
    from pynix_os.services.jupyter import Jupyter as Jupyter, Jupyter_Kernels_Value as Jupyter_Kernels_Value
    from pynix_os.services.jupyterhub import (
        Jupyterhub as Jupyterhub,
        Jupyterhub_Kernels_Value as Jupyterhub_Kernels_Value,
    )
    from pynix_os.services.k3s import (
        K3s as K3s,
        K3s_AutoDeployCharts_Value as K3s_AutoDeployCharts_Value,
        K3s_GracefulNodeShutdown as K3s_GracefulNodeShutdown,
        K3s_Manifests_Value as K3s_Manifests_Value,
    )
    from pynix_os.services.kanata import Kanata as Kanata, Kanata_Keyboards_Value as Kanata_Keyboards_Value
    from pynix_os.services.kanboard import (
        Kanboard as Kanboard,
        Kanboard_Nginx as Kanboard_Nginx,
        Kanboard_Nginx_Listen_Item as Kanboard_Nginx_Listen_Item,
        Kanboard_Nginx_Locations_Value as Kanboard_Nginx_Locations_Value,
        Kanboard_Phpfpm as Kanboard_Phpfpm,
    )
    from pynix_os.services.kanidm import (
        Kanidm as Kanidm,
        Kanidm_Client as Kanidm_Client,
        Kanidm_Client_Settings as Kanidm_Client_Settings,
        Kanidm_Provision as Kanidm_Provision,
        Kanidm_Provision_Groups_Value as Kanidm_Provision_Groups_Value,
        Kanidm_Provision_Persons_Value as Kanidm_Provision_Persons_Value,
        Kanidm_Provision_Systems as Kanidm_Provision_Systems,
        Kanidm_Provision_Systems_Oauth2_Value as Kanidm_Provision_Systems_Oauth2_Value,
        Kanidm_Provision_Systems_Oauth2_Value_ClaimMaps_Value as Kanidm_Provision_Systems_Oauth2_Value_ClaimMaps_Value,
        Kanidm_Server as Kanidm_Server,
        Kanidm_Server_EntryManagement as Kanidm_Server_EntryManagement,
        Kanidm_Server_Settings as Kanidm_Server_Settings,
        Kanidm_Unix as Kanidm_Unix,
        Kanidm_Unix_Settings as Kanidm_Unix_Settings,
    )
    from pynix_os.services.kanshi import Kanshi as Kanshi, Kanshi_Systemd as Kanshi_Systemd
    from pynix_os.services.kapacitor import (
        Kapacitor as Kapacitor,
        Kapacitor_Alerta as Kapacitor_Alerta,
        Kapacitor_DefaultDatabase as Kapacitor_DefaultDatabase,
    )
    from pynix_os.services.kapla import Kapla as Kapla, Kapla_ErisSocket as Kapla_ErisSocket
    from pynix_os.services.karakeep import (
        Karakeep as Karakeep,
        Karakeep_Browser as Karakeep_Browser,
        Karakeep_Meilisearch as Karakeep_Meilisearch,
    )
    from pynix_os.services.karma import Karma as Karma, Karma_Settings as Karma_Settings
    from pynix_os.services.kasmweb import Kasmweb as Kasmweb, Kasmweb_Postgres as Kasmweb_Postgres
    from pynix_os.services.kavita import Kavita as Kavita, Kavita_Settings as Kavita_Settings
    from pynix_os.services.kbfs import Kbfs as Kbfs
    from pynix_os.services.kea import (
        Kea as Kea,
        Kea_Dhcp4 as Kea_Dhcp4,
        Kea_Dhcp6 as Kea_Dhcp6,
        Kea_DhcpDdns as Kea_DhcpDdns,
    )
    from pynix_os.services.keepalived import (
        Keepalived as Keepalived,
        Keepalived_Snmp as Keepalived_Snmp,
        Keepalived_VrrpInstances_Value as Keepalived_VrrpInstances_Value,
        Keepalived_VrrpInstances_Value_VirtualIps_Item as Keepalived_VrrpInstances_Value_VirtualIps_Item,
        Keepalived_VrrpScripts_Value as Keepalived_VrrpScripts_Value,
    )
    from pynix_os.services.kener import Kener as Kener, Kener_Redis as Kener_Redis, Kener_Settings as Kener_Settings
    from pynix_os.services.kerberos_server import (
        KerberosServer as KerberosServer,
        KerberosServer_Settings as KerberosServer_Settings,
        KerberosServer_Settings_Realms_Value as KerberosServer_Settings_Realms_Value,
        KerberosServer_Settings_Realms_Value_Acl_Item as KerberosServer_Settings_Realms_Value_Acl_Item,
    )
    from pynix_os.services.keter import (
        Keter as Keter,
        Keter_Bundle as Keter_Bundle,
        Keter_GlobalKeterConfig as Keter_GlobalKeterConfig,
        Keter_GlobalKeterConfig_Listeners_Item as Keter_GlobalKeterConfig_Listeners_Item,
    )
    from pynix_os.services.keybase import Keybase as Keybase
    from pynix_os.services.keycloak import Keycloak as Keycloak, Keycloak_Settings as Keycloak_Settings
    from pynix_os.services.keyd import Keyd as Keyd, Keyd_Keyboards_Value as Keyd_Keyboards_Value
    from pynix_os.services.kimai import Kimai as Kimai, Kimai_Sites_Value as Kimai_Sites_Value
    from pynix_os.services.kismet import Kismet as Kismet, Kismet_Httpd as Kismet_Httpd
    from pynix_os.services.kiwix_serve import KiwixServe as KiwixServe
    from pynix_os.services.klipper import Klipper as Klipper, Klipper_Firmwares_Value as Klipper_Firmwares_Value
    from pynix_os.services.kmonad import Kmonad as Kmonad, Kmonad_Keyboards_Value as Kmonad_Keyboards_Value
    from pynix_os.services.kmscon import Kmscon as Kmscon, Kmscon_Config as Kmscon_Config
    from pynix_os.services.knot import Knot as Knot
    from pynix_os.services.knot_resolver import (
        KnotResolver as KnotResolver,
        KnotResolver_Settings as KnotResolver_Settings,
        KnotResolver_Settings_NetworkListen_Item as KnotResolver_Settings_NetworkListen_Item,
    )
    from pynix_os.services.koito import Koito as Koito, Koito_Environment as Koito_Environment
    from pynix_os.services.komga import Komga as Komga, Komga_Settings as Komga_Settings
    from pynix_os.services.komodo_periphery import (
        KomodoPeriphery as KomodoPeriphery,
        KomodoPeriphery_Auth as KomodoPeriphery_Auth,
        KomodoPeriphery_Inbound as KomodoPeriphery_Inbound,
        KomodoPeriphery_Inbound_Ssl as KomodoPeriphery_Inbound_Ssl,
        KomodoPeriphery_Logging as KomodoPeriphery_Logging,
        KomodoPeriphery_Outbound as KomodoPeriphery_Outbound,
    )
    from pynix_os.services.kresd import Kresd as Kresd
    from pynix_os.services.krill import Krill as Krill, Krill_Settings as Krill_Settings
    from pynix_os.services.kthxbye import Kthxbye as Kthxbye, Kthxbye_Alertmanager as Kthxbye_Alertmanager
    from pynix_os.services.kubernetes import (
        Kubernetes as Kubernetes,
        Kubernetes_AddonManager as Kubernetes_AddonManager,
        Kubernetes_Addons as Kubernetes_Addons,
        Kubernetes_Addons_Dns as Kubernetes_Addons_Dns,
        Kubernetes_Apiserver as Kubernetes_Apiserver,
        Kubernetes_Apiserver_Etcd as Kubernetes_Apiserver_Etcd,
        Kubernetes_ControllerManager as Kubernetes_ControllerManager,
        Kubernetes_ControllerManager_Kubeconfig as Kubernetes_ControllerManager_Kubeconfig,
        Kubernetes_Flannel as Kubernetes_Flannel,
        Kubernetes_Kubeconfig as Kubernetes_Kubeconfig,
        Kubernetes_Kubelet as Kubernetes_Kubelet,
        Kubernetes_Kubelet_Cni as Kubernetes_Kubelet_Cni,
        Kubernetes_Kubelet_Healthz as Kubernetes_Kubelet_Healthz,
        Kubernetes_Kubelet_Kubeconfig as Kubernetes_Kubelet_Kubeconfig,
        Kubernetes_Kubelet_Taints_Value as Kubernetes_Kubelet_Taints_Value,
        Kubernetes_Pki as Kubernetes_Pki,
        Kubernetes_Proxy as Kubernetes_Proxy,
        Kubernetes_Proxy_Kubeconfig as Kubernetes_Proxy_Kubeconfig,
        Kubernetes_Scheduler as Kubernetes_Scheduler,
        Kubernetes_Scheduler_Kubeconfig as Kubernetes_Scheduler_Kubeconfig,
    )
    from pynix_os.services.kubo import Kubo as Kubo, Kubo_Settings as Kubo_Settings
    from pynix_os.services.kvrocks import Kvrocks as Kvrocks, Kvrocks_Settings as Kvrocks_Settings
    from pynix_os.services.labgrid import Labgrid as Labgrid, Labgrid_Coordinator as Labgrid_Coordinator
    from pynix_os.services.lact import Lact as Lact, Lact_Settings as Lact_Settings
    from pynix_os.services.lambdabot import Lambdabot as Lambdabot
    from pynix_os.services.languagetool import (
        Languagetool as Languagetool,
        Languagetool_Settings as Languagetool_Settings,
    )
    from pynix_os.services.lanraragi import Lanraragi as Lanraragi, Lanraragi_Redis as Lanraragi_Redis
    from pynix_os.services.lasuite_docs import (
        LasuiteDocs as LasuiteDocs,
        LasuiteDocs_Celery as LasuiteDocs_Celery,
        LasuiteDocs_CollaborationServer as LasuiteDocs_CollaborationServer,
        LasuiteDocs_CollaborationServer_Settings as LasuiteDocs_CollaborationServer_Settings,
        LasuiteDocs_Gunicorn as LasuiteDocs_Gunicorn,
        LasuiteDocs_Postgresql as LasuiteDocs_Postgresql,
        LasuiteDocs_Redis as LasuiteDocs_Redis,
        LasuiteDocs_Settings as LasuiteDocs_Settings,
    )
    from pynix_os.services.lasuite_drive import (
        LasuiteDrive as LasuiteDrive,
        LasuiteDrive_Celery as LasuiteDrive_Celery,
        LasuiteDrive_Gunicorn as LasuiteDrive_Gunicorn,
        LasuiteDrive_Postgresql as LasuiteDrive_Postgresql,
        LasuiteDrive_Redis as LasuiteDrive_Redis,
        LasuiteDrive_Settings as LasuiteDrive_Settings,
    )
    from pynix_os.services.lasuite_meet import (
        LasuiteMeet as LasuiteMeet,
        LasuiteMeet_Celery as LasuiteMeet_Celery,
        LasuiteMeet_Gunicorn as LasuiteMeet_Gunicorn,
        LasuiteMeet_Livekit as LasuiteMeet_Livekit,
        LasuiteMeet_Postgresql as LasuiteMeet_Postgresql,
        LasuiteMeet_Redis as LasuiteMeet_Redis,
        LasuiteMeet_Settings as LasuiteMeet_Settings,
    )
    from pynix_os.services.lauti import Lauti as Lauti
    from pynix_os.services.lavalink import (
        Lavalink as Lavalink,
        Lavalink_ExtraConfig as Lavalink_ExtraConfig,
        Lavalink_Plugins_Item as Lavalink_Plugins_Item,
        Lavalink_Plugins_Item_ExtraConfig as Lavalink_Plugins_Item_ExtraConfig,
    )
    from pynix_os.services.leaps import Leaps as Leaps
    from pynix_os.services.legit import Legit as Legit, Legit_Settings as Legit_Settings
    from pynix_os.services.lemmy import (
        Lemmy as Lemmy,
        Lemmy_Caddy as Lemmy_Caddy,
        Lemmy_Database as Lemmy_Database,
        Lemmy_Nginx as Lemmy_Nginx,
        Lemmy_Server as Lemmy_Server,
        Lemmy_Settings as Lemmy_Settings,
        Lemmy_Ui as Lemmy_Ui,
    )
    from pynix_os.services.libeufin import (
        Libeufin as Libeufin,
        Libeufin_Bank as Libeufin_Bank,
        Libeufin_Bank_Settings as Libeufin_Bank_Settings,
        Libeufin_Nexus as Libeufin_Nexus,
        Libeufin_Nexus_Settings as Libeufin_Nexus_Settings,
        Libeufin_Settings as Libeufin_Settings,
    )
    from pynix_os.services.libinput import (
        Libinput as Libinput,
        Libinput_Mouse as Libinput_Mouse,
        Libinput_Touchpad as Libinput_Touchpad,
    )
    from pynix_os.services.librechat import (
        Librechat as Librechat,
        Librechat_Env as Librechat_Env,
        Librechat_Meilisearch as Librechat_Meilisearch,
        Librechat_Settings as Librechat_Settings,
    )
    from pynix_os.services.librenms import (
        Librenms as Librenms,
        Librenms_Database as Librenms_Database,
        Librenms_DistributedPoller as Librenms_DistributedPoller,
        Librenms_Nginx as Librenms_Nginx,
        Librenms_Nginx_Listen_Item as Librenms_Nginx_Listen_Item,
        Librenms_Nginx_Locations_Value as Librenms_Nginx_Locations_Value,
        Librenms_Settings as Librenms_Settings,
    )
    from pynix_os.services.librespeed import (
        Librespeed as Librespeed,
        Librespeed_Frontend as Librespeed_Frontend,
        Librespeed_Frontend_Servers_Item as Librespeed_Frontend_Servers_Item,
        Librespeed_Frontend_Settings as Librespeed_Frontend_Settings,
    )
    from pynix_os.services.libreswan import Libreswan as Libreswan
    from pynix_os.services.libretranslate import Libretranslate as Libretranslate
    from pynix_os.services.libvirtd import (
        Libvirtd_AutoSnapshot as Libvirtd_AutoSnapshot,
        Libvirtd_AutoSnapshot_Vms_Item_Or as Libvirtd_AutoSnapshot_Vms_Item_Or,
        Libvirtd as Services_Libvirtd,
    )
    from pynix_os.services.lidarr import Lidarr as Lidarr, Lidarr_Settings as Lidarr_Settings
    from pynix_os.services.lifecycled import (
        Lifecycled as Lifecycled,
        Lifecycled_QueueCleaner as Lifecycled_QueueCleaner,
    )
    from pynix_os.services.lighthouse import (
        Lighthouse as Lighthouse,
        Lighthouse_Beacon as Lighthouse_Beacon,
        Lighthouse_Validator as Lighthouse_Validator,
    )
    from pynix_os.services.lighttpd import (
        Lighttpd as Lighttpd,
        Lighttpd_Cgit as Lighttpd_Cgit,
        Lighttpd_Collectd as Lighttpd_Collectd,
        Lighttpd_Gitweb as Lighttpd_Gitweb,
    )
    from pynix_os.services.limesurvey import (
        Limesurvey as Limesurvey,
        Limesurvey_Httpd as Limesurvey_Httpd,
        Limesurvey_Httpd_VirtualHost as Limesurvey_Httpd_VirtualHost,
        Limesurvey_Httpd_VirtualHost_Listen_Item as Limesurvey_Httpd_VirtualHost_Listen_Item,
        Limesurvey_Httpd_VirtualHost_Locations_Value as Limesurvey_Httpd_VirtualHost_Locations_Value,
        Limesurvey_Nginx as Limesurvey_Nginx,
        Limesurvey_Nginx_VirtualHost as Limesurvey_Nginx_VirtualHost,
        Limesurvey_Nginx_VirtualHost_Listen_Item as Limesurvey_Nginx_VirtualHost_Listen_Item,
        Limesurvey_Nginx_VirtualHost_Locations_Value as Limesurvey_Nginx_VirtualHost_Locations_Value,
    )
    from pynix_os.services.linkding import Linkding as Linkding
    from pynix_os.services.linkwarden import Linkwarden as Linkwarden, Linkwarden_Database as Linkwarden_Database
    from pynix_os.services.linux_enable_ir_emitter import LinuxEnableIrEmitter as LinuxEnableIrEmitter
    from pynix_os.services.linyaps import Linyaps as Linyaps
    from pynix_os.services.liquidsoap import Liquidsoap as Liquidsoap
    from pynix_os.services.lirc import Lirc as Lirc
    from pynix_os.services.listmonk import (
        Listmonk as Listmonk,
        Listmonk_Database as Listmonk_Database,
        Listmonk_Database_Settings as Listmonk_Database_Settings,
        Listmonk_Database_Settings_BounceMailboxes_Item as Listmonk_Database_Settings_BounceMailboxes_Item,
        Listmonk_Database_Settings_Smtp_Item as Listmonk_Database_Settings_Smtp_Item,
        Listmonk_Settings as Listmonk_Settings,
    )
    from pynix_os.services.litellm import Litellm as Litellm, Litellm_Settings as Litellm_Settings
    from pynix_os.services.litestream import Litestream as Litestream
    from pynix_os.services.livebook import Livebook as Livebook
    from pynix_os.services.livekit import (
        Livekit as Livekit,
        Livekit_Ingress as Livekit_Ingress,
        Livekit_Ingress_OpenFirewall as Livekit_Ingress_OpenFirewall,
        Livekit_Ingress_Settings as Livekit_Ingress_Settings,
        Livekit_Redis as Livekit_Redis,
        Livekit_Settings as Livekit_Settings,
    )
    from pynix_os.services.lk_jwt_service import LkJwtService as LkJwtService
    from pynix_os.services.llama_cpp import LlamaCpp as LlamaCpp, LlamaCpp_Settings as LlamaCpp_Settings
    from pynix_os.services.llama_swap import (
        LlamaSwap as LlamaSwap,
        LlamaSwap_Settings as LlamaSwap_Settings,
        LlamaSwap_Tls as LlamaSwap_Tls,
    )
    from pynix_os.services.lldap import Lldap as Lldap, Lldap_Settings as Lldap_Settings
    from pynix_os.services.lldpd import Lldpd as Lldpd
    from pynix_os.services.local_content_share import LocalContentShare as LocalContentShare
    from pynix_os.services.localtimed import Localtimed as Localtimed
    from pynix_os.services.locate import Locate as Locate
    from pynix_os.services.logcheck import (
        Logcheck as Logcheck,
        Logcheck_IgnoreCron_Value as Logcheck_IgnoreCron_Value,
        Logcheck_Ignore_Value as Logcheck_Ignore_Value,
    )
    from pynix_os.services.logind import (
        Logind as Logind,
        Logind_Settings as Logind_Settings,
        Logind_Settings_Login as Logind_Settings_Login,
    )
    from pynix_os.services.logiops import Logiops as Logiops
    from pynix_os.services.logkeys import Logkeys as Logkeys
    from pynix_os.services.logmein_hamachi import LogmeinHamachi as LogmeinHamachi
    from pynix_os.services.logrotate import Logrotate as Logrotate, Logrotate_Settings_Value as Logrotate_Settings_Value
    from pynix_os.services.logstash import Logstash as Logstash
    from pynix_os.services.loki import Loki as Loki
    from pynix_os.services.lokinet import Lokinet as Lokinet, Lokinet_Settings as Lokinet_Settings
    from pynix_os.services.longview import Longview as Longview
    from pynix_os.services.lorri import Lorri as Lorri
    from pynix_os.services.lubelogger import Lubelogger as Lubelogger
    from pynix_os.services.lvm import (
        Lvm as Lvm,
        Lvm_Boot as Lvm_Boot,
        Lvm_Boot_Thin as Lvm_Boot_Thin,
        Lvm_Boot_Vdo as Lvm_Boot_Vdo,
        Lvm_Dmeventd as Lvm_Dmeventd,
        Lvm_ResizeHelper as Lvm_ResizeHelper,
    )
    from pynix_os.services.lxd_image_server import (
        LxdImageServer as LxdImageServer,
        LxdImageServer_Nginx as LxdImageServer_Nginx,
    )
    from pynix_os.services.lxmd import Lxmd as Lxmd, Lxmd_HealthCheck as Lxmd_HealthCheck, Lxmd_Rnsd as Lxmd_Rnsd
    from pynix_os.services.mackerel_agent import (
        MackerelAgent as MackerelAgent,
        MackerelAgent_Settings as MackerelAgent_Settings,
    )
    from pynix_os.services.maddy import (
        Maddy as Maddy,
        Maddy_EnsureCredentials_Value as Maddy_EnsureCredentials_Value,
        Maddy_Tls as Maddy_Tls,
        Maddy_Tls_Certificates_Item as Maddy_Tls_Certificates_Item,
    )
    from pynix_os.services.magic_wormhole_mailbox_server import MagicWormholeMailboxServer as MagicWormholeMailboxServer
    from pynix_os.services.magnetico import (
        Magnetico as Magnetico,
        Magnetico_Crawler as Magnetico_Crawler,
        Magnetico_Web as Magnetico_Web,
    )
    from pynix_os.services.mail import Mail as Mail, Mail_SendmailSetuidWrapper as Mail_SendmailSetuidWrapper
    from pynix_os.services.mailcatcher import (
        Mailcatcher as Mailcatcher,
        Mailcatcher_Http as Mailcatcher_Http,
        Mailcatcher_Smtp as Mailcatcher_Smtp,
    )
    from pynix_os.services.mailhog import Mailhog as Mailhog
    from pynix_os.services.mailman import (
        Mailman as Mailman,
        Mailman_Hyperkitty as Mailman_Hyperkitty,
        Mailman_Ldap as Mailman_Ldap,
        Mailman_Ldap_AttrMap as Mailman_Ldap_AttrMap,
        Mailman_Ldap_UserSearch as Mailman_Ldap_UserSearch,
        Mailman_Serve as Mailman_Serve,
    )
    from pynix_os.services.mailpit import Mailpit as Mailpit, Mailpit_Instances_Value as Mailpit_Instances_Value
    from pynix_os.services.mainsail import (
        Mainsail as Mainsail,
        Mainsail_Nginx as Mainsail_Nginx,
        Mainsail_Nginx_Listen_Item as Mainsail_Nginx_Listen_Item,
        Mainsail_Nginx_Locations_Value as Mainsail_Nginx_Locations_Value,
    )
    from pynix_os.services.malcontent import Malcontent as Malcontent
    from pynix_os.services.mame import Mame as Mame
    from pynix_os.services.manticore import Manticore as Manticore, Manticore_Settings as Manticore_Settings
    from pynix_os.services.marytts import Marytts as Marytts, Marytts_Settings as Marytts_Settings
    from pynix_os.services.mastodon import (
        Mastodon as Mastodon,
        Mastodon_Database as Mastodon_Database,
        Mastodon_Elasticsearch as Mastodon_Elasticsearch,
        Mastodon_MediaAutoRemove as Mastodon_MediaAutoRemove,
        Mastodon_Redis as Mastodon_Redis,
        Mastodon_SidekiqProcesses_Value as Mastodon_SidekiqProcesses_Value,
        Mastodon_Smtp as Mastodon_Smtp,
    )
    from pynix_os.services.matomo import (
        Matomo as Matomo,
        Matomo_Nginx as Matomo_Nginx,
        Matomo_Nginx_Listen_Item as Matomo_Nginx_Listen_Item,
        Matomo_Nginx_Locations_Value as Matomo_Nginx_Locations_Value,
    )
    from pynix_os.services.matrix_alertmanager import (
        MatrixAlertmanager as MatrixAlertmanager,
        MatrixAlertmanager_MatrixRooms_Item as MatrixAlertmanager_MatrixRooms_Item,
    )
    from pynix_os.services.matrix_appservice_irc import (
        MatrixAppserviceIrc as MatrixAppserviceIrc,
        MatrixAppserviceIrc_Settings as MatrixAppserviceIrc_Settings,
        MatrixAppserviceIrc_Settings_Database as MatrixAppserviceIrc_Settings_Database,
        MatrixAppserviceIrc_Settings_Homeserver as MatrixAppserviceIrc_Settings_Homeserver,
        MatrixAppserviceIrc_Settings_IrcService as MatrixAppserviceIrc_Settings_IrcService,
        MatrixAppserviceIrc_Settings_IrcService_Servers as MatrixAppserviceIrc_Settings_IrcService_Servers,
    )
    from pynix_os.services.matrix_authentication_service import (
        MatrixAuthenticationService as MatrixAuthenticationService,
        MatrixAuthenticationService_Settings as MatrixAuthenticationService_Settings,
        MatrixAuthenticationService_Settings_HttpListeners_Item as MatrixAuthenticationService_Settings_HttpListeners_Item,
        MatrixAuthenticationService_Settings_HttpListeners_Item_Binds_Item as MatrixAuthenticationService_Settings_HttpListeners_Item_Binds_Item,
        MatrixAuthenticationService_Settings_HttpListeners_Item_Resources_Item as MatrixAuthenticationService_Settings_HttpListeners_Item_Resources_Item,
        MatrixAuthenticationService_Settings_PasswordsSchemes_Item as MatrixAuthenticationService_Settings_PasswordsSchemes_Item,
        MatrixAuthenticationService_Settings_UpstreamOauth2Providers_Item as MatrixAuthenticationService_Settings_UpstreamOauth2Providers_Item,
    )
    from pynix_os.services.matrix_conduit import (
        MatrixConduit as MatrixConduit,
        MatrixConduit_Settings as MatrixConduit_Settings,
    )
    from pynix_os.services.matrix_continuwuity import (
        MatrixContinuwuity as MatrixContinuwuity,
        MatrixContinuwuity_Admin as MatrixContinuwuity_Admin,
        MatrixContinuwuity_Settings as MatrixContinuwuity_Settings,
    )
    from pynix_os.services.matrix_hookshot import (
        MatrixHookshot as MatrixHookshot,
        MatrixHookshot_Settings as MatrixHookshot_Settings,
    )
    from pynix_os.services.matrix_synapse import (
        MatrixSynapse as MatrixSynapse,
        MatrixSynapse_Settings as MatrixSynapse_Settings,
        MatrixSynapse_Settings_Listeners_Item as MatrixSynapse_Settings_Listeners_Item,
        MatrixSynapse_Settings_Listeners_Item_Resources_Item as MatrixSynapse_Settings_Listeners_Item_Resources_Item,
        MatrixSynapse_Settings_Redis as MatrixSynapse_Settings_Redis,
        MatrixSynapse_Settings_TrustedKeyServers_Item as MatrixSynapse_Settings_TrustedKeyServers_Item,
        MatrixSynapse_Workers_Value as MatrixSynapse_Workers_Value,
    )
    from pynix_os.services.matrix_tuwunel import (
        MatrixTuwunel as MatrixTuwunel,
        MatrixTuwunel_Settings as MatrixTuwunel_Settings,
    )
    from pynix_os.services.matter_server import MatterServer as MatterServer
    from pynix_os.services.matterbridge import Matterbridge as Matterbridge
    from pynix_os.services.matterjs_server import MatterjsServer as MatterjsServer
    from pynix_os.services.mattermost import (
        Mattermost as Mattermost,
        Mattermost_Database as Mattermost_Database,
        Mattermost_Matterircd as Mattermost_Matterircd,
        Mattermost_Socket as Mattermost_Socket,
        Mattermost_Telemetry as Mattermost_Telemetry,
    )
    from pynix_os.services.maubot import (
        Maubot as Maubot,
        Maubot_Settings as Maubot_Settings,
        Maubot_Settings_Homeservers_Value as Maubot_Settings_Homeservers_Value,
        Maubot_Settings_PluginDatabases as Maubot_Settings_PluginDatabases,
        Maubot_Settings_PluginDirectories as Maubot_Settings_PluginDirectories,
        Maubot_Settings_Server as Maubot_Settings_Server,
    )
    from pynix_os.services.mautrix_discord import MautrixDiscord as MautrixDiscord
    from pynix_os.services.mautrix_meta import (
        MautrixMeta as MautrixMeta,
        MautrixMeta_Instances_Value as MautrixMeta_Instances_Value,
    )
    from pynix_os.services.mautrix_signal import MautrixSignal as MautrixSignal
    from pynix_os.services.mautrix_telegram import MautrixTelegram as MautrixTelegram
    from pynix_os.services.mautrix_whatsapp import MautrixWhatsapp as MautrixWhatsapp
    from pynix_os.services.mbpfan import Mbpfan as Mbpfan, Mbpfan_Settings as Mbpfan_Settings
    from pynix_os.services.mchprs import (
        Mchprs as Mchprs,
        Mchprs_Settings as Mchprs_Settings,
        Mchprs_Whitelist as Mchprs_Whitelist,
    )
    from pynix_os.services.mealie import Mealie as Mealie, Mealie_Database as Mealie_Database
    from pynix_os.services.mediagoblin import (
        Mediagoblin as Mediagoblin,
        Mediagoblin_Paste as Mediagoblin_Paste,
        Mediagoblin_Paste_Settings as Mediagoblin_Paste_Settings,
        Mediagoblin_Settings as Mediagoblin_Settings,
    )
    from pynix_os.services.mediamtx import Mediamtx as Mediamtx
    from pynix_os.services.mediatomb import (
        Mediatomb as Mediatomb,
        Mediatomb_MediaDirectories_Item as Mediatomb_MediaDirectories_Item,
    )
    from pynix_os.services.mediawiki import (
        Mediawiki as Mediawiki,
        Mediawiki_Httpd as Mediawiki_Httpd,
        Mediawiki_Httpd_VirtualHost as Mediawiki_Httpd_VirtualHost,
        Mediawiki_Httpd_VirtualHost_Listen_Item as Mediawiki_Httpd_VirtualHost_Listen_Item,
        Mediawiki_Httpd_VirtualHost_Locations_Value as Mediawiki_Httpd_VirtualHost_Locations_Value,
        Mediawiki_Nginx as Mediawiki_Nginx,
    )
    from pynix_os.services.meilisearch import Meilisearch as Meilisearch, Meilisearch_Settings as Meilisearch_Settings
    from pynix_os.services.memcached import Memcached as Memcached
    from pynix_os.services.meme_bingo_web import MemeBingoWeb as MemeBingoWeb
    from pynix_os.services.memos import Memos as Memos
    from pynix_os.services.merecat import Merecat as Merecat
    from pynix_os.services.meshcentral import Meshcentral as Meshcentral, Meshcentral_Settings as Meshcentral_Settings
    from pynix_os.services.meshtasticd import Meshtasticd as Meshtasticd
    from pynix_os.services.metabase import (
        Metabase as Metabase,
        Metabase_Listen as Metabase_Listen,
        Metabase_Ssl as Metabase_Ssl,
    )
    from pynix_os.services.metricbeat import (
        Metricbeat as Metricbeat,
        Metricbeat_Modules_Value as Metricbeat_Modules_Value,
        Metricbeat_Settings as Metricbeat_Settings,
    )
    from pynix_os.services.microbin import Microbin as Microbin, Microbin_Settings as Microbin_Settings
    from pynix_os.services.microsocks import Microsocks as Microsocks
    from pynix_os.services.mighttpd2 import Mighttpd2 as Mighttpd2
    from pynix_os.services.mihomo import Mihomo as Mihomo
    from pynix_os.services.mimir import Mimir as Mimir
    from pynix_os.services.minecraft_server import MinecraftServer as MinecraftServer
    from pynix_os.services.minetest_server import MinetestServer as MinetestServer
    from pynix_os.services.minidlna import Minidlna as Minidlna, Minidlna_Settings as Minidlna_Settings
    from pynix_os.services.miniflux import Miniflux as Miniflux, Miniflux_Config as Miniflux_Config
    from pynix_os.services.minio import Minio as Minio
    from pynix_os.services.miniupnpd import Miniupnpd as Miniupnpd
    from pynix_os.services.mirakurun import Mirakurun as Mirakurun
    from pynix_os.services.miredo import Miredo as Miredo
    from pynix_os.services.misskey import (
        Misskey as Misskey,
        Misskey_Database as Misskey_Database,
        Misskey_Meilisearch as Misskey_Meilisearch,
        Misskey_Redis as Misskey_Redis,
        Misskey_ReverseProxy as Misskey_ReverseProxy,
        Misskey_Settings as Misskey_Settings,
        Misskey_Settings_Db as Misskey_Settings_Db,
        Misskey_Settings_Meilisearch as Misskey_Settings_Meilisearch,
        Misskey_Settings_Redis as Misskey_Settings_Redis,
    )
    from pynix_os.services.mjolnir import (
        Mjolnir as Mjolnir,
        Mjolnir_Encryption as Mjolnir_Encryption,
        Mjolnir_Pantalaimon as Mjolnir_Pantalaimon,
        Mjolnir_Pantalaimon_Options as Mjolnir_Pantalaimon_Options,
    )
    from pynix_os.services.mjpg_streamer import MjpgStreamer as MjpgStreamer
    from pynix_os.services.mlmmj import Mlmmj as Mlmmj
    from pynix_os.services.mmsd import Mmsd as Mmsd
    from pynix_os.services.mobilizon import (
        Mobilizon as Mobilizon,
        Mobilizon_Nginx as Mobilizon_Nginx,
        Mobilizon_Settings as Mobilizon_Settings,
    )
    from pynix_os.services.molly_brown import MollyBrown as MollyBrown
    from pynix_os.services.mollysocket import Mollysocket as Mollysocket, Mollysocket_Settings as Mollysocket_Settings
    from pynix_os.services.monado import Monado as Monado
    from pynix_os.services.monero import (
        Monero as Monero,
        Monero_Limits as Monero_Limits,
        Monero_Mining as Monero_Mining,
        Monero_Rpc as Monero_Rpc,
    )
    from pynix_os.services.monetdb import Monetdb as Monetdb
    from pynix_os.services.mongodb import Mongodb as Mongodb
    from pynix_os.services.monica import (
        Monica as Monica,
        Monica_Config_Value_Or as Monica_Config_Value_Or,
        Monica_Database as Monica_Database,
        Monica_Mail as Monica_Mail,
        Monica_Nginx as Monica_Nginx,
        Monica_Nginx_Listen_Item as Monica_Nginx_Listen_Item,
        Monica_Nginx_Locations_Value as Monica_Nginx_Locations_Value,
    )
    from pynix_os.services.monit import Monit as Monit
    from pynix_os.services.moodle import (
        Moodle as Moodle,
        Moodle_VirtualHost as Moodle_VirtualHost,
        Moodle_VirtualHost_Listen_Item as Moodle_VirtualHost_Listen_Item,
        Moodle_VirtualHost_Locations_Value as Moodle_VirtualHost_Locations_Value,
    )
    from pynix_os.services.moonraker import Moonraker as Moonraker, Moonraker_Analysis as Moonraker_Analysis
    from pynix_os.services.moonshine import Moonshine as Moonshine
    from pynix_os.services.moosefs import (
        Moosefs as Moosefs,
        Moosefs_Cgiserver as Moosefs_Cgiserver,
        Moosefs_Cgiserver_Settings as Moosefs_Cgiserver_Settings,
        Moosefs_Chunkserver as Moosefs_Chunkserver,
        Moosefs_Chunkserver_Settings as Moosefs_Chunkserver_Settings,
        Moosefs_Client as Moosefs_Client,
        Moosefs_Master as Moosefs_Master,
        Moosefs_Master_Settings as Moosefs_Master_Settings,
        Moosefs_Metalogger as Moosefs_Metalogger,
        Moosefs_Metalogger_Settings as Moosefs_Metalogger_Settings,
    )
    from pynix_os.services.mopidy import Mopidy as Mopidy
    from pynix_os.services.mosquitto import (
        Mosquitto as Mosquitto,
        Mosquitto_Bridges_Value as Mosquitto_Bridges_Value,
        Mosquitto_Bridges_Value_Addresses_Item as Mosquitto_Bridges_Value_Addresses_Item,
        Mosquitto_Bridges_Value_Settings as Mosquitto_Bridges_Value_Settings,
        Mosquitto_Listeners_Item as Mosquitto_Listeners_Item,
        Mosquitto_Listeners_Item_AuthPlugins_Item as Mosquitto_Listeners_Item_AuthPlugins_Item,
        Mosquitto_Listeners_Item_Settings as Mosquitto_Listeners_Item_Settings,
        Mosquitto_Listeners_Item_Users_Value as Mosquitto_Listeners_Item_Users_Value,
        Mosquitto_Settings as Mosquitto_Settings,
    )
    from pynix_os.services.motioneye import Motioneye as Motioneye, Motioneye_Packages as Motioneye_Packages
    from pynix_os.services.movim import (
        Movim as Movim,
        Movim_H2o as Movim_H2o,
        Movim_H2o_Acme as Movim_H2o_Acme,
        Movim_H2o_Http as Movim_H2o_Http,
        Movim_H2o_Tls as Movim_H2o_Tls,
        Movim_H2o_Tls_Identity_Item as Movim_H2o_Tls_Identity_Item,
        Movim_MinifyStaticFiles_Or as Movim_MinifyStaticFiles_Or,
        Movim_MinifyStaticFiles_Or_Script as Movim_MinifyStaticFiles_Or_Script,
        Movim_MinifyStaticFiles_Or_Style as Movim_MinifyStaticFiles_Or_Style,
        Movim_MinifyStaticFiles_Or_Svg as Movim_MinifyStaticFiles_Or_Svg,
        Movim_Nginx as Movim_Nginx,
        Movim_Nginx_Listen_Item as Movim_Nginx_Listen_Item,
        Movim_Nginx_Locations_Value as Movim_Nginx_Locations_Value,
        Movim_PodConfig as Movim_PodConfig,
        Movim_PrecompressStaticFiles as Movim_PrecompressStaticFiles,
    )
    from pynix_os.services.mozillavpn import Mozillavpn as Mozillavpn
    from pynix_os.services.mpd import (
        Mpd as Mpd,
        Mpd_Credentials_Item as Mpd_Credentials_Item,
        Mpd_Settings as Mpd_Settings,
    )
    from pynix_os.services.mpdscribble import (
        Mpdscribble as Mpdscribble,
        Mpdscribble_Endpoints_Value as Mpdscribble_Endpoints_Value,
    )
    from pynix_os.services.mptcpd import Mptcpd as Mptcpd
    from pynix_os.services.mqtt2influxdb import (
        Mqtt2influxdb as Mqtt2influxdb,
        Mqtt2influxdb_Influxdb as Mqtt2influxdb_Influxdb,
        Mqtt2influxdb_Mqtt as Mqtt2influxdb_Mqtt,
        Mqtt2influxdb_Points_Item as Mqtt2influxdb_Points_Item,
        Mqtt2influxdb_Points_Item_Fields as Mqtt2influxdb_Points_Item_Fields,
    )
    from pynix_os.services.mstpd import Mstpd as Mstpd
    from pynix_os.services.mtprotoproxy import Mtprotoproxy as Mtprotoproxy
    from pynix_os.services.mtr_exporter import (
        MtrExporter as MtrExporter,
        MtrExporter_Jobs_Item as MtrExporter_Jobs_Item,
    )
    from pynix_os.services.mullvad_vpn import MullvadVpn as MullvadVpn, MullvadVpn_Gui as MullvadVpn_Gui
    from pynix_os.services.multipath import (
        Multipath as Multipath,
        Multipath_Devices_Item as Multipath_Devices_Item,
        Multipath_PathGroups_Item as Multipath_PathGroups_Item,
    )
    from pynix_os.services.munge import Munge as Munge
    from pynix_os.services.munin_cron import MuninCron as MuninCron
    from pynix_os.services.munin_node import MuninNode as MuninNode
    from pynix_os.services.murmur import Murmur as Murmur, Murmur_Tls as Murmur_Tls
    from pynix_os.services.music_assistant import MusicAssistant as MusicAssistant
    from pynix_os.services.mycelium import Mycelium as Mycelium
    from pynix_os.services.mympd import Mympd as Mympd, Mympd_Settings as Mympd_Settings
    from pynix_os.services.mysql import (
        Mysql_EnsureUsers_Item as Mysql_EnsureUsers_Item,
        Mysql_GaleraCluster as Mysql_GaleraCluster,
        Mysql_InitialDatabases_Item as Mysql_InitialDatabases_Item,
        Mysql_Replication as Mysql_Replication,
        Mysql as Services_Mysql,
    )
    from pynix_os.services.mysqlBackup import MysqlBackup as MysqlBackup
    from pynix_os.services.n8n import (
        N8n as N8n,
        N8n_Environment as N8n_Environment,
        N8n_TaskRunners as N8n_TaskRunners,
        N8n_TaskRunners_Environment as N8n_TaskRunners_Environment,
        N8n_TaskRunners_Runners_Value as N8n_TaskRunners_Runners_Value,
    )
    from pynix_os.services.n__3proxy import (
        N3proxy as N3proxy,
        N3proxy_Resolution as N3proxy_Resolution,
        N3proxy_Services_Item as N3proxy_Services_Item,
        N3proxy_Services_Item_Acl_Item as N3proxy_Services_Item_Acl_Item,
    )
    from pynix_os.services.nagios import (
        Nagios as Nagios,
        Nagios_VirtualHost as Nagios_VirtualHost,
        Nagios_VirtualHost_Listen_Item as Nagios_VirtualHost_Listen_Item,
        Nagios_VirtualHost_Locations_Value as Nagios_VirtualHost_Locations_Value,
    )
    from pynix_os.services.namecoind import Namecoind as Namecoind, Namecoind_Rpc as Namecoind_Rpc
    from pynix_os.services.nar_serve import NarServe as NarServe
    from pynix_os.services.nats import Nats as Nats
    from pynix_os.services.navidrome import Navidrome as Navidrome, Navidrome_Settings as Navidrome_Settings
    from pynix_os.services.nbd import (
        Nbd_Server as Nbd_Server,
        Nbd_Server_Exports_Value as Nbd_Server_Exports_Value,
        Nbd as Services_Nbd,
    )
    from pynix_os.services.ncdns import (
        Ncdns as Ncdns,
        Ncdns_Dnssec as Ncdns_Dnssec,
        Ncdns_Dnssec_Keys as Ncdns_Dnssec_Keys,
        Ncdns_Identity as Ncdns_Identity,
    )
    from pynix_os.services.ncps import (
        Ncps as Ncps,
        Ncps_Analytics as Ncps_Analytics,
        Ncps_Analytics_Reporting as Ncps_Analytics_Reporting,
        Ncps_Cache as Ncps_Cache,
        Ncps_Cache_Cdc as Ncps_Cache_Cdc,
        Ncps_Cache_Database as Ncps_Cache_Database,
        Ncps_Cache_Database_Pool as Ncps_Cache_Database_Pool,
        Ncps_Cache_Lock as Ncps_Cache_Lock,
        Ncps_Cache_Lock_Retry as Ncps_Cache_Lock_Retry,
        Ncps_Cache_Lru as Ncps_Cache_Lru,
        Ncps_Cache_Redis as Ncps_Cache_Redis,
        Ncps_Cache_Storage as Ncps_Cache_Storage,
        Ncps_Cache_Storage_S3 as Ncps_Cache_Storage_S3,
        Ncps_Cache_Upstream as Ncps_Cache_Upstream,
        Ncps_OpenTelemetry as Ncps_OpenTelemetry,
        Ncps_Prometheus as Ncps_Prometheus,
        Ncps_Server as Ncps_Server,
    )
    from pynix_os.services.ndppd import (
        Ndppd as Ndppd,
        Ndppd_Proxies_Value as Ndppd_Proxies_Value,
        Ndppd_Proxies_Value_Rules_Value as Ndppd_Proxies_Value_Rules_Value,
    )
    from pynix_os.services.neard import Neard as Neard, Neard_Settings as Neard_Settings
    from pynix_os.services.nebula import Nebula as Nebula, Nebula_Networks_Value as Nebula_Networks_Value
    from pynix_os.services.nebula_lighthouse_service import NebulaLighthouseService as NebulaLighthouseService
    from pynix_os.services.neo4j import (
        Neo4j as Neo4j,
        Neo4j_Bolt as Neo4j_Bolt,
        Neo4j_Directories as Neo4j_Directories,
        Neo4j_Http as Neo4j_Http,
        Neo4j_Https as Neo4j_Https,
        Neo4j_Shell as Neo4j_Shell,
        Neo4j_Ssl as Neo4j_Ssl,
        Neo4j_Ssl_Policies_Value as Neo4j_Ssl_Policies_Value,
    )
    from pynix_os.services.netatalk import Netatalk as Netatalk
    from pynix_os.services.netbird import (
        Netbird as Netbird,
        Netbird_Clients_Value as Netbird_Clients_Value,
        Netbird_Relay as Netbird_Relay,
        Netbird_Relay_Settings as Netbird_Relay_Settings,
        Netbird_Server as Netbird_Server,
        Netbird_Server_Coturn as Netbird_Server_Coturn,
        Netbird_Server_Dashboard as Netbird_Server_Dashboard,
        Netbird_Server_Dashboard_Settings as Netbird_Server_Dashboard_Settings,
        Netbird_Server_Management as Netbird_Server_Management,
        Netbird_Server_Signal as Netbird_Server_Signal,
        Netbird_Tunnels_Value as Netbird_Tunnels_Value,
        Netbird_Ui as Netbird_Ui,
    )
    from pynix_os.services.netbox import (
        Netbox as Netbox,
        Netbox_Gunicorn as Netbox_Gunicorn,
        Netbox_Nginx as Netbox_Nginx,
        Netbox_Postgresql as Netbox_Postgresql,
        Netbox_Redis as Netbox_Redis,
        Netbox_Settings as Netbox_Settings,
    )
    from pynix_os.services.netclient import Netclient as Netclient
    from pynix_os.services.netdata import Netdata as Netdata, Netdata_Python as Netdata_Python
    from pynix_os.services.netfoil import (
        Netfoil as Netfoil,
        Netfoil_Listen as Netfoil_Listen,
        Netfoil_Rules as Netfoil_Rules,
        Netfoil_Rules_Allow as Netfoil_Rules_Allow,
        Netfoil_Rules_Deny as Netfoil_Rules_Deny,
        Netfoil_Rules_Known as Netfoil_Rules_Known,
        Netfoil_Rules_Pin as Netfoil_Rules_Pin,
    )
    from pynix_os.services.networkaudiod import Networkaudiod as Networkaudiod
    from pynix_os.services.networkd_dispatcher import (
        NetworkdDispatcher as NetworkdDispatcher,
        NetworkdDispatcher_Rules_Value as NetworkdDispatcher_Rules_Value,
    )
    from pynix_os.services.networking import (
        Networking_Websockify as Networking_Websockify,
        Networking as Services_Networking,
    )
    from pynix_os.services.newt import Newt as Newt
    from pynix_os.services.nextcloud import (
        Nextcloud as Nextcloud,
        Nextcloud_AutoUpdateApps as Nextcloud_AutoUpdateApps,
        Nextcloud_Caching as Nextcloud_Caching,
        Nextcloud_Cli as Nextcloud_Cli,
        Nextcloud_Config as Nextcloud_Config,
        Nextcloud_Config_Objectstore as Nextcloud_Config_Objectstore,
        Nextcloud_Config_Objectstore_S3 as Nextcloud_Config_Objectstore_S3,
        Nextcloud_Database as Nextcloud_Database,
        Nextcloud_Imaginary as Nextcloud_Imaginary,
        Nextcloud_Nginx as Nextcloud_Nginx,
        Nextcloud_NotifyPush as Nextcloud_NotifyPush,
        Nextcloud_Settings as Nextcloud_Settings,
    )
    from pynix_os.services.nextcloud_spreed_signaling import (
        NextcloudSpreedSignaling as NextcloudSpreedSignaling,
        NextcloudSpreedSignaling_Backends_Value as NextcloudSpreedSignaling_Backends_Value,
        NextcloudSpreedSignaling_Settings as NextcloudSpreedSignaling_Settings,
    )
    from pynix_os.services.nextcloud_whiteboard_server import NextcloudWhiteboardServer as NextcloudWhiteboardServer
    from pynix_os.services.nextdns import Nextdns as Nextdns
    from pynix_os.services.nextjs_ollama_llm_ui import NextjsOllamaLlmUi as NextjsOllamaLlmUi
    from pynix_os.services.nexus import Nexus as Nexus
    from pynix_os.services.nezha import Nezha as Nezha, Nezha_Settings as Nezha_Settings
    from pynix_os.services.nezha_agent import NezhaAgent as NezhaAgent, NezhaAgent_Settings as NezhaAgent_Settings
    from pynix_os.services.nfs import Nfs as Nfs, Nfs_Idmapd as Nfs_Idmapd, Nfs_Server as Nfs_Server
    from pynix_os.services.nghttpx import (
        Nghttpx as Nghttpx,
        Nghttpx_Backends_Item as Nghttpx_Backends_Item,
        Nghttpx_Backends_Item_Params as Nghttpx_Backends_Item_Params,
        Nghttpx_Backends_Item_Server as Nghttpx_Backends_Item_Server,
        Nghttpx_Frontends_Item as Nghttpx_Frontends_Item,
        Nghttpx_Frontends_Item_Params as Nghttpx_Frontends_Item_Params,
        Nghttpx_Tls as Nghttpx_Tls,
    )
    from pynix_os.services.nginx import (
        Nginx as Nginx,
        Nginx_DefaultListen_Item as Nginx_DefaultListen_Item,
        Nginx_Lua as Nginx_Lua,
        Nginx_ProxyCachePath_Value as Nginx_ProxyCachePath_Value,
        Nginx_Resolver as Nginx_Resolver,
        Nginx_Sso as Nginx_Sso,
        Nginx_TailscaleAuth as Nginx_TailscaleAuth,
        Nginx_Upstreams_Value as Nginx_Upstreams_Value,
        Nginx_Upstreams_Value_Servers_Value as Nginx_Upstreams_Value_Servers_Value,
        Nginx_VirtualHosts_Value as Nginx_VirtualHosts_Value,
        Nginx_VirtualHosts_Value_Listen_Item as Nginx_VirtualHosts_Value_Listen_Item,
        Nginx_VirtualHosts_Value_Locations_Value as Nginx_VirtualHosts_Value_Locations_Value,
    )
    from pynix_os.services.ngircd import Ngircd as Ngircd
    from pynix_os.services.nifi import Nifi as Nifi
    from pynix_os.services.nipap import (
        Nipap as Nipap,
        Nipap_AuthBackendSettings as Nipap_AuthBackendSettings,
        Nipap_NipapWww as Nipap_NipapWww,
        Nipap_Nipapd as Nipap_Nipapd,
        Nipap_Nipapd_Database as Nipap_Nipapd_Database,
        Nipap_Settings as Nipap_Settings,
    )
    from pynix_os.services.nitter import (
        Nitter as Nitter,
        Nitter_Cache as Nitter_Cache,
        Nitter_Config as Nitter_Config,
        Nitter_Preferences as Nitter_Preferences,
        Nitter_Server as Nitter_Server,
    )
    from pynix_os.services.nix_serve import NixServe as NixServe
    from pynix_os.services.nixops_dns import NixopsDns as NixopsDns
    from pynix_os.services.nixseparatedebuginfod2 import Nixseparatedebuginfod2 as Nixseparatedebuginfod2
    from pynix_os.services.nmtrust import (
        Nmtrust as Nmtrust,
        Nmtrust_SystemUnits_Value as Nmtrust_SystemUnits_Value,
        Nmtrust_UserUnits_Value_Value as Nmtrust_UserUnits_Value_Value,
    )
    from pynix_os.services.nncp import (
        Nncp_Caller as Nncp_Caller,
        Nncp_Daemon as Nncp_Daemon,
        Nncp_Daemon_SocketActivation as Nncp_Daemon_SocketActivation,
        Nncp as Services_Nncp,
    )
    from pynix_os.services.nntp_proxy import NntpProxy as NntpProxy, NntpProxy_Users_Value as NntpProxy_Users_Value
    from pynix_os.services.node_red import NodeRed as NodeRed
    from pynix_os.services.nohang import Nohang as Nohang
    from pynix_os.services.nomad import Nomad as Nomad
    from pynix_os.services.nominatim import (
        Nominatim as Nominatim,
        Nominatim_Database as Nominatim_Database,
        Nominatim_Ui as Nominatim_Ui,
    )
    from pynix_os.services.nordvpn import Nordvpn as Nordvpn
    from pynix_os.services.nostr_rs_relay import NostrRsRelay as NostrRsRelay
    from pynix_os.services.novacomd import Novacomd as Novacomd
    from pynix_os.services.nscd import Nscd as Nscd
    from pynix_os.services.nsd import (
        Nsd as Nsd,
        Nsd_Keys_Value as Nsd_Keys_Value,
        Nsd_Ratelimit as Nsd_Ratelimit,
        Nsd_RemoteControl as Nsd_RemoteControl,
        Nsd_Zones_Value as Nsd_Zones_Value,
        Nsd_Zones_Value_DnssecPolicyKsk as Nsd_Zones_Value_DnssecPolicyKsk,
    )
    from pynix_os.services.ntfy_sh import (
        NtfySh as NtfySh,
        NtfySh_Nginx as NtfySh_Nginx,
        NtfySh_Settings as NtfySh_Settings,
    )
    from pynix_os.services.ntopng import Ntopng as Ntopng, Ntopng_Redis as Ntopng_Redis
    from pynix_os.services.ntp import Ntp as Ntp
    from pynix_os.services.ntpd_rs import (
        NtpdRs as NtpdRs,
        NtpdRs_Metrics as NtpdRs_Metrics,
        NtpdRs_Settings as NtpdRs_Settings,
    )
    from pynix_os.services.nullidentdmod import Nullidentdmod as Nullidentdmod
    from pynix_os.services.nullmailer import Nullmailer as Nullmailer, Nullmailer_Config as Nullmailer_Config
    from pynix_os.services.nvme_rs import (
        NvmeRs as NvmeRs,
        NvmeRs_Settings as NvmeRs_Settings,
        NvmeRs_Settings_Email as NvmeRs_Settings_Email,
        NvmeRs_Settings_Thresholds as NvmeRs_Settings_Thresholds,
    )
    from pynix_os.services.nzbget import Nzbget as Nzbget
    from pynix_os.services.nzbhydra2 import Nzbhydra2 as Nzbhydra2
    from pynix_os.services.oauth2_proxy import (
        Oauth2Proxy as Oauth2Proxy,
        Oauth2Proxy_Azure as Oauth2Proxy_Azure,
        Oauth2Proxy_Cookie as Oauth2Proxy_Cookie,
        Oauth2Proxy_Email as Oauth2Proxy_Email,
        Oauth2Proxy_Github as Oauth2Proxy_Github,
        Oauth2Proxy_Google as Oauth2Proxy_Google,
        Oauth2Proxy_Htpasswd as Oauth2Proxy_Htpasswd,
        Oauth2Proxy_Nginx as Oauth2Proxy_Nginx,
        Oauth2Proxy_Nginx_VirtualHosts_Value as Oauth2Proxy_Nginx_VirtualHosts_Value,
        Oauth2Proxy_Tls as Oauth2Proxy_Tls,
    )
    from pynix_os.services.ocis import Ocis as Ocis
    from pynix_os.services.ocserv import Ocserv as Ocserv
    from pynix_os.services.ocsinventory_agent import (
        OcsinventoryAgent as OcsinventoryAgent,
        OcsinventoryAgent_Settings as OcsinventoryAgent_Settings,
    )
    from pynix_os.services.octoprint import Octoprint as Octoprint
    from pynix_os.services.odoo import Odoo as Odoo, Odoo_Settings as Odoo_Settings
    from pynix_os.services.offlineimap import Offlineimap as Offlineimap
    from pynix_os.services.ofono import Ofono as Ofono
    from pynix_os.services.oidentd import Oidentd as Oidentd
    from pynix_os.services.oink import Oink as Oink, Oink_Settings as Oink_Settings
    from pynix_os.services.olivetin import Olivetin as Olivetin, Olivetin_Settings as Olivetin_Settings
    from pynix_os.services.ollama import Ollama as Ollama
    from pynix_os.services.ollaya import Ollaya as Ollaya, Ollaya_Settings as Ollaya_Settings
    from pynix_os.services.omada import Omada as Omada
    from pynix_os.services.ombi import Ombi as Ombi
    from pynix_os.services.omnom import Omnom as Omnom, Omnom_Settings as Omnom_Settings
    from pynix_os.services.oncall import (
        Oncall as Oncall,
        Oncall_Database as Oncall_Database,
        Oncall_Settings as Oncall_Settings,
    )
    from pynix_os.services.onedrive import Onedrive as Onedrive
    from pynix_os.services.onlyoffice import Onlyoffice as Onlyoffice
    from pynix_os.services.oo7 import Oo7 as Oo7
    from pynix_os.services.open_web_calendar import (
        OpenWebCalendar as OpenWebCalendar,
        OpenWebCalendar_CalendarSettings as OpenWebCalendar_CalendarSettings,
        OpenWebCalendar_Settings as OpenWebCalendar_Settings,
    )
    from pynix_os.services.open_webui import OpenWebui as OpenWebui
    from pynix_os.services.openafsClient import (
        OpenafsClient as OpenafsClient,
        OpenafsClient_Cache as OpenafsClient_Cache,
        OpenafsClient_CellServDB_Value_Item as OpenafsClient_CellServDB_Value_Item,
        OpenafsClient_Packages as OpenafsClient_Packages,
    )
    from pynix_os.services.openafsServer import (
        OpenafsServer as OpenafsServer,
        OpenafsServer_CellServDB_Value_Item as OpenafsServer_CellServDB_Value_Item,
        OpenafsServer_Roles as OpenafsServer_Roles,
        OpenafsServer_Roles_Backup as OpenafsServer_Roles_Backup,
        OpenafsServer_Roles_Database as OpenafsServer_Roles_Database,
        OpenafsServer_Roles_Fileserver as OpenafsServer_Roles_Fileserver,
    )
    from pynix_os.services.openarena import Openarena as Openarena
    from pynix_os.services.openbao import (
        Openbao as Openbao,
        Openbao_Settings as Openbao_Settings,
        Openbao_Settings_Listener_Value as Openbao_Settings_Listener_Value,
    )
    from pynix_os.services.openbao_agent import (
        OpenbaoAgent as OpenbaoAgent,
        OpenbaoAgent_Instances_Value as OpenbaoAgent_Instances_Value,
        OpenbaoAgent_Instances_Value_Settings as OpenbaoAgent_Instances_Value_Settings,
    )
    from pynix_os.services.opencloud import Opencloud as Opencloud
    from pynix_os.services.opendkim import Opendkim as Opendkim, Opendkim_Settings as Opendkim_Settings
    from pynix_os.services.openiscsi import Openiscsi as Openiscsi
    from pynix_os.services.openldap import (
        Openldap as Openldap,
        Openldap_Settings as Openldap_Settings,
        Openldap_Settings_Children_Value as Openldap_Settings_Children_Value,
    )
    from pynix_os.services.openntpd import Openntpd as Openntpd
    from pynix_os.services.opensearch import Opensearch as Opensearch, Opensearch_Settings as Opensearch_Settings
    from pynix_os.services.opensearch_dashboards import (
        OpensearchDashboards as OpensearchDashboards,
        OpensearchDashboards_Settings as OpensearchDashboards_Settings,
    )
    from pynix_os.services.opensmtpd import Opensmtpd as Opensmtpd
    from pynix_os.services.opensnitch import (
        Opensnitch as Opensnitch,
        Opensnitch_Rules as Opensnitch_Rules,
        Opensnitch_Settings as Opensnitch_Settings,
    )
    from pynix_os.services.openssh import (
        Openssh as Openssh,
        Openssh_KnownHosts_Value as Openssh_KnownHosts_Value,
        Openssh_ListenAddresses_Item as Openssh_ListenAddresses_Item,
        Openssh_Settings as Openssh_Settings,
    )
    from pynix_os.services.opentelemetry_collector import OpentelemetryCollector as OpentelemetryCollector
    from pynix_os.services.openthread_border_router import (
        OpenthreadBorderRouter as OpenthreadBorderRouter,
        OpenthreadBorderRouter_Radio as OpenthreadBorderRouter_Radio,
        OpenthreadBorderRouter_Rest as OpenthreadBorderRouter_Rest,
        OpenthreadBorderRouter_Web as OpenthreadBorderRouter_Web,
    )
    from pynix_os.services.opentracker import Opentracker as Opentracker
    from pynix_os.services.opentsdb import Opentsdb as Opentsdb
    from pynix_os.services.openvpn import (
        Openvpn as Openvpn,
        Openvpn_Servers_Value as Openvpn_Servers_Value,
        Openvpn_Servers_Value_AuthUserPass_Or as Openvpn_Servers_Value_AuthUserPass_Or,
    )
    from pynix_os.services.openvscode_server import OpenvscodeServer as OpenvscodeServer
    from pynix_os.services.openwebrx import Openwebrx as Openwebrx
    from pynix_os.services.opkssh import (
        Opkssh as Opkssh,
        Opkssh_Authorizations_Item as Opkssh_Authorizations_Item,
        Opkssh_Providers_Value as Opkssh_Providers_Value,
    )
    from pynix_os.services.orangefs import (
        Orangefs as Orangefs,
        Orangefs_Client as Orangefs_Client,
        Orangefs_Client_FileSystems_Item as Orangefs_Client_FileSystems_Item,
        Orangefs_Server as Orangefs_Server,
        Orangefs_Server_FileSystems_Value as Orangefs_Server_FileSystems_Value,
    )
    from pynix_os.services.orbit import Orbit as Orbit, Orbit_Desktop as Orbit_Desktop
    from pynix_os.services.orca import Orca as Orca
    from pynix_os.services.orthanc import Orthanc as Orthanc, Orthanc_Settings as Orthanc_Settings
    from pynix_os.services.osquery import Osquery as Osquery, Osquery_Flags as Osquery_Flags
    from pynix_os.services.osrm import Osrm as Osrm
    from pynix_os.services.ostinato import (
        Ostinato as Ostinato,
        Ostinato_PortList as Ostinato_PortList,
        Ostinato_RpcServer as Ostinato_RpcServer,
    )
    from pynix_os.services.outline import (
        Outline as Outline,
        Outline_AzureAuthentication as Outline_AzureAuthentication,
        Outline_DiscordAuthentication as Outline_DiscordAuthentication,
        Outline_GoogleAuthentication as Outline_GoogleAuthentication,
        Outline_OidcAuthentication as Outline_OidcAuthentication,
        Outline_RateLimiter as Outline_RateLimiter,
        Outline_SlackAuthentication as Outline_SlackAuthentication,
        Outline_SlackIntegration as Outline_SlackIntegration,
        Outline_Smtp as Outline_Smtp,
        Outline_Storage as Outline_Storage,
    )
    from pynix_os.services.owamp import Owamp as Owamp
    from pynix_os.services.owncast import Owncast as Owncast
    from pynix_os.services.oxidized import Oxidized as Oxidized
    from pynix_os.services.p2pool import P2pool as P2pool, P2pool_Socks5 as P2pool_Socks5
    from pynix_os.services.pacemaker import Pacemaker as Pacemaker
    from pynix_os.services.packagekit import Packagekit as Packagekit
    from pynix_os.services.pairdrop import Pairdrop as Pairdrop, Pairdrop_Environment as Pairdrop_Environment
    from pynix_os.services.paisa import Paisa as Paisa, Paisa_Settings as Paisa_Settings
    from pynix_os.services.pangolin import Pangolin as Pangolin
    from pynix_os.services.pantalaimon_headless import (
        PantalaimonHeadless as PantalaimonHeadless,
        PantalaimonHeadless_Instances_Value as PantalaimonHeadless_Instances_Value,
    )
    from pynix_os.services.pantheon import (
        Pantheon_Apps as Pantheon_Apps,
        Pantheon_Contractor as Pantheon_Contractor,
        Pantheon_ParentalControls as Pantheon_ParentalControls,
        Pantheon as Services_Pantheon,
    )
    from pynix_os.services.paperless import (
        Paperless as Paperless,
        Paperless_Database as Paperless_Database,
        Paperless_Exporter as Paperless_Exporter,
        Paperless_Settings as Paperless_Settings,
    )
    from pynix_os.services.papra import Papra as Papra, Papra_Environment as Papra_Environment
    from pynix_os.services.paretosecurity import (
        Paretosecurity as Paretosecurity,
        Paretosecurity_Users_Value as Paretosecurity_Users_Value,
    )
    from pynix_os.services.parsedmarc import (
        Parsedmarc as Parsedmarc,
        Parsedmarc_Provision as Parsedmarc_Provision,
        Parsedmarc_Provision_Grafana as Parsedmarc_Provision_Grafana,
        Parsedmarc_Provision_LocalMail as Parsedmarc_Provision_LocalMail,
        Parsedmarc_Settings as Parsedmarc_Settings,
    )
    from pynix_os.services.part_db import PartDb as PartDb, PartDb_Settings as PartDb_Settings
    from pynix_os.services.passSecretService import PassSecretService as PassSecretService
    from pynix_os.services.patroni import Patroni as Patroni
    from pynix_os.services.pcscd import Pcscd as Pcscd
    from pynix_os.services.pdfding import (
        Pdfding as Pdfding,
        Pdfding_Consume as Pdfding_Consume,
        Pdfding_Gunicorn as Pdfding_Gunicorn,
    )
    from pynix_os.services.pdns_recursor import (
        PdnsRecursor as PdnsRecursor,
        PdnsRecursor_Api as PdnsRecursor_Api,
        PdnsRecursor_Dns as PdnsRecursor_Dns,
    )
    from pynix_os.services.pdnsd import Pdnsd as Pdnsd
    from pynix_os.services.pdudaemon import Pdudaemon as Pdudaemon
    from pynix_os.services.peerflix import Peerflix as Peerflix
    from pynix_os.services.peering_manager import (
        PeeringManager as PeeringManager,
        PeeringManager_Settings as PeeringManager_Settings,
    )
    from pynix_os.services.peertube import (
        Peertube as Peertube,
        Peertube_Database as Peertube_Database,
        Peertube_Redis as Peertube_Redis,
        Peertube_Secrets as Peertube_Secrets,
        Peertube_Settings as Peertube_Settings,
        Peertube_Smtp as Peertube_Smtp,
    )
    from pynix_os.services.peertube_runner import (
        PeertubeRunner as PeertubeRunner,
        PeertubeRunner_InstancesToRegister_Value as PeertubeRunner_InstancesToRegister_Value,
    )
    from pynix_os.services.perses import Perses as Perses, Perses_Settings as Perses_Settings
    from pynix_os.services.persistent_evdev import PersistentEvdev as PersistentEvdev
    from pynix_os.services.pgadmin import Pgadmin as Pgadmin, Pgadmin_EmailServer as Pgadmin_EmailServer
    from pynix_os.services.pgbackrest import (
        Pgbackrest as Pgbackrest,
        Pgbackrest_Commands as Pgbackrest_Commands,
        Pgbackrest_Commands_Annotate as Pgbackrest_Commands_Annotate,
        Pgbackrest_Repos_Value as Pgbackrest_Repos_Value,
        Pgbackrest_Settings as Pgbackrest_Settings,
        Pgbackrest_Stanzas_Value as Pgbackrest_Stanzas_Value,
        Pgbackrest_Stanzas_Value_Instances_Value as Pgbackrest_Stanzas_Value_Instances_Value,
        Pgbackrest_Stanzas_Value_Jobs_Value as Pgbackrest_Stanzas_Value_Jobs_Value,
        Pgbackrest_Stanzas_Value_Settings as Pgbackrest_Stanzas_Value_Settings,
    )
    from pynix_os.services.pgbouncer import Pgbouncer as Pgbouncer, Pgbouncer_Settings as Pgbouncer_Settings
    from pynix_os.services.pgmanage import Pgmanage as Pgmanage, Pgmanage_Tls as Pgmanage_Tls
    from pynix_os.services.pgpkeyserver_lite import PgpkeyserverLite as PgpkeyserverLite
    from pynix_os.services.pgscv import Pgscv as Pgscv
    from pynix_os.services.photonvision import Photonvision as Photonvision
    from pynix_os.services.photoprism import Photoprism as Photoprism
    from pynix_os.services.photoview import Photoview as Photoview, Photoview_Settings as Photoview_Settings
    from pynix_os.services.phpfpm import Phpfpm as Phpfpm, Phpfpm_Pools_Value as Phpfpm_Pools_Value
    from pynix_os.services.phylactery import Phylactery as Phylactery
    from pynix_os.services.physlock import Physlock as Physlock, Physlock_LockOn as Physlock_LockOn
    from pynix_os.services.picom import Picom as Picom
    from pynix_os.services.picosnitch import Picosnitch as Picosnitch
    from pynix_os.services.pict_rs import PictRs as PictRs
    from pynix_os.services.pid_fan_controller import (
        PidFanController as PidFanController,
        PidFanController_Settings as PidFanController_Settings,
    )
    from pynix_os.services.pihole_ftl import (
        PiholeFtl as PiholeFtl,
        PiholeFtl_Lists_Item as PiholeFtl_Lists_Item,
        PiholeFtl_QueryLogDeleter as PiholeFtl_QueryLogDeleter,
    )
    from pynix_os.services.pihole_web import PiholeWeb as PiholeWeb, PiholeWeb_Ports_Item_Or as PiholeWeb_Ports_Item_Or
    from pynix_os.services.pinchflat import Pinchflat as Pinchflat
    from pynix_os.services.pinnwand import Pinnwand as Pinnwand, Pinnwand_Settings as Pinnwand_Settings
    from pynix_os.services.pipewire import (
        Pipewire as Pipewire,
        Pipewire_Alsa as Pipewire_Alsa,
        Pipewire_Audio as Pipewire_Audio,
        Pipewire_ExtraConfig as Pipewire_ExtraConfig,
        Pipewire_Jack as Pipewire_Jack,
        Pipewire_Pulse as Pipewire_Pulse,
        Pipewire_Wireplumber as Pipewire_Wireplumber,
    )
    from pynix_os.services.pixelfed import (
        Pixelfed as Pixelfed,
        Pixelfed_Nginx as Pixelfed_Nginx,
        Pixelfed_Nginx_Listen_Item as Pixelfed_Nginx_Listen_Item,
        Pixelfed_Nginx_Locations_Value as Pixelfed_Nginx_Locations_Value,
        Pixelfed_Redis as Pixelfed_Redis,
    )
    from pynix_os.services.pixiecore import Pixiecore as Pixiecore
    from pynix_os.services.plantuml_server import (
        PlantumlServer as PlantumlServer,
        PlantumlServer_Packages as PlantumlServer_Packages,
    )
    from pynix_os.services.plausible import (
        Plausible as Plausible,
        Plausible_AdminUser as Plausible_AdminUser,
        Plausible_Database as Plausible_Database,
        Plausible_Database_Clickhouse as Plausible_Database_Clickhouse,
        Plausible_Database_Postgres as Plausible_Database_Postgres,
        Plausible_Mail as Plausible_Mail,
        Plausible_Mail_Smtp as Plausible_Mail_Smtp,
        Plausible_Server as Plausible_Server,
    )
    from pynix_os.services.playerctld import Playerctld as Playerctld
    from pynix_os.services.pleroma import Pleroma as Pleroma
    from pynix_os.services.plex import Plex as Plex
    from pynix_os.services.plikd import Plikd as Plikd
    from pynix_os.services.pocket_id import PocketId as PocketId, PocketId_Settings as PocketId_Settings
    from pynix_os.services.podgrab import Podgrab as Podgrab
    from pynix_os.services.polaris import Polaris as Polaris
    from pynix_os.services.pomerium import Pomerium as Pomerium
    from pynix_os.services.porn_vault import PornVault as PornVault
    from pynix_os.services.portmaster import (
        Portmaster as Portmaster,
        Portmaster_Profiles_Value as Portmaster_Profiles_Value,
        Portmaster_Profiles_Value_Fingerprints_Item as Portmaster_Profiles_Value_Fingerprints_Item,
        Portmaster_Profiles_Value_Packages_Item as Portmaster_Profiles_Value_Packages_Item,
        Portmaster_Profiles_Value_Settings as Portmaster_Profiles_Value_Settings,
        Portmaster_Settings as Portmaster_Settings,
    )
    from pynix_os.services.portunus import (
        Portunus as Portunus,
        Portunus_Dex as Portunus_Dex,
        Portunus_Dex_OidcClients_Item as Portunus_Dex_OidcClients_Item,
        Portunus_Ldap as Portunus_Ldap,
    )
    from pynix_os.services.porxie import Porxie as Porxie, Porxie_Settings as Porxie_Settings
    from pynix_os.services.postfix import (
        Postfix as Postfix,
        Postfix_HeaderChecks_Item as Postfix_HeaderChecks_Item,
        Postfix_Settings as Postfix_Settings,
        Postfix_Settings_Main as Postfix_Settings_Main,
        Postfix_Settings_Master_Value as Postfix_Settings_Master_Value,
    )
    from pynix_os.services.postfix_tlspol import (
        PostfixTlspol as PostfixTlspol,
        PostfixTlspol_Settings as PostfixTlspol_Settings,
    )
    from pynix_os.services.postgres_websockets import (
        PostgresWebsockets as PostgresWebsockets,
        PostgresWebsockets_Environment as PostgresWebsockets_Environment,
        PostgresWebsockets_Environment_PGWSDBURI as PostgresWebsockets_Environment_PGWSDBURI,
    )
    from pynix_os.services.postgresql import (
        Postgresql as Postgresql,
        Postgresql_EnsureUsers_Item as Postgresql_EnsureUsers_Item,
        Postgresql_EnsureUsers_Item_EnsureClauses as Postgresql_EnsureUsers_Item_EnsureClauses,
        Postgresql_Settings as Postgresql_Settings,
        Postgresql_SystemCallFilter_Value as Postgresql_SystemCallFilter_Value,
    )
    from pynix_os.services.postgresqlBackup import PostgresqlBackup as PostgresqlBackup
    from pynix_os.services.postgresqlWalReceiver import (
        PostgresqlWalReceiver as PostgresqlWalReceiver,
        PostgresqlWalReceiver_Receivers_Value as PostgresqlWalReceiver_Receivers_Value,
    )
    from pynix_os.services.postgrest import (
        Postgrest as Postgrest,
        Postgrest_Settings as Postgrest_Settings,
        Postgrest_Settings_DbUri as Postgrest_Settings_DbUri,
    )
    from pynix_os.services.postgrey import (
        Postgrey as Postgrey,
        Postgrey_Socket as Postgrey_Socket,
        Postgrey_Socket_Or as Postgrey_Socket_Or,
    )
    from pynix_os.services.postsrsd import Postsrsd as Postsrsd, Postsrsd_Settings as Postsrsd_Settings
    from pynix_os.services.power_profiles_daemon import PowerProfilesDaemon as PowerProfilesDaemon
    from pynix_os.services.powerdns import Powerdns as Powerdns
    from pynix_os.services.powerdns_admin import PowerdnsAdmin as PowerdnsAdmin
    from pynix_os.services.powerstation import Powerstation as Powerstation
    from pynix_os.services.pppd import Pppd as Pppd, Pppd_Peers_Value as Pppd_Peers_Value
    from pynix_os.services.pptpd import Pptpd as Pptpd
    from pynix_os.services.prefect import Prefect as Prefect, Prefect_WorkerPools_Value as Prefect_WorkerPools_Value
    from pynix_os.services.pretalx import (
        Pretalx as Pretalx,
        Pretalx_Celery as Pretalx_Celery,
        Pretalx_Database as Pretalx_Database,
        Pretalx_Gunicorn as Pretalx_Gunicorn,
        Pretalx_Nginx as Pretalx_Nginx,
        Pretalx_Settings as Pretalx_Settings,
    )
    from pynix_os.services.pretix import (
        Pretix as Pretix,
        Pretix_Celery as Pretix_Celery,
        Pretix_Database as Pretix_Database,
        Pretix_Gunicorn as Pretix_Gunicorn,
        Pretix_Nginx as Pretix_Nginx,
        Pretix_Settings as Pretix_Settings,
    )
    from pynix_os.services.printing import (
        Printing as Printing,
        Printing_Browsed as Printing_Browsed,
        Printing_CupsPdf as Printing_CupsPdf,
        Printing_CupsPdf_Instances_Value as Printing_CupsPdf_Instances_Value,
        Printing_CupsPdf_Instances_Value_Settings as Printing_CupsPdf_Instances_Value_Settings,
    )
    from pynix_os.services.privatebin import Privatebin as Privatebin, Privatebin_Settings as Privatebin_Settings
    from pynix_os.services.privoxy import Privoxy as Privoxy, Privoxy_Settings as Privoxy_Settings
    from pynix_os.services.prometheus import (
        Prometheus as Prometheus,
        Prometheus_Alertmanager as Prometheus_Alertmanager,
        Prometheus_AlertmanagerGotify as Prometheus_AlertmanagerGotify,
        Prometheus_AlertmanagerGotify_GotifyEndpoint as Prometheus_AlertmanagerGotify_GotifyEndpoint,
        Prometheus_AlertmanagerGotify_Metrics as Prometheus_AlertmanagerGotify_Metrics,
        Prometheus_AlertmanagerIrcRelay as Prometheus_AlertmanagerIrcRelay,
        Prometheus_AlertmanagerNtfy as Prometheus_AlertmanagerNtfy,
        Prometheus_AlertmanagerNtfy_Settings as Prometheus_AlertmanagerNtfy_Settings,
        Prometheus_AlertmanagerNtfy_Settings_NtfyNotificationTags_Item as Prometheus_AlertmanagerNtfy_Settings_NtfyNotificationTags_Item,
        Prometheus_AlertmanagerWebhookLogger as Prometheus_AlertmanagerWebhookLogger,
        Prometheus_Exporters as Prometheus_Exporters,
        Prometheus_Exporters_Apcupsd as Prometheus_Exporters_Apcupsd,
        Prometheus_Exporters_Artifactory as Prometheus_Exporters_Artifactory,
        Prometheus_Exporters_Bind as Prometheus_Exporters_Bind,
        Prometheus_Exporters_Bird as Prometheus_Exporters_Bird,
        Prometheus_Exporters_Bitcoin as Prometheus_Exporters_Bitcoin,
        Prometheus_Exporters_Blackbox as Prometheus_Exporters_Blackbox,
        Prometheus_Exporters_Borgmatic as Prometheus_Exporters_Borgmatic,
        Prometheus_Exporters_BuildkiteAgent as Prometheus_Exporters_BuildkiteAgent,
        Prometheus_Exporters_Chrony as Prometheus_Exporters_Chrony,
        Prometheus_Exporters_Collectd as Prometheus_Exporters_Collectd,
        Prometheus_Exporters_Deluge as Prometheus_Exporters_Deluge,
        Prometheus_Exporters_Dmarc as Prometheus_Exporters_Dmarc,
        Prometheus_Exporters_Dnsmasq as Prometheus_Exporters_Dnsmasq,
        Prometheus_Exporters_Dnssec as Prometheus_Exporters_Dnssec,
        Prometheus_Exporters_Domain as Prometheus_Exporters_Domain,
        Prometheus_Exporters_Dovecot as Prometheus_Exporters_Dovecot,
        Prometheus_Exporters_Ebpf as Prometheus_Exporters_Ebpf,
        Prometheus_Exporters_Ecoflow as Prometheus_Exporters_Ecoflow,
        Prometheus_Exporters_Elasticsearch as Prometheus_Exporters_Elasticsearch,
        Prometheus_Exporters_ExportarrBazarr as Prometheus_Exporters_ExportarrBazarr,
        Prometheus_Exporters_ExportarrLidarr as Prometheus_Exporters_ExportarrLidarr,
        Prometheus_Exporters_ExportarrProwlarr as Prometheus_Exporters_ExportarrProwlarr,
        Prometheus_Exporters_ExportarrRadarr as Prometheus_Exporters_ExportarrRadarr,
        Prometheus_Exporters_ExportarrReadarr as Prometheus_Exporters_ExportarrReadarr,
        Prometheus_Exporters_ExportarrSonarr as Prometheus_Exporters_ExportarrSonarr,
        Prometheus_Exporters_Fail2ban as Prometheus_Exporters_Fail2ban,
        Prometheus_Exporters_Fastly as Prometheus_Exporters_Fastly,
        Prometheus_Exporters_Flow as Prometheus_Exporters_Flow,
        Prometheus_Exporters_Fritz as Prometheus_Exporters_Fritz,
        Prometheus_Exporters_Fritz_Settings as Prometheus_Exporters_Fritz_Settings,
        Prometheus_Exporters_Fritz_Settings_Devices_Item as Prometheus_Exporters_Fritz_Settings_Devices_Item,
        Prometheus_Exporters_Fritzbox as Prometheus_Exporters_Fritzbox,
        Prometheus_Exporters_Frr as Prometheus_Exporters_Frr,
        Prometheus_Exporters_Graphite as Prometheus_Exporters_Graphite,
        Prometheus_Exporters_Graphite_MappingSettings as Prometheus_Exporters_Graphite_MappingSettings,
        Prometheus_Exporters_Idrac as Prometheus_Exporters_Idrac,
        Prometheus_Exporters_ImapMailstat as Prometheus_Exporters_ImapMailstat,
        Prometheus_Exporters_ImapMailstat_Accounts_Value as Prometheus_Exporters_ImapMailstat_Accounts_Value,
        Prometheus_Exporters_Influxdb as Prometheus_Exporters_Influxdb,
        Prometheus_Exporters_Ipmi as Prometheus_Exporters_Ipmi,
        Prometheus_Exporters_Jitsi as Prometheus_Exporters_Jitsi,
        Prometheus_Exporters_Json as Prometheus_Exporters_Json,
        Prometheus_Exporters_JunosCzerwonk as Prometheus_Exporters_JunosCzerwonk,
        Prometheus_Exporters_Kafka as Prometheus_Exporters_Kafka,
        Prometheus_Exporters_Kea as Prometheus_Exporters_Kea,
        Prometheus_Exporters_Keylight as Prometheus_Exporters_Keylight,
        Prometheus_Exporters_Klipper as Prometheus_Exporters_Klipper,
        Prometheus_Exporters_Knot as Prometheus_Exporters_Knot,
        Prometheus_Exporters_Kvrocks as Prometheus_Exporters_Kvrocks,
        Prometheus_Exporters_Libvirt as Prometheus_Exporters_Libvirt,
        Prometheus_Exporters_Lnd as Prometheus_Exporters_Lnd,
        Prometheus_Exporters_Mail as Prometheus_Exporters_Mail,
        Prometheus_Exporters_MailTlsaCheck as Prometheus_Exporters_MailTlsaCheck,
        Prometheus_Exporters_MailTlsaCheck_Settings as Prometheus_Exporters_MailTlsaCheck_Settings,
        Prometheus_Exporters_Mail_Configuration as Prometheus_Exporters_Mail_Configuration,
        Prometheus_Exporters_Mail_Configuration_Servers_Item as Prometheus_Exporters_Mail_Configuration_Servers_Item,
        Prometheus_Exporters_Mailman3 as Prometheus_Exporters_Mailman3,
        Prometheus_Exporters_Mikrotik as Prometheus_Exporters_Mikrotik,
        Prometheus_Exporters_Modemmanager as Prometheus_Exporters_Modemmanager,
        Prometheus_Exporters_Mongodb as Prometheus_Exporters_Mongodb,
        Prometheus_Exporters_Mqtt as Prometheus_Exporters_Mqtt,
        Prometheus_Exporters_Mysqld as Prometheus_Exporters_Mysqld,
        Prometheus_Exporters_Nats as Prometheus_Exporters_Nats,
        Prometheus_Exporters_Nextcloud as Prometheus_Exporters_Nextcloud,
        Prometheus_Exporters_Nginx as Prometheus_Exporters_Nginx,
        Prometheus_Exporters_Nginxlog as Prometheus_Exporters_Nginxlog,
        Prometheus_Exporters_Nginxlog_Settings as Prometheus_Exporters_Nginxlog_Settings,
        Prometheus_Exporters_Node as Prometheus_Exporters_Node,
        Prometheus_Exporters_NodeCert as Prometheus_Exporters_NodeCert,
        Prometheus_Exporters_Nut as Prometheus_Exporters_Nut,
        Prometheus_Exporters_NvidiaGpu as Prometheus_Exporters_NvidiaGpu,
        Prometheus_Exporters_Opnsense as Prometheus_Exporters_Opnsense,
        Prometheus_Exporters_Pgbouncer as Prometheus_Exporters_Pgbouncer,
        Prometheus_Exporters_PhpFpm as Prometheus_Exporters_PhpFpm,
        Prometheus_Exporters_Pihole as Prometheus_Exporters_Pihole,
        Prometheus_Exporters_Ping as Prometheus_Exporters_Ping,
        Prometheus_Exporters_Postfix as Prometheus_Exporters_Postfix,
        Prometheus_Exporters_Postgres as Prometheus_Exporters_Postgres,
        Prometheus_Exporters_Process as Prometheus_Exporters_Process,
        Prometheus_Exporters_Pve as Prometheus_Exporters_Pve,
        Prometheus_Exporters_PyAirControl as Prometheus_Exporters_PyAirControl,
        Prometheus_Exporters_Rasdaemon as Prometheus_Exporters_Rasdaemon,
        Prometheus_Exporters_Redis as Prometheus_Exporters_Redis,
        Prometheus_Exporters_Restic as Prometheus_Exporters_Restic,
        Prometheus_Exporters_Rtl433 as Prometheus_Exporters_Rtl433,
        Prometheus_Exporters_Rtl433_Channels_Item as Prometheus_Exporters_Rtl433_Channels_Item,
        Prometheus_Exporters_Rtl433_Ids_Item as Prometheus_Exporters_Rtl433_Ids_Item,
        Prometheus_Exporters_Sabnzbd as Prometheus_Exporters_Sabnzbd,
        Prometheus_Exporters_Sabnzbd_Servers_Item as Prometheus_Exporters_Sabnzbd_Servers_Item,
        Prometheus_Exporters_Script as Prometheus_Exporters_Script,
        Prometheus_Exporters_Shelly as Prometheus_Exporters_Shelly,
        Prometheus_Exporters_Smartctl as Prometheus_Exporters_Smartctl,
        Prometheus_Exporters_Smokeping as Prometheus_Exporters_Smokeping,
        Prometheus_Exporters_Snmp as Prometheus_Exporters_Snmp,
        Prometheus_Exporters_Snowflake as Prometheus_Exporters_Snowflake,
        Prometheus_Exporters_Speedtest as Prometheus_Exporters_Speedtest,
        Prometheus_Exporters_Sql as Prometheus_Exporters_Sql,
        Prometheus_Exporters_Sql_Configuration as Prometheus_Exporters_Sql_Configuration,
        Prometheus_Exporters_Sql_Configuration_Jobs_Value as Prometheus_Exporters_Sql_Configuration_Jobs_Value,
        Prometheus_Exporters_Sql_Configuration_Jobs_Value_Queries_Value as Prometheus_Exporters_Sql_Configuration_Jobs_Value_Queries_Value,
        Prometheus_Exporters_Statsd as Prometheus_Exporters_Statsd,
        Prometheus_Exporters_Storagebox as Prometheus_Exporters_Storagebox,
        Prometheus_Exporters_Surfboard as Prometheus_Exporters_Surfboard,
        Prometheus_Exporters_Systemd as Prometheus_Exporters_Systemd,
        Prometheus_Exporters_Tailscale as Prometheus_Exporters_Tailscale,
        Prometheus_Exporters_Tibber as Prometheus_Exporters_Tibber,
        Prometheus_Exporters_Unbound as Prometheus_Exporters_Unbound,
        Prometheus_Exporters_Unpoller as Prometheus_Exporters_Unpoller,
        Prometheus_Exporters_Unpoller_Controllers_Item as Prometheus_Exporters_Unpoller_Controllers_Item,
        Prometheus_Exporters_V2ray as Prometheus_Exporters_V2ray,
        Prometheus_Exporters_Varnish as Prometheus_Exporters_Varnish,
        Prometheus_Exporters_Wireguard as Prometheus_Exporters_Wireguard,
        Prometheus_Exporters_Xray as Prometheus_Exporters_Xray,
        Prometheus_Exporters_Yace as Prometheus_Exporters_Yace,
        Prometheus_Exporters_Zfs as Prometheus_Exporters_Zfs,
        Prometheus_Exporters_ZfsSiebenmann as Prometheus_Exporters_ZfsSiebenmann,
        Prometheus_GlobalConfig as Prometheus_GlobalConfig,
        Prometheus_Pushgateway as Prometheus_Pushgateway,
        Prometheus_Pushgateway_Log as Prometheus_Pushgateway_Log,
        Prometheus_Pushgateway_Persistence as Prometheus_Pushgateway_Persistence,
        Prometheus_Pushgateway_Web as Prometheus_Pushgateway_Web,
        Prometheus_RemoteRead_Item as Prometheus_RemoteRead_Item,
        Prometheus_RemoteRead_Item_BasicAuth as Prometheus_RemoteRead_Item_BasicAuth,
        Prometheus_RemoteRead_Item_TlsConfig as Prometheus_RemoteRead_Item_TlsConfig,
        Prometheus_RemoteWrite_Item as Prometheus_RemoteWrite_Item,
        Prometheus_RemoteWrite_Item_MetadataConfig as Prometheus_RemoteWrite_Item_MetadataConfig,
        Prometheus_RemoteWrite_Item_QueueConfig as Prometheus_RemoteWrite_Item_QueueConfig,
        Prometheus_RemoteWrite_Item_Sigv4 as Prometheus_RemoteWrite_Item_Sigv4,
        Prometheus_RemoteWrite_Item_WriteRelabelConfigs_Item as Prometheus_RemoteWrite_Item_WriteRelabelConfigs_Item,
        Prometheus_Sachet as Prometheus_Sachet,
        Prometheus_ScrapeConfigs_Item as Prometheus_ScrapeConfigs_Item,
        Prometheus_ScrapeConfigs_Item_AzureSdConfigs_Item as Prometheus_ScrapeConfigs_Item_AzureSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item as Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Authorization as Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Authorization,
        Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Oauth2 as Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Oauth2,
        Prometheus_ScrapeConfigs_Item_DigitaloceanSdConfigs_Item as Prometheus_ScrapeConfigs_Item_DigitaloceanSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_DnsSdConfigs_Item as Prometheus_ScrapeConfigs_Item_DnsSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item as Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item_Filters_Item as Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item_Filters_Item,
        Prometheus_ScrapeConfigs_Item_DockerswarmSdConfigs_Item as Prometheus_ScrapeConfigs_Item_DockerswarmSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item as Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item_Filters_Item as Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item_Filters_Item,
        Prometheus_ScrapeConfigs_Item_EurekaSdConfigs_Item as Prometheus_ScrapeConfigs_Item_EurekaSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_FileSdConfigs_Item as Prometheus_ScrapeConfigs_Item_FileSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_GceSdConfigs_Item as Prometheus_ScrapeConfigs_Item_GceSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_HetznerSdConfigs_Item as Prometheus_ScrapeConfigs_Item_HetznerSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_HttpSdConfigs_Item as Prometheus_ScrapeConfigs_Item_HttpSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item as Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Namespaces as Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Namespaces,
        Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Selectors_Item as Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Selectors_Item,
        Prometheus_ScrapeConfigs_Item_KumaSdConfigs_Item as Prometheus_ScrapeConfigs_Item_KumaSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_LightsailSdConfigs_Item as Prometheus_ScrapeConfigs_Item_LightsailSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_LinodeSdConfigs_Item as Prometheus_ScrapeConfigs_Item_LinodeSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_MarathonSdConfigs_Item as Prometheus_ScrapeConfigs_Item_MarathonSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_NerveSdConfigs_Item as Prometheus_ScrapeConfigs_Item_NerveSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_OpenstackSdConfigs_Item as Prometheus_ScrapeConfigs_Item_OpenstackSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_PuppetdbSdConfigs_Item as Prometheus_ScrapeConfigs_Item_PuppetdbSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_ScalewaySdConfigs_Item as Prometheus_ScrapeConfigs_Item_ScalewaySdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_StaticConfigs_Item as Prometheus_ScrapeConfigs_Item_StaticConfigs_Item,
        Prometheus_ScrapeConfigs_Item_TritonSdConfigs_Item as Prometheus_ScrapeConfigs_Item_TritonSdConfigs_Item,
        Prometheus_ScrapeConfigs_Item_UyuniSdConfigs_Item as Prometheus_ScrapeConfigs_Item_UyuniSdConfigs_Item,
        Prometheus_XmppAlerts as Prometheus_XmppAlerts,
    )
    from pynix_os.services.prosody import (
        Prosody as Prosody,
        Prosody_DiscoItems_Item as Prosody_DiscoItems_Item,
        Prosody_HttpFileShare as Prosody_HttpFileShare,
        Prosody_Modules as Prosody_Modules,
        Prosody_Muc_Item as Prosody_Muc_Item,
        Prosody_Ssl as Prosody_Ssl,
        Prosody_VirtualHosts_Value as Prosody_VirtualHosts_Value,
    )
    from pynix_os.services.protonmail_bridge import ProtonmailBridge as ProtonmailBridge
    from pynix_os.services.prowlarr import Prowlarr as Prowlarr, Prowlarr_Settings as Prowlarr_Settings
    from pynix_os.services.psd import Psd as Psd
    from pynix_os.services.public_inbox import (
        PublicInbox as PublicInbox,
        PublicInbox_Http as PublicInbox_Http,
        PublicInbox_Imap as PublicInbox_Imap,
        PublicInbox_Inboxes_Value as PublicInbox_Inboxes_Value,
        PublicInbox_Mda as PublicInbox_Mda,
        PublicInbox_Nntp as PublicInbox_Nntp,
        PublicInbox_Postfix as PublicInbox_Postfix,
        PublicInbox_Settings as PublicInbox_Settings,
        PublicInbox_Settings_Coderepo_Value as PublicInbox_Settings_Coderepo_Value,
        PublicInbox_Settings_Publicinbox as PublicInbox_Settings_Publicinbox,
    )
    from pynix_os.services.pufferpanel import Pufferpanel as Pufferpanel
    from pynix_os.services.pulseaudio import (
        Pulseaudio as Pulseaudio,
        Pulseaudio_Daemon as Pulseaudio_Daemon,
        Pulseaudio_Tcp as Pulseaudio_Tcp,
        Pulseaudio_Tcp_AnonymousClients as Pulseaudio_Tcp_AnonymousClients,
        Pulseaudio_Zeroconf as Pulseaudio_Zeroconf,
        Pulseaudio_Zeroconf_Discovery as Pulseaudio_Zeroconf_Discovery,
        Pulseaudio_Zeroconf_Publish as Pulseaudio_Zeroconf_Publish,
    )
    from pynix_os.services.pumpkin import (
        Pumpkin as Pumpkin,
        Pumpkin_Settings as Pumpkin_Settings,
        Pumpkin_Whitelist as Pumpkin_Whitelist,
        Pumpkin_Whitelist_Entries_Item as Pumpkin_Whitelist_Entries_Item,
    )
    from pynix_os.services.pykms import Pykms as Pykms
    from pynix_os.services.pyroscope import Pyroscope as Pyroscope, Pyroscope_Settings as Pyroscope_Settings
    from pynix_os.services.qbit_manage import (
        QbitManage as QbitManage,
        QbitManage_Commands as QbitManage_Commands,
        QbitManage_Settings as QbitManage_Settings,
        QbitManage_Settings_Directory as QbitManage_Settings_Directory,
        QbitManage_Settings_Qbt as QbitManage_Settings_Qbt,
        QbitManage_Settings_Tracker_Value as QbitManage_Settings_Tracker_Value,
        QbitManage_WebServer as QbitManage_WebServer,
    )
    from pynix_os.services.qbittorrent import (
        Qbittorrent as Qbittorrent,
        Qbittorrent_ServerConfig as Qbittorrent_ServerConfig,
    )
    from pynix_os.services.qdrant import Qdrant as Qdrant
    from pynix_os.services.qemuGuest import QemuGuest as QemuGuest
    from pynix_os.services.quake3_server import (
        Quake3Server as Quake3Server,
        Quake3Server_Settings as Quake3Server_Settings,
    )
    from pynix_os.services.quassel import Quassel as Quassel
    from pynix_os.services.qui import Qui as Qui, Qui_Settings as Qui_Settings
    from pynix_os.services.quickwit import (
        Quickwit as Quickwit,
        Quickwit_Settings as Quickwit_Settings,
        Quickwit_Settings_Rest as Quickwit_Settings_Rest,
    )
    from pynix_os.services.r53_ddns import R53Ddns as R53Ddns
    from pynix_os.services.rabbitmq import Rabbitmq as Rabbitmq, Rabbitmq_ManagementPlugin as Rabbitmq_ManagementPlugin
    from pynix_os.services.radarr import Radarr as Radarr, Radarr_Settings as Radarr_Settings
    from pynix_os.services.radicale import Radicale as Radicale
    from pynix_os.services.radicle import (
        Radicle as Radicle,
        Radicle_Ci as Radicle_Ci,
        Radicle_Ci_Adapters as Radicle_Ci_Adapters,
        Radicle_Ci_Adapters_Native as Radicle_Ci_Adapters_Native,
        Radicle_Ci_Adapters_Native_Instances_Value as Radicle_Ci_Adapters_Native_Instances_Value,
        Radicle_Ci_Adapters_Native_Instances_Value_Settings as Radicle_Ci_Adapters_Native_Instances_Value_Settings,
        Radicle_Ci_Broker as Radicle_Ci_Broker,
        Radicle_Ci_Broker_Settings as Radicle_Ci_Broker_Settings,
        Radicle_Ci_Broker_Settings_Adapters_Value as Radicle_Ci_Broker_Settings_Adapters_Value,
        Radicle_Ci_Broker_Settings_Triggers_Item as Radicle_Ci_Broker_Settings_Triggers_Item,
        Radicle_Httpd as Radicle_Httpd,
        Radicle_Httpd_Nginx as Radicle_Httpd_Nginx,
        Radicle_Httpd_Nginx_Listen_Item as Radicle_Httpd_Nginx_Listen_Item,
        Radicle_Httpd_Nginx_Locations_Value as Radicle_Httpd_Nginx_Locations_Value,
        Radicle_Node as Radicle_Node,
        Radicle_Settings as Radicle_Settings,
    )
    from pynix_os.services.radvd import Radvd as Radvd
    from pynix_os.services.ratbagd import Ratbagd as Ratbagd
    from pynix_os.services.rathole import Rathole as Rathole
    from pynix_os.services.rauc import (
        Rauc as Rauc,
        Rauc_Client as Rauc_Client,
        Rauc_MarkGood as Rauc_MarkGood,
        Rauc_Slots_Value_Item as Rauc_Slots_Value_Item,
    )
    from pynix_os.services.rdnssd import Rdnssd as Rdnssd
    from pynix_os.services.reaction import (
        Reaction as Reaction,
        Reaction_Settings as Reaction_Settings,
        Reaction_Settings_Plugins_Value as Reaction_Settings_Plugins_Value,
    )
    from pynix_os.services.readarr import Readarr as Readarr, Readarr_Settings as Readarr_Settings
    from pynix_os.services.readeck import Readeck as Readeck
    from pynix_os.services.realm import Realm as Realm, Realm_Config as Realm_Config
    from pynix_os.services.realmd import Realmd as Realmd
    from pynix_os.services.rebuilderd import Rebuilderd as Rebuilderd, Rebuilderd_Settings as Rebuilderd_Settings
    from pynix_os.services.recyclarr import Recyclarr as Recyclarr
    from pynix_os.services.redis import (
        Redis as Redis,
        Redis_Servers_Value as Redis_Servers_Value,
        Redis_Servers_Value_SlaveOf as Redis_Servers_Value_SlaveOf,
    )
    from pynix_os.services.redlib import Redlib as Redlib, Redlib_Settings as Redlib_Settings
    from pynix_os.services.redmine import Redmine as Redmine, Redmine_Components as Redmine_Components
    from pynix_os.services.redshift import (
        Redshift as Redshift,
        Redshift_Brightness as Redshift_Brightness,
        Redshift_Temperature as Redshift_Temperature,
    )
    from pynix_os.services.redsocks import Redsocks as Redsocks, Redsocks_Redsocks_Item as Redsocks_Redsocks_Item
    from pynix_os.services.reframe import Reframe as Reframe, Reframe_Configs as Reframe_Configs
    from pynix_os.services.remark42 import Remark42 as Remark42
    from pynix_os.services.renovate import Renovate as Renovate
    from pynix_os.services.reposilite import (
        Reposilite as Reposilite,
        Reposilite_Database as Reposilite_Database,
        Reposilite_Settings as Reposilite_Settings,
    )
    from pynix_os.services.resilio import Resilio as Resilio
    from pynix_os.services.resolved import (
        Resolved as Resolved,
        Resolved_DnsDelegates_Value as Resolved_DnsDelegates_Value,
        Resolved_DnsDelegates_Value_Delegate as Resolved_DnsDelegates_Value_Delegate,
        Resolved_Settings as Resolved_Settings,
        Resolved_Settings_Resolve as Resolved_Settings_Resolve,
    )
    from pynix_os.services.restic import (
        Restic as Restic,
        Restic_Backups_Value as Restic_Backups_Value,
        Restic_Server as Restic_Server,
    )
    from pynix_os.services.rethinkdb import Rethinkdb as Rethinkdb
    from pynix_os.services.riemann import Riemann as Riemann
    from pynix_os.services.riemann_dash import RiemannDash as RiemannDash
    from pynix_os.services.riemann_tools import RiemannTools as RiemannTools
    from pynix_os.services.rimgo import Rimgo as Rimgo, Rimgo_Settings as Rimgo_Settings
    from pynix_os.services.ringboard import (
        Ringboard as Ringboard,
        Ringboard_Wayland as Ringboard_Wayland,
        Ringboard_X11 as Ringboard_X11,
    )
    from pynix_os.services.rke2 import (
        Rke2 as Rke2,
        Rke2_AutoDeployCharts_Value as Rke2_AutoDeployCharts_Value,
        Rke2_GracefulNodeShutdown as Rke2_GracefulNodeShutdown,
        Rke2_Manifests_Value as Rke2_Manifests_Value,
    )
    from pynix_os.services.rkvm import (
        Rkvm as Rkvm,
        Rkvm_Client as Rkvm_Client,
        Rkvm_Client_Settings as Rkvm_Client_Settings,
        Rkvm_Server as Rkvm_Server,
        Rkvm_Server_Settings as Rkvm_Server_Settings,
    )
    from pynix_os.services.rmfakecloud import Rmfakecloud as Rmfakecloud
    from pynix_os.services.rnsd import Rnsd as Rnsd, Rnsd_HealthCheck as Rnsd_HealthCheck
    from pynix_os.services.robustirc_bridge import RobustircBridge as RobustircBridge
    from pynix_os.services.romm import (
        Romm as Romm,
        Romm_Database as Romm_Database,
        Romm_Nginx as Romm_Nginx,
        Romm_Redis as Romm_Redis,
        Romm_Watcher as Romm_Watcher,
    )
    from pynix_os.services.roon_bridge import RoonBridge as RoonBridge
    from pynix_os.services.roon_server import RoonServer as RoonServer
    from pynix_os.services.rosec import Rosec as Rosec, Rosec_Pam as Rosec_Pam
    from pynix_os.services.rosenpass import (
        Rosenpass as Rosenpass,
        Rosenpass_Settings as Rosenpass_Settings,
        Rosenpass_Settings_Peers_Item as Rosenpass_Settings_Peers_Item,
    )
    from pynix_os.services.roundcube import Roundcube as Roundcube, Roundcube_Database as Roundcube_Database
    from pynix_os.services.routedns import Routedns as Routedns
    from pynix_os.services.routinator import Routinator as Routinator, Routinator_Settings as Routinator_Settings
    from pynix_os.services.rpcbind import Rpcbind as Rpcbind
    from pynix_os.services.rqbit import Rqbit as Rqbit
    from pynix_os.services.rshim import Rshim as Rshim
    from pynix_os.services.rsnapshot import Rsnapshot as Rsnapshot
    from pynix_os.services.rspamd import (
        Rspamd as Rspamd,
        Rspamd_Locals_Value as Rspamd_Locals_Value,
        Rspamd_Overrides_Value as Rspamd_Overrides_Value,
        Rspamd_Postfix as Rspamd_Postfix,
        Rspamd_Workers_Value as Rspamd_Workers_Value,
        Rspamd_Workers_Value_BindSockets_Item_Or as Rspamd_Workers_Value_BindSockets_Item_Or,
    )
    from pynix_os.services.rspamd_trainer import (
        RspamdTrainer as RspamdTrainer,
        RspamdTrainer_Settings as RspamdTrainer_Settings,
    )
    from pynix_os.services.rss2email import Rss2email as Rss2email, Rss2email_Feeds_Value as Rss2email_Feeds_Value
    from pynix_os.services.rss_bridge import RssBridge as RssBridge, RssBridge_Config as RssBridge_Config
    from pynix_os.services.rsshub import (
        Rsshub as Rsshub,
        Rsshub_Redis as Rsshub_Redis,
        Rsshub_Settings as Rsshub_Settings,
    )
    from pynix_os.services.rstudio_server import RstudioServer as RstudioServer
    from pynix_os.services.rsync import Rsync as Rsync, Rsync_Jobs_Value as Rsync_Jobs_Value
    from pynix_os.services.rsyncd import Rsyncd as Rsyncd, Rsyncd_Settings as Rsyncd_Settings
    from pynix_os.services.rsyslogd import Rsyslogd as Rsyslogd
    from pynix_os.services.rtorrent import Rtorrent as Rtorrent
    from pynix_os.services.rumno import Rumno as Rumno
    from pynix_os.services.rundeck import (
        Rundeck as Rundeck,
        Rundeck_FrameworkSettings as Rundeck_FrameworkSettings,
        Rundeck_Settings as Rundeck_Settings,
        Rundeck_Ssl as Rundeck_Ssl,
    )
    from pynix_os.services.rust_federation_tester import (
        RustFederationTester as RustFederationTester,
        RustFederationTester_Settings as RustFederationTester_Settings,
    )
    from pynix_os.services.rustdesk_server import (
        RustdeskServer as RustdeskServer,
        RustdeskServer_Relay as RustdeskServer_Relay,
        RustdeskServer_Signal as RustdeskServer_Signal,
    )
    from pynix_os.services.rustfs import Rustfs as Rustfs, Rustfs_Settings as Rustfs_Settings
    from pynix_os.services.rustical import Rustical as Rustical, Rustical_Settings as Rustical_Settings
    from pynix_os.services.rustus import (
        Rustus as Rustus,
        Rustus_InfoStorage as Rustus_InfoStorage,
        Rustus_Storage as Rustus_Storage,
    )
    from pynix_os.services.rutorrent import Rutorrent as Rutorrent, Rutorrent_Nginx as Rutorrent_Nginx
    from pynix_os.services.sabnzbd import (
        Sabnzbd as Sabnzbd,
        Sabnzbd_Settings as Sabnzbd_Settings,
        Sabnzbd_Settings_Ntfosd as Sabnzbd_Settings_Ntfosd,
        Sabnzbd_Settings_Servers_Value as Sabnzbd_Settings_Servers_Value,
    )
    from pynix_os.services.safeeyes import Safeeyes as Safeeyes
    from pynix_os.services.salt import Salt as Salt, Salt_Master as Salt_Master, Salt_Minion as Salt_Minion
    from pynix_os.services.samba import (
        Samba as Samba,
        Samba_Nmbd as Samba_Nmbd,
        Samba_Settings as Samba_Settings,
        Samba_Smbd as Samba_Smbd,
        Samba_Usershares as Samba_Usershares,
        Samba_Winbindd as Samba_Winbindd,
    )
    from pynix_os.services.samba_wsdd import SambaWsdd as SambaWsdd
    from pynix_os.services.saned import Saned as Saned
    from pynix_os.services.sanoid import (
        Sanoid as Sanoid,
        Sanoid_Datasets_Value as Sanoid_Datasets_Value,
        Sanoid_Templates_Value as Sanoid_Templates_Value,
    )
    from pynix_os.services.saslauthd import Saslauthd as Saslauthd
    from pynix_os.services.saunafs import (
        Saunafs as Saunafs,
        Saunafs_Chunkserver as Saunafs_Chunkserver,
        Saunafs_Chunkserver_Settings as Saunafs_Chunkserver_Settings,
        Saunafs_Client as Saunafs_Client,
        Saunafs_Master as Saunafs_Master,
        Saunafs_Master_Settings as Saunafs_Master_Settings,
        Saunafs_Metalogger as Saunafs_Metalogger,
        Saunafs_Metalogger_Settings as Saunafs_Metalogger_Settings,
    )
    from pynix_os.services.scanservjs import Scanservjs as Scanservjs, Scanservjs_Settings as Scanservjs_Settings
    from pynix_os.services.schleuder import Schleuder as Schleuder, Schleuder_Settings as Schleuder_Settings
    from pynix_os.services.scion import (
        Scion as Scion,
        Scion_ScionControl as Scion_ScionControl,
        Scion_ScionDaemon as Scion_ScionDaemon,
        Scion_ScionDispatcher as Scion_ScionDispatcher,
        Scion_ScionIpGateway as Scion_ScionIpGateway,
        Scion_ScionRouter as Scion_ScionRouter,
    )
    from pynix_os.services.scollector import Scollector as Scollector
    from pynix_os.services.screego import Screego as Screego
    from pynix_os.services.scrutiny import (
        Scrutiny as Scrutiny,
        Scrutiny_Collector as Scrutiny_Collector,
        Scrutiny_Collector_Settings as Scrutiny_Collector_Settings,
        Scrutiny_Influxdb as Scrutiny_Influxdb,
        Scrutiny_Settings as Scrutiny_Settings,
    )
    from pynix_os.services.scx import Scx as Scx
    from pynix_os.services.scx_loader import ScxLoader as ScxLoader, ScxLoader_Config as ScxLoader_Config
    from pynix_os.services.sdrplayApi import SdrplayApi as SdrplayApi
    from pynix_os.services.searx import Searx as Searx, Searx_Settings as Searx_Settings
    from pynix_os.services.seatd import Seatd as Seatd
    from pynix_os.services.seerr import Seerr as Seerr
    from pynix_os.services.self_deploy import SelfDeploy as SelfDeploy
    from pynix_os.services.selfoss import (
        Selfoss as Selfoss,
        Selfoss_Nginx as Selfoss_Nginx,
        Selfoss_Settings as Selfoss_Settings,
    )
    from pynix_os.services.send import Send as Send, Send_Redis as Send_Redis
    from pynix_os.services.serviio import Serviio as Serviio
    from pynix_os.services.sftpgo import (
        Sftpgo as Sftpgo,
        Sftpgo_Settings as Sftpgo_Settings,
        Sftpgo_Settings_FtpdBindings_Item as Sftpgo_Settings_FtpdBindings_Item,
        Sftpgo_Settings_HttpdBindings_Item as Sftpgo_Settings_HttpdBindings_Item,
        Sftpgo_Settings_SftpdBindings_Item as Sftpgo_Settings_SftpdBindings_Item,
        Sftpgo_Settings_Smtp as Sftpgo_Settings_Smtp,
        Sftpgo_Settings_WebdavdBindings_Item as Sftpgo_Settings_WebdavdBindings_Item,
    )
    from pynix_os.services.shadowsocks import Shadowsocks as Shadowsocks
    from pynix_os.services.shairport_sync import ShairportSync as ShairportSync
    from pynix_os.services.sharkey import Sharkey as Sharkey, Sharkey_Settings as Sharkey_Settings
    from pynix_os.services.shelfmark import Shelfmark as Shelfmark, Shelfmark_Environment as Shelfmark_Environment
    from pynix_os.services.shellhub_agent import ShellhubAgent as ShellhubAgent
    from pynix_os.services.shibboleth_sp import (
        ShibbolethSp as ShibbolethSp,
        ShibbolethSp_Fastcgi as ShibbolethSp_Fastcgi,
    )
    from pynix_os.services.shiori import Shiori as Shiori
    from pynix_os.services.shoko import Shoko as Shoko
    from pynix_os.services.shorewall import Shorewall as Shorewall
    from pynix_os.services.shorewall6 import Shorewall6 as Shorewall6
    from pynix_os.services.sillytavern import Sillytavern as Sillytavern
    from pynix_os.services.silverbullet import Silverbullet as Silverbullet
    from pynix_os.services.sing_box import SingBox as SingBox, SingBox_Settings as SingBox_Settings
    from pynix_os.services.sitespeed_io import (
        SitespeedIo as SitespeedIo,
        SitespeedIo_Runs_Item as SitespeedIo_Runs_Item,
        SitespeedIo_Runs_Item_Settings as SitespeedIo_Runs_Item_Settings,
    )
    from pynix_os.services.sks import Sks as Sks
    from pynix_os.services.skydns import Skydns as Skydns, Skydns_Etcd as Skydns_Etcd
    from pynix_os.services.slimserver import Slimserver as Slimserver
    from pynix_os.services.slskd import (
        Slskd as Slskd,
        Slskd_Nginx as Slskd_Nginx,
        Slskd_Nginx_Listen_Item as Slskd_Nginx_Listen_Item,
        Slskd_Nginx_Locations_Value as Slskd_Nginx_Locations_Value,
        Slskd_Settings as Slskd_Settings,
    )
    from pynix_os.services.slurm import (
        Slurm as Slurm,
        Slurm_Client as Slurm_Client,
        Slurm_Dbdserver as Slurm_Dbdserver,
        Slurm_Mpi as Slurm_Mpi,
        Slurm_Rest as Slurm_Rest,
        Slurm_Rest_Environment as Slurm_Rest_Environment,
        Slurm_Server as Slurm_Server,
    )
    from pynix_os.services.smartd import (
        Smartd as Smartd,
        Smartd_Defaults as Smartd_Defaults,
        Smartd_Devices_Item as Smartd_Devices_Item,
        Smartd_Notifications as Smartd_Notifications,
        Smartd_Notifications_Mail as Smartd_Notifications_Mail,
        Smartd_Notifications_SystembusNotify as Smartd_Notifications_SystembusNotify,
        Smartd_Notifications_Wall as Smartd_Notifications_Wall,
        Smartd_Notifications_X11 as Smartd_Notifications_X11,
    )
    from pynix_os.services.smartdns import Smartdns as Smartdns
    from pynix_os.services.smokeping import Smokeping as Smokeping
    from pynix_os.services.snapper import Snapper as Snapper, Snapper_Configs_Value as Snapper_Configs_Value
    from pynix_os.services.snapraid import (
        Snapraid as Snapraid,
        Snapraid_Scrub as Snapraid_Scrub,
        Snapraid_Sync as Snapraid_Sync,
    )
    from pynix_os.services.snapserver import Snapserver as Snapserver, Snapserver_Settings as Snapserver_Settings
    from pynix_os.services.snipe_it import (
        SnipeIt as SnipeIt,
        SnipeIt_Config_Value_Or as SnipeIt_Config_Value_Or,
        SnipeIt_Database as SnipeIt_Database,
        SnipeIt_Mail as SnipeIt_Mail,
        SnipeIt_Mail_From as SnipeIt_Mail_From,
        SnipeIt_Mail_ReplyTo as SnipeIt_Mail_ReplyTo,
        SnipeIt_Nginx as SnipeIt_Nginx,
        SnipeIt_Nginx_Listen_Item as SnipeIt_Nginx_Listen_Item,
        SnipeIt_Nginx_Locations_Value as SnipeIt_Nginx_Locations_Value,
    )
    from pynix_os.services.sniproxy import Sniproxy as Sniproxy
    from pynix_os.services.snips_sh import SnipsSh as SnipsSh, SnipsSh_Settings as SnipsSh_Settings
    from pynix_os.services.snmpd import Snmpd as Snmpd
    from pynix_os.services.snowflake_proxy import SnowflakeProxy as SnowflakeProxy
    from pynix_os.services.soft_serve import SoftServe as SoftServe
    from pynix_os.services.softether import (
        Softether as Softether,
        Softether_Vpnbridge as Softether_Vpnbridge,
        Softether_Vpnclient as Softether_Vpnclient,
        Softether_Vpnserver as Softether_Vpnserver,
    )
    from pynix_os.services.sogo import Sogo as Sogo
    from pynix_os.services.soju import Soju as Soju, Soju_AdminSocket as Soju_AdminSocket
    from pynix_os.services.solanum import Solanum as Solanum
    from pynix_os.services.sonarr import Sonarr as Sonarr, Sonarr_Settings as Sonarr_Settings
    from pynix_os.services.sonic_server import SonicServer as SonicServer, SonicServer_Settings as SonicServer_Settings
    from pynix_os.services.spacecookie import Spacecookie as Spacecookie, Spacecookie_Settings as Spacecookie_Settings
    from pynix_os.services.spamassassin import Spamassassin as Spamassassin
    from pynix_os.services.spark import Spark as Spark, Spark_Master as Spark_Master, Spark_Worker as Spark_Worker
    from pynix_os.services.speechd import (
        Speechd as Speechd,
        Speechd_Clients as Speechd_Clients,
        Speechd_Modules as Speechd_Modules,
    )
    from pynix_os.services.speedify import Speedify as Speedify
    from pynix_os.services.speedtest_tracker import (
        SpeedtestTracker as SpeedtestTracker,
        SpeedtestTracker_Settings as SpeedtestTracker_Settings,
    )
    from pynix_os.services.spice_autorandr import SpiceAutorandr as SpiceAutorandr
    from pynix_os.services.spice_vdagentd import SpiceVdagentd as SpiceVdagentd
    from pynix_os.services.spice_webdavd import SpiceWebdavd as SpiceWebdavd
    from pynix_os.services.spiped import Spiped as Spiped, Spiped_Config_Value as Spiped_Config_Value
    from pynix_os.services.spire import (
        Spire as Spire,
        Spire_Agent as Spire_Agent,
        Spire_Agent_Settings as Spire_Agent_Settings,
        Spire_Agent_Settings_Plugins as Spire_Agent_Settings_Plugins,
        Spire_Agent_Settings_Plugins_NodeAttestor as Spire_Agent_Settings_Plugins_NodeAttestor,
        Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken as Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken,
        Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken_PluginData as Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken_PluginData,
        Spire_Agent_Settings_Plugins_NodeAttestor_Tpm as Spire_Agent_Settings_Plugins_NodeAttestor_Tpm,
        Spire_Server as Spire_Server,
        Spire_Server_Settings as Spire_Server_Settings,
        Spire_Server_Settings_Plugins as Spire_Server_Settings_Plugins,
        Spire_Server_Settings_Plugins_NodeAttestor as Spire_Server_Settings_Plugins_NodeAttestor,
        Spire_Server_Settings_Plugins_NodeAttestor_JoinToken as Spire_Server_Settings_Plugins_NodeAttestor_JoinToken,
        Spire_Server_Settings_Plugins_NodeAttestor_Tpm as Spire_Server_Settings_Plugins_NodeAttestor_Tpm,
        Spire_Server_Settings_Plugins_NodeAttestor_Tpm_PluginData as Spire_Server_Settings_Plugins_NodeAttestor_Tpm_PluginData,
    )
    from pynix_os.services.spoolman import Spoolman as Spoolman
    from pynix_os.services.spotifyd import Spotifyd as Spotifyd
    from pynix_os.services.squeezelite import (
        Squeezelite as Squeezelite,
        Squeezelite_Pulseaudio as Squeezelite_Pulseaudio,
    )
    from pynix_os.services.squid import Squid as Squid
    from pynix_os.services.ssh_agent_switcher import SshAgentSwitcher as SshAgentSwitcher
    from pynix_os.services.sshd import Sshd as Sshd
    from pynix_os.services.sshguard import Sshguard as Sshguard
    from pynix_os.services.sshwifty import Sshwifty as Sshwifty
    from pynix_os.services.sslh import Sslh as Sslh, Sslh_Settings as Sslh_Settings
    from pynix_os.services.sslmate_agent import SslmateAgent as SslmateAgent
    from pynix_os.services.sssd import Sssd as Sssd
    from pynix_os.services.sstorytime import (
        Sstorytime as Sstorytime,
        Sstorytime_Database as Sstorytime_Database,
        Sstorytime_Settings as Sstorytime_Settings,
    )
    from pynix_os.services.stalwart import Stalwart as Stalwart
    from pynix_os.services.stargazer import Stargazer as Stargazer, Stargazer_Routes_Item as Stargazer_Routes_Item
    from pynix_os.services.stash import (
        Stash as Stash,
        Stash_Settings as Stash_Settings,
        Stash_Settings_StashBoxes_Item as Stash_Settings_StashBoxes_Item,
        Stash_Settings_Stash_Item as Stash_Settings_Stash_Item,
    )
    from pynix_os.services.stash_clipboard import StashClipboard as StashClipboard
    from pynix_os.services.static_web_server import StaticWebServer as StaticWebServer
    from pynix_os.services.step_ca import StepCa as StepCa
    from pynix_os.services.stirling_pdf import StirlingPdf as StirlingPdf
    from pynix_os.services.stratis import Stratis as Stratis
    from pynix_os.services.strfry import Strfry as Strfry
    from pynix_os.services.strichliste import (
        Strichliste as Strichliste,
        Strichliste_Environment as Strichliste_Environment,
        Strichliste_Nginx as Strichliste_Nginx,
        Strichliste_Nginx_VirtualHost as Strichliste_Nginx_VirtualHost,
        Strichliste_Nginx_VirtualHost_Listen_Item as Strichliste_Nginx_VirtualHost_Listen_Item,
        Strichliste_Nginx_VirtualHost_Locations_Value as Strichliste_Nginx_VirtualHost_Locations_Value,
        Strichliste_Packages as Strichliste_Packages,
        Strichliste_Settings as Strichliste_Settings,
    )
    from pynix_os.services.strongswan import Strongswan as Strongswan
    from pynix_os.services.strongswan_swanctl import (
        StrongswanSwanctl as StrongswanSwanctl,
        StrongswanSwanctl_Strongswan as StrongswanSwanctl_Strongswan,
        StrongswanSwanctl_Swanctl as StrongswanSwanctl_Swanctl,
        StrongswanSwanctl_Swanctl_Authorities_Value as StrongswanSwanctl_Swanctl_Authorities_Value,
        StrongswanSwanctl_Swanctl_Connections_Value as StrongswanSwanctl_Swanctl_Connections_Value,
        StrongswanSwanctl_Swanctl_Connections_Value_Children_Value as StrongswanSwanctl_Swanctl_Connections_Value_Children_Value,
        StrongswanSwanctl_Swanctl_Connections_Value_Local_Value as StrongswanSwanctl_Swanctl_Connections_Value_Local_Value,
        StrongswanSwanctl_Swanctl_Connections_Value_Local_Value_Cert_Value as StrongswanSwanctl_Swanctl_Connections_Value_Local_Value_Cert_Value,
        StrongswanSwanctl_Swanctl_Connections_Value_Remote_Value as StrongswanSwanctl_Swanctl_Connections_Value_Remote_Value,
        StrongswanSwanctl_Swanctl_Pools_Value as StrongswanSwanctl_Swanctl_Pools_Value,
        StrongswanSwanctl_Swanctl_Secrets as StrongswanSwanctl_Swanctl_Secrets,
        StrongswanSwanctl_Swanctl_Secrets_Eap_Value as StrongswanSwanctl_Swanctl_Secrets_Eap_Value,
        StrongswanSwanctl_Swanctl_Secrets_Ecdsa_Value as StrongswanSwanctl_Swanctl_Secrets_Ecdsa_Value,
        StrongswanSwanctl_Swanctl_Secrets_Ike_Value as StrongswanSwanctl_Swanctl_Secrets_Ike_Value,
        StrongswanSwanctl_Swanctl_Secrets_Ntlm_Value as StrongswanSwanctl_Swanctl_Secrets_Ntlm_Value,
        StrongswanSwanctl_Swanctl_Secrets_Pkcs12_Value as StrongswanSwanctl_Swanctl_Secrets_Pkcs12_Value,
        StrongswanSwanctl_Swanctl_Secrets_Pkcs8_Value as StrongswanSwanctl_Swanctl_Secrets_Pkcs8_Value,
        StrongswanSwanctl_Swanctl_Secrets_Ppk_Value as StrongswanSwanctl_Swanctl_Secrets_Ppk_Value,
        StrongswanSwanctl_Swanctl_Secrets_Private_Value as StrongswanSwanctl_Swanctl_Secrets_Private_Value,
        StrongswanSwanctl_Swanctl_Secrets_Rsa_Value as StrongswanSwanctl_Swanctl_Secrets_Rsa_Value,
        StrongswanSwanctl_Swanctl_Secrets_Token_Value as StrongswanSwanctl_Swanctl_Secrets_Token_Value,
    )
    from pynix_os.services.stubby import Stubby as Stubby
    from pynix_os.services.stump import Stump as Stump
    from pynix_os.services.stunnel import Stunnel as Stunnel
    from pynix_os.services.subsonic import Subsonic as Subsonic
    from pynix_os.services.sundtek import Sundtek as Sundtek
    from pynix_os.services.sunshine import (
        Sunshine as Sunshine,
        Sunshine_Applications as Sunshine_Applications,
        Sunshine_Settings as Sunshine_Settings,
    )
    from pynix_os.services.supergfxd import Supergfxd as Supergfxd
    from pynix_os.services.supybot import Supybot as Supybot
    from pynix_os.services.suricata import (
        Suricata as Suricata,
        Suricata_Settings as Suricata_Settings,
        Suricata_Settings_AfPacket_Item as Suricata_Settings_AfPacket_Item,
        Suricata_Settings_AfXdp_Item as Suricata_Settings_AfXdp_Item,
        Suricata_Settings_AppLayer as Suricata_Settings_AppLayer,
        Suricata_Settings_AppLayer_Protocols_Value as Suricata_Settings_AppLayer_Protocols_Value,
        Suricata_Settings_Dpdk as Suricata_Settings_Dpdk,
        Suricata_Settings_Dpdk_Interfaces_Item as Suricata_Settings_Dpdk_Interfaces_Item,
        Suricata_Settings_Outputs_Item_Value as Suricata_Settings_Outputs_Item_Value,
        Suricata_Settings_Pcap_Item as Suricata_Settings_Pcap_Item,
        Suricata_Settings_Stats as Suricata_Settings_Stats,
        Suricata_Settings_UnixCommand as Suricata_Settings_UnixCommand,
        Suricata_Settings_Vars as Suricata_Settings_Vars,
        Suricata_Settings_Vars_AddressGroups as Suricata_Settings_Vars_AddressGroups,
    )
    from pynix_os.services.surrealdb import Surrealdb as Surrealdb
    from pynix_os.services.suwayomi_server import (
        SuwayomiServer as SuwayomiServer,
        SuwayomiServer_Settings as SuwayomiServer_Settings,
    )
    from pynix_os.services.svnserve import Svnserve as Svnserve
    from pynix_os.services.swapspace import Swapspace as Swapspace, Swapspace_Settings as Swapspace_Settings
    from pynix_os.services.switcherooControl import SwitcherooControl as SwitcherooControl
    from pynix_os.services.sympa import (
        Sympa as Sympa,
        Sympa_Domains_Value as Sympa_Domains_Value,
        Sympa_SettingsFile_Value as Sympa_SettingsFile_Value,
        Sympa_Web as Sympa_Web,
    )
    from pynix_os.services.synapse_auto_compressor import (
        SynapseAutoCompressor as SynapseAutoCompressor,
        SynapseAutoCompressor_Settings as SynapseAutoCompressor_Settings,
    )
    from pynix_os.services.syncoid import Syncoid as Syncoid, Syncoid_Commands_Value as Syncoid_Commands_Value
    from pynix_os.services.syncplay import Syncplay as Syncplay
    from pynix_os.services.syncthing import (
        Syncthing as Syncthing,
        Syncthing_Relay as Syncthing_Relay,
        Syncthing_Settings as Syncthing_Settings,
        Syncthing_Settings_Devices_Value as Syncthing_Settings_Devices_Value,
        Syncthing_Settings_Folders_Value as Syncthing_Settings_Folders_Value,
        Syncthing_Settings_Folders_Value_Devices_Item_Or as Syncthing_Settings_Folders_Value_Devices_Item_Or,
        Syncthing_Settings_Folders_Value_Versioning as Syncthing_Settings_Folders_Value_Versioning,
        Syncthing_Settings_Options as Syncthing_Settings_Options,
    )
    from pynix_os.services.synergy import (
        Synergy as Synergy,
        Synergy_Client as Synergy_Client,
        Synergy_Server as Synergy_Server,
        Synergy_Server_Tls as Synergy_Server_Tls,
    )
    from pynix_os.services.syslog_ng import SyslogNg as SyslogNg
    from pynix_os.services.syslogd import Syslogd as Syslogd
    from pynix_os.services.sysprof import Sysprof as Sysprof
    from pynix_os.services.sysstat import Sysstat as Sysstat
    from pynix_os.services.system76_scheduler import (
        System76Scheduler as System76Scheduler,
        System76Scheduler_Assignments_Value as System76Scheduler_Assignments_Value,
        System76Scheduler_Settings as System76Scheduler_Settings,
        System76Scheduler_Settings_CfsProfiles as System76Scheduler_Settings_CfsProfiles,
        System76Scheduler_Settings_CfsProfiles_Default as System76Scheduler_Settings_CfsProfiles_Default,
        System76Scheduler_Settings_CfsProfiles_Responsive as System76Scheduler_Settings_CfsProfiles_Responsive,
        System76Scheduler_Settings_ProcessScheduler as System76Scheduler_Settings_ProcessScheduler,
        System76Scheduler_Settings_ProcessScheduler_ForegroundBoost as System76Scheduler_Settings_ProcessScheduler_ForegroundBoost,
        System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Background as System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Background,
        System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Foreground as System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Foreground,
        System76Scheduler_Settings_ProcessScheduler_PipewireBoost as System76Scheduler_Settings_ProcessScheduler_PipewireBoost,
        System76Scheduler_Settings_ProcessScheduler_PipewireBoost_Profile as System76Scheduler_Settings_ProcessScheduler_PipewireBoost_Profile,
    )
    from pynix_os.services.system_config_printer import SystemConfigPrinter as Services_SystemConfigPrinter
    from pynix_os.services.systembus_notify import SystembusNotify as SystembusNotify
    from pynix_os.services.systemd_lock_handler import SystemdLockHandler as SystemdLockHandler
    from pynix_os.services.szurubooru import (
        Szurubooru as Szurubooru,
        Szurubooru_Client as Szurubooru_Client,
        Szurubooru_Database as Szurubooru_Database,
        Szurubooru_Server as Szurubooru_Server,
        Szurubooru_Server_Settings as Szurubooru_Server_Settings,
    )
    from pynix_os.services.tabby import Tabby as Tabby
    from pynix_os.services.tabbyapi import (
        Tabbyapi as Tabbyapi,
        Tabbyapi_Settings as Tabbyapi_Settings,
        Tabbyapi_Settings_LoraLoras_Item as Tabbyapi_Settings_LoraLoras_Item,
    )
    from pynix_os.services.tahoe import (
        Tahoe as Tahoe,
        Tahoe_Introducers_Value as Tahoe_Introducers_Value,
        Tahoe_Nodes_Value as Tahoe_Nodes_Value,
    )
    from pynix_os.services.tailscale import (
        Tailscale as Tailscale,
        Tailscale_AuthKeyParameters as Tailscale_AuthKeyParameters,
        Tailscale_Derper as Tailscale_Derper,
        Tailscale_Serve as Tailscale_Serve,
        Tailscale_Serve_Services_Value as Tailscale_Serve_Services_Value,
    )
    from pynix_os.services.tailscaleAuth import TailscaleAuth as TailscaleAuth
    from pynix_os.services.taler import (
        Taler as Taler,
        Taler_Exchange as Taler_Exchange,
        Taler_Exchange_Settings as Taler_Exchange_Settings,
        Taler_Merchant as Taler_Merchant,
        Taler_Merchant_Settings as Taler_Merchant_Settings,
        Taler_Settings as Taler_Settings,
    )
    from pynix_os.services.tandoor_recipes import (
        TandoorRecipes as TandoorRecipes,
        TandoorRecipes_Database as TandoorRecipes_Database,
    )
    from pynix_os.services.tang import Tang as Tang
    from pynix_os.services.tap import Tap as Tap, Tap_Settings as Tap_Settings
    from pynix_os.services.target import Target as Target
    from pynix_os.services.tarsnap import Tarsnap as Tarsnap, Tarsnap_Archives_Value as Tarsnap_Archives_Value
    from pynix_os.services.taskchampion_sync_server import (
        TaskchampionSyncServer as TaskchampionSyncServer,
        TaskchampionSyncServer_Snapshot as TaskchampionSyncServer_Snapshot,
    )
    from pynix_os.services.taskserver import (
        Taskserver as Taskserver,
        Taskserver_Organisations_Value as Taskserver_Organisations_Value,
        Taskserver_Pki as Taskserver_Pki,
        Taskserver_Pki_Auto as Taskserver_Pki_Auto,
        Taskserver_Pki_Auto_Expiration as Taskserver_Pki_Auto_Expiration,
        Taskserver_Pki_Manual as Taskserver_Pki_Manual,
        Taskserver_Pki_Manual_Ca as Taskserver_Pki_Manual_Ca,
        Taskserver_Pki_Manual_Server as Taskserver_Pki_Manual_Server,
    )
    from pynix_os.services.tautulli import Tautulli as Tautulli
    from pynix_os.services.tayga import (
        Tayga as Tayga,
        Tayga_Ipv4 as Tayga_Ipv4,
        Tayga_Ipv4_Pool as Tayga_Ipv4_Pool,
        Tayga_Ipv6 as Tayga_Ipv6,
        Tayga_Ipv6_Pool as Tayga_Ipv6_Pool,
    )
    from pynix_os.services.tcsd import Tcsd as Tcsd
    from pynix_os.services.tdarr import (
        Tdarr as Tdarr,
        Tdarr_Nodes_Value as Tdarr_Nodes_Value,
        Tdarr_Nodes_Value_PathTranslators_Item as Tdarr_Nodes_Value_PathTranslators_Item,
        Tdarr_Server as Tdarr_Server,
        Tdarr_Server_Auth as Tdarr_Server_Auth,
    )
    from pynix_os.services.teamspeak3 import Teamspeak3 as Teamspeak3
    from pynix_os.services.teamviewer import Teamviewer as Teamviewer
    from pynix_os.services.technitium_dns_server import TechnitiumDnsServer as TechnitiumDnsServer
    from pynix_os.services.tee_supplicant import TeeSupplicant as TeeSupplicant
    from pynix_os.services.teeworlds import (
        Teeworlds as Teeworlds,
        Teeworlds_Game as Teeworlds_Game,
        Teeworlds_Server as Teeworlds_Server,
    )
    from pynix_os.services.telegraf import Telegraf as Telegraf
    from pynix_os.services.telepathy import Telepathy as Telepathy
    from pynix_os.services.teleport import (
        Teleport as Teleport,
        Teleport_Diag as Teleport_Diag,
        Teleport_Insecure as Teleport_Insecure,
    )
    from pynix_os.services.tempo import Tempo as Tempo
    from pynix_os.services.temporal import Temporal as Temporal, Temporal_Settings as Temporal_Settings
    from pynix_os.services.terraria import Terraria as Terraria
    from pynix_os.services.tetrd import Tetrd as Tetrd
    from pynix_os.services.tftpd import Tftpd as Tftpd
    from pynix_os.services.thanos import (
        Thanos as Thanos,
        Thanos_Compact as Thanos_Compact,
        Thanos_Compact_Compact as Thanos_Compact_Compact,
        Thanos_Compact_Downsampling as Thanos_Compact_Downsampling,
        Thanos_Compact_Log as Thanos_Compact_Log,
        Thanos_Compact_Objstore as Thanos_Compact_Objstore,
        Thanos_Compact_Retention as Thanos_Compact_Retention,
        Thanos_Compact_Tracing as Thanos_Compact_Tracing,
        Thanos_Downsample as Thanos_Downsample,
        Thanos_Downsample_Log as Thanos_Downsample_Log,
        Thanos_Downsample_Objstore as Thanos_Downsample_Objstore,
        Thanos_Downsample_Tracing as Thanos_Downsample_Tracing,
        Thanos_Query as Thanos_Query,
        Thanos_QueryFrontend as Thanos_QueryFrontend,
        Thanos_QueryFrontend_Log as Thanos_QueryFrontend_Log,
        Thanos_QueryFrontend_QueryFrontend as Thanos_QueryFrontend_QueryFrontend,
        Thanos_QueryFrontend_Tracing as Thanos_QueryFrontend_Tracing,
        Thanos_Query_Log as Thanos_Query_Log,
        Thanos_Query_Query as Thanos_Query_Query,
        Thanos_Query_Store as Thanos_Query_Store,
        Thanos_Query_Tracing as Thanos_Query_Tracing,
        Thanos_Query_Web as Thanos_Query_Web,
        Thanos_Receive as Thanos_Receive,
        Thanos_Receive_Log as Thanos_Receive_Log,
        Thanos_Receive_Objstore as Thanos_Receive_Objstore,
        Thanos_Receive_Receive as Thanos_Receive_Receive,
        Thanos_Receive_RemoteWrite as Thanos_Receive_RemoteWrite,
        Thanos_Receive_Tracing as Thanos_Receive_Tracing,
        Thanos_Receive_Tsdb as Thanos_Receive_Tsdb,
        Thanos_Rule as Thanos_Rule,
        Thanos_Rule_Alert as Thanos_Rule_Alert,
        Thanos_Rule_Alertmanagers as Thanos_Rule_Alertmanagers,
        Thanos_Rule_Log as Thanos_Rule_Log,
        Thanos_Rule_Objstore as Thanos_Rule_Objstore,
        Thanos_Rule_Query as Thanos_Rule_Query,
        Thanos_Rule_Tracing as Thanos_Rule_Tracing,
        Thanos_Rule_Tsdb as Thanos_Rule_Tsdb,
        Thanos_Rule_Web as Thanos_Rule_Web,
        Thanos_Sidecar as Thanos_Sidecar,
        Thanos_Sidecar_Log as Thanos_Sidecar_Log,
        Thanos_Sidecar_Objstore as Thanos_Sidecar_Objstore,
        Thanos_Sidecar_Prometheus as Thanos_Sidecar_Prometheus,
        Thanos_Sidecar_Reloader as Thanos_Sidecar_Reloader,
        Thanos_Sidecar_Tracing as Thanos_Sidecar_Tracing,
        Thanos_Sidecar_Tsdb as Thanos_Sidecar_Tsdb,
        Thanos_Store as Thanos_Store,
        Thanos_Store_Log as Thanos_Store_Log,
        Thanos_Store_Objstore as Thanos_Store_Objstore,
        Thanos_Store_Store as Thanos_Store_Store,
        Thanos_Store_Store_Grpc as Thanos_Store_Store_Grpc,
        Thanos_Store_Store_Limits as Thanos_Store_Store_Limits,
        Thanos_Store_Tracing as Thanos_Store_Tracing,
    )
    from pynix_os.services.thelounge import Thelounge as Thelounge
    from pynix_os.services.thermald import Thermald as Thermald
    from pynix_os.services.thinkfan import (
        Thinkfan as Thinkfan,
        Thinkfan_Fans_Item as Thinkfan_Fans_Item,
        Thinkfan_Sensors_Item as Thinkfan_Sensors_Item,
    )
    from pynix_os.services.throttled import Throttled as Throttled
    from pynix_os.services.tiddlywiki import Tiddlywiki as Tiddlywiki
    from pynix_os.services.tigerbeetle import Tigerbeetle as Tigerbeetle
    from pynix_os.services.tika import Tika as Tika
    from pynix_os.services.timekpr import Timekpr as Timekpr
    from pynix_os.services.timesyncd import (
        Timesyncd as Timesyncd,
        Timesyncd_Settings as Timesyncd_Settings,
        Timesyncd_Settings_Time as Timesyncd_Settings_Time,
    )
    from pynix_os.services.tinc import (
        Tinc as Tinc,
        Tinc_Networks_Value as Tinc_Networks_Value,
        Tinc_Networks_Value_HostSettings_Value as Tinc_Networks_Value_HostSettings_Value,
        Tinc_Networks_Value_HostSettings_Value_Addresses_Item as Tinc_Networks_Value_HostSettings_Value_Addresses_Item,
        Tinc_Networks_Value_HostSettings_Value_Settings as Tinc_Networks_Value_HostSettings_Value_Settings,
        Tinc_Networks_Value_HostSettings_Value_Subnets_Item as Tinc_Networks_Value_HostSettings_Value_Subnets_Item,
        Tinc_Networks_Value_Settings as Tinc_Networks_Value_Settings,
    )
    from pynix_os.services.tinyauth import Tinyauth as Tinyauth, Tinyauth_Settings as Tinyauth_Settings
    from pynix_os.services.tinydns import Tinydns as Tinydns
    from pynix_os.services.tinyproxy import Tinyproxy as Tinyproxy, Tinyproxy_Settings as Tinyproxy_Settings
    from pynix_os.services.tlp import Tlp as Tlp, Tlp_Pd as Tlp_Pd
    from pynix_os.services.tlsrpt import (
        Tlsrpt as Tlsrpt,
        Tlsrpt_Collectd as Tlsrpt_Collectd,
        Tlsrpt_Collectd_Settings as Tlsrpt_Collectd_Settings,
        Tlsrpt_Fetcher as Tlsrpt_Fetcher,
        Tlsrpt_Fetcher_Settings as Tlsrpt_Fetcher_Settings,
        Tlsrpt_Reportd as Tlsrpt_Reportd,
        Tlsrpt_Reportd_Settings as Tlsrpt_Reportd_Settings,
    )
    from pynix_os.services.tmate_ssh_server import TmateSshServer as TmateSshServer
    from pynix_os.services.todesk import Todesk as Todesk
    from pynix_os.services.tomcat import (
        Tomcat as Tomcat,
        Tomcat_Axis2 as Tomcat_Axis2,
        Tomcat_VirtualHosts_Item as Tomcat_VirtualHosts_Item,
    )
    from pynix_os.services.tor import (
        Tor as Tor,
        Tor_Client as Tor_Client,
        Tor_Client_Dns as Tor_Client_Dns,
        Tor_Client_OnionServices_Value as Tor_Client_OnionServices_Value,
        Tor_Client_SocksListenAddress_Or as Tor_Client_SocksListenAddress_Or,
        Tor_Client_TransparentProxy as Tor_Client_TransparentProxy,
        Tor_ControlSocket as Tor_ControlSocket,
        Tor_Relay as Tor_Relay,
        Tor_Relay_OnionServices_Value as Tor_Relay_OnionServices_Value,
        Tor_Relay_OnionServices_Value_AuthorizeClient as Tor_Relay_OnionServices_Value_AuthorizeClient,
        Tor_Relay_OnionServices_Value_Map_Item_Or as Tor_Relay_OnionServices_Value_Map_Item_Or,
        Tor_Relay_OnionServices_Value_Map_Item_Or_Target as Tor_Relay_OnionServices_Value_Map_Item_Or_Target,
        Tor_Relay_OnionServices_Value_Settings as Tor_Relay_OnionServices_Value_Settings,
        Tor_Settings as Tor_Settings,
        Tor_Settings_ControlPort_Or_Item_Or as Tor_Settings_ControlPort_Or_Item_Or,
        Tor_Settings_DNSPort_Or as Tor_Settings_DNSPort_Or,
        Tor_Settings_DirPort_Or_Item_Or as Tor_Settings_DirPort_Or_Item_Or,
        Tor_Settings_ExtORPort_Or as Tor_Settings_ExtORPort_Or,
        Tor_Settings_HidServAuth_Item as Tor_Settings_HidServAuth_Item,
        Tor_Settings_ServerTransportPlugin as Tor_Settings_ServerTransportPlugin,
        Tor_Torsocks as Tor_Torsocks,
        Tor_Tsocks as Tor_Tsocks,
    )
    from pynix_os.services.torque import Torque as Torque, Torque_Mom as Torque_Mom, Torque_Server as Torque_Server
    from pynix_os.services.torrentstream import Torrentstream as Torrentstream
    from pynix_os.services.touchegg import Touchegg as Touchegg
    from pynix_os.services.toxBootstrapd import ToxBootstrapd as ToxBootstrapd
    from pynix_os.services.tox_node import ToxNode as ToxNode
    from pynix_os.services.toxvpn import Toxvpn as Toxvpn
    from pynix_os.services.tp_auto_kbbl import TpAutoKbbl as TpAutoKbbl
    from pynix_os.services.traccar import Traccar as Traccar
    from pynix_os.services.traefik import Traefik as Traefik
    from pynix_os.services.trafficserver import (
        Trafficserver as Trafficserver,
        Trafficserver_Plugins_Item as Trafficserver_Plugins_Item,
    )
    from pynix_os.services.tranquil_pds import (
        TranquilPds as TranquilPds,
        TranquilPds_Database as TranquilPds_Database,
        TranquilPds_Settings as TranquilPds_Settings,
    )
    from pynix_os.services.transfer_sh import TransferSh as TransferSh, TransferSh_Settings as TransferSh_Settings
    from pynix_os.services.transmission import (
        Transmission as Transmission,
        Transmission_Settings as Transmission_Settings,
    )
    from pynix_os.services.tremor_rs import TremorRs as TremorRs
    from pynix_os.services.trezord import Trezord as Trezord, Trezord_Emulator as Trezord_Emulator
    from pynix_os.services.trickster import Trickster as Trickster
    from pynix_os.services.triggerhappy import (
        Triggerhappy as Triggerhappy,
        Triggerhappy_Bindings_Item as Triggerhappy_Bindings_Item,
    )
    from pynix_os.services.trilium_server import (
        TriliumServer as TriliumServer,
        TriliumServer_Nginx as TriliumServer_Nginx,
    )
    from pynix_os.services.tsidp import Tsidp as Tsidp, Tsidp_Settings as Tsidp_Settings
    from pynix_os.services.tsmBackup import TsmBackup as TsmBackup
    from pynix_os.services.tt_rss import (
        TtRss as TtRss,
        TtRss_Auth as TtRss_Auth,
        TtRss_Email as TtRss_Email,
        TtRss_PubSubHubbub as TtRss_PubSubHubbub,
        TtRss_Registration as TtRss_Registration,
        TtRss_Sphinx as TtRss_Sphinx,
        TtRss_UpdateDaemon as TtRss_UpdateDaemon,
    )
    from pynix_os.services.tts import Tts as Tts, Tts_Servers_Value as Tts_Servers_Value
    from pynix_os.services.ttyd import Ttyd as Ttyd
    from pynix_os.services.tuliprox import Tuliprox as Tuliprox
    from pynix_os.services.tumbler import Tumbler as Tumbler
    from pynix_os.services.tuned import (
        Tuned as Tuned,
        Tuned_PpdSettings as Tuned_PpdSettings,
        Tuned_PpdSettings_Main as Tuned_PpdSettings_Main,
        Tuned_Profiles_Value as Tuned_Profiles_Value,
        Tuned_Settings as Tuned_Settings,
    )
    from pynix_os.services.tuptime import Tuptime as Tuptime, Tuptime_Timer as Tuptime_Timer
    from pynix_os.services.turborepo_remote_cache import TurborepoRemoteCache as TurborepoRemoteCache
    from pynix_os.services.turn_rs import TurnRs as TurnRs, TurnRs_Settings as TurnRs_Settings
    from pynix_os.services.tusd import Tusd as Tusd
    from pynix_os.services.twingate import Twingate as Twingate
    from pynix_os.services.typesense import Typesense as Typesense, Typesense_Settings as Typesense_Settings
    from pynix_os.services.tzupdate import Tzupdate as Tzupdate, Tzupdate_Timer as Tzupdate_Timer
    from pynix_os.services.u9fs import U9fs as U9fs
    from pynix_os.services.udev import Udev as Udev
    from pynix_os.services.udisks2 import Udisks2 as Udisks2
    from pynix_os.services.udp514_journal import Udp514Journal as Udp514Journal
    from pynix_os.services.udp_over_tcp import (
        UdpOverTcp as UdpOverTcp,
        UdpOverTcp_Tcp2udp_Value as UdpOverTcp_Tcp2udp_Value,
        UdpOverTcp_Udp2tcp_Value as UdpOverTcp_Udp2tcp_Value,
    )
    from pynix_os.services.ulogd import Ulogd as Ulogd
    from pynix_os.services.umami import Umami as Umami, Umami_Settings as Umami_Settings
    from pynix_os.services.umurmur import Umurmur as Umurmur, Umurmur_Settings as Umurmur_Settings
    from pynix_os.services.unbound import Unbound as Unbound, Unbound_Settings as Unbound_Settings
    from pynix_os.services.unclutter import Unclutter as Unclutter
    from pynix_os.services.unclutter_xfixes import UnclutterXfixes as UnclutterXfixes
    from pynix_os.services.undervolt import (
        Undervolt as Undervolt,
        Undervolt_P1 as Undervolt_P1,
        Undervolt_P2 as Undervolt_P2,
    )
    from pynix_os.services.unifi import Unifi as Unifi
    from pynix_os.services.unit import Unit as Unit
    from pynix_os.services.unpackerr import Unpackerr as Unpackerr
    from pynix_os.services.unpoller import (
        Unpoller as Unpoller,
        Unpoller_Influxdb as Unpoller_Influxdb,
        Unpoller_Loki as Unpoller_Loki,
        Unpoller_Poller as Unpoller_Poller,
        Unpoller_Prometheus as Unpoller_Prometheus,
        Unpoller_Unifi as Unpoller_Unifi,
        Unpoller_Unifi_Controllers_Item as Unpoller_Unifi_Controllers_Item,
        Unpoller_Unifi_Defaults as Unpoller_Unifi_Defaults,
    )
    from pynix_os.services.upki import Upki as Upki
    from pynix_os.services.upower import Upower as Upower
    from pynix_os.services.uptermd import Uptermd as Uptermd
    from pynix_os.services.uptime_kuma import UptimeKuma as UptimeKuma, UptimeKuma_Settings as UptimeKuma_Settings
    from pynix_os.services.uptimed import Uptimed as Uptimed
    from pynix_os.services.urserver import Urserver as Urserver
    from pynix_os.services.urxvtd import Urxvtd as Urxvtd
    from pynix_os.services.usbguard import Usbguard as Usbguard, Usbguard_Dbus as Usbguard_Dbus
    from pynix_os.services.usbmuxd import Usbmuxd as Usbmuxd
    from pynix_os.services.usbrelayd import Usbrelayd as Usbrelayd
    from pynix_os.services.userborn import Userborn as Userborn
    from pynix_os.services.userdbd import Userdbd as Userdbd
    from pynix_os.services.ustreamer import Ustreamer as Ustreamer
    from pynix_os.services.uvcvideo import Uvcvideo as Uvcvideo, Uvcvideo_Dynctrl as Uvcvideo_Dynctrl
    from pynix_os.services.uwsgi import Uwsgi as Uwsgi
    from pynix_os.services.v2ray import V2ray as V2ray
    from pynix_os.services.v2raya import V2raya as V2raya
    from pynix_os.services.v4l2_relayd import (
        V4l2Relayd as V4l2Relayd,
        V4l2Relayd_Instances_Value as V4l2Relayd_Instances_Value,
    )
    from pynix_os.services.varnish import Varnish as Varnish, Varnish_Listen_Item as Varnish_Listen_Item
    from pynix_os.services.vault import Vault as Vault
    from pynix_os.services.vault_agent import (
        VaultAgent as VaultAgent,
        VaultAgent_Instances_Value as VaultAgent_Instances_Value,
        VaultAgent_Instances_Value_Settings as VaultAgent_Instances_Value_Settings,
    )
    from pynix_os.services.vaultwarden import Vaultwarden as Vaultwarden
    from pynix_os.services.vdirsyncer import Vdirsyncer as Vdirsyncer, Vdirsyncer_Jobs_Value as Vdirsyncer_Jobs_Value
    from pynix_os.services.vdr import Vdr as Vdr
    from pynix_os.services.vector import Vector as Vector
    from pynix_os.services.veilid import Veilid as Veilid, Veilid_Settings as Veilid_Settings
    from pynix_os.services.victorialogs import Victorialogs as Victorialogs
    from pynix_os.services.victoriametrics import (
        Victoriametrics as Victoriametrics,
        Victoriametrics_PrometheusConfig as Victoriametrics_PrometheusConfig,
    )
    from pynix_os.services.victoriatraces import Victoriatraces as Victoriatraces
    from pynix_os.services.vikunja import Vikunja as Vikunja
    from pynix_os.services.vinyl_cache import VinylCache as VinylCache, VinylCache_Listen_Item as VinylCache_Listen_Item
    from pynix_os.services.vlagent import Vlagent as Vlagent, Vlagent_RemoteWrite as Vlagent_RemoteWrite
    from pynix_os.services.vmagent import (
        Vmagent as Vmagent,
        Vmagent_PrometheusConfig as Vmagent_PrometheusConfig,
        Vmagent_RemoteWrite as Vmagent_RemoteWrite,
    )
    from pynix_os.services.vmalert import (
        Vmalert as Vmalert,
        Vmalert_Instances_Value as Vmalert_Instances_Value,
        Vmalert_Instances_Value_Settings as Vmalert_Instances_Value_Settings,
    )
    from pynix_os.services.vnstat import Vnstat as Vnstat, Vnstat_Settings as Vnstat_Settings
    from pynix_os.services.vsftpd import Vsftpd as Vsftpd
    from pynix_os.services.vsmartcard_vpcd import VsmartcardVpcd as VsmartcardVpcd
    from pynix_os.services.vwifi import (
        Vwifi as Vwifi,
        Vwifi_Client as Vwifi_Client,
        Vwifi_Module as Vwifi_Module,
        Vwifi_Server as Vwifi_Server,
        Vwifi_Server_Ports as Vwifi_Server_Ports,
        Vwifi_Server_Vsock as Vwifi_Server_Vsock,
    )
    from pynix_os.services.waagent import Waagent as Waagent, Waagent_Settings as Waagent_Settings
    from pynix_os.services.wakapi import Wakapi as Wakapi, Wakapi_Database as Wakapi_Database
    from pynix_os.services.warpgate import (
        Warpgate as Warpgate,
        Warpgate_Settings as Warpgate_Settings,
        Warpgate_Settings_HttpSniCertificates_Item as Warpgate_Settings_HttpSniCertificates_Item,
        Warpgate_Settings_SsoProviders_Item as Warpgate_Settings_SsoProviders_Item,
    )
    from pynix_os.services.wasabibackend import (
        Wasabibackend as Wasabibackend,
        Wasabibackend_Endpoint as Wasabibackend_Endpoint,
        Wasabibackend_Rpc as Wasabibackend_Rpc,
    )
    from pynix_os.services.wastebin import Wastebin as Wastebin, Wastebin_Settings as Wastebin_Settings
    from pynix_os.services.watchdogd import Watchdogd as Watchdogd, Watchdogd_Settings as Watchdogd_Settings
    from pynix_os.services.watt import Watt as Watt, Watt_Settings as Watt_Settings
    from pynix_os.services.wealthfolio import Wealthfolio as Wealthfolio
    from pynix_os.services.webdav import Webdav as Webdav
    from pynix_os.services.webdav_server_rs import WebdavServerRs as WebdavServerRs
    from pynix_os.services.webhook import Webhook as Webhook, Webhook_Hooks_Value as Webhook_Hooks_Value
    from pynix_os.services.weblate import Weblate as Weblate, Weblate_Smtp as Weblate_Smtp
    from pynix_os.services.websurfx import Websurfx as Websurfx, Websurfx_Settings as Websurfx_Settings
    from pynix_os.services.weechat import Weechat as Weechat
    from pynix_os.services.wg_access_server import (
        WgAccessServer as WgAccessServer,
        WgAccessServer_Settings as WgAccessServer_Settings,
    )
    from pynix_os.services.wg_netmanager import WgNetmanager as WgNetmanager
    from pynix_os.services.wgautomesh import (
        Wgautomesh as Wgautomesh,
        Wgautomesh_Settings as Wgautomesh_Settings,
        Wgautomesh_Settings_Peers_Item as Wgautomesh_Settings_Peers_Item,
    )
    from pynix_os.services.whisparr import Whisparr as Whisparr, Whisparr_Settings as Whisparr_Settings
    from pynix_os.services.whitebophir import Whitebophir as Whitebophir
    from pynix_os.services.whoami import Whoami as Whoami
    from pynix_os.services.whoogle_search import WhoogleSearch as WhoogleSearch
    from pynix_os.services.wiki_js import WikiJs as WikiJs, WikiJs_Settings as WikiJs_Settings
    from pynix_os.services.windmill import Windmill as Windmill, Windmill_Database as Windmill_Database
    from pynix_os.services.wivrn import Wivrn as Wivrn, Wivrn_Config as Wivrn_Config, Wivrn_Steam as Wivrn_Steam
    from pynix_os.services.wlock import Wlock as Wlock
    from pynix_os.services.woodpecker_agents import (
        WoodpeckerAgents as WoodpeckerAgents,
        WoodpeckerAgents_Agents_Value as WoodpeckerAgents_Agents_Value,
    )
    from pynix_os.services.woodpecker_server import WoodpeckerServer as WoodpeckerServer
    from pynix_os.services.wordpress import (
        Wordpress as Wordpress,
        Wordpress_Sites_Value as Wordpress_Sites_Value,
        Wordpress_Sites_Value_VirtualHost as Wordpress_Sites_Value_VirtualHost,
        Wordpress_Sites_Value_VirtualHost_Listen_Item as Wordpress_Sites_Value_VirtualHost_Listen_Item,
        Wordpress_Sites_Value_VirtualHost_Locations_Value as Wordpress_Sites_Value_VirtualHost_Locations_Value,
    )
    from pynix_os.services.workout_tracker import WorkoutTracker as WorkoutTracker
    from pynix_os.services.writefreely import (
        Writefreely as Writefreely,
        Writefreely_Acme as Writefreely_Acme,
        Writefreely_Admin as Writefreely_Admin,
        Writefreely_Email as Writefreely_Email,
        Writefreely_Nginx as Writefreely_Nginx,
        Writefreely_Settings as Writefreely_Settings,
    )
    from pynix_os.services.wstunnel import (
        Wstunnel as Wstunnel,
        Wstunnel_Clients_Value as Wstunnel_Clients_Value,
        Wstunnel_Clients_Value_Settings as Wstunnel_Clients_Value_Settings,
        Wstunnel_Servers_Value as Wstunnel_Servers_Value,
        Wstunnel_Servers_Value_Listen as Wstunnel_Servers_Value_Listen,
        Wstunnel_Servers_Value_Settings as Wstunnel_Servers_Value_Settings,
        Wstunnel_Servers_Value_Settings_RestrictTo_Item as Wstunnel_Servers_Value_Settings_RestrictTo_Item,
    )
    from pynix_os.services.wyoming import (
        Wyoming as Wyoming,
        Wyoming_FasterWhisper as Wyoming_FasterWhisper,
        Wyoming_FasterWhisper_Servers_Value as Wyoming_FasterWhisper_Servers_Value,
        Wyoming_Openwakeword as Wyoming_Openwakeword,
        Wyoming_Piper as Wyoming_Piper,
        Wyoming_Piper_Servers_Value as Wyoming_Piper_Servers_Value,
        Wyoming_Satellite as Wyoming_Satellite,
        Wyoming_Satellite_Microphone as Wyoming_Satellite_Microphone,
        Wyoming_Satellite_Sound as Wyoming_Satellite_Sound,
        Wyoming_Satellite_Sounds as Wyoming_Satellite_Sounds,
        Wyoming_Satellite_Vad as Wyoming_Satellite_Vad,
    )
    from pynix_os.services.x2goserver import X2goserver as X2goserver, X2goserver_Superenicer as X2goserver_Superenicer
    from pynix_os.services.xandikos import Xandikos as Xandikos, Xandikos_Nginx as Xandikos_Nginx
    from pynix_os.services.xbanish import Xbanish as Xbanish
    from pynix_os.services.xe_guest_utilities import XeGuestUtilities as XeGuestUtilities
    from pynix_os.services.xfs import Xfs as Xfs
    from pynix_os.services.xinetd import Xinetd as Xinetd, Xinetd_Services_Item as Xinetd_Services_Item
    from pynix_os.services.xl2tpd import Xl2tpd as Xl2tpd
    from pynix_os.services.xmrig import Xmrig as Xmrig
    from pynix_os.services.xonotic import Xonotic as Xonotic, Xonotic_Settings as Xonotic_Settings
    from pynix_os.services.xray import Xray as Xray
    from pynix_os.services.xrdp import Xrdp as Xrdp, Xrdp_Audio as Xrdp_Audio
    from pynix_os.services.xscreensaver import Xscreensaver as Services_Xscreensaver
    from pynix_os.services.xserver import (
        Xserver as Xserver,
        Xserver_DesktopManager as Xserver_DesktopManager,
        Xserver_DesktopManager_Cde as Xserver_DesktopManager_Cde,
        Xserver_DesktopManager_Cinnamon as Xserver_DesktopManager_Cinnamon,
        Xserver_DesktopManager_Enlightenment as Xserver_DesktopManager_Enlightenment,
        Xserver_DesktopManager_Kodi as Xserver_DesktopManager_Kodi,
        Xserver_DesktopManager_Lumina as Xserver_DesktopManager_Lumina,
        Xserver_DesktopManager_Lxqt as Xserver_DesktopManager_Lxqt,
        Xserver_DesktopManager_Mate as Xserver_DesktopManager_Mate,
        Xserver_DesktopManager_Phosh as Xserver_DesktopManager_Phosh,
        Xserver_DesktopManager_Phosh_PhocConfig_Or as Xserver_DesktopManager_Phosh_PhocConfig_Or,
        Xserver_DesktopManager_Phosh_PhocConfig_Or_Outputs_Value as Xserver_DesktopManager_Phosh_PhocConfig_Or_Outputs_Value,
        Xserver_DesktopManager_Retroarch as Xserver_DesktopManager_Retroarch,
        Xserver_DesktopManager_SurfDisplay as Xserver_DesktopManager_SurfDisplay,
        Xserver_DesktopManager_Wallpaper as Xserver_DesktopManager_Wallpaper,
        Xserver_DesktopManager_Xfce as Xserver_DesktopManager_Xfce,
        Xserver_DesktopManager_Xterm as Xserver_DesktopManager_Xterm,
        Xserver_Digimend as Xserver_Digimend,
        Xserver_DisplayManager as Xserver_DisplayManager,
        Xserver_DisplayManager_Lightdm as Xserver_DisplayManager_Lightdm,
        Xserver_DisplayManager_Lightdm_AutoLogin as Xserver_DisplayManager_Lightdm_AutoLogin,
        Xserver_DisplayManager_Lightdm_Greeter as Xserver_DisplayManager_Lightdm_Greeter,
        Xserver_DisplayManager_Lightdm_Greeters as Xserver_DisplayManager_Lightdm_Greeters,
        Xserver_DisplayManager_Lightdm_Greeters_Gtk as Xserver_DisplayManager_Lightdm_Greeters_Gtk,
        Xserver_DisplayManager_Lightdm_Greeters_Gtk_CursorTheme as Xserver_DisplayManager_Lightdm_Greeters_Gtk_CursorTheme,
        Xserver_DisplayManager_Lightdm_Greeters_Gtk_IconTheme as Xserver_DisplayManager_Lightdm_Greeters_Gtk_IconTheme,
        Xserver_DisplayManager_Lightdm_Greeters_Gtk_Theme as Xserver_DisplayManager_Lightdm_Greeters_Gtk_Theme,
        Xserver_DisplayManager_Lightdm_Greeters_Lomiri as Xserver_DisplayManager_Lightdm_Greeters_Lomiri,
        Xserver_DisplayManager_Lightdm_Greeters_Mini as Xserver_DisplayManager_Lightdm_Greeters_Mini,
        Xserver_DisplayManager_Lightdm_Greeters_Mobile as Xserver_DisplayManager_Lightdm_Greeters_Mobile,
        Xserver_DisplayManager_Lightdm_Greeters_Pantheon as Xserver_DisplayManager_Lightdm_Greeters_Pantheon,
        Xserver_DisplayManager_Lightdm_Greeters_Slick as Xserver_DisplayManager_Lightdm_Greeters_Slick,
        Xserver_DisplayManager_Lightdm_Greeters_Slick_CursorTheme as Xserver_DisplayManager_Lightdm_Greeters_Slick_CursorTheme,
        Xserver_DisplayManager_Lightdm_Greeters_Slick_Font as Xserver_DisplayManager_Lightdm_Greeters_Slick_Font,
        Xserver_DisplayManager_Lightdm_Greeters_Slick_IconTheme as Xserver_DisplayManager_Lightdm_Greeters_Slick_IconTheme,
        Xserver_DisplayManager_Lightdm_Greeters_Slick_Theme as Xserver_DisplayManager_Lightdm_Greeters_Slick_Theme,
        Xserver_DisplayManager_Lightdm_Greeters_Tiny as Xserver_DisplayManager_Lightdm_Greeters_Tiny,
        Xserver_DisplayManager_Lightdm_Greeters_Tiny_Label as Xserver_DisplayManager_Lightdm_Greeters_Tiny_Label,
        Xserver_DisplayManager_Startx as Xserver_DisplayManager_Startx,
        Xserver_DisplayManager_Sx as Xserver_DisplayManager_Sx,
        Xserver_DisplayManager_Xpra as Xserver_DisplayManager_Xpra,
        Xserver_Imwheel as Xserver_Imwheel,
        Xserver_Synaptics as Xserver_Synaptics,
        Xserver_Wacom as Xserver_Wacom,
        Xserver_WindowManager as Xserver_WindowManager,
        Xserver_WindowManager_Awesome as Xserver_WindowManager_Awesome,
        Xserver_WindowManager_Berry as Xserver_WindowManager_Berry,
        Xserver_WindowManager_Bspwm as Xserver_WindowManager_Bspwm,
        Xserver_WindowManager_Bspwm_Sxhkd as Xserver_WindowManager_Bspwm_Sxhkd,
        Xserver_WindowManager_Clfswm as Xserver_WindowManager_Clfswm,
        Xserver_WindowManager_Cwm as Xserver_WindowManager_Cwm,
        Xserver_WindowManager_Dk as Xserver_WindowManager_Dk,
        Xserver_WindowManager_Dwm as Xserver_WindowManager_Dwm,
        Xserver_WindowManager_E16 as Xserver_WindowManager_E16,
        Xserver_WindowManager_Evilwm as Xserver_WindowManager_Evilwm,
        Xserver_WindowManager_Exwm as Xserver_WindowManager_Exwm,
        Xserver_WindowManager_Fluxbox as Xserver_WindowManager_Fluxbox,
        Xserver_WindowManager_Fvwm2 as Xserver_WindowManager_Fvwm2,
        Xserver_WindowManager_Fvwm3 as Xserver_WindowManager_Fvwm3,
        Xserver_WindowManager_Hackedbox as Xserver_WindowManager_Hackedbox,
        Xserver_WindowManager_Herbstluftwm as Xserver_WindowManager_Herbstluftwm,
        Xserver_WindowManager_Hypr as Xserver_WindowManager_Hypr,
        Xserver_WindowManager_I3 as Xserver_WindowManager_I3,
        Xserver_WindowManager_Icewm as Xserver_WindowManager_Icewm,
        Xserver_WindowManager_Jwm as Xserver_WindowManager_Jwm,
        Xserver_WindowManager_Katriawm as Xserver_WindowManager_Katriawm,
        Xserver_WindowManager_Leftwm as Xserver_WindowManager_Leftwm,
        Xserver_WindowManager_Lwm as Xserver_WindowManager_Lwm,
        Xserver_WindowManager_Metacity as Xserver_WindowManager_Metacity,
        Xserver_WindowManager_Mlvwm as Xserver_WindowManager_Mlvwm,
        Xserver_WindowManager_Mwm as Xserver_WindowManager_Mwm,
        Xserver_WindowManager_N2bwm as Xserver_WindowManager_N2bwm,
        Xserver_WindowManager_Nimdow as Xserver_WindowManager_Nimdow,
        Xserver_WindowManager_Notion as Xserver_WindowManager_Notion,
        Xserver_WindowManager_Openbox as Xserver_WindowManager_Openbox,
        Xserver_WindowManager_Oxwm as Xserver_WindowManager_Oxwm,
        Xserver_WindowManager_Pekwm as Xserver_WindowManager_Pekwm,
        Xserver_WindowManager_Qtile as Xserver_WindowManager_Qtile,
        Xserver_WindowManager_Ratpoison as Xserver_WindowManager_Ratpoison,
        Xserver_WindowManager_Smallwm as Xserver_WindowManager_Smallwm,
        Xserver_WindowManager_Spectrwm as Xserver_WindowManager_Spectrwm,
        Xserver_WindowManager_Stumpwm as Xserver_WindowManager_Stumpwm,
        Xserver_WindowManager_Tinywm as Xserver_WindowManager_Tinywm,
        Xserver_WindowManager_Twm as Xserver_WindowManager_Twm,
        Xserver_WindowManager_Vxwm as Xserver_WindowManager_Vxwm,
        Xserver_WindowManager_Windowlab as Xserver_WindowManager_Windowlab,
        Xserver_WindowManager_Windowmaker as Xserver_WindowManager_Windowmaker,
        Xserver_WindowManager_Wmderland as Xserver_WindowManager_Wmderland,
        Xserver_WindowManager_Wmii as Xserver_WindowManager_Wmii,
        Xserver_WindowManager_Xmonad as Xserver_WindowManager_Xmonad,
        Xserver_Xautolock as Xserver_Xautolock,
        Xserver_Xkb as Xserver_Xkb,
        Xserver_Xkb_ExtraLayouts_Value as Xserver_Xkb_ExtraLayouts_Value,
        Xserver_XrandrHeads_Item as Xserver_XrandrHeads_Item,
    )
    from pynix_os.services.yandex_disk import YandexDisk as YandexDisk
    from pynix_os.services.yarr import Yarr as Yarr
    from pynix_os.services.yggdrasil import Yggdrasil as Yggdrasil, Yggdrasil_Settings as Yggdrasil_Settings
    from pynix_os.services.yggdrasil_jumper import YggdrasilJumper as YggdrasilJumper
    from pynix_os.services.ympd import Ympd as Ympd, Ympd_Mpd as Ympd_Mpd
    from pynix_os.services.your_spotify import YourSpotify as YourSpotify, YourSpotify_Settings as YourSpotify_Settings
    from pynix_os.services.youtrack import (
        Youtrack as Youtrack,
        Youtrack_EnvironmentalParameters as Youtrack_EnvironmentalParameters,
    )
    from pynix_os.services.ytdl_sub import YtdlSub as YtdlSub, YtdlSub_Instances_Value as YtdlSub_Instances_Value
    from pynix_os.services.yubikey_agent import YubikeyAgent as YubikeyAgent
    from pynix_os.services.zabbixAgent import ZabbixAgent as ZabbixAgent, ZabbixAgent_Listen as ZabbixAgent_Listen
    from pynix_os.services.zabbixProxy import ZabbixProxy as ZabbixProxy, ZabbixProxy_Listen as ZabbixProxy_Listen
    from pynix_os.services.zabbixServer import ZabbixServer as ZabbixServer, ZabbixServer_Listen as ZabbixServer_Listen
    from pynix_os.services.zabbixWeb import (
        ZabbixWeb as ZabbixWeb,
        ZabbixWeb_Httpd as ZabbixWeb_Httpd,
        ZabbixWeb_Httpd_VirtualHost as ZabbixWeb_Httpd_VirtualHost,
        ZabbixWeb_Httpd_VirtualHost_Listen_Item as ZabbixWeb_Httpd_VirtualHost_Listen_Item,
        ZabbixWeb_Httpd_VirtualHost_Locations_Value as ZabbixWeb_Httpd_VirtualHost_Locations_Value,
        ZabbixWeb_Nginx as ZabbixWeb_Nginx,
        ZabbixWeb_Nginx_VirtualHost as ZabbixWeb_Nginx_VirtualHost,
        ZabbixWeb_Nginx_VirtualHost_Listen_Item as ZabbixWeb_Nginx_VirtualHost_Listen_Item,
        ZabbixWeb_Nginx_VirtualHost_Locations_Value as ZabbixWeb_Nginx_VirtualHost_Locations_Value,
        ZabbixWeb_Server as ZabbixWeb_Server,
    )
    from pynix_os.services.zammad import (
        Zammad as Zammad,
        Zammad_Database as Zammad_Database,
        Zammad_Nginx as Zammad_Nginx,
        Zammad_Redis as Zammad_Redis,
    )
    from pynix_os.services.zapret import Zapret as Zapret
    from pynix_os.services.zapret2 import (
        Zapret2 as Zapret2,
        Zapret2_Firewall as Zapret2_Firewall,
        Zapret2_Profiles_Value as Zapret2_Profiles_Value,
    )
    from pynix_os.services.zeitgeist import Zeitgeist as Zeitgeist
    from pynix_os.services.zenohd import Zenohd as Zenohd, Zenohd_Settings as Zenohd_Settings
    from pynix_os.services.zerobin import Zerobin as Zerobin
    from pynix_os.services.zerobyte import Zerobyte as Zerobyte, Zerobyte_Settings as Zerobyte_Settings
    from pynix_os.services.zeronet import Zeronet as Zeronet
    from pynix_os.services.zeronsd import (
        Zeronsd as Zeronsd,
        Zeronsd_ServedNetworks_Value as Zeronsd_ServedNetworks_Value,
        Zeronsd_ServedNetworks_Value_Settings as Zeronsd_ServedNetworks_Value_Settings,
    )
    from pynix_os.services.zerotierone import Zerotierone as Zerotierone
    from pynix_os.services.zeyple import Zeyple as Zeyple
    from pynix_os.services.zfs import (
        Zfs as Services_Zfs,
        Zfs_AutoReplication as Zfs_AutoReplication,
        Zfs_AutoScrub as Zfs_AutoScrub,
        Zfs_AutoSnapshot as Zfs_AutoSnapshot,
        Zfs_Trim as Zfs_Trim,
        Zfs_Zed as Zfs_Zed,
    )
    from pynix_os.services.zigbee2mqtt import Zigbee2mqtt as Zigbee2mqtt
    from pynix_os.services.zipline import (
        Zipline as Zipline,
        Zipline_Database as Zipline_Database,
        Zipline_Settings as Zipline_Settings,
    )
    from pynix_os.services.zitadel import Zitadel as Zitadel, Zitadel_Settings as Zitadel_Settings
    from pynix_os.services.znapzend import (
        Znapzend as Znapzend,
        Znapzend_Features as Znapzend_Features,
        Znapzend_Zetup_Value as Znapzend_Zetup_Value,
        Znapzend_Zetup_Value_Destinations_Value as Znapzend_Zetup_Value_Destinations_Value,
    )
    from pynix_os.services.znc import (
        Znc as Znc,
        Znc_ConfOptions as Znc_ConfOptions,
        Znc_ConfOptions_Networks_Value as Znc_ConfOptions_Networks_Value,
    )
    from pynix_os.services.zoneminder import Zoneminder as Zoneminder, Zoneminder_Database as Zoneminder_Database
    from pynix_os.services.zookeeper import Zookeeper as Zookeeper
    from pynix_os.services.zram_generator import (
        ZramGenerator as ZramGenerator,
        ZramGenerator_Settings as ZramGenerator_Settings,
    )
    from pynix_os.services.zrepl import Zrepl as Zrepl, Zrepl_Settings as Zrepl_Settings
    from pynix_os.services.zwave_js import ZwaveJs as ZwaveJs, ZwaveJs_Settings as ZwaveJs_Settings
    from pynix_os.services.zwave_js_ui import ZwaveJsUi as ZwaveJsUi, ZwaveJsUi_Settings as ZwaveJsUi_Settings
    from pynix_os.system.__options__ import (
        System as System,
        System_ActivationScripts_Value_Or as System_ActivationScripts_Value_Or,
        System_Build as System_Build,
        System_Services_Value as System_Services_Value,
        System_Services_Value_ConfigData_Value as System_Services_Value_ConfigData_Value,
        System_Services_Value_NotificationProtocol as System_Services_Value_NotificationProtocol,
        System_Services_Value_Services_Value as System_Services_Value_Services_Value,
        System_Services_Value_SystemdService as System_Services_Value_SystemdService,
        System_Services_Value_SystemdServices_Value as System_Services_Value_SystemdServices_Value,
        System_UserActivationScripts_Value_Or as System_UserActivationScripts_Value_Or,
    )
    from pynix_os.system.autoUpgrade import (
        AutoUpgrade as AutoUpgrade,
        AutoUpgrade_RebootWindow as AutoUpgrade_RebootWindow,
    )
    from pynix_os.system.boot import (
        Boot_ExtraInitrd as Boot_ExtraInitrd,
        Boot_Loader as Boot_Loader,
        Boot as System_Boot,
    )
    from pynix_os.system.etc import Etc as Etc, Etc_Overlay as Etc_Overlay
    from pynix_os.system.image import Image as System_Image
    from pynix_os.system.nixos import Nixos as System_Nixos
    from pynix_os.system.nixos_generate_config import NixosGenerateConfig as NixosGenerateConfig
    from pynix_os.system.nixos_init import NixosInit as NixosInit
    from pynix_os.system.nssDatabases import NssDatabases as NssDatabases
    from pynix_os.system.replaceDependencies import (
        ReplaceDependencies as ReplaceDependencies,
        ReplaceDependencies_Replacements_Item as ReplaceDependencies_Replacements_Item,
    )
    from pynix_os.system.switch import Switch as Switch
    from pynix_os.system.tools import (
        Tools as Tools,
        Tools_NixosBuildVms as Tools_NixosBuildVms,
        Tools_NixosEnter as Tools_NixosEnter,
        Tools_NixosGenerateConfig as Tools_NixosGenerateConfig,
        Tools_NixosInstall as Tools_NixosInstall,
        Tools_NixosOption as Tools_NixosOption,
        Tools_NixosRebuild as Tools_NixosRebuild,
        Tools_NixosVersion as Tools_NixosVersion,
    )
    from pynix_os.systemd.__options__ import (
        Systemd as Systemd,
        Systemd_Automounts_Item as Systemd_Automounts_Item,
        Systemd_Mounts_Item as Systemd_Mounts_Item,
        Systemd_Nspawn_Value as Systemd_Nspawn_Value,
        Systemd_Paths_Value as Systemd_Paths_Value,
        Systemd_Services_Value as Systemd_Services_Value,
        Systemd_Slices_Value as Systemd_Slices_Value,
        Systemd_Sockets_Value as Systemd_Sockets_Value,
        Systemd_Targets_Value as Systemd_Targets_Value,
        Systemd_Timers_Value as Systemd_Timers_Value,
        Systemd_Units_Value as Systemd_Units_Value,
    )
    from pynix_os.systemd.coredump import (
        Coredump as Coredump,
        Coredump_Settings as Coredump_Settings,
        Coredump_Settings_Coredump as Coredump_Settings_Coredump,
    )
    from pynix_os.systemd.network import (
        Network as Network,
        Network_Config as Network_Config,
        Network_Links_Value as Network_Links_Value,
        Network_Netdevs_Value as Network_Netdevs_Value,
        Network_Networks_Value as Network_Networks_Value,
        Network_Units_Value as Network_Units_Value,
        Network_WaitOnline as Network_WaitOnline,
    )
    from pynix_os.systemd.oomd import (
        Oomd as Oomd,
        Oomd_Settings as Oomd_Settings,
        Oomd_Settings_OOM as Oomd_Settings_OOM,
    )
    from pynix_os.systemd.repart import Repart as Repart
    from pynix_os.systemd.settings import Settings as Settings, Settings_Manager as Settings_Manager
    from pynix_os.systemd.shutdownRamfs import (
        ShutdownRamfs as ShutdownRamfs,
        ShutdownRamfs_Contents_Value as ShutdownRamfs_Contents_Value,
        ShutdownRamfs_Shell as ShutdownRamfs_Shell,
        ShutdownRamfs_StorePaths_Item as ShutdownRamfs_StorePaths_Item,
    )
    from pynix_os.systemd.sleep import (
        Sleep as Sleep,
        Sleep_Settings as Sleep_Settings,
        Sleep_Settings_Sleep as Sleep_Settings_Sleep,
    )
    from pynix_os.systemd.sysupdate import Sysupdate as Sysupdate, Sysupdate_Reboot as Sysupdate_Reboot
    from pynix_os.systemd.sysusers import Sysusers as Sysusers
    from pynix_os.systemd.tmpfiles import (
        Tmpfiles as Tmpfiles,
        Tmpfiles_Settings_Value_Value_Value as Tmpfiles_Settings_Value_Value_Value,
    )
    from pynix_os.systemd.tpm2 import Tpm2 as Systemd_Tpm2, Tpm2_Pcrphases as Tpm2_Pcrphases
    from pynix_os.systemd.user import (
        User as User,
        User_Paths_Value as User_Paths_Value,
        User_Services_Value as User_Services_Value,
        User_Settings as User_Settings,
        User_Settings_Manager as User_Settings_Manager,
        User_Slices_Value as User_Slices_Value,
        User_Sockets_Value as User_Sockets_Value,
        User_Targets_Value as User_Targets_Value,
        User_Timers_Value as User_Timers_Value,
        User_Tmpfiles as User_Tmpfiles,
        User_Tmpfiles_Users_Value as User_Tmpfiles_Users_Value,
        User_Units_Value as User_Units_Value,
    )
    from pynix_os.time.__options__ import Time as Time
    from pynix_os.top import (
        Top as Top,
        Top_Containers_Value as Top_Containers_Value,
        Top_Containers_Value_AllowedDevices_Item as Top_Containers_Value_AllowedDevices_Item,
        Top_Containers_Value_BindMounts_Value as Top_Containers_Value_BindMounts_Value,
        Top_Containers_Value_ExtraVeths_Value as Top_Containers_Value_ExtraVeths_Value,
        Top_Containers_Value_ForwardPorts_Item as Top_Containers_Value_ForwardPorts_Item,
        Top_FileSystems_Value as Top_FileSystems_Value,
        Top_Specialisation_Value as Top_Specialisation_Value,
        Top_SwapDevices_Item as Top_SwapDevices_Item,
        Top_SwapDevices_Item_RandomEncryption as Top_SwapDevices_Item_RandomEncryption,
    )
    from pynix_os.users.__options__ import (
        Users as Users,
        Users_ExtraGroups_Value as Users_ExtraGroups_Value,
        Users_ExtraUsers_Value as Users_ExtraUsers_Value,
        Users_ExtraUsers_Value_SubGidRanges_Item as Users_ExtraUsers_Value_SubGidRanges_Item,
        Users_ExtraUsers_Value_SubUidRanges_Item as Users_ExtraUsers_Value_SubUidRanges_Item,
        Users_Groups_Value as Users_Groups_Value,
        Users_Users_Value as Users_Users_Value,
    )
    from pynix_os.users.ldap import Ldap as Ldap, Ldap_Bind as Ldap_Bind, Ldap_Daemon as Ldap_Daemon
    from pynix_os.users.mysql import Mysql_Nss as Mysql_Nss, Mysql_Pam as Mysql_Pam, Mysql as Users_Mysql
    from pynix_os.virtualisation.__options__ import Virtualisation as Virtualisation
    from pynix_os.virtualisation.appvm import Appvm as Appvm
    from pynix_os.virtualisation.containerd import Containerd as Containerd
    from pynix_os.virtualisation.containers import (
        Containers as Containers,
        Containers_ContainersConf as Containers_ContainersConf,
        Containers_OciSeccompBpfHook as Containers_OciSeccompBpfHook,
        Containers_Registries as Containers_Registries,
        Containers_Storage as Containers_Storage,
    )
    from pynix_os.virtualisation.cri_o import CriO as CriO
    from pynix_os.virtualisation.docker import (
        Docker as Docker,
        Docker_AutoPrune as Docker_AutoPrune,
        Docker_AutoPrune_AllVolumes as Docker_AutoPrune_AllVolumes,
        Docker_Daemon as Docker_Daemon,
        Docker_Daemon_Settings as Docker_Daemon_Settings,
        Docker_LiveRestore as Docker_LiveRestore,
        Docker_Rootless as Docker_Rootless,
        Docker_Rootless_Daemon as Docker_Rootless_Daemon,
    )
    from pynix_os.virtualisation.hypervGuest import HypervGuest as HypervGuest
    from pynix_os.virtualisation.incus import (
        Incus as Incus,
        Incus_Agent as Incus_Agent,
        Incus_Preseed as Incus_Preseed,
        Incus_Storage as Incus_Storage,
        Incus_Storage_Truenas as Incus_Storage_Truenas,
        Incus_Ui as Incus_Ui,
    )
    from pynix_os.virtualisation.kvmgt import Kvmgt as Kvmgt, Kvmgt_Vgpus_Value as Kvmgt_Vgpus_Value
    from pynix_os.virtualisation.libvirtd import (
        Libvirtd_Dbus as Libvirtd_Dbus,
        Libvirtd_Hooks as Libvirtd_Hooks,
        Libvirtd_Nss as Libvirtd_Nss,
        Libvirtd_Qemu as Libvirtd_Qemu,
        Libvirtd_Qemu_Ovmf as Libvirtd_Qemu_Ovmf,
        Libvirtd_Qemu_Swtpm as Libvirtd_Qemu_Swtpm,
        Libvirtd as Virtualisation_Libvirtd,
    )
    from pynix_os.virtualisation.lxc import Lxc as Lxc, Lxc_Lxcfs as Lxc_Lxcfs
    from pynix_os.virtualisation.oci_containers import (
        OciContainers as OciContainers,
        OciContainers_Containers_Value as OciContainers_Containers_Value,
        OciContainers_Containers_Value_Podman as OciContainers_Containers_Value_Podman,
    )
    from pynix_os.virtualisation.podman import (
        Podman as Podman,
        Podman_AutoPrune as Podman_AutoPrune,
        Podman_DefaultNetwork as Podman_DefaultNetwork,
        Podman_DockerSocket as Podman_DockerSocket,
        Podman_NetworkSocket as Podman_NetworkSocket,
        Podman_NetworkSocket_Tls as Podman_NetworkSocket_Tls,
    )
    from pynix_os.virtualisation.qemu import Qemu as Qemu, Qemu_Firmware as Qemu_Firmware
    from pynix_os.virtualisation.rosetta import Rosetta as Rosetta
    from pynix_os.virtualisation.spiceUSBRedirection import SpiceUSBRedirection as SpiceUSBRedirection
    from pynix_os.virtualisation.virtualbox import (
        Virtualbox as Virtualbox,
        Virtualbox_Guest as Virtualbox_Guest,
        Virtualbox_Host as Virtualbox_Host,
    )
    from pynix_os.virtualisation.vmware import (
        Vmware as Vmware,
        Vmware_Guest as Vmware_Guest,
        Vmware_Host as Vmware_Host,
    )
    from pynix_os.virtualisation.vswitch import Vswitch as Vswitch
    from pynix_os.virtualisation.waydroid import Waydroid as Waydroid
    from pynix_os.virtualisation.xen import (
        Xen as Xen,
        Xen_Boot as Xen_Boot,
        Xen_Boot_Bios as Xen_Boot_Bios,
        Xen_Boot_Efi as Xen_Boot_Efi,
        Xen_Dom0Resources as Xen_Dom0Resources,
        Xen_Domains as Xen_Domains,
        Xen_Qemu as Xen_Qemu,
    )
    from pynix_os.xdg.autostart import Autostart as Autostart
    from pynix_os.xdg.icons import Icons as Icons
    from pynix_os.xdg.menus import Menus as Menus
    from pynix_os.xdg.mime import Mime as Mime
    from pynix_os.xdg.portal import (
        Portal as Portal,
        Portal_Lxqt as Portal_Lxqt,
        Portal_Wlr as Portal_Wlr,
        Portal_Wlr_Settings as Portal_Wlr_Settings,
    )
    from pynix_os.xdg.sounds import Sounds as Sounds
    from pynix_os.xdg.terminal_exec import TerminalExec as TerminalExec
    from pynix_os.zramSwap.__options__ import ZramSwap as ZramSwap
else:
    _INDEX = {
        "A2boot": "pynix_os.services.a2boot:A2boot",
        "AccountUtils": "pynix_os.security.account_utils:AccountUtils",
        "AccountUtils_Pwaccessd": "pynix_os.security.account_utils:AccountUtils_Pwaccessd",
        "AccountUtils_Pwaccessd_Settings": "pynix_os.security.account_utils:AccountUtils_Pwaccessd_Settings",
        "AccountsDaemon": "pynix_os.services.accounts_daemon:AccountsDaemon",
        "Acme": "pynix_os.security.acme:Acme",
        "AcmeDns": "pynix_os.services.acme_dns:AcmeDns",
        "AcmeDns_Settings": "pynix_os.services.acme_dns:AcmeDns_Settings",
        "Acme_Certs_Value": "pynix_os.security.acme:Acme_Certs_Value",
        "Acme_Defaults": "pynix_os.security.acme:Acme_Defaults",
        "Acpid": "pynix_os.services.acpid:Acpid",
        "Acpid_Handlers_Value": "pynix_os.services.acpid:Acpid_Handlers_Value",
        "Acpilight": "pynix_os.hardware.acpilight:Acpilight",
        "Activemq": "pynix_os.services.activemq:Activemq",
        "Actkbd": "pynix_os.services.actkbd:Actkbd",
        "Actkbd_Bindings_Item": "pynix_os.services.actkbd:Actkbd_Bindings_Item",
        "Actual": "pynix_os.services.actual:Actual",
        "Actual_Settings": "pynix_os.services.actual:Actual_Settings",
        "Adguardhome": "pynix_os.services.adguardhome:Adguardhome",
        "Adguardhome_Settings": "pynix_os.services.adguardhome:Adguardhome_Settings",
        "AdwBluetooth": "pynix_os.services.adw_bluetooth:AdwBluetooth",
        "Aerospike": "pynix_os.services.aerospike:Aerospike",
        "Aesmd": "pynix_os.services.aesmd:Aesmd",
        "Aesmd_Settings": "pynix_os.services.aesmd:Aesmd_Settings",
        "Agate": "pynix_os.services.agate:Agate",
        "Agnos": "pynix_os.security.agnos:Agnos",
        "Agnos_GenerateKeys": "pynix_os.security.agnos:Agnos_GenerateKeys",
        "Agnos_Settings": "pynix_os.security.agnos:Agnos_Settings",
        "Agnos_Settings_Accounts_Item": "pynix_os.security.agnos:Agnos_Settings_Accounts_Item",
        "Agnos_Settings_Accounts_Item_Certificates_Item": "pynix_os.security.agnos:Agnos_Settings_Accounts_Item_Certificates_Item",
        "Agorakit": "pynix_os.services.agorakit:Agorakit",
        "Agorakit_Config_Value_Or": "pynix_os.services.agorakit:Agorakit_Config_Value_Or",
        "Agorakit_Database": "pynix_os.services.agorakit:Agorakit_Database",
        "Agorakit_Mail": "pynix_os.services.agorakit:Agorakit_Mail",
        "Agorakit_Nginx": "pynix_os.services.agorakit:Agorakit_Nginx",
        "Agorakit_Nginx_Listen_Item": "pynix_os.services.agorakit:Agorakit_Nginx_Listen_Item",
        "Agorakit_Nginx_Locations_Value": "pynix_os.services.agorakit:Agorakit_Nginx_Locations_Value",
        "Airsonic": "pynix_os.services.airsonic:Airsonic",
        "Akkoma": "pynix_os.services.akkoma:Akkoma",
        "Akkoma_Config": "pynix_os.services.akkoma:Akkoma_Config",
        "Akkoma_Config_NWebPushEncryption": "pynix_os.services.akkoma:Akkoma_Config_NWebPushEncryption",
        "Akkoma_Dist": "pynix_os.services.akkoma:Akkoma_Dist",
        "Akkoma_Frontends_Value": "pynix_os.services.akkoma:Akkoma_Frontends_Value",
        "Akkoma_InitDb": "pynix_os.services.akkoma:Akkoma_InitDb",
        "Akkoma_Nginx": "pynix_os.services.akkoma:Akkoma_Nginx",
        "Akkoma_Nginx_Listen_Item": "pynix_os.services.akkoma:Akkoma_Nginx_Listen_Item",
        "Akkoma_Nginx_Locations_Value": "pynix_os.services.akkoma:Akkoma_Nginx_Locations_Value",
        "Alerta": "pynix_os.services.alerta:Alerta",
        "AliceLg": "pynix_os.services.alice_lg:AliceLg",
        "Alloy": "pynix_os.services.alloy:Alloy",
        "Alps": "pynix_os.services.alps:Alps",
        "Alps_Settings": "pynix_os.services.alps:Alps_Settings",
        "Alsa": "pynix_os.hardware.alsa:Alsa",
        "Alsa_CardAliases_Value": "pynix_os.hardware.alsa:Alsa_CardAliases_Value",
        "Alsa_Controls_Value": "pynix_os.hardware.alsa:Alsa_Controls_Value",
        "Alsa_DefaultDevice": "pynix_os.hardware.alsa:Alsa_DefaultDevice",
        "Alvr": "pynix_os.programs.alvr:Alvr",
        "AmazonCloudwatchAgent": "pynix_os.services.amazon_cloudwatch_agent:AmazonCloudwatchAgent",
        "AmazonSsmAgent": "pynix_os.services.amazon_ssm_agent:AmazonSsmAgent",
        "Amdgpu": "pynix_os.hardware.amdgpu:Amdgpu",
        "Amdgpu_Initrd": "pynix_os.hardware.amdgpu:Amdgpu_Initrd",
        "Amdgpu_LegacySupport": "pynix_os.hardware.amdgpu:Amdgpu_LegacySupport",
        "Amdgpu_Opencl": "pynix_os.hardware.amdgpu:Amdgpu_Opencl",
        "Amdgpu_Overdrive": "pynix_os.hardware.amdgpu:Amdgpu_Overdrive",
        "Amdgpu_Zluda": "pynix_os.hardware.amdgpu:Amdgpu_Zluda",
        "AmneziaVpn": "pynix_os.programs.amnezia_vpn:AmneziaVpn",
        "Amule": "pynix_os.services.amule:Amule",
        "Amule_Settings": "pynix_os.services.amule:Amule_Settings",
        "Ananicy": "pynix_os.services.ananicy:Ananicy",
        "Angrr": "pynix_os.services.angrr:Angrr",
        "Angrr_Settings": "pynix_os.services.angrr:Angrr_Settings",
        "Angrr_Settings_ProfilePolicies_Value": "pynix_os.services.angrr:Angrr_Settings_ProfilePolicies_Value",
        "Angrr_Settings_ProfilePolicies_Value_KeepNPerBucket_Item": "pynix_os.services.angrr:Angrr_Settings_ProfilePolicies_Value_KeepNPerBucket_Item",
        "Angrr_Settings_TemporaryRootPolicies_Value": "pynix_os.services.angrr:Angrr_Settings_TemporaryRootPolicies_Value",
        "Angrr_Settings_TemporaryRootPolicies_Value_Filter": "pynix_os.services.angrr:Angrr_Settings_TemporaryRootPolicies_Value_Filter",
        "Angrr_Timer": "pynix_os.services.angrr:Angrr_Timer",
        "AnkiSyncServer": "pynix_os.services.anki_sync_server:AnkiSyncServer",
        "AnkiSyncServer_Users_Item": "pynix_os.services.anki_sync_server:AnkiSyncServer_Users_Item",
        "Anubis": "pynix_os.services.anubis:Anubis",
        "Anubis_DefaultOptions": "pynix_os.services.anubis:Anubis_DefaultOptions",
        "Anubis_DefaultOptions_Policy": "pynix_os.services.anubis:Anubis_DefaultOptions_Policy",
        "Anubis_DefaultOptions_Settings": "pynix_os.services.anubis:Anubis_DefaultOptions_Settings",
        "Anubis_Instances_Value": "pynix_os.services.anubis:Anubis_Instances_Value",
        "Anubis_Instances_Value_Policy": "pynix_os.services.anubis:Anubis_Instances_Value_Policy",
        "Anubis_Instances_Value_Settings": "pynix_os.services.anubis:Anubis_Instances_Value_Settings",
        "AnukoTimeTracker": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker",
        "AnukoTimeTracker_Database": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker_Database",
        "AnukoTimeTracker_Nginx": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker_Nginx",
        "AnukoTimeTracker_Nginx_Listen_Item": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker_Nginx_Listen_Item",
        "AnukoTimeTracker_Nginx_Locations_Value": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker_Nginx_Locations_Value",
        "AnukoTimeTracker_Settings": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker_Settings",
        "AnukoTimeTracker_Settings_Email": "pynix_os.services.anuko_time_tracker:AnukoTimeTracker_Settings_Email",
        "ApacheKafka": "pynix_os.services.apache_kafka:ApacheKafka",
        "ApacheKafka_ConfigFiles": "pynix_os.services.apache_kafka:ApacheKafka_ConfigFiles",
        "ApacheKafka_Settings": "pynix_os.services.apache_kafka:ApacheKafka_Settings",
        "Apcupsd": "pynix_os.services.apcupsd:Apcupsd",
        "Apparmor": "pynix_os.security.apparmor:Apparmor",
        "Apparmor_Policies_Value": "pynix_os.security.apparmor:Apparmor_Policies_Value",
        "AppgateSdp": "pynix_os.programs.appgate_sdp:AppgateSdp",
        "Appimage": "pynix_os.programs.appimage:Appimage",
        "Apple": "pynix_os.hardware.apple:Apple",
        "Apple_TouchBar": "pynix_os.hardware.apple:Apple_TouchBar",
        "Appstream": "pynix_os.appstream.__options__:Appstream",
        "Appvm": "pynix_os.virtualisation.appvm:Appvm",
        "Arbtt": "pynix_os.services.arbtt:Arbtt",
        "Archisteamfarm": "pynix_os.services.archisteamfarm:Archisteamfarm",
        "Archisteamfarm_Bots_Value": "pynix_os.services.archisteamfarm:Archisteamfarm_Bots_Value",
        "Archisteamfarm_WebUi": "pynix_os.services.archisteamfarm:Archisteamfarm_WebUi",
        "Aria2": "pynix_os.services.aria2:Aria2",
        "Aria2_Settings": "pynix_os.services.aria2:Aria2_Settings",
        "Armagetronad": "pynix_os.services.armagetronad:Armagetronad",
        "Armagetronad_Servers_Value": "pynix_os.services.armagetronad:Armagetronad_Servers_Value",
        "ArpScan": "pynix_os.programs.arp_scan:ArpScan",
        "Arsenik": "pynix_os.services.arsenik:Arsenik",
        "Artalk": "pynix_os.services.artalk:Artalk",
        "Artalk_Settings": "pynix_os.services.artalk:Artalk_Settings",
        "Asterisk": "pynix_os.services.asterisk:Asterisk",
        "Asusd": "pynix_os.services.asusd:Asusd",
        "Asusd_AnimeConfig": "pynix_os.services.asusd:Asusd_AnimeConfig",
        "Atalkd": "pynix_os.services.atalkd:Atalkd",
        "Atalkd_Interfaces_Value": "pynix_os.services.atalkd:Atalkd_Interfaces_Value",
        "Atd": "pynix_os.services.atd:Atd",
        "Atftpd": "pynix_os.services.atftpd:Atftpd",
        "Athens": "pynix_os.services.athens:Athens",
        "Athens_Index": "pynix_os.services.athens:Athens_Index",
        "Athens_Index_Mysql": "pynix_os.services.athens:Athens_Index_Mysql",
        "Athens_Index_Mysql_Params": "pynix_os.services.athens:Athens_Index_Mysql_Params",
        "Athens_Index_Postgres": "pynix_os.services.athens:Athens_Index_Postgres",
        "Athens_Index_Postgres_Params": "pynix_os.services.athens:Athens_Index_Postgres_Params",
        "Athens_SingleFlight": "pynix_os.services.athens:Athens_SingleFlight",
        "Athens_SingleFlight_Etcd": "pynix_os.services.athens:Athens_SingleFlight_Etcd",
        "Athens_SingleFlight_Redis": "pynix_os.services.athens:Athens_SingleFlight_Redis",
        "Athens_SingleFlight_RedisSentinel": "pynix_os.services.athens:Athens_SingleFlight_RedisSentinel",
        "Athens_SingleFlight_RedisSentinel_LockConfig": "pynix_os.services.athens:Athens_SingleFlight_RedisSentinel_LockConfig",
        "Athens_SingleFlight_Redis_LockConfig": "pynix_os.services.athens:Athens_SingleFlight_Redis_LockConfig",
        "Athens_Storage": "pynix_os.services.athens:Athens_Storage",
        "Athens_Storage_Azureblob": "pynix_os.services.athens:Athens_Storage_Azureblob",
        "Athens_Storage_Cdn": "pynix_os.services.athens:Athens_Storage_Cdn",
        "Athens_Storage_Disk": "pynix_os.services.athens:Athens_Storage_Disk",
        "Athens_Storage_External": "pynix_os.services.athens:Athens_Storage_External",
        "Athens_Storage_Gcp": "pynix_os.services.athens:Athens_Storage_Gcp",
        "Athens_Storage_Mongo": "pynix_os.services.athens:Athens_Storage_Mongo",
        "Athens_Storage_S3": "pynix_os.services.athens:Athens_Storage_S3",
        "Atop": "pynix_os.programs.atop:Atop",
        "Atop_AtopRotateTimer": "pynix_os.programs.atop:Atop_AtopRotateTimer",
        "Atop_AtopService": "pynix_os.programs.atop:Atop_AtopService",
        "Atop_AtopacctService": "pynix_os.programs.atop:Atop_AtopacctService",
        "Atop_Atopgpu": "pynix_os.programs.atop:Atop_Atopgpu",
        "Atop_Netatop": "pynix_os.programs.atop:Atop_Netatop",
        "Atop_SetuidWrapper": "pynix_os.programs.atop:Atop_SetuidWrapper",
        "Atticd": "pynix_os.services.atticd:Atticd",
        "Programs_Atuin": "pynix_os.programs.atuin:Atuin",
        "Services_Atuin": "pynix_os.services.atuin:Atuin",
        "Atuin_Daemon": "pynix_os.programs.atuin:Atuin_Daemon",
        "Atuin_Database": "pynix_os.services.atuin:Atuin_Database",
        "Audiobookshelf": "pynix_os.services.audiobookshelf:Audiobookshelf",
        "Audit": "pynix_os.security.audit:Audit",
        "Auditd": "pynix_os.security.auditd:Auditd",
        "Auditd_Plugins_Value": "pynix_os.security.auditd:Auditd_Plugins_Value",
        "Auditd_Plugins_Value_Settings": "pynix_os.security.auditd:Auditd_Plugins_Value_Settings",
        "Auditd_Settings": "pynix_os.security.auditd:Auditd_Settings",
        "Aurral": "pynix_os.services.aurral:Aurral",
        "Ausweisapp": "pynix_os.programs.ausweisapp:Ausweisapp",
        "Authelia": "pynix_os.services.authelia:Authelia",
        "Authelia_Instances_Value": "pynix_os.services.authelia:Authelia_Instances_Value",
        "Authelia_Instances_Value_Secrets": "pynix_os.services.authelia:Authelia_Instances_Value_Secrets",
        "Authelia_Instances_Value_Settings": "pynix_os.services.authelia:Authelia_Instances_Value_Settings",
        "AutoCpufreq": "pynix_os.services.auto_cpufreq:AutoCpufreq",
        "AutoCpufreq_Settings": "pynix_os.services.auto_cpufreq:AutoCpufreq_Settings",
        "AutoEpp": "pynix_os.services.auto_epp:AutoEpp",
        "AutoEpp_Settings": "pynix_os.services.auto_epp:AutoEpp_Settings",
        "AutoUpgrade": "pynix_os.system.autoUpgrade:AutoUpgrade",
        "AutoUpgrade_RebootWindow": "pynix_os.system.autoUpgrade:AutoUpgrade_RebootWindow",
        "Autobrr": "pynix_os.services.autobrr:Autobrr",
        "Autobrr_Settings": "pynix_os.services.autobrr:Autobrr_Settings",
        "Autoenv": "pynix_os.programs.autoenv:Autoenv",
        "Autofs": "pynix_os.services.autofs:Autofs",
        "Autojump": "pynix_os.programs.autojump:Autojump",
        "AutomaticTimezoned": "pynix_os.services.automatic_timezoned:AutomaticTimezoned",
        "Automx2": "pynix_os.services.automx2:Automx2",
        "Automysqlbackup": "pynix_os.services.automysqlbackup:Automysqlbackup",
        "Autorandr": "pynix_os.services.autorandr:Autorandr",
        "Autorandr_Hooks": "pynix_os.services.autorandr:Autorandr_Hooks",
        "Autorandr_Profiles_Value": "pynix_os.services.autorandr:Autorandr_Profiles_Value",
        "Autorandr_Profiles_Value_Config_Value": "pynix_os.services.autorandr:Autorandr_Profiles_Value_Config_Value",
        "Autorandr_Profiles_Value_Config_Value_Scale": "pynix_os.services.autorandr:Autorandr_Profiles_Value_Config_Value_Scale",
        "Autossh": "pynix_os.services.autossh:Autossh",
        "AutosshNg": "pynix_os.services.autossh_ng:AutosshNg",
        "AutosshNg_Sessions_Value": "pynix_os.services.autossh_ng:AutosshNg_Sessions_Value",
        "Autossh_Sessions_Item": "pynix_os.services.autossh:Autossh_Sessions_Item",
        "Autostart": "pynix_os.xdg.autostart:Autostart",
        "Autosuspend": "pynix_os.services.autosuspend:Autosuspend",
        "Autosuspend_Checks_Value": "pynix_os.services.autosuspend:Autosuspend_Checks_Value",
        "Autosuspend_Settings": "pynix_os.services.autosuspend:Autosuspend_Settings",
        "Autosuspend_Wakeups_Value": "pynix_os.services.autosuspend:Autosuspend_Wakeups_Value",
        "Autotierfs": "pynix_os.services.autotierfs:Autotierfs",
        "Autotierfs_Settings": "pynix_os.services.autotierfs:Autotierfs_Settings",
        "Avahi": "pynix_os.services.avahi:Avahi",
        "Avahi_Publish": "pynix_os.services.avahi:Avahi_Publish",
        "Awstats": "pynix_os.services.awstats:Awstats",
        "Awstats_Configs_Value": "pynix_os.services.awstats:Awstats_Configs_Value",
        "Ax25": "pynix_os.services.ax25:Ax25",
        "Ax25_Axlisten": "pynix_os.services.ax25:Ax25_Axlisten",
        "Ax25_Axports_Value": "pynix_os.services.ax25:Ax25_Axports_Value",
        "AyatanaIndicators": "pynix_os.services.ayatana_indicators:AyatanaIndicators",
        "Babeld": "pynix_os.services.babeld:Babeld",
        "BaculaDir": "pynix_os.services.bacula_dir:BaculaDir",
        "BaculaDir_Tls": "pynix_os.services.bacula_dir:BaculaDir_Tls",
        "BaculaFd": "pynix_os.services.bacula_fd:BaculaFd",
        "BaculaFd_Director_Value": "pynix_os.services.bacula_fd:BaculaFd_Director_Value",
        "BaculaFd_Director_Value_Tls": "pynix_os.services.bacula_fd:BaculaFd_Director_Value_Tls",
        "BaculaFd_Tls": "pynix_os.services.bacula_fd:BaculaFd_Tls",
        "BaculaSd": "pynix_os.services.bacula_sd:BaculaSd",
        "BaculaSd_Autochanger_Value": "pynix_os.services.bacula_sd:BaculaSd_Autochanger_Value",
        "BaculaSd_Device_Value": "pynix_os.services.bacula_sd:BaculaSd_Device_Value",
        "BaculaSd_Director_Value": "pynix_os.services.bacula_sd:BaculaSd_Director_Value",
        "BaculaSd_Director_Value_Tls": "pynix_os.services.bacula_sd:BaculaSd_Director_Value_Tls",
        "BaculaSd_Tls": "pynix_os.services.bacula_sd:BaculaSd_Tls",
        "Baikal": "pynix_os.services.baikal:Baikal",
        "Bamf": "pynix_os.services.bamf:Bamf",
        "Bandwhich": "pynix_os.programs.bandwhich:Bandwhich",
        "Bash": "pynix_os.programs.bash:Bash",
        "BashMyAws": "pynix_os.programs.bash_my_aws:BashMyAws",
        "Bash_Blesh": "pynix_os.programs.bash:Bash_Blesh",
        "Bash_Completion": "pynix_os.programs.bash:Bash_Completion",
        "Bash_UndistractMe": "pynix_os.programs.bash:Bash_UndistractMe",
        "Bat": "pynix_os.programs.bat:Bat",
        "Bazarr": "pynix_os.services.bazarr:Bazarr",
        "Bazarr_Settings": "pynix_os.services.bazarr:Bazarr_Settings",
        "Bazecor": "pynix_os.programs.bazecor:Bazecor",
        "Bcache": "pynix_os.boot.bcache:Bcache",
        "Boot_Bcachefs": "pynix_os.boot.bcachefs:Bcachefs",
        "Services_Bcachefs": "pynix_os.services.bcachefs:Bcachefs",
        "Bcachefs_AutoScrub": "pynix_os.services.bcachefs:Bcachefs_AutoScrub",
        "Bcc": "pynix_os.programs.bcc:Bcc",
        "Bcg": "pynix_os.services.bcg:Bcg",
        "Bcg_Mqtt": "pynix_os.services.bcg:Bcg_Mqtt",
        "Beanstalkd": "pynix_os.services.beanstalkd:Beanstalkd",
        "Beanstalkd_Listen": "pynix_os.services.beanstalkd:Beanstalkd_Listen",
        "Bee": "pynix_os.services.bee:Bee",
        "Beesd": "pynix_os.services.beesd:Beesd",
        "Beesd_Filesystems_Value": "pynix_os.services.beesd:Beesd_Filesystems_Value",
        "Below": "pynix_os.services.below:Below",
        "Below_Collect": "pynix_os.services.below:Below_Collect",
        "Below_Compression": "pynix_os.services.below:Below_Compression",
        "Below_Dirs": "pynix_os.services.below:Below_Dirs",
        "Below_Retention": "pynix_os.services.below:Below_Retention",
        "Benchexec": "pynix_os.programs.benchexec:Benchexec",
        "Bentopdf": "pynix_os.services.bentopdf:Bentopdf",
        "Bentopdf_Caddy": "pynix_os.services.bentopdf:Bentopdf_Caddy",
        "Bentopdf_Caddy_VirtualHost": "pynix_os.services.bentopdf:Bentopdf_Caddy_VirtualHost",
        "Bentopdf_Nginx": "pynix_os.services.bentopdf:Bentopdf_Nginx",
        "Bentopdf_Nginx_VirtualHost": "pynix_os.services.bentopdf:Bentopdf_Nginx_VirtualHost",
        "Bentopdf_Nginx_VirtualHost_Listen_Item": "pynix_os.services.bentopdf:Bentopdf_Nginx_VirtualHost_Listen_Item",
        "Bentopdf_Nginx_VirtualHost_Locations_Value": "pynix_os.services.bentopdf:Bentopdf_Nginx_VirtualHost_Locations_Value",
        "Bepasty": "pynix_os.services.bepasty:Bepasty",
        "Bepasty_Servers_Value": "pynix_os.services.bepasty:Bepasty_Servers_Value",
        "Beszel": "pynix_os.services.beszel:Beszel",
        "Beszel_Agent": "pynix_os.services.beszel:Beszel_Agent",
        "Beszel_Agent_Environment": "pynix_os.services.beszel:Beszel_Agent_Environment",
        "Beszel_Agent_Smartmon": "pynix_os.services.beszel:Beszel_Agent_Smartmon",
        "Beszel_Hub": "pynix_os.services.beszel:Beszel_Hub",
        "Biboumi": "pynix_os.services.biboumi:Biboumi",
        "Biboumi_Settings": "pynix_os.services.biboumi:Biboumi_Settings",
        "Bind": "pynix_os.services.bind:Bind",
        "Bind_Zones_Value": "pynix_os.services.bind:Bind_Zones_Value",
        "Binfmt": "pynix_os.boot.binfmt:Binfmt",
        "Binfmt_Registrations_Value": "pynix_os.boot.binfmt:Binfmt_Registrations_Value",
        "Bird": "pynix_os.services.bird:Bird",
        "BirdLg": "pynix_os.services.bird_lg:BirdLg",
        "BirdLg_Frontend": "pynix_os.services.bird_lg:BirdLg_Frontend",
        "BirdLg_Frontend_Navbar": "pynix_os.services.bird_lg:BirdLg_Frontend_Navbar",
        "BirdLg_Proxy": "pynix_os.services.bird_lg:BirdLg_Proxy",
        "BirdLg_Proxy_Traceroute": "pynix_os.services.bird_lg:BirdLg_Proxy_Traceroute",
        "Birdwatcher": "pynix_os.services.birdwatcher:Birdwatcher",
        "BitboxBridge": "pynix_os.services.bitbox_bridge:BitboxBridge",
        "Bitlbee": "pynix_os.services.bitlbee:Bitlbee",
        "Bitmagnet": "pynix_os.services.bitmagnet:Bitmagnet",
        "Bitmagnet_Settings": "pynix_os.services.bitmagnet:Bitmagnet_Settings",
        "Bitmagnet_Settings_DhtServer": "pynix_os.services.bitmagnet:Bitmagnet_Settings_DhtServer",
        "Bitmagnet_Settings_HttpServer": "pynix_os.services.bitmagnet:Bitmagnet_Settings_HttpServer",
        "Bitmagnet_Settings_Postgres": "pynix_os.services.bitmagnet:Bitmagnet_Settings_Postgres",
        "Bitmagnet_Settings_Tmdb": "pynix_os.services.bitmagnet:Bitmagnet_Settings_Tmdb",
        "BitwardenDirectoryConnectorCli": "pynix_os.services.bitwarden_directory_connector_cli:BitwardenDirectoryConnectorCli",
        "BitwardenDirectoryConnectorCli_Ldap": "pynix_os.services.bitwarden_directory_connector_cli:BitwardenDirectoryConnectorCli_Ldap",
        "BitwardenDirectoryConnectorCli_Secrets": "pynix_os.services.bitwarden_directory_connector_cli:BitwardenDirectoryConnectorCli_Secrets",
        "BitwardenDirectoryConnectorCli_Secrets_Bitwarden": "pynix_os.services.bitwarden_directory_connector_cli:BitwardenDirectoryConnectorCli_Secrets_Bitwarden",
        "BitwardenDirectoryConnectorCli_Sync": "pynix_os.services.bitwarden_directory_connector_cli:BitwardenDirectoryConnectorCli_Sync",
        "BlackfireAgent": "pynix_os.services.blackfire_agent:BlackfireAgent",
        "BlackfireAgent_Settings": "pynix_os.services.blackfire_agent:BlackfireAgent_Settings",
        "BladeRF": "pynix_os.hardware.bladeRF:BladeRF",
        "Blendfarm": "pynix_os.services.blendfarm:Blendfarm",
        "Blendfarm_ServerConfig": "pynix_os.services.blendfarm:Blendfarm_ServerConfig",
        "Block": "pynix_os.hardware.block:Block",
        "Blocky": "pynix_os.services.blocky:Blocky",
        "Bloop": "pynix_os.services.bloop:Bloop",
        "Blueman": "pynix_os.services.blueman:Blueman",
        "Bluemap": "pynix_os.services.bluemap:Bluemap",
        "Bluemap_CoreSettings": "pynix_os.services.bluemap:Bluemap_CoreSettings",
        "Bluemap_Maps_Value": "pynix_os.services.bluemap:Bluemap_Maps_Value",
        "Bluemap_Storage_Value": "pynix_os.services.bluemap:Bluemap_Storage_Value",
        "Bluemap_WebappSettings": "pynix_os.services.bluemap:Bluemap_WebappSettings",
        "Bluemap_WebserverSettings": "pynix_os.services.bluemap:Bluemap_WebserverSettings",
        "BlueskyPds": "pynix_os.services.bluesky_pds:BlueskyPds",
        "BlueskyPds_Goat": "pynix_os.services.bluesky_pds:BlueskyPds_Goat",
        "BlueskyPds_Pdsadmin": "pynix_os.services.bluesky_pds:BlueskyPds_Pdsadmin",
        "BlueskyPds_Settings": "pynix_os.services.bluesky_pds:BlueskyPds_Settings",
        "Bluetooth": "pynix_os.hardware.bluetooth:Bluetooth",
        "Bluetooth_Hsphfpd": "pynix_os.hardware.bluetooth:Bluetooth_Hsphfpd",
        "Boinc": "pynix_os.services.boinc:Boinc",
        "Bonsaid": "pynix_os.services.bonsaid:Bonsaid",
        "Bonsaid_Settings_Item": "pynix_os.services.bonsaid:Bonsaid_Settings_Item",
        "Bookorbit": "pynix_os.services.bookorbit:Bookorbit",
        "Bookorbit_Environment": "pynix_os.services.bookorbit:Bookorbit_Environment",
        "Bookstack": "pynix_os.services.bookstack:Bookstack",
        "Bookstack_Nginx": "pynix_os.services.bookstack:Bookstack_Nginx",
        "Bookstack_Nginx_Listen_Item": "pynix_os.services.bookstack:Bookstack_Nginx_Listen_Item",
        "Bookstack_Nginx_Locations_Value": "pynix_os.services.bookstack:Bookstack_Nginx_Locations_Value",
        "Bookstack_Settings": "pynix_os.services.bookstack:Bookstack_Settings",
        "Boot": "pynix_os.boot.__options__:Boot",
        "System_Boot": "pynix_os.system.boot:Boot",
        "Boot_ExtraInitrd": "pynix_os.system.boot:Boot_ExtraInitrd",
        "Boot_Loader": "pynix_os.system.boot:Boot_Loader",
        "Boot_SpecialFileSystems_Value": "pynix_os.boot.__options__:Boot_SpecialFileSystems_Value",
        "Bootspec": "pynix_os.boot.bootspec:Bootspec",
        "Borgbackup": "pynix_os.services.borgbackup:Borgbackup",
        "Borgbackup_Jobs_Value": "pynix_os.services.borgbackup:Borgbackup_Jobs_Value",
        "Borgbackup_Repos_Value": "pynix_os.services.borgbackup:Borgbackup_Repos_Value",
        "Borgmatic": "pynix_os.services.borgmatic:Borgmatic",
        "Borgmatic_Configurations_Value": "pynix_os.services.borgmatic:Borgmatic_Configurations_Value",
        "Borgmatic_Configurations_Value_Repositories_Item": "pynix_os.services.borgmatic:Borgmatic_Configurations_Value_Repositories_Item",
        "Bpftune": "pynix_os.services.bpftune:Bpftune",
        "Brillo": "pynix_os.hardware.brillo:Brillo",
        "Brltty": "pynix_os.services.brltty:Brltty",
        "BroadcastBox": "pynix_os.services.broadcast_box:BroadcastBox",
        "BroadcastBox_Settings": "pynix_os.services.broadcast_box:BroadcastBox_Settings",
        "BroadcastBox_Web": "pynix_os.services.broadcast_box:BroadcastBox_Web",
        "Browserpass": "pynix_os.programs.browserpass:Browserpass",
        "Btrbk": "pynix_os.services.btrbk:Btrbk",
        "Btrbk_Instances_Value": "pynix_os.services.btrbk:Btrbk_Instances_Value",
        "Btrbk_Instances_Value_Settings": "pynix_os.services.btrbk:Btrbk_Instances_Value_Settings",
        "Btrbk_SshAccess_Item": "pynix_os.services.btrbk:Btrbk_SshAccess_Item",
        "Btrfs": "pynix_os.services.btrfs:Btrfs",
        "BtrfsHeatmap": "pynix_os.programs.btrfs_heatmap:BtrfsHeatmap",
        "Btrfs_AutoScrub": "pynix_os.services.btrfs:Btrfs_AutoScrub",
        "Budgie": "pynix_os.environment.budgie:Budgie",
        "Buffyboard": "pynix_os.services.buffyboard:Buffyboard",
        "Buffyboard_Settings": "pynix_os.services.buffyboard:Buffyboard_Settings",
        "BuildbotMaster": "pynix_os.services.buildbot_master:BuildbotMaster",
        "BuildbotWorker": "pynix_os.services.buildbot_worker:BuildbotWorker",
        "Bulwark": "pynix_os.services.bulwark:Bulwark",
        "Bulwark_Admin": "pynix_os.services.bulwark:Bulwark_Admin",
        "Bulwark_Plugins_Item": "pynix_os.services.bulwark:Bulwark_Plugins_Item",
        "Bulwark_Plugins_Item_Config": "pynix_os.services.bulwark:Bulwark_Plugins_Item_Config",
        "Bulwark_Policies": "pynix_os.services.bulwark:Bulwark_Policies",
        "Bulwark_Policies_RestrictionsAnimationsEnabled": "pynix_os.services.bulwark:Bulwark_Policies_RestrictionsAnimationsEnabled",
        "Bulwark_Settings": "pynix_os.services.bulwark:Bulwark_Settings",
        "Bulwark_Settings_Branding": "pynix_os.services.bulwark:Bulwark_Settings_Branding",
        "Bulwark_Settings_DomainBranding_Value": "pynix_os.services.bulwark:Bulwark_Settings_DomainBranding_Value",
        "Bulwark_Settings_JmapServers_Value": "pynix_os.services.bulwark:Bulwark_Settings_JmapServers_Value",
        "Bulwark_Settings_Oauth": "pynix_os.services.bulwark:Bulwark_Settings_Oauth",
        "Bulwark_Telemetry": "pynix_os.services.bulwark:Bulwark_Telemetry",
        "Bulwark_UpdateCheck": "pynix_os.services.bulwark:Bulwark_UpdateCheck",
        "Bumblebee": "pynix_os.hardware.bumblebee:Bumblebee",
        "Byedpi": "pynix_os.services.byedpi:Byedpi",
        "C2fmzqServer": "pynix_os.services.c2fmzq_server:C2fmzqServer",
        "C2fmzqServer_Settings": "pynix_os.services.c2fmzq_server:C2fmzqServer_Settings",
        "Cachefilesd": "pynix_os.services.cachefilesd:Cachefilesd",
        "CachixAgent": "pynix_os.services.cachix_agent:CachixAgent",
        "CachixWatchStore": "pynix_os.services.cachix_watch_store:CachixWatchStore",
        "Caddy": "pynix_os.services.caddy:Caddy",
        "Caddy_VirtualHosts_Value": "pynix_os.services.caddy:Caddy_VirtualHosts_Value",
        "Cadvisor": "pynix_os.services.cadvisor:Cadvisor",
        "Cage": "pynix_os.services.cage:Cage",
        "CalibreServer": "pynix_os.services.calibre_server:CalibreServer",
        "CalibreServer_Auth": "pynix_os.services.calibre_server:CalibreServer_Auth",
        "CalibreWeb": "pynix_os.services.calibre_web:CalibreWeb",
        "CalibreWeb_Listen": "pynix_os.services.calibre_web:CalibreWeb_Listen",
        "CalibreWeb_Options": "pynix_os.services.calibre_web:CalibreWeb_Options",
        "CalibreWeb_Options_ReverseProxyAuth": "pynix_os.services.calibre_web:CalibreWeb_Options_ReverseProxyAuth",
        "Calls": "pynix_os.programs.calls:Calls",
        "Canaille": "pynix_os.services.canaille:Canaille",
        "Canaille_Settings": "pynix_os.services.canaille:Canaille_Settings",
        "Canaille_Settings_CANAILLEACL": "pynix_os.services.canaille:Canaille_Settings_CANAILLEACL",
        "Canaille_Settings_CANAILLELDAP": "pynix_os.services.canaille:Canaille_Settings_CANAILLELDAP",
        "Canaille_Settings_CANAILLEOIDC": "pynix_os.services.canaille:Canaille_Settings_CANAILLEOIDC",
        "Canaille_Settings_CANAILLESMTP": "pynix_os.services.canaille:Canaille_Settings_CANAILLESMTP",
        "CantoDaemon": "pynix_os.services.canto_daemon:CantoDaemon",
        "CaptiveBrowser": "pynix_os.programs.captive_browser:CaptiveBrowser",
        "Cardwired": "pynix_os.services.cardwired:Cardwired",
        "Cardwired_Settings": "pynix_os.services.cardwired:Cardwired_Settings",
        "Cassandra": "pynix_os.services.cassandra:Cassandra",
        "Cassandra_JmxRoles_Item": "pynix_os.services.cassandra:Cassandra_JmxRoles_Item",
        "Castopod": "pynix_os.services.castopod:Castopod",
        "Castopod_Database": "pynix_os.services.castopod:Castopod_Database",
        "Castsponsorskip": "pynix_os.services.castsponsorskip:Castsponsorskip",
        "CatoClient": "pynix_os.services.cato_client:CatoClient",
        "Ccache": "pynix_os.programs.ccache:Ccache",
        "Cdemu": "pynix_os.programs.cdemu:Cdemu",
        "Centrifugo": "pynix_os.services.centrifugo:Centrifugo",
        "Ceph": "pynix_os.services.ceph:Ceph",
        "Ceph_Client": "pynix_os.services.ceph:Ceph_Client",
        "Ceph_Global": "pynix_os.services.ceph:Ceph_Global",
        "Ceph_Mds": "pynix_os.services.ceph:Ceph_Mds",
        "Ceph_Mgr": "pynix_os.services.ceph:Ceph_Mgr",
        "Ceph_Mon": "pynix_os.services.ceph:Ceph_Mon",
        "Ceph_Osd": "pynix_os.services.ceph:Ceph_Osd",
        "Ceph_Rgw": "pynix_os.services.ceph:Ceph_Rgw",
        "Certmgr": "pynix_os.services.certmgr:Certmgr",
        "Certmgr_Specs_Value_Or": "pynix_os.services.certmgr:Certmgr_Specs_Value_Or",
        "Certspotter": "pynix_os.services.certspotter:Certspotter",
        "Cfdyndns": "pynix_os.services.cfdyndns:Cfdyndns",
        "CfsZenTweaks": "pynix_os.programs.cfs_zen_tweaks:CfsZenTweaks",
        "Cfssl": "pynix_os.services.cfssl:Cfssl",
        "Cgminer": "pynix_os.services.cgminer:Cgminer",
        "ChangedetectionIo": "pynix_os.services.changedetection_io:ChangedetectionIo",
        "Channel": "pynix_os.nix.channel:Channel",
        "ChhotoUrl": "pynix_os.services.chhoto_url:ChhotoUrl",
        "ChhotoUrl_Settings": "pynix_os.services.chhoto_url:ChhotoUrl_Settings",
        "ChiselServer": "pynix_os.services.chisel_server:ChiselServer",
        "Chromadb": "pynix_os.services.chromadb:Chromadb",
        "Chromium": "pynix_os.programs.chromium:Chromium",
        "ChromiumSuidSandbox": "pynix_os.security.chromiumSuidSandbox:ChromiumSuidSandbox",
        "Chrony": "pynix_os.services.chrony:Chrony",
        "Chrony_Initstepslew": "pynix_os.services.chrony:Chrony_Initstepslew",
        "Chrony_Makestep": "pynix_os.services.chrony:Chrony_Makestep",
        "Chrysalis": "pynix_os.programs.chrysalis:Chrysalis",
        "Environment_Cinnamon": "pynix_os.environment.cinnamon:Cinnamon",
        "Services_Cinnamon": "pynix_os.services.cinnamon:Cinnamon",
        "Cinnamon_Apps": "pynix_os.services.cinnamon:Cinnamon_Apps",
        "Cjdns": "pynix_os.services.cjdns:Cjdns",
        "Cjdns_Admin": "pynix_os.services.cjdns:Cjdns_Admin",
        "Cjdns_ETHInterface": "pynix_os.services.cjdns:Cjdns_ETHInterface",
        "Cjdns_ETHInterface_ConnectTo_Value": "pynix_os.services.cjdns:Cjdns_ETHInterface_ConnectTo_Value",
        "Cjdns_UDPInterface": "pynix_os.services.cjdns:Cjdns_UDPInterface",
        "CkbNext": "pynix_os.hardware.ckb_next:CkbNext",
        "Clamav": "pynix_os.services.clamav:Clamav",
        "Clamav_Clamonacc": "pynix_os.services.clamav:Clamav_Clamonacc",
        "Clamav_Daemon": "pynix_os.services.clamav:Clamav_Daemon",
        "Clamav_Fangfrisch": "pynix_os.services.clamav:Clamav_Fangfrisch",
        "Clamav_Fangfrisch_Settings": "pynix_os.services.clamav:Clamav_Fangfrisch_Settings",
        "Clamav_Scanner": "pynix_os.services.clamav:Clamav_Scanner",
        "Clamav_Updater": "pynix_os.services.clamav:Clamav_Updater",
        "ClashVerge": "pynix_os.programs.clash_verge:ClashVerge",
        "Clatd": "pynix_os.services.clatd:Clatd",
        "Clatd_Settings": "pynix_os.services.clatd:Clatd_Settings",
        "Clickhouse": "pynix_os.services.clickhouse:Clickhouse",
        "Clight": "pynix_os.services.clight:Clight",
        "Clight_Temperature": "pynix_os.services.clight:Clight_Temperature",
        "Clipcat": "pynix_os.services.clipcat:Clipcat",
        "Clipmenu": "pynix_os.services.clipmenu:Clipmenu",
        "Cliproxyapi": "pynix_os.services.cliproxyapi:Cliproxyapi",
        "Cliproxyapi_Settings": "pynix_os.services.cliproxyapi:Cliproxyapi_Settings",
        "CloudInit": "pynix_os.services.cloud_init:CloudInit",
        "CloudInit_Btrfs": "pynix_os.services.cloud_init:CloudInit_Btrfs",
        "CloudInit_Ext4": "pynix_os.services.cloud_init:CloudInit_Ext4",
        "CloudInit_Network": "pynix_os.services.cloud_init:CloudInit_Network",
        "CloudInit_Settings": "pynix_os.services.cloud_init:CloudInit_Settings",
        "CloudInit_Xfs": "pynix_os.services.cloud_init:CloudInit_Xfs",
        "CloudflareDdns": "pynix_os.services.cloudflare_ddns:CloudflareDdns",
        "CloudflareDdns_Provider": "pynix_os.services.cloudflare_ddns:CloudflareDdns_Provider",
        "CloudflareDyndns": "pynix_os.services.cloudflare_dyndns:CloudflareDyndns",
        "CloudflareWarp": "pynix_os.services.cloudflare_warp:CloudflareWarp",
        "Cloudflared": "pynix_os.services.cloudflared:Cloudflared",
        "Cloudflared_Tunnels_Value": "pynix_os.services.cloudflared:Cloudflared_Tunnels_Value",
        "Cloudflared_Tunnels_Value_Ingress_Value_Or": "pynix_os.services.cloudflared:Cloudflared_Tunnels_Value_Ingress_Value_Or",
        "Cloudlog": "pynix_os.services.cloudlog:Cloudlog",
        "Cloudlog_Database": "pynix_os.services.cloudlog:Cloudlog_Database",
        "Cloudlog_UpdateClublogScp": "pynix_os.services.cloudlog:Cloudlog_UpdateClublogScp",
        "Cloudlog_UpdateDok": "pynix_os.services.cloudlog:Cloudlog_UpdateDok",
        "Cloudlog_UpdateLotwUsers": "pynix_os.services.cloudlog:Cloudlog_UpdateLotwUsers",
        "Cloudlog_UpdateSota": "pynix_os.services.cloudlog:Cloudlog_UpdateSota",
        "Cloudlog_UpdateWwff": "pynix_os.services.cloudlog:Cloudlog_UpdateWwff",
        "Cloudlog_UploadClublog": "pynix_os.services.cloudlog:Cloudlog_UploadClublog",
        "Cloudlog_UploadLotw": "pynix_os.services.cloudlog:Cloudlog_UploadLotw",
        "Cloudlog_UploadQrz": "pynix_os.services.cloudlog:Cloudlog_UploadQrz",
        "Cnping": "pynix_os.programs.cnping:Cnping",
        "Cntlm": "pynix_os.services.cntlm:Cntlm",
        "Cockpit": "pynix_os.services.cockpit:Cockpit",
        "Cockroachdb": "pynix_os.services.cockroachdb:Cockroachdb",
        "Cockroachdb_Http": "pynix_os.services.cockroachdb:Cockroachdb_Http",
        "Cockroachdb_Listen": "pynix_os.services.cockroachdb:Cockroachdb_Listen",
        "Cocoon": "pynix_os.services.cocoon:Cocoon",
        "Cocoon_Settings": "pynix_os.services.cocoon:Cocoon_Settings",
        "CodeServer": "pynix_os.services.code_server:CodeServer",
        "Coder": "pynix_os.services.coder:Coder",
        "Coder_Database": "pynix_os.services.coder:Coder_Database",
        "Coder_Environment": "pynix_os.services.coder:Coder_Environment",
        "CollaboraOnline": "pynix_os.services.collabora_online:CollaboraOnline",
        "CollaboraOnline_AliasGroups_Item": "pynix_os.services.collabora_online:CollaboraOnline_AliasGroups_Item",
        "Collectd": "pynix_os.services.collectd:Collectd",
        "Colord": "pynix_os.services.colord:Colord",
        "Comfyui": "pynix_os.services.comfyui:Comfyui",
        "Comfyui_Models_Item": "pynix_os.services.comfyui:Comfyui_Models_Item",
        "Comma": "pynix_os.programs.comma:Comma",
        "Commafeed": "pynix_os.services.commafeed:Commafeed",
        "CommandNotFound": "pynix_os.programs.command_not_found:CommandNotFound",
        "Compsize": "pynix_os.programs.compsize:Compsize",
        "Confd": "pynix_os.services.confd:Confd",
        "Conman": "pynix_os.services.conman:Conman",
        "Connman": "pynix_os.services.connman:Connman",
        "Connman_Wifi": "pynix_os.services.connman:Connman_Wifi",
        "Console": "pynix_os.console.__options__:Console",
        "Consul": "pynix_os.services.consul:Consul",
        "ConsulTemplate": "pynix_os.services.consul_template:ConsulTemplate",
        "ConsulTemplate_Instances_Value": "pynix_os.services.consul_template:ConsulTemplate_Instances_Value",
        "ConsulTemplate_Instances_Value_Settings": "pynix_os.services.consul_template:ConsulTemplate_Instances_Value_Settings",
        "Consul_Alerts": "pynix_os.services.consul:Consul_Alerts",
        "Consul_Interface": "pynix_os.services.consul:Consul_Interface",
        "Containerd": "pynix_os.virtualisation.containerd:Containerd",
        "Containers": "pynix_os.virtualisation.containers:Containers",
        "Containers_ContainersConf": "pynix_os.virtualisation.containers:Containers_ContainersConf",
        "Containers_OciSeccompBpfHook": "pynix_os.virtualisation.containers:Containers_OciSeccompBpfHook",
        "Containers_Registries": "pynix_os.virtualisation.containers:Containers_Registries",
        "Containers_Storage": "pynix_os.virtualisation.containers:Containers_Storage",
        "Convos": "pynix_os.services.convos:Convos",
        "CookCli": "pynix_os.services.cook_cli:CookCli",
        "Coolercontrol": "pynix_os.programs.coolercontrol:Coolercontrol",
        "Coral": "pynix_os.hardware.coral:Coral",
        "Coral_Pcie": "pynix_os.hardware.coral:Coral_Pcie",
        "Coral_Usb": "pynix_os.hardware.coral:Coral_Usb",
        "Corectrl": "pynix_os.programs.corectrl:Corectrl",
        "Coredns": "pynix_os.services.coredns:Coredns",
        "Coredump": "pynix_os.systemd.coredump:Coredump",
        "Coredump_Settings": "pynix_os.systemd.coredump:Coredump_Settings",
        "Coredump_Settings_Coredump": "pynix_os.systemd.coredump:Coredump_Settings_Coredump",
        "Corefreq": "pynix_os.programs.corefreq:Corefreq",
        "Corerad": "pynix_os.services.corerad:Corerad",
        "Corosync": "pynix_os.services.corosync:Corosync",
        "Corosync_Nodelist_Item": "pynix_os.services.corosync:Corosync_Nodelist_Item",
        "Corteza": "pynix_os.services.corteza:Corteza",
        "Corteza_Settings": "pynix_os.services.corteza:Corteza_Settings",
        "Cosmic": "pynix_os.environment.cosmic:Cosmic",
        "Coturn": "pynix_os.services.coturn:Coturn",
        "Couchdb": "pynix_os.services.couchdb:Couchdb",
        "Cpu": "pynix_os.hardware.cpu:Cpu",
        "CpuEnergyMeter": "pynix_os.programs.cpu_energy_meter:CpuEnergyMeter",
        "Cpu_Amd": "pynix_os.hardware.cpu:Cpu_Amd",
        "Cpu_Amd_RyzenSmu": "pynix_os.hardware.cpu:Cpu_Amd_RyzenSmu",
        "Cpu_Amd_Sev": "pynix_os.hardware.cpu:Cpu_Amd_Sev",
        "Cpu_Amd_SevGuest": "pynix_os.hardware.cpu:Cpu_Amd_SevGuest",
        "Cpu_Intel": "pynix_os.hardware.cpu:Cpu_Intel",
        "Cpu_Intel_Npu": "pynix_os.hardware.cpu:Cpu_Intel_Npu",
        "Cpu_Intel_Sgx": "pynix_os.hardware.cpu:Cpu_Intel_Sgx",
        "Cpu_Intel_Sgx_Provision": "pynix_os.hardware.cpu:Cpu_Intel_Sgx_Provision",
        "Cpu_X86": "pynix_os.hardware.cpu:Cpu_X86",
        "Cpu_X86_Msr": "pynix_os.hardware.cpu:Cpu_X86_Msr",
        "Cpu_X86_Msr_Settings": "pynix_os.hardware.cpu:Cpu_X86_Msr_Settings",
        "Cpufreq": "pynix_os.powerManagement.cpufreq:Cpufreq",
        "CpuminerCryptonight": "pynix_os.services.cpuminer_cryptonight:CpuminerCryptonight",
        "CpupowerGui": "pynix_os.services.cpupower_gui:CpupowerGui",
        "CrabHole": "pynix_os.services.crab_hole:CrabHole",
        "CrabHole_Settings": "pynix_os.services.crab_hole:CrabHole_Settings",
        "CrashDump": "pynix_os.boot.crashDump:CrashDump",
        "CreateAp": "pynix_os.services.create_ap:CreateAp",
        "CriO": "pynix_os.virtualisation.cri_o:CriO",
        "Criu": "pynix_os.programs.criu:Criu",
        "Croc": "pynix_os.services.croc:Croc",
        "Cron": "pynix_os.services.cron:Cron",
        "CrossSeed": "pynix_os.services.cross_seed:CrossSeed",
        "CrossSeed_Settings": "pynix_os.services.cross_seed:CrossSeed_Settings",
        "CrossfireServer": "pynix_os.services.crossfire_server:CrossfireServer",
        "Crossmacro": "pynix_os.services.crossmacro:Crossmacro",
        "Crowdsec": "pynix_os.services.crowdsec:Crowdsec",
        "CrowdsecFirewallBouncer": "pynix_os.services.crowdsec_firewall_bouncer:CrowdsecFirewallBouncer",
        "CrowdsecFirewallBouncer_RegisterBouncer": "pynix_os.services.crowdsec_firewall_bouncer:CrowdsecFirewallBouncer_RegisterBouncer",
        "CrowdsecFirewallBouncer_Secrets": "pynix_os.services.crowdsec_firewall_bouncer:CrowdsecFirewallBouncer_Secrets",
        "CrowdsecFirewallBouncer_Settings": "pynix_os.services.crowdsec_firewall_bouncer:CrowdsecFirewallBouncer_Settings",
        "Crowdsec_Hub": "pynix_os.services.crowdsec:Crowdsec_Hub",
        "Crowdsec_LocalConfig": "pynix_os.services.crowdsec:Crowdsec_LocalConfig",
        "Crowdsec_LocalConfig_Parsers": "pynix_os.services.crowdsec:Crowdsec_LocalConfig_Parsers",
        "Crowdsec_LocalConfig_PostOverflows": "pynix_os.services.crowdsec:Crowdsec_LocalConfig_PostOverflows",
        "Crowdsec_Settings": "pynix_os.services.crowdsec:Crowdsec_Settings",
        "Crowdsec_Settings_Capi": "pynix_os.services.crowdsec:Crowdsec_Settings_Capi",
        "Crowdsec_Settings_Console": "pynix_os.services.crowdsec:Crowdsec_Settings_Console",
        "Crowdsec_Settings_Lapi": "pynix_os.services.crowdsec:Crowdsec_Settings_Lapi",
        "Cryptpad": "pynix_os.services.cryptpad:Cryptpad",
        "Cryptpad_Settings": "pynix_os.services.cryptpad:Cryptpad_Settings",
        "CyrusImap": "pynix_os.services.cyrus_imap:CyrusImap",
        "CyrusImap_CyrusSettings": "pynix_os.services.cyrus_imap:CyrusImap_CyrusSettings",
        "CyrusImap_ImapdSettings": "pynix_os.services.cyrus_imap:CyrusImap_ImapdSettings",
        "Dae": "pynix_os.services.dae:Dae",
        "Dae_OpenFirewall": "pynix_os.services.dae:Dae_OpenFirewall",
        "Daemon": "pynix_os.nix.daemon:Daemon",
        "Dante": "pynix_os.services.dante:Dante",
        "Darkhttpd": "pynix_os.services.darkhttpd:Darkhttpd",
        "DasWatchdog": "pynix_os.services.das_watchdog:DasWatchdog",
        "Dashy": "pynix_os.services.dashy:Dashy",
        "Dashy_VirtualHost": "pynix_os.services.dashy:Dashy_VirtualHost",
        "DatadogAgent": "pynix_os.services.datadog_agent:DatadogAgent",
        "Davfs2": "pynix_os.services.davfs2:Davfs2",
        "Davfs2_Settings": "pynix_os.services.davfs2:Davfs2_Settings",
        "Davis": "pynix_os.services.davis:Davis",
        "Davis_Config_Value_Or": "pynix_os.services.davis:Davis_Config_Value_Or",
        "Davis_Database": "pynix_os.services.davis:Davis_Database",
        "Davis_Mail": "pynix_os.services.davis:Davis_Mail",
        "Davis_Nginx": "pynix_os.services.davis:Davis_Nginx",
        "Davis_Nginx_Listen_Item": "pynix_os.services.davis:Davis_Nginx_Listen_Item",
        "Davis_Nginx_Locations_Value": "pynix_os.services.davis:Davis_Nginx_Locations_Value",
        "Davmail": "pynix_os.services.davmail:Davmail",
        "Dawarich": "pynix_os.services.dawarich:Dawarich",
        "Dawarich_Database": "pynix_os.services.dawarich:Dawarich_Database",
        "Dawarich_Redis": "pynix_os.services.dawarich:Dawarich_Redis",
        "Dawarich_SidekiqProcesses_Value": "pynix_os.services.dawarich:Dawarich_SidekiqProcesses_Value",
        "Dawarich_Smtp": "pynix_os.services.dawarich:Dawarich_Smtp",
        "DbRest": "pynix_os.services.db_rest:DbRest",
        "DbRest_Redis": "pynix_os.services.db_rest:DbRest_Redis",
        "Dbus": "pynix_os.services.dbus:Dbus",
        "Dconf": "pynix_os.programs.dconf:Dconf",
        "Dconf_Profiles_Value_Or": "pynix_os.programs.dconf:Dconf_Profiles_Value_Or",
        "Dconf_Profiles_Value_Or_Databases_Item_Or": "pynix_os.programs.dconf:Dconf_Profiles_Value_Or_Databases_Item_Or",
        "Ddccontrol": "pynix_os.services.ddccontrol:Ddccontrol",
        "Ddclient": "pynix_os.services.ddclient:Ddclient",
        "DdnsUpdater": "pynix_os.services.ddns_updater:DdnsUpdater",
        "Decklink": "pynix_os.hardware.decklink:Decklink",
        "Deconz": "pynix_os.services.deconz:Deconz",
        "Deluge": "pynix_os.services.deluge:Deluge",
        "Deluge_Web": "pynix_os.services.deluge:Deluge_Web",
        "Dendrite": "pynix_os.services.dendrite:Dendrite",
        "Dendrite_Settings": "pynix_os.services.dendrite:Dendrite_Settings",
        "DependencyTrack": "pynix_os.services.dependency_track:DependencyTrack",
        "DependencyTrack_Frontend": "pynix_os.services.dependency_track:DependencyTrack_Frontend",
        "DependencyTrack_Ldap": "pynix_os.services.dependency_track:DependencyTrack_Ldap",
        "DependencyTrack_Nginx": "pynix_os.services.dependency_track:DependencyTrack_Nginx",
        "DependencyTrack_Oidc": "pynix_os.services.dependency_track:DependencyTrack_Oidc",
        "DependencyTrack_Oidc_Teams": "pynix_os.services.dependency_track:DependencyTrack_Oidc_Teams",
        "DependencyTrack_Settings": "pynix_os.services.dependency_track:DependencyTrack_Settings",
        "DesktopManager": "pynix_os.services.desktopManager:DesktopManager",
        "DesktopManager_Budgie": "pynix_os.services.desktopManager:DesktopManager_Budgie",
        "DesktopManager_Cosmic": "pynix_os.services.desktopManager:DesktopManager_Cosmic",
        "DesktopManager_Cosmic_Xwayland": "pynix_os.services.desktopManager:DesktopManager_Cosmic_Xwayland",
        "DesktopManager_Gnome": "pynix_os.services.desktopManager:DesktopManager_Gnome",
        "DesktopManager_Gnome_Flashback": "pynix_os.services.desktopManager:DesktopManager_Gnome_Flashback",
        "DesktopManager_Gnome_Flashback_CustomSessions_Item": "pynix_os.services.desktopManager:DesktopManager_Gnome_Flashback_CustomSessions_Item",
        "DesktopManager_Lomiri": "pynix_os.services.desktopManager:DesktopManager_Lomiri",
        "DesktopManager_Pantheon": "pynix_os.services.desktopManager:DesktopManager_Pantheon",
        "DesktopManager_Plasma6": "pynix_os.services.desktopManager:DesktopManager_Plasma6",
        "Dev": "pynix_os.documentation.dev:Dev",
        "DeviceTree": "pynix_os.hardware.deviceTree:DeviceTree",
        "DeviceTree_Overlays_Item": "pynix_os.hardware.deviceTree:DeviceTree_Overlays_Item",
        "Devmon": "pynix_os.services.devmon:Devmon",
        "DevpiServer": "pynix_os.services.devpi_server:DevpiServer",
        "Dex": "pynix_os.services.dex:Dex",
        "DeyeDummycloud": "pynix_os.services.deye_dummycloud:DeyeDummycloud",
        "Dgraph": "pynix_os.services.dgraph:Dgraph",
        "Dgraph_Alpha": "pynix_os.services.dgraph:Dgraph_Alpha",
        "Dgraph_Zero": "pynix_os.services.dgraph:Dgraph_Zero",
        "Dhcpcd": "pynix_os.networking.dhcpcd:Dhcpcd",
        "Dictd": "pynix_os.services.dictd:Dictd",
        "Hardware_Digitalbitbox": "pynix_os.hardware.digitalbitbox:Digitalbitbox",
        "Programs_Digitalbitbox": "pynix_os.programs.digitalbitbox:Digitalbitbox",
        "Diod": "pynix_os.services.diod:Diod",
        "Direnv": "pynix_os.programs.direnv:Direnv",
        "Direnv_Angrr": "pynix_os.programs.direnv:Direnv_Angrr",
        "Direnv_NixDirenv": "pynix_os.programs.direnv:Direnv_NixDirenv",
        "Discourse": "pynix_os.services.discourse:Discourse",
        "Discourse_Admin": "pynix_os.services.discourse:Discourse_Admin",
        "Discourse_Database": "pynix_os.services.discourse:Discourse_Database",
        "Discourse_Mail": "pynix_os.services.discourse:Discourse_Mail",
        "Discourse_Mail_Incoming": "pynix_os.services.discourse:Discourse_Mail_Incoming",
        "Discourse_Mail_Outgoing": "pynix_os.services.discourse:Discourse_Mail_Outgoing",
        "Discourse_Nginx": "pynix_os.services.discourse:Discourse_Nginx",
        "Discourse_Redis": "pynix_os.services.discourse:Discourse_Redis",
        "Disnix": "pynix_os.services.disnix:Disnix",
        "Display": "pynix_os.hardware.display:Display",
        "DisplayManager": "pynix_os.services.displayManager:DisplayManager",
        "DisplayManager_Airlock": "pynix_os.services.displayManager:DisplayManager_Airlock",
        "DisplayManager_Airlock_Compositor": "pynix_os.services.displayManager:DisplayManager_Airlock_Compositor",
        "DisplayManager_Airlock_SyncDynamicScheme": "pynix_os.services.displayManager:DisplayManager_Airlock_SyncDynamicScheme",
        "DisplayManager_AutoLogin": "pynix_os.services.displayManager:DisplayManager_AutoLogin",
        "DisplayManager_CosmicGreeter": "pynix_os.services.displayManager:DisplayManager_CosmicGreeter",
        "DisplayManager_DmsGreeter": "pynix_os.services.displayManager:DisplayManager_DmsGreeter",
        "DisplayManager_DmsGreeter_Compositor": "pynix_os.services.displayManager:DisplayManager_DmsGreeter_Compositor",
        "DisplayManager_DmsGreeter_Logs": "pynix_os.services.displayManager:DisplayManager_DmsGreeter_Logs",
        "DisplayManager_DmsGreeter_Quickshell": "pynix_os.services.displayManager:DisplayManager_DmsGreeter_Quickshell",
        "DisplayManager_Gdm": "pynix_os.services.displayManager:DisplayManager_Gdm",
        "DisplayManager_Gdm_AutoLogin": "pynix_os.services.displayManager:DisplayManager_Gdm_AutoLogin",
        "DisplayManager_Generic": "pynix_os.services.displayManager:DisplayManager_Generic",
        "DisplayManager_Lemurs": "pynix_os.services.displayManager:DisplayManager_Lemurs",
        "DisplayManager_Ly": "pynix_os.services.displayManager:DisplayManager_Ly",
        "DisplayManager_NoctaliaGreeter": "pynix_os.services.displayManager:DisplayManager_NoctaliaGreeter",
        "DisplayManager_NoctaliaGreeter_CursorTheme": "pynix_os.services.displayManager:DisplayManager_NoctaliaGreeter_CursorTheme",
        "DisplayManager_PlasmaLoginManager": "pynix_os.services.displayManager:DisplayManager_PlasmaLoginManager",
        "DisplayManager_Regreet": "pynix_os.services.displayManager:DisplayManager_Regreet",
        "DisplayManager_Regreet_CursorTheme": "pynix_os.services.displayManager:DisplayManager_Regreet_CursorTheme",
        "DisplayManager_Regreet_Font": "pynix_os.services.displayManager:DisplayManager_Regreet_Font",
        "DisplayManager_Regreet_IconTheme": "pynix_os.services.displayManager:DisplayManager_Regreet_IconTheme",
        "DisplayManager_Regreet_Theme": "pynix_os.services.displayManager:DisplayManager_Regreet_Theme",
        "DisplayManager_Sddm": "pynix_os.services.displayManager:DisplayManager_Sddm",
        "DisplayManager_Sddm_AutoLogin": "pynix_os.services.displayManager:DisplayManager_Sddm_AutoLogin",
        "DisplayManager_Sddm_Wayland": "pynix_os.services.displayManager:DisplayManager_Sddm_Wayland",
        "Display_Edid": "pynix_os.hardware.display:Display_Edid",
        "Display_Outputs_Value": "pynix_os.hardware.display:Display_Outputs_Value",
        "Distccd": "pynix_os.services.distccd:Distccd",
        "Distccd_Stats": "pynix_os.services.distccd:Distccd_Stats",
        "DkimproxyOut": "pynix_os.services.dkimproxy_out:DkimproxyOut",
        "Dleyna": "pynix_os.services.dleyna:Dleyna",
        "Dmrconfig": "pynix_os.programs.dmrconfig:Dmrconfig",
        "DmsShell": "pynix_os.programs.dms_shell:DmsShell",
        "DmsShell_Plugins_Value": "pynix_os.programs.dms_shell:DmsShell_Plugins_Value",
        "DmsShell_Quickshell": "pynix_os.programs.dms_shell:DmsShell_Quickshell",
        "DmsShell_Systemd": "pynix_os.programs.dms_shell:DmsShell_Systemd",
        "Dnscache": "pynix_os.services.dnscache:Dnscache",
        "DnscryptProxy": "pynix_os.services.dnscrypt_proxy:DnscryptProxy",
        "Dnsdist": "pynix_os.services.dnsdist:Dnsdist",
        "Dnsdist_Dnscrypt": "pynix_os.services.dnsdist:Dnsdist_Dnscrypt",
        "Dnsmasq": "pynix_os.services.dnsmasq:Dnsmasq",
        "Dnsmasq_Settings": "pynix_os.services.dnsmasq:Dnsmasq_Settings",
        "Dnsproxy": "pynix_os.services.dnsproxy:Dnsproxy",
        "DoAgent": "pynix_os.services.do_agent:DoAgent",
        "Doas": "pynix_os.security.doas:Doas",
        "Doas_ExtraRules_Item": "pynix_os.security.doas:Doas_ExtraRules_Item",
        "Doc": "pynix_os.documentation.doc:Doc",
        "Docker": "pynix_os.virtualisation.docker:Docker",
        "DockerRegistry": "pynix_os.services.dockerRegistry:DockerRegistry",
        "Docker_AutoPrune": "pynix_os.virtualisation.docker:Docker_AutoPrune",
        "Docker_AutoPrune_AllVolumes": "pynix_os.virtualisation.docker:Docker_AutoPrune_AllVolumes",
        "Docker_Daemon": "pynix_os.virtualisation.docker:Docker_Daemon",
        "Docker_Daemon_Settings": "pynix_os.virtualisation.docker:Docker_Daemon_Settings",
        "Docker_LiveRestore": "pynix_os.virtualisation.docker:Docker_LiveRestore",
        "Docker_Rootless": "pynix_os.virtualisation.docker:Docker_Rootless",
        "Docker_Rootless_Daemon": "pynix_os.virtualisation.docker:Docker_Rootless_Daemon",
        "DoclingServe": "pynix_os.services.docling_serve:DoclingServe",
        "Documentation": "pynix_os.documentation.__options__:Documentation",
        "Documize": "pynix_os.services.documize:Documize",
        "Docuseal": "pynix_os.services.docuseal:Docuseal",
        "Docuseal_Redis": "pynix_os.services.docuseal:Docuseal_Redis",
        "Docuum": "pynix_os.services.docuum:Docuum",
        "DohProxyRust": "pynix_os.services.doh_proxy_rust:DohProxyRust",
        "DohServer": "pynix_os.services.doh_server:DohServer",
        "DohServer_Settings": "pynix_os.services.doh_server:DohServer_Settings",
        "Dokuwiki": "pynix_os.services.dokuwiki:Dokuwiki",
        "Dokuwiki_Sites_Value": "pynix_os.services.dokuwiki:Dokuwiki_Sites_Value",
        "Dokuwiki_Sites_Value_Acl_Item": "pynix_os.services.dokuwiki:Dokuwiki_Sites_Value_Acl_Item",
        "Dolibarr": "pynix_os.services.dolibarr:Dolibarr",
        "Dolibarr_H2o": "pynix_os.services.dolibarr:Dolibarr_H2o",
        "Dolibarr_H2o_Acme": "pynix_os.services.dolibarr:Dolibarr_H2o_Acme",
        "Dolibarr_H2o_Http": "pynix_os.services.dolibarr:Dolibarr_H2o_Http",
        "Dolibarr_H2o_Tls": "pynix_os.services.dolibarr:Dolibarr_H2o_Tls",
        "Dolibarr_H2o_Tls_Identity_Item": "pynix_os.services.dolibarr:Dolibarr_H2o_Tls_Identity_Item",
        "Dolibarr_Nginx": "pynix_os.services.dolibarr:Dolibarr_Nginx",
        "Dolibarr_Nginx_Listen_Item": "pynix_os.services.dolibarr:Dolibarr_Nginx_Listen_Item",
        "Dolibarr_Nginx_Locations_Value": "pynix_os.services.dolibarr:Dolibarr_Nginx_Locations_Value",
        "Domoticz": "pynix_os.services.domoticz:Domoticz",
        "Dovecot2": "pynix_os.services.dovecot2:Dovecot2",
        "Dovecot2_Imapsieve": "pynix_os.services.dovecot2:Dovecot2_Imapsieve",
        "Dovecot2_Imapsieve_Mailbox_Item": "pynix_os.services.dovecot2:Dovecot2_Imapsieve_Mailbox_Item",
        "Dovecot2_MailPlugins": "pynix_os.services.dovecot2:Dovecot2_MailPlugins",
        "Dovecot2_MailPlugins_Globally": "pynix_os.services.dovecot2:Dovecot2_MailPlugins_Globally",
        "Dovecot2_MailPlugins_PerProtocol_Value": "pynix_os.services.dovecot2:Dovecot2_MailPlugins_PerProtocol_Value",
        "Dovecot2_Settings": "pynix_os.services.dovecot2:Dovecot2_Settings",
        "Dovecot2_Settings_Extra_Or": "pynix_os.services.dovecot2:Dovecot2_Settings_Extra_Or",
        "Dovecot2_Settings_PassdbPam": "pynix_os.services.dovecot2:Dovecot2_Settings_PassdbPam",
        "Dovecot2_Settings_Plugin": "pynix_os.services.dovecot2:Dovecot2_Settings_Plugin",
        "Dovecot2_Settings_UserdbPasswd": "pynix_os.services.dovecot2:Dovecot2_Settings_UserdbPasswd",
        "Dovecot2_Sieve": "pynix_os.services.dovecot2:Dovecot2_Sieve",
        "Dragonflydb": "pynix_os.services.dragonflydb:Dragonflydb",
        "Drasl": "pynix_os.services.drasl:Drasl",
        "Drasl_Settings": "pynix_os.services.drasl:Drasl_Settings",
        "Drasl_Settings_RegistrationOIDC_Item": "pynix_os.services.drasl:Drasl_Settings_RegistrationOIDC_Item",
        "Draupnir": "pynix_os.services.draupnir:Draupnir",
        "Draupnir_Secrets": "pynix_os.services.draupnir:Draupnir_Secrets",
        "Draupnir_Secrets_Pantalaimon": "pynix_os.services.draupnir:Draupnir_Secrets_Pantalaimon",
        "Draupnir_Secrets_Web": "pynix_os.services.draupnir:Draupnir_Secrets_Web",
        "Draupnir_Secrets_Web_SynapseHTTPAntispam": "pynix_os.services.draupnir:Draupnir_Secrets_Web_SynapseHTTPAntispam",
        "Draupnir_Settings": "pynix_os.services.draupnir:Draupnir_Settings",
        "Drbd": "pynix_os.services.drbd:Drbd",
        "Droidcam": "pynix_os.programs.droidcam:Droidcam",
        "Druid": "pynix_os.services.druid:Druid",
        "Druid_Broker": "pynix_os.services.druid:Druid_Broker",
        "Druid_Coordinator": "pynix_os.services.druid:Druid_Coordinator",
        "Druid_Historical": "pynix_os.services.druid:Druid_Historical",
        "Druid_Historical_SegmentLocations_Item": "pynix_os.services.druid:Druid_Historical_SegmentLocations_Item",
        "Druid_MiddleManager": "pynix_os.services.druid:Druid_MiddleManager",
        "Druid_Overlord": "pynix_os.services.druid:Druid_Overlord",
        "Druid_Router": "pynix_os.services.druid:Druid_Router",
        "Drupal": "pynix_os.services.drupal:Drupal",
        "Drupal_Sites_Value": "pynix_os.services.drupal:Drupal_Sites_Value",
        "Drupal_Sites_Value_VirtualHost": "pynix_os.services.drupal:Drupal_Sites_Value_VirtualHost",
        "Drupal_Sites_Value_VirtualHost_Listen_Item": "pynix_os.services.drupal:Drupal_Sites_Value_VirtualHost_Listen_Item",
        "Drupal_Sites_Value_VirtualHost_Locations_Value": "pynix_os.services.drupal:Drupal_Sites_Value_VirtualHost_Locations_Value",
        "Dsearch": "pynix_os.programs.dsearch:Dsearch",
        "Dsearch_Systemd": "pynix_os.programs.dsearch:Dsearch_Systemd",
        "Dsnet": "pynix_os.services.dsnet:Dsnet",
        "Dsnet_Settings": "pynix_os.services.dsnet:Dsnet_Settings",
        "Dspam": "pynix_os.services.dspam:Dspam",
        "DublinTraceroute": "pynix_os.programs.dublin_traceroute:DublinTraceroute",
        "Duckdns": "pynix_os.services.duckdns:Duckdns",
        "Duckling": "pynix_os.services.duckling:Duckling",
        "Dump1090Fa": "pynix_os.services.dump1090_fa:Dump1090Fa",
        "Dunst": "pynix_os.services.dunst:Dunst",
        "Duosec": "pynix_os.security.duosec:Duosec",
        "Duosec_Pam": "pynix_os.security.duosec:Duosec_Pam",
        "Duosec_Ssh": "pynix_os.security.duosec:Duosec_Ssh",
        "Duplicati": "pynix_os.services.duplicati:Duplicati",
        "Duplicity": "pynix_os.services.duplicity:Duplicity",
        "Duplicity_Cleanup": "pynix_os.services.duplicity:Duplicity_Cleanup",
        "Dwl": "pynix_os.programs.dwl:Dwl",
        "DwmStatus": "pynix_os.services.dwm_status:DwmStatus",
        "DwmStatus_Settings": "pynix_os.services.dwm_status:DwmStatus_Settings",
        "Dysnomia": "pynix_os.services.dysnomia:Dysnomia",
        "EImzo": "pynix_os.services.e_imzo:EImzo",
        "Earlyoom": "pynix_os.services.earlyoom:Earlyoom",
        "Easytier": "pynix_os.services.easytier:Easytier",
        "Easytier_Instances_Value": "pynix_os.services.easytier:Easytier_Instances_Value",
        "Easytier_Instances_Value_Settings": "pynix_os.services.easytier:Easytier_Instances_Value_Settings",
        "Ebusd": "pynix_os.services.ebusd:Ebusd",
        "Ebusd_Logs": "pynix_os.services.ebusd:Ebusd_Logs",
        "Ebusd_Mqtt": "pynix_os.services.ebusd:Ebusd_Mqtt",
        "Ec2": "pynix_os.ec2.__options__:Ec2",
        "Echoip": "pynix_os.services.echoip:Echoip",
        "EcsAgent": "pynix_os.services.ecs_agent:EcsAgent",
        "Eg25Manager": "pynix_os.services.eg25_manager:Eg25Manager",
        "Ejabberd": "pynix_os.services.ejabberd:Ejabberd",
        "Elasticsearch": "pynix_os.services.elasticsearch:Elasticsearch",
        "ElasticsearchCurator": "pynix_os.services.elasticsearch_curator:ElasticsearchCurator",
        "Elephant": "pynix_os.services.elephant:Elephant",
        "Elk": "pynix_os.services.elk:Elk",
        "Elk_Settings": "pynix_os.services.elk:Elk_Settings",
        "Emacs": "pynix_os.services.emacs:Emacs",
        "Endlessh": "pynix_os.services.endlessh:Endlessh",
        "EndlesshGo": "pynix_os.services.endlessh_go:EndlesshGo",
        "EndlesshGo_Prometheus": "pynix_os.services.endlessh_go:EndlesshGo_Prometheus",
        "Engelsystem": "pynix_os.services.engelsystem:Engelsystem",
        "Enlightenment": "pynix_os.environment.enlightenment:Enlightenment",
        "Ente": "pynix_os.services.ente:Ente",
        "EnteAuth": "pynix_os.programs.ente_auth:EnteAuth",
        "Ente_Api": "pynix_os.services.ente:Ente_Api",
        "Ente_Api_Nginx": "pynix_os.services.ente:Ente_Api_Nginx",
        "Ente_Api_Settings": "pynix_os.services.ente:Ente_Api_Settings",
        "Ente_Web": "pynix_os.services.ente:Ente_Web",
        "Ente_Web_Domains": "pynix_os.services.ente:Ente_Web_Domains",
        "Entropy": "pynix_os.programs.entropy:Entropy",
        "Envfs": "pynix_os.services.envfs:Envfs",
        "Environment": "pynix_os.environment.__options__:Environment",
        "Environment_Etc_Value": "pynix_os.environment.__options__:Environment_Etc_Value",
        "Envision": "pynix_os.programs.envision:Envision",
        "Envoy": "pynix_os.services.envoy:Envoy",
        "Epgstation": "pynix_os.services.epgstation:Epgstation",
        "Epgstation_Database": "pynix_os.services.epgstation:Epgstation_Database",
        "Epgstation_Settings": "pynix_os.services.epgstation:Epgstation_Settings",
        "Epmd": "pynix_os.services.epmd:Epmd",
        "Ergo": "pynix_os.services.ergo:Ergo",
        "Ergo_Api": "pynix_os.services.ergo:Ergo_Api",
        "Ergo_Api_Listen": "pynix_os.services.ergo:Ergo_Api_Listen",
        "Ergo_Listen": "pynix_os.services.ergo:Ergo_Listen",
        "Ergochat": "pynix_os.services.ergochat:Ergochat",
        "Erigon": "pynix_os.services.erigon:Erigon",
        "Errbot": "pynix_os.services.errbot:Errbot",
        "Errbot_Instances_Value": "pynix_os.services.errbot:Errbot_Instances_Value",
        "Ersatztv": "pynix_os.services.ersatztv:Ersatztv",
        "Esdm": "pynix_os.services.esdm:Esdm",
        "Espanso": "pynix_os.services.espanso:Espanso",
        "Esphome": "pynix_os.services.esphome:Esphome",
        "Etc": "pynix_os.system.etc:Etc",
        "Etc_Overlay": "pynix_os.system.etc:Etc_Overlay",
        "Etcd": "pynix_os.services.etcd:Etcd",
        "EtebaseServer": "pynix_os.services.etebase_server:EtebaseServer",
        "EtebaseServer_Settings": "pynix_os.services.etebase_server:EtebaseServer_Settings",
        "EternalTerminal": "pynix_os.services.eternal_terminal:EternalTerminal",
        "EtesyncDav": "pynix_os.services.etesync_dav:EtesyncDav",
        "Evcc": "pynix_os.services.evcc:Evcc",
        "Evdevremapkeys": "pynix_os.services.evdevremapkeys:Evdevremapkeys",
        "Evince": "pynix_os.programs.evince:Evince",
        "Evolution": "pynix_os.programs.evolution:Evolution",
        "Evremap": "pynix_os.services.evremap:Evremap",
        "Evremap_Settings": "pynix_os.services.evremap:Evremap_Settings",
        "Evremap_Settings_DualRole_Item": "pynix_os.services.evremap:Evremap_Settings_DualRole_Item",
        "Evremap_Settings_Remap_Item": "pynix_os.services.evremap:Evremap_Settings_Remap_Item",
        "Exim": "pynix_os.services.exim:Exim",
        "Expressvpn": "pynix_os.services.expressvpn:Expressvpn",
        "ExtraContainer": "pynix_os.programs.extra_container:ExtraContainer",
        "Facetimehd": "pynix_os.hardware.facetimehd:Facetimehd",
        "Facter": "pynix_os.hardware.facter:Facter",
        "Facter_Debug": "pynix_os.hardware.facter:Facter_Debug",
        "Facter_Detected": "pynix_os.hardware.facter:Facter_Detected",
        "Facter_Detected_Bluetooth": "pynix_os.hardware.facter:Facter_Detected_Bluetooth",
        "Facter_Detected_Boot": "pynix_os.hardware.facter:Facter_Detected_Boot",
        "Facter_Detected_Boot_Disk": "pynix_os.hardware.facter:Facter_Detected_Boot_Disk",
        "Facter_Detected_Boot_Graphics": "pynix_os.hardware.facter:Facter_Detected_Boot_Graphics",
        "Facter_Detected_Boot_Initrd": "pynix_os.hardware.facter:Facter_Detected_Boot_Initrd",
        "Facter_Detected_Boot_Initrd_Networking": "pynix_os.hardware.facter:Facter_Detected_Boot_Initrd_Networking",
        "Facter_Detected_Boot_Keyboard": "pynix_os.hardware.facter:Facter_Detected_Boot_Keyboard",
        "Facter_Detected_Camera": "pynix_os.hardware.facter:Facter_Detected_Camera",
        "Facter_Detected_Camera_Ipu6": "pynix_os.hardware.facter:Facter_Detected_Camera_Ipu6",
        "Facter_Detected_Dhcp": "pynix_os.hardware.facter:Facter_Detected_Dhcp",
        "Facter_Detected_Fingerprint": "pynix_os.hardware.facter:Facter_Detected_Fingerprint",
        "Facter_Detected_Graphics": "pynix_os.hardware.facter:Facter_Detected_Graphics",
        "Facter_Detected_Graphics_Amd": "pynix_os.hardware.facter:Facter_Detected_Graphics_Amd",
        "Facter_Detected_Networking": "pynix_os.hardware.facter:Facter_Detected_Networking",
        "Facter_Detected_Networking_Intel": "pynix_os.hardware.facter:Facter_Detected_Networking_Intel",
        "Facter_Detected_Networking_Intel_N2200BG": "pynix_os.hardware.facter:Facter_Detected_Networking_Intel_N2200BG",
        "Facter_Detected_Networking_Intel_N3945ABG": "pynix_os.hardware.facter:Facter_Detected_Networking_Intel_N3945ABG",
        "Facter_Detected_Uefi": "pynix_os.hardware.facter:Facter_Detected_Uefi",
        "Facter_Detected_Virtualisation": "pynix_os.hardware.facter:Facter_Detected_Virtualisation",
        "Facter_Detected_Virtualisation_Hyperv": "pynix_os.hardware.facter:Facter_Detected_Virtualisation_Hyperv",
        "Facter_Detected_Virtualisation_None": "pynix_os.hardware.facter:Facter_Detected_Virtualisation_None",
        "Facter_Detected_Virtualisation_Oracle": "pynix_os.hardware.facter:Facter_Detected_Virtualisation_Oracle",
        "Facter_Detected_Virtualisation_Parallels": "pynix_os.hardware.facter:Facter_Detected_Virtualisation_Parallels",
        "Facter_Detected_Virtualisation_Qemu": "pynix_os.hardware.facter:Facter_Detected_Virtualisation_Qemu",
        "Facter_Detected_Virtualisation_VirtioScsi": "pynix_os.hardware.facter:Facter_Detected_Virtualisation_VirtioScsi",
        "Factorio": "pynix_os.services.factorio:Factorio",
        "Fail2ban": "pynix_os.services.fail2ban:Fail2ban",
        "Fail2ban_BantimeIncrement": "pynix_os.services.fail2ban:Fail2ban_BantimeIncrement",
        "Fail2ban_Jails_Value_Or": "pynix_os.services.fail2ban:Fail2ban_Jails_Value_Or",
        "Fakeroute": "pynix_os.services.fakeroute:Fakeroute",
        "Fancontrol": "pynix_os.hardware.fancontrol:Fancontrol",
        "Fanout": "pynix_os.services.fanout:Fanout",
        "FastnetmonAdvanced": "pynix_os.services.fastnetmon_advanced:FastnetmonAdvanced",
        "FastnetmonAdvanced_TrafficDb": "pynix_os.services.fastnetmon_advanced:FastnetmonAdvanced_TrafficDb",
        "FcastReceiver": "pynix_os.programs.fcast_receiver:FcastReceiver",
        "Fcgiwrap": "pynix_os.services.fcgiwrap:Fcgiwrap",
        "Fcgiwrap_Instances_Value": "pynix_os.services.fcgiwrap:Fcgiwrap_Instances_Value",
        "Fcron": "pynix_os.services.fcron:Fcron",
        "Fediwall": "pynix_os.services.fediwall:Fediwall",
        "Fediwall_Nginx": "pynix_os.services.fediwall:Fediwall_Nginx",
        "Fediwall_Nginx_Listen_Item": "pynix_os.services.fediwall:Fediwall_Nginx_Listen_Item",
        "Fediwall_Nginx_Locations_Value": "pynix_os.services.fediwall:Fediwall_Nginx_Locations_Value",
        "Fediwall_Settings": "pynix_os.services.fediwall:Fediwall_Settings",
        "Feedbackd": "pynix_os.programs.feedbackd:Feedbackd",
        "Feishin": "pynix_os.services.feishin:Feishin",
        "Feishin_Caddy": "pynix_os.services.feishin:Feishin_Caddy",
        "Feishin_Caddy_VirtualHost": "pynix_os.services.feishin:Feishin_Caddy_VirtualHost",
        "Feishin_Nginx": "pynix_os.services.feishin:Feishin_Nginx",
        "Feishin_Nginx_VirtualHost": "pynix_os.services.feishin:Feishin_Nginx_VirtualHost",
        "Feishin_Nginx_VirtualHost_Listen_Item": "pynix_os.services.feishin:Feishin_Nginx_VirtualHost_Listen_Item",
        "Feishin_Nginx_VirtualHost_Locations_Value": "pynix_os.services.feishin:Feishin_Nginx_VirtualHost_Locations_Value",
        "Felix": "pynix_os.services.felix:Felix",
        "Ferm": "pynix_os.services.ferm:Ferm",
        "Ferretdb": "pynix_os.services.ferretdb:Ferretdb",
        "Ferretdb_Settings": "pynix_os.services.ferretdb:Ferretdb_Settings",
        "Fider": "pynix_os.services.fider:Fider",
        "Fider_Database": "pynix_os.services.fider:Fider_Database",
        "Filebeat": "pynix_os.services.filebeat:Filebeat",
        "Filebeat_Inputs_Value": "pynix_os.services.filebeat:Filebeat_Inputs_Value",
        "Filebeat_Modules_Value": "pynix_os.services.filebeat:Filebeat_Modules_Value",
        "Filebeat_Settings": "pynix_os.services.filebeat:Filebeat_Settings",
        "Filebrowser": "pynix_os.services.filebrowser:Filebrowser",
        "Filebrowser_Settings": "pynix_os.services.filebrowser:Filebrowser_Settings",
        "Firebird": "pynix_os.services.firebird:Firebird",
        "FireflyIii": "pynix_os.services.firefly_iii:FireflyIii",
        "FireflyIiiDataImporter": "pynix_os.services.firefly_iii_data_importer:FireflyIiiDataImporter",
        "FireflyIiiDataImporter_Settings": "pynix_os.services.firefly_iii_data_importer:FireflyIiiDataImporter_Settings",
        "FireflyIii_Settings": "pynix_os.services.firefly_iii:FireflyIii_Settings",
        "Firefox": "pynix_os.programs.firefox:Firefox",
        "FirefoxSyncserver": "pynix_os.services.firefox_syncserver:FirefoxSyncserver",
        "FirefoxSyncserver_Settings": "pynix_os.services.firefox_syncserver:FirefoxSyncserver_Settings",
        "FirefoxSyncserver_SingleNode": "pynix_os.services.firefox_syncserver:FirefoxSyncserver_SingleNode",
        "Firefox_NativeMessagingHosts": "pynix_os.programs.firefox:Firefox_NativeMessagingHosts",
        "Firejail": "pynix_os.programs.firejail:Firejail",
        "Firejail_WrappedBinaries_Value_Or": "pynix_os.programs.firejail:Firejail_WrappedBinaries_Value_Or",
        "Fireqos": "pynix_os.services.fireqos:Fireqos",
        "Networking_Firewall": "pynix_os.networking.firewall:Firewall",
        "Nix_Firewall": "pynix_os.nix.firewall:Firewall",
        "Firewall_Interfaces_Value": "pynix_os.networking.firewall:Firewall_Interfaces_Value",
        "Firewalld": "pynix_os.services.firewalld:Firewalld",
        "Firewalld_Services_Value": "pynix_os.services.firewalld:Firewalld_Services_Value",
        "Firewalld_Services_Value_Destination": "pynix_os.services.firewalld:Firewalld_Services_Value_Destination",
        "Firewalld_Services_Value_Ports_Item": "pynix_os.services.firewalld:Firewalld_Services_Value_Ports_Item",
        "Firewalld_Services_Value_Ports_Item_Port_Or": "pynix_os.services.firewalld:Firewalld_Services_Value_Ports_Item_Port_Or",
        "Firewalld_Settings": "pynix_os.services.firewalld:Firewalld_Settings",
        "Firewalld_Zones_Value": "pynix_os.services.firewalld:Firewalld_Zones_Value",
        "Firewalld_Zones_Value_ForwardPorts_Item": "pynix_os.services.firewalld:Firewalld_Zones_Value_ForwardPorts_Item",
        "Firewalld_Zones_Value_Ports_Item": "pynix_os.services.firewalld:Firewalld_Zones_Value_Ports_Item",
        "Firezone": "pynix_os.services.firezone:Firezone",
        "Firezone_Gateway": "pynix_os.services.firezone:Firezone_Gateway",
        "Firezone_GuiClient": "pynix_os.services.firezone:Firezone_GuiClient",
        "Firezone_HeadlessClient": "pynix_os.services.firezone:Firezone_HeadlessClient",
        "Firezone_Relay": "pynix_os.services.firezone:Firezone_Relay",
        "Firezone_Server": "pynix_os.services.firezone:Firezone_Server",
        "Firezone_Server_Api": "pynix_os.services.firezone:Firezone_Server_Api",
        "Firezone_Server_Api_Settings": "pynix_os.services.firezone:Firezone_Server_Api_Settings",
        "Firezone_Server_Domain": "pynix_os.services.firezone:Firezone_Server_Domain",
        "Firezone_Server_Nginx": "pynix_os.services.firezone:Firezone_Server_Nginx",
        "Firezone_Server_Settings": "pynix_os.services.firezone:Firezone_Server_Settings",
        "Firezone_Server_SettingsSecret": "pynix_os.services.firezone:Firezone_Server_SettingsSecret",
        "Firezone_Server_Smtp": "pynix_os.services.firezone:Firezone_Server_Smtp",
        "Firezone_Server_Web": "pynix_os.services.firezone:Firezone_Server_Web",
        "Fish": "pynix_os.programs.fish:Fish",
        "Fish_ShellFunctions_Value": "pynix_os.programs.fish:Fish_ShellFunctions_Value",
        "Fish_Vendor": "pynix_os.programs.fish:Fish_Vendor",
        "Fish_Vendor_Completions": "pynix_os.programs.fish:Fish_Vendor_Completions",
        "Fish_Vendor_Config": "pynix_os.programs.fish:Fish_Vendor_Config",
        "Fish_Vendor_Functions": "pynix_os.programs.fish:Fish_Vendor_Functions",
        "Flake": "pynix_os.nixpkgs.flake:Flake",
        "Flame": "pynix_os.services.flame:Flame",
        "Flame_Apps_Item": "pynix_os.services.flame:Flame_Apps_Item",
        "Flame_Categories_Item": "pynix_os.services.flame:Flame_Categories_Item",
        "Flame_Categories_Item_Bookmarks_Item": "pynix_os.services.flame:Flame_Categories_Item_Bookmarks_Item",
        "Flame_Settings": "pynix_os.services.flame:Flame_Settings",
        "Flannel": "pynix_os.services.flannel:Flannel",
        "Flannel_Etcd": "pynix_os.services.flannel:Flannel_Etcd",
        "FlapAlerted": "pynix_os.services.flap_alerted:FlapAlerted",
        "FlapAlerted_Settings": "pynix_os.services.flap_alerted:FlapAlerted_Settings",
        "Flaresolverr": "pynix_os.services.flaresolverr:Flaresolverr",
        "Flarum": "pynix_os.services.flarum:Flarum",
        "Flarum_Database": "pynix_os.services.flarum:Flarum_Database",
        "Flashprog": "pynix_os.programs.flashprog:Flashprog",
        "Flashrom": "pynix_os.programs.flashrom:Flashrom",
        "Flatpak": "pynix_os.services.flatpak:Flatpak",
        "Flexget": "pynix_os.services.flexget:Flexget",
        "FlexoptixApp": "pynix_os.programs.flexoptix_app:FlexoptixApp",
        "Flipperzero": "pynix_os.hardware.flipperzero:Flipperzero",
        "Flirc": "pynix_os.hardware.flirc:Flirc",
        "Flood": "pynix_os.services.flood:Flood",
        "FluentBit": "pynix_os.services.fluent_bit:FluentBit",
        "Fluentd": "pynix_os.services.fluentd:Fluentd",
        "Fluidd": "pynix_os.services.fluidd:Fluidd",
        "Fluidd_Nginx": "pynix_os.services.fluidd:Fluidd_Nginx",
        "Fluidd_Nginx_Listen_Item": "pynix_os.services.fluidd:Fluidd_Nginx_Listen_Item",
        "Fluidd_Nginx_Locations_Value": "pynix_os.services.fluidd:Fluidd_Nginx_Locations_Value",
        "Foldingathome": "pynix_os.services.foldingathome:Foldingathome",
        "FontDir": "pynix_os.fonts.fontDir:FontDir",
        "Fontconfig": "pynix_os.fonts.fontconfig:Fontconfig",
        "Fontconfig_Aliases_Value": "pynix_os.fonts.fontconfig:Fontconfig_Aliases_Value",
        "Fontconfig_DefaultFonts": "pynix_os.fonts.fontconfig:Fontconfig_DefaultFonts",
        "Fontconfig_Hinting": "pynix_os.fonts.fontconfig:Fontconfig_Hinting",
        "Fontconfig_Subpixel": "pynix_os.fonts.fontconfig:Fontconfig_Subpixel",
        "Fonts": "pynix_os.fonts.__options__:Fonts",
        "Foot": "pynix_os.programs.foot:Foot",
        "Foot_Xdg": "pynix_os.programs.foot:Foot_Xdg",
        "Forgejo": "pynix_os.services.forgejo:Forgejo",
        "ForgejoRunner": "pynix_os.services.forgejo_runner:ForgejoRunner",
        "ForgejoRunner_Instances_Value": "pynix_os.services.forgejo_runner:ForgejoRunner_Instances_Value",
        "ForgejoRunner_Instances_Value_Settings": "pynix_os.services.forgejo_runner:ForgejoRunner_Instances_Value_Settings",
        "ForgejoRunner_Instances_Value_Settings_ServerConnections_Value": "pynix_os.services.forgejo_runner:ForgejoRunner_Instances_Value_Settings_ServerConnections_Value",
        "Forgejo_Lfs": "pynix_os.services.forgejo:Forgejo_Lfs",
        "Forgejo_Secrets": "pynix_os.services.forgejo:Forgejo_Secrets",
        "Forgejo_Settings": "pynix_os.services.forgejo:Forgejo_Settings",
        "Foundationdb": "pynix_os.services.foundationdb:Foundationdb",
        "Foundationdb_Locality": "pynix_os.services.foundationdb:Foundationdb_Locality",
        "Foundationdb_Tls": "pynix_os.services.foundationdb:Foundationdb_Tls",
        "Fprintd": "pynix_os.services.fprintd:Fprintd",
        "Fprintd_Tod": "pynix_os.services.fprintd:Fprintd_Tod",
        "Fractalart": "pynix_os.services.fractalart:Fractalart",
        "FrameworkControl": "pynix_os.services.framework_control:FrameworkControl",
        "Freeciv": "pynix_os.services.freeciv:Freeciv",
        "Freeciv_Settings": "pynix_os.services.freeciv:Freeciv_Settings",
        "Freefall": "pynix_os.services.freefall:Freefall",
        "Freeradius": "pynix_os.services.freeradius:Freeradius",
        "Freescout": "pynix_os.services.freescout:Freescout",
        "Freescout_DatabaseSetup": "pynix_os.services.freescout:Freescout_DatabaseSetup",
        "Freeswitch": "pynix_os.services.freeswitch:Freeswitch",
        "Freshrss": "pynix_os.services.freshrss:Freshrss",
        "Freshrss_Api": "pynix_os.services.freshrss:Freshrss_Api",
        "Frigate": "pynix_os.services.frigate:Frigate",
        "Frigate_Settings": "pynix_os.services.frigate:Frigate_Settings",
        "Frigate_Settings_Cameras_Value": "pynix_os.services.frigate:Frigate_Settings_Cameras_Value",
        "Frigate_Settings_Cameras_Value_FfmpegInputs_Item": "pynix_os.services.frigate:Frigate_Settings_Cameras_Value_FfmpegInputs_Item",
        "FroideGovplan": "pynix_os.services.froide_govplan:FroideGovplan",
        "FroideGovplan_Settings": "pynix_os.services.froide_govplan:FroideGovplan_Settings",
        "Frp": "pynix_os.services.frp:Frp",
        "Frp_Instances_Value": "pynix_os.services.frp:Frp_Instances_Value",
        "Frr": "pynix_os.services.frr:Frr",
        "Frr_Babeld": "pynix_os.services.frr:Frr_Babeld",
        "Frr_Bfdd": "pynix_os.services.frr:Frr_Bfdd",
        "Frr_Bgpd": "pynix_os.services.frr:Frr_Bgpd",
        "Frr_Eigrpd": "pynix_os.services.frr:Frr_Eigrpd",
        "Frr_Fabricd": "pynix_os.services.frr:Frr_Fabricd",
        "Frr_Isisd": "pynix_os.services.frr:Frr_Isisd",
        "Frr_Ldpd": "pynix_os.services.frr:Frr_Ldpd",
        "Frr_Mgmtd": "pynix_os.services.frr:Frr_Mgmtd",
        "Frr_Nhrpd": "pynix_os.services.frr:Frr_Nhrpd",
        "Frr_Ospf6d": "pynix_os.services.frr:Frr_Ospf6d",
        "Frr_Ospfd": "pynix_os.services.frr:Frr_Ospfd",
        "Frr_Pathd": "pynix_os.services.frr:Frr_Pathd",
        "Frr_Pbrd": "pynix_os.services.frr:Frr_Pbrd",
        "Frr_Pim6d": "pynix_os.services.frr:Frr_Pim6d",
        "Frr_Pimd": "pynix_os.services.frr:Frr_Pimd",
        "Frr_Ripd": "pynix_os.services.frr:Frr_Ripd",
        "Frr_Ripngd": "pynix_os.services.frr:Frr_Ripngd",
        "Frr_Sharpd": "pynix_os.services.frr:Frr_Sharpd",
        "Frr_Staticd": "pynix_os.services.frr:Frr_Staticd",
        "Frr_Vrrpd": "pynix_os.services.frr:Frr_Vrrpd",
        "Frr_Zebra": "pynix_os.services.frr:Frr_Zebra",
        "Fstrim": "pynix_os.services.fstrim:Fstrim",
        "Fuse": "pynix_os.programs.fuse:Fuse",
        "FusionInventory": "pynix_os.services.fusionInventory:FusionInventory",
        "FwFanctrl": "pynix_os.hardware.fw_fanctrl:FwFanctrl",
        "FwFanctrl_Config": "pynix_os.hardware.fw_fanctrl:FwFanctrl_Config",
        "FwFanctrl_Config_Strategies_Value": "pynix_os.hardware.fw_fanctrl:FwFanctrl_Config_Strategies_Value",
        "FwFanctrl_Config_Strategies_Value_SpeedCurve_Item": "pynix_os.hardware.fw_fanctrl:FwFanctrl_Config_Strategies_Value_SpeedCurve_Item",
        "Fwupd": "pynix_os.services.fwupd:Fwupd",
        "Fwupd_DaemonSettings": "pynix_os.services.fwupd:Fwupd_DaemonSettings",
        "Fwupd_UefiCapsuleSettings": "pynix_os.services.fwupd:Fwupd_UefiCapsuleSettings",
        "Fzf": "pynix_os.programs.fzf:Fzf",
        "G3proxy": "pynix_os.services.g3proxy:G3proxy",
        "G810Led": "pynix_os.services.g810_led:G810Led",
        "Galene": "pynix_os.services.galene:Galene",
        "Gamemode": "pynix_os.programs.gamemode:Gamemode",
        "Gamescope": "pynix_os.programs.gamescope:Gamescope",
        "GammuSmsd": "pynix_os.services.gammu_smsd:GammuSmsd",
        "GammuSmsd_Backend": "pynix_os.services.gammu_smsd:GammuSmsd_Backend",
        "GammuSmsd_Backend_Files": "pynix_os.services.gammu_smsd:GammuSmsd_Backend_Files",
        "GammuSmsd_Backend_Sql": "pynix_os.services.gammu_smsd:GammuSmsd_Backend_Sql",
        "GammuSmsd_Device": "pynix_os.services.gammu_smsd:GammuSmsd_Device",
        "GammuSmsd_ExtraConfig": "pynix_os.services.gammu_smsd:GammuSmsd_ExtraConfig",
        "GammuSmsd_Log": "pynix_os.services.gammu_smsd:GammuSmsd_Log",
        "Gancio": "pynix_os.services.gancio:Gancio",
        "Gancio_Nginx": "pynix_os.services.gancio:Gancio_Nginx",
        "Gancio_Nginx_Listen_Item": "pynix_os.services.gancio:Gancio_Nginx_Listen_Item",
        "Gancio_Nginx_Locations_Value": "pynix_os.services.gancio:Gancio_Nginx_Locations_Value",
        "Gancio_Settings": "pynix_os.services.gancio:Gancio_Settings",
        "Garage": "pynix_os.services.garage:Garage",
        "Garage_Settings": "pynix_os.services.garage:Garage_Settings",
        "Garm": "pynix_os.services.garm:Garm",
        "Garm_Settings": "pynix_os.services.garm:Garm_Settings",
        "Gatus": "pynix_os.services.gatus:Gatus",
        "Gatus_Settings": "pynix_os.services.gatus:Gatus_Settings",
        "Gc": "pynix_os.nix.gc:Gc",
        "GdkPixbuf": "pynix_os.programs.gdk_pixbuf:GdkPixbuf",
        "Gdomap": "pynix_os.services.gdomap:Gdomap",
        "Geary": "pynix_os.programs.geary:Geary",
        "Gemstash": "pynix_os.services.gemstash:Gemstash",
        "Gemstash_Settings": "pynix_os.services.gemstash:Gemstash_Settings",
        "Geoclue2": "pynix_os.services.geoclue2:Geoclue2",
        "Geoclue2_AppConfig_Value": "pynix_os.services.geoclue2:Geoclue2_AppConfig_Value",
        "Geoipupdate": "pynix_os.services.geoipupdate:Geoipupdate",
        "Geoipupdate_Settings": "pynix_os.services.geoipupdate:Geoipupdate_Settings",
        "Geoserver": "pynix_os.services.geoserver:Geoserver",
        "Geph": "pynix_os.services.geph:Geph",
        "Gerbil": "pynix_os.services.gerbil:Gerbil",
        "Gerrit": "pynix_os.services.gerrit:Gerrit",
        "Getaddrinfo": "pynix_os.networking.getaddrinfo:Getaddrinfo",
        "Getty": "pynix_os.services.getty:Getty",
        "Ghidra": "pynix_os.programs.ghidra:Ghidra",
        "Ghostunnel": "pynix_os.services.ghostunnel:Ghostunnel",
        "Ghostunnel_Servers_Value": "pynix_os.services.ghostunnel:Ghostunnel_Servers_Value",
        "Git": "pynix_os.programs.git:Git",
        "GitDaemon": "pynix_os.services.gitDaemon:GitDaemon",
        "GitWorktreeSwitcher": "pynix_os.programs.git_worktree_switcher:GitWorktreeSwitcher",
        "Git_Lfs": "pynix_os.programs.git:Git_Lfs",
        "Git_Prompt": "pynix_os.programs.git:Git_Prompt",
        "Gitea": "pynix_os.services.gitea:Gitea",
        "GiteaActionsRunner": "pynix_os.services.gitea_actions_runner:GiteaActionsRunner",
        "GiteaActionsRunner_Instances_Value": "pynix_os.services.gitea_actions_runner:GiteaActionsRunner_Instances_Value",
        "GiteaActionsRunner_Instances_Value_Settings": "pynix_os.services.gitea_actions_runner:GiteaActionsRunner_Instances_Value_Settings",
        "Gitea_Lfs": "pynix_os.services.gitea:Gitea_Lfs",
        "Gitea_Settings": "pynix_os.services.gitea:Gitea_Settings",
        "Gitlab": "pynix_os.services.gitlab:Gitlab",
        "GitlabRunner": "pynix_os.services.gitlab_runner:GitlabRunner",
        "GitlabRunner_ClearDockerCache": "pynix_os.services.gitlab_runner:GitlabRunner_ClearDockerCache",
        "GitlabRunner_Services_Value": "pynix_os.services.gitlab_runner:GitlabRunner_Services_Value",
        "GitlabRunner_Settings": "pynix_os.services.gitlab_runner:GitlabRunner_Settings",
        "Gitlab_Backup": "pynix_os.services.gitlab:Gitlab_Backup",
        "Gitlab_Logrotate": "pynix_os.services.gitlab:Gitlab_Logrotate",
        "Gitlab_Packages": "pynix_os.services.gitlab:Gitlab_Packages",
        "Gitlab_Pages": "pynix_os.services.gitlab:Gitlab_Pages",
        "Gitlab_Pages_Settings": "pynix_os.services.gitlab:Gitlab_Pages_Settings",
        "Gitlab_Puma": "pynix_os.services.gitlab:Gitlab_Puma",
        "Gitlab_Registry": "pynix_os.services.gitlab:Gitlab_Registry",
        "Gitlab_Registry_GarbageCollection": "pynix_os.services.gitlab:Gitlab_Registry_GarbageCollection",
        "Gitlab_Registry_Settings": "pynix_os.services.gitlab:Gitlab_Registry_Settings",
        "Gitlab_Secrets": "pynix_os.services.gitlab:Gitlab_Secrets",
        "Gitlab_Sidekiq": "pynix_os.services.gitlab:Gitlab_Sidekiq",
        "Gitlab_Sidekiq_MemoryKiller": "pynix_os.services.gitlab:Gitlab_Sidekiq_MemoryKiller",
        "Gitlab_Smtp": "pynix_os.services.gitlab:Gitlab_Smtp",
        "Gitlab_Workhorse": "pynix_os.services.gitlab:Gitlab_Workhorse",
        "Gitolite": "pynix_os.services.gitolite:Gitolite",
        "Gitweb": "pynix_os.services.gitweb:Gitweb",
        "Gitweb_Nginx": "pynix_os.services.gitweb:Gitweb_Nginx",
        "Glance": "pynix_os.services.glance:Glance",
        "Glance_Settings": "pynix_os.services.glance:Glance_Settings",
        "Glances": "pynix_os.services.glances:Glances",
        "Glasgow": "pynix_os.hardware.glasgow:Glasgow",
        "Glitchtip": "pynix_os.services.glitchtip:Glitchtip",
        "Glitchtip_Database": "pynix_os.services.glitchtip:Glitchtip_Database",
        "Glitchtip_Nginx": "pynix_os.services.glitchtip:Glitchtip_Nginx",
        "Glitchtip_Redis": "pynix_os.services.glitchtip:Glitchtip_Redis",
        "Glitchtip_Settings": "pynix_os.services.glitchtip:Glitchtip_Settings",
        "GlpiAgent": "pynix_os.services.glpiAgent:GlpiAgent",
        "Glusterfs": "pynix_os.services.glusterfs:Glusterfs",
        "Glusterfs_TlsSettings": "pynix_os.services.glusterfs:Glusterfs_TlsSettings",
        "Gmediarender": "pynix_os.services.gmediarender:Gmediarender",
        "Environment_Gnome": "pynix_os.environment.gnome:Gnome",
        "Services_Gnome": "pynix_os.services.gnome:Gnome",
        "GnomeDisks": "pynix_os.programs.gnome_disks:GnomeDisks",
        "GnomeTerminal": "pynix_os.programs.gnome_terminal:GnomeTerminal",
        "Gnome_AtSpi2Core": "pynix_os.services.gnome:Gnome_AtSpi2Core",
        "Gnome_CoreApps": "pynix_os.services.gnome:Gnome_CoreApps",
        "Gnome_CoreDeveloperTools": "pynix_os.services.gnome:Gnome_CoreDeveloperTools",
        "Gnome_CoreOsServices": "pynix_os.services.gnome:Gnome_CoreOsServices",
        "Gnome_CoreShell": "pynix_os.services.gnome:Gnome_CoreShell",
        "Gnome_EvolutionDataServer": "pynix_os.services.gnome:Gnome_EvolutionDataServer",
        "Gnome_Games": "pynix_os.services.gnome:Gnome_Games",
        "Gnome_GcrSshAgent": "pynix_os.services.gnome:Gnome_GcrSshAgent",
        "Gnome_GlibNetworking": "pynix_os.services.gnome:Gnome_GlibNetworking",
        "Gnome_GnomeBrowserConnector": "pynix_os.services.gnome:Gnome_GnomeBrowserConnector",
        "Gnome_GnomeInitialSetup": "pynix_os.services.gnome:Gnome_GnomeInitialSetup",
        "Gnome_GnomeKeyring": "pynix_os.services.gnome:Gnome_GnomeKeyring",
        "Gnome_GnomeOnlineAccounts": "pynix_os.services.gnome:Gnome_GnomeOnlineAccounts",
        "Gnome_GnomeRemoteDesktop": "pynix_os.services.gnome:Gnome_GnomeRemoteDesktop",
        "Gnome_GnomeSettingsDaemon": "pynix_os.services.gnome:Gnome_GnomeSettingsDaemon",
        "Gnome_GnomeSoftware": "pynix_os.services.gnome:Gnome_GnomeSoftware",
        "Gnome_GnomeUserShare": "pynix_os.services.gnome:Gnome_GnomeUserShare",
        "Gnome_Localsearch": "pynix_os.services.gnome:Gnome_Localsearch",
        "Gnome_Rygel": "pynix_os.services.gnome:Gnome_Rygel",
        "Gnome_Sushi": "pynix_os.services.gnome:Gnome_Sushi",
        "Gnome_Tinysparql": "pynix_os.services.gnome:Gnome_Tinysparql",
        "Gns3Server": "pynix_os.services.gns3_server:Gns3Server",
        "Gns3Server_Auth": "pynix_os.services.gns3_server:Gns3Server_Auth",
        "Gns3Server_Dynamips": "pynix_os.services.gns3_server:Gns3Server_Dynamips",
        "Gns3Server_Log": "pynix_os.services.gns3_server:Gns3Server_Log",
        "Gns3Server_Settings": "pynix_os.services.gns3_server:Gns3Server_Settings",
        "Gns3Server_Ssl": "pynix_os.services.gns3_server:Gns3Server_Ssl",
        "Gns3Server_Ubridge": "pynix_os.services.gns3_server:Gns3Server_Ubridge",
        "Gns3Server_Vpcs": "pynix_os.services.gns3_server:Gns3Server_Vpcs",
        "Gnunet": "pynix_os.services.gnunet:Gnunet",
        "Gnunet_FileSharing": "pynix_os.services.gnunet:Gnunet_FileSharing",
        "Gnunet_Load": "pynix_os.services.gnunet:Gnunet_Load",
        "Gnunet_Tcp": "pynix_os.services.gnunet:Gnunet_Tcp",
        "Gnunet_Udp": "pynix_os.services.gnunet:Gnunet_Udp",
        "Gnupg": "pynix_os.programs.gnupg:Gnupg",
        "Gnupg_Agent": "pynix_os.programs.gnupg:Gnupg_Agent",
        "Gnupg_Dirmngr": "pynix_os.programs.gnupg:Gnupg_Dirmngr",
        "Go2rtc": "pynix_os.services.go2rtc:Go2rtc",
        "Go2rtc_Settings": "pynix_os.services.go2rtc:Go2rtc_Settings",
        "GoAutoconfig": "pynix_os.services.go_autoconfig:GoAutoconfig",
        "GoAutoconfig_Settings": "pynix_os.services.go_autoconfig:GoAutoconfig_Settings",
        "GoCamo": "pynix_os.services.go_camo:GoCamo",
        "GoCspCollector": "pynix_os.services.go_csp_collector:GoCspCollector",
        "GoCspCollector_Settings": "pynix_os.services.go_csp_collector:GoCspCollector_Settings",
        "GoHttpbin": "pynix_os.services.go_httpbin:GoHttpbin",
        "GoHttpbin_Settings": "pynix_os.services.go_httpbin:GoHttpbin_Settings",
        "GoShadowsocks2": "pynix_os.services.go_shadowsocks2:GoShadowsocks2",
        "GoShadowsocks2_Server": "pynix_os.services.go_shadowsocks2:GoShadowsocks2_Server",
        "Goatcounter": "pynix_os.services.goatcounter:Goatcounter",
        "Gobgpd": "pynix_os.services.gobgpd:Gobgpd",
        "GocdAgent": "pynix_os.services.gocd_agent:GocdAgent",
        "GocdServer": "pynix_os.services.gocd_server:GocdServer",
        "Gocron": "pynix_os.services.gocron:Gocron",
        "Gocron_Hardening": "pynix_os.services.gocron:Gocron_Hardening",
        "Godns": "pynix_os.services.godns:Godns",
        "Godns_Settings": "pynix_os.services.godns:Godns_Settings",
        "Goeland": "pynix_os.services.goeland:Goeland",
        "Gokapi": "pynix_os.services.gokapi:Gokapi",
        "Gokapi_Environment": "pynix_os.services.gokapi:Gokapi_Environment",
        "Gokapi_Settings": "pynix_os.services.gokapi:Gokapi_Settings",
        "Gollum": "pynix_os.services.gollum:Gollum",
        "Gonic": "pynix_os.services.gonic:Gonic",
        "GoogleChrome": "pynix_os.programs.google_chrome:GoogleChrome",
        "GoogleOsLogin": "pynix_os.security.googleOsLogin:GoogleOsLogin",
        "Gophernicus": "pynix_os.services.gophernicus:Gophernicus",
        "Goss": "pynix_os.services.goss:Goss",
        "Goss_Settings": "pynix_os.services.goss:Goss_Settings",
        "Gotenberg": "pynix_os.services.gotenberg:Gotenberg",
        "Gotenberg_Chromium": "pynix_os.services.gotenberg:Gotenberg_Chromium",
        "Gotenberg_DownloadFrom": "pynix_os.services.gotenberg:Gotenberg_DownloadFrom",
        "Gotenberg_Libreoffice": "pynix_os.services.gotenberg:Gotenberg_Libreoffice",
        "Gotenberg_PdfEngines": "pynix_os.services.gotenberg:Gotenberg_PdfEngines",
        "Gotify": "pynix_os.services.gotify:Gotify",
        "Gotosocial": "pynix_os.services.gotosocial:Gotosocial",
        "Goupile": "pynix_os.services.goupile:Goupile",
        "Goupile_Settings": "pynix_os.services.goupile:Goupile_Settings",
        "Govee2mqtt": "pynix_os.services.govee2mqtt:Govee2mqtt",
        "GoxlrUtility": "pynix_os.services.goxlr_utility:GoxlrUtility",
        "GoxlrUtility_AutoStart": "pynix_os.services.goxlr_utility:GoxlrUtility_AutoStart",
        "Gpaste": "pynix_os.programs.gpaste:Gpaste",
        "GpgSmartcards": "pynix_os.hardware.gpgSmartcards:GpgSmartcards",
        "Gphoto2": "pynix_os.programs.gphoto2:Gphoto2",
        "Gpm": "pynix_os.services.gpm:Gpm",
        "Gpsd": "pynix_os.services.gpsd:Gpsd",
        "GpuScreenRecorder": "pynix_os.programs.gpu_screen_recorder:GpuScreenRecorder",
        "GpuScreenRecorder_Ui": "pynix_os.programs.gpu_screen_recorder:GpuScreenRecorder_Ui",
        "Grafana": "pynix_os.services.grafana:Grafana",
        "GrafanaImageRenderer": "pynix_os.services.grafana_image_renderer:GrafanaImageRenderer",
        "GrafanaImageRenderer_Settings": "pynix_os.services.grafana_image_renderer:GrafanaImageRenderer_Settings",
        "GrafanaReporter": "pynix_os.services.grafana_reporter:GrafanaReporter",
        "GrafanaReporter_Grafana": "pynix_os.services.grafana_reporter:GrafanaReporter_Grafana",
        "GrafanaToNtfy": "pynix_os.services.grafana_to_ntfy:GrafanaToNtfy",
        "GrafanaToNtfy_Settings": "pynix_os.services.grafana_to_ntfy:GrafanaToNtfy_Settings",
        "Grafana_Provision": "pynix_os.services.grafana:Grafana_Provision",
        "Grafana_Provision_Alerting": "pynix_os.services.grafana:Grafana_Provision_Alerting",
        "Grafana_Provision_Alerting_ContactPoints": "pynix_os.services.grafana:Grafana_Provision_Alerting_ContactPoints",
        "Grafana_Provision_Alerting_ContactPoints_Settings": "pynix_os.services.grafana:Grafana_Provision_Alerting_ContactPoints_Settings",
        "Grafana_Provision_Alerting_ContactPoints_Settings_ContactPoints_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_ContactPoints_Settings_ContactPoints_Item",
        "Grafana_Provision_Alerting_ContactPoints_Settings_DeleteContactPoints_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_ContactPoints_Settings_DeleteContactPoints_Item",
        "Grafana_Provision_Alerting_MuteTimings": "pynix_os.services.grafana:Grafana_Provision_Alerting_MuteTimings",
        "Grafana_Provision_Alerting_MuteTimings_Settings": "pynix_os.services.grafana:Grafana_Provision_Alerting_MuteTimings_Settings",
        "Grafana_Provision_Alerting_MuteTimings_Settings_DeleteMuteTimes_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_MuteTimings_Settings_DeleteMuteTimes_Item",
        "Grafana_Provision_Alerting_MuteTimings_Settings_MuteTimes_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_MuteTimings_Settings_MuteTimes_Item",
        "Grafana_Provision_Alerting_Policies": "pynix_os.services.grafana:Grafana_Provision_Alerting_Policies",
        "Grafana_Provision_Alerting_Policies_Settings": "pynix_os.services.grafana:Grafana_Provision_Alerting_Policies_Settings",
        "Grafana_Provision_Alerting_Policies_Settings_Policies_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_Policies_Settings_Policies_Item",
        "Grafana_Provision_Alerting_Rules": "pynix_os.services.grafana:Grafana_Provision_Alerting_Rules",
        "Grafana_Provision_Alerting_Rules_Settings": "pynix_os.services.grafana:Grafana_Provision_Alerting_Rules_Settings",
        "Grafana_Provision_Alerting_Rules_Settings_DeleteRules_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_Rules_Settings_DeleteRules_Item",
        "Grafana_Provision_Alerting_Rules_Settings_Groups_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_Rules_Settings_Groups_Item",
        "Grafana_Provision_Alerting_Templates": "pynix_os.services.grafana:Grafana_Provision_Alerting_Templates",
        "Grafana_Provision_Alerting_Templates_Settings": "pynix_os.services.grafana:Grafana_Provision_Alerting_Templates_Settings",
        "Grafana_Provision_Alerting_Templates_Settings_DeleteTemplates_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_Templates_Settings_DeleteTemplates_Item",
        "Grafana_Provision_Alerting_Templates_Settings_Templates_Item": "pynix_os.services.grafana:Grafana_Provision_Alerting_Templates_Settings_Templates_Item",
        "Grafana_Provision_Dashboards": "pynix_os.services.grafana:Grafana_Provision_Dashboards",
        "Grafana_Provision_Dashboards_Settings": "pynix_os.services.grafana:Grafana_Provision_Dashboards_Settings",
        "Grafana_Provision_Dashboards_Settings_Providers_Item": "pynix_os.services.grafana:Grafana_Provision_Dashboards_Settings_Providers_Item",
        "Grafana_Provision_Datasources": "pynix_os.services.grafana:Grafana_Provision_Datasources",
        "Grafana_Provision_Datasources_Settings": "pynix_os.services.grafana:Grafana_Provision_Datasources_Settings",
        "Grafana_Provision_Datasources_Settings_Datasources_Item": "pynix_os.services.grafana:Grafana_Provision_Datasources_Settings_Datasources_Item",
        "Grafana_Provision_Datasources_Settings_DeleteDatasources_Item": "pynix_os.services.grafana:Grafana_Provision_Datasources_Settings_DeleteDatasources_Item",
        "Grafana_Settings": "pynix_os.services.grafana:Grafana_Settings",
        "GraphicalDesktop": "pynix_os.services.graphical_desktop:GraphicalDesktop",
        "Graphics": "pynix_os.hardware.graphics:Graphics",
        "Graphite": "pynix_os.services.graphite:Graphite",
        "Graphite_Carbon": "pynix_os.services.graphite:Graphite_Carbon",
        "Graphite_Seyren": "pynix_os.services.graphite:Graphite_Seyren",
        "Graphite_Web": "pynix_os.services.graphite:Graphite_Web",
        "Grav": "pynix_os.services.grav:Grav",
        "Graylog": "pynix_os.services.graylog:Graylog",
        "Greenclip": "pynix_os.services.greenclip:Greenclip",
        "Greenlight": "pynix_os.services.greenlight:Greenlight",
        "Greenlight_Database": "pynix_os.services.greenlight:Greenlight_Database",
        "Greenlight_Redis": "pynix_os.services.greenlight:Greenlight_Redis",
        "Greenlight_Settings": "pynix_os.services.greenlight:Greenlight_Settings",
        "Greetd": "pynix_os.services.greetd:Greetd",
        "Grist": "pynix_os.services.grist:Grist",
        "Grist_Environment": "pynix_os.services.grist:Grist_Environment",
        "Grocy": "pynix_os.services.grocy:Grocy",
        "Grocy_Nginx": "pynix_os.services.grocy:Grocy_Nginx",
        "Grocy_Phpfpm": "pynix_os.services.grocy:Grocy_Phpfpm",
        "Grocy_Settings": "pynix_os.services.grocy:Grocy_Settings",
        "Grocy_Settings_Calendar": "pynix_os.services.grocy:Grocy_Settings_Calendar",
        "Gs1200Exporter": "pynix_os.services.gs1200_exporter:Gs1200Exporter",
        "Gtklock": "pynix_os.programs.gtklock:Gtklock",
        "GuacamoleClient": "pynix_os.services.guacamole_client:GuacamoleClient",
        "GuacamoleClient_Settings": "pynix_os.services.guacamole_client:GuacamoleClient_Settings",
        "GuacamoleServer": "pynix_os.services.guacamole_server:GuacamoleServer",
        "Guix": "pynix_os.services.guix:Guix",
        "Guix_Gc": "pynix_os.services.guix:Guix_Gc",
        "Guix_Publish": "pynix_os.services.guix:Guix_Publish",
        "Guix_Substituters": "pynix_os.services.guix:Guix_Substituters",
        "Gvfs": "pynix_os.services.gvfs:Gvfs",
        "Gvpe": "pynix_os.services.gvpe:Gvpe",
        "H2o": "pynix_os.services.h2o:H2o",
        "H2o_Hosts_Value": "pynix_os.services.h2o:H2o_Hosts_Value",
        "H2o_Hosts_Value_Acme": "pynix_os.services.h2o:H2o_Hosts_Value_Acme",
        "H2o_Hosts_Value_Http": "pynix_os.services.h2o:H2o_Hosts_Value_Http",
        "H2o_Hosts_Value_Tls": "pynix_os.services.h2o:H2o_Hosts_Value_Tls",
        "H2o_Hosts_Value_Tls_Identity_Item": "pynix_os.services.h2o:H2o_Hosts_Value_Tls_Identity_Item",
        "Hackrf": "pynix_os.hardware.hackrf:Hackrf",
        "Hadoop": "pynix_os.services.hadoop:Hadoop",
        "Hadoop_GatewayRole": "pynix_os.services.hadoop:Hadoop_GatewayRole",
        "Hadoop_Hbase": "pynix_os.services.hadoop:Hadoop_Hbase",
        "Hadoop_Hbase_Master": "pynix_os.services.hadoop:Hadoop_Hbase_Master",
        "Hadoop_Hbase_RegionServer": "pynix_os.services.hadoop:Hadoop_Hbase_RegionServer",
        "Hadoop_Hbase_Rest": "pynix_os.services.hadoop:Hadoop_Hbase_Rest",
        "Hadoop_Hbase_Thrift": "pynix_os.services.hadoop:Hadoop_Hbase_Thrift",
        "Hadoop_Hdfs": "pynix_os.services.hadoop:Hadoop_Hdfs",
        "Hadoop_Hdfs_Datanode": "pynix_os.services.hadoop:Hadoop_Hdfs_Datanode",
        "Hadoop_Hdfs_Datanode_DataDirs_Item": "pynix_os.services.hadoop:Hadoop_Hdfs_Datanode_DataDirs_Item",
        "Hadoop_Hdfs_Httpfs": "pynix_os.services.hadoop:Hadoop_Hdfs_Httpfs",
        "Hadoop_Hdfs_Journalnode": "pynix_os.services.hadoop:Hadoop_Hdfs_Journalnode",
        "Hadoop_Hdfs_Namenode": "pynix_os.services.hadoop:Hadoop_Hdfs_Namenode",
        "Hadoop_Hdfs_Zkfc": "pynix_os.services.hadoop:Hadoop_Hdfs_Zkfc",
        "Hadoop_Yarn": "pynix_os.services.hadoop:Hadoop_Yarn",
        "Hadoop_Yarn_Nodemanager": "pynix_os.services.hadoop:Hadoop_Yarn_Nodemanager",
        "Hadoop_Yarn_Nodemanager_Resource": "pynix_os.services.hadoop:Hadoop_Yarn_Nodemanager_Resource",
        "Hadoop_Yarn_Resourcemanager": "pynix_os.services.hadoop:Hadoop_Yarn_Resourcemanager",
        "Haguichi": "pynix_os.programs.haguichi:Haguichi",
        "Hamster": "pynix_os.programs.hamster:Hamster",
        "HandheldDaemon": "pynix_os.services.handheld_daemon:HandheldDaemon",
        "HandheldDaemon_Adjustor": "pynix_os.services.handheld_daemon:HandheldDaemon_Adjustor",
        "HandheldDaemon_Ui": "pynix_os.services.handheld_daemon:HandheldDaemon_Ui",
        "Hans": "pynix_os.services.hans:Hans",
        "Hans_Clients_Value": "pynix_os.services.hans:Hans_Clients_Value",
        "Hans_Server": "pynix_os.services.hans:Hans_Server",
        "Haproxy": "pynix_os.services.haproxy:Haproxy",
        "Hardware": "pynix_os.hardware.__options__:Hardware",
        "Services_Hardware": "pynix_os.services.hardware:Hardware",
        "Hardware_Argonone": "pynix_os.services.hardware:Hardware_Argonone",
        "Hardware_Bolt": "pynix_os.services.hardware:Hardware_Bolt",
        "Hardware_DeepcoolDigitalLinux": "pynix_os.services.hardware:Hardware_DeepcoolDigitalLinux",
        "Hardware_DellBiosFanControl": "pynix_os.services.hardware:Hardware_DellBiosFanControl",
        "Hardware_Lcd": "pynix_os.services.hardware:Hardware_Lcd",
        "Hardware_Lcd_Client": "pynix_os.services.hardware:Hardware_Lcd_Client",
        "Hardware_Lcd_Server": "pynix_os.services.hardware:Hardware_Lcd_Server",
        "Hardware_Openrgb": "pynix_os.services.hardware:Hardware_Openrgb",
        "Hardware_Openrgb_Server": "pynix_os.services.hardware:Hardware_Openrgb_Server",
        "Hardware_Pommed": "pynix_os.services.hardware:Hardware_Pommed",
        "Harmonia": "pynix_os.services.harmonia:Harmonia",
        "Harmonia_Cache": "pynix_os.services.harmonia:Harmonia_Cache",
        "Harmonia_Daemon": "pynix_os.services.harmonia:Harmonia_Daemon",
        "Harmonia_Gc": "pynix_os.services.harmonia:Harmonia_Gc",
        "HasteServer": "pynix_os.services.haste_server:HasteServer",
        "Hatsu": "pynix_os.services.hatsu:Hatsu",
        "Hatsu_Settings": "pynix_os.services.hatsu:Hatsu_Settings",
        "Haveged": "pynix_os.services.haveged:Haveged",
        "Haven": "pynix_os.services.haven:Haven",
        "HbaseStandalone": "pynix_os.services.hbase_standalone:HbaseStandalone",
        "Hdapsd": "pynix_os.services.hdapsd:Hdapsd",
        "Hddfancontrol": "pynix_os.services.hddfancontrol:Hddfancontrol",
        "Hddfancontrol_Settings_Value": "pynix_os.services.hddfancontrol:Hddfancontrol_Settings_Value",
        "Headphones": "pynix_os.services.headphones:Headphones",
        "Headplane": "pynix_os.services.headplane:Headplane",
        "Headplane_Agent": "pynix_os.services.headplane:Headplane_Agent",
        "Headplane_Settings": "pynix_os.services.headplane:Headplane_Settings",
        "Headplane_Settings_Headscale": "pynix_os.services.headplane:Headplane_Settings_Headscale",
        "Headplane_Settings_Integration": "pynix_os.services.headplane:Headplane_Settings_Integration",
        "Headplane_Settings_Integration_Agent": "pynix_os.services.headplane:Headplane_Settings_Integration_Agent",
        "Headplane_Settings_Integration_Proc": "pynix_os.services.headplane:Headplane_Settings_Integration_Proc",
        "Headplane_Settings_Oidc": "pynix_os.services.headplane:Headplane_Settings_Oidc",
        "Headplane_Settings_Server": "pynix_os.services.headplane:Headplane_Settings_Server",
        "Headplane_Settings_Server_ProxyAuth": "pynix_os.services.headplane:Headplane_Settings_Server_ProxyAuth",
        "Headscale": "pynix_os.services.headscale:Headscale",
        "Headscale_Settings": "pynix_os.services.headscale:Headscale_Settings",
        "Headscale_Settings_DnsExtraRecords_Item": "pynix_os.services.headscale:Headscale_Settings_DnsExtraRecords_Item",
        "Healthchecks": "pynix_os.services.healthchecks:Healthchecks",
        "Healthchecks_Settings": "pynix_os.services.healthchecks:Healthchecks_Settings",
        "Heapster": "pynix_os.services.heapster:Heapster",
        "Heartbeat": "pynix_os.services.heartbeat:Heartbeat",
        "Hebbot": "pynix_os.services.hebbot:Hebbot",
        "Hebbot_Templates": "pynix_os.services.hebbot:Hebbot_Templates",
        "Hedgedoc": "pynix_os.services.hedgedoc:Hedgedoc",
        "Hedgedoc_Settings": "pynix_os.services.hedgedoc:Hedgedoc_Settings",
        "Heisenbridge": "pynix_os.services.heisenbridge:Heisenbridge",
        "Heisenbridge_Identd": "pynix_os.services.heisenbridge:Heisenbridge_Identd",
        "Heisenbridge_Namespaces": "pynix_os.services.heisenbridge:Heisenbridge_Namespaces",
        "HerculesCiAgent": "pynix_os.services.hercules_ci_agent:HerculesCiAgent",
        "HerculesCiAgent_Settings": "pynix_os.services.hercules_ci_agent:HerculesCiAgent_Settings",
        "HickoryDns": "pynix_os.services.hickory_dns:HickoryDns",
        "HickoryDns_Settings": "pynix_os.services.hickory_dns:HickoryDns_Settings",
        "HickoryDns_Settings_Zones_Item": "pynix_os.services.hickory_dns:HickoryDns_Settings_Zones_Item",
        "HidFanatecff": "pynix_os.hardware.hid_fanatecff:HidFanatecff",
        "Hister": "pynix_os.services.hister:Hister",
        "Hitch": "pynix_os.services.hitch:Hitch",
        "Hitch_OcspStapling": "pynix_os.services.hitch:Hitch_OcspStapling",
        "HledgerWeb": "pynix_os.services.hledger_web:HledgerWeb",
        "Hockeypuck": "pynix_os.services.hockeypuck:Hockeypuck",
        "HologramAgent": "pynix_os.services.hologram_agent:HologramAgent",
        "HologramServer": "pynix_os.services.hologram_server:HologramServer",
        "HomeAssistant": "pynix_os.services.home_assistant:HomeAssistant",
        "HomeAssistantMatterHub": "pynix_os.services.home_assistant_matter_hub:HomeAssistantMatterHub",
        "HomeAssistantMatterHub_Settings": "pynix_os.services.home_assistant_matter_hub:HomeAssistantMatterHub_Settings",
        "HomeAssistant_Blueprints": "pynix_os.services.home_assistant:HomeAssistant_Blueprints",
        "HomeAssistant_Config": "pynix_os.services.home_assistant:HomeAssistant_Config",
        "Homebox": "pynix_os.services.homebox:Homebox",
        "Homebox_Database": "pynix_os.services.homebox:Homebox_Database",
        "Homebox_Secrets": "pynix_os.services.homebox:Homebox_Secrets",
        "Homebox_Settings": "pynix_os.services.homebox:Homebox_Settings",
        "Homebridge": "pynix_os.services.homebridge:Homebridge",
        "Homebridge_Settings": "pynix_os.services.homebridge:Homebridge_Settings",
        "Homebridge_Settings_Accessories_Item": "pynix_os.services.homebridge:Homebridge_Settings_Accessories_Item",
        "Homebridge_Settings_Platforms_Item": "pynix_os.services.homebridge:Homebridge_Settings_Platforms_Item",
        "Homebridge_UiSettings": "pynix_os.services.homebridge:Homebridge_UiSettings",
        "Homed": "pynix_os.services.homed:Homed",
        "Homed_Settings": "pynix_os.services.homed:Homed_Settings",
        "Homed_Settings_Home": "pynix_os.services.homed:Homed_Settings_Home",
        "HomepageDashboard": "pynix_os.services.homepage_dashboard:HomepageDashboard",
        "Homer": "pynix_os.services.homer:Homer",
        "Homer_VirtualHost": "pynix_os.services.homer:Homer_VirtualHost",
        "Homer_VirtualHost_Caddy": "pynix_os.services.homer:Homer_VirtualHost_Caddy",
        "Homer_VirtualHost_Nginx": "pynix_os.services.homer:Homer_VirtualHost_Nginx",
        "Hoogle": "pynix_os.services.hoogle:Hoogle",
        "Hostapd": "pynix_os.services.hostapd:Hostapd",
        "Hostapd_Radios_Value": "pynix_os.services.hostapd:Hostapd_Radios_Value",
        "Hostapd_Radios_Value_Networks_Value": "pynix_os.services.hostapd:Hostapd_Radios_Value_Networks_Value",
        "Hostapd_Radios_Value_Networks_Value_AuthenticationSaePasswords_Item": "pynix_os.services.hostapd:Hostapd_Radios_Value_Networks_Value_AuthenticationSaePasswords_Item",
        "Hostapd_Radios_Value_Networks_Value_Settings": "pynix_os.services.hostapd:Hostapd_Radios_Value_Networks_Value_Settings",
        "Hostapd_Radios_Value_Settings": "pynix_os.services.hostapd:Hostapd_Radios_Value_Settings",
        "Hound": "pynix_os.services.hound:Hound",
        "Howdy": "pynix_os.services.howdy:Howdy",
        "Hqplayerd": "pynix_os.services.hqplayerd:Hqplayerd",
        "Hqplayerd_Auth": "pynix_os.services.hqplayerd:Hqplayerd_Auth",
        "Htop": "pynix_os.programs.htop:Htop",
        "Htpdate": "pynix_os.services.htpdate:Htpdate",
        "Httpd": "pynix_os.services.httpd:Httpd",
        "Httpd_VirtualHosts_Value": "pynix_os.services.httpd:Httpd_VirtualHosts_Value",
        "Httpd_VirtualHosts_Value_Listen_Item": "pynix_os.services.httpd:Httpd_VirtualHosts_Value_Listen_Item",
        "Httpd_VirtualHosts_Value_Locations_Value": "pynix_os.services.httpd:Httpd_VirtualHosts_Value_Locations_Value",
        "HttpsDnsProxy": "pynix_os.services.https_dns_proxy:HttpsDnsProxy",
        "HttpsDnsProxy_Provider": "pynix_os.services.https_dns_proxy:HttpsDnsProxy_Provider",
        "Hydra": "pynix_os.services.hydra:Hydra",
        "HydraBuilder": "pynix_os.services.hydra_builder:HydraBuilder",
        "HydraBuilder_Mtls": "pynix_os.services.hydra_builder:HydraBuilder_Mtls",
        "HydraBuilder_Settings": "pynix_os.services.hydra_builder:HydraBuilder_Settings",
        "Hydra_AdHoc": "pynix_os.services.hydra:Hydra_AdHoc",
        "Hydra_AdHoc_Settings": "pynix_os.services.hydra:Hydra_AdHoc_Settings",
        "Hydra_EvaluatorSettings": "pynix_os.services.hydra:Hydra_EvaluatorSettings",
        "Hydra_QueueRunner": "pynix_os.services.hydra:Hydra_QueueRunner",
        "Hydra_QueueRunner_Grpc": "pynix_os.services.hydra:Hydra_QueueRunner_Grpc",
        "Hydra_QueueRunner_Mtls": "pynix_os.services.hydra:Hydra_QueueRunner_Mtls",
        "Hydra_QueueRunner_Rest": "pynix_os.services.hydra:Hydra_QueueRunner_Rest",
        "Hydra_QueueRunner_Settings": "pynix_os.services.hydra:Hydra_QueueRunner_Settings",
        "Hydra_QueueRunner_Settings_OverflowStore": "pynix_os.services.hydra:Hydra_QueueRunner_Settings_OverflowStore",
        "Hydra_Ws": "pynix_os.services.hydra:Hydra_Ws",
        "Hydra_Ws_Bind": "pynix_os.services.hydra:Hydra_Ws_Bind",
        "Hydra_Ws_Settings": "pynix_os.services.hydra:Hydra_Ws_Settings",
        "Hylafax": "pynix_os.services.hylafax:Hylafax",
        "Hylafax_Faxcron": "pynix_os.services.hylafax:Hylafax_Faxcron",
        "Hylafax_Faxcron_Enable": "pynix_os.services.hylafax:Hylafax_Faxcron_Enable",
        "Hylafax_Faxqclean": "pynix_os.services.hylafax:Hylafax_Faxqclean",
        "Hylafax_Faxqclean_Enable": "pynix_os.services.hylafax:Hylafax_Faxqclean_Enable",
        "Hylafax_Modems_Value": "pynix_os.services.hylafax:Hylafax_Modems_Value",
        "HypervGuest": "pynix_os.virtualisation.hypervGuest:HypervGuest",
        "Hyphanet": "pynix_os.services.hyphanet:Hyphanet",
        "Hypridle": "pynix_os.services.hypridle:Hypridle",
        "Hyprland": "pynix_os.programs.hyprland:Hyprland",
        "Hyprland_Systemd": "pynix_os.programs.hyprland:Hyprland_Systemd",
        "Hyprland_Systemd_SetPath": "pynix_os.programs.hyprland:Hyprland_Systemd_SetPath",
        "Hyprland_Xwayland": "pynix_os.programs.hyprland:Hyprland_Xwayland",
        "Hyprlock": "pynix_os.programs.hyprlock:Hyprlock",
        "HyprwhsprRs": "pynix_os.services.hyprwhspr_rs:HyprwhsprRs",
        "I18n": "pynix_os.i18n.__options__:I18n",
        "I2c": "pynix_os.hardware.i2c:I2c",
        "I2p": "pynix_os.services.i2p:I2p",
        "I2pd": "pynix_os.services.i2pd:I2pd",
        "I2pd_ClientTunnels_Value": "pynix_os.services.i2pd:I2pd_ClientTunnels_Value",
        "I2pd_ServerTunnels_Value": "pynix_os.services.i2pd:I2pd_ServerTunnels_Value",
        "I2pd_Settings": "pynix_os.services.i2pd:I2pd_Settings",
        "I3lock": "pynix_os.programs.i3lock:I3lock",
        "Iay": "pynix_os.programs.iay:Iay",
        "Icecast": "pynix_os.services.icecast:Icecast",
        "Icecast_Admin": "pynix_os.services.icecast:Icecast_Admin",
        "Icecast_Listen": "pynix_os.services.icecast:Icecast_Listen",
        "Icecream": "pynix_os.services.icecream:Icecream",
        "Icecream_Daemon": "pynix_os.services.icecream:Icecream_Daemon",
        "Icecream_Scheduler": "pynix_os.services.icecream:Icecream_Scheduler",
        "Icingaweb2": "pynix_os.services.icingaweb2:Icingaweb2",
        "Icingaweb2_Modules": "pynix_os.services.icingaweb2:Icingaweb2_Modules",
        "Icingaweb2_Modules_Doc": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Doc",
        "Icingaweb2_Modules_Migrate": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Migrate",
        "Icingaweb2_Modules_Monitoring": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Monitoring",
        "Icingaweb2_Modules_Monitoring_Backends_Value": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Monitoring_Backends_Value",
        "Icingaweb2_Modules_Monitoring_GeneralConfig": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Monitoring_GeneralConfig",
        "Icingaweb2_Modules_Monitoring_Transports_Value": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Monitoring_Transports_Value",
        "Icingaweb2_Modules_Setup": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Setup",
        "Icingaweb2_Modules_Test": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Test",
        "Icingaweb2_Modules_Translation": "pynix_os.services.icingaweb2:Icingaweb2_Modules_Translation",
        "IconCache": "pynix_os.gtk.iconCache:IconCache",
        "Icons": "pynix_os.xdg.icons:Icons",
        "Idescriptor": "pynix_os.programs.idescriptor:Idescriptor",
        "Ids": "pynix_os.ids.__options__:Ids",
        "Ifm": "pynix_os.services.ifm:Ifm",
        "Ifstate": "pynix_os.networking.ifstate:Ifstate",
        "Iftop": "pynix_os.programs.iftop:Iftop",
        "Ihaskell": "pynix_os.services.ihaskell:Ihaskell",
        "IioHyprland": "pynix_os.programs.iio_hyprland:IioHyprland",
        "IioNiri": "pynix_os.services.iio_niri:IioNiri",
        "Illum": "pynix_os.services.illum:Illum",
        "Image": "pynix_os.image.__options__:Image",
        "System_Image": "pynix_os.system.image:Image",
        "Image_Modules_Value": "pynix_os.image.__options__:Image_Modules_Value",
        "Imaginary": "pynix_os.services.imaginary:Imaginary",
        "Imaginary_Settings": "pynix_os.services.imaginary:Imaginary_Settings",
        "Immersed": "pynix_os.programs.immersed:Immersed",
        "Immich": "pynix_os.services.immich:Immich",
        "ImmichKiosk": "pynix_os.services.immich_kiosk:ImmichKiosk",
        "ImmichKiosk_Settings": "pynix_os.services.immich_kiosk:ImmichKiosk_Settings",
        "ImmichPublicProxy": "pynix_os.services.immich_public_proxy:ImmichPublicProxy",
        "ImmichPublicProxy_Settings": "pynix_os.services.immich_public_proxy:ImmichPublicProxy_Settings",
        "Immich_Database": "pynix_os.services.immich:Immich_Database",
        "Immich_Environment": "pynix_os.services.immich:Immich_Environment",
        "Immich_MachineLearning": "pynix_os.services.immich:Immich_MachineLearning",
        "Immich_MachineLearning_Environment": "pynix_os.services.immich:Immich_MachineLearning_Environment",
        "Immich_Redis": "pynix_os.services.immich:Immich_Redis",
        "Immich_Settings": "pynix_os.services.immich:Immich_Settings",
        "Immichframe": "pynix_os.services.immichframe:Immichframe",
        "Immichframe_Settings": "pynix_os.services.immichframe:Immichframe_Settings",
        "Immichframe_Settings_Accounts_Item": "pynix_os.services.immichframe:Immichframe_Settings_Accounts_Item",
        "Inadyn": "pynix_os.services.inadyn:Inadyn",
        "Inadyn_Settings": "pynix_os.services.inadyn:Inadyn_Settings",
        "Inadyn_Settings_Custom_Value": "pynix_os.services.inadyn:Inadyn_Settings_Custom_Value",
        "Inadyn_Settings_Provider_Value": "pynix_os.services.inadyn:Inadyn_Settings_Provider_Value",
        "Incron": "pynix_os.services.incron:Incron",
        "Incus": "pynix_os.virtualisation.incus:Incus",
        "Incus_Agent": "pynix_os.virtualisation.incus:Incus_Agent",
        "Incus_Preseed": "pynix_os.virtualisation.incus:Incus_Preseed",
        "Incus_Storage": "pynix_os.virtualisation.incus:Incus_Storage",
        "Incus_Storage_Truenas": "pynix_os.virtualisation.incus:Incus_Storage_Truenas",
        "Incus_Ui": "pynix_os.virtualisation.incus:Incus_Ui",
        "Infiniband": "pynix_os.hardware.infiniband:Infiniband",
        "Infinoted": "pynix_os.services.infinoted:Infinoted",
        "Influxdb": "pynix_os.services.influxdb:Influxdb",
        "Influxdb2": "pynix_os.services.influxdb2:Influxdb2",
        "Influxdb2_Provision": "pynix_os.services.influxdb2:Influxdb2_Provision",
        "Influxdb2_Provision_InitialSetup": "pynix_os.services.influxdb2:Influxdb2_Provision_InitialSetup",
        "Influxdb2_Provision_Organizations_Value": "pynix_os.services.influxdb2:Influxdb2_Provision_Organizations_Value",
        "Influxdb2_Provision_Organizations_Value_Auths_Value": "pynix_os.services.influxdb2:Influxdb2_Provision_Organizations_Value_Auths_Value",
        "Influxdb2_Provision_Organizations_Value_Buckets_Value": "pynix_os.services.influxdb2:Influxdb2_Provision_Organizations_Value_Buckets_Value",
        "Influxdb2_Provision_Users_Value": "pynix_os.services.influxdb2:Influxdb2_Provision_Users_Value",
        "Influxdb_Settings": "pynix_os.services.influxdb:Influxdb_Settings",
        "Infnoise": "pynix_os.services.infnoise:Infnoise",
        "Info": "pynix_os.documentation.info:Info",
        "Initrd": "pynix_os.boot.initrd:Initrd",
        "Initrd_Clevis": "pynix_os.boot.initrd:Initrd_Clevis",
        "Initrd_ClevisLuksAskpass": "pynix_os.boot.initrd:Initrd_ClevisLuksAskpass",
        "Initrd_Clevis_Devices_Value": "pynix_os.boot.initrd:Initrd_Clevis_Devices_Value",
        "Initrd_ExtraFiles_Value": "pynix_os.boot.initrd:Initrd_ExtraFiles_Value",
        "Initrd_Luks": "pynix_os.boot.initrd:Initrd_Luks",
        "Initrd_Luks_Devices_Value": "pynix_os.boot.initrd:Initrd_Luks_Devices_Value",
        "Initrd_Luks_Devices_Value_GpgCard": "pynix_os.boot.initrd:Initrd_Luks_Devices_Value_GpgCard",
        "Initrd_Luks_Devices_Value_Yubikey": "pynix_os.boot.initrd:Initrd_Luks_Devices_Value_Yubikey",
        "Initrd_Network": "pynix_os.boot.initrd:Initrd_Network",
        "Initrd_Network_Ifstate": "pynix_os.boot.initrd:Initrd_Network_Ifstate",
        "Initrd_Network_Openvpn": "pynix_os.boot.initrd:Initrd_Network_Openvpn",
        "Initrd_Network_Ssh": "pynix_os.boot.initrd:Initrd_Network_Ssh",
        "Initrd_Network_Udhcpc": "pynix_os.boot.initrd:Initrd_Network_Udhcpc",
        "Initrd_NixStoreVeritysetup": "pynix_os.boot.initrd:Initrd_NixStoreVeritysetup",
        "Initrd_Services": "pynix_os.boot.initrd:Initrd_Services",
        "Initrd_Services_Bcache": "pynix_os.boot.initrd:Initrd_Services_Bcache",
        "Initrd_Services_Lvm": "pynix_os.boot.initrd:Initrd_Services_Lvm",
        "Initrd_Services_Resolved": "pynix_os.boot.initrd:Initrd_Services_Resolved",
        "Initrd_Services_Udev": "pynix_os.boot.initrd:Initrd_Services_Udev",
        "Initrd_Systemd": "pynix_os.boot.initrd:Initrd_Systemd",
        "Initrd_Systemd_Automounts_Item": "pynix_os.boot.initrd:Initrd_Systemd_Automounts_Item",
        "Initrd_Systemd_Contents_Value": "pynix_os.boot.initrd:Initrd_Systemd_Contents_Value",
        "Initrd_Systemd_Dbus": "pynix_os.boot.initrd:Initrd_Systemd_Dbus",
        "Initrd_Systemd_DmVerity": "pynix_os.boot.initrd:Initrd_Systemd_DmVerity",
        "Initrd_Systemd_Fido2": "pynix_os.boot.initrd:Initrd_Systemd_Fido2",
        "Initrd_Systemd_Groups_Value": "pynix_os.boot.initrd:Initrd_Systemd_Groups_Value",
        "Initrd_Systemd_Mounts_Item": "pynix_os.boot.initrd:Initrd_Systemd_Mounts_Item",
        "Initrd_Systemd_Network": "pynix_os.boot.initrd:Initrd_Systemd_Network",
        "Initrd_Systemd_Network_Config": "pynix_os.boot.initrd:Initrd_Systemd_Network_Config",
        "Initrd_Systemd_Network_Links_Value": "pynix_os.boot.initrd:Initrd_Systemd_Network_Links_Value",
        "Initrd_Systemd_Network_Netdevs_Value": "pynix_os.boot.initrd:Initrd_Systemd_Network_Netdevs_Value",
        "Initrd_Systemd_Network_Networks_Value": "pynix_os.boot.initrd:Initrd_Systemd_Network_Networks_Value",
        "Initrd_Systemd_Network_Units_Value": "pynix_os.boot.initrd:Initrd_Systemd_Network_Units_Value",
        "Initrd_Systemd_Network_WaitOnline": "pynix_os.boot.initrd:Initrd_Systemd_Network_WaitOnline",
        "Initrd_Systemd_Paths_Value": "pynix_os.boot.initrd:Initrd_Systemd_Paths_Value",
        "Initrd_Systemd_Repart": "pynix_os.boot.initrd:Initrd_Systemd_Repart",
        "Initrd_Systemd_Services_Value": "pynix_os.boot.initrd:Initrd_Systemd_Services_Value",
        "Initrd_Systemd_Settings": "pynix_os.boot.initrd:Initrd_Systemd_Settings",
        "Initrd_Systemd_Settings_Manager": "pynix_os.boot.initrd:Initrd_Systemd_Settings_Manager",
        "Initrd_Systemd_Shell": "pynix_os.boot.initrd:Initrd_Systemd_Shell",
        "Initrd_Systemd_Slices_Value": "pynix_os.boot.initrd:Initrd_Systemd_Slices_Value",
        "Initrd_Systemd_Sockets_Value": "pynix_os.boot.initrd:Initrd_Systemd_Sockets_Value",
        "Initrd_Systemd_StorePaths_Item": "pynix_os.boot.initrd:Initrd_Systemd_StorePaths_Item",
        "Initrd_Systemd_Targets_Value": "pynix_os.boot.initrd:Initrd_Systemd_Targets_Value",
        "Initrd_Systemd_Timers_Value": "pynix_os.boot.initrd:Initrd_Systemd_Timers_Value",
        "Initrd_Systemd_Tmpfiles": "pynix_os.boot.initrd:Initrd_Systemd_Tmpfiles",
        "Initrd_Systemd_Tmpfiles_Settings_Value_Value_Value": "pynix_os.boot.initrd:Initrd_Systemd_Tmpfiles_Settings_Value_Value_Value",
        "Initrd_Systemd_Tpm2": "pynix_os.boot.initrd:Initrd_Systemd_Tpm2",
        "Initrd_Systemd_Tpm2_Pcrosseparator": "pynix_os.boot.initrd:Initrd_Systemd_Tpm2_Pcrosseparator",
        "Initrd_Systemd_Tpm2_Pcrphases": "pynix_os.boot.initrd:Initrd_Systemd_Tpm2_Pcrphases",
        "Initrd_Systemd_Units_Value": "pynix_os.boot.initrd:Initrd_Systemd_Units_Value",
        "Initrd_Systemd_Users_Value": "pynix_os.boot.initrd:Initrd_Systemd_Users_Value",
        "Initrd_Unl0kr": "pynix_os.boot.initrd:Initrd_Unl0kr",
        "Initrd_Unl0kr_Settings": "pynix_os.boot.initrd:Initrd_Unl0kr_Settings",
        "InputRemapper": "pynix_os.services.input_remapper:InputRemapper",
        "Inputmodule": "pynix_os.hardware.inputmodule:Inputmodule",
        "Inputplumber": "pynix_os.services.inputplumber:Inputplumber",
        "Inspircd": "pynix_os.services.inspircd:Inspircd",
        "IntelGpuTools": "pynix_os.hardware.intel_gpu_tools:IntelGpuTools",
        "InterceptionTools": "pynix_os.services.interception_tools:InterceptionTools",
        "Intune": "pynix_os.services.intune:Intune",
        "Inventree": "pynix_os.services.inventree:Inventree",
        "Inventree_Database": "pynix_os.services.inventree:Inventree_Database",
        "Invidious": "pynix_os.services.invidious:Invidious",
        "InvidiousRouter": "pynix_os.services.invidious_router:InvidiousRouter",
        "InvidiousRouter_Nginx": "pynix_os.services.invidious_router:InvidiousRouter_Nginx",
        "InvidiousRouter_Settings": "pynix_os.services.invidious_router:InvidiousRouter_Settings",
        "Invidious_Database": "pynix_os.services.invidious:Invidious_Database",
        "Invidious_Http3Ytproxy": "pynix_os.services.invidious:Invidious_Http3Ytproxy",
        "Invidious_Nginx": "pynix_os.services.invidious:Invidious_Nginx",
        "Invidious_SigHelper": "pynix_os.services.invidious:Invidious_SigHelper",
        "Iocaine": "pynix_os.services.iocaine:Iocaine",
        "Iocaine_Settings": "pynix_os.services.iocaine:Iocaine_Settings",
        "Iodine": "pynix_os.services.iodine:Iodine",
        "Iodine_Clients_Value": "pynix_os.services.iodine:Iodine_Clients_Value",
        "Iodine_Server": "pynix_os.services.iodine:Iodine_Server",
        "Ioquake3": "pynix_os.programs.ioquake3:Ioquake3",
        "Iotop": "pynix_os.programs.iotop:Iotop",
        "Ipa": "pynix_os.security.ipa:Ipa",
        "Ipa_Dyndns": "pynix_os.security.ipa:Ipa_Dyndns",
        "Iperf3": "pynix_os.services.iperf3:Iperf3",
        "IpfsCluster": "pynix_os.services.ipfs_cluster:IpfsCluster",
        "IppUsb": "pynix_os.services.ipp_usb:IppUsb",
        "Iproute2": "pynix_os.networking.iproute2:Iproute2",
        "Iptsd": "pynix_os.services.iptsd:Iptsd",
        "Iptsd_Config": "pynix_os.services.iptsd:Iptsd_Config",
        "Ipu6": "pynix_os.hardware.ipu6:Ipu6",
        "Ipu7": "pynix_os.hardware.ipu7:Ipu7",
        "IrcdHybrid": "pynix_os.services.ircdHybrid:IrcdHybrid",
        "Irkerd": "pynix_os.services.irkerd:Irkerd",
        "Irqbalance": "pynix_os.services.irqbalance:Irqbalance",
        "IscsiInitiator": "pynix_os.boot.iscsi_initiator:IscsiInitiator",
        "Isolate": "pynix_os.security.isolate:Isolate",
        "Isso": "pynix_os.services.isso:Isso",
        "Isso_Settings": "pynix_os.services.isso:Isso_Settings",
        "Ivpn": "pynix_os.services.ivpn:Ivpn",
        "Jack": "pynix_os.services.jack:Jack",
        "Jack_Alsa": "pynix_os.services.jack:Jack_Alsa",
        "Jack_Jackd": "pynix_os.services.jack:Jack_Jackd",
        "Jack_Loopback": "pynix_os.services.jack:Jack_Loopback",
        "Jackett": "pynix_os.services.jackett:Jackett",
        "JaiJail": "pynix_os.programs.jai_jail:JaiJail",
        "Java": "pynix_os.programs.java:Java",
        "Jboss": "pynix_os.services.jboss:Jboss",
        "Jellyfin": "pynix_os.services.jellyfin:Jellyfin",
        "Jellyfin_Transcoding": "pynix_os.services.jellyfin:Jellyfin_Transcoding",
        "Jellyfin_Transcoding_HardwareDecodingCodecs": "pynix_os.services.jellyfin:Jellyfin_Transcoding_HardwareDecodingCodecs",
        "Jellyfin_Transcoding_HardwareEncodingCodecs": "pynix_os.services.jellyfin:Jellyfin_Transcoding_HardwareEncodingCodecs",
        "Jenkins": "pynix_os.services.jenkins:Jenkins",
        "JenkinsSlave": "pynix_os.services.jenkinsSlave:JenkinsSlave",
        "Jenkins_JobBuilder": "pynix_os.services.jenkins:Jenkins_JobBuilder",
        "Jibri": "pynix_os.services.jibri:Jibri",
        "Jibri_XmppEnvironments_Value": "pynix_os.services.jibri:Jibri_XmppEnvironments_Value",
        "Jicofo": "pynix_os.services.jicofo:Jicofo",
        "Jigasi": "pynix_os.services.jigasi:Jigasi",
        "Jirafeau": "pynix_os.services.jirafeau:Jirafeau",
        "Jirafeau_NginxConfig": "pynix_os.services.jirafeau:Jirafeau_NginxConfig",
        "Jirafeau_NginxConfig_Listen_Item": "pynix_os.services.jirafeau:Jirafeau_NginxConfig_Listen_Item",
        "Jirafeau_NginxConfig_Locations_Value": "pynix_os.services.jirafeau:Jirafeau_NginxConfig_Locations_Value",
        "JitsiMeet": "pynix_os.services.jitsi_meet:JitsiMeet",
        "JitsiMeet_Caddy": "pynix_os.services.jitsi_meet:JitsiMeet_Caddy",
        "JitsiMeet_Excalidraw": "pynix_os.services.jitsi_meet:JitsiMeet_Excalidraw",
        "JitsiMeet_Jibri": "pynix_os.services.jitsi_meet:JitsiMeet_Jibri",
        "JitsiMeet_Jicofo": "pynix_os.services.jitsi_meet:JitsiMeet_Jicofo",
        "JitsiMeet_Jigasi": "pynix_os.services.jitsi_meet:JitsiMeet_Jigasi",
        "JitsiMeet_Nginx": "pynix_os.services.jitsi_meet:JitsiMeet_Nginx",
        "JitsiMeet_Prosody": "pynix_os.services.jitsi_meet:JitsiMeet_Prosody",
        "JitsiMeet_SecureDomain": "pynix_os.services.jitsi_meet:JitsiMeet_SecureDomain",
        "JitsiMeet_Videobridge": "pynix_os.services.jitsi_meet:JitsiMeet_Videobridge",
        "JitsiVideobridge": "pynix_os.services.jitsi_videobridge:JitsiVideobridge",
        "JitsiVideobridge_Nat": "pynix_os.services.jitsi_videobridge:JitsiVideobridge_Nat",
        "JitsiVideobridge_XmppConfigs_Value": "pynix_os.services.jitsi_videobridge:JitsiVideobridge_XmppConfigs_Value",
        "JitterentropyRngd": "pynix_os.services.jitterentropy_rngd:JitterentropyRngd",
        "Jmusicbot": "pynix_os.services.jmusicbot:Jmusicbot",
        "Jool": "pynix_os.networking.jool:Jool",
        "Jool_Nat64_Value": "pynix_os.networking.jool:Jool_Nat64_Value",
        "Jool_Siit_Value": "pynix_os.networking.jool:Jool_Siit_Value",
        "JottaCli": "pynix_os.services.jotta_cli:JottaCli",
        "Journalbeat": "pynix_os.services.journalbeat:Journalbeat",
        "Journald": "pynix_os.services.journald:Journald",
        "Journald_Gateway": "pynix_os.services.journald:Journald_Gateway",
        "Journald_Remote": "pynix_os.services.journald:Journald_Remote",
        "Journald_Remote_Settings": "pynix_os.services.journald:Journald_Remote_Settings",
        "Journald_Settings": "pynix_os.services.journald:Journald_Settings",
        "Journald_Settings_Journal": "pynix_os.services.journald:Journald_Settings_Journal",
        "Journald_Upload": "pynix_os.services.journald:Journald_Upload",
        "Journald_Upload_Settings": "pynix_os.services.journald:Journald_Upload_Settings",
        "Journaldriver": "pynix_os.services.journaldriver:Journaldriver",
        "Journalwatch": "pynix_os.services.journalwatch:Journalwatch",
        "Journalwatch_FilterBlocks_Item": "pynix_os.services.journalwatch:Journalwatch_FilterBlocks_Item",
        "Joycond": "pynix_os.services.joycond:Joycond",
        "JoycondCemuhook": "pynix_os.programs.joycond_cemuhook:JoycondCemuhook",
        "Jupyter": "pynix_os.services.jupyter:Jupyter",
        "Jupyter_Kernels_Value": "pynix_os.services.jupyter:Jupyter_Kernels_Value",
        "Jupyterhub": "pynix_os.services.jupyterhub:Jupyterhub",
        "Jupyterhub_Kernels_Value": "pynix_os.services.jupyterhub:Jupyterhub_Kernels_Value",
        "K3b": "pynix_os.programs.k3b:K3b",
        "K3s": "pynix_os.services.k3s:K3s",
        "K3s_AutoDeployCharts_Value": "pynix_os.services.k3s:K3s_AutoDeployCharts_Value",
        "K3s_GracefulNodeShutdown": "pynix_os.services.k3s:K3s_GracefulNodeShutdown",
        "K3s_Manifests_Value": "pynix_os.services.k3s:K3s_Manifests_Value",
        "K40Whisperer": "pynix_os.programs.k40_whisperer:K40Whisperer",
        "Kanata": "pynix_os.services.kanata:Kanata",
        "Kanata_Keyboards_Value": "pynix_os.services.kanata:Kanata_Keyboards_Value",
        "Kanboard": "pynix_os.services.kanboard:Kanboard",
        "Kanboard_Nginx": "pynix_os.services.kanboard:Kanboard_Nginx",
        "Kanboard_Nginx_Listen_Item": "pynix_os.services.kanboard:Kanboard_Nginx_Listen_Item",
        "Kanboard_Nginx_Locations_Value": "pynix_os.services.kanboard:Kanboard_Nginx_Locations_Value",
        "Kanboard_Phpfpm": "pynix_os.services.kanboard:Kanboard_Phpfpm",
        "Kanidm": "pynix_os.services.kanidm:Kanidm",
        "Kanidm_Client": "pynix_os.services.kanidm:Kanidm_Client",
        "Kanidm_Client_Settings": "pynix_os.services.kanidm:Kanidm_Client_Settings",
        "Kanidm_Provision": "pynix_os.services.kanidm:Kanidm_Provision",
        "Kanidm_Provision_Groups_Value": "pynix_os.services.kanidm:Kanidm_Provision_Groups_Value",
        "Kanidm_Provision_Persons_Value": "pynix_os.services.kanidm:Kanidm_Provision_Persons_Value",
        "Kanidm_Provision_Systems": "pynix_os.services.kanidm:Kanidm_Provision_Systems",
        "Kanidm_Provision_Systems_Oauth2_Value": "pynix_os.services.kanidm:Kanidm_Provision_Systems_Oauth2_Value",
        "Kanidm_Provision_Systems_Oauth2_Value_ClaimMaps_Value": "pynix_os.services.kanidm:Kanidm_Provision_Systems_Oauth2_Value_ClaimMaps_Value",
        "Kanidm_Server": "pynix_os.services.kanidm:Kanidm_Server",
        "Kanidm_Server_EntryManagement": "pynix_os.services.kanidm:Kanidm_Server_EntryManagement",
        "Kanidm_Server_Settings": "pynix_os.services.kanidm:Kanidm_Server_Settings",
        "Kanidm_Unix": "pynix_os.services.kanidm:Kanidm_Unix",
        "Kanidm_Unix_Settings": "pynix_os.services.kanidm:Kanidm_Unix_Settings",
        "Kanshi": "pynix_os.services.kanshi:Kanshi",
        "Kanshi_Systemd": "pynix_os.services.kanshi:Kanshi_Systemd",
        "Kapacitor": "pynix_os.services.kapacitor:Kapacitor",
        "Kapacitor_Alerta": "pynix_os.services.kapacitor:Kapacitor_Alerta",
        "Kapacitor_DefaultDatabase": "pynix_os.services.kapacitor:Kapacitor_DefaultDatabase",
        "Kapla": "pynix_os.services.kapla:Kapla",
        "Kapla_ErisSocket": "pynix_os.services.kapla:Kapla_ErisSocket",
        "Karakeep": "pynix_os.services.karakeep:Karakeep",
        "Karakeep_Browser": "pynix_os.services.karakeep:Karakeep_Browser",
        "Karakeep_Meilisearch": "pynix_os.services.karakeep:Karakeep_Meilisearch",
        "Karma": "pynix_os.services.karma:Karma",
        "Karma_Settings": "pynix_os.services.karma:Karma_Settings",
        "Kasmweb": "pynix_os.services.kasmweb:Kasmweb",
        "Kasmweb_Postgres": "pynix_os.services.kasmweb:Kasmweb_Postgres",
        "Kavita": "pynix_os.services.kavita:Kavita",
        "Kavita_Settings": "pynix_os.services.kavita:Kavita_Settings",
        "Kbdlight": "pynix_os.programs.kbdlight:Kbdlight",
        "Kbfs": "pynix_os.services.kbfs:Kbfs",
        "Kclock": "pynix_os.programs.kclock:Kclock",
        "KdePim": "pynix_os.programs.kde_pim:KdePim",
        "Kdeconnect": "pynix_os.programs.kdeconnect:Kdeconnect",
        "Kea": "pynix_os.services.kea:Kea",
        "Kea_Dhcp4": "pynix_os.services.kea:Kea_Dhcp4",
        "Kea_Dhcp6": "pynix_os.services.kea:Kea_Dhcp6",
        "Kea_DhcpDdns": "pynix_os.services.kea:Kea_DhcpDdns",
        "Keepalived": "pynix_os.services.keepalived:Keepalived",
        "Keepalived_Snmp": "pynix_os.services.keepalived:Keepalived_Snmp",
        "Keepalived_VrrpInstances_Value": "pynix_os.services.keepalived:Keepalived_VrrpInstances_Value",
        "Keepalived_VrrpInstances_Value_VirtualIps_Item": "pynix_os.services.keepalived:Keepalived_VrrpInstances_Value_VirtualIps_Item",
        "Keepalived_VrrpScripts_Value": "pynix_os.services.keepalived:Keepalived_VrrpScripts_Value",
        "Kener": "pynix_os.services.kener:Kener",
        "Kener_Redis": "pynix_os.services.kener:Kener_Redis",
        "Kener_Settings": "pynix_os.services.kener:Kener_Settings",
        "KerberosServer": "pynix_os.services.kerberos_server:KerberosServer",
        "KerberosServer_Settings": "pynix_os.services.kerberos_server:KerberosServer_Settings",
        "KerberosServer_Settings_Realms_Value": "pynix_os.services.kerberos_server:KerberosServer_Settings_Realms_Value",
        "KerberosServer_Settings_Realms_Value_Acl_Item": "pynix_os.services.kerberos_server:KerberosServer_Settings_Realms_Value_Acl_Item",
        "Kernel": "pynix_os.boot.kernel:Kernel",
        "Kernel_Sysctl": "pynix_os.boot.kernel:Kernel_Sysctl",
        "Kernel_Sysfs": "pynix_os.boot.kernel:Kernel_Sysfs",
        "Keter": "pynix_os.services.keter:Keter",
        "Keter_Bundle": "pynix_os.services.keter:Keter_Bundle",
        "Keter_GlobalKeterConfig": "pynix_os.services.keter:Keter_GlobalKeterConfig",
        "Keter_GlobalKeterConfig_Listeners_Item": "pynix_os.services.keter:Keter_GlobalKeterConfig_Listeners_Item",
        "Kexec": "pynix_os.boot.kexec:Kexec",
        "Keybase": "pynix_os.services.keybase:Keybase",
        "Keyboard": "pynix_os.hardware.keyboard:Keyboard",
        "Keyboard_Qmk": "pynix_os.hardware.keyboard:Keyboard_Qmk",
        "Keyboard_Teck": "pynix_os.hardware.keyboard:Keyboard_Teck",
        "Keyboard_Uhk": "pynix_os.hardware.keyboard:Keyboard_Uhk",
        "Keyboard_Zsa": "pynix_os.hardware.keyboard:Keyboard_Zsa",
        "Keycloak": "pynix_os.services.keycloak:Keycloak",
        "Keycloak_Settings": "pynix_os.services.keycloak:Keycloak_Settings",
        "Keyd": "pynix_os.services.keyd:Keyd",
        "Keyd_Keyboards_Value": "pynix_os.services.keyd:Keyd_Keyboards_Value",
        "Kimai": "pynix_os.services.kimai:Kimai",
        "Kimai_Sites_Value": "pynix_os.services.kimai:Kimai_Sites_Value",
        "Kismet": "pynix_os.services.kismet:Kismet",
        "Kismet_Httpd": "pynix_os.services.kismet:Kismet_Httpd",
        "KiwixServe": "pynix_os.services.kiwix_serve:KiwixServe",
        "Klipper": "pynix_os.services.klipper:Klipper",
        "Klipper_Firmwares_Value": "pynix_os.services.klipper:Klipper_Firmwares_Value",
        "Kmonad": "pynix_os.services.kmonad:Kmonad",
        "Kmonad_Keyboards_Value": "pynix_os.services.kmonad:Kmonad_Keyboards_Value",
        "Kmscon": "pynix_os.services.kmscon:Kmscon",
        "Kmscon_Config": "pynix_os.services.kmscon:Kmscon_Config",
        "Knot": "pynix_os.services.knot:Knot",
        "KnotResolver": "pynix_os.services.knot_resolver:KnotResolver",
        "KnotResolver_Settings": "pynix_os.services.knot_resolver:KnotResolver_Settings",
        "KnotResolver_Settings_NetworkListen_Item": "pynix_os.services.knot_resolver:KnotResolver_Settings_NetworkListen_Item",
        "Koito": "pynix_os.services.koito:Koito",
        "Koito_Environment": "pynix_os.services.koito:Koito_Environment",
        "Komga": "pynix_os.services.komga:Komga",
        "Komga_Settings": "pynix_os.services.komga:Komga_Settings",
        "KomodoPeriphery": "pynix_os.services.komodo_periphery:KomodoPeriphery",
        "KomodoPeriphery_Auth": "pynix_os.services.komodo_periphery:KomodoPeriphery_Auth",
        "KomodoPeriphery_Inbound": "pynix_os.services.komodo_periphery:KomodoPeriphery_Inbound",
        "KomodoPeriphery_Inbound_Ssl": "pynix_os.services.komodo_periphery:KomodoPeriphery_Inbound_Ssl",
        "KomodoPeriphery_Logging": "pynix_os.services.komodo_periphery:KomodoPeriphery_Logging",
        "KomodoPeriphery_Outbound": "pynix_os.services.komodo_periphery:KomodoPeriphery_Outbound",
        "Krb5": "pynix_os.security.krb5:Krb5",
        "Krb5_Settings": "pynix_os.security.krb5:Krb5_Settings",
        "Kresd": "pynix_os.services.kresd:Kresd",
        "Krill": "pynix_os.services.krill:Krill",
        "Krill_Settings": "pynix_os.services.krill:Krill_Settings",
        "Kryoflux": "pynix_os.hardware.kryoflux:Kryoflux",
        "Ksm": "pynix_os.hardware.ksm:Ksm",
        "Kthxbye": "pynix_os.services.kthxbye:Kthxbye",
        "Kthxbye_Alertmanager": "pynix_os.services.kthxbye:Kthxbye_Alertmanager",
        "Kubernetes": "pynix_os.services.kubernetes:Kubernetes",
        "Kubernetes_AddonManager": "pynix_os.services.kubernetes:Kubernetes_AddonManager",
        "Kubernetes_Addons": "pynix_os.services.kubernetes:Kubernetes_Addons",
        "Kubernetes_Addons_Dns": "pynix_os.services.kubernetes:Kubernetes_Addons_Dns",
        "Kubernetes_Apiserver": "pynix_os.services.kubernetes:Kubernetes_Apiserver",
        "Kubernetes_Apiserver_Etcd": "pynix_os.services.kubernetes:Kubernetes_Apiserver_Etcd",
        "Kubernetes_ControllerManager": "pynix_os.services.kubernetes:Kubernetes_ControllerManager",
        "Kubernetes_ControllerManager_Kubeconfig": "pynix_os.services.kubernetes:Kubernetes_ControllerManager_Kubeconfig",
        "Kubernetes_Flannel": "pynix_os.services.kubernetes:Kubernetes_Flannel",
        "Kubernetes_Kubeconfig": "pynix_os.services.kubernetes:Kubernetes_Kubeconfig",
        "Kubernetes_Kubelet": "pynix_os.services.kubernetes:Kubernetes_Kubelet",
        "Kubernetes_Kubelet_Cni": "pynix_os.services.kubernetes:Kubernetes_Kubelet_Cni",
        "Kubernetes_Kubelet_Healthz": "pynix_os.services.kubernetes:Kubernetes_Kubelet_Healthz",
        "Kubernetes_Kubelet_Kubeconfig": "pynix_os.services.kubernetes:Kubernetes_Kubelet_Kubeconfig",
        "Kubernetes_Kubelet_Taints_Value": "pynix_os.services.kubernetes:Kubernetes_Kubelet_Taints_Value",
        "Kubernetes_Pki": "pynix_os.services.kubernetes:Kubernetes_Pki",
        "Kubernetes_Proxy": "pynix_os.services.kubernetes:Kubernetes_Proxy",
        "Kubernetes_Proxy_Kubeconfig": "pynix_os.services.kubernetes:Kubernetes_Proxy_Kubeconfig",
        "Kubernetes_Scheduler": "pynix_os.services.kubernetes:Kubernetes_Scheduler",
        "Kubernetes_Scheduler_Kubeconfig": "pynix_os.services.kubernetes:Kubernetes_Scheduler_Kubeconfig",
        "Kubeswitch": "pynix_os.programs.kubeswitch:Kubeswitch",
        "Kubo": "pynix_os.services.kubo:Kubo",
        "Kubo_Settings": "pynix_os.services.kubo:Kubo_Settings",
        "Kvmgt": "pynix_os.virtualisation.kvmgt:Kvmgt",
        "Kvmgt_Vgpus_Value": "pynix_os.virtualisation.kvmgt:Kvmgt_Vgpus_Value",
        "Kvrocks": "pynix_os.services.kvrocks:Kvrocks",
        "Kvrocks_Settings": "pynix_os.services.kvrocks:Kvrocks_Settings",
        "Labgrid": "pynix_os.services.labgrid:Labgrid",
        "Labgrid_Coordinator": "pynix_os.services.labgrid:Labgrid_Coordinator",
        "Labwc": "pynix_os.programs.labwc:Labwc",
        "Lact": "pynix_os.services.lact:Lact",
        "Lact_Settings": "pynix_os.services.lact:Lact_Settings",
        "Ladybird": "pynix_os.programs.ladybird:Ladybird",
        "Lambdabot": "pynix_os.services.lambdabot:Lambdabot",
        "Languagetool": "pynix_os.services.languagetool:Languagetool",
        "Languagetool_Settings": "pynix_os.services.languagetool:Languagetool_Settings",
        "Lanraragi": "pynix_os.services.lanraragi:Lanraragi",
        "Lanraragi_Redis": "pynix_os.services.lanraragi:Lanraragi_Redis",
        "LasuiteDocs": "pynix_os.services.lasuite_docs:LasuiteDocs",
        "LasuiteDocs_Celery": "pynix_os.services.lasuite_docs:LasuiteDocs_Celery",
        "LasuiteDocs_CollaborationServer": "pynix_os.services.lasuite_docs:LasuiteDocs_CollaborationServer",
        "LasuiteDocs_CollaborationServer_Settings": "pynix_os.services.lasuite_docs:LasuiteDocs_CollaborationServer_Settings",
        "LasuiteDocs_Gunicorn": "pynix_os.services.lasuite_docs:LasuiteDocs_Gunicorn",
        "LasuiteDocs_Postgresql": "pynix_os.services.lasuite_docs:LasuiteDocs_Postgresql",
        "LasuiteDocs_Redis": "pynix_os.services.lasuite_docs:LasuiteDocs_Redis",
        "LasuiteDocs_Settings": "pynix_os.services.lasuite_docs:LasuiteDocs_Settings",
        "LasuiteDrive": "pynix_os.services.lasuite_drive:LasuiteDrive",
        "LasuiteDrive_Celery": "pynix_os.services.lasuite_drive:LasuiteDrive_Celery",
        "LasuiteDrive_Gunicorn": "pynix_os.services.lasuite_drive:LasuiteDrive_Gunicorn",
        "LasuiteDrive_Postgresql": "pynix_os.services.lasuite_drive:LasuiteDrive_Postgresql",
        "LasuiteDrive_Redis": "pynix_os.services.lasuite_drive:LasuiteDrive_Redis",
        "LasuiteDrive_Settings": "pynix_os.services.lasuite_drive:LasuiteDrive_Settings",
        "LasuiteMeet": "pynix_os.services.lasuite_meet:LasuiteMeet",
        "LasuiteMeet_Celery": "pynix_os.services.lasuite_meet:LasuiteMeet_Celery",
        "LasuiteMeet_Gunicorn": "pynix_os.services.lasuite_meet:LasuiteMeet_Gunicorn",
        "LasuiteMeet_Livekit": "pynix_os.services.lasuite_meet:LasuiteMeet_Livekit",
        "LasuiteMeet_Postgresql": "pynix_os.services.lasuite_meet:LasuiteMeet_Postgresql",
        "LasuiteMeet_Redis": "pynix_os.services.lasuite_meet:LasuiteMeet_Redis",
        "LasuiteMeet_Settings": "pynix_os.services.lasuite_meet:LasuiteMeet_Settings",
        "Lauti": "pynix_os.services.lauti:Lauti",
        "Lavalink": "pynix_os.services.lavalink:Lavalink",
        "Lavalink_ExtraConfig": "pynix_os.services.lavalink:Lavalink_ExtraConfig",
        "Lavalink_Plugins_Item": "pynix_os.services.lavalink:Lavalink_Plugins_Item",
        "Lavalink_Plugins_Item_ExtraConfig": "pynix_os.services.lavalink:Lavalink_Plugins_Item_ExtraConfig",
        "Lazygit": "pynix_os.programs.lazygit:Lazygit",
        "Ldap": "pynix_os.users.ldap:Ldap",
        "Ldap_Bind": "pynix_os.users.ldap:Ldap_Bind",
        "Ldap_Daemon": "pynix_os.users.ldap:Ldap_Daemon",
        "Leaps": "pynix_os.services.leaps:Leaps",
        "Ledger": "pynix_os.hardware.ledger:Ledger",
        "Legit": "pynix_os.services.legit:Legit",
        "Legit_Settings": "pynix_os.services.legit:Legit_Settings",
        "Lemmy": "pynix_os.services.lemmy:Lemmy",
        "Lemmy_Caddy": "pynix_os.services.lemmy:Lemmy_Caddy",
        "Lemmy_Database": "pynix_os.services.lemmy:Lemmy_Database",
        "Lemmy_Nginx": "pynix_os.services.lemmy:Lemmy_Nginx",
        "Lemmy_Server": "pynix_os.services.lemmy:Lemmy_Server",
        "Lemmy_Settings": "pynix_os.services.lemmy:Lemmy_Settings",
        "Lemmy_Ui": "pynix_os.services.lemmy:Lemmy_Ui",
        "Less": "pynix_os.programs.less:Less",
        "Libeufin": "pynix_os.services.libeufin:Libeufin",
        "Libeufin_Bank": "pynix_os.services.libeufin:Libeufin_Bank",
        "Libeufin_Bank_Settings": "pynix_os.services.libeufin:Libeufin_Bank_Settings",
        "Libeufin_Nexus": "pynix_os.services.libeufin:Libeufin_Nexus",
        "Libeufin_Nexus_Settings": "pynix_os.services.libeufin:Libeufin_Nexus_Settings",
        "Libeufin_Settings": "pynix_os.services.libeufin:Libeufin_Settings",
        "Libftdi": "pynix_os.hardware.libftdi:Libftdi",
        "Libinput": "pynix_os.services.libinput:Libinput",
        "Libinput_Mouse": "pynix_os.services.libinput:Libinput_Mouse",
        "Libinput_Touchpad": "pynix_os.services.libinput:Libinput_Touchpad",
        "Libjaylink": "pynix_os.hardware.libjaylink:Libjaylink",
        "Liboping": "pynix_os.programs.liboping:Liboping",
        "Librechat": "pynix_os.services.librechat:Librechat",
        "Librechat_Env": "pynix_os.services.librechat:Librechat_Env",
        "Librechat_Meilisearch": "pynix_os.services.librechat:Librechat_Meilisearch",
        "Librechat_Settings": "pynix_os.services.librechat:Librechat_Settings",
        "Librenms": "pynix_os.services.librenms:Librenms",
        "Librenms_Database": "pynix_os.services.librenms:Librenms_Database",
        "Librenms_DistributedPoller": "pynix_os.services.librenms:Librenms_DistributedPoller",
        "Librenms_Nginx": "pynix_os.services.librenms:Librenms_Nginx",
        "Librenms_Nginx_Listen_Item": "pynix_os.services.librenms:Librenms_Nginx_Listen_Item",
        "Librenms_Nginx_Locations_Value": "pynix_os.services.librenms:Librenms_Nginx_Locations_Value",
        "Librenms_Settings": "pynix_os.services.librenms:Librenms_Settings",
        "Librepods": "pynix_os.programs.librepods:Librepods",
        "Librespeed": "pynix_os.services.librespeed:Librespeed",
        "Librespeed_Frontend": "pynix_os.services.librespeed:Librespeed_Frontend",
        "Librespeed_Frontend_Servers_Item": "pynix_os.services.librespeed:Librespeed_Frontend_Servers_Item",
        "Librespeed_Frontend_Settings": "pynix_os.services.librespeed:Librespeed_Frontend_Settings",
        "Libreswan": "pynix_os.services.libreswan:Libreswan",
        "Libretranslate": "pynix_os.services.libretranslate:Libretranslate",
        "Services_Libvirtd": "pynix_os.services.libvirtd:Libvirtd",
        "Virtualisation_Libvirtd": "pynix_os.virtualisation.libvirtd:Libvirtd",
        "Libvirtd_AutoSnapshot": "pynix_os.services.libvirtd:Libvirtd_AutoSnapshot",
        "Libvirtd_AutoSnapshot_Vms_Item_Or": "pynix_os.services.libvirtd:Libvirtd_AutoSnapshot_Vms_Item_Or",
        "Libvirtd_Dbus": "pynix_os.virtualisation.libvirtd:Libvirtd_Dbus",
        "Libvirtd_Hooks": "pynix_os.virtualisation.libvirtd:Libvirtd_Hooks",
        "Libvirtd_Nss": "pynix_os.virtualisation.libvirtd:Libvirtd_Nss",
        "Libvirtd_Qemu": "pynix_os.virtualisation.libvirtd:Libvirtd_Qemu",
        "Libvirtd_Qemu_Ovmf": "pynix_os.virtualisation.libvirtd:Libvirtd_Qemu_Ovmf",
        "Libvirtd_Qemu_Swtpm": "pynix_os.virtualisation.libvirtd:Libvirtd_Qemu_Swtpm",
        "Lidarr": "pynix_os.services.lidarr:Lidarr",
        "Lidarr_Settings": "pynix_os.services.lidarr:Lidarr_Settings",
        "Lifecycled": "pynix_os.services.lifecycled:Lifecycled",
        "Lifecycled_QueueCleaner": "pynix_os.services.lifecycled:Lifecycled_QueueCleaner",
        "Lighthouse": "pynix_os.services.lighthouse:Lighthouse",
        "Lighthouse_Beacon": "pynix_os.services.lighthouse:Lighthouse_Beacon",
        "Lighthouse_Validator": "pynix_os.services.lighthouse:Lighthouse_Validator",
        "Lighttpd": "pynix_os.services.lighttpd:Lighttpd",
        "Lighttpd_Cgit": "pynix_os.services.lighttpd:Lighttpd_Cgit",
        "Lighttpd_Collectd": "pynix_os.services.lighttpd:Lighttpd_Collectd",
        "Lighttpd_Gitweb": "pynix_os.services.lighttpd:Lighttpd_Gitweb",
        "Limesurvey": "pynix_os.services.limesurvey:Limesurvey",
        "Limesurvey_Httpd": "pynix_os.services.limesurvey:Limesurvey_Httpd",
        "Limesurvey_Httpd_VirtualHost": "pynix_os.services.limesurvey:Limesurvey_Httpd_VirtualHost",
        "Limesurvey_Httpd_VirtualHost_Listen_Item": "pynix_os.services.limesurvey:Limesurvey_Httpd_VirtualHost_Listen_Item",
        "Limesurvey_Httpd_VirtualHost_Locations_Value": "pynix_os.services.limesurvey:Limesurvey_Httpd_VirtualHost_Locations_Value",
        "Limesurvey_Nginx": "pynix_os.services.limesurvey:Limesurvey_Nginx",
        "Limesurvey_Nginx_VirtualHost": "pynix_os.services.limesurvey:Limesurvey_Nginx_VirtualHost",
        "Limesurvey_Nginx_VirtualHost_Listen_Item": "pynix_os.services.limesurvey:Limesurvey_Nginx_VirtualHost_Listen_Item",
        "Limesurvey_Nginx_VirtualHost_Locations_Value": "pynix_os.services.limesurvey:Limesurvey_Nginx_VirtualHost_Locations_Value",
        "Linkding": "pynix_os.services.linkding:Linkding",
        "Linkwarden": "pynix_os.services.linkwarden:Linkwarden",
        "Linkwarden_Database": "pynix_os.services.linkwarden:Linkwarden_Database",
        "LinuxEnableIrEmitter": "pynix_os.services.linux_enable_ir_emitter:LinuxEnableIrEmitter",
        "Linyaps": "pynix_os.services.linyaps:Linyaps",
        "Liquidsoap": "pynix_os.services.liquidsoap:Liquidsoap",
        "Lirc": "pynix_os.services.lirc:Lirc",
        "Listmonk": "pynix_os.services.listmonk:Listmonk",
        "Listmonk_Database": "pynix_os.services.listmonk:Listmonk_Database",
        "Listmonk_Database_Settings": "pynix_os.services.listmonk:Listmonk_Database_Settings",
        "Listmonk_Database_Settings_BounceMailboxes_Item": "pynix_os.services.listmonk:Listmonk_Database_Settings_BounceMailboxes_Item",
        "Listmonk_Database_Settings_Smtp_Item": "pynix_os.services.listmonk:Listmonk_Database_Settings_Smtp_Item",
        "Listmonk_Settings": "pynix_os.services.listmonk:Listmonk_Settings",
        "Litellm": "pynix_os.services.litellm:Litellm",
        "Litellm_Settings": "pynix_os.services.litellm:Litellm_Settings",
        "Litestream": "pynix_os.services.litestream:Litestream",
        "Livebook": "pynix_os.services.livebook:Livebook",
        "Livekit": "pynix_os.services.livekit:Livekit",
        "Livekit_Ingress": "pynix_os.services.livekit:Livekit_Ingress",
        "Livekit_Ingress_OpenFirewall": "pynix_os.services.livekit:Livekit_Ingress_OpenFirewall",
        "Livekit_Ingress_Settings": "pynix_os.services.livekit:Livekit_Ingress_Settings",
        "Livekit_Redis": "pynix_os.services.livekit:Livekit_Redis",
        "Livekit_Settings": "pynix_os.services.livekit:Livekit_Settings",
        "Lix": "pynix_os.lix.__options__:Lix",
        "Lix_BuildMachines": "pynix_os.lix.__options__:Lix_BuildMachines",
        "Lix_BuildMachines_Machines_Value": "pynix_os.lix.__options__:Lix_BuildMachines_Machines_Value",
        "LkJwtService": "pynix_os.services.lk_jwt_service:LkJwtService",
        "LlamaCpp": "pynix_os.services.llama_cpp:LlamaCpp",
        "LlamaCpp_Settings": "pynix_os.services.llama_cpp:LlamaCpp_Settings",
        "LlamaSwap": "pynix_os.services.llama_swap:LlamaSwap",
        "LlamaSwap_Settings": "pynix_os.services.llama_swap:LlamaSwap_Settings",
        "LlamaSwap_Tls": "pynix_os.services.llama_swap:LlamaSwap_Tls",
        "Lldap": "pynix_os.services.lldap:Lldap",
        "Lldap_Settings": "pynix_os.services.lldap:Lldap_Settings",
        "Lldpd": "pynix_os.services.lldpd:Lldpd",
        "Loader": "pynix_os.boot.loader:Loader",
        "Loader_Efi": "pynix_os.boot.loader:Loader_Efi",
        "Loader_External": "pynix_os.boot.loader:Loader_External",
        "Loader_GenerationsDir": "pynix_os.boot.loader:Loader_GenerationsDir",
        "Loader_GenericExtlinuxCompatible": "pynix_os.boot.loader:Loader_GenericExtlinuxCompatible",
        "Loader_GenericExtlinuxCompatible_MirroredBoots_Item": "pynix_os.boot.loader:Loader_GenericExtlinuxCompatible_MirroredBoots_Item",
        "Loader_Grub": "pynix_os.boot.loader:Loader_Grub",
        "Loader_Grub_Memtest86": "pynix_os.boot.loader:Loader_Grub_Memtest86",
        "Loader_Grub_MirroredBoots_Item": "pynix_os.boot.loader:Loader_Grub_MirroredBoots_Item",
        "Loader_Grub_Users_Value": "pynix_os.boot.loader:Loader_Grub_Users_Value",
        "Loader_InitScript": "pynix_os.boot.loader:Loader_InitScript",
        "Loader_Limine": "pynix_os.boot.loader:Loader_Limine",
        "Loader_Limine_SecureBoot": "pynix_os.boot.loader:Loader_Limine_SecureBoot",
        "Loader_Limine_SecureBoot_AutoEnrollKeys": "pynix_os.boot.loader:Loader_Limine_SecureBoot_AutoEnrollKeys",
        "Loader_Limine_Style": "pynix_os.boot.loader:Loader_Limine_Style",
        "Loader_Limine_Style_GraphicalTerminal": "pynix_os.boot.loader:Loader_Limine_Style_GraphicalTerminal",
        "Loader_Limine_Style_GraphicalTerminal_Font": "pynix_os.boot.loader:Loader_Limine_Style_GraphicalTerminal_Font",
        "Loader_Limine_Style_Interface": "pynix_os.boot.loader:Loader_Limine_Style_Interface",
        "Loader_Refind": "pynix_os.boot.loader:Loader_Refind",
        "Loader_SystemdBoot": "pynix_os.boot.loader:Loader_SystemdBoot",
        "Loader_SystemdBoot_BootCounting": "pynix_os.boot.loader:Loader_SystemdBoot_BootCounting",
        "Loader_SystemdBoot_Edk2UefiShell": "pynix_os.boot.loader:Loader_SystemdBoot_Edk2UefiShell",
        "Loader_SystemdBoot_Memtest86": "pynix_os.boot.loader:Loader_SystemdBoot_Memtest86",
        "Loader_SystemdBoot_Netbootxyz": "pynix_os.boot.loader:Loader_SystemdBoot_Netbootxyz",
        "Loader_SystemdBoot_Windows_Value": "pynix_os.boot.loader:Loader_SystemdBoot_Windows_Value",
        "LocalContentShare": "pynix_os.services.local_content_share:LocalContentShare",
        "Localsend": "pynix_os.programs.localsend:Localsend",
        "Localtimed": "pynix_os.services.localtimed:Localtimed",
        "Locate": "pynix_os.services.locate:Locate",
        "Location": "pynix_os.location.__options__:Location",
        "Logcheck": "pynix_os.services.logcheck:Logcheck",
        "Logcheck_IgnoreCron_Value": "pynix_os.services.logcheck:Logcheck_IgnoreCron_Value",
        "Logcheck_Ignore_Value": "pynix_os.services.logcheck:Logcheck_Ignore_Value",
        "LoginDefs": "pynix_os.security.loginDefs:LoginDefs",
        "LoginDefs_Settings": "pynix_os.security.loginDefs:LoginDefs_Settings",
        "Logind": "pynix_os.services.logind:Logind",
        "Logind_Settings": "pynix_os.services.logind:Logind_Settings",
        "Logind_Settings_Login": "pynix_os.services.logind:Logind_Settings_Login",
        "Logiops": "pynix_os.services.logiops:Logiops",
        "Logitech": "pynix_os.hardware.logitech:Logitech",
        "Logitech_Lcd": "pynix_os.hardware.logitech:Logitech_Lcd",
        "Logitech_Wireless": "pynix_os.hardware.logitech:Logitech_Wireless",
        "Logkeys": "pynix_os.services.logkeys:Logkeys",
        "LogmeinHamachi": "pynix_os.services.logmein_hamachi:LogmeinHamachi",
        "Logrotate": "pynix_os.services.logrotate:Logrotate",
        "Logrotate_Settings_Value": "pynix_os.services.logrotate:Logrotate_Settings_Value",
        "Logstash": "pynix_os.services.logstash:Logstash",
        "Loki": "pynix_os.services.loki:Loki",
        "Lokinet": "pynix_os.services.lokinet:Lokinet",
        "Lokinet_Settings": "pynix_os.services.lokinet:Lokinet_Settings",
        "Longview": "pynix_os.services.longview:Longview",
        "Lorri": "pynix_os.services.lorri:Lorri",
        "Lubelogger": "pynix_os.services.lubelogger:Lubelogger",
        "Lvm": "pynix_os.services.lvm:Lvm",
        "Lvm_Boot": "pynix_os.services.lvm:Lvm_Boot",
        "Lvm_Boot_Thin": "pynix_os.services.lvm:Lvm_Boot_Thin",
        "Lvm_Boot_Vdo": "pynix_os.services.lvm:Lvm_Boot_Vdo",
        "Lvm_Dmeventd": "pynix_os.services.lvm:Lvm_Dmeventd",
        "Lvm_ResizeHelper": "pynix_os.services.lvm:Lvm_ResizeHelper",
        "Lxc": "pynix_os.virtualisation.lxc:Lxc",
        "Lxc_Lxcfs": "pynix_os.virtualisation.lxc:Lxc_Lxcfs",
        "LxdImageServer": "pynix_os.services.lxd_image_server:LxdImageServer",
        "LxdImageServer_Nginx": "pynix_os.services.lxd_image_server:LxdImageServer_Nginx",
        "Lxmd": "pynix_os.services.lxmd:Lxmd",
        "Lxmd_HealthCheck": "pynix_os.services.lxmd:Lxmd_HealthCheck",
        "Lxmd_Rnsd": "pynix_os.services.lxmd:Lxmd_Rnsd",
        "Lxqt": "pynix_os.environment.lxqt:Lxqt",
        "MackerelAgent": "pynix_os.services.mackerel_agent:MackerelAgent",
        "MackerelAgent_Settings": "pynix_os.services.mackerel_agent:MackerelAgent_Settings",
        "Maddy": "pynix_os.services.maddy:Maddy",
        "Maddy_EnsureCredentials_Value": "pynix_os.services.maddy:Maddy_EnsureCredentials_Value",
        "Maddy_Tls": "pynix_os.services.maddy:Maddy_Tls",
        "Maddy_Tls_Certificates_Item": "pynix_os.services.maddy:Maddy_Tls_Certificates_Item",
        "MagicWormholeMailboxServer": "pynix_os.services.magic_wormhole_mailbox_server:MagicWormholeMailboxServer",
        "Magnetico": "pynix_os.services.magnetico:Magnetico",
        "Magnetico_Crawler": "pynix_os.services.magnetico:Magnetico_Crawler",
        "Magnetico_Web": "pynix_os.services.magnetico:Magnetico_Web",
        "Mail": "pynix_os.services.mail:Mail",
        "Mail_SendmailSetuidWrapper": "pynix_os.services.mail:Mail_SendmailSetuidWrapper",
        "Mailcatcher": "pynix_os.services.mailcatcher:Mailcatcher",
        "Mailcatcher_Http": "pynix_os.services.mailcatcher:Mailcatcher_Http",
        "Mailcatcher_Smtp": "pynix_os.services.mailcatcher:Mailcatcher_Smtp",
        "Mailhog": "pynix_os.services.mailhog:Mailhog",
        "Mailman": "pynix_os.services.mailman:Mailman",
        "Mailman_Hyperkitty": "pynix_os.services.mailman:Mailman_Hyperkitty",
        "Mailman_Ldap": "pynix_os.services.mailman:Mailman_Ldap",
        "Mailman_Ldap_AttrMap": "pynix_os.services.mailman:Mailman_Ldap_AttrMap",
        "Mailman_Ldap_UserSearch": "pynix_os.services.mailman:Mailman_Ldap_UserSearch",
        "Mailman_Serve": "pynix_os.services.mailman:Mailman_Serve",
        "Mailpit": "pynix_os.services.mailpit:Mailpit",
        "Mailpit_Instances_Value": "pynix_os.services.mailpit:Mailpit_Instances_Value",
        "Mainsail": "pynix_os.services.mainsail:Mainsail",
        "Mainsail_Nginx": "pynix_os.services.mainsail:Mainsail_Nginx",
        "Mainsail_Nginx_Listen_Item": "pynix_os.services.mainsail:Mainsail_Nginx_Listen_Item",
        "Mainsail_Nginx_Locations_Value": "pynix_os.services.mainsail:Mainsail_Nginx_Locations_Value",
        "Malcontent": "pynix_os.services.malcontent:Malcontent",
        "Mame": "pynix_os.services.mame:Mame",
        "Man": "pynix_os.documentation.man:Man",
        "Man_Cache": "pynix_os.documentation.man:Man_Cache",
        "Man_ManDb": "pynix_os.documentation.man:Man_ManDb",
        "Man_Mandoc": "pynix_os.documentation.man:Man_Mandoc",
        "Man_Mandoc_Settings": "pynix_os.documentation.man:Man_Mandoc_Settings",
        "Mango": "pynix_os.programs.mango:Mango",
        "Manticore": "pynix_os.services.manticore:Manticore",
        "Manticore_Settings": "pynix_os.services.manticore:Manticore_Settings",
        "Marytts": "pynix_os.services.marytts:Marytts",
        "Marytts_Settings": "pynix_os.services.marytts:Marytts_Settings",
        "Mastodon": "pynix_os.services.mastodon:Mastodon",
        "Mastodon_Database": "pynix_os.services.mastodon:Mastodon_Database",
        "Mastodon_Elasticsearch": "pynix_os.services.mastodon:Mastodon_Elasticsearch",
        "Mastodon_MediaAutoRemove": "pynix_os.services.mastodon:Mastodon_MediaAutoRemove",
        "Mastodon_Redis": "pynix_os.services.mastodon:Mastodon_Redis",
        "Mastodon_SidekiqProcesses_Value": "pynix_os.services.mastodon:Mastodon_SidekiqProcesses_Value",
        "Mastodon_Smtp": "pynix_os.services.mastodon:Mastodon_Smtp",
        "Mate": "pynix_os.environment.mate:Mate",
        "Matomo": "pynix_os.services.matomo:Matomo",
        "Matomo_Nginx": "pynix_os.services.matomo:Matomo_Nginx",
        "Matomo_Nginx_Listen_Item": "pynix_os.services.matomo:Matomo_Nginx_Listen_Item",
        "Matomo_Nginx_Locations_Value": "pynix_os.services.matomo:Matomo_Nginx_Locations_Value",
        "MatrixAlertmanager": "pynix_os.services.matrix_alertmanager:MatrixAlertmanager",
        "MatrixAlertmanager_MatrixRooms_Item": "pynix_os.services.matrix_alertmanager:MatrixAlertmanager_MatrixRooms_Item",
        "MatrixAppserviceIrc": "pynix_os.services.matrix_appservice_irc:MatrixAppserviceIrc",
        "MatrixAppserviceIrc_Settings": "pynix_os.services.matrix_appservice_irc:MatrixAppserviceIrc_Settings",
        "MatrixAppserviceIrc_Settings_Database": "pynix_os.services.matrix_appservice_irc:MatrixAppserviceIrc_Settings_Database",
        "MatrixAppserviceIrc_Settings_Homeserver": "pynix_os.services.matrix_appservice_irc:MatrixAppserviceIrc_Settings_Homeserver",
        "MatrixAppserviceIrc_Settings_IrcService": "pynix_os.services.matrix_appservice_irc:MatrixAppserviceIrc_Settings_IrcService",
        "MatrixAppserviceIrc_Settings_IrcService_Servers": "pynix_os.services.matrix_appservice_irc:MatrixAppserviceIrc_Settings_IrcService_Servers",
        "MatrixAuthenticationService": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService",
        "MatrixAuthenticationService_Settings": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService_Settings",
        "MatrixAuthenticationService_Settings_HttpListeners_Item": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService_Settings_HttpListeners_Item",
        "MatrixAuthenticationService_Settings_HttpListeners_Item_Binds_Item": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService_Settings_HttpListeners_Item_Binds_Item",
        "MatrixAuthenticationService_Settings_HttpListeners_Item_Resources_Item": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService_Settings_HttpListeners_Item_Resources_Item",
        "MatrixAuthenticationService_Settings_PasswordsSchemes_Item": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService_Settings_PasswordsSchemes_Item",
        "MatrixAuthenticationService_Settings_UpstreamOauth2Providers_Item": "pynix_os.services.matrix_authentication_service:MatrixAuthenticationService_Settings_UpstreamOauth2Providers_Item",
        "MatrixConduit": "pynix_os.services.matrix_conduit:MatrixConduit",
        "MatrixConduit_Settings": "pynix_os.services.matrix_conduit:MatrixConduit_Settings",
        "MatrixContinuwuity": "pynix_os.services.matrix_continuwuity:MatrixContinuwuity",
        "MatrixContinuwuity_Admin": "pynix_os.services.matrix_continuwuity:MatrixContinuwuity_Admin",
        "MatrixContinuwuity_Settings": "pynix_os.services.matrix_continuwuity:MatrixContinuwuity_Settings",
        "MatrixHookshot": "pynix_os.services.matrix_hookshot:MatrixHookshot",
        "MatrixHookshot_Settings": "pynix_os.services.matrix_hookshot:MatrixHookshot_Settings",
        "MatrixSynapse": "pynix_os.services.matrix_synapse:MatrixSynapse",
        "MatrixSynapse_Settings": "pynix_os.services.matrix_synapse:MatrixSynapse_Settings",
        "MatrixSynapse_Settings_Listeners_Item": "pynix_os.services.matrix_synapse:MatrixSynapse_Settings_Listeners_Item",
        "MatrixSynapse_Settings_Listeners_Item_Resources_Item": "pynix_os.services.matrix_synapse:MatrixSynapse_Settings_Listeners_Item_Resources_Item",
        "MatrixSynapse_Settings_Redis": "pynix_os.services.matrix_synapse:MatrixSynapse_Settings_Redis",
        "MatrixSynapse_Settings_TrustedKeyServers_Item": "pynix_os.services.matrix_synapse:MatrixSynapse_Settings_TrustedKeyServers_Item",
        "MatrixSynapse_Workers_Value": "pynix_os.services.matrix_synapse:MatrixSynapse_Workers_Value",
        "MatrixTuwunel": "pynix_os.services.matrix_tuwunel:MatrixTuwunel",
        "MatrixTuwunel_Settings": "pynix_os.services.matrix_tuwunel:MatrixTuwunel_Settings",
        "MatterServer": "pynix_os.services.matter_server:MatterServer",
        "Matterbridge": "pynix_os.services.matterbridge:Matterbridge",
        "MatterjsServer": "pynix_os.services.matterjs_server:MatterjsServer",
        "Mattermost": "pynix_os.services.mattermost:Mattermost",
        "Mattermost_Database": "pynix_os.services.mattermost:Mattermost_Database",
        "Mattermost_Matterircd": "pynix_os.services.mattermost:Mattermost_Matterircd",
        "Mattermost_Socket": "pynix_os.services.mattermost:Mattermost_Socket",
        "Mattermost_Telemetry": "pynix_os.services.mattermost:Mattermost_Telemetry",
        "Maubot": "pynix_os.services.maubot:Maubot",
        "Maubot_Settings": "pynix_os.services.maubot:Maubot_Settings",
        "Maubot_Settings_Homeservers_Value": "pynix_os.services.maubot:Maubot_Settings_Homeservers_Value",
        "Maubot_Settings_PluginDatabases": "pynix_os.services.maubot:Maubot_Settings_PluginDatabases",
        "Maubot_Settings_PluginDirectories": "pynix_os.services.maubot:Maubot_Settings_PluginDirectories",
        "Maubot_Settings_Server": "pynix_os.services.maubot:Maubot_Settings_Server",
        "MautrixDiscord": "pynix_os.services.mautrix_discord:MautrixDiscord",
        "MautrixMeta": "pynix_os.services.mautrix_meta:MautrixMeta",
        "MautrixMeta_Instances_Value": "pynix_os.services.mautrix_meta:MautrixMeta_Instances_Value",
        "MautrixSignal": "pynix_os.services.mautrix_signal:MautrixSignal",
        "MautrixTelegram": "pynix_os.services.mautrix_telegram:MautrixTelegram",
        "MautrixWhatsapp": "pynix_os.services.mautrix_whatsapp:MautrixWhatsapp",
        "Mbpfan": "pynix_os.services.mbpfan:Mbpfan",
        "Mbpfan_Settings": "pynix_os.services.mbpfan:Mbpfan_Settings",
        "Mcelog": "pynix_os.hardware.mcelog:Mcelog",
        "Mchprs": "pynix_os.services.mchprs:Mchprs",
        "Mchprs_Settings": "pynix_os.services.mchprs:Mchprs_Settings",
        "Mchprs_Whitelist": "pynix_os.services.mchprs:Mchprs_Whitelist",
        "Mdevctl": "pynix_os.programs.mdevctl:Mdevctl",
        "Mealie": "pynix_os.services.mealie:Mealie",
        "Mealie_Database": "pynix_os.services.mealie:Mealie_Database",
        "Mediagoblin": "pynix_os.services.mediagoblin:Mediagoblin",
        "Mediagoblin_Paste": "pynix_os.services.mediagoblin:Mediagoblin_Paste",
        "Mediagoblin_Paste_Settings": "pynix_os.services.mediagoblin:Mediagoblin_Paste_Settings",
        "Mediagoblin_Settings": "pynix_os.services.mediagoblin:Mediagoblin_Settings",
        "Mediamtx": "pynix_os.services.mediamtx:Mediamtx",
        "Mediatomb": "pynix_os.services.mediatomb:Mediatomb",
        "Mediatomb_MediaDirectories_Item": "pynix_os.services.mediatomb:Mediatomb_MediaDirectories_Item",
        "Mediawiki": "pynix_os.services.mediawiki:Mediawiki",
        "Mediawiki_Httpd": "pynix_os.services.mediawiki:Mediawiki_Httpd",
        "Mediawiki_Httpd_VirtualHost": "pynix_os.services.mediawiki:Mediawiki_Httpd_VirtualHost",
        "Mediawiki_Httpd_VirtualHost_Listen_Item": "pynix_os.services.mediawiki:Mediawiki_Httpd_VirtualHost_Listen_Item",
        "Mediawiki_Httpd_VirtualHost_Locations_Value": "pynix_os.services.mediawiki:Mediawiki_Httpd_VirtualHost_Locations_Value",
        "Mediawiki_Nginx": "pynix_os.services.mediawiki:Mediawiki_Nginx",
        "Meilisearch": "pynix_os.services.meilisearch:Meilisearch",
        "Meilisearch_Settings": "pynix_os.services.meilisearch:Meilisearch_Settings",
        "Memcached": "pynix_os.services.memcached:Memcached",
        "MemeBingoWeb": "pynix_os.services.meme_bingo_web:MemeBingoWeb",
        "MemoryAllocator": "pynix_os.environment.memoryAllocator:MemoryAllocator",
        "Memos": "pynix_os.services.memos:Memos",
        "Menus": "pynix_os.xdg.menus:Menus",
        "Mepo": "pynix_os.programs.mepo:Mepo",
        "Mepo_LocationBackends": "pynix_os.programs.mepo:Mepo_LocationBackends",
        "Merecat": "pynix_os.services.merecat:Merecat",
        "Meshcentral": "pynix_os.services.meshcentral:Meshcentral",
        "Meshcentral_Settings": "pynix_os.services.meshcentral:Meshcentral_Settings",
        "Meshtasticd": "pynix_os.services.meshtasticd:Meshtasticd",
        "Meta": "pynix_os.meta.__options__:Meta",
        "Metabase": "pynix_os.services.metabase:Metabase",
        "Metabase_Listen": "pynix_os.services.metabase:Metabase_Listen",
        "Metabase_Ssl": "pynix_os.services.metabase:Metabase_Ssl",
        "Metricbeat": "pynix_os.services.metricbeat:Metricbeat",
        "Metricbeat_Modules_Value": "pynix_os.services.metricbeat:Metricbeat_Modules_Value",
        "Metricbeat_Settings": "pynix_os.services.metricbeat:Metricbeat_Settings",
        "Microbin": "pynix_os.services.microbin:Microbin",
        "Microbin_Settings": "pynix_os.services.microbin:Microbin_Settings",
        "Microsocks": "pynix_os.services.microsocks:Microsocks",
        "Mighttpd2": "pynix_os.services.mighttpd2:Mighttpd2",
        "Mihomo": "pynix_os.services.mihomo:Mihomo",
        "Mime": "pynix_os.xdg.mime:Mime",
        "Mimir": "pynix_os.services.mimir:Mimir",
        "MinecraftServer": "pynix_os.services.minecraft_server:MinecraftServer",
        "MinetestServer": "pynix_os.services.minetest_server:MinetestServer",
        "Minidlna": "pynix_os.services.minidlna:Minidlna",
        "Minidlna_Settings": "pynix_os.services.minidlna:Minidlna_Settings",
        "Miniflux": "pynix_os.services.miniflux:Miniflux",
        "Miniflux_Config": "pynix_os.services.miniflux:Miniflux_Config",
        "Mininet": "pynix_os.programs.mininet:Mininet",
        "Minio": "pynix_os.services.minio:Minio",
        "Minipro": "pynix_os.programs.minipro:Minipro",
        "Miniupnpd": "pynix_os.services.miniupnpd:Miniupnpd",
        "Mirakurun": "pynix_os.services.mirakurun:Mirakurun",
        "Miredo": "pynix_os.services.miredo:Miredo",
        "Miriway": "pynix_os.programs.miriway:Miriway",
        "Misskey": "pynix_os.services.misskey:Misskey",
        "Misskey_Database": "pynix_os.services.misskey:Misskey_Database",
        "Misskey_Meilisearch": "pynix_os.services.misskey:Misskey_Meilisearch",
        "Misskey_Redis": "pynix_os.services.misskey:Misskey_Redis",
        "Misskey_ReverseProxy": "pynix_os.services.misskey:Misskey_ReverseProxy",
        "Misskey_Settings": "pynix_os.services.misskey:Misskey_Settings",
        "Misskey_Settings_Db": "pynix_os.services.misskey:Misskey_Settings_Db",
        "Misskey_Settings_Meilisearch": "pynix_os.services.misskey:Misskey_Settings_Meilisearch",
        "Misskey_Settings_Redis": "pynix_os.services.misskey:Misskey_Settings_Redis",
        "Mjolnir": "pynix_os.services.mjolnir:Mjolnir",
        "Mjolnir_Encryption": "pynix_os.services.mjolnir:Mjolnir_Encryption",
        "Mjolnir_Pantalaimon": "pynix_os.services.mjolnir:Mjolnir_Pantalaimon",
        "Mjolnir_Pantalaimon_Options": "pynix_os.services.mjolnir:Mjolnir_Pantalaimon_Options",
        "MjpgStreamer": "pynix_os.services.mjpg_streamer:MjpgStreamer",
        "Mlmmj": "pynix_os.services.mlmmj:Mlmmj",
        "Mmsd": "pynix_os.services.mmsd:Mmsd",
        "Mobilizon": "pynix_os.services.mobilizon:Mobilizon",
        "Mobilizon_Nginx": "pynix_os.services.mobilizon:Mobilizon_Nginx",
        "Mobilizon_Settings": "pynix_os.services.mobilizon:Mobilizon_Settings",
        "Modemmanager": "pynix_os.networking.modemmanager:Modemmanager",
        "Modemmanager_FccUnlockScripts_Item": "pynix_os.networking.modemmanager:Modemmanager_FccUnlockScripts_Item",
        "ModprobeConfig": "pynix_os.boot.modprobeConfig:ModprobeConfig",
        "MollyBrown": "pynix_os.services.molly_brown:MollyBrown",
        "Mollysocket": "pynix_os.services.mollysocket:Mollysocket",
        "Mollysocket_Settings": "pynix_os.services.mollysocket:Mollysocket_Settings",
        "Monado": "pynix_os.services.monado:Monado",
        "Monero": "pynix_os.services.monero:Monero",
        "Monero_Limits": "pynix_os.services.monero:Monero_Limits",
        "Monero_Mining": "pynix_os.services.monero:Monero_Mining",
        "Monero_Rpc": "pynix_os.services.monero:Monero_Rpc",
        "Monetdb": "pynix_os.services.monetdb:Monetdb",
        "Mongodb": "pynix_os.services.mongodb:Mongodb",
        "Monica": "pynix_os.services.monica:Monica",
        "Monica_Config_Value_Or": "pynix_os.services.monica:Monica_Config_Value_Or",
        "Monica_Database": "pynix_os.services.monica:Monica_Database",
        "Monica_Mail": "pynix_os.services.monica:Monica_Mail",
        "Monica_Nginx": "pynix_os.services.monica:Monica_Nginx",
        "Monica_Nginx_Listen_Item": "pynix_os.services.monica:Monica_Nginx_Listen_Item",
        "Monica_Nginx_Locations_Value": "pynix_os.services.monica:Monica_Nginx_Locations_Value",
        "Monit": "pynix_os.services.monit:Monit",
        "Moodle": "pynix_os.services.moodle:Moodle",
        "Moodle_VirtualHost": "pynix_os.services.moodle:Moodle_VirtualHost",
        "Moodle_VirtualHost_Listen_Item": "pynix_os.services.moodle:Moodle_VirtualHost_Listen_Item",
        "Moodle_VirtualHost_Locations_Value": "pynix_os.services.moodle:Moodle_VirtualHost_Locations_Value",
        "MoonlightQt": "pynix_os.programs.moonlight_qt:MoonlightQt",
        "Moonraker": "pynix_os.services.moonraker:Moonraker",
        "Moonraker_Analysis": "pynix_os.services.moonraker:Moonraker_Analysis",
        "Moonshine": "pynix_os.services.moonshine:Moonshine",
        "Moosefs": "pynix_os.services.moosefs:Moosefs",
        "Moosefs_Cgiserver": "pynix_os.services.moosefs:Moosefs_Cgiserver",
        "Moosefs_Cgiserver_Settings": "pynix_os.services.moosefs:Moosefs_Cgiserver_Settings",
        "Moosefs_Chunkserver": "pynix_os.services.moosefs:Moosefs_Chunkserver",
        "Moosefs_Chunkserver_Settings": "pynix_os.services.moosefs:Moosefs_Chunkserver_Settings",
        "Moosefs_Client": "pynix_os.services.moosefs:Moosefs_Client",
        "Moosefs_Master": "pynix_os.services.moosefs:Moosefs_Master",
        "Moosefs_Master_Settings": "pynix_os.services.moosefs:Moosefs_Master_Settings",
        "Moosefs_Metalogger": "pynix_os.services.moosefs:Moosefs_Metalogger",
        "Moosefs_Metalogger_Settings": "pynix_os.services.moosefs:Moosefs_Metalogger_Settings",
        "Mopidy": "pynix_os.services.mopidy:Mopidy",
        "Mosh": "pynix_os.programs.mosh:Mosh",
        "Mosquitto": "pynix_os.services.mosquitto:Mosquitto",
        "Mosquitto_Bridges_Value": "pynix_os.services.mosquitto:Mosquitto_Bridges_Value",
        "Mosquitto_Bridges_Value_Addresses_Item": "pynix_os.services.mosquitto:Mosquitto_Bridges_Value_Addresses_Item",
        "Mosquitto_Bridges_Value_Settings": "pynix_os.services.mosquitto:Mosquitto_Bridges_Value_Settings",
        "Mosquitto_Listeners_Item": "pynix_os.services.mosquitto:Mosquitto_Listeners_Item",
        "Mosquitto_Listeners_Item_AuthPlugins_Item": "pynix_os.services.mosquitto:Mosquitto_Listeners_Item_AuthPlugins_Item",
        "Mosquitto_Listeners_Item_Settings": "pynix_os.services.mosquitto:Mosquitto_Listeners_Item_Settings",
        "Mosquitto_Listeners_Item_Users_Value": "pynix_os.services.mosquitto:Mosquitto_Listeners_Item_Users_Value",
        "Mosquitto_Settings": "pynix_os.services.mosquitto:Mosquitto_Settings",
        "Motioneye": "pynix_os.services.motioneye:Motioneye",
        "Motioneye_Packages": "pynix_os.services.motioneye:Motioneye_Packages",
        "MouseActions": "pynix_os.programs.mouse_actions:MouseActions",
        "Movim": "pynix_os.services.movim:Movim",
        "Movim_H2o": "pynix_os.services.movim:Movim_H2o",
        "Movim_H2o_Acme": "pynix_os.services.movim:Movim_H2o_Acme",
        "Movim_H2o_Http": "pynix_os.services.movim:Movim_H2o_Http",
        "Movim_H2o_Tls": "pynix_os.services.movim:Movim_H2o_Tls",
        "Movim_H2o_Tls_Identity_Item": "pynix_os.services.movim:Movim_H2o_Tls_Identity_Item",
        "Movim_MinifyStaticFiles_Or": "pynix_os.services.movim:Movim_MinifyStaticFiles_Or",
        "Movim_MinifyStaticFiles_Or_Script": "pynix_os.services.movim:Movim_MinifyStaticFiles_Or_Script",
        "Movim_MinifyStaticFiles_Or_Style": "pynix_os.services.movim:Movim_MinifyStaticFiles_Or_Style",
        "Movim_MinifyStaticFiles_Or_Svg": "pynix_os.services.movim:Movim_MinifyStaticFiles_Or_Svg",
        "Movim_Nginx": "pynix_os.services.movim:Movim_Nginx",
        "Movim_Nginx_Listen_Item": "pynix_os.services.movim:Movim_Nginx_Listen_Item",
        "Movim_Nginx_Locations_Value": "pynix_os.services.movim:Movim_Nginx_Locations_Value",
        "Movim_PodConfig": "pynix_os.services.movim:Movim_PodConfig",
        "Movim_PrecompressStaticFiles": "pynix_os.services.movim:Movim_PrecompressStaticFiles",
        "Mozillavpn": "pynix_os.services.mozillavpn:Mozillavpn",
        "Mpd": "pynix_os.services.mpd:Mpd",
        "Mpd_Credentials_Item": "pynix_os.services.mpd:Mpd_Credentials_Item",
        "Mpd_Settings": "pynix_os.services.mpd:Mpd_Settings",
        "Mpdscribble": "pynix_os.services.mpdscribble:Mpdscribble",
        "Mpdscribble_Endpoints_Value": "pynix_os.services.mpdscribble:Mpdscribble_Endpoints_Value",
        "Mptcpd": "pynix_os.services.mptcpd:Mptcpd",
        "Mqtt2influxdb": "pynix_os.services.mqtt2influxdb:Mqtt2influxdb",
        "Mqtt2influxdb_Influxdb": "pynix_os.services.mqtt2influxdb:Mqtt2influxdb_Influxdb",
        "Mqtt2influxdb_Mqtt": "pynix_os.services.mqtt2influxdb:Mqtt2influxdb_Mqtt",
        "Mqtt2influxdb_Points_Item": "pynix_os.services.mqtt2influxdb:Mqtt2influxdb_Points_Item",
        "Mqtt2influxdb_Points_Item_Fields": "pynix_os.services.mqtt2influxdb:Mqtt2influxdb_Points_Item_Fields",
        "Msmtp": "pynix_os.programs.msmtp:Msmtp",
        "Mstpd": "pynix_os.services.mstpd:Mstpd",
        "Mtprotoproxy": "pynix_os.services.mtprotoproxy:Mtprotoproxy",
        "Mtr": "pynix_os.programs.mtr:Mtr",
        "MtrExporter": "pynix_os.services.mtr_exporter:MtrExporter",
        "MtrExporter_Jobs_Item": "pynix_os.services.mtr_exporter:MtrExporter_Jobs_Item",
        "MullvadVpn": "pynix_os.services.mullvad_vpn:MullvadVpn",
        "MullvadVpn_Gui": "pynix_os.services.mullvad_vpn:MullvadVpn_Gui",
        "Multipath": "pynix_os.services.multipath:Multipath",
        "Multipath_Devices_Item": "pynix_os.services.multipath:Multipath_Devices_Item",
        "Multipath_PathGroups_Item": "pynix_os.services.multipath:Multipath_PathGroups_Item",
        "Munge": "pynix_os.services.munge:Munge",
        "MuninCron": "pynix_os.services.munin_cron:MuninCron",
        "MuninNode": "pynix_os.services.munin_node:MuninNode",
        "Murmur": "pynix_os.services.murmur:Murmur",
        "Murmur_Tls": "pynix_os.services.murmur:Murmur_Tls",
        "MusicAssistant": "pynix_os.services.music_assistant:MusicAssistant",
        "MwProCapture": "pynix_os.hardware.mwProCapture:MwProCapture",
        "Mycelium": "pynix_os.services.mycelium:Mycelium",
        "Mympd": "pynix_os.services.mympd:Mympd",
        "Mympd_Settings": "pynix_os.services.mympd:Mympd_Settings",
        "Services_Mysql": "pynix_os.services.mysql:Mysql",
        "Users_Mysql": "pynix_os.users.mysql:Mysql",
        "MysqlBackup": "pynix_os.services.mysqlBackup:MysqlBackup",
        "Mysql_EnsureUsers_Item": "pynix_os.services.mysql:Mysql_EnsureUsers_Item",
        "Mysql_GaleraCluster": "pynix_os.services.mysql:Mysql_GaleraCluster",
        "Mysql_InitialDatabases_Item": "pynix_os.services.mysql:Mysql_InitialDatabases_Item",
        "Mysql_Nss": "pynix_os.users.mysql:Mysql_Nss",
        "Mysql_Pam": "pynix_os.users.mysql:Mysql_Pam",
        "Mysql_Replication": "pynix_os.services.mysql:Mysql_Replication",
        "N1password": "pynix_os.programs.n__1password:N1password",
        "N1passwordGui": "pynix_os.programs.n__1password_gui:N1passwordGui",
        "N3proxy": "pynix_os.services.n__3proxy:N3proxy",
        "N3proxy_Resolution": "pynix_os.services.n__3proxy:N3proxy_Resolution",
        "N3proxy_Services_Item": "pynix_os.services.n__3proxy:N3proxy_Services_Item",
        "N3proxy_Services_Item_Acl_Item": "pynix_os.services.n__3proxy:N3proxy_Services_Item_Acl_Item",
        "N8n": "pynix_os.services.n8n:N8n",
        "N8n_Environment": "pynix_os.services.n8n:N8n_Environment",
        "N8n_TaskRunners": "pynix_os.services.n8n:N8n_TaskRunners",
        "N8n_TaskRunners_Environment": "pynix_os.services.n8n:N8n_TaskRunners_Environment",
        "N8n_TaskRunners_Runners_Value": "pynix_os.services.n8n:N8n_TaskRunners_Runners_Value",
        "Nagios": "pynix_os.services.nagios:Nagios",
        "Nagios_VirtualHost": "pynix_os.services.nagios:Nagios_VirtualHost",
        "Nagios_VirtualHost_Listen_Item": "pynix_os.services.nagios:Nagios_VirtualHost_Listen_Item",
        "Nagios_VirtualHost_Locations_Value": "pynix_os.services.nagios:Nagios_VirtualHost_Locations_Value",
        "Namecoind": "pynix_os.services.namecoind:Namecoind",
        "Namecoind_Rpc": "pynix_os.services.namecoind:Namecoind_Rpc",
        "Nano": "pynix_os.programs.nano:Nano",
        "NarServe": "pynix_os.services.nar_serve:NarServe",
        "Nat": "pynix_os.networking.nat:Nat",
        "Nat_ForwardPorts_Item": "pynix_os.networking.nat:Nat_ForwardPorts_Item",
        "Nats": "pynix_os.services.nats:Nats",
        "NautilusOpenAnyTerminal": "pynix_os.programs.nautilus_open_any_terminal:NautilusOpenAnyTerminal",
        "Navidrome": "pynix_os.services.navidrome:Navidrome",
        "Navidrome_Settings": "pynix_os.services.navidrome:Navidrome_Settings",
        "Programs_Nbd": "pynix_os.programs.nbd:Nbd",
        "Services_Nbd": "pynix_os.services.nbd:Nbd",
        "Nbd_Server": "pynix_os.services.nbd:Nbd_Server",
        "Nbd_Server_Exports_Value": "pynix_os.services.nbd:Nbd_Server_Exports_Value",
        "Ncdns": "pynix_os.services.ncdns:Ncdns",
        "Ncdns_Dnssec": "pynix_os.services.ncdns:Ncdns_Dnssec",
        "Ncdns_Dnssec_Keys": "pynix_os.services.ncdns:Ncdns_Dnssec_Keys",
        "Ncdns_Identity": "pynix_os.services.ncdns:Ncdns_Identity",
        "Ncps": "pynix_os.services.ncps:Ncps",
        "Ncps_Analytics": "pynix_os.services.ncps:Ncps_Analytics",
        "Ncps_Analytics_Reporting": "pynix_os.services.ncps:Ncps_Analytics_Reporting",
        "Ncps_Cache": "pynix_os.services.ncps:Ncps_Cache",
        "Ncps_Cache_Cdc": "pynix_os.services.ncps:Ncps_Cache_Cdc",
        "Ncps_Cache_Database": "pynix_os.services.ncps:Ncps_Cache_Database",
        "Ncps_Cache_Database_Pool": "pynix_os.services.ncps:Ncps_Cache_Database_Pool",
        "Ncps_Cache_Lock": "pynix_os.services.ncps:Ncps_Cache_Lock",
        "Ncps_Cache_Lock_Retry": "pynix_os.services.ncps:Ncps_Cache_Lock_Retry",
        "Ncps_Cache_Lru": "pynix_os.services.ncps:Ncps_Cache_Lru",
        "Ncps_Cache_Redis": "pynix_os.services.ncps:Ncps_Cache_Redis",
        "Ncps_Cache_Storage": "pynix_os.services.ncps:Ncps_Cache_Storage",
        "Ncps_Cache_Storage_S3": "pynix_os.services.ncps:Ncps_Cache_Storage_S3",
        "Ncps_Cache_Upstream": "pynix_os.services.ncps:Ncps_Cache_Upstream",
        "Ncps_OpenTelemetry": "pynix_os.services.ncps:Ncps_OpenTelemetry",
        "Ncps_Prometheus": "pynix_os.services.ncps:Ncps_Prometheus",
        "Ncps_Server": "pynix_os.services.ncps:Ncps_Server",
        "Ndppd": "pynix_os.services.ndppd:Ndppd",
        "Ndppd_Proxies_Value": "pynix_os.services.ndppd:Ndppd_Proxies_Value",
        "Ndppd_Proxies_Value_Rules_Value": "pynix_os.services.ndppd:Ndppd_Proxies_Value_Rules_Value",
        "Neard": "pynix_os.services.neard:Neard",
        "Neard_Settings": "pynix_os.services.neard:Neard_Settings",
        "Nebula": "pynix_os.services.nebula:Nebula",
        "NebulaLighthouseService": "pynix_os.services.nebula_lighthouse_service:NebulaLighthouseService",
        "Nebula_Networks_Value": "pynix_os.services.nebula:Nebula_Networks_Value",
        "Neo4j": "pynix_os.services.neo4j:Neo4j",
        "Neo4j_Bolt": "pynix_os.services.neo4j:Neo4j_Bolt",
        "Neo4j_Directories": "pynix_os.services.neo4j:Neo4j_Directories",
        "Neo4j_Http": "pynix_os.services.neo4j:Neo4j_Http",
        "Neo4j_Https": "pynix_os.services.neo4j:Neo4j_Https",
        "Neo4j_Shell": "pynix_os.services.neo4j:Neo4j_Shell",
        "Neo4j_Ssl": "pynix_os.services.neo4j:Neo4j_Ssl",
        "Neo4j_Ssl_Policies_Value": "pynix_os.services.neo4j:Neo4j_Ssl_Policies_Value",
        "Neovim": "pynix_os.programs.neovim:Neovim",
        "Neovim_Runtime_Value": "pynix_os.programs.neovim:Neovim_Runtime_Value",
        "Netatalk": "pynix_os.services.netatalk:Netatalk",
        "Netbird": "pynix_os.services.netbird:Netbird",
        "Netbird_Clients_Value": "pynix_os.services.netbird:Netbird_Clients_Value",
        "Netbird_Relay": "pynix_os.services.netbird:Netbird_Relay",
        "Netbird_Relay_Settings": "pynix_os.services.netbird:Netbird_Relay_Settings",
        "Netbird_Server": "pynix_os.services.netbird:Netbird_Server",
        "Netbird_Server_Coturn": "pynix_os.services.netbird:Netbird_Server_Coturn",
        "Netbird_Server_Dashboard": "pynix_os.services.netbird:Netbird_Server_Dashboard",
        "Netbird_Server_Dashboard_Settings": "pynix_os.services.netbird:Netbird_Server_Dashboard_Settings",
        "Netbird_Server_Management": "pynix_os.services.netbird:Netbird_Server_Management",
        "Netbird_Server_Signal": "pynix_os.services.netbird:Netbird_Server_Signal",
        "Netbird_Tunnels_Value": "pynix_os.services.netbird:Netbird_Tunnels_Value",
        "Netbird_Ui": "pynix_os.services.netbird:Netbird_Ui",
        "Netbox": "pynix_os.services.netbox:Netbox",
        "Netbox_Gunicorn": "pynix_os.services.netbox:Netbox_Gunicorn",
        "Netbox_Nginx": "pynix_os.services.netbox:Netbox_Nginx",
        "Netbox_Postgresql": "pynix_os.services.netbox:Netbox_Postgresql",
        "Netbox_Redis": "pynix_os.services.netbox:Netbox_Redis",
        "Netbox_Settings": "pynix_os.services.netbox:Netbox_Settings",
        "Netclient": "pynix_os.services.netclient:Netclient",
        "Netdata": "pynix_os.services.netdata:Netdata",
        "Netdata_Python": "pynix_os.services.netdata:Netdata_Python",
        "Netfoil": "pynix_os.services.netfoil:Netfoil",
        "Netfoil_Listen": "pynix_os.services.netfoil:Netfoil_Listen",
        "Netfoil_Rules": "pynix_os.services.netfoil:Netfoil_Rules",
        "Netfoil_Rules_Allow": "pynix_os.services.netfoil:Netfoil_Rules_Allow",
        "Netfoil_Rules_Deny": "pynix_os.services.netfoil:Netfoil_Rules_Deny",
        "Netfoil_Rules_Known": "pynix_os.services.netfoil:Netfoil_Rules_Known",
        "Netfoil_Rules_Pin": "pynix_os.services.netfoil:Netfoil_Rules_Pin",
        "Nethoscope": "pynix_os.programs.nethoscope:Nethoscope",
        "Netplan": "pynix_os.networking.netplan:Netplan",
        "Network": "pynix_os.systemd.network:Network",
        "Network_Config": "pynix_os.systemd.network:Network_Config",
        "Network_Links_Value": "pynix_os.systemd.network:Network_Links_Value",
        "Network_Netdevs_Value": "pynix_os.systemd.network:Network_Netdevs_Value",
        "Network_Networks_Value": "pynix_os.systemd.network:Network_Networks_Value",
        "Network_Units_Value": "pynix_os.systemd.network:Network_Units_Value",
        "Network_WaitOnline": "pynix_os.systemd.network:Network_WaitOnline",
        "Networkaudiod": "pynix_os.services.networkaudiod:Networkaudiod",
        "NetworkdDispatcher": "pynix_os.services.networkd_dispatcher:NetworkdDispatcher",
        "NetworkdDispatcher_Rules_Value": "pynix_os.services.networkd_dispatcher:NetworkdDispatcher_Rules_Value",
        "Networking": "pynix_os.networking.__options__:Networking",
        "Services_Networking": "pynix_os.services.networking:Networking",
        "Networking_Bonds_Value": "pynix_os.networking.__options__:Networking_Bonds_Value",
        "Networking_Bridges_Value": "pynix_os.networking.__options__:Networking_Bridges_Value",
        "Networking_DefaultGateway": "pynix_os.networking.__options__:Networking_DefaultGateway",
        "Networking_FooOverUDP_Value": "pynix_os.networking.__options__:Networking_FooOverUDP_Value",
        "Networking_FooOverUDP_Value_Local": "pynix_os.networking.__options__:Networking_FooOverUDP_Value_Local",
        "Networking_GreTunnels_Value": "pynix_os.networking.__options__:Networking_GreTunnels_Value",
        "Networking_Interfaces_Value": "pynix_os.networking.__options__:Networking_Interfaces_Value",
        "Networking_Interfaces_Value_Ipv4Addresses_Item": "pynix_os.networking.__options__:Networking_Interfaces_Value_Ipv4Addresses_Item",
        "Networking_Interfaces_Value_Ipv4Routes_Item": "pynix_os.networking.__options__:Networking_Interfaces_Value_Ipv4Routes_Item",
        "Networking_Interfaces_Value_Ipv6Addresses_Item": "pynix_os.networking.__options__:Networking_Interfaces_Value_Ipv6Addresses_Item",
        "Networking_Interfaces_Value_Ipv6Routes_Item": "pynix_os.networking.__options__:Networking_Interfaces_Value_Ipv6Routes_Item",
        "Networking_Ipips_Value": "pynix_os.networking.__options__:Networking_Ipips_Value",
        "Networking_Ipvlans_Value": "pynix_os.networking.__options__:Networking_Ipvlans_Value",
        "Networking_Macvlans_Value": "pynix_os.networking.__options__:Networking_Macvlans_Value",
        "Networking_Sits_Value": "pynix_os.networking.__options__:Networking_Sits_Value",
        "Networking_Sits_Value_Encapsulation": "pynix_os.networking.__options__:Networking_Sits_Value_Encapsulation",
        "Networking_Supplicant_Value": "pynix_os.networking.__options__:Networking_Supplicant_Value",
        "Networking_Vlans_Value": "pynix_os.networking.__options__:Networking_Vlans_Value",
        "Networking_Vswitches_Value": "pynix_os.networking.__options__:Networking_Vswitches_Value",
        "Networking_Vswitches_Value_Interfaces_Value": "pynix_os.networking.__options__:Networking_Vswitches_Value_Interfaces_Value",
        "Networking_Websockify": "pynix_os.services.networking:Networking_Websockify",
        "Networking_WlanInterfaces_Value": "pynix_os.networking.__options__:Networking_WlanInterfaces_Value",
        "Networkmanager": "pynix_os.networking.networkmanager:Networkmanager",
        "Networkmanager_DispatcherScripts_Item": "pynix_os.networking.networkmanager:Networkmanager_DispatcherScripts_Item",
        "Networkmanager_EnsureProfiles": "pynix_os.networking.networkmanager:Networkmanager_EnsureProfiles",
        "Networkmanager_EnsureProfiles_Profiles_Value": "pynix_os.networking.networkmanager:Networkmanager_EnsureProfiles_Profiles_Value",
        "Networkmanager_EnsureProfiles_Secrets": "pynix_os.networking.networkmanager:Networkmanager_EnsureProfiles_Secrets",
        "Networkmanager_EnsureProfiles_Secrets_Entries_Item": "pynix_os.networking.networkmanager:Networkmanager_EnsureProfiles_Secrets_Entries_Item",
        "Networkmanager_Ethernet": "pynix_os.networking.networkmanager:Networkmanager_Ethernet",
        "Networkmanager_Wifi": "pynix_os.networking.networkmanager:Networkmanager_Wifi",
        "NewLg4ff": "pynix_os.hardware.new_lg4ff:NewLg4ff",
        "Newt": "pynix_os.services.newt:Newt",
        "Nextcloud": "pynix_os.services.nextcloud:Nextcloud",
        "NextcloudSpreedSignaling": "pynix_os.services.nextcloud_spreed_signaling:NextcloudSpreedSignaling",
        "NextcloudSpreedSignaling_Backends_Value": "pynix_os.services.nextcloud_spreed_signaling:NextcloudSpreedSignaling_Backends_Value",
        "NextcloudSpreedSignaling_Settings": "pynix_os.services.nextcloud_spreed_signaling:NextcloudSpreedSignaling_Settings",
        "NextcloudWhiteboardServer": "pynix_os.services.nextcloud_whiteboard_server:NextcloudWhiteboardServer",
        "Nextcloud_AutoUpdateApps": "pynix_os.services.nextcloud:Nextcloud_AutoUpdateApps",
        "Nextcloud_Caching": "pynix_os.services.nextcloud:Nextcloud_Caching",
        "Nextcloud_Cli": "pynix_os.services.nextcloud:Nextcloud_Cli",
        "Nextcloud_Config": "pynix_os.services.nextcloud:Nextcloud_Config",
        "Nextcloud_Config_Objectstore": "pynix_os.services.nextcloud:Nextcloud_Config_Objectstore",
        "Nextcloud_Config_Objectstore_S3": "pynix_os.services.nextcloud:Nextcloud_Config_Objectstore_S3",
        "Nextcloud_Database": "pynix_os.services.nextcloud:Nextcloud_Database",
        "Nextcloud_Imaginary": "pynix_os.services.nextcloud:Nextcloud_Imaginary",
        "Nextcloud_Nginx": "pynix_os.services.nextcloud:Nextcloud_Nginx",
        "Nextcloud_NotifyPush": "pynix_os.services.nextcloud:Nextcloud_NotifyPush",
        "Nextcloud_Settings": "pynix_os.services.nextcloud:Nextcloud_Settings",
        "Nextdns": "pynix_os.services.nextdns:Nextdns",
        "NextjsOllamaLlmUi": "pynix_os.services.nextjs_ollama_llm_ui:NextjsOllamaLlmUi",
        "Nexttrace": "pynix_os.programs.nexttrace:Nexttrace",
        "Nexus": "pynix_os.services.nexus:Nexus",
        "Nezha": "pynix_os.services.nezha:Nezha",
        "NezhaAgent": "pynix_os.services.nezha_agent:NezhaAgent",
        "NezhaAgent_Settings": "pynix_os.services.nezha_agent:NezhaAgent_Settings",
        "Nezha_Settings": "pynix_os.services.nezha:Nezha_Settings",
        "NfcNci": "pynix_os.hardware.nfc_nci:NfcNci",
        "Nfs": "pynix_os.services.nfs:Nfs",
        "Nfs_Idmapd": "pynix_os.services.nfs:Nfs_Idmapd",
        "Nfs_Server": "pynix_os.services.nfs:Nfs_Server",
        "Nftables": "pynix_os.networking.nftables:Nftables",
        "Nftables_Tables_Value": "pynix_os.networking.nftables:Nftables_Tables_Value",
        "Nghttpx": "pynix_os.services.nghttpx:Nghttpx",
        "Nghttpx_Backends_Item": "pynix_os.services.nghttpx:Nghttpx_Backends_Item",
        "Nghttpx_Backends_Item_Params": "pynix_os.services.nghttpx:Nghttpx_Backends_Item_Params",
        "Nghttpx_Backends_Item_Server": "pynix_os.services.nghttpx:Nghttpx_Backends_Item_Server",
        "Nghttpx_Frontends_Item": "pynix_os.services.nghttpx:Nghttpx_Frontends_Item",
        "Nghttpx_Frontends_Item_Params": "pynix_os.services.nghttpx:Nghttpx_Frontends_Item_Params",
        "Nghttpx_Tls": "pynix_os.services.nghttpx:Nghttpx_Tls",
        "Nginx": "pynix_os.services.nginx:Nginx",
        "Nginx_DefaultListen_Item": "pynix_os.services.nginx:Nginx_DefaultListen_Item",
        "Nginx_Lua": "pynix_os.services.nginx:Nginx_Lua",
        "Nginx_ProxyCachePath_Value": "pynix_os.services.nginx:Nginx_ProxyCachePath_Value",
        "Nginx_Resolver": "pynix_os.services.nginx:Nginx_Resolver",
        "Nginx_Sso": "pynix_os.services.nginx:Nginx_Sso",
        "Nginx_TailscaleAuth": "pynix_os.services.nginx:Nginx_TailscaleAuth",
        "Nginx_Upstreams_Value": "pynix_os.services.nginx:Nginx_Upstreams_Value",
        "Nginx_Upstreams_Value_Servers_Value": "pynix_os.services.nginx:Nginx_Upstreams_Value_Servers_Value",
        "Nginx_VirtualHosts_Value": "pynix_os.services.nginx:Nginx_VirtualHosts_Value",
        "Nginx_VirtualHosts_Value_Listen_Item": "pynix_os.services.nginx:Nginx_VirtualHosts_Value_Listen_Item",
        "Nginx_VirtualHosts_Value_Locations_Value": "pynix_os.services.nginx:Nginx_VirtualHosts_Value_Locations_Value",
        "Ngircd": "pynix_os.services.ngircd:Ngircd",
        "Nh": "pynix_os.programs.nh:Nh",
        "Nh_Clean": "pynix_os.programs.nh:Nh_Clean",
        "Nifi": "pynix_os.services.nifi:Nifi",
        "Nipap": "pynix_os.services.nipap:Nipap",
        "Nipap_AuthBackendSettings": "pynix_os.services.nipap:Nipap_AuthBackendSettings",
        "Nipap_NipapWww": "pynix_os.services.nipap:Nipap_NipapWww",
        "Nipap_Nipapd": "pynix_os.services.nipap:Nipap_Nipapd",
        "Nipap_Nipapd_Database": "pynix_os.services.nipap:Nipap_Nipapd_Database",
        "Nipap_Settings": "pynix_os.services.nipap:Nipap_Settings",
        "Niri": "pynix_os.programs.niri:Niri",
        "Nitrokey": "pynix_os.hardware.nitrokey:Nitrokey",
        "Nitter": "pynix_os.services.nitter:Nitter",
        "Nitter_Cache": "pynix_os.services.nitter:Nitter_Cache",
        "Nitter_Config": "pynix_os.services.nitter:Nitter_Config",
        "Nitter_Preferences": "pynix_os.services.nitter:Nitter_Preferences",
        "Nitter_Server": "pynix_os.services.nitter:Nitter_Server",
        "Nix": "pynix_os.nix.__options__:Nix",
        "NixIndex": "pynix_os.programs.nix_index:NixIndex",
        "NixLd": "pynix_os.programs.nix_ld:NixLd",
        "NixRequiredMounts": "pynix_os.programs.nix_required_mounts:NixRequiredMounts",
        "NixRequiredMounts_AllowedPatterns_Value": "pynix_os.programs.nix_required_mounts:NixRequiredMounts_AllowedPatterns_Value",
        "NixRequiredMounts_AllowedPatterns_Value_Paths_Item_Or": "pynix_os.programs.nix_required_mounts:NixRequiredMounts_AllowedPatterns_Value_Paths_Item_Or",
        "NixRequiredMounts_Presets": "pynix_os.programs.nix_required_mounts:NixRequiredMounts_Presets",
        "NixRequiredMounts_Presets_NvidiaGpu": "pynix_os.programs.nix_required_mounts:NixRequiredMounts_Presets_NvidiaGpu",
        "NixRequiredMounts_Presets_Zluda": "pynix_os.programs.nix_required_mounts:NixRequiredMounts_Presets_Zluda",
        "NixServe": "pynix_os.services.nix_serve:NixServe",
        "Nix_BuildMachines_Item": "pynix_os.nix.__options__:Nix_BuildMachines_Item",
        "Nix_Registry_Value": "pynix_os.nix.__options__:Nix_Registry_Value",
        "Nix_Settings": "pynix_os.nix.__options__:Nix_Settings",
        "Nixbit": "pynix_os.programs.nixbit:Nixbit",
        "Nixops": "pynix_os.nixops.__options__:Nixops",
        "NixopsDns": "pynix_os.services.nixops_dns:NixopsDns",
        "Documentation_Nixos": "pynix_os.documentation.nixos:Nixos",
        "System_Nixos": "pynix_os.system.nixos:Nixos",
        "NixosGenerateConfig": "pynix_os.system.nixos_generate_config:NixosGenerateConfig",
        "NixosInit": "pynix_os.system.nixos_init:NixosInit",
        "Nixos_Options": "pynix_os.documentation.nixos:Nixos_Options",
        "Nixpkgs": "pynix_os.nixpkgs.__options__:Nixpkgs",
        "Nixseparatedebuginfod2": "pynix_os.services.nixseparatedebuginfod2:Nixseparatedebuginfod2",
        "NmApplet": "pynix_os.programs.nm_applet:NmApplet",
        "Nmtrust": "pynix_os.services.nmtrust:Nmtrust",
        "Nmtrust_SystemUnits_Value": "pynix_os.services.nmtrust:Nmtrust_SystemUnits_Value",
        "Nmtrust_UserUnits_Value_Value": "pynix_os.services.nmtrust:Nmtrust_UserUnits_Value_Value",
        "Programs_Nncp": "pynix_os.programs.nncp:Nncp",
        "Services_Nncp": "pynix_os.services.nncp:Nncp",
        "Nncp_Caller": "pynix_os.services.nncp:Nncp_Caller",
        "Nncp_Daemon": "pynix_os.services.nncp:Nncp_Daemon",
        "Nncp_Daemon_SocketActivation": "pynix_os.services.nncp:Nncp_Daemon_SocketActivation",
        "NntpProxy": "pynix_os.services.nntp_proxy:NntpProxy",
        "NntpProxy_Users_Value": "pynix_os.services.nntp_proxy:NntpProxy_Users_Value",
        "Noctalia": "pynix_os.programs.noctalia:Noctalia",
        "Noctalia_RecommendedServices": "pynix_os.programs.noctalia:Noctalia_RecommendedServices",
        "Noctalia_Systemd": "pynix_os.programs.noctalia:Noctalia_Systemd",
        "NodeRed": "pynix_os.services.node_red:NodeRed",
        "Nohang": "pynix_os.services.nohang:Nohang",
        "Noisetorch": "pynix_os.programs.noisetorch:Noisetorch",
        "Nomad": "pynix_os.services.nomad:Nomad",
        "Nominatim": "pynix_os.services.nominatim:Nominatim",
        "Nominatim_Database": "pynix_os.services.nominatim:Nominatim_Database",
        "Nominatim_Ui": "pynix_os.services.nominatim:Nominatim_Ui",
        "Nordvpn": "pynix_os.services.nordvpn:Nordvpn",
        "NostrRsRelay": "pynix_os.services.nostr_rs_relay:NostrRsRelay",
        "Novacomd": "pynix_os.services.novacomd:Novacomd",
        "Npm": "pynix_os.programs.npm:Npm",
        "NsUsbloader": "pynix_os.programs.ns_usbloader:NsUsbloader",
        "Nscd": "pynix_os.services.nscd:Nscd",
        "Nsd": "pynix_os.services.nsd:Nsd",
        "Nsd_Keys_Value": "pynix_os.services.nsd:Nsd_Keys_Value",
        "Nsd_Ratelimit": "pynix_os.services.nsd:Nsd_Ratelimit",
        "Nsd_RemoteControl": "pynix_os.services.nsd:Nsd_RemoteControl",
        "Nsd_Zones_Value": "pynix_os.services.nsd:Nsd_Zones_Value",
        "Nsd_Zones_Value_DnssecPolicyKsk": "pynix_os.services.nsd:Nsd_Zones_Value_DnssecPolicyKsk",
        "NssDatabases": "pynix_os.system.nssDatabases:NssDatabases",
        "NtfySh": "pynix_os.services.ntfy_sh:NtfySh",
        "NtfySh_Nginx": "pynix_os.services.ntfy_sh:NtfySh_Nginx",
        "NtfySh_Settings": "pynix_os.services.ntfy_sh:NtfySh_Settings",
        "Ntopng": "pynix_os.services.ntopng:Ntopng",
        "Ntopng_Redis": "pynix_os.services.ntopng:Ntopng_Redis",
        "Ntp": "pynix_os.services.ntp:Ntp",
        "NtpdRs": "pynix_os.services.ntpd_rs:NtpdRs",
        "NtpdRs_Metrics": "pynix_os.services.ntpd_rs:NtpdRs_Metrics",
        "NtpdRs_Settings": "pynix_os.services.ntpd_rs:NtpdRs_Settings",
        "Nullidentdmod": "pynix_os.services.nullidentdmod:Nullidentdmod",
        "Nullmailer": "pynix_os.services.nullmailer:Nullmailer",
        "Nullmailer_Config": "pynix_os.services.nullmailer:Nullmailer_Config",
        "Nushell": "pynix_os.programs.nushell:Nushell",
        "Nvidia": "pynix_os.hardware.nvidia:Nvidia",
        "NvidiaContainerToolkit": "pynix_os.hardware.nvidia_container_toolkit:NvidiaContainerToolkit",
        "NvidiaContainerToolkit_Mounts_Item": "pynix_os.hardware.nvidia_container_toolkit:NvidiaContainerToolkit_Mounts_Item",
        "NvidiaOptimus": "pynix_os.hardware.nvidiaOptimus:NvidiaOptimus",
        "Nvidia_Datacenter": "pynix_os.hardware.nvidia:Nvidia_Datacenter",
        "Nvidia_DynamicBoost": "pynix_os.hardware.nvidia:Nvidia_DynamicBoost",
        "Nvidia_Gsp": "pynix_os.hardware.nvidia:Nvidia_Gsp",
        "Nvidia_Modesetting": "pynix_os.hardware.nvidia:Nvidia_Modesetting",
        "Nvidia_PowerManagement": "pynix_os.hardware.nvidia:Nvidia_PowerManagement",
        "Nvidia_Prime": "pynix_os.hardware.nvidia:Nvidia_Prime",
        "Nvidia_Prime_Offload": "pynix_os.hardware.nvidia:Nvidia_Prime_Offload",
        "Nvidia_Prime_ReverseSync": "pynix_os.hardware.nvidia:Nvidia_Prime_ReverseSync",
        "Nvidia_Prime_ReverseSync_SetupCommands": "pynix_os.hardware.nvidia:Nvidia_Prime_ReverseSync_SetupCommands",
        "Nvidia_Prime_Sync": "pynix_os.hardware.nvidia:Nvidia_Prime_Sync",
        "NvmeRs": "pynix_os.services.nvme_rs:NvmeRs",
        "NvmeRs_Settings": "pynix_os.services.nvme_rs:NvmeRs_Settings",
        "NvmeRs_Settings_Email": "pynix_os.services.nvme_rs:NvmeRs_Settings_Email",
        "NvmeRs_Settings_Thresholds": "pynix_os.services.nvme_rs:NvmeRs_Settings_Thresholds",
        "Nvrs": "pynix_os.programs.nvrs:Nvrs",
        "Nvrs_Settings": "pynix_os.programs.nvrs:Nvrs_Settings",
        "Nxdumpclient": "pynix_os.programs.nxdumpclient:Nxdumpclient",
        "Nzbget": "pynix_os.services.nzbget:Nzbget",
        "Nzbhydra2": "pynix_os.services.nzbhydra2:Nzbhydra2",
        "Oauth2Proxy": "pynix_os.services.oauth2_proxy:Oauth2Proxy",
        "Oauth2Proxy_Azure": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Azure",
        "Oauth2Proxy_Cookie": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Cookie",
        "Oauth2Proxy_Email": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Email",
        "Oauth2Proxy_Github": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Github",
        "Oauth2Proxy_Google": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Google",
        "Oauth2Proxy_Htpasswd": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Htpasswd",
        "Oauth2Proxy_Nginx": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Nginx",
        "Oauth2Proxy_Nginx_VirtualHosts_Value": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Nginx_VirtualHosts_Value",
        "Oauth2Proxy_Tls": "pynix_os.services.oauth2_proxy:Oauth2Proxy_Tls",
        "ObsStudio": "pynix_os.programs.obs_studio:ObsStudio",
        "Oci": "pynix_os.oci.__options__:Oci",
        "OciContainers": "pynix_os.virtualisation.oci_containers:OciContainers",
        "OciContainers_Containers_Value": "pynix_os.virtualisation.oci_containers:OciContainers_Containers_Value",
        "OciContainers_Containers_Value_Podman": "pynix_os.virtualisation.oci_containers:OciContainers_Containers_Value_Podman",
        "Ocis": "pynix_os.services.ocis:Ocis",
        "Ocserv": "pynix_os.services.ocserv:Ocserv",
        "OcsinventoryAgent": "pynix_os.services.ocsinventory_agent:OcsinventoryAgent",
        "OcsinventoryAgent_Settings": "pynix_os.services.ocsinventory_agent:OcsinventoryAgent_Settings",
        "Octoprint": "pynix_os.services.octoprint:Octoprint",
        "Oddjobd": "pynix_os.programs.oddjobd:Oddjobd",
        "Odoo": "pynix_os.services.odoo:Odoo",
        "Odoo_Settings": "pynix_os.services.odoo:Odoo_Settings",
        "Offlineimap": "pynix_os.services.offlineimap:Offlineimap",
        "Ofono": "pynix_os.services.ofono:Ofono",
        "Oidentd": "pynix_os.services.oidentd:Oidentd",
        "Oink": "pynix_os.services.oink:Oink",
        "Oink_Settings": "pynix_os.services.oink:Oink_Settings",
        "Olivetin": "pynix_os.services.olivetin:Olivetin",
        "Olivetin_Settings": "pynix_os.services.olivetin:Olivetin_Settings",
        "Ollama": "pynix_os.services.ollama:Ollama",
        "Ollaya": "pynix_os.services.ollaya:Ollaya",
        "Ollaya_Settings": "pynix_os.services.ollaya:Ollaya_Settings",
        "Omada": "pynix_os.services.omada:Omada",
        "Ombi": "pynix_os.services.ombi:Ombi",
        "Omnom": "pynix_os.services.omnom:Omnom",
        "Omnom_Settings": "pynix_os.services.omnom:Omnom_Settings",
        "Oncall": "pynix_os.services.oncall:Oncall",
        "Oncall_Database": "pynix_os.services.oncall:Oncall_Database",
        "Oncall_Settings": "pynix_os.services.oncall:Oncall_Settings",
        "Onedrive": "pynix_os.services.onedrive:Onedrive",
        "Onlykey": "pynix_os.hardware.onlykey:Onlykey",
        "Onlyoffice": "pynix_os.services.onlyoffice:Onlyoffice",
        "Oo7": "pynix_os.services.oo7:Oo7",
        "Oomd": "pynix_os.systemd.oomd:Oomd",
        "Oomd_Settings": "pynix_os.systemd.oomd:Oomd_Settings",
        "Oomd_Settings_OOM": "pynix_os.systemd.oomd:Oomd_Settings_OOM",
        "OpenWebCalendar": "pynix_os.services.open_web_calendar:OpenWebCalendar",
        "OpenWebCalendar_CalendarSettings": "pynix_os.services.open_web_calendar:OpenWebCalendar_CalendarSettings",
        "OpenWebCalendar_Settings": "pynix_os.services.open_web_calendar:OpenWebCalendar_Settings",
        "OpenWebui": "pynix_os.services.open_webui:OpenWebui",
        "OpenafsClient": "pynix_os.services.openafsClient:OpenafsClient",
        "OpenafsClient_Cache": "pynix_os.services.openafsClient:OpenafsClient_Cache",
        "OpenafsClient_CellServDB_Value_Item": "pynix_os.services.openafsClient:OpenafsClient_CellServDB_Value_Item",
        "OpenafsClient_Packages": "pynix_os.services.openafsClient:OpenafsClient_Packages",
        "OpenafsServer": "pynix_os.services.openafsServer:OpenafsServer",
        "OpenafsServer_CellServDB_Value_Item": "pynix_os.services.openafsServer:OpenafsServer_CellServDB_Value_Item",
        "OpenafsServer_Roles": "pynix_os.services.openafsServer:OpenafsServer_Roles",
        "OpenafsServer_Roles_Backup": "pynix_os.services.openafsServer:OpenafsServer_Roles_Backup",
        "OpenafsServer_Roles_Database": "pynix_os.services.openafsServer:OpenafsServer_Roles_Database",
        "OpenafsServer_Roles_Fileserver": "pynix_os.services.openafsServer:OpenafsServer_Roles_Fileserver",
        "Openarena": "pynix_os.services.openarena:Openarena",
        "Openbao": "pynix_os.services.openbao:Openbao",
        "OpenbaoAgent": "pynix_os.services.openbao_agent:OpenbaoAgent",
        "OpenbaoAgent_Instances_Value": "pynix_os.services.openbao_agent:OpenbaoAgent_Instances_Value",
        "OpenbaoAgent_Instances_Value_Settings": "pynix_os.services.openbao_agent:OpenbaoAgent_Instances_Value_Settings",
        "Openbao_Settings": "pynix_os.services.openbao:Openbao_Settings",
        "Openbao_Settings_Listener_Value": "pynix_os.services.openbao:Openbao_Settings_Listener_Value",
        "Opencloud": "pynix_os.services.opencloud:Opencloud",
        "Openconnect": "pynix_os.networking.openconnect:Openconnect",
        "Openconnect_Interfaces_Value": "pynix_os.networking.openconnect:Openconnect_Interfaces_Value",
        "Opendkim": "pynix_os.services.opendkim:Opendkim",
        "Opendkim_Settings": "pynix_os.services.opendkim:Opendkim_Settings",
        "Opengamepadui": "pynix_os.programs.opengamepadui:Opengamepadui",
        "Opengamepadui_GamescopeSession": "pynix_os.programs.opengamepadui:Opengamepadui_GamescopeSession",
        "Opengamepadui_Inputplumber": "pynix_os.programs.opengamepadui:Opengamepadui_Inputplumber",
        "Opengamepadui_Powerstation": "pynix_os.programs.opengamepadui:Opengamepadui_Powerstation",
        "Openiscsi": "pynix_os.services.openiscsi:Openiscsi",
        "Openldap": "pynix_os.services.openldap:Openldap",
        "Openldap_Settings": "pynix_os.services.openldap:Openldap_Settings",
        "Openldap_Settings_Children_Value": "pynix_os.services.openldap:Openldap_Settings_Children_Value",
        "Openntpd": "pynix_os.services.openntpd:Openntpd",
        "Openrazer": "pynix_os.hardware.openrazer:Openrazer",
        "Openrazer_BatteryNotifier": "pynix_os.hardware.openrazer:Openrazer_BatteryNotifier",
        "Openrazer_Packages": "pynix_os.hardware.openrazer:Openrazer_Packages",
        "Opensearch": "pynix_os.services.opensearch:Opensearch",
        "OpensearchDashboards": "pynix_os.services.opensearch_dashboards:OpensearchDashboards",
        "OpensearchDashboards_Settings": "pynix_os.services.opensearch_dashboards:OpensearchDashboards_Settings",
        "Opensearch_Settings": "pynix_os.services.opensearch:Opensearch_Settings",
        "Opensmtpd": "pynix_os.services.opensmtpd:Opensmtpd",
        "Opensnitch": "pynix_os.services.opensnitch:Opensnitch",
        "Opensnitch_Rules": "pynix_os.services.opensnitch:Opensnitch_Rules",
        "Opensnitch_Settings": "pynix_os.services.opensnitch:Opensnitch_Settings",
        "Openssh": "pynix_os.services.openssh:Openssh",
        "Openssh_KnownHosts_Value": "pynix_os.services.openssh:Openssh_KnownHosts_Value",
        "Openssh_ListenAddresses_Item": "pynix_os.services.openssh:Openssh_ListenAddresses_Item",
        "Openssh_Settings": "pynix_os.services.openssh:Openssh_Settings",
        "Openstack": "pynix_os.openstack.__options__:Openstack",
        "Opentabletdriver": "pynix_os.hardware.opentabletdriver:Opentabletdriver",
        "Opentabletdriver_Daemon": "pynix_os.hardware.opentabletdriver:Opentabletdriver_Daemon",
        "OpentelemetryCollector": "pynix_os.services.opentelemetry_collector:OpentelemetryCollector",
        "OpenthreadBorderRouter": "pynix_os.services.openthread_border_router:OpenthreadBorderRouter",
        "OpenthreadBorderRouter_Radio": "pynix_os.services.openthread_border_router:OpenthreadBorderRouter_Radio",
        "OpenthreadBorderRouter_Rest": "pynix_os.services.openthread_border_router:OpenthreadBorderRouter_Rest",
        "OpenthreadBorderRouter_Web": "pynix_os.services.openthread_border_router:OpenthreadBorderRouter_Web",
        "Opentracker": "pynix_os.services.opentracker:Opentracker",
        "Opentsdb": "pynix_os.services.opentsdb:Opentsdb",
        "Openvpn": "pynix_os.services.openvpn:Openvpn",
        "Openvpn3": "pynix_os.programs.openvpn3:Openvpn3",
        "Openvpn3_LogService": "pynix_os.programs.openvpn3:Openvpn3_LogService",
        "Openvpn3_LogService_Settings": "pynix_os.programs.openvpn3:Openvpn3_LogService_Settings",
        "Openvpn3_Netcfg": "pynix_os.programs.openvpn3:Openvpn3_Netcfg",
        "Openvpn3_Netcfg_Settings": "pynix_os.programs.openvpn3:Openvpn3_Netcfg_Settings",
        "Openvpn_Servers_Value": "pynix_os.services.openvpn:Openvpn_Servers_Value",
        "Openvpn_Servers_Value_AuthUserPass_Or": "pynix_os.services.openvpn:Openvpn_Servers_Value_AuthUserPass_Or",
        "OpenvscodeServer": "pynix_os.services.openvscode_server:OpenvscodeServer",
        "Openwebrx": "pynix_os.services.openwebrx:Openwebrx",
        "Opkssh": "pynix_os.services.opkssh:Opkssh",
        "Opkssh_Authorizations_Item": "pynix_os.services.opkssh:Opkssh_Authorizations_Item",
        "Opkssh_Providers_Value": "pynix_os.services.opkssh:Opkssh_Providers_Value",
        "Optimise": "pynix_os.nix.optimise:Optimise",
        "Orangefs": "pynix_os.services.orangefs:Orangefs",
        "Orangefs_Client": "pynix_os.services.orangefs:Orangefs_Client",
        "Orangefs_Client_FileSystems_Item": "pynix_os.services.orangefs:Orangefs_Client_FileSystems_Item",
        "Orangefs_Server": "pynix_os.services.orangefs:Orangefs_Server",
        "Orangefs_Server_FileSystems_Value": "pynix_os.services.orangefs:Orangefs_Server_FileSystems_Value",
        "Orbit": "pynix_os.services.orbit:Orbit",
        "Orbit_Desktop": "pynix_os.services.orbit:Orbit_Desktop",
        "Orca": "pynix_os.services.orca:Orca",
        "Orthanc": "pynix_os.services.orthanc:Orthanc",
        "Orthanc_Settings": "pynix_os.services.orthanc:Orthanc_Settings",
        "Osquery": "pynix_os.services.osquery:Osquery",
        "Osquery_Flags": "pynix_os.services.osquery:Osquery_Flags",
        "Osrm": "pynix_os.services.osrm:Osrm",
        "Ostinato": "pynix_os.services.ostinato:Ostinato",
        "Ostinato_PortList": "pynix_os.services.ostinato:Ostinato_PortList",
        "Ostinato_RpcServer": "pynix_os.services.ostinato:Ostinato_RpcServer",
        "Outline": "pynix_os.services.outline:Outline",
        "Outline_AzureAuthentication": "pynix_os.services.outline:Outline_AzureAuthentication",
        "Outline_DiscordAuthentication": "pynix_os.services.outline:Outline_DiscordAuthentication",
        "Outline_GoogleAuthentication": "pynix_os.services.outline:Outline_GoogleAuthentication",
        "Outline_OidcAuthentication": "pynix_os.services.outline:Outline_OidcAuthentication",
        "Outline_RateLimiter": "pynix_os.services.outline:Outline_RateLimiter",
        "Outline_SlackAuthentication": "pynix_os.services.outline:Outline_SlackAuthentication",
        "Outline_SlackIntegration": "pynix_os.services.outline:Outline_SlackIntegration",
        "Outline_Smtp": "pynix_os.services.outline:Outline_Smtp",
        "Outline_Storage": "pynix_os.services.outline:Outline_Storage",
        "Owamp": "pynix_os.services.owamp:Owamp",
        "Owncast": "pynix_os.services.owncast:Owncast",
        "Oxidized": "pynix_os.services.oxidized:Oxidized",
        "P2pool": "pynix_os.services.p2pool:P2pool",
        "P2pool_Socks5": "pynix_os.services.p2pool:P2pool_Socks5",
        "Pacemaker": "pynix_os.services.pacemaker:Pacemaker",
        "Packagekit": "pynix_os.services.packagekit:Packagekit",
        "Pairdrop": "pynix_os.services.pairdrop:Pairdrop",
        "Pairdrop_Environment": "pynix_os.services.pairdrop:Pairdrop_Environment",
        "Paisa": "pynix_os.services.paisa:Paisa",
        "Paisa_Settings": "pynix_os.services.paisa:Paisa_Settings",
        "Pam": "pynix_os.security.pam:Pam",
        "Pam_Dp9ik": "pynix_os.security.pam:Pam_Dp9ik",
        "Pam_Howdy": "pynix_os.security.pam:Pam_Howdy",
        "Pam_Krb5": "pynix_os.security.pam:Pam_Krb5",
        "Pam_LoginLimits_Item": "pynix_os.security.pam:Pam_LoginLimits_Item",
        "Pam_MakeHomeDir": "pynix_os.security.pam:Pam_MakeHomeDir",
        "Pam_Mount": "pynix_os.security.pam:Pam_Mount",
        "Pam_Oath": "pynix_os.security.pam:Pam_Oath",
        "Pam_P11": "pynix_os.security.pam:Pam_P11",
        "Pam_Rssh": "pynix_os.security.pam:Pam_Rssh",
        "Pam_Rssh_Settings": "pynix_os.security.pam:Pam_Rssh_Settings",
        "Pam_Services_Value": "pynix_os.security.pam:Pam_Services_Value",
        "Pam_Services_Value_Rules": "pynix_os.security.pam:Pam_Services_Value_Rules",
        "Pam_Services_Value_Rules_Account_Value": "pynix_os.security.pam:Pam_Services_Value_Rules_Account_Value",
        "Pam_Services_Value_SlurmAdoptSettings": "pynix_os.security.pam:Pam_Services_Value_SlurmAdoptSettings",
        "Pam_SshAgentAuth": "pynix_os.security.pam:Pam_SshAgentAuth",
        "Pam_U2f": "pynix_os.security.pam:Pam_U2f",
        "Pam_U2f_Settings": "pynix_os.security.pam:Pam_U2f_Settings",
        "Pam_Ussh": "pynix_os.security.pam:Pam_Ussh",
        "Pam_Yubico": "pynix_os.security.pam:Pam_Yubico",
        "Pam_Zfs": "pynix_os.security.pam:Pam_Zfs",
        "Pangolin": "pynix_os.services.pangolin:Pangolin",
        "PantalaimonHeadless": "pynix_os.services.pantalaimon_headless:PantalaimonHeadless",
        "PantalaimonHeadless_Instances_Value": "pynix_os.services.pantalaimon_headless:PantalaimonHeadless_Instances_Value",
        "Environment_Pantheon": "pynix_os.environment.pantheon:Pantheon",
        "Services_Pantheon": "pynix_os.services.pantheon:Pantheon",
        "Pantheon_Apps": "pynix_os.services.pantheon:Pantheon_Apps",
        "Pantheon_Contractor": "pynix_os.services.pantheon:Pantheon_Contractor",
        "Pantheon_ParentalControls": "pynix_os.services.pantheon:Pantheon_ParentalControls",
        "Paperless": "pynix_os.services.paperless:Paperless",
        "Paperless_Database": "pynix_os.services.paperless:Paperless_Database",
        "Paperless_Exporter": "pynix_os.services.paperless:Paperless_Exporter",
        "Paperless_Settings": "pynix_os.services.paperless:Paperless_Settings",
        "Papra": "pynix_os.services.papra:Papra",
        "Papra_Environment": "pynix_os.services.papra:Papra_Environment",
        "Parallels": "pynix_os.hardware.parallels:Parallels",
        "Paretosecurity": "pynix_os.services.paretosecurity:Paretosecurity",
        "Paretosecurity_Users_Value": "pynix_os.services.paretosecurity:Paretosecurity_Users_Value",
        "Parsedmarc": "pynix_os.services.parsedmarc:Parsedmarc",
        "Parsedmarc_Provision": "pynix_os.services.parsedmarc:Parsedmarc_Provision",
        "Parsedmarc_Provision_Grafana": "pynix_os.services.parsedmarc:Parsedmarc_Provision_Grafana",
        "Parsedmarc_Provision_LocalMail": "pynix_os.services.parsedmarc:Parsedmarc_Provision_LocalMail",
        "Parsedmarc_Settings": "pynix_os.services.parsedmarc:Parsedmarc_Settings",
        "PartDb": "pynix_os.services.part_db:PartDb",
        "PartDb_Settings": "pynix_os.services.part_db:PartDb_Settings",
        "PartitionManager": "pynix_os.programs.partition_manager:PartitionManager",
        "PassSecretService": "pynix_os.services.passSecretService:PassSecretService",
        "Passless": "pynix_os.programs.passless:Passless",
        "Patroni": "pynix_os.services.patroni:Patroni",
        "PayRespects": "pynix_os.programs.pay_respects:PayRespects",
        "PayRespects_AiIntegration_Or": "pynix_os.programs.pay_respects:PayRespects_AiIntegration_Or",
        "Pcmcia": "pynix_os.hardware.pcmcia:Pcmcia",
        "Pcscd": "pynix_os.services.pcscd:Pcscd",
        "Pdfding": "pynix_os.services.pdfding:Pdfding",
        "Pdfding_Consume": "pynix_os.services.pdfding:Pdfding_Consume",
        "Pdfding_Gunicorn": "pynix_os.services.pdfding:Pdfding_Gunicorn",
        "PdnsRecursor": "pynix_os.services.pdns_recursor:PdnsRecursor",
        "PdnsRecursor_Api": "pynix_os.services.pdns_recursor:PdnsRecursor_Api",
        "PdnsRecursor_Dns": "pynix_os.services.pdns_recursor:PdnsRecursor_Dns",
        "Pdnsd": "pynix_os.services.pdnsd:Pdnsd",
        "Pdudaemon": "pynix_os.services.pdudaemon:Pdudaemon",
        "Peerflix": "pynix_os.services.peerflix:Peerflix",
        "PeeringManager": "pynix_os.services.peering_manager:PeeringManager",
        "PeeringManager_Settings": "pynix_os.services.peering_manager:PeeringManager_Settings",
        "Peertube": "pynix_os.services.peertube:Peertube",
        "PeertubeRunner": "pynix_os.services.peertube_runner:PeertubeRunner",
        "PeertubeRunner_InstancesToRegister_Value": "pynix_os.services.peertube_runner:PeertubeRunner_InstancesToRegister_Value",
        "Peertube_Database": "pynix_os.services.peertube:Peertube_Database",
        "Peertube_Redis": "pynix_os.services.peertube:Peertube_Redis",
        "Peertube_Secrets": "pynix_os.services.peertube:Peertube_Secrets",
        "Peertube_Settings": "pynix_os.services.peertube:Peertube_Settings",
        "Peertube_Smtp": "pynix_os.services.peertube:Peertube_Smtp",
        "Perses": "pynix_os.services.perses:Perses",
        "Perses_Settings": "pynix_os.services.perses:Perses_Settings",
        "PersistentEvdev": "pynix_os.services.persistent_evdev:PersistentEvdev",
        "Pgadmin": "pynix_os.services.pgadmin:Pgadmin",
        "Pgadmin_EmailServer": "pynix_os.services.pgadmin:Pgadmin_EmailServer",
        "Pgbackrest": "pynix_os.services.pgbackrest:Pgbackrest",
        "Pgbackrest_Commands": "pynix_os.services.pgbackrest:Pgbackrest_Commands",
        "Pgbackrest_Commands_Annotate": "pynix_os.services.pgbackrest:Pgbackrest_Commands_Annotate",
        "Pgbackrest_Repos_Value": "pynix_os.services.pgbackrest:Pgbackrest_Repos_Value",
        "Pgbackrest_Settings": "pynix_os.services.pgbackrest:Pgbackrest_Settings",
        "Pgbackrest_Stanzas_Value": "pynix_os.services.pgbackrest:Pgbackrest_Stanzas_Value",
        "Pgbackrest_Stanzas_Value_Instances_Value": "pynix_os.services.pgbackrest:Pgbackrest_Stanzas_Value_Instances_Value",
        "Pgbackrest_Stanzas_Value_Jobs_Value": "pynix_os.services.pgbackrest:Pgbackrest_Stanzas_Value_Jobs_Value",
        "Pgbackrest_Stanzas_Value_Settings": "pynix_os.services.pgbackrest:Pgbackrest_Stanzas_Value_Settings",
        "Pgbouncer": "pynix_os.services.pgbouncer:Pgbouncer",
        "Pgbouncer_Settings": "pynix_os.services.pgbouncer:Pgbouncer_Settings",
        "Pgmanage": "pynix_os.services.pgmanage:Pgmanage",
        "Pgmanage_Tls": "pynix_os.services.pgmanage:Pgmanage_Tls",
        "PgpkeyserverLite": "pynix_os.services.pgpkeyserver_lite:PgpkeyserverLite",
        "Pgscv": "pynix_os.services.pgscv:Pgscv",
        "Photonvision": "pynix_os.services.photonvision:Photonvision",
        "Photoprism": "pynix_os.services.photoprism:Photoprism",
        "Photoview": "pynix_os.services.photoview:Photoview",
        "Photoview_Settings": "pynix_os.services.photoview:Photoview_Settings",
        "Phpfpm": "pynix_os.services.phpfpm:Phpfpm",
        "Phpfpm_Pools_Value": "pynix_os.services.phpfpm:Phpfpm_Pools_Value",
        "Phylactery": "pynix_os.services.phylactery:Phylactery",
        "Physlock": "pynix_os.services.physlock:Physlock",
        "Physlock_LockOn": "pynix_os.services.physlock:Physlock_LockOn",
        "Picom": "pynix_os.services.picom:Picom",
        "Picosnitch": "pynix_os.services.picosnitch:Picosnitch",
        "PictRs": "pynix_os.services.pict_rs:PictRs",
        "PidFanController": "pynix_os.services.pid_fan_controller:PidFanController",
        "PidFanController_Settings": "pynix_os.services.pid_fan_controller:PidFanController_Settings",
        "PiholeFtl": "pynix_os.services.pihole_ftl:PiholeFtl",
        "PiholeFtl_Lists_Item": "pynix_os.services.pihole_ftl:PiholeFtl_Lists_Item",
        "PiholeFtl_QueryLogDeleter": "pynix_os.services.pihole_ftl:PiholeFtl_QueryLogDeleter",
        "PiholeWeb": "pynix_os.services.pihole_web:PiholeWeb",
        "PiholeWeb_Ports_Item_Or": "pynix_os.services.pihole_web:PiholeWeb_Ports_Item_Or",
        "Pinchflat": "pynix_os.services.pinchflat:Pinchflat",
        "Pinnacle": "pynix_os.programs.pinnacle:Pinnacle",
        "Pinnacle_XdgPortals": "pynix_os.programs.pinnacle:Pinnacle_XdgPortals",
        "Pinnwand": "pynix_os.services.pinnwand:Pinnwand",
        "Pinnwand_Settings": "pynix_os.services.pinnwand:Pinnwand_Settings",
        "Pipewire": "pynix_os.services.pipewire:Pipewire",
        "Pipewire_Alsa": "pynix_os.services.pipewire:Pipewire_Alsa",
        "Pipewire_Audio": "pynix_os.services.pipewire:Pipewire_Audio",
        "Pipewire_ExtraConfig": "pynix_os.services.pipewire:Pipewire_ExtraConfig",
        "Pipewire_Jack": "pynix_os.services.pipewire:Pipewire_Jack",
        "Pipewire_Pulse": "pynix_os.services.pipewire:Pipewire_Pulse",
        "Pipewire_Wireplumber": "pynix_os.services.pipewire:Pipewire_Wireplumber",
        "Pixelfed": "pynix_os.services.pixelfed:Pixelfed",
        "Pixelfed_Nginx": "pynix_os.services.pixelfed:Pixelfed_Nginx",
        "Pixelfed_Nginx_Listen_Item": "pynix_os.services.pixelfed:Pixelfed_Nginx_Listen_Item",
        "Pixelfed_Nginx_Locations_Value": "pynix_os.services.pixelfed:Pixelfed_Nginx_Locations_Value",
        "Pixelfed_Redis": "pynix_os.services.pixelfed:Pixelfed_Redis",
        "Pixiecore": "pynix_os.services.pixiecore:Pixiecore",
        "Pki": "pynix_os.security.pki:Pki",
        "PlantumlServer": "pynix_os.services.plantuml_server:PlantumlServer",
        "PlantumlServer_Packages": "pynix_os.services.plantuml_server:PlantumlServer_Packages",
        "Plasma6": "pynix_os.environment.plasma6:Plasma6",
        "Plausible": "pynix_os.services.plausible:Plausible",
        "Plausible_AdminUser": "pynix_os.services.plausible:Plausible_AdminUser",
        "Plausible_Database": "pynix_os.services.plausible:Plausible_Database",
        "Plausible_Database_Clickhouse": "pynix_os.services.plausible:Plausible_Database_Clickhouse",
        "Plausible_Database_Postgres": "pynix_os.services.plausible:Plausible_Database_Postgres",
        "Plausible_Mail": "pynix_os.services.plausible:Plausible_Mail",
        "Plausible_Mail_Smtp": "pynix_os.services.plausible:Plausible_Mail_Smtp",
        "Plausible_Server": "pynix_os.services.plausible:Plausible_Server",
        "Playerctld": "pynix_os.services.playerctld:Playerctld",
        "Please": "pynix_os.security.please:Please",
        "Pleroma": "pynix_os.services.pleroma:Pleroma",
        "Plex": "pynix_os.services.plex:Plex",
        "Plikd": "pynix_os.services.plikd:Plikd",
        "Plotinus": "pynix_os.programs.plotinus:Plotinus",
        "Plymouth": "pynix_os.boot.plymouth:Plymouth",
        "Plymouth_Tpm2Totp": "pynix_os.boot.plymouth:Plymouth_Tpm2Totp",
        "Pmount": "pynix_os.programs.pmount:Pmount",
        "PocketId": "pynix_os.services.pocket_id:PocketId",
        "PocketId_Settings": "pynix_os.services.pocket_id:PocketId_Settings",
        "Podgrab": "pynix_os.services.podgrab:Podgrab",
        "Podman": "pynix_os.virtualisation.podman:Podman",
        "Podman_AutoPrune": "pynix_os.virtualisation.podman:Podman_AutoPrune",
        "Podman_DefaultNetwork": "pynix_os.virtualisation.podman:Podman_DefaultNetwork",
        "Podman_DockerSocket": "pynix_os.virtualisation.podman:Podman_DockerSocket",
        "Podman_NetworkSocket": "pynix_os.virtualisation.podman:Podman_NetworkSocket",
        "Podman_NetworkSocket_Tls": "pynix_os.virtualisation.podman:Podman_NetworkSocket_Tls",
        "Polaris": "pynix_os.services.polaris:Polaris",
        "Polkit": "pynix_os.security.polkit:Polkit",
        "Polkit_Settings": "pynix_os.security.polkit:Polkit_Settings",
        "Pomerium": "pynix_os.services.pomerium:Pomerium",
        "PornVault": "pynix_os.services.porn_vault:PornVault",
        "Portal": "pynix_os.xdg.portal:Portal",
        "Portal_Lxqt": "pynix_os.xdg.portal:Portal_Lxqt",
        "Portal_Wlr": "pynix_os.xdg.portal:Portal_Wlr",
        "Portal_Wlr_Settings": "pynix_os.xdg.portal:Portal_Wlr_Settings",
        "Portmaster": "pynix_os.services.portmaster:Portmaster",
        "Portmaster_Profiles_Value": "pynix_os.services.portmaster:Portmaster_Profiles_Value",
        "Portmaster_Profiles_Value_Fingerprints_Item": "pynix_os.services.portmaster:Portmaster_Profiles_Value_Fingerprints_Item",
        "Portmaster_Profiles_Value_Packages_Item": "pynix_os.services.portmaster:Portmaster_Profiles_Value_Packages_Item",
        "Portmaster_Profiles_Value_Settings": "pynix_os.services.portmaster:Portmaster_Profiles_Value_Settings",
        "Portmaster_Settings": "pynix_os.services.portmaster:Portmaster_Settings",
        "Portunus": "pynix_os.services.portunus:Portunus",
        "Portunus_Dex": "pynix_os.services.portunus:Portunus_Dex",
        "Portunus_Dex_OidcClients_Item": "pynix_os.services.portunus:Portunus_Dex_OidcClients_Item",
        "Portunus_Ldap": "pynix_os.services.portunus:Portunus_Ldap",
        "Porxie": "pynix_os.services.porxie:Porxie",
        "Porxie_Settings": "pynix_os.services.porxie:Porxie_Settings",
        "Postfix": "pynix_os.services.postfix:Postfix",
        "PostfixTlspol": "pynix_os.services.postfix_tlspol:PostfixTlspol",
        "PostfixTlspol_Settings": "pynix_os.services.postfix_tlspol:PostfixTlspol_Settings",
        "Postfix_HeaderChecks_Item": "pynix_os.services.postfix:Postfix_HeaderChecks_Item",
        "Postfix_Settings": "pynix_os.services.postfix:Postfix_Settings",
        "Postfix_Settings_Main": "pynix_os.services.postfix:Postfix_Settings_Main",
        "Postfix_Settings_Master_Value": "pynix_os.services.postfix:Postfix_Settings_Master_Value",
        "PostgresWebsockets": "pynix_os.services.postgres_websockets:PostgresWebsockets",
        "PostgresWebsockets_Environment": "pynix_os.services.postgres_websockets:PostgresWebsockets_Environment",
        "PostgresWebsockets_Environment_PGWSDBURI": "pynix_os.services.postgres_websockets:PostgresWebsockets_Environment_PGWSDBURI",
        "Postgresql": "pynix_os.services.postgresql:Postgresql",
        "PostgresqlBackup": "pynix_os.services.postgresqlBackup:PostgresqlBackup",
        "PostgresqlWalReceiver": "pynix_os.services.postgresqlWalReceiver:PostgresqlWalReceiver",
        "PostgresqlWalReceiver_Receivers_Value": "pynix_os.services.postgresqlWalReceiver:PostgresqlWalReceiver_Receivers_Value",
        "Postgresql_EnsureUsers_Item": "pynix_os.services.postgresql:Postgresql_EnsureUsers_Item",
        "Postgresql_EnsureUsers_Item_EnsureClauses": "pynix_os.services.postgresql:Postgresql_EnsureUsers_Item_EnsureClauses",
        "Postgresql_Settings": "pynix_os.services.postgresql:Postgresql_Settings",
        "Postgresql_SystemCallFilter_Value": "pynix_os.services.postgresql:Postgresql_SystemCallFilter_Value",
        "Postgrest": "pynix_os.services.postgrest:Postgrest",
        "Postgrest_Settings": "pynix_os.services.postgrest:Postgrest_Settings",
        "Postgrest_Settings_DbUri": "pynix_os.services.postgrest:Postgrest_Settings_DbUri",
        "Postgrey": "pynix_os.services.postgrey:Postgrey",
        "Postgrey_Socket": "pynix_os.services.postgrey:Postgrey_Socket",
        "Postgrey_Socket_Or": "pynix_os.services.postgrey:Postgrey_Socket_Or",
        "Postsrsd": "pynix_os.services.postsrsd:Postsrsd",
        "Postsrsd_Settings": "pynix_os.services.postsrsd:Postsrsd_Settings",
        "PowerManagement": "pynix_os.powerManagement.__options__:PowerManagement",
        "PowerProfilesDaemon": "pynix_os.services.power_profiles_daemon:PowerProfilesDaemon",
        "Powerdns": "pynix_os.services.powerdns:Powerdns",
        "PowerdnsAdmin": "pynix_os.services.powerdns_admin:PowerdnsAdmin",
        "Powerstation": "pynix_os.services.powerstation:Powerstation",
        "Powertop": "pynix_os.powerManagement.powertop:Powertop",
        "Pppd": "pynix_os.services.pppd:Pppd",
        "Pppd_Peers_Value": "pynix_os.services.pppd:Pppd_Peers_Value",
        "Pptpd": "pynix_os.services.pptpd:Pptpd",
        "Prefect": "pynix_os.services.prefect:Prefect",
        "Prefect_WorkerPools_Value": "pynix_os.services.prefect:Prefect_WorkerPools_Value",
        "Pretalx": "pynix_os.services.pretalx:Pretalx",
        "Pretalx_Celery": "pynix_os.services.pretalx:Pretalx_Celery",
        "Pretalx_Database": "pynix_os.services.pretalx:Pretalx_Database",
        "Pretalx_Gunicorn": "pynix_os.services.pretalx:Pretalx_Gunicorn",
        "Pretalx_Nginx": "pynix_os.services.pretalx:Pretalx_Nginx",
        "Pretalx_Settings": "pynix_os.services.pretalx:Pretalx_Settings",
        "Pretix": "pynix_os.services.pretix:Pretix",
        "Pretix_Celery": "pynix_os.services.pretix:Pretix_Celery",
        "Pretix_Database": "pynix_os.services.pretix:Pretix_Database",
        "Pretix_Gunicorn": "pynix_os.services.pretix:Pretix_Gunicorn",
        "Pretix_Nginx": "pynix_os.services.pretix:Pretix_Nginx",
        "Pretix_Settings": "pynix_os.services.pretix:Pretix_Settings",
        "Printers": "pynix_os.hardware.printers:Printers",
        "Printers_EnsureClasses_Value": "pynix_os.hardware.printers:Printers_EnsureClasses_Value",
        "Printers_EnsurePrinters_Item": "pynix_os.hardware.printers:Printers_EnsurePrinters_Item",
        "Printing": "pynix_os.services.printing:Printing",
        "Printing_Browsed": "pynix_os.services.printing:Printing_Browsed",
        "Printing_CupsPdf": "pynix_os.services.printing:Printing_CupsPdf",
        "Printing_CupsPdf_Instances_Value": "pynix_os.services.printing:Printing_CupsPdf_Instances_Value",
        "Printing_CupsPdf_Instances_Value_Settings": "pynix_os.services.printing:Printing_CupsPdf_Instances_Value_Settings",
        "Privatebin": "pynix_os.services.privatebin:Privatebin",
        "Privatebin_Settings": "pynix_os.services.privatebin:Privatebin_Settings",
        "Privoxy": "pynix_os.services.privoxy:Privoxy",
        "Privoxy_Settings": "pynix_os.services.privoxy:Privoxy_Settings",
        "Projecteur": "pynix_os.programs.projecteur:Projecteur",
        "Prometheus": "pynix_os.services.prometheus:Prometheus",
        "Prometheus_Alertmanager": "pynix_os.services.prometheus:Prometheus_Alertmanager",
        "Prometheus_AlertmanagerGotify": "pynix_os.services.prometheus:Prometheus_AlertmanagerGotify",
        "Prometheus_AlertmanagerGotify_GotifyEndpoint": "pynix_os.services.prometheus:Prometheus_AlertmanagerGotify_GotifyEndpoint",
        "Prometheus_AlertmanagerGotify_Metrics": "pynix_os.services.prometheus:Prometheus_AlertmanagerGotify_Metrics",
        "Prometheus_AlertmanagerIrcRelay": "pynix_os.services.prometheus:Prometheus_AlertmanagerIrcRelay",
        "Prometheus_AlertmanagerNtfy": "pynix_os.services.prometheus:Prometheus_AlertmanagerNtfy",
        "Prometheus_AlertmanagerNtfy_Settings": "pynix_os.services.prometheus:Prometheus_AlertmanagerNtfy_Settings",
        "Prometheus_AlertmanagerNtfy_Settings_NtfyNotificationTags_Item": "pynix_os.services.prometheus:Prometheus_AlertmanagerNtfy_Settings_NtfyNotificationTags_Item",
        "Prometheus_AlertmanagerWebhookLogger": "pynix_os.services.prometheus:Prometheus_AlertmanagerWebhookLogger",
        "Prometheus_Exporters": "pynix_os.services.prometheus:Prometheus_Exporters",
        "Prometheus_Exporters_Apcupsd": "pynix_os.services.prometheus:Prometheus_Exporters_Apcupsd",
        "Prometheus_Exporters_Artifactory": "pynix_os.services.prometheus:Prometheus_Exporters_Artifactory",
        "Prometheus_Exporters_Bind": "pynix_os.services.prometheus:Prometheus_Exporters_Bind",
        "Prometheus_Exporters_Bird": "pynix_os.services.prometheus:Prometheus_Exporters_Bird",
        "Prometheus_Exporters_Bitcoin": "pynix_os.services.prometheus:Prometheus_Exporters_Bitcoin",
        "Prometheus_Exporters_Blackbox": "pynix_os.services.prometheus:Prometheus_Exporters_Blackbox",
        "Prometheus_Exporters_Borgmatic": "pynix_os.services.prometheus:Prometheus_Exporters_Borgmatic",
        "Prometheus_Exporters_BuildkiteAgent": "pynix_os.services.prometheus:Prometheus_Exporters_BuildkiteAgent",
        "Prometheus_Exporters_Chrony": "pynix_os.services.prometheus:Prometheus_Exporters_Chrony",
        "Prometheus_Exporters_Collectd": "pynix_os.services.prometheus:Prometheus_Exporters_Collectd",
        "Prometheus_Exporters_Deluge": "pynix_os.services.prometheus:Prometheus_Exporters_Deluge",
        "Prometheus_Exporters_Dmarc": "pynix_os.services.prometheus:Prometheus_Exporters_Dmarc",
        "Prometheus_Exporters_Dnsmasq": "pynix_os.services.prometheus:Prometheus_Exporters_Dnsmasq",
        "Prometheus_Exporters_Dnssec": "pynix_os.services.prometheus:Prometheus_Exporters_Dnssec",
        "Prometheus_Exporters_Domain": "pynix_os.services.prometheus:Prometheus_Exporters_Domain",
        "Prometheus_Exporters_Dovecot": "pynix_os.services.prometheus:Prometheus_Exporters_Dovecot",
        "Prometheus_Exporters_Ebpf": "pynix_os.services.prometheus:Prometheus_Exporters_Ebpf",
        "Prometheus_Exporters_Ecoflow": "pynix_os.services.prometheus:Prometheus_Exporters_Ecoflow",
        "Prometheus_Exporters_Elasticsearch": "pynix_os.services.prometheus:Prometheus_Exporters_Elasticsearch",
        "Prometheus_Exporters_ExportarrBazarr": "pynix_os.services.prometheus:Prometheus_Exporters_ExportarrBazarr",
        "Prometheus_Exporters_ExportarrLidarr": "pynix_os.services.prometheus:Prometheus_Exporters_ExportarrLidarr",
        "Prometheus_Exporters_ExportarrProwlarr": "pynix_os.services.prometheus:Prometheus_Exporters_ExportarrProwlarr",
        "Prometheus_Exporters_ExportarrRadarr": "pynix_os.services.prometheus:Prometheus_Exporters_ExportarrRadarr",
        "Prometheus_Exporters_ExportarrReadarr": "pynix_os.services.prometheus:Prometheus_Exporters_ExportarrReadarr",
        "Prometheus_Exporters_ExportarrSonarr": "pynix_os.services.prometheus:Prometheus_Exporters_ExportarrSonarr",
        "Prometheus_Exporters_Fail2ban": "pynix_os.services.prometheus:Prometheus_Exporters_Fail2ban",
        "Prometheus_Exporters_Fastly": "pynix_os.services.prometheus:Prometheus_Exporters_Fastly",
        "Prometheus_Exporters_Flow": "pynix_os.services.prometheus:Prometheus_Exporters_Flow",
        "Prometheus_Exporters_Fritz": "pynix_os.services.prometheus:Prometheus_Exporters_Fritz",
        "Prometheus_Exporters_Fritz_Settings": "pynix_os.services.prometheus:Prometheus_Exporters_Fritz_Settings",
        "Prometheus_Exporters_Fritz_Settings_Devices_Item": "pynix_os.services.prometheus:Prometheus_Exporters_Fritz_Settings_Devices_Item",
        "Prometheus_Exporters_Fritzbox": "pynix_os.services.prometheus:Prometheus_Exporters_Fritzbox",
        "Prometheus_Exporters_Frr": "pynix_os.services.prometheus:Prometheus_Exporters_Frr",
        "Prometheus_Exporters_Graphite": "pynix_os.services.prometheus:Prometheus_Exporters_Graphite",
        "Prometheus_Exporters_Graphite_MappingSettings": "pynix_os.services.prometheus:Prometheus_Exporters_Graphite_MappingSettings",
        "Prometheus_Exporters_Idrac": "pynix_os.services.prometheus:Prometheus_Exporters_Idrac",
        "Prometheus_Exporters_ImapMailstat": "pynix_os.services.prometheus:Prometheus_Exporters_ImapMailstat",
        "Prometheus_Exporters_ImapMailstat_Accounts_Value": "pynix_os.services.prometheus:Prometheus_Exporters_ImapMailstat_Accounts_Value",
        "Prometheus_Exporters_Influxdb": "pynix_os.services.prometheus:Prometheus_Exporters_Influxdb",
        "Prometheus_Exporters_Ipmi": "pynix_os.services.prometheus:Prometheus_Exporters_Ipmi",
        "Prometheus_Exporters_Jitsi": "pynix_os.services.prometheus:Prometheus_Exporters_Jitsi",
        "Prometheus_Exporters_Json": "pynix_os.services.prometheus:Prometheus_Exporters_Json",
        "Prometheus_Exporters_JunosCzerwonk": "pynix_os.services.prometheus:Prometheus_Exporters_JunosCzerwonk",
        "Prometheus_Exporters_Kafka": "pynix_os.services.prometheus:Prometheus_Exporters_Kafka",
        "Prometheus_Exporters_Kea": "pynix_os.services.prometheus:Prometheus_Exporters_Kea",
        "Prometheus_Exporters_Keylight": "pynix_os.services.prometheus:Prometheus_Exporters_Keylight",
        "Prometheus_Exporters_Klipper": "pynix_os.services.prometheus:Prometheus_Exporters_Klipper",
        "Prometheus_Exporters_Knot": "pynix_os.services.prometheus:Prometheus_Exporters_Knot",
        "Prometheus_Exporters_Kvrocks": "pynix_os.services.prometheus:Prometheus_Exporters_Kvrocks",
        "Prometheus_Exporters_Libvirt": "pynix_os.services.prometheus:Prometheus_Exporters_Libvirt",
        "Prometheus_Exporters_Lnd": "pynix_os.services.prometheus:Prometheus_Exporters_Lnd",
        "Prometheus_Exporters_Mail": "pynix_os.services.prometheus:Prometheus_Exporters_Mail",
        "Prometheus_Exporters_MailTlsaCheck": "pynix_os.services.prometheus:Prometheus_Exporters_MailTlsaCheck",
        "Prometheus_Exporters_MailTlsaCheck_Settings": "pynix_os.services.prometheus:Prometheus_Exporters_MailTlsaCheck_Settings",
        "Prometheus_Exporters_Mail_Configuration": "pynix_os.services.prometheus:Prometheus_Exporters_Mail_Configuration",
        "Prometheus_Exporters_Mail_Configuration_Servers_Item": "pynix_os.services.prometheus:Prometheus_Exporters_Mail_Configuration_Servers_Item",
        "Prometheus_Exporters_Mailman3": "pynix_os.services.prometheus:Prometheus_Exporters_Mailman3",
        "Prometheus_Exporters_Mikrotik": "pynix_os.services.prometheus:Prometheus_Exporters_Mikrotik",
        "Prometheus_Exporters_Modemmanager": "pynix_os.services.prometheus:Prometheus_Exporters_Modemmanager",
        "Prometheus_Exporters_Mongodb": "pynix_os.services.prometheus:Prometheus_Exporters_Mongodb",
        "Prometheus_Exporters_Mqtt": "pynix_os.services.prometheus:Prometheus_Exporters_Mqtt",
        "Prometheus_Exporters_Mysqld": "pynix_os.services.prometheus:Prometheus_Exporters_Mysqld",
        "Prometheus_Exporters_Nats": "pynix_os.services.prometheus:Prometheus_Exporters_Nats",
        "Prometheus_Exporters_Nextcloud": "pynix_os.services.prometheus:Prometheus_Exporters_Nextcloud",
        "Prometheus_Exporters_Nginx": "pynix_os.services.prometheus:Prometheus_Exporters_Nginx",
        "Prometheus_Exporters_Nginxlog": "pynix_os.services.prometheus:Prometheus_Exporters_Nginxlog",
        "Prometheus_Exporters_Nginxlog_Settings": "pynix_os.services.prometheus:Prometheus_Exporters_Nginxlog_Settings",
        "Prometheus_Exporters_Node": "pynix_os.services.prometheus:Prometheus_Exporters_Node",
        "Prometheus_Exporters_NodeCert": "pynix_os.services.prometheus:Prometheus_Exporters_NodeCert",
        "Prometheus_Exporters_Nut": "pynix_os.services.prometheus:Prometheus_Exporters_Nut",
        "Prometheus_Exporters_NvidiaGpu": "pynix_os.services.prometheus:Prometheus_Exporters_NvidiaGpu",
        "Prometheus_Exporters_Opnsense": "pynix_os.services.prometheus:Prometheus_Exporters_Opnsense",
        "Prometheus_Exporters_Pgbouncer": "pynix_os.services.prometheus:Prometheus_Exporters_Pgbouncer",
        "Prometheus_Exporters_PhpFpm": "pynix_os.services.prometheus:Prometheus_Exporters_PhpFpm",
        "Prometheus_Exporters_Pihole": "pynix_os.services.prometheus:Prometheus_Exporters_Pihole",
        "Prometheus_Exporters_Ping": "pynix_os.services.prometheus:Prometheus_Exporters_Ping",
        "Prometheus_Exporters_Postfix": "pynix_os.services.prometheus:Prometheus_Exporters_Postfix",
        "Prometheus_Exporters_Postgres": "pynix_os.services.prometheus:Prometheus_Exporters_Postgres",
        "Prometheus_Exporters_Process": "pynix_os.services.prometheus:Prometheus_Exporters_Process",
        "Prometheus_Exporters_Pve": "pynix_os.services.prometheus:Prometheus_Exporters_Pve",
        "Prometheus_Exporters_PyAirControl": "pynix_os.services.prometheus:Prometheus_Exporters_PyAirControl",
        "Prometheus_Exporters_Rasdaemon": "pynix_os.services.prometheus:Prometheus_Exporters_Rasdaemon",
        "Prometheus_Exporters_Redis": "pynix_os.services.prometheus:Prometheus_Exporters_Redis",
        "Prometheus_Exporters_Restic": "pynix_os.services.prometheus:Prometheus_Exporters_Restic",
        "Prometheus_Exporters_Rtl433": "pynix_os.services.prometheus:Prometheus_Exporters_Rtl433",
        "Prometheus_Exporters_Rtl433_Channels_Item": "pynix_os.services.prometheus:Prometheus_Exporters_Rtl433_Channels_Item",
        "Prometheus_Exporters_Rtl433_Ids_Item": "pynix_os.services.prometheus:Prometheus_Exporters_Rtl433_Ids_Item",
        "Prometheus_Exporters_Sabnzbd": "pynix_os.services.prometheus:Prometheus_Exporters_Sabnzbd",
        "Prometheus_Exporters_Sabnzbd_Servers_Item": "pynix_os.services.prometheus:Prometheus_Exporters_Sabnzbd_Servers_Item",
        "Prometheus_Exporters_Script": "pynix_os.services.prometheus:Prometheus_Exporters_Script",
        "Prometheus_Exporters_Shelly": "pynix_os.services.prometheus:Prometheus_Exporters_Shelly",
        "Prometheus_Exporters_Smartctl": "pynix_os.services.prometheus:Prometheus_Exporters_Smartctl",
        "Prometheus_Exporters_Smokeping": "pynix_os.services.prometheus:Prometheus_Exporters_Smokeping",
        "Prometheus_Exporters_Snmp": "pynix_os.services.prometheus:Prometheus_Exporters_Snmp",
        "Prometheus_Exporters_Snowflake": "pynix_os.services.prometheus:Prometheus_Exporters_Snowflake",
        "Prometheus_Exporters_Speedtest": "pynix_os.services.prometheus:Prometheus_Exporters_Speedtest",
        "Prometheus_Exporters_Sql": "pynix_os.services.prometheus:Prometheus_Exporters_Sql",
        "Prometheus_Exporters_Sql_Configuration": "pynix_os.services.prometheus:Prometheus_Exporters_Sql_Configuration",
        "Prometheus_Exporters_Sql_Configuration_Jobs_Value": "pynix_os.services.prometheus:Prometheus_Exporters_Sql_Configuration_Jobs_Value",
        "Prometheus_Exporters_Sql_Configuration_Jobs_Value_Queries_Value": "pynix_os.services.prometheus:Prometheus_Exporters_Sql_Configuration_Jobs_Value_Queries_Value",
        "Prometheus_Exporters_Statsd": "pynix_os.services.prometheus:Prometheus_Exporters_Statsd",
        "Prometheus_Exporters_Storagebox": "pynix_os.services.prometheus:Prometheus_Exporters_Storagebox",
        "Prometheus_Exporters_Surfboard": "pynix_os.services.prometheus:Prometheus_Exporters_Surfboard",
        "Prometheus_Exporters_Systemd": "pynix_os.services.prometheus:Prometheus_Exporters_Systemd",
        "Prometheus_Exporters_Tailscale": "pynix_os.services.prometheus:Prometheus_Exporters_Tailscale",
        "Prometheus_Exporters_Tibber": "pynix_os.services.prometheus:Prometheus_Exporters_Tibber",
        "Prometheus_Exporters_Unbound": "pynix_os.services.prometheus:Prometheus_Exporters_Unbound",
        "Prometheus_Exporters_Unpoller": "pynix_os.services.prometheus:Prometheus_Exporters_Unpoller",
        "Prometheus_Exporters_Unpoller_Controllers_Item": "pynix_os.services.prometheus:Prometheus_Exporters_Unpoller_Controllers_Item",
        "Prometheus_Exporters_V2ray": "pynix_os.services.prometheus:Prometheus_Exporters_V2ray",
        "Prometheus_Exporters_Varnish": "pynix_os.services.prometheus:Prometheus_Exporters_Varnish",
        "Prometheus_Exporters_Wireguard": "pynix_os.services.prometheus:Prometheus_Exporters_Wireguard",
        "Prometheus_Exporters_Xray": "pynix_os.services.prometheus:Prometheus_Exporters_Xray",
        "Prometheus_Exporters_Yace": "pynix_os.services.prometheus:Prometheus_Exporters_Yace",
        "Prometheus_Exporters_Zfs": "pynix_os.services.prometheus:Prometheus_Exporters_Zfs",
        "Prometheus_Exporters_ZfsSiebenmann": "pynix_os.services.prometheus:Prometheus_Exporters_ZfsSiebenmann",
        "Prometheus_GlobalConfig": "pynix_os.services.prometheus:Prometheus_GlobalConfig",
        "Prometheus_Pushgateway": "pynix_os.services.prometheus:Prometheus_Pushgateway",
        "Prometheus_Pushgateway_Log": "pynix_os.services.prometheus:Prometheus_Pushgateway_Log",
        "Prometheus_Pushgateway_Persistence": "pynix_os.services.prometheus:Prometheus_Pushgateway_Persistence",
        "Prometheus_Pushgateway_Web": "pynix_os.services.prometheus:Prometheus_Pushgateway_Web",
        "Prometheus_RemoteRead_Item": "pynix_os.services.prometheus:Prometheus_RemoteRead_Item",
        "Prometheus_RemoteRead_Item_BasicAuth": "pynix_os.services.prometheus:Prometheus_RemoteRead_Item_BasicAuth",
        "Prometheus_RemoteRead_Item_TlsConfig": "pynix_os.services.prometheus:Prometheus_RemoteRead_Item_TlsConfig",
        "Prometheus_RemoteWrite_Item": "pynix_os.services.prometheus:Prometheus_RemoteWrite_Item",
        "Prometheus_RemoteWrite_Item_MetadataConfig": "pynix_os.services.prometheus:Prometheus_RemoteWrite_Item_MetadataConfig",
        "Prometheus_RemoteWrite_Item_QueueConfig": "pynix_os.services.prometheus:Prometheus_RemoteWrite_Item_QueueConfig",
        "Prometheus_RemoteWrite_Item_Sigv4": "pynix_os.services.prometheus:Prometheus_RemoteWrite_Item_Sigv4",
        "Prometheus_RemoteWrite_Item_WriteRelabelConfigs_Item": "pynix_os.services.prometheus:Prometheus_RemoteWrite_Item_WriteRelabelConfigs_Item",
        "Prometheus_Sachet": "pynix_os.services.prometheus:Prometheus_Sachet",
        "Prometheus_ScrapeConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_AzureSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_AzureSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Authorization": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Authorization",
        "Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Oauth2": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_ConsulSdConfigs_Item_Oauth2",
        "Prometheus_ScrapeConfigs_Item_DigitaloceanSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_DigitaloceanSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_DnsSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_DnsSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item_Filters_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_DockerSdConfigs_Item_Filters_Item",
        "Prometheus_ScrapeConfigs_Item_DockerswarmSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_DockerswarmSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item_Filters_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_Ec2SdConfigs_Item_Filters_Item",
        "Prometheus_ScrapeConfigs_Item_EurekaSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_EurekaSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_FileSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_FileSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_GceSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_GceSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_HetznerSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_HetznerSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_HttpSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_HttpSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Namespaces": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Namespaces",
        "Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Selectors_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_KubernetesSdConfigs_Item_Selectors_Item",
        "Prometheus_ScrapeConfigs_Item_KumaSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_KumaSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_LightsailSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_LightsailSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_LinodeSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_LinodeSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_MarathonSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_MarathonSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_NerveSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_NerveSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_OpenstackSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_OpenstackSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_PuppetdbSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_PuppetdbSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_ScalewaySdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_ScalewaySdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_StaticConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_StaticConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_TritonSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_TritonSdConfigs_Item",
        "Prometheus_ScrapeConfigs_Item_UyuniSdConfigs_Item": "pynix_os.services.prometheus:Prometheus_ScrapeConfigs_Item_UyuniSdConfigs_Item",
        "Prometheus_XmppAlerts": "pynix_os.services.prometheus:Prometheus_XmppAlerts",
        "Prosody": "pynix_os.services.prosody:Prosody",
        "Prosody_DiscoItems_Item": "pynix_os.services.prosody:Prosody_DiscoItems_Item",
        "Prosody_HttpFileShare": "pynix_os.services.prosody:Prosody_HttpFileShare",
        "Prosody_Modules": "pynix_os.services.prosody:Prosody_Modules",
        "Prosody_Muc_Item": "pynix_os.services.prosody:Prosody_Muc_Item",
        "Prosody_Ssl": "pynix_os.services.prosody:Prosody_Ssl",
        "Prosody_VirtualHosts_Value": "pynix_os.services.prosody:Prosody_VirtualHosts_Value",
        "ProtonmailBridge": "pynix_os.services.protonmail_bridge:ProtonmailBridge",
        "Prowlarr": "pynix_os.services.prowlarr:Prowlarr",
        "Prowlarr_Settings": "pynix_os.services.prowlarr:Prowlarr_Settings",
        "Proxy": "pynix_os.networking.proxy:Proxy",
        "Proxychains": "pynix_os.programs.proxychains:Proxychains",
        "Proxychains_Proxies_Value": "pynix_os.programs.proxychains:Proxychains_Proxies_Value",
        "Psd": "pynix_os.services.psd:Psd",
        "PublicInbox": "pynix_os.services.public_inbox:PublicInbox",
        "PublicInbox_Http": "pynix_os.services.public_inbox:PublicInbox_Http",
        "PublicInbox_Imap": "pynix_os.services.public_inbox:PublicInbox_Imap",
        "PublicInbox_Inboxes_Value": "pynix_os.services.public_inbox:PublicInbox_Inboxes_Value",
        "PublicInbox_Mda": "pynix_os.services.public_inbox:PublicInbox_Mda",
        "PublicInbox_Nntp": "pynix_os.services.public_inbox:PublicInbox_Nntp",
        "PublicInbox_Postfix": "pynix_os.services.public_inbox:PublicInbox_Postfix",
        "PublicInbox_Settings": "pynix_os.services.public_inbox:PublicInbox_Settings",
        "PublicInbox_Settings_Coderepo_Value": "pynix_os.services.public_inbox:PublicInbox_Settings_Coderepo_Value",
        "PublicInbox_Settings_Publicinbox": "pynix_os.services.public_inbox:PublicInbox_Settings_Publicinbox",
        "Pufferpanel": "pynix_os.services.pufferpanel:Pufferpanel",
        "Pulseaudio": "pynix_os.services.pulseaudio:Pulseaudio",
        "Pulseaudio_Daemon": "pynix_os.services.pulseaudio:Pulseaudio_Daemon",
        "Pulseaudio_Tcp": "pynix_os.services.pulseaudio:Pulseaudio_Tcp",
        "Pulseaudio_Tcp_AnonymousClients": "pynix_os.services.pulseaudio:Pulseaudio_Tcp_AnonymousClients",
        "Pulseaudio_Zeroconf": "pynix_os.services.pulseaudio:Pulseaudio_Zeroconf",
        "Pulseaudio_Zeroconf_Discovery": "pynix_os.services.pulseaudio:Pulseaudio_Zeroconf_Discovery",
        "Pulseaudio_Zeroconf_Publish": "pynix_os.services.pulseaudio:Pulseaudio_Zeroconf_Publish",
        "Pulseview": "pynix_os.programs.pulseview:Pulseview",
        "Pumpkin": "pynix_os.services.pumpkin:Pumpkin",
        "Pumpkin_Settings": "pynix_os.services.pumpkin:Pumpkin_Settings",
        "Pumpkin_Whitelist": "pynix_os.services.pumpkin:Pumpkin_Whitelist",
        "Pumpkin_Whitelist_Entries_Item": "pynix_os.services.pumpkin:Pumpkin_Whitelist_Entries_Item",
        "Pykms": "pynix_os.services.pykms:Pykms",
        "Pyroscope": "pynix_os.services.pyroscope:Pyroscope",
        "Pyroscope_Settings": "pynix_os.services.pyroscope:Pyroscope_Settings",
        "QbitManage": "pynix_os.services.qbit_manage:QbitManage",
        "QbitManage_Commands": "pynix_os.services.qbit_manage:QbitManage_Commands",
        "QbitManage_Settings": "pynix_os.services.qbit_manage:QbitManage_Settings",
        "QbitManage_Settings_Directory": "pynix_os.services.qbit_manage:QbitManage_Settings_Directory",
        "QbitManage_Settings_Qbt": "pynix_os.services.qbit_manage:QbitManage_Settings_Qbt",
        "QbitManage_Settings_Tracker_Value": "pynix_os.services.qbit_manage:QbitManage_Settings_Tracker_Value",
        "QbitManage_WebServer": "pynix_os.services.qbit_manage:QbitManage_WebServer",
        "Qbittorrent": "pynix_os.services.qbittorrent:Qbittorrent",
        "Qbittorrent_ServerConfig": "pynix_os.services.qbittorrent:Qbittorrent_ServerConfig",
        "Qdmr": "pynix_os.programs.qdmr:Qdmr",
        "Qdrant": "pynix_os.services.qdrant:Qdrant",
        "Qemu": "pynix_os.virtualisation.qemu:Qemu",
        "QemuGuest": "pynix_os.services.qemuGuest:QemuGuest",
        "Qemu_Firmware": "pynix_os.virtualisation.qemu:Qemu_Firmware",
        "Qgroundcontrol": "pynix_os.programs.qgroundcontrol:Qgroundcontrol",
        "Qt": "pynix_os.qt.__options__:Qt",
        "Quake3Server": "pynix_os.services.quake3_server:Quake3Server",
        "Quake3Server_Settings": "pynix_os.services.quake3_server:Quake3Server_Settings",
        "QuarkGoldleaf": "pynix_os.programs.quark_goldleaf:QuarkGoldleaf",
        "Quassel": "pynix_os.services.quassel:Quassel",
        "Qui": "pynix_os.services.qui:Qui",
        "Qui_Settings": "pynix_os.services.qui:Qui_Settings",
        "Quickwit": "pynix_os.services.quickwit:Quickwit",
        "Quickwit_Settings": "pynix_os.services.quickwit:Quickwit_Settings",
        "Quickwit_Settings_Rest": "pynix_os.services.quickwit:Quickwit_Settings_Rest",
        "R53Ddns": "pynix_os.services.r53_ddns:R53Ddns",
        "Rabbitmq": "pynix_os.services.rabbitmq:Rabbitmq",
        "Rabbitmq_ManagementPlugin": "pynix_os.services.rabbitmq:Rabbitmq_ManagementPlugin",
        "Radarr": "pynix_os.services.radarr:Radarr",
        "Radarr_Settings": "pynix_os.services.radarr:Radarr_Settings",
        "Radicale": "pynix_os.services.radicale:Radicale",
        "Radicle": "pynix_os.services.radicle:Radicle",
        "Radicle_Ci": "pynix_os.services.radicle:Radicle_Ci",
        "Radicle_Ci_Adapters": "pynix_os.services.radicle:Radicle_Ci_Adapters",
        "Radicle_Ci_Adapters_Native": "pynix_os.services.radicle:Radicle_Ci_Adapters_Native",
        "Radicle_Ci_Adapters_Native_Instances_Value": "pynix_os.services.radicle:Radicle_Ci_Adapters_Native_Instances_Value",
        "Radicle_Ci_Adapters_Native_Instances_Value_Settings": "pynix_os.services.radicle:Radicle_Ci_Adapters_Native_Instances_Value_Settings",
        "Radicle_Ci_Broker": "pynix_os.services.radicle:Radicle_Ci_Broker",
        "Radicle_Ci_Broker_Settings": "pynix_os.services.radicle:Radicle_Ci_Broker_Settings",
        "Radicle_Ci_Broker_Settings_Adapters_Value": "pynix_os.services.radicle:Radicle_Ci_Broker_Settings_Adapters_Value",
        "Radicle_Ci_Broker_Settings_Triggers_Item": "pynix_os.services.radicle:Radicle_Ci_Broker_Settings_Triggers_Item",
        "Radicle_Httpd": "pynix_os.services.radicle:Radicle_Httpd",
        "Radicle_Httpd_Nginx": "pynix_os.services.radicle:Radicle_Httpd_Nginx",
        "Radicle_Httpd_Nginx_Listen_Item": "pynix_os.services.radicle:Radicle_Httpd_Nginx_Listen_Item",
        "Radicle_Httpd_Nginx_Locations_Value": "pynix_os.services.radicle:Radicle_Httpd_Nginx_Locations_Value",
        "Radicle_Node": "pynix_os.services.radicle:Radicle_Node",
        "Radicle_Settings": "pynix_os.services.radicle:Radicle_Settings",
        "Radvd": "pynix_os.services.radvd:Radvd",
        "Raid": "pynix_os.hardware.raid:Raid",
        "Raid_HPSmartArray": "pynix_os.hardware.raid:Raid_HPSmartArray",
        "Rasdaemon": "pynix_os.hardware.rasdaemon:Rasdaemon",
        "Ratbagd": "pynix_os.services.ratbagd:Ratbagd",
        "Rathole": "pynix_os.services.rathole:Rathole",
        "Rauc": "pynix_os.services.rauc:Rauc",
        "Rauc_Client": "pynix_os.services.rauc:Rauc_Client",
        "Rauc_MarkGood": "pynix_os.services.rauc:Rauc_MarkGood",
        "Rauc_Slots_Value_Item": "pynix_os.services.rauc:Rauc_Slots_Value_Item",
        "Rdnssd": "pynix_os.services.rdnssd:Rdnssd",
        "Reaction": "pynix_os.services.reaction:Reaction",
        "Reaction_Settings": "pynix_os.services.reaction:Reaction_Settings",
        "Reaction_Settings_Plugins_Value": "pynix_os.services.reaction:Reaction_Settings_Plugins_Value",
        "Readarr": "pynix_os.services.readarr:Readarr",
        "Readarr_Settings": "pynix_os.services.readarr:Readarr_Settings",
        "Readeck": "pynix_os.services.readeck:Readeck",
        "Realm": "pynix_os.services.realm:Realm",
        "Realm_Config": "pynix_os.services.realm:Realm_Config",
        "Realmd": "pynix_os.services.realmd:Realmd",
        "Rebuilderd": "pynix_os.services.rebuilderd:Rebuilderd",
        "Rebuilderd_Settings": "pynix_os.services.rebuilderd:Rebuilderd_Settings",
        "Recyclarr": "pynix_os.services.recyclarr:Recyclarr",
        "Redis": "pynix_os.services.redis:Redis",
        "Redis_Servers_Value": "pynix_os.services.redis:Redis_Servers_Value",
        "Redis_Servers_Value_SlaveOf": "pynix_os.services.redis:Redis_Servers_Value_SlaveOf",
        "Redlib": "pynix_os.services.redlib:Redlib",
        "Redlib_Settings": "pynix_os.services.redlib:Redlib_Settings",
        "Redmine": "pynix_os.services.redmine:Redmine",
        "Redmine_Components": "pynix_os.services.redmine:Redmine_Components",
        "Redshift": "pynix_os.services.redshift:Redshift",
        "Redshift_Brightness": "pynix_os.services.redshift:Redshift_Brightness",
        "Redshift_Temperature": "pynix_os.services.redshift:Redshift_Temperature",
        "Redsocks": "pynix_os.services.redsocks:Redsocks",
        "Redsocks_Redsocks_Item": "pynix_os.services.redsocks:Redsocks_Redsocks_Item",
        "Reframe": "pynix_os.services.reframe:Reframe",
        "Reframe_Configs": "pynix_os.services.reframe:Reframe_Configs",
        "Remark42": "pynix_os.services.remark42:Remark42",
        "Renderdoc": "pynix_os.programs.renderdoc:Renderdoc",
        "Renovate": "pynix_os.services.renovate:Renovate",
        "Repart": "pynix_os.systemd.repart:Repart",
        "ReplaceDependencies": "pynix_os.system.replaceDependencies:ReplaceDependencies",
        "ReplaceDependencies_Replacements_Item": "pynix_os.system.replaceDependencies:ReplaceDependencies_Replacements_Item",
        "Reposilite": "pynix_os.services.reposilite:Reposilite",
        "Reposilite_Database": "pynix_os.services.reposilite:Reposilite_Database",
        "Reposilite_Settings": "pynix_os.services.reposilite:Reposilite_Settings",
        "Resilio": "pynix_os.services.resilio:Resilio",
        "Resolvconf": "pynix_os.networking.resolvconf:Resolvconf",
        "Resolved": "pynix_os.services.resolved:Resolved",
        "Resolved_DnsDelegates_Value": "pynix_os.services.resolved:Resolved_DnsDelegates_Value",
        "Resolved_DnsDelegates_Value_Delegate": "pynix_os.services.resolved:Resolved_DnsDelegates_Value_Delegate",
        "Resolved_Settings": "pynix_os.services.resolved:Resolved_Settings",
        "Resolved_Settings_Resolve": "pynix_os.services.resolved:Resolved_Settings_Resolve",
        "Restic": "pynix_os.services.restic:Restic",
        "Restic_Backups_Value": "pynix_os.services.restic:Restic_Backups_Value",
        "Restic_Server": "pynix_os.services.restic:Restic_Server",
        "Rethinkdb": "pynix_os.services.rethinkdb:Rethinkdb",
        "Riemann": "pynix_os.services.riemann:Riemann",
        "RiemannDash": "pynix_os.services.riemann_dash:RiemannDash",
        "RiemannTools": "pynix_os.services.riemann_tools:RiemannTools",
        "Rimgo": "pynix_os.services.rimgo:Rimgo",
        "Rimgo_Settings": "pynix_os.services.rimgo:Rimgo_Settings",
        "Ringboard": "pynix_os.services.ringboard:Ringboard",
        "Ringboard_Wayland": "pynix_os.services.ringboard:Ringboard_Wayland",
        "Ringboard_X11": "pynix_os.services.ringboard:Ringboard_X11",
        "RiverClassic": "pynix_os.programs.river_classic:RiverClassic",
        "RiverClassic_Xwayland": "pynix_os.programs.river_classic:RiverClassic_Xwayland",
        "Rke2": "pynix_os.services.rke2:Rke2",
        "Rke2_AutoDeployCharts_Value": "pynix_os.services.rke2:Rke2_AutoDeployCharts_Value",
        "Rke2_GracefulNodeShutdown": "pynix_os.services.rke2:Rke2_GracefulNodeShutdown",
        "Rke2_Manifests_Value": "pynix_os.services.rke2:Rke2_Manifests_Value",
        "Rkvm": "pynix_os.services.rkvm:Rkvm",
        "Rkvm_Client": "pynix_os.services.rkvm:Rkvm_Client",
        "Rkvm_Client_Settings": "pynix_os.services.rkvm:Rkvm_Client_Settings",
        "Rkvm_Server": "pynix_os.services.rkvm:Rkvm_Server",
        "Rkvm_Server_Settings": "pynix_os.services.rkvm:Rkvm_Server_Settings",
        "Rmfakecloud": "pynix_os.services.rmfakecloud:Rmfakecloud",
        "Rnsd": "pynix_os.services.rnsd:Rnsd",
        "Rnsd_HealthCheck": "pynix_os.services.rnsd:Rnsd_HealthCheck",
        "RobustircBridge": "pynix_os.services.robustirc_bridge:RobustircBridge",
        "RogControlCenter": "pynix_os.programs.rog_control_center:RogControlCenter",
        "Romm": "pynix_os.services.romm:Romm",
        "Romm_Database": "pynix_os.services.romm:Romm_Database",
        "Romm_Nginx": "pynix_os.services.romm:Romm_Nginx",
        "Romm_Redis": "pynix_os.services.romm:Romm_Redis",
        "Romm_Watcher": "pynix_os.services.romm:Romm_Watcher",
        "RoonBridge": "pynix_os.services.roon_bridge:RoonBridge",
        "RoonServer": "pynix_os.services.roon_server:RoonServer",
        "Rosec": "pynix_os.services.rosec:Rosec",
        "Rosec_Pam": "pynix_os.services.rosec:Rosec_Pam",
        "Rosenpass": "pynix_os.services.rosenpass:Rosenpass",
        "Rosenpass_Settings": "pynix_os.services.rosenpass:Rosenpass_Settings",
        "Rosenpass_Settings_Peers_Item": "pynix_os.services.rosenpass:Rosenpass_Settings_Peers_Item",
        "Rosetta": "pynix_os.virtualisation.rosetta:Rosetta",
        "Roundcube": "pynix_os.services.roundcube:Roundcube",
        "Roundcube_Database": "pynix_os.services.roundcube:Roundcube_Database",
        "Routedns": "pynix_os.services.routedns:Routedns",
        "Routinator": "pynix_os.services.routinator:Routinator",
        "Routinator_Settings": "pynix_os.services.routinator:Routinator_Settings",
        "Rpcbind": "pynix_os.services.rpcbind:Rpcbind",
        "Rqbit": "pynix_os.services.rqbit:Rqbit",
        "Rshim": "pynix_os.services.rshim:Rshim",
        "Rsnapshot": "pynix_os.services.rsnapshot:Rsnapshot",
        "Rspamd": "pynix_os.services.rspamd:Rspamd",
        "RspamdTrainer": "pynix_os.services.rspamd_trainer:RspamdTrainer",
        "RspamdTrainer_Settings": "pynix_os.services.rspamd_trainer:RspamdTrainer_Settings",
        "Rspamd_Locals_Value": "pynix_os.services.rspamd:Rspamd_Locals_Value",
        "Rspamd_Overrides_Value": "pynix_os.services.rspamd:Rspamd_Overrides_Value",
        "Rspamd_Postfix": "pynix_os.services.rspamd:Rspamd_Postfix",
        "Rspamd_Workers_Value": "pynix_os.services.rspamd:Rspamd_Workers_Value",
        "Rspamd_Workers_Value_BindSockets_Item_Or": "pynix_os.services.rspamd:Rspamd_Workers_Value_BindSockets_Item_Or",
        "Rss2email": "pynix_os.services.rss2email:Rss2email",
        "Rss2email_Feeds_Value": "pynix_os.services.rss2email:Rss2email_Feeds_Value",
        "RssBridge": "pynix_os.services.rss_bridge:RssBridge",
        "RssBridge_Config": "pynix_os.services.rss_bridge:RssBridge_Config",
        "Rsshub": "pynix_os.services.rsshub:Rsshub",
        "Rsshub_Redis": "pynix_os.services.rsshub:Rsshub_Redis",
        "Rsshub_Settings": "pynix_os.services.rsshub:Rsshub_Settings",
        "RstudioServer": "pynix_os.services.rstudio_server:RstudioServer",
        "Rsync": "pynix_os.services.rsync:Rsync",
        "Rsync_Jobs_Value": "pynix_os.services.rsync:Rsync_Jobs_Value",
        "Rsyncd": "pynix_os.services.rsyncd:Rsyncd",
        "Rsyncd_Settings": "pynix_os.services.rsyncd:Rsyncd_Settings",
        "Rsyslogd": "pynix_os.services.rsyslogd:Rsyslogd",
        "Rtkit": "pynix_os.security.rtkit:Rtkit",
        "RtlSdr": "pynix_os.hardware.rtl_sdr:RtlSdr",
        "Rtorrent": "pynix_os.services.rtorrent:Rtorrent",
        "Rumno": "pynix_os.services.rumno:Rumno",
        "Run0": "pynix_os.security.run0:Run0",
        "Run0_PersistentAuth": "pynix_os.security.run0:Run0_PersistentAuth",
        "Run0_SudoShim": "pynix_os.security.run0:Run0_SudoShim",
        "Rundeck": "pynix_os.services.rundeck:Rundeck",
        "Rundeck_FrameworkSettings": "pynix_os.services.rundeck:Rundeck_FrameworkSettings",
        "Rundeck_Settings": "pynix_os.services.rundeck:Rundeck_Settings",
        "Rundeck_Ssl": "pynix_os.services.rundeck:Rundeck_Ssl",
        "Rush": "pynix_os.programs.rush:Rush",
        "RustFederationTester": "pynix_os.services.rust_federation_tester:RustFederationTester",
        "RustFederationTester_Settings": "pynix_os.services.rust_federation_tester:RustFederationTester_Settings",
        "RustMotd": "pynix_os.programs.rust_motd:RustMotd",
        "RustdeskServer": "pynix_os.services.rustdesk_server:RustdeskServer",
        "RustdeskServer_Relay": "pynix_os.services.rustdesk_server:RustdeskServer_Relay",
        "RustdeskServer_Signal": "pynix_os.services.rustdesk_server:RustdeskServer_Signal",
        "Rustfs": "pynix_os.services.rustfs:Rustfs",
        "Rustfs_Settings": "pynix_os.services.rustfs:Rustfs_Settings",
        "Rustical": "pynix_os.services.rustical:Rustical",
        "Rustical_Settings": "pynix_os.services.rustical:Rustical_Settings",
        "Rustus": "pynix_os.services.rustus:Rustus",
        "Rustus_InfoStorage": "pynix_os.services.rustus:Rustus_InfoStorage",
        "Rustus_Storage": "pynix_os.services.rustus:Rustus_Storage",
        "Rutorrent": "pynix_os.services.rutorrent:Rutorrent",
        "Rutorrent_Nginx": "pynix_os.services.rutorrent:Rutorrent_Nginx",
        "Rxe": "pynix_os.networking.rxe:Rxe",
        "RyzenMonitorNg": "pynix_os.programs.ryzen_monitor_ng:RyzenMonitorNg",
        "Sabnzbd": "pynix_os.services.sabnzbd:Sabnzbd",
        "Sabnzbd_Settings": "pynix_os.services.sabnzbd:Sabnzbd_Settings",
        "Sabnzbd_Settings_Ntfosd": "pynix_os.services.sabnzbd:Sabnzbd_Settings_Ntfosd",
        "Sabnzbd_Settings_Servers_Value": "pynix_os.services.sabnzbd:Sabnzbd_Settings_Servers_Value",
        "Safeeyes": "pynix_os.services.safeeyes:Safeeyes",
        "SaleaeLogic": "pynix_os.hardware.saleae_logic:SaleaeLogic",
        "Salt": "pynix_os.services.salt:Salt",
        "Salt_Master": "pynix_os.services.salt:Salt_Master",
        "Salt_Minion": "pynix_os.services.salt:Salt_Minion",
        "Samba": "pynix_os.services.samba:Samba",
        "SambaWsdd": "pynix_os.services.samba_wsdd:SambaWsdd",
        "Samba_Nmbd": "pynix_os.services.samba:Samba_Nmbd",
        "Samba_Settings": "pynix_os.services.samba:Samba_Settings",
        "Samba_Smbd": "pynix_os.services.samba:Samba_Smbd",
        "Samba_Usershares": "pynix_os.services.samba:Samba_Usershares",
        "Samba_Winbindd": "pynix_os.services.samba:Samba_Winbindd",
        "Sane": "pynix_os.hardware.sane:Sane",
        "Sane_Brscan4": "pynix_os.hardware.sane:Sane_Brscan4",
        "Sane_Brscan4_NetDevices_Value": "pynix_os.hardware.sane:Sane_Brscan4_NetDevices_Value",
        "Sane_Brscan5": "pynix_os.hardware.sane:Sane_Brscan5",
        "Sane_Brscan5_NetDevices_Value": "pynix_os.hardware.sane:Sane_Brscan5_NetDevices_Value",
        "Sane_Drivers": "pynix_os.hardware.sane:Sane_Drivers",
        "Sane_Drivers_ScanSnap": "pynix_os.hardware.sane:Sane_Drivers_ScanSnap",
        "Sane_Dsseries": "pynix_os.hardware.sane:Sane_Dsseries",
        "Saned": "pynix_os.services.saned:Saned",
        "Sanoid": "pynix_os.services.sanoid:Sanoid",
        "Sanoid_Datasets_Value": "pynix_os.services.sanoid:Sanoid_Datasets_Value",
        "Sanoid_Templates_Value": "pynix_os.services.sanoid:Sanoid_Templates_Value",
        "Saslauthd": "pynix_os.services.saslauthd:Saslauthd",
        "Sata": "pynix_os.hardware.sata:Sata",
        "Sata_Timeout": "pynix_os.hardware.sata:Sata_Timeout",
        "Sata_Timeout_Drives_Item": "pynix_os.hardware.sata:Sata_Timeout_Drives_Item",
        "Saunafs": "pynix_os.services.saunafs:Saunafs",
        "Saunafs_Chunkserver": "pynix_os.services.saunafs:Saunafs_Chunkserver",
        "Saunafs_Chunkserver_Settings": "pynix_os.services.saunafs:Saunafs_Chunkserver_Settings",
        "Saunafs_Client": "pynix_os.services.saunafs:Saunafs_Client",
        "Saunafs_Master": "pynix_os.services.saunafs:Saunafs_Master",
        "Saunafs_Master_Settings": "pynix_os.services.saunafs:Saunafs_Master_Settings",
        "Saunafs_Metalogger": "pynix_os.services.saunafs:Saunafs_Metalogger",
        "Saunafs_Metalogger_Settings": "pynix_os.services.saunafs:Saunafs_Metalogger_Settings",
        "Scanservjs": "pynix_os.services.scanservjs:Scanservjs",
        "Scanservjs_Settings": "pynix_os.services.scanservjs:Scanservjs_Settings",
        "Schleuder": "pynix_os.services.schleuder:Schleuder",
        "Schleuder_Settings": "pynix_os.services.schleuder:Schleuder_Settings",
        "Schroot": "pynix_os.programs.schroot:Schroot",
        "Schroot_Profiles_Value": "pynix_os.programs.schroot:Schroot_Profiles_Value",
        "Scion": "pynix_os.services.scion:Scion",
        "Scion_ScionControl": "pynix_os.services.scion:Scion_ScionControl",
        "Scion_ScionDaemon": "pynix_os.services.scion:Scion_ScionDaemon",
        "Scion_ScionDispatcher": "pynix_os.services.scion:Scion_ScionDispatcher",
        "Scion_ScionIpGateway": "pynix_os.services.scion:Scion_ScionIpGateway",
        "Scion_ScionRouter": "pynix_os.services.scion:Scion_ScionRouter",
        "Scollector": "pynix_os.services.scollector:Scollector",
        "Screego": "pynix_os.services.screego:Screego",
        "Screen": "pynix_os.programs.screen:Screen",
        "Scrutiny": "pynix_os.services.scrutiny:Scrutiny",
        "Scrutiny_Collector": "pynix_os.services.scrutiny:Scrutiny_Collector",
        "Scrutiny_Collector_Settings": "pynix_os.services.scrutiny:Scrutiny_Collector_Settings",
        "Scrutiny_Influxdb": "pynix_os.services.scrutiny:Scrutiny_Influxdb",
        "Scrutiny_Settings": "pynix_os.services.scrutiny:Scrutiny_Settings",
        "Scx": "pynix_os.services.scx:Scx",
        "ScxLoader": "pynix_os.services.scx_loader:ScxLoader",
        "ScxLoader_Config": "pynix_os.services.scx_loader:ScxLoader_Config",
        "SdrplayApi": "pynix_os.services.sdrplayApi:SdrplayApi",
        "Seahorse": "pynix_os.programs.seahorse:Seahorse",
        "Searx": "pynix_os.services.searx:Searx",
        "Searx_Settings": "pynix_os.services.searx:Searx_Settings",
        "Seatd": "pynix_os.services.seatd:Seatd",
        "Security": "pynix_os.security.__options__:Security",
        "Security_Wrappers_Value": "pynix_os.security.__options__:Security_Wrappers_Value",
        "Sedutil": "pynix_os.programs.sedutil:Sedutil",
        "Seerr": "pynix_os.services.seerr:Seerr",
        "SelfDeploy": "pynix_os.services.self_deploy:SelfDeploy",
        "Selfoss": "pynix_os.services.selfoss:Selfoss",
        "Selfoss_Nginx": "pynix_os.services.selfoss:Selfoss_Nginx",
        "Selfoss_Settings": "pynix_os.services.selfoss:Selfoss_Settings",
        "Send": "pynix_os.services.send:Send",
        "Send_Redis": "pynix_os.services.send:Send_Redis",
        "Sensor": "pynix_os.hardware.sensor:Sensor",
        "Sensor_Hddtemp": "pynix_os.hardware.sensor:Sensor_Hddtemp",
        "Sensor_Iio": "pynix_os.hardware.sensor:Sensor_Iio",
        "Services": "pynix_os.services.__options__:Services",
        "Services_Bitcoind_Value": "pynix_os.services.__options__:Services_Bitcoind_Value",
        "Services_Bitcoind_Value_RpcUsers_Value": "pynix_os.services.__options__:Services_Bitcoind_Value_RpcUsers_Value",
        "Services_BlockbookFrontend_Value": "pynix_os.services.__options__:Services_BlockbookFrontend_Value",
        "Services_BuildkiteAgents_Value": "pynix_os.services.__options__:Services_BuildkiteAgents_Value",
        "Services_Cgit_Value": "pynix_os.services.__options__:Services_Cgit_Value",
        "Services_Compton": "pynix_os.services.__options__:Services_Compton",
        "Services_Fedimintd_Value": "pynix_os.services.__options__:Services_Fedimintd_Value",
        "Services_Fedimintd_Value_NginxConfig": "pynix_os.services.__options__:Services_Fedimintd_Value_NginxConfig",
        "Services_Fedimintd_Value_NginxConfig_Listen_Item": "pynix_os.services.__options__:Services_Fedimintd_Value_NginxConfig_Listen_Item",
        "Services_Fedimintd_Value_NginxConfig_Locations_Value": "pynix_os.services.__options__:Services_Fedimintd_Value_NginxConfig_Locations_Value",
        "Services_Geth_Value": "pynix_os.services.__options__:Services_Geth_Value",
        "Services_GithubRunners_Value": "pynix_os.services.__options__:Services_GithubRunners_Value",
        "Services_GithubRunners_Value_GithubApp": "pynix_os.services.__options__:Services_GithubRunners_Value_GithubApp",
        "Services_GithubRunners_Value_Orgs_Value": "pynix_os.services.__options__:Services_GithubRunners_Value_Orgs_Value",
        "Services_Gitwatch_Value": "pynix_os.services.__options__:Services_Gitwatch_Value",
        "Services_Invoiceplane": "pynix_os.services.__options__:Services_Invoiceplane",
        "Services_Invoiceplane_Sites_Value": "pynix_os.services.__options__:Services_Invoiceplane_Sites_Value",
        "Services_NixStoreGcsProxy_Value": "pynix_os.services.__options__:Services_NixStoreGcsProxy_Value",
        "Services_Nylon_Value": "pynix_os.services.__options__:Services_Nylon_Value",
        "Services_Quicktun_Value": "pynix_os.services.__options__:Services_Quicktun_Value",
        "Services_Uhub_Value": "pynix_os.services.__options__:Services_Uhub_Value",
        "Services_Uhub_Value_Plugins_Item": "pynix_os.services.__options__:Services_Uhub_Value_Plugins_Item",
        "Serviio": "pynix_os.services.serviio:Serviio",
        "Settings": "pynix_os.systemd.settings:Settings",
        "Settings_Manager": "pynix_os.systemd.settings:Settings_Manager",
        "Sftpgo": "pynix_os.services.sftpgo:Sftpgo",
        "Sftpgo_Settings": "pynix_os.services.sftpgo:Sftpgo_Settings",
        "Sftpgo_Settings_FtpdBindings_Item": "pynix_os.services.sftpgo:Sftpgo_Settings_FtpdBindings_Item",
        "Sftpgo_Settings_HttpdBindings_Item": "pynix_os.services.sftpgo:Sftpgo_Settings_HttpdBindings_Item",
        "Sftpgo_Settings_SftpdBindings_Item": "pynix_os.services.sftpgo:Sftpgo_Settings_SftpdBindings_Item",
        "Sftpgo_Settings_Smtp": "pynix_os.services.sftpgo:Sftpgo_Settings_Smtp",
        "Sftpgo_Settings_WebdavdBindings_Item": "pynix_os.services.sftpgo:Sftpgo_Settings_WebdavdBindings_Item",
        "Shadow": "pynix_os.security.shadow:Shadow",
        "Shadow_Su": "pynix_os.security.shadow:Shadow_Su",
        "Shadowsocks": "pynix_os.services.shadowsocks:Shadowsocks",
        "ShairportSync": "pynix_os.services.shairport_sync:ShairportSync",
        "Sharing": "pynix_os.programs.sharing:Sharing",
        "Sharkey": "pynix_os.services.sharkey:Sharkey",
        "Sharkey_Settings": "pynix_os.services.sharkey:Sharkey_Settings",
        "SheepNet": "pynix_os.hardware.sheep_net:SheepNet",
        "Shelfmark": "pynix_os.services.shelfmark:Shelfmark",
        "Shelfmark_Environment": "pynix_os.services.shelfmark:Shelfmark_Environment",
        "Shell": "pynix_os.environment.shell:Shell",
        "ShellhubAgent": "pynix_os.services.shellhub_agent:ShellhubAgent",
        "ShibbolethSp": "pynix_os.services.shibboleth_sp:ShibbolethSp",
        "ShibbolethSp_Fastcgi": "pynix_os.services.shibboleth_sp:ShibbolethSp_Fastcgi",
        "Shiori": "pynix_os.services.shiori:Shiori",
        "Shoko": "pynix_os.services.shoko:Shoko",
        "Shorewall": "pynix_os.services.shorewall:Shorewall",
        "Shorewall6": "pynix_os.services.shorewall6:Shorewall6",
        "ShutdownRamfs": "pynix_os.systemd.shutdownRamfs:ShutdownRamfs",
        "ShutdownRamfs_Contents_Value": "pynix_os.systemd.shutdownRamfs:ShutdownRamfs_Contents_Value",
        "ShutdownRamfs_Shell": "pynix_os.systemd.shutdownRamfs:ShutdownRamfs_Shell",
        "ShutdownRamfs_StorePaths_Item": "pynix_os.systemd.shutdownRamfs:ShutdownRamfs_StorePaths_Item",
        "Sillytavern": "pynix_os.services.sillytavern:Sillytavern",
        "Silverbullet": "pynix_os.services.silverbullet:Silverbullet",
        "SingBox": "pynix_os.services.sing_box:SingBox",
        "SingBox_Settings": "pynix_os.services.sing_box:SingBox_Settings",
        "Singularity": "pynix_os.programs.singularity:Singularity",
        "SitespeedIo": "pynix_os.services.sitespeed_io:SitespeedIo",
        "SitespeedIo_Runs_Item": "pynix_os.services.sitespeed_io:SitespeedIo_Runs_Item",
        "SitespeedIo_Runs_Item_Settings": "pynix_os.services.sitespeed_io:SitespeedIo_Runs_Item_Settings",
        "Skim": "pynix_os.programs.skim:Skim",
        "Sks": "pynix_os.services.sks:Sks",
        "Skydns": "pynix_os.services.skydns:Skydns",
        "Skydns_Etcd": "pynix_os.services.skydns:Skydns_Etcd",
        "Sleep": "pynix_os.systemd.sleep:Sleep",
        "Sleep_Settings": "pynix_os.systemd.sleep:Sleep_Settings",
        "Sleep_Settings_Sleep": "pynix_os.systemd.sleep:Sleep_Settings_Sleep",
        "Slimserver": "pynix_os.services.slimserver:Slimserver",
        "Slock": "pynix_os.programs.slock:Slock",
        "Slskd": "pynix_os.services.slskd:Slskd",
        "Slskd_Nginx": "pynix_os.services.slskd:Slskd_Nginx",
        "Slskd_Nginx_Listen_Item": "pynix_os.services.slskd:Slskd_Nginx_Listen_Item",
        "Slskd_Nginx_Locations_Value": "pynix_os.services.slskd:Slskd_Nginx_Locations_Value",
        "Slskd_Settings": "pynix_os.services.slskd:Slskd_Settings",
        "Slurm": "pynix_os.services.slurm:Slurm",
        "Slurm_Client": "pynix_os.services.slurm:Slurm_Client",
        "Slurm_Dbdserver": "pynix_os.services.slurm:Slurm_Dbdserver",
        "Slurm_Mpi": "pynix_os.services.slurm:Slurm_Mpi",
        "Slurm_Rest": "pynix_os.services.slurm:Slurm_Rest",
        "Slurm_Rest_Environment": "pynix_os.services.slurm:Slurm_Rest_Environment",
        "Slurm_Server": "pynix_os.services.slurm:Slurm_Server",
        "Smartd": "pynix_os.services.smartd:Smartd",
        "Smartd_Defaults": "pynix_os.services.smartd:Smartd_Defaults",
        "Smartd_Devices_Item": "pynix_os.services.smartd:Smartd_Devices_Item",
        "Smartd_Notifications": "pynix_os.services.smartd:Smartd_Notifications",
        "Smartd_Notifications_Mail": "pynix_os.services.smartd:Smartd_Notifications_Mail",
        "Smartd_Notifications_SystembusNotify": "pynix_os.services.smartd:Smartd_Notifications_SystembusNotify",
        "Smartd_Notifications_Wall": "pynix_os.services.smartd:Smartd_Notifications_Wall",
        "Smartd_Notifications_X11": "pynix_os.services.smartd:Smartd_Notifications_X11",
        "Smartdns": "pynix_os.services.smartdns:Smartdns",
        "Smokeping": "pynix_os.services.smokeping:Smokeping",
        "Snapper": "pynix_os.services.snapper:Snapper",
        "Snapper_Configs_Value": "pynix_os.services.snapper:Snapper_Configs_Value",
        "Snapraid": "pynix_os.services.snapraid:Snapraid",
        "Snapraid_Scrub": "pynix_os.services.snapraid:Snapraid_Scrub",
        "Snapraid_Sync": "pynix_os.services.snapraid:Snapraid_Sync",
        "Snapserver": "pynix_os.services.snapserver:Snapserver",
        "Snapserver_Settings": "pynix_os.services.snapserver:Snapserver_Settings",
        "Sniffnet": "pynix_os.programs.sniffnet:Sniffnet",
        "SnipeIt": "pynix_os.services.snipe_it:SnipeIt",
        "SnipeIt_Config_Value_Or": "pynix_os.services.snipe_it:SnipeIt_Config_Value_Or",
        "SnipeIt_Database": "pynix_os.services.snipe_it:SnipeIt_Database",
        "SnipeIt_Mail": "pynix_os.services.snipe_it:SnipeIt_Mail",
        "SnipeIt_Mail_From": "pynix_os.services.snipe_it:SnipeIt_Mail_From",
        "SnipeIt_Mail_ReplyTo": "pynix_os.services.snipe_it:SnipeIt_Mail_ReplyTo",
        "SnipeIt_Nginx": "pynix_os.services.snipe_it:SnipeIt_Nginx",
        "SnipeIt_Nginx_Listen_Item": "pynix_os.services.snipe_it:SnipeIt_Nginx_Listen_Item",
        "SnipeIt_Nginx_Locations_Value": "pynix_os.services.snipe_it:SnipeIt_Nginx_Locations_Value",
        "Sniproxy": "pynix_os.services.sniproxy:Sniproxy",
        "SnipsSh": "pynix_os.services.snips_sh:SnipsSh",
        "SnipsSh_Settings": "pynix_os.services.snips_sh:SnipsSh_Settings",
        "Snmpd": "pynix_os.services.snmpd:Snmpd",
        "SnowflakeProxy": "pynix_os.services.snowflake_proxy:SnowflakeProxy",
        "SoftServe": "pynix_os.services.soft_serve:SoftServe",
        "Softether": "pynix_os.services.softether:Softether",
        "Softether_Vpnbridge": "pynix_os.services.softether:Softether_Vpnbridge",
        "Softether_Vpnclient": "pynix_os.services.softether:Softether_Vpnclient",
        "Softether_Vpnserver": "pynix_os.services.softether:Softether_Vpnserver",
        "Sogo": "pynix_os.services.sogo:Sogo",
        "Soju": "pynix_os.services.soju:Soju",
        "Soju_AdminSocket": "pynix_os.services.soju:Soju_AdminSocket",
        "Solaar": "pynix_os.programs.solaar:Solaar",
        "Solaar_UserService": "pynix_os.programs.solaar:Solaar_UserService",
        "Solanum": "pynix_os.services.solanum:Solanum",
        "Sonarr": "pynix_os.services.sonarr:Sonarr",
        "Sonarr_Settings": "pynix_os.services.sonarr:Sonarr_Settings",
        "SonicServer": "pynix_os.services.sonic_server:SonicServer",
        "SonicServer_Settings": "pynix_os.services.sonic_server:SonicServer_Settings",
        "Soteria": "pynix_os.security.soteria:Soteria",
        "Soundmodem": "pynix_os.programs.soundmodem:Soundmodem",
        "Sounds": "pynix_os.xdg.sounds:Sounds",
        "Spacecookie": "pynix_os.services.spacecookie:Spacecookie",
        "Spacecookie_Settings": "pynix_os.services.spacecookie:Spacecookie_Settings",
        "Spacenavd": "pynix_os.hardware.spacenavd:Spacenavd",
        "Spamassassin": "pynix_os.services.spamassassin:Spamassassin",
        "Spark": "pynix_os.services.spark:Spark",
        "Spark_Master": "pynix_os.services.spark:Spark_Master",
        "Spark_Worker": "pynix_os.services.spark:Spark_Worker",
        "Speechd": "pynix_os.services.speechd:Speechd",
        "Speechd_Clients": "pynix_os.services.speechd:Speechd_Clients",
        "Speechd_Modules": "pynix_os.services.speechd:Speechd_Modules",
        "Speedify": "pynix_os.services.speedify:Speedify",
        "SpeedtestTracker": "pynix_os.services.speedtest_tracker:SpeedtestTracker",
        "SpeedtestTracker_Settings": "pynix_os.services.speedtest_tracker:SpeedtestTracker_Settings",
        "SpiceAutorandr": "pynix_os.services.spice_autorandr:SpiceAutorandr",
        "SpiceUSBRedirection": "pynix_os.virtualisation.spiceUSBRedirection:SpiceUSBRedirection",
        "SpiceVdagentd": "pynix_os.services.spice_vdagentd:SpiceVdagentd",
        "SpiceWebdavd": "pynix_os.services.spice_webdavd:SpiceWebdavd",
        "Spiped": "pynix_os.services.spiped:Spiped",
        "Spiped_Config_Value": "pynix_os.services.spiped:Spiped_Config_Value",
        "Spire": "pynix_os.services.spire:Spire",
        "Spire_Agent": "pynix_os.services.spire:Spire_Agent",
        "Spire_Agent_Settings": "pynix_os.services.spire:Spire_Agent_Settings",
        "Spire_Agent_Settings_Plugins": "pynix_os.services.spire:Spire_Agent_Settings_Plugins",
        "Spire_Agent_Settings_Plugins_NodeAttestor": "pynix_os.services.spire:Spire_Agent_Settings_Plugins_NodeAttestor",
        "Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken": "pynix_os.services.spire:Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken",
        "Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken_PluginData": "pynix_os.services.spire:Spire_Agent_Settings_Plugins_NodeAttestor_JoinToken_PluginData",
        "Spire_Agent_Settings_Plugins_NodeAttestor_Tpm": "pynix_os.services.spire:Spire_Agent_Settings_Plugins_NodeAttestor_Tpm",
        "Spire_Server": "pynix_os.services.spire:Spire_Server",
        "Spire_Server_Settings": "pynix_os.services.spire:Spire_Server_Settings",
        "Spire_Server_Settings_Plugins": "pynix_os.services.spire:Spire_Server_Settings_Plugins",
        "Spire_Server_Settings_Plugins_NodeAttestor": "pynix_os.services.spire:Spire_Server_Settings_Plugins_NodeAttestor",
        "Spire_Server_Settings_Plugins_NodeAttestor_JoinToken": "pynix_os.services.spire:Spire_Server_Settings_Plugins_NodeAttestor_JoinToken",
        "Spire_Server_Settings_Plugins_NodeAttestor_Tpm": "pynix_os.services.spire:Spire_Server_Settings_Plugins_NodeAttestor_Tpm",
        "Spire_Server_Settings_Plugins_NodeAttestor_Tpm_PluginData": "pynix_os.services.spire:Spire_Server_Settings_Plugins_NodeAttestor_Tpm_PluginData",
        "Spoolman": "pynix_os.services.spoolman:Spoolman",
        "Spotifyd": "pynix_os.services.spotifyd:Spotifyd",
        "Squeezelite": "pynix_os.services.squeezelite:Squeezelite",
        "Squeezelite_Pulseaudio": "pynix_os.services.squeezelite:Squeezelite_Pulseaudio",
        "Squid": "pynix_os.services.squid:Squid",
        "Ssh": "pynix_os.programs.ssh:Ssh",
        "SshAgentSwitcher": "pynix_os.services.ssh_agent_switcher:SshAgentSwitcher",
        "SshServe": "pynix_os.nix.sshServe:SshServe",
        "Ssh_KnownHosts_Value": "pynix_os.programs.ssh:Ssh_KnownHosts_Value",
        "Ssh_SystemdSshProxy": "pynix_os.programs.ssh:Ssh_SystemdSshProxy",
        "Sshd": "pynix_os.services.sshd:Sshd",
        "Sshguard": "pynix_os.services.sshguard:Sshguard",
        "Sshwifty": "pynix_os.services.sshwifty:Sshwifty",
        "Sslh": "pynix_os.services.sslh:Sslh",
        "Sslh_Settings": "pynix_os.services.sslh:Sslh_Settings",
        "SslmateAgent": "pynix_os.services.sslmate_agent:SslmateAgent",
        "Sssd": "pynix_os.services.sssd:Sssd",
        "Sstorytime": "pynix_os.services.sstorytime:Sstorytime",
        "Sstorytime_Database": "pynix_os.services.sstorytime:Sstorytime_Database",
        "Sstorytime_Settings": "pynix_os.services.sstorytime:Sstorytime_Settings",
        "Stalwart": "pynix_os.services.stalwart:Stalwart",
        "Stargazer": "pynix_os.services.stargazer:Stargazer",
        "Stargazer_Routes_Item": "pynix_os.services.stargazer:Stargazer_Routes_Item",
        "Starship": "pynix_os.programs.starship:Starship",
        "Starship_TransientPrompt": "pynix_os.programs.starship:Starship_TransientPrompt",
        "Stash": "pynix_os.services.stash:Stash",
        "StashClipboard": "pynix_os.services.stash_clipboard:StashClipboard",
        "Stash_Settings": "pynix_os.services.stash:Stash_Settings",
        "Stash_Settings_StashBoxes_Item": "pynix_os.services.stash:Stash_Settings_StashBoxes_Item",
        "Stash_Settings_Stash_Item": "pynix_os.services.stash:Stash_Settings_Stash_Item",
        "StaticWebServer": "pynix_os.services.static_web_server:StaticWebServer",
        "Steam": "pynix_os.programs.steam:Steam",
        "SteamHardware": "pynix_os.hardware.steam_hardware:SteamHardware",
        "Steam_DedicatedServer": "pynix_os.programs.steam:Steam_DedicatedServer",
        "Steam_Extest": "pynix_os.programs.steam:Steam_Extest",
        "Steam_GamescopeSession": "pynix_os.programs.steam:Steam_GamescopeSession",
        "Steam_LocalNetworkGameTransfers": "pynix_os.programs.steam:Steam_LocalNetworkGameTransfers",
        "Steam_Protontricks": "pynix_os.programs.steam:Steam_Protontricks",
        "Steam_RemotePlay": "pynix_os.programs.steam:Steam_RemotePlay",
        "StepCa": "pynix_os.services.step_ca:StepCa",
        "Stevenblack": "pynix_os.networking.stevenblack:Stevenblack",
        "StirlingPdf": "pynix_os.services.stirling_pdf:StirlingPdf",
        "Stratis": "pynix_os.services.stratis:Stratis",
        "Streamcontroller": "pynix_os.programs.streamcontroller:Streamcontroller",
        "StreamdeckUi": "pynix_os.programs.streamdeck_ui:StreamdeckUi",
        "Strfry": "pynix_os.services.strfry:Strfry",
        "Strichliste": "pynix_os.services.strichliste:Strichliste",
        "Strichliste_Environment": "pynix_os.services.strichliste:Strichliste_Environment",
        "Strichliste_Nginx": "pynix_os.services.strichliste:Strichliste_Nginx",
        "Strichliste_Nginx_VirtualHost": "pynix_os.services.strichliste:Strichliste_Nginx_VirtualHost",
        "Strichliste_Nginx_VirtualHost_Listen_Item": "pynix_os.services.strichliste:Strichliste_Nginx_VirtualHost_Listen_Item",
        "Strichliste_Nginx_VirtualHost_Locations_Value": "pynix_os.services.strichliste:Strichliste_Nginx_VirtualHost_Locations_Value",
        "Strichliste_Packages": "pynix_os.services.strichliste:Strichliste_Packages",
        "Strichliste_Settings": "pynix_os.services.strichliste:Strichliste_Settings",
        "Strongswan": "pynix_os.services.strongswan:Strongswan",
        "StrongswanSwanctl": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl",
        "StrongswanSwanctl_Strongswan": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Strongswan",
        "StrongswanSwanctl_Swanctl": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl",
        "StrongswanSwanctl_Swanctl_Authorities_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Authorities_Value",
        "StrongswanSwanctl_Swanctl_Connections_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Connections_Value",
        "StrongswanSwanctl_Swanctl_Connections_Value_Children_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Connections_Value_Children_Value",
        "StrongswanSwanctl_Swanctl_Connections_Value_Local_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Connections_Value_Local_Value",
        "StrongswanSwanctl_Swanctl_Connections_Value_Local_Value_Cert_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Connections_Value_Local_Value_Cert_Value",
        "StrongswanSwanctl_Swanctl_Connections_Value_Remote_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Connections_Value_Remote_Value",
        "StrongswanSwanctl_Swanctl_Pools_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Pools_Value",
        "StrongswanSwanctl_Swanctl_Secrets": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets",
        "StrongswanSwanctl_Swanctl_Secrets_Eap_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Eap_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Ecdsa_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Ecdsa_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Ike_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Ike_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Ntlm_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Ntlm_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Pkcs12_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Pkcs12_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Pkcs8_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Pkcs8_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Ppk_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Ppk_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Private_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Private_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Rsa_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Rsa_Value",
        "StrongswanSwanctl_Swanctl_Secrets_Token_Value": "pynix_os.services.strongswan_swanctl:StrongswanSwanctl_Swanctl_Secrets_Token_Value",
        "StubLd": "pynix_os.environment.stub_ld:StubLd",
        "Stubby": "pynix_os.services.stubby:Stubby",
        "Stump": "pynix_os.services.stump:Stump",
        "Stunnel": "pynix_os.services.stunnel:Stunnel",
        "Subsonic": "pynix_os.services.subsonic:Subsonic",
        "Sudo": "pynix_os.security.sudo:Sudo",
        "SudoRs": "pynix_os.security.sudo_rs:SudoRs",
        "SudoRs_ExtraRules_Item": "pynix_os.security.sudo_rs:SudoRs_ExtraRules_Item",
        "SudoRs_ExtraRules_Item_Commands_Item_Or": "pynix_os.security.sudo_rs:SudoRs_ExtraRules_Item_Commands_Item_Or",
        "Sudo_ExtraRules_Item": "pynix_os.security.sudo:Sudo_ExtraRules_Item",
        "Sudo_ExtraRules_Item_Commands_Item_Or": "pynix_os.security.sudo:Sudo_ExtraRules_Item_Commands_Item_Or",
        "Sundtek": "pynix_os.services.sundtek:Sundtek",
        "Sunshine": "pynix_os.services.sunshine:Sunshine",
        "Sunshine_Applications": "pynix_os.services.sunshine:Sunshine_Applications",
        "Sunshine_Settings": "pynix_os.services.sunshine:Sunshine_Settings",
        "Supergfxd": "pynix_os.services.supergfxd:Supergfxd",
        "Supybot": "pynix_os.services.supybot:Supybot",
        "Suricata": "pynix_os.services.suricata:Suricata",
        "Suricata_Settings": "pynix_os.services.suricata:Suricata_Settings",
        "Suricata_Settings_AfPacket_Item": "pynix_os.services.suricata:Suricata_Settings_AfPacket_Item",
        "Suricata_Settings_AfXdp_Item": "pynix_os.services.suricata:Suricata_Settings_AfXdp_Item",
        "Suricata_Settings_AppLayer": "pynix_os.services.suricata:Suricata_Settings_AppLayer",
        "Suricata_Settings_AppLayer_Protocols_Value": "pynix_os.services.suricata:Suricata_Settings_AppLayer_Protocols_Value",
        "Suricata_Settings_Dpdk": "pynix_os.services.suricata:Suricata_Settings_Dpdk",
        "Suricata_Settings_Dpdk_Interfaces_Item": "pynix_os.services.suricata:Suricata_Settings_Dpdk_Interfaces_Item",
        "Suricata_Settings_Outputs_Item_Value": "pynix_os.services.suricata:Suricata_Settings_Outputs_Item_Value",
        "Suricata_Settings_Pcap_Item": "pynix_os.services.suricata:Suricata_Settings_Pcap_Item",
        "Suricata_Settings_Stats": "pynix_os.services.suricata:Suricata_Settings_Stats",
        "Suricata_Settings_UnixCommand": "pynix_os.services.suricata:Suricata_Settings_UnixCommand",
        "Suricata_Settings_Vars": "pynix_os.services.suricata:Suricata_Settings_Vars",
        "Suricata_Settings_Vars_AddressGroups": "pynix_os.services.suricata:Suricata_Settings_Vars_AddressGroups",
        "Surrealdb": "pynix_os.services.surrealdb:Surrealdb",
        "SuwayomiServer": "pynix_os.services.suwayomi_server:SuwayomiServer",
        "SuwayomiServer_Settings": "pynix_os.services.suwayomi_server:SuwayomiServer_Settings",
        "Svnserve": "pynix_os.services.svnserve:Svnserve",
        "Swapspace": "pynix_os.services.swapspace:Swapspace",
        "Swapspace_Settings": "pynix_os.services.swapspace:Swapspace_Settings",
        "Sway": "pynix_os.programs.sway:Sway",
        "Sway_WrapperFeatures": "pynix_os.programs.sway:Sway_WrapperFeatures",
        "Sway_Xwayland": "pynix_os.programs.sway:Sway_Xwayland",
        "Switch": "pynix_os.system.switch:Switch",
        "SwitcherooControl": "pynix_os.services.switcherooControl:SwitcherooControl",
        "Swraid": "pynix_os.boot.swraid:Swraid",
        "Sympa": "pynix_os.services.sympa:Sympa",
        "Sympa_Domains_Value": "pynix_os.services.sympa:Sympa_Domains_Value",
        "Sympa_SettingsFile_Value": "pynix_os.services.sympa:Sympa_SettingsFile_Value",
        "Sympa_Web": "pynix_os.services.sympa:Sympa_Web",
        "SynapseAutoCompressor": "pynix_os.services.synapse_auto_compressor:SynapseAutoCompressor",
        "SynapseAutoCompressor_Settings": "pynix_os.services.synapse_auto_compressor:SynapseAutoCompressor_Settings",
        "Syncoid": "pynix_os.services.syncoid:Syncoid",
        "Syncoid_Commands_Value": "pynix_os.services.syncoid:Syncoid_Commands_Value",
        "Syncplay": "pynix_os.services.syncplay:Syncplay",
        "Syncthing": "pynix_os.services.syncthing:Syncthing",
        "Syncthing_Relay": "pynix_os.services.syncthing:Syncthing_Relay",
        "Syncthing_Settings": "pynix_os.services.syncthing:Syncthing_Settings",
        "Syncthing_Settings_Devices_Value": "pynix_os.services.syncthing:Syncthing_Settings_Devices_Value",
        "Syncthing_Settings_Folders_Value": "pynix_os.services.syncthing:Syncthing_Settings_Folders_Value",
        "Syncthing_Settings_Folders_Value_Devices_Item_Or": "pynix_os.services.syncthing:Syncthing_Settings_Folders_Value_Devices_Item_Or",
        "Syncthing_Settings_Folders_Value_Versioning": "pynix_os.services.syncthing:Syncthing_Settings_Folders_Value_Versioning",
        "Syncthing_Settings_Options": "pynix_os.services.syncthing:Syncthing_Settings_Options",
        "Synergy": "pynix_os.services.synergy:Synergy",
        "Synergy_Client": "pynix_os.services.synergy:Synergy_Client",
        "Synergy_Server": "pynix_os.services.synergy:Synergy_Server",
        "Synergy_Server_Tls": "pynix_os.services.synergy:Synergy_Server_Tls",
        "Sysdig": "pynix_os.programs.sysdig:Sysdig",
        "SyslogNg": "pynix_os.services.syslog_ng:SyslogNg",
        "Syslogd": "pynix_os.services.syslogd:Syslogd",
        "Sysprof": "pynix_os.services.sysprof:Sysprof",
        "Sysstat": "pynix_os.services.sysstat:Sysstat",
        "System": "pynix_os.system.__options__:System",
        "System76": "pynix_os.hardware.system76:System76",
        "System76Scheduler": "pynix_os.services.system76_scheduler:System76Scheduler",
        "System76Scheduler_Assignments_Value": "pynix_os.services.system76_scheduler:System76Scheduler_Assignments_Value",
        "System76Scheduler_Settings": "pynix_os.services.system76_scheduler:System76Scheduler_Settings",
        "System76Scheduler_Settings_CfsProfiles": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_CfsProfiles",
        "System76Scheduler_Settings_CfsProfiles_Default": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_CfsProfiles_Default",
        "System76Scheduler_Settings_CfsProfiles_Responsive": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_CfsProfiles_Responsive",
        "System76Scheduler_Settings_ProcessScheduler": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_ProcessScheduler",
        "System76Scheduler_Settings_ProcessScheduler_ForegroundBoost": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_ProcessScheduler_ForegroundBoost",
        "System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Background": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Background",
        "System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Foreground": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_ProcessScheduler_ForegroundBoost_Foreground",
        "System76Scheduler_Settings_ProcessScheduler_PipewireBoost": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_ProcessScheduler_PipewireBoost",
        "System76Scheduler_Settings_ProcessScheduler_PipewireBoost_Profile": "pynix_os.services.system76_scheduler:System76Scheduler_Settings_ProcessScheduler_PipewireBoost_Profile",
        "System76_FirmwareDaemon": "pynix_os.hardware.system76:System76_FirmwareDaemon",
        "System76_KernelModules": "pynix_os.hardware.system76:System76_KernelModules",
        "System76_PowerDaemon": "pynix_os.hardware.system76:System76_PowerDaemon",
        "Programs_SystemConfigPrinter": "pynix_os.programs.system_config_printer:SystemConfigPrinter",
        "Services_SystemConfigPrinter": "pynix_os.services.system_config_printer:SystemConfigPrinter",
        "System_ActivationScripts_Value_Or": "pynix_os.system.__options__:System_ActivationScripts_Value_Or",
        "System_Build": "pynix_os.system.__options__:System_Build",
        "System_Services_Value": "pynix_os.system.__options__:System_Services_Value",
        "System_Services_Value_ConfigData_Value": "pynix_os.system.__options__:System_Services_Value_ConfigData_Value",
        "System_Services_Value_NotificationProtocol": "pynix_os.system.__options__:System_Services_Value_NotificationProtocol",
        "System_Services_Value_Services_Value": "pynix_os.system.__options__:System_Services_Value_Services_Value",
        "System_Services_Value_SystemdService": "pynix_os.system.__options__:System_Services_Value_SystemdService",
        "System_Services_Value_SystemdServices_Value": "pynix_os.system.__options__:System_Services_Value_SystemdServices_Value",
        "System_UserActivationScripts_Value_Or": "pynix_os.system.__options__:System_UserActivationScripts_Value_Or",
        "SystembusNotify": "pynix_os.services.systembus_notify:SystembusNotify",
        "Systemd": "pynix_os.systemd.__options__:Systemd",
        "SystemdJournal2Gelf": "pynix_os.services.SystemdJournal2Gelf:SystemdJournal2Gelf",
        "SystemdLockHandler": "pynix_os.services.systemd_lock_handler:SystemdLockHandler",
        "Systemd_Automounts_Item": "pynix_os.systemd.__options__:Systemd_Automounts_Item",
        "Systemd_Mounts_Item": "pynix_os.systemd.__options__:Systemd_Mounts_Item",
        "Systemd_Nspawn_Value": "pynix_os.systemd.__options__:Systemd_Nspawn_Value",
        "Systemd_Paths_Value": "pynix_os.systemd.__options__:Systemd_Paths_Value",
        "Systemd_Services_Value": "pynix_os.systemd.__options__:Systemd_Services_Value",
        "Systemd_Slices_Value": "pynix_os.systemd.__options__:Systemd_Slices_Value",
        "Systemd_Sockets_Value": "pynix_os.systemd.__options__:Systemd_Sockets_Value",
        "Systemd_Targets_Value": "pynix_os.systemd.__options__:Systemd_Targets_Value",
        "Systemd_Timers_Value": "pynix_os.systemd.__options__:Systemd_Timers_Value",
        "Systemd_Units_Value": "pynix_os.systemd.__options__:Systemd_Units_Value",
        "Systemtap": "pynix_os.programs.systemtap:Systemtap",
        "Sysupdate": "pynix_os.systemd.sysupdate:Sysupdate",
        "Sysupdate_Reboot": "pynix_os.systemd.sysupdate:Sysupdate_Reboot",
        "Sysusers": "pynix_os.systemd.sysusers:Sysusers",
        "Szurubooru": "pynix_os.services.szurubooru:Szurubooru",
        "Szurubooru_Client": "pynix_os.services.szurubooru:Szurubooru_Client",
        "Szurubooru_Database": "pynix_os.services.szurubooru:Szurubooru_Database",
        "Szurubooru_Server": "pynix_os.services.szurubooru:Szurubooru_Server",
        "Szurubooru_Server_Settings": "pynix_os.services.szurubooru:Szurubooru_Server_Settings",
        "Tabby": "pynix_os.services.tabby:Tabby",
        "Tabbyapi": "pynix_os.services.tabbyapi:Tabbyapi",
        "Tabbyapi_Settings": "pynix_os.services.tabbyapi:Tabbyapi_Settings",
        "Tabbyapi_Settings_LoraLoras_Item": "pynix_os.services.tabbyapi:Tabbyapi_Settings_LoraLoras_Item",
        "Tack": "pynix_os.programs.tack:Tack",
        "Tahoe": "pynix_os.services.tahoe:Tahoe",
        "Tahoe_Introducers_Value": "pynix_os.services.tahoe:Tahoe_Introducers_Value",
        "Tahoe_Nodes_Value": "pynix_os.services.tahoe:Tahoe_Nodes_Value",
        "Tailscale": "pynix_os.services.tailscale:Tailscale",
        "TailscaleAuth": "pynix_os.services.tailscaleAuth:TailscaleAuth",
        "Tailscale_AuthKeyParameters": "pynix_os.services.tailscale:Tailscale_AuthKeyParameters",
        "Tailscale_Derper": "pynix_os.services.tailscale:Tailscale_Derper",
        "Tailscale_Serve": "pynix_os.services.tailscale:Tailscale_Serve",
        "Tailscale_Serve_Services_Value": "pynix_os.services.tailscale:Tailscale_Serve_Services_Value",
        "Taler": "pynix_os.services.taler:Taler",
        "Taler_Exchange": "pynix_os.services.taler:Taler_Exchange",
        "Taler_Exchange_Settings": "pynix_os.services.taler:Taler_Exchange_Settings",
        "Taler_Merchant": "pynix_os.services.taler:Taler_Merchant",
        "Taler_Merchant_Settings": "pynix_os.services.taler:Taler_Merchant_Settings",
        "Taler_Settings": "pynix_os.services.taler:Taler_Settings",
        "TandoorRecipes": "pynix_os.services.tandoor_recipes:TandoorRecipes",
        "TandoorRecipes_Database": "pynix_os.services.tandoor_recipes:TandoorRecipes_Database",
        "Tang": "pynix_os.services.tang:Tang",
        "Tap": "pynix_os.services.tap:Tap",
        "Tap_Settings": "pynix_os.services.tap:Tap_Settings",
        "Target": "pynix_os.services.target:Target",
        "Tarsnap": "pynix_os.services.tarsnap:Tarsnap",
        "Tarsnap_Archives_Value": "pynix_os.services.tarsnap:Tarsnap_Archives_Value",
        "TaskchampionSyncServer": "pynix_os.services.taskchampion_sync_server:TaskchampionSyncServer",
        "TaskchampionSyncServer_Snapshot": "pynix_os.services.taskchampion_sync_server:TaskchampionSyncServer_Snapshot",
        "Taskserver": "pynix_os.services.taskserver:Taskserver",
        "Taskserver_Organisations_Value": "pynix_os.services.taskserver:Taskserver_Organisations_Value",
        "Taskserver_Pki": "pynix_os.services.taskserver:Taskserver_Pki",
        "Taskserver_Pki_Auto": "pynix_os.services.taskserver:Taskserver_Pki_Auto",
        "Taskserver_Pki_Auto_Expiration": "pynix_os.services.taskserver:Taskserver_Pki_Auto_Expiration",
        "Taskserver_Pki_Manual": "pynix_os.services.taskserver:Taskserver_Pki_Manual",
        "Taskserver_Pki_Manual_Ca": "pynix_os.services.taskserver:Taskserver_Pki_Manual_Ca",
        "Taskserver_Pki_Manual_Server": "pynix_os.services.taskserver:Taskserver_Pki_Manual_Server",
        "Tautulli": "pynix_os.services.tautulli:Tautulli",
        "Tayga": "pynix_os.services.tayga:Tayga",
        "Tayga_Ipv4": "pynix_os.services.tayga:Tayga_Ipv4",
        "Tayga_Ipv4_Pool": "pynix_os.services.tayga:Tayga_Ipv4_Pool",
        "Tayga_Ipv6": "pynix_os.services.tayga:Tayga_Ipv6",
        "Tayga_Ipv6_Pool": "pynix_os.services.tayga:Tayga_Ipv6_Pool",
        "Tcpcrypt": "pynix_os.networking.tcpcrypt:Tcpcrypt",
        "Tcpdump": "pynix_os.programs.tcpdump:Tcpdump",
        "Tcsd": "pynix_os.services.tcsd:Tcsd",
        "Tdarr": "pynix_os.services.tdarr:Tdarr",
        "Tdarr_Nodes_Value": "pynix_os.services.tdarr:Tdarr_Nodes_Value",
        "Tdarr_Nodes_Value_PathTranslators_Item": "pynix_os.services.tdarr:Tdarr_Nodes_Value_PathTranslators_Item",
        "Tdarr_Server": "pynix_os.services.tdarr:Tdarr_Server",
        "Tdarr_Server_Auth": "pynix_os.services.tdarr:Tdarr_Server_Auth",
        "Teamspeak3": "pynix_os.services.teamspeak3:Teamspeak3",
        "Teamviewer": "pynix_os.services.teamviewer:Teamviewer",
        "TechnitiumDnsServer": "pynix_os.services.technitium_dns_server:TechnitiumDnsServer",
        "TeeSupplicant": "pynix_os.services.tee_supplicant:TeeSupplicant",
        "Teeworlds": "pynix_os.services.teeworlds:Teeworlds",
        "Teeworlds_Game": "pynix_os.services.teeworlds:Teeworlds_Game",
        "Teeworlds_Server": "pynix_os.services.teeworlds:Teeworlds_Server",
        "Telegraf": "pynix_os.services.telegraf:Telegraf",
        "Telepathy": "pynix_os.services.telepathy:Telepathy",
        "Teleport": "pynix_os.services.teleport:Teleport",
        "Teleport_Diag": "pynix_os.services.teleport:Teleport_Diag",
        "Teleport_Insecure": "pynix_os.services.teleport:Teleport_Insecure",
        "Television": "pynix_os.programs.television:Television",
        "Tempo": "pynix_os.services.tempo:Tempo",
        "Temporal": "pynix_os.services.temporal:Temporal",
        "Temporal_Settings": "pynix_os.services.temporal:Temporal_Settings",
        "Tenstorrent": "pynix_os.hardware.tenstorrent:Tenstorrent",
        "TerminalExec": "pynix_os.xdg.terminal_exec:TerminalExec",
        "Terraria": "pynix_os.services.terraria:Terraria",
        "Tetrd": "pynix_os.services.tetrd:Tetrd",
        "Tftpd": "pynix_os.services.tftpd:Tftpd",
        "Thanos": "pynix_os.services.thanos:Thanos",
        "Thanos_Compact": "pynix_os.services.thanos:Thanos_Compact",
        "Thanos_Compact_Compact": "pynix_os.services.thanos:Thanos_Compact_Compact",
        "Thanos_Compact_Downsampling": "pynix_os.services.thanos:Thanos_Compact_Downsampling",
        "Thanos_Compact_Log": "pynix_os.services.thanos:Thanos_Compact_Log",
        "Thanos_Compact_Objstore": "pynix_os.services.thanos:Thanos_Compact_Objstore",
        "Thanos_Compact_Retention": "pynix_os.services.thanos:Thanos_Compact_Retention",
        "Thanos_Compact_Tracing": "pynix_os.services.thanos:Thanos_Compact_Tracing",
        "Thanos_Downsample": "pynix_os.services.thanos:Thanos_Downsample",
        "Thanos_Downsample_Log": "pynix_os.services.thanos:Thanos_Downsample_Log",
        "Thanos_Downsample_Objstore": "pynix_os.services.thanos:Thanos_Downsample_Objstore",
        "Thanos_Downsample_Tracing": "pynix_os.services.thanos:Thanos_Downsample_Tracing",
        "Thanos_Query": "pynix_os.services.thanos:Thanos_Query",
        "Thanos_QueryFrontend": "pynix_os.services.thanos:Thanos_QueryFrontend",
        "Thanos_QueryFrontend_Log": "pynix_os.services.thanos:Thanos_QueryFrontend_Log",
        "Thanos_QueryFrontend_QueryFrontend": "pynix_os.services.thanos:Thanos_QueryFrontend_QueryFrontend",
        "Thanos_QueryFrontend_Tracing": "pynix_os.services.thanos:Thanos_QueryFrontend_Tracing",
        "Thanos_Query_Log": "pynix_os.services.thanos:Thanos_Query_Log",
        "Thanos_Query_Query": "pynix_os.services.thanos:Thanos_Query_Query",
        "Thanos_Query_Store": "pynix_os.services.thanos:Thanos_Query_Store",
        "Thanos_Query_Tracing": "pynix_os.services.thanos:Thanos_Query_Tracing",
        "Thanos_Query_Web": "pynix_os.services.thanos:Thanos_Query_Web",
        "Thanos_Receive": "pynix_os.services.thanos:Thanos_Receive",
        "Thanos_Receive_Log": "pynix_os.services.thanos:Thanos_Receive_Log",
        "Thanos_Receive_Objstore": "pynix_os.services.thanos:Thanos_Receive_Objstore",
        "Thanos_Receive_Receive": "pynix_os.services.thanos:Thanos_Receive_Receive",
        "Thanos_Receive_RemoteWrite": "pynix_os.services.thanos:Thanos_Receive_RemoteWrite",
        "Thanos_Receive_Tracing": "pynix_os.services.thanos:Thanos_Receive_Tracing",
        "Thanos_Receive_Tsdb": "pynix_os.services.thanos:Thanos_Receive_Tsdb",
        "Thanos_Rule": "pynix_os.services.thanos:Thanos_Rule",
        "Thanos_Rule_Alert": "pynix_os.services.thanos:Thanos_Rule_Alert",
        "Thanos_Rule_Alertmanagers": "pynix_os.services.thanos:Thanos_Rule_Alertmanagers",
        "Thanos_Rule_Log": "pynix_os.services.thanos:Thanos_Rule_Log",
        "Thanos_Rule_Objstore": "pynix_os.services.thanos:Thanos_Rule_Objstore",
        "Thanos_Rule_Query": "pynix_os.services.thanos:Thanos_Rule_Query",
        "Thanos_Rule_Tracing": "pynix_os.services.thanos:Thanos_Rule_Tracing",
        "Thanos_Rule_Tsdb": "pynix_os.services.thanos:Thanos_Rule_Tsdb",
        "Thanos_Rule_Web": "pynix_os.services.thanos:Thanos_Rule_Web",
        "Thanos_Sidecar": "pynix_os.services.thanos:Thanos_Sidecar",
        "Thanos_Sidecar_Log": "pynix_os.services.thanos:Thanos_Sidecar_Log",
        "Thanos_Sidecar_Objstore": "pynix_os.services.thanos:Thanos_Sidecar_Objstore",
        "Thanos_Sidecar_Prometheus": "pynix_os.services.thanos:Thanos_Sidecar_Prometheus",
        "Thanos_Sidecar_Reloader": "pynix_os.services.thanos:Thanos_Sidecar_Reloader",
        "Thanos_Sidecar_Tracing": "pynix_os.services.thanos:Thanos_Sidecar_Tracing",
        "Thanos_Sidecar_Tsdb": "pynix_os.services.thanos:Thanos_Sidecar_Tsdb",
        "Thanos_Store": "pynix_os.services.thanos:Thanos_Store",
        "Thanos_Store_Log": "pynix_os.services.thanos:Thanos_Store_Log",
        "Thanos_Store_Objstore": "pynix_os.services.thanos:Thanos_Store_Objstore",
        "Thanos_Store_Store": "pynix_os.services.thanos:Thanos_Store_Store",
        "Thanos_Store_Store_Grpc": "pynix_os.services.thanos:Thanos_Store_Store_Grpc",
        "Thanos_Store_Store_Limits": "pynix_os.services.thanos:Thanos_Store_Store_Limits",
        "Thanos_Store_Tracing": "pynix_os.services.thanos:Thanos_Store_Tracing",
        "Thelounge": "pynix_os.services.thelounge:Thelounge",
        "Thermald": "pynix_os.services.thermald:Thermald",
        "Thinkfan": "pynix_os.services.thinkfan:Thinkfan",
        "Thinkfan_Fans_Item": "pynix_os.services.thinkfan:Thinkfan_Fans_Item",
        "Thinkfan_Sensors_Item": "pynix_os.services.thinkfan:Thinkfan_Sensors_Item",
        "Throne": "pynix_os.programs.throne:Throne",
        "Throne_TunMode": "pynix_os.programs.throne:Throne_TunMode",
        "Throttled": "pynix_os.services.throttled:Throttled",
        "Thunar": "pynix_os.programs.thunar:Thunar",
        "Thunderbird": "pynix_os.programs.thunderbird:Thunderbird",
        "Tiddlywiki": "pynix_os.services.tiddlywiki:Tiddlywiki",
        "Tigerbeetle": "pynix_os.services.tigerbeetle:Tigerbeetle",
        "Tika": "pynix_os.services.tika:Tika",
        "Time": "pynix_os.time.__options__:Time",
        "Timekpr": "pynix_os.services.timekpr:Timekpr",
        "Timesyncd": "pynix_os.services.timesyncd:Timesyncd",
        "Timesyncd_Settings": "pynix_os.services.timesyncd:Timesyncd_Settings",
        "Timesyncd_Settings_Time": "pynix_os.services.timesyncd:Timesyncd_Settings_Time",
        "Tinc": "pynix_os.services.tinc:Tinc",
        "Tinc_Networks_Value": "pynix_os.services.tinc:Tinc_Networks_Value",
        "Tinc_Networks_Value_HostSettings_Value": "pynix_os.services.tinc:Tinc_Networks_Value_HostSettings_Value",
        "Tinc_Networks_Value_HostSettings_Value_Addresses_Item": "pynix_os.services.tinc:Tinc_Networks_Value_HostSettings_Value_Addresses_Item",
        "Tinc_Networks_Value_HostSettings_Value_Settings": "pynix_os.services.tinc:Tinc_Networks_Value_HostSettings_Value_Settings",
        "Tinc_Networks_Value_HostSettings_Value_Subnets_Item": "pynix_os.services.tinc:Tinc_Networks_Value_HostSettings_Value_Subnets_Item",
        "Tinc_Networks_Value_Settings": "pynix_os.services.tinc:Tinc_Networks_Value_Settings",
        "Tinyauth": "pynix_os.services.tinyauth:Tinyauth",
        "Tinyauth_Settings": "pynix_os.services.tinyauth:Tinyauth_Settings",
        "Tinydns": "pynix_os.services.tinydns:Tinydns",
        "Tinyproxy": "pynix_os.services.tinyproxy:Tinyproxy",
        "Tinyproxy_Settings": "pynix_os.services.tinyproxy:Tinyproxy_Settings",
        "Tlp": "pynix_os.services.tlp:Tlp",
        "Tlp_Pd": "pynix_os.services.tlp:Tlp_Pd",
        "Tlsrpt": "pynix_os.services.tlsrpt:Tlsrpt",
        "Tlsrpt_Collectd": "pynix_os.services.tlsrpt:Tlsrpt_Collectd",
        "Tlsrpt_Collectd_Settings": "pynix_os.services.tlsrpt:Tlsrpt_Collectd_Settings",
        "Tlsrpt_Fetcher": "pynix_os.services.tlsrpt:Tlsrpt_Fetcher",
        "Tlsrpt_Fetcher_Settings": "pynix_os.services.tlsrpt:Tlsrpt_Fetcher_Settings",
        "Tlsrpt_Reportd": "pynix_os.services.tlsrpt:Tlsrpt_Reportd",
        "Tlsrpt_Reportd_Settings": "pynix_os.services.tlsrpt:Tlsrpt_Reportd_Settings",
        "TmateSshServer": "pynix_os.services.tmate_ssh_server:TmateSshServer",
        "Tmp": "pynix_os.boot.tmp:Tmp",
        "Tmp_ZramSettings": "pynix_os.boot.tmp:Tmp_ZramSettings",
        "Tmpfiles": "pynix_os.systemd.tmpfiles:Tmpfiles",
        "Tmpfiles_Settings_Value_Value_Value": "pynix_os.systemd.tmpfiles:Tmpfiles_Settings_Value_Value_Value",
        "Tmux": "pynix_os.programs.tmux:Tmux",
        "Todesk": "pynix_os.services.todesk:Todesk",
        "Tomcat": "pynix_os.services.tomcat:Tomcat",
        "Tomcat_Axis2": "pynix_os.services.tomcat:Tomcat_Axis2",
        "Tomcat_VirtualHosts_Item": "pynix_os.services.tomcat:Tomcat_VirtualHosts_Item",
        "Tools": "pynix_os.system.tools:Tools",
        "Tools_NixosBuildVms": "pynix_os.system.tools:Tools_NixosBuildVms",
        "Tools_NixosEnter": "pynix_os.system.tools:Tools_NixosEnter",
        "Tools_NixosGenerateConfig": "pynix_os.system.tools:Tools_NixosGenerateConfig",
        "Tools_NixosInstall": "pynix_os.system.tools:Tools_NixosInstall",
        "Tools_NixosOption": "pynix_os.system.tools:Tools_NixosOption",
        "Tools_NixosRebuild": "pynix_os.system.tools:Tools_NixosRebuild",
        "Tools_NixosVersion": "pynix_os.system.tools:Tools_NixosVersion",
        "Top": "pynix_os.top:Top",
        "Top_Containers_Value": "pynix_os.top:Top_Containers_Value",
        "Top_Containers_Value_AllowedDevices_Item": "pynix_os.top:Top_Containers_Value_AllowedDevices_Item",
        "Top_Containers_Value_BindMounts_Value": "pynix_os.top:Top_Containers_Value_BindMounts_Value",
        "Top_Containers_Value_ExtraVeths_Value": "pynix_os.top:Top_Containers_Value_ExtraVeths_Value",
        "Top_Containers_Value_ForwardPorts_Item": "pynix_os.top:Top_Containers_Value_ForwardPorts_Item",
        "Top_FileSystems_Value": "pynix_os.top:Top_FileSystems_Value",
        "Top_Specialisation_Value": "pynix_os.top:Top_Specialisation_Value",
        "Top_SwapDevices_Item": "pynix_os.top:Top_SwapDevices_Item",
        "Top_SwapDevices_Item_RandomEncryption": "pynix_os.top:Top_SwapDevices_Item_RandomEncryption",
        "Tor": "pynix_os.services.tor:Tor",
        "Tor_Client": "pynix_os.services.tor:Tor_Client",
        "Tor_Client_Dns": "pynix_os.services.tor:Tor_Client_Dns",
        "Tor_Client_OnionServices_Value": "pynix_os.services.tor:Tor_Client_OnionServices_Value",
        "Tor_Client_SocksListenAddress_Or": "pynix_os.services.tor:Tor_Client_SocksListenAddress_Or",
        "Tor_Client_TransparentProxy": "pynix_os.services.tor:Tor_Client_TransparentProxy",
        "Tor_ControlSocket": "pynix_os.services.tor:Tor_ControlSocket",
        "Tor_Relay": "pynix_os.services.tor:Tor_Relay",
        "Tor_Relay_OnionServices_Value": "pynix_os.services.tor:Tor_Relay_OnionServices_Value",
        "Tor_Relay_OnionServices_Value_AuthorizeClient": "pynix_os.services.tor:Tor_Relay_OnionServices_Value_AuthorizeClient",
        "Tor_Relay_OnionServices_Value_Map_Item_Or": "pynix_os.services.tor:Tor_Relay_OnionServices_Value_Map_Item_Or",
        "Tor_Relay_OnionServices_Value_Map_Item_Or_Target": "pynix_os.services.tor:Tor_Relay_OnionServices_Value_Map_Item_Or_Target",
        "Tor_Relay_OnionServices_Value_Settings": "pynix_os.services.tor:Tor_Relay_OnionServices_Value_Settings",
        "Tor_Settings": "pynix_os.services.tor:Tor_Settings",
        "Tor_Settings_ControlPort_Or_Item_Or": "pynix_os.services.tor:Tor_Settings_ControlPort_Or_Item_Or",
        "Tor_Settings_DNSPort_Or": "pynix_os.services.tor:Tor_Settings_DNSPort_Or",
        "Tor_Settings_DirPort_Or_Item_Or": "pynix_os.services.tor:Tor_Settings_DirPort_Or_Item_Or",
        "Tor_Settings_ExtORPort_Or": "pynix_os.services.tor:Tor_Settings_ExtORPort_Or",
        "Tor_Settings_HidServAuth_Item": "pynix_os.services.tor:Tor_Settings_HidServAuth_Item",
        "Tor_Settings_ServerTransportPlugin": "pynix_os.services.tor:Tor_Settings_ServerTransportPlugin",
        "Tor_Torsocks": "pynix_os.services.tor:Tor_Torsocks",
        "Tor_Tsocks": "pynix_os.services.tor:Tor_Tsocks",
        "Torque": "pynix_os.services.torque:Torque",
        "Torque_Mom": "pynix_os.services.torque:Torque_Mom",
        "Torque_Server": "pynix_os.services.torque:Torque_Server",
        "Torrentstream": "pynix_os.services.torrentstream:Torrentstream",
        "Touchegg": "pynix_os.services.touchegg:Touchegg",
        "ToxBootstrapd": "pynix_os.services.toxBootstrapd:ToxBootstrapd",
        "ToxNode": "pynix_os.services.tox_node:ToxNode",
        "Toxvpn": "pynix_os.services.toxvpn:Toxvpn",
        "TpAutoKbbl": "pynix_os.services.tp_auto_kbbl:TpAutoKbbl",
        "Security_Tpm2": "pynix_os.security.tpm2:Tpm2",
        "Systemd_Tpm2": "pynix_os.systemd.tpm2:Tpm2",
        "Tpm2_Abrmd": "pynix_os.security.tpm2:Tpm2_Abrmd",
        "Tpm2_Fapi": "pynix_os.security.tpm2:Tpm2_Fapi",
        "Tpm2_Pcrphases": "pynix_os.systemd.tpm2:Tpm2_Pcrphases",
        "Tpm2_Pkcs11": "pynix_os.security.tpm2:Tpm2_Pkcs11",
        "Tpm2_TctiEnvironment": "pynix_os.security.tpm2:Tpm2_TctiEnvironment",
        "Traccar": "pynix_os.services.traccar:Traccar",
        "Traceroute": "pynix_os.programs.traceroute:Traceroute",
        "Trackpoint": "pynix_os.hardware.trackpoint:Trackpoint",
        "Traefik": "pynix_os.services.traefik:Traefik",
        "Trafficserver": "pynix_os.services.trafficserver:Trafficserver",
        "Trafficserver_Plugins_Item": "pynix_os.services.trafficserver:Trafficserver_Plugins_Item",
        "TranquilPds": "pynix_os.services.tranquil_pds:TranquilPds",
        "TranquilPds_Database": "pynix_os.services.tranquil_pds:TranquilPds_Database",
        "TranquilPds_Settings": "pynix_os.services.tranquil_pds:TranquilPds_Settings",
        "TransferSh": "pynix_os.services.transfer_sh:TransferSh",
        "TransferSh_Settings": "pynix_os.services.transfer_sh:TransferSh_Settings",
        "Transmission": "pynix_os.services.transmission:Transmission",
        "Transmission_Settings": "pynix_os.services.transmission:Transmission_Settings",
        "TremorRs": "pynix_os.services.tremor_rs:TremorRs",
        "Trezord": "pynix_os.services.trezord:Trezord",
        "Trezord_Emulator": "pynix_os.services.trezord:Trezord_Emulator",
        "Trickster": "pynix_os.services.trickster:Trickster",
        "Triggerhappy": "pynix_os.services.triggerhappy:Triggerhappy",
        "Triggerhappy_Bindings_Item": "pynix_os.services.triggerhappy:Triggerhappy_Bindings_Item",
        "TriliumServer": "pynix_os.services.trilium_server:TriliumServer",
        "TriliumServer_Nginx": "pynix_os.services.trilium_server:TriliumServer_Nginx",
        "Trippy": "pynix_os.programs.trippy:Trippy",
        "Tsidp": "pynix_os.services.tsidp:Tsidp",
        "Tsidp_Settings": "pynix_os.services.tsidp:Tsidp_Settings",
        "TsmBackup": "pynix_os.services.tsmBackup:TsmBackup",
        "TsmClient": "pynix_os.programs.tsmClient:TsmClient",
        "TsmClient_Servers_Value": "pynix_os.programs.tsmClient:TsmClient_Servers_Value",
        "TtRss": "pynix_os.services.tt_rss:TtRss",
        "TtRss_Auth": "pynix_os.services.tt_rss:TtRss_Auth",
        "TtRss_Email": "pynix_os.services.tt_rss:TtRss_Email",
        "TtRss_PubSubHubbub": "pynix_os.services.tt_rss:TtRss_PubSubHubbub",
        "TtRss_Registration": "pynix_os.services.tt_rss:TtRss_Registration",
        "TtRss_Sphinx": "pynix_os.services.tt_rss:TtRss_Sphinx",
        "TtRss_UpdateDaemon": "pynix_os.services.tt_rss:TtRss_UpdateDaemon",
        "Tts": "pynix_os.services.tts:Tts",
        "Tts_Servers_Value": "pynix_os.services.tts:Tts_Servers_Value",
        "Ttyd": "pynix_os.services.ttyd:Ttyd",
        "Tuliprox": "pynix_os.services.tuliprox:Tuliprox",
        "Tumbler": "pynix_os.services.tumbler:Tumbler",
        "Tuned": "pynix_os.services.tuned:Tuned",
        "Tuned_PpdSettings": "pynix_os.services.tuned:Tuned_PpdSettings",
        "Tuned_PpdSettings_Main": "pynix_os.services.tuned:Tuned_PpdSettings_Main",
        "Tuned_Profiles_Value": "pynix_os.services.tuned:Tuned_Profiles_Value",
        "Tuned_Settings": "pynix_os.services.tuned:Tuned_Settings",
        "Tuptime": "pynix_os.services.tuptime:Tuptime",
        "Tuptime_Timer": "pynix_os.services.tuptime:Tuptime_Timer",
        "TurborepoRemoteCache": "pynix_os.services.turborepo_remote_cache:TurborepoRemoteCache",
        "Turbovnc": "pynix_os.programs.turbovnc:Turbovnc",
        "TurnRs": "pynix_os.services.turn_rs:TurnRs",
        "TurnRs_Settings": "pynix_os.services.turn_rs:TurnRs_Settings",
        "Tusd": "pynix_os.services.tusd:Tusd",
        "Tuxclocker": "pynix_os.programs.tuxclocker:Tuxclocker",
        "TuxedoDrivers": "pynix_os.hardware.tuxedo_drivers:TuxedoDrivers",
        "TuxedoDrivers_Settings": "pynix_os.hardware.tuxedo_drivers:TuxedoDrivers_Settings",
        "TuxedoRs": "pynix_os.hardware.tuxedo_rs:TuxedoRs",
        "TuxedoRs_TailorGui": "pynix_os.hardware.tuxedo_rs:TuxedoRs_TailorGui",
        "Twingate": "pynix_os.services.twingate:Twingate",
        "Typesense": "pynix_os.services.typesense:Typesense",
        "Typesense_Settings": "pynix_os.services.typesense:Typesense_Settings",
        "Tzupdate": "pynix_os.services.tzupdate:Tzupdate",
        "Tzupdate_Timer": "pynix_os.services.tzupdate:Tzupdate_Timer",
        "U9fs": "pynix_os.services.u9fs:U9fs",
        "Ubertooth": "pynix_os.hardware.ubertooth:Ubertooth",
        "Ucarp": "pynix_os.networking.ucarp:Ucarp",
        "Udev": "pynix_os.services.udev:Udev",
        "Udevil": "pynix_os.programs.udevil:Udevil",
        "Udisks2": "pynix_os.services.udisks2:Udisks2",
        "Udp514Journal": "pynix_os.services.udp514_journal:Udp514Journal",
        "UdpOverTcp": "pynix_os.services.udp_over_tcp:UdpOverTcp",
        "UdpOverTcp_Tcp2udp_Value": "pynix_os.services.udp_over_tcp:UdpOverTcp_Tcp2udp_Value",
        "UdpOverTcp_Udp2tcp_Value": "pynix_os.services.udp_over_tcp:UdpOverTcp_Udp2tcp_Value",
        "Uinput": "pynix_os.hardware.uinput:Uinput",
        "Uki": "pynix_os.boot.uki:Uki",
        "Ulogd": "pynix_os.services.ulogd:Ulogd",
        "Umami": "pynix_os.services.umami:Umami",
        "Umami_Settings": "pynix_os.services.umami:Umami_Settings",
        "Umbriel": "pynix_os.programs.umbriel:Umbriel",
        "Umurmur": "pynix_os.services.umurmur:Umurmur",
        "Umurmur_Settings": "pynix_os.services.umurmur:Umurmur_Settings",
        "Unbound": "pynix_os.services.unbound:Unbound",
        "Unbound_Settings": "pynix_os.services.unbound:Unbound_Settings",
        "Unclutter": "pynix_os.services.unclutter:Unclutter",
        "UnclutterXfixes": "pynix_os.services.unclutter_xfixes:UnclutterXfixes",
        "Undervolt": "pynix_os.services.undervolt:Undervolt",
        "Undervolt_P1": "pynix_os.services.undervolt:Undervolt_P1",
        "Undervolt_P2": "pynix_os.services.undervolt:Undervolt_P2",
        "UniSync": "pynix_os.hardware.uni_sync:UniSync",
        "UniSync_Devices_Item": "pynix_os.hardware.uni_sync:UniSync_Devices_Item",
        "UniSync_Devices_Item_Channels_Item": "pynix_os.hardware.uni_sync:UniSync_Devices_Item_Channels_Item",
        "Unifi": "pynix_os.services.unifi:Unifi",
        "Unit": "pynix_os.services.unit:Unit",
        "Unpackerr": "pynix_os.services.unpackerr:Unpackerr",
        "Unpoller": "pynix_os.services.unpoller:Unpoller",
        "Unpoller_Influxdb": "pynix_os.services.unpoller:Unpoller_Influxdb",
        "Unpoller_Loki": "pynix_os.services.unpoller:Unpoller_Loki",
        "Unpoller_Poller": "pynix_os.services.unpoller:Unpoller_Poller",
        "Unpoller_Prometheus": "pynix_os.services.unpoller:Unpoller_Prometheus",
        "Unpoller_Unifi": "pynix_os.services.unpoller:Unpoller_Unifi",
        "Unpoller_Unifi_Controllers_Item": "pynix_os.services.unpoller:Unpoller_Unifi_Controllers_Item",
        "Unpoller_Unifi_Defaults": "pynix_os.services.unpoller:Unpoller_Unifi_Defaults",
        "Upki": "pynix_os.services.upki:Upki",
        "Upower": "pynix_os.services.upower:Upower",
        "Ups": "pynix_os.power.ups:Ups",
        "Ups_Ups_Value": "pynix_os.power.ups:Ups_Ups_Value",
        "Ups_Upsd": "pynix_os.power.ups:Ups_Upsd",
        "Ups_Upsd_Listen_Item": "pynix_os.power.ups:Ups_Upsd_Listen_Item",
        "Ups_Upsmon": "pynix_os.power.ups:Ups_Upsmon",
        "Ups_Upsmon_Monitor_Value": "pynix_os.power.ups:Ups_Upsmon_Monitor_Value",
        "Ups_Users_Value": "pynix_os.power.ups:Ups_Users_Value",
        "Uptermd": "pynix_os.services.uptermd:Uptermd",
        "UptimeKuma": "pynix_os.services.uptime_kuma:UptimeKuma",
        "UptimeKuma_Settings": "pynix_os.services.uptime_kuma:UptimeKuma_Settings",
        "Uptimed": "pynix_os.services.uptimed:Uptimed",
        "Urserver": "pynix_os.services.urserver:Urserver",
        "Urxvtd": "pynix_os.services.urxvtd:Urxvtd",
        "UsbModeswitch": "pynix_os.hardware.usb_modeswitch:UsbModeswitch",
        "UsbStorage": "pynix_os.hardware.usbStorage:UsbStorage",
        "Usbguard": "pynix_os.services.usbguard:Usbguard",
        "Usbguard_Dbus": "pynix_os.services.usbguard:Usbguard_Dbus",
        "Usbmuxd": "pynix_os.services.usbmuxd:Usbmuxd",
        "Usbrelayd": "pynix_os.services.usbrelayd:Usbrelayd",
        "Usbtop": "pynix_os.programs.usbtop:Usbtop",
        "User": "pynix_os.systemd.user:User",
        "User_Paths_Value": "pynix_os.systemd.user:User_Paths_Value",
        "User_Services_Value": "pynix_os.systemd.user:User_Services_Value",
        "User_Settings": "pynix_os.systemd.user:User_Settings",
        "User_Settings_Manager": "pynix_os.systemd.user:User_Settings_Manager",
        "User_Slices_Value": "pynix_os.systemd.user:User_Slices_Value",
        "User_Sockets_Value": "pynix_os.systemd.user:User_Sockets_Value",
        "User_Targets_Value": "pynix_os.systemd.user:User_Targets_Value",
        "User_Timers_Value": "pynix_os.systemd.user:User_Timers_Value",
        "User_Tmpfiles": "pynix_os.systemd.user:User_Tmpfiles",
        "User_Tmpfiles_Users_Value": "pynix_os.systemd.user:User_Tmpfiles_Users_Value",
        "User_Units_Value": "pynix_os.systemd.user:User_Units_Value",
        "Userborn": "pynix_os.services.userborn:Userborn",
        "Userdbd": "pynix_os.services.userdbd:Userdbd",
        "Users": "pynix_os.users.__options__:Users",
        "Users_ExtraGroups_Value": "pynix_os.users.__options__:Users_ExtraGroups_Value",
        "Users_ExtraUsers_Value": "pynix_os.users.__options__:Users_ExtraUsers_Value",
        "Users_ExtraUsers_Value_SubGidRanges_Item": "pynix_os.users.__options__:Users_ExtraUsers_Value_SubGidRanges_Item",
        "Users_ExtraUsers_Value_SubUidRanges_Item": "pynix_os.users.__options__:Users_ExtraUsers_Value_SubUidRanges_Item",
        "Users_Groups_Value": "pynix_os.users.__options__:Users_Groups_Value",
        "Users_Users_Value": "pynix_os.users.__options__:Users_Users_Value",
        "Ustreamer": "pynix_os.services.ustreamer:Ustreamer",
        "Uvcvideo": "pynix_os.services.uvcvideo:Uvcvideo",
        "Uvcvideo_Dynctrl": "pynix_os.services.uvcvideo:Uvcvideo_Dynctrl",
        "Uvesafb": "pynix_os.boot.uvesafb:Uvesafb",
        "Uvesafb_V86d": "pynix_os.boot.uvesafb:Uvesafb_V86d",
        "Uwsgi": "pynix_os.services.uwsgi:Uwsgi",
        "Uwsm": "pynix_os.programs.uwsm:Uwsm",
        "Uwsm_WaylandCompositors_Value": "pynix_os.programs.uwsm:Uwsm_WaylandCompositors_Value",
        "V2ray": "pynix_os.services.v2ray:V2ray",
        "V2raya": "pynix_os.services.v2raya:V2raya",
        "V4l2Relayd": "pynix_os.services.v4l2_relayd:V4l2Relayd",
        "V4l2Relayd_Instances_Value": "pynix_os.services.v4l2_relayd:V4l2Relayd_Instances_Value",
        "Varnish": "pynix_os.services.varnish:Varnish",
        "Varnish_Listen_Item": "pynix_os.services.varnish:Varnish_Listen_Item",
        "Vault": "pynix_os.services.vault:Vault",
        "VaultAgent": "pynix_os.services.vault_agent:VaultAgent",
        "VaultAgent_Instances_Value": "pynix_os.services.vault_agent:VaultAgent_Instances_Value",
        "VaultAgent_Instances_Value_Settings": "pynix_os.services.vault_agent:VaultAgent_Instances_Value_Settings",
        "Vaultwarden": "pynix_os.services.vaultwarden:Vaultwarden",
        "Vdirsyncer": "pynix_os.services.vdirsyncer:Vdirsyncer",
        "Vdirsyncer_Jobs_Value": "pynix_os.services.vdirsyncer:Vdirsyncer_Jobs_Value",
        "Vdr": "pynix_os.services.vdr:Vdr",
        "Vector": "pynix_os.services.vector:Vector",
        "Veilid": "pynix_os.services.veilid:Veilid",
        "Veilid_Settings": "pynix_os.services.veilid:Veilid_Settings",
        "Vellum": "pynix_os.programs.vellum:Vellum",
        "Victorialogs": "pynix_os.services.victorialogs:Victorialogs",
        "Victoriametrics": "pynix_os.services.victoriametrics:Victoriametrics",
        "Victoriametrics_PrometheusConfig": "pynix_os.services.victoriametrics:Victoriametrics_PrometheusConfig",
        "Victoriatraces": "pynix_os.services.victoriatraces:Victoriatraces",
        "Vikunja": "pynix_os.services.vikunja:Vikunja",
        "Vim": "pynix_os.programs.vim:Vim",
        "VinylCache": "pynix_os.services.vinyl_cache:VinylCache",
        "VinylCache_Listen_Item": "pynix_os.services.vinyl_cache:VinylCache_Listen_Item",
        "VirtManager": "pynix_os.programs.virt_manager:VirtManager",
        "Virtualbox": "pynix_os.virtualisation.virtualbox:Virtualbox",
        "Virtualbox_Guest": "pynix_os.virtualisation.virtualbox:Virtualbox_Guest",
        "Virtualbox_Host": "pynix_os.virtualisation.virtualbox:Virtualbox_Host",
        "Security_Virtualisation": "pynix_os.security.virtualisation:Virtualisation",
        "Virtualisation": "pynix_os.virtualisation.__options__:Virtualisation",
        "Vivid": "pynix_os.programs.vivid:Vivid",
        "Vlagent": "pynix_os.services.vlagent:Vlagent",
        "Vlagent_RemoteWrite": "pynix_os.services.vlagent:Vlagent_RemoteWrite",
        "Vmagent": "pynix_os.services.vmagent:Vmagent",
        "Vmagent_PrometheusConfig": "pynix_os.services.vmagent:Vmagent_PrometheusConfig",
        "Vmagent_RemoteWrite": "pynix_os.services.vmagent:Vmagent_RemoteWrite",
        "Vmalert": "pynix_os.services.vmalert:Vmalert",
        "Vmalert_Instances_Value": "pynix_os.services.vmalert:Vmalert_Instances_Value",
        "Vmalert_Instances_Value_Settings": "pynix_os.services.vmalert:Vmalert_Instances_Value_Settings",
        "Vmware": "pynix_os.virtualisation.vmware:Vmware",
        "Vmware_Guest": "pynix_os.virtualisation.vmware:Vmware_Guest",
        "Vmware_Host": "pynix_os.virtualisation.vmware:Vmware_Host",
        "Vnstat": "pynix_os.services.vnstat:Vnstat",
        "Vnstat_Settings": "pynix_os.services.vnstat:Vnstat_Settings",
        "Vscode": "pynix_os.programs.vscode:Vscode",
        "Vsftpd": "pynix_os.services.vsftpd:Vsftpd",
        "VsmartcardVpcd": "pynix_os.services.vsmartcard_vpcd:VsmartcardVpcd",
        "Vswitch": "pynix_os.virtualisation.vswitch:Vswitch",
        "Vwifi": "pynix_os.services.vwifi:Vwifi",
        "Vwifi_Client": "pynix_os.services.vwifi:Vwifi_Client",
        "Vwifi_Module": "pynix_os.services.vwifi:Vwifi_Module",
        "Vwifi_Server": "pynix_os.services.vwifi:Vwifi_Server",
        "Vwifi_Server_Ports": "pynix_os.services.vwifi:Vwifi_Server_Ports",
        "Vwifi_Server_Vsock": "pynix_os.services.vwifi:Vwifi_Server_Vsock",
        "Waagent": "pynix_os.services.waagent:Waagent",
        "Waagent_Settings": "pynix_os.services.waagent:Waagent_Settings",
        "Wakapi": "pynix_os.services.wakapi:Wakapi",
        "Wakapi_Database": "pynix_os.services.wakapi:Wakapi_Database",
        "Warpgate": "pynix_os.services.warpgate:Warpgate",
        "Warpgate_Settings": "pynix_os.services.warpgate:Warpgate_Settings",
        "Warpgate_Settings_HttpSniCertificates_Item": "pynix_os.services.warpgate:Warpgate_Settings_HttpSniCertificates_Item",
        "Warpgate_Settings_SsoProviders_Item": "pynix_os.services.warpgate:Warpgate_Settings_SsoProviders_Item",
        "Wasabibackend": "pynix_os.services.wasabibackend:Wasabibackend",
        "Wasabibackend_Endpoint": "pynix_os.services.wasabibackend:Wasabibackend_Endpoint",
        "Wasabibackend_Rpc": "pynix_os.services.wasabibackend:Wasabibackend_Rpc",
        "Wastebin": "pynix_os.services.wastebin:Wastebin",
        "Wastebin_Settings": "pynix_os.services.wastebin:Wastebin_Settings",
        "Watchdogd": "pynix_os.services.watchdogd:Watchdogd",
        "Watchdogd_Settings": "pynix_os.services.watchdogd:Watchdogd_Settings",
        "Watt": "pynix_os.services.watt:Watt",
        "Watt_Settings": "pynix_os.services.watt:Watt_Settings",
        "Wavemon": "pynix_os.programs.wavemon:Wavemon",
        "Waybar": "pynix_os.programs.waybar:Waybar",
        "Waybar_Systemd": "pynix_os.programs.waybar:Waybar_Systemd",
        "Waydroid": "pynix_os.virtualisation.waydroid:Waydroid",
        "Wayfire": "pynix_os.programs.wayfire:Wayfire",
        "Wayfire_Xwayland": "pynix_os.programs.wayfire:Wayfire_Xwayland",
        "Wayland": "pynix_os.programs.wayland:Wayland",
        "Wayland_MiracleWm": "pynix_os.programs.wayland:Wayland_MiracleWm",
        "Wayvnc": "pynix_os.programs.wayvnc:Wayvnc",
        "Wealthfolio": "pynix_os.services.wealthfolio:Wealthfolio",
        "Webdav": "pynix_os.services.webdav:Webdav",
        "WebdavServerRs": "pynix_os.services.webdav_server_rs:WebdavServerRs",
        "Webhook": "pynix_os.services.webhook:Webhook",
        "Webhook_Hooks_Value": "pynix_os.services.webhook:Webhook_Hooks_Value",
        "Weblate": "pynix_os.services.weblate:Weblate",
        "Weblate_Smtp": "pynix_os.services.weblate:Weblate_Smtp",
        "Websurfx": "pynix_os.services.websurfx:Websurfx",
        "Websurfx_Settings": "pynix_os.services.websurfx:Websurfx_Settings",
        "Weechat": "pynix_os.services.weechat:Weechat",
        "Weylus": "pynix_os.programs.weylus:Weylus",
        "WgAccessServer": "pynix_os.services.wg_access_server:WgAccessServer",
        "WgAccessServer_Settings": "pynix_os.services.wg_access_server:WgAccessServer_Settings",
        "WgNetmanager": "pynix_os.services.wg_netmanager:WgNetmanager",
        "WgQuick": "pynix_os.networking.wg_quick:WgQuick",
        "WgQuick_Interfaces_Value": "pynix_os.networking.wg_quick:WgQuick_Interfaces_Value",
        "WgQuick_Interfaces_Value_Peers_Item": "pynix_os.networking.wg_quick:WgQuick_Interfaces_Value_Peers_Item",
        "Wgautomesh": "pynix_os.services.wgautomesh:Wgautomesh",
        "Wgautomesh_Settings": "pynix_os.services.wgautomesh:Wgautomesh_Settings",
        "Wgautomesh_Settings_Peers_Item": "pynix_os.services.wgautomesh:Wgautomesh_Settings_Peers_Item",
        "Whisparr": "pynix_os.services.whisparr:Whisparr",
        "Whisparr_Settings": "pynix_os.services.whisparr:Whisparr_Settings",
        "Whitebophir": "pynix_os.services.whitebophir:Whitebophir",
        "Whoami": "pynix_os.services.whoami:Whoami",
        "Whois": "pynix_os.programs.whois:Whois",
        "Whois_Settings_Item": "pynix_os.programs.whois:Whois_Settings_Item",
        "WhoogleSearch": "pynix_os.services.whoogle_search:WhoogleSearch",
        "WikiJs": "pynix_os.services.wiki_js:WikiJs",
        "WikiJs_Settings": "pynix_os.services.wiki_js:WikiJs_Settings",
        "Winbox": "pynix_os.programs.winbox:Winbox",
        "Windmill": "pynix_os.services.windmill:Windmill",
        "Windmill_Database": "pynix_os.services.windmill:Windmill_Database",
        "Wireguard": "pynix_os.networking.wireguard:Wireguard",
        "Wireguard_Interfaces_Value": "pynix_os.networking.wireguard:Wireguard_Interfaces_Value",
        "Wireguard_Interfaces_Value_Peers_Item": "pynix_os.networking.wireguard:Wireguard_Interfaces_Value_Peers_Item",
        "Wireless": "pynix_os.networking.wireless:Wireless",
        "Wireless_Iwd": "pynix_os.networking.wireless:Wireless_Iwd",
        "Wireless_Networks_Value": "pynix_os.networking.wireless:Wireless_Networks_Value",
        "Wireless_Pkcs11": "pynix_os.networking.wireless:Wireless_Pkcs11",
        "Wireshark": "pynix_os.programs.wireshark:Wireshark",
        "Wireshark_Dumpcap": "pynix_os.programs.wireshark:Wireshark_Dumpcap",
        "Wireshark_Usbmon": "pynix_os.programs.wireshark:Wireshark_Usbmon",
        "Wivrn": "pynix_os.services.wivrn:Wivrn",
        "Wivrn_Config": "pynix_os.services.wivrn:Wivrn_Config",
        "Wivrn_Steam": "pynix_os.services.wivrn:Wivrn_Steam",
        "Wlock": "pynix_os.services.wlock:Wlock",
        "WoodpeckerAgents": "pynix_os.services.woodpecker_agents:WoodpeckerAgents",
        "WoodpeckerAgents_Agents_Value": "pynix_os.services.woodpecker_agents:WoodpeckerAgents_Agents_Value",
        "WoodpeckerServer": "pynix_os.services.woodpecker_server:WoodpeckerServer",
        "Wooting": "pynix_os.hardware.wooting:Wooting",
        "Wordlist": "pynix_os.environment.wordlist:Wordlist",
        "Wordpress": "pynix_os.services.wordpress:Wordpress",
        "Wordpress_Sites_Value": "pynix_os.services.wordpress:Wordpress_Sites_Value",
        "Wordpress_Sites_Value_VirtualHost": "pynix_os.services.wordpress:Wordpress_Sites_Value_VirtualHost",
        "Wordpress_Sites_Value_VirtualHost_Listen_Item": "pynix_os.services.wordpress:Wordpress_Sites_Value_VirtualHost_Listen_Item",
        "Wordpress_Sites_Value_VirtualHost_Locations_Value": "pynix_os.services.wordpress:Wordpress_Sites_Value_VirtualHost_Locations_Value",
        "WorkoutTracker": "pynix_os.services.workout_tracker:WorkoutTracker",
        "Writefreely": "pynix_os.services.writefreely:Writefreely",
        "Writefreely_Acme": "pynix_os.services.writefreely:Writefreely_Acme",
        "Writefreely_Admin": "pynix_os.services.writefreely:Writefreely_Admin",
        "Writefreely_Email": "pynix_os.services.writefreely:Writefreely_Email",
        "Writefreely_Nginx": "pynix_os.services.writefreely:Writefreely_Nginx",
        "Writefreely_Settings": "pynix_os.services.writefreely:Writefreely_Settings",
        "Wshowkeys": "pynix_os.programs.wshowkeys:Wshowkeys",
        "Wstunnel": "pynix_os.services.wstunnel:Wstunnel",
        "Wstunnel_Clients_Value": "pynix_os.services.wstunnel:Wstunnel_Clients_Value",
        "Wstunnel_Clients_Value_Settings": "pynix_os.services.wstunnel:Wstunnel_Clients_Value_Settings",
        "Wstunnel_Servers_Value": "pynix_os.services.wstunnel:Wstunnel_Servers_Value",
        "Wstunnel_Servers_Value_Listen": "pynix_os.services.wstunnel:Wstunnel_Servers_Value_Listen",
        "Wstunnel_Servers_Value_Settings": "pynix_os.services.wstunnel:Wstunnel_Servers_Value_Settings",
        "Wstunnel_Servers_Value_Settings_RestrictTo_Item": "pynix_os.services.wstunnel:Wstunnel_Servers_Value_Settings_RestrictTo_Item",
        "Wvdial": "pynix_os.environment.wvdial:Wvdial",
        "Wyoming": "pynix_os.services.wyoming:Wyoming",
        "Wyoming_FasterWhisper": "pynix_os.services.wyoming:Wyoming_FasterWhisper",
        "Wyoming_FasterWhisper_Servers_Value": "pynix_os.services.wyoming:Wyoming_FasterWhisper_Servers_Value",
        "Wyoming_Openwakeword": "pynix_os.services.wyoming:Wyoming_Openwakeword",
        "Wyoming_Piper": "pynix_os.services.wyoming:Wyoming_Piper",
        "Wyoming_Piper_Servers_Value": "pynix_os.services.wyoming:Wyoming_Piper_Servers_Value",
        "Wyoming_Satellite": "pynix_os.services.wyoming:Wyoming_Satellite",
        "Wyoming_Satellite_Microphone": "pynix_os.services.wyoming:Wyoming_Satellite_Microphone",
        "Wyoming_Satellite_Sound": "pynix_os.services.wyoming:Wyoming_Satellite_Sound",
        "Wyoming_Satellite_Sounds": "pynix_os.services.wyoming:Wyoming_Satellite_Sounds",
        "Wyoming_Satellite_Vad": "pynix_os.services.wyoming:Wyoming_Satellite_Vad",
        "X2goserver": "pynix_os.services.x2goserver:X2goserver",
        "X2goserver_Superenicer": "pynix_os.services.x2goserver:X2goserver_Superenicer",
        "Xandikos": "pynix_os.services.xandikos:Xandikos",
        "Xandikos_Nginx": "pynix_os.services.xandikos:Xandikos_Nginx",
        "Xastir": "pynix_os.programs.xastir:Xastir",
        "Xbanish": "pynix_os.services.xbanish:Xbanish",
        "XeGuestUtilities": "pynix_os.services.xe_guest_utilities:XeGuestUtilities",
        "Xen": "pynix_os.virtualisation.xen:Xen",
        "Xen_Boot": "pynix_os.virtualisation.xen:Xen_Boot",
        "Xen_Boot_Bios": "pynix_os.virtualisation.xen:Xen_Boot_Bios",
        "Xen_Boot_Efi": "pynix_os.virtualisation.xen:Xen_Boot_Efi",
        "Xen_Dom0Resources": "pynix_os.virtualisation.xen:Xen_Dom0Resources",
        "Xen_Domains": "pynix_os.virtualisation.xen:Xen_Domains",
        "Xen_Qemu": "pynix_os.virtualisation.xen:Xen_Qemu",
        "Xfce": "pynix_os.environment.xfce:Xfce",
        "Xfconf": "pynix_os.programs.xfconf:Xfconf",
        "Xfs": "pynix_os.services.xfs:Xfs",
        "XfsQuota": "pynix_os.programs.xfs_quota:XfsQuota",
        "XfsQuota_Projects_Value": "pynix_os.programs.xfs_quota:XfsQuota_Projects_Value",
        "Xinetd": "pynix_os.services.xinetd:Xinetd",
        "Xinetd_Services_Item": "pynix_os.services.xinetd:Xinetd_Services_Item",
        "Xl2tpd": "pynix_os.services.xl2tpd:Xl2tpd",
        "Xmrig": "pynix_os.services.xmrig:Xmrig",
        "Xone": "pynix_os.hardware.xone:Xone",
        "Xonotic": "pynix_os.services.xonotic:Xonotic",
        "Xonotic_Settings": "pynix_os.services.xonotic:Xonotic_Settings",
        "Xonsh": "pynix_os.programs.xonsh:Xonsh",
        "Xonsh_BashCompletion": "pynix_os.programs.xonsh:Xonsh_BashCompletion",
        "XpadNoone": "pynix_os.hardware.xpad_noone:XpadNoone",
        "Xpadneo": "pynix_os.hardware.xpadneo:Xpadneo",
        "Xpadneo_RumbleAttenuation": "pynix_os.hardware.xpadneo:Xpadneo_RumbleAttenuation",
        "Xppen": "pynix_os.programs.xppen:Xppen",
        "Xray": "pynix_os.services.xray:Xray",
        "Xrdp": "pynix_os.services.xrdp:Xrdp",
        "Xrdp_Audio": "pynix_os.services.xrdp:Xrdp_Audio",
        "Programs_Xscreensaver": "pynix_os.programs.xscreensaver:Xscreensaver",
        "Services_Xscreensaver": "pynix_os.services.xscreensaver:Xscreensaver",
        "Xscreensaver_Sonar": "pynix_os.programs.xscreensaver:Xscreensaver_Sonar",
        "Xserver": "pynix_os.services.xserver:Xserver",
        "Xserver_DesktopManager": "pynix_os.services.xserver:Xserver_DesktopManager",
        "Xserver_DesktopManager_Cde": "pynix_os.services.xserver:Xserver_DesktopManager_Cde",
        "Xserver_DesktopManager_Cinnamon": "pynix_os.services.xserver:Xserver_DesktopManager_Cinnamon",
        "Xserver_DesktopManager_Enlightenment": "pynix_os.services.xserver:Xserver_DesktopManager_Enlightenment",
        "Xserver_DesktopManager_Kodi": "pynix_os.services.xserver:Xserver_DesktopManager_Kodi",
        "Xserver_DesktopManager_Lumina": "pynix_os.services.xserver:Xserver_DesktopManager_Lumina",
        "Xserver_DesktopManager_Lxqt": "pynix_os.services.xserver:Xserver_DesktopManager_Lxqt",
        "Xserver_DesktopManager_Mate": "pynix_os.services.xserver:Xserver_DesktopManager_Mate",
        "Xserver_DesktopManager_Phosh": "pynix_os.services.xserver:Xserver_DesktopManager_Phosh",
        "Xserver_DesktopManager_Phosh_PhocConfig_Or": "pynix_os.services.xserver:Xserver_DesktopManager_Phosh_PhocConfig_Or",
        "Xserver_DesktopManager_Phosh_PhocConfig_Or_Outputs_Value": "pynix_os.services.xserver:Xserver_DesktopManager_Phosh_PhocConfig_Or_Outputs_Value",
        "Xserver_DesktopManager_Retroarch": "pynix_os.services.xserver:Xserver_DesktopManager_Retroarch",
        "Xserver_DesktopManager_SurfDisplay": "pynix_os.services.xserver:Xserver_DesktopManager_SurfDisplay",
        "Xserver_DesktopManager_Wallpaper": "pynix_os.services.xserver:Xserver_DesktopManager_Wallpaper",
        "Xserver_DesktopManager_Xfce": "pynix_os.services.xserver:Xserver_DesktopManager_Xfce",
        "Xserver_DesktopManager_Xterm": "pynix_os.services.xserver:Xserver_DesktopManager_Xterm",
        "Xserver_Digimend": "pynix_os.services.xserver:Xserver_Digimend",
        "Xserver_DisplayManager": "pynix_os.services.xserver:Xserver_DisplayManager",
        "Xserver_DisplayManager_Lightdm": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm",
        "Xserver_DisplayManager_Lightdm_AutoLogin": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_AutoLogin",
        "Xserver_DisplayManager_Lightdm_Greeter": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeter",
        "Xserver_DisplayManager_Lightdm_Greeters": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters",
        "Xserver_DisplayManager_Lightdm_Greeters_Gtk": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Gtk",
        "Xserver_DisplayManager_Lightdm_Greeters_Gtk_CursorTheme": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Gtk_CursorTheme",
        "Xserver_DisplayManager_Lightdm_Greeters_Gtk_IconTheme": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Gtk_IconTheme",
        "Xserver_DisplayManager_Lightdm_Greeters_Gtk_Theme": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Gtk_Theme",
        "Xserver_DisplayManager_Lightdm_Greeters_Lomiri": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Lomiri",
        "Xserver_DisplayManager_Lightdm_Greeters_Mini": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Mini",
        "Xserver_DisplayManager_Lightdm_Greeters_Mobile": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Mobile",
        "Xserver_DisplayManager_Lightdm_Greeters_Pantheon": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Pantheon",
        "Xserver_DisplayManager_Lightdm_Greeters_Slick": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Slick",
        "Xserver_DisplayManager_Lightdm_Greeters_Slick_CursorTheme": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Slick_CursorTheme",
        "Xserver_DisplayManager_Lightdm_Greeters_Slick_Font": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Slick_Font",
        "Xserver_DisplayManager_Lightdm_Greeters_Slick_IconTheme": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Slick_IconTheme",
        "Xserver_DisplayManager_Lightdm_Greeters_Slick_Theme": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Slick_Theme",
        "Xserver_DisplayManager_Lightdm_Greeters_Tiny": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Tiny",
        "Xserver_DisplayManager_Lightdm_Greeters_Tiny_Label": "pynix_os.services.xserver:Xserver_DisplayManager_Lightdm_Greeters_Tiny_Label",
        "Xserver_DisplayManager_Startx": "pynix_os.services.xserver:Xserver_DisplayManager_Startx",
        "Xserver_DisplayManager_Sx": "pynix_os.services.xserver:Xserver_DisplayManager_Sx",
        "Xserver_DisplayManager_Xpra": "pynix_os.services.xserver:Xserver_DisplayManager_Xpra",
        "Xserver_Imwheel": "pynix_os.services.xserver:Xserver_Imwheel",
        "Xserver_Synaptics": "pynix_os.services.xserver:Xserver_Synaptics",
        "Xserver_Wacom": "pynix_os.services.xserver:Xserver_Wacom",
        "Xserver_WindowManager": "pynix_os.services.xserver:Xserver_WindowManager",
        "Xserver_WindowManager_Awesome": "pynix_os.services.xserver:Xserver_WindowManager_Awesome",
        "Xserver_WindowManager_Berry": "pynix_os.services.xserver:Xserver_WindowManager_Berry",
        "Xserver_WindowManager_Bspwm": "pynix_os.services.xserver:Xserver_WindowManager_Bspwm",
        "Xserver_WindowManager_Bspwm_Sxhkd": "pynix_os.services.xserver:Xserver_WindowManager_Bspwm_Sxhkd",
        "Xserver_WindowManager_Clfswm": "pynix_os.services.xserver:Xserver_WindowManager_Clfswm",
        "Xserver_WindowManager_Cwm": "pynix_os.services.xserver:Xserver_WindowManager_Cwm",
        "Xserver_WindowManager_Dk": "pynix_os.services.xserver:Xserver_WindowManager_Dk",
        "Xserver_WindowManager_Dwm": "pynix_os.services.xserver:Xserver_WindowManager_Dwm",
        "Xserver_WindowManager_E16": "pynix_os.services.xserver:Xserver_WindowManager_E16",
        "Xserver_WindowManager_Evilwm": "pynix_os.services.xserver:Xserver_WindowManager_Evilwm",
        "Xserver_WindowManager_Exwm": "pynix_os.services.xserver:Xserver_WindowManager_Exwm",
        "Xserver_WindowManager_Fluxbox": "pynix_os.services.xserver:Xserver_WindowManager_Fluxbox",
        "Xserver_WindowManager_Fvwm2": "pynix_os.services.xserver:Xserver_WindowManager_Fvwm2",
        "Xserver_WindowManager_Fvwm3": "pynix_os.services.xserver:Xserver_WindowManager_Fvwm3",
        "Xserver_WindowManager_Hackedbox": "pynix_os.services.xserver:Xserver_WindowManager_Hackedbox",
        "Xserver_WindowManager_Herbstluftwm": "pynix_os.services.xserver:Xserver_WindowManager_Herbstluftwm",
        "Xserver_WindowManager_Hypr": "pynix_os.services.xserver:Xserver_WindowManager_Hypr",
        "Xserver_WindowManager_I3": "pynix_os.services.xserver:Xserver_WindowManager_I3",
        "Xserver_WindowManager_Icewm": "pynix_os.services.xserver:Xserver_WindowManager_Icewm",
        "Xserver_WindowManager_Jwm": "pynix_os.services.xserver:Xserver_WindowManager_Jwm",
        "Xserver_WindowManager_Katriawm": "pynix_os.services.xserver:Xserver_WindowManager_Katriawm",
        "Xserver_WindowManager_Leftwm": "pynix_os.services.xserver:Xserver_WindowManager_Leftwm",
        "Xserver_WindowManager_Lwm": "pynix_os.services.xserver:Xserver_WindowManager_Lwm",
        "Xserver_WindowManager_Metacity": "pynix_os.services.xserver:Xserver_WindowManager_Metacity",
        "Xserver_WindowManager_Mlvwm": "pynix_os.services.xserver:Xserver_WindowManager_Mlvwm",
        "Xserver_WindowManager_Mwm": "pynix_os.services.xserver:Xserver_WindowManager_Mwm",
        "Xserver_WindowManager_N2bwm": "pynix_os.services.xserver:Xserver_WindowManager_N2bwm",
        "Xserver_WindowManager_Nimdow": "pynix_os.services.xserver:Xserver_WindowManager_Nimdow",
        "Xserver_WindowManager_Notion": "pynix_os.services.xserver:Xserver_WindowManager_Notion",
        "Xserver_WindowManager_Openbox": "pynix_os.services.xserver:Xserver_WindowManager_Openbox",
        "Xserver_WindowManager_Oxwm": "pynix_os.services.xserver:Xserver_WindowManager_Oxwm",
        "Xserver_WindowManager_Pekwm": "pynix_os.services.xserver:Xserver_WindowManager_Pekwm",
        "Xserver_WindowManager_Qtile": "pynix_os.services.xserver:Xserver_WindowManager_Qtile",
        "Xserver_WindowManager_Ratpoison": "pynix_os.services.xserver:Xserver_WindowManager_Ratpoison",
        "Xserver_WindowManager_Smallwm": "pynix_os.services.xserver:Xserver_WindowManager_Smallwm",
        "Xserver_WindowManager_Spectrwm": "pynix_os.services.xserver:Xserver_WindowManager_Spectrwm",
        "Xserver_WindowManager_Stumpwm": "pynix_os.services.xserver:Xserver_WindowManager_Stumpwm",
        "Xserver_WindowManager_Tinywm": "pynix_os.services.xserver:Xserver_WindowManager_Tinywm",
        "Xserver_WindowManager_Twm": "pynix_os.services.xserver:Xserver_WindowManager_Twm",
        "Xserver_WindowManager_Vxwm": "pynix_os.services.xserver:Xserver_WindowManager_Vxwm",
        "Xserver_WindowManager_Windowlab": "pynix_os.services.xserver:Xserver_WindowManager_Windowlab",
        "Xserver_WindowManager_Windowmaker": "pynix_os.services.xserver:Xserver_WindowManager_Windowmaker",
        "Xserver_WindowManager_Wmderland": "pynix_os.services.xserver:Xserver_WindowManager_Wmderland",
        "Xserver_WindowManager_Wmii": "pynix_os.services.xserver:Xserver_WindowManager_Wmii",
        "Xserver_WindowManager_Xmonad": "pynix_os.services.xserver:Xserver_WindowManager_Xmonad",
        "Xserver_Xautolock": "pynix_os.services.xserver:Xserver_Xautolock",
        "Xserver_Xkb": "pynix_os.services.xserver:Xserver_Xkb",
        "Xserver_Xkb_ExtraLayouts_Value": "pynix_os.services.xserver:Xserver_Xkb_ExtraLayouts_Value",
        "Xserver_XrandrHeads_Item": "pynix_os.services.xserver:Xserver_XrandrHeads_Item",
        "XssLock": "pynix_os.programs.xss_lock:XssLock",
        "Xwayland": "pynix_os.programs.xwayland:Xwayland",
        "YandexDisk": "pynix_os.services.yandex_disk:YandexDisk",
        "Yarr": "pynix_os.services.yarr:Yarr",
        "Yazi": "pynix_os.programs.yazi:Yazi",
        "Yazi_Settings": "pynix_os.programs.yazi:Yazi_Settings",
        "Ydotool": "pynix_os.programs.ydotool:Ydotool",
        "Yggdrasil": "pynix_os.services.yggdrasil:Yggdrasil",
        "YggdrasilJumper": "pynix_os.services.yggdrasil_jumper:YggdrasilJumper",
        "Yggdrasil_Settings": "pynix_os.services.yggdrasil:Yggdrasil_Settings",
        "Ympd": "pynix_os.services.ympd:Ympd",
        "Ympd_Mpd": "pynix_os.services.ympd:Ympd_Mpd",
        "YourSpotify": "pynix_os.services.your_spotify:YourSpotify",
        "YourSpotify_Settings": "pynix_os.services.your_spotify:YourSpotify_Settings",
        "Youtrack": "pynix_os.services.youtrack:Youtrack",
        "Youtrack_EnvironmentalParameters": "pynix_os.services.youtrack:Youtrack_EnvironmentalParameters",
        "YtdlSub": "pynix_os.services.ytdl_sub:YtdlSub",
        "YtdlSub_Instances_Value": "pynix_os.services.ytdl_sub:YtdlSub_Instances_Value",
        "YubikeyAgent": "pynix_os.services.yubikey_agent:YubikeyAgent",
        "YubikeyManager": "pynix_os.programs.yubikey_manager:YubikeyManager",
        "YubikeyTouchDetector": "pynix_os.programs.yubikey_touch_detector:YubikeyTouchDetector",
        "ZabbixAgent": "pynix_os.services.zabbixAgent:ZabbixAgent",
        "ZabbixAgent_Listen": "pynix_os.services.zabbixAgent:ZabbixAgent_Listen",
        "ZabbixProxy": "pynix_os.services.zabbixProxy:ZabbixProxy",
        "ZabbixProxy_Listen": "pynix_os.services.zabbixProxy:ZabbixProxy_Listen",
        "ZabbixServer": "pynix_os.services.zabbixServer:ZabbixServer",
        "ZabbixServer_Listen": "pynix_os.services.zabbixServer:ZabbixServer_Listen",
        "ZabbixWeb": "pynix_os.services.zabbixWeb:ZabbixWeb",
        "ZabbixWeb_Httpd": "pynix_os.services.zabbixWeb:ZabbixWeb_Httpd",
        "ZabbixWeb_Httpd_VirtualHost": "pynix_os.services.zabbixWeb:ZabbixWeb_Httpd_VirtualHost",
        "ZabbixWeb_Httpd_VirtualHost_Listen_Item": "pynix_os.services.zabbixWeb:ZabbixWeb_Httpd_VirtualHost_Listen_Item",
        "ZabbixWeb_Httpd_VirtualHost_Locations_Value": "pynix_os.services.zabbixWeb:ZabbixWeb_Httpd_VirtualHost_Locations_Value",
        "ZabbixWeb_Nginx": "pynix_os.services.zabbixWeb:ZabbixWeb_Nginx",
        "ZabbixWeb_Nginx_VirtualHost": "pynix_os.services.zabbixWeb:ZabbixWeb_Nginx_VirtualHost",
        "ZabbixWeb_Nginx_VirtualHost_Listen_Item": "pynix_os.services.zabbixWeb:ZabbixWeb_Nginx_VirtualHost_Listen_Item",
        "ZabbixWeb_Nginx_VirtualHost_Locations_Value": "pynix_os.services.zabbixWeb:ZabbixWeb_Nginx_VirtualHost_Locations_Value",
        "ZabbixWeb_Server": "pynix_os.services.zabbixWeb:ZabbixWeb_Server",
        "Zammad": "pynix_os.services.zammad:Zammad",
        "Zammad_Database": "pynix_os.services.zammad:Zammad_Database",
        "Zammad_Nginx": "pynix_os.services.zammad:Zammad_Nginx",
        "Zammad_Redis": "pynix_os.services.zammad:Zammad_Redis",
        "Zapret": "pynix_os.services.zapret:Zapret",
        "Zapret2": "pynix_os.services.zapret2:Zapret2",
        "Zapret2_Firewall": "pynix_os.services.zapret2:Zapret2_Firewall",
        "Zapret2_Profiles_Value": "pynix_os.services.zapret2:Zapret2_Profiles_Value",
        "Zeitgeist": "pynix_os.services.zeitgeist:Zeitgeist",
        "Zenohd": "pynix_os.services.zenohd:Zenohd",
        "Zenohd_Settings": "pynix_os.services.zenohd:Zenohd_Settings",
        "Zerobin": "pynix_os.services.zerobin:Zerobin",
        "Zerobyte": "pynix_os.services.zerobyte:Zerobyte",
        "Zerobyte_Settings": "pynix_os.services.zerobyte:Zerobyte_Settings",
        "Zeronet": "pynix_os.services.zeronet:Zeronet",
        "Zeronsd": "pynix_os.services.zeronsd:Zeronsd",
        "Zeronsd_ServedNetworks_Value": "pynix_os.services.zeronsd:Zeronsd_ServedNetworks_Value",
        "Zeronsd_ServedNetworks_Value_Settings": "pynix_os.services.zeronsd:Zeronsd_ServedNetworks_Value_Settings",
        "Zerotierone": "pynix_os.services.zerotierone:Zerotierone",
        "Zeyple": "pynix_os.services.zeyple:Zeyple",
        "Boot_Zfs": "pynix_os.boot.zfs:Zfs",
        "Ec2_Zfs": "pynix_os.ec2.zfs:Zfs",
        "Openstack_Zfs": "pynix_os.openstack.zfs:Zfs",
        "Services_Zfs": "pynix_os.services.zfs:Zfs",
        "Zfs_AutoReplication": "pynix_os.services.zfs:Zfs_AutoReplication",
        "Zfs_AutoScrub": "pynix_os.services.zfs:Zfs_AutoScrub",
        "Zfs_AutoSnapshot": "pynix_os.services.zfs:Zfs_AutoSnapshot",
        "Ec2_Zfs_Zfs_Datasets_Value": "pynix_os.ec2.zfs:Zfs_Datasets_Value",
        "Openstack_Zfs_Zfs_Datasets_Value": "pynix_os.openstack.zfs:Zfs_Datasets_Value",
        "Zfs_Pools_Value": "pynix_os.boot.zfs:Zfs_Pools_Value",
        "Zfs_Trim": "pynix_os.services.zfs:Zfs_Trim",
        "Zfs_Tzpfms": "pynix_os.boot.zfs:Zfs_Tzpfms",
        "Zfs_Zed": "pynix_os.services.zfs:Zfs_Zed",
        "Zigbee2mqtt": "pynix_os.services.zigbee2mqtt:Zigbee2mqtt",
        "Zipline": "pynix_os.services.zipline:Zipline",
        "Zipline_Database": "pynix_os.services.zipline:Zipline_Database",
        "Zipline_Settings": "pynix_os.services.zipline:Zipline_Settings",
        "Zitadel": "pynix_os.services.zitadel:Zitadel",
        "Zitadel_Settings": "pynix_os.services.zitadel:Zitadel_Settings",
        "Zmap": "pynix_os.programs.zmap:Zmap",
        "Znapzend": "pynix_os.services.znapzend:Znapzend",
        "Znapzend_Features": "pynix_os.services.znapzend:Znapzend_Features",
        "Znapzend_Zetup_Value": "pynix_os.services.znapzend:Znapzend_Zetup_Value",
        "Znapzend_Zetup_Value_Destinations_Value": "pynix_os.services.znapzend:Znapzend_Zetup_Value_Destinations_Value",
        "Znc": "pynix_os.services.znc:Znc",
        "Znc_ConfOptions": "pynix_os.services.znc:Znc_ConfOptions",
        "Znc_ConfOptions_Networks_Value": "pynix_os.services.znc:Znc_ConfOptions_Networks_Value",
        "Zoneminder": "pynix_os.services.zoneminder:Zoneminder",
        "Zoneminder_Database": "pynix_os.services.zoneminder:Zoneminder_Database",
        "Zookeeper": "pynix_os.services.zookeeper:Zookeeper",
        "ZoomUs": "pynix_os.programs.zoom_us:ZoomUs",
        "Zoxide": "pynix_os.programs.zoxide:Zoxide",
        "ZramGenerator": "pynix_os.services.zram_generator:ZramGenerator",
        "ZramGenerator_Settings": "pynix_os.services.zram_generator:ZramGenerator_Settings",
        "ZramSwap": "pynix_os.zramSwap.__options__:ZramSwap",
        "Zrepl": "pynix_os.services.zrepl:Zrepl",
        "Zrepl_Settings": "pynix_os.services.zrepl:Zrepl_Settings",
        "Zsh": "pynix_os.programs.zsh:Zsh",
        "Zsh_Autosuggestions": "pynix_os.programs.zsh:Zsh_Autosuggestions",
        "Zsh_OhMyZsh": "pynix_os.programs.zsh:Zsh_OhMyZsh",
        "Zsh_SyntaxHighlighting": "pynix_os.programs.zsh:Zsh_SyntaxHighlighting",
        "Zsh_ZshAutoenv": "pynix_os.programs.zsh:Zsh_ZshAutoenv",
        "Zswap": "pynix_os.boot.zswap:Zswap",
        "ZwaveJs": "pynix_os.services.zwave_js:ZwaveJs",
        "ZwaveJsUi": "pynix_os.services.zwave_js_ui:ZwaveJsUi",
        "ZwaveJsUi_Settings": "pynix_os.services.zwave_js_ui:ZwaveJsUi_Settings",
        "ZwaveJs_Settings": "pynix_os.services.zwave_js:ZwaveJs_Settings",
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
