from startuppy import utils
from typing import *

class StartupRemove:
    def filename(self, command: str) -> str:
        raise NotImplementedError

    def remove(self, command: str):
        raise NotImplementedError

class SystemDLinuxRemove(StartupRemove):
    def remove(self, command: str):
        pass

class UpstartLinuxRemove(StartupRemove):
    def remove(self, command: str):
        pass

class SysVInitLinuxRemove(StartupRemove):
    def remove(self, command: str):
        pass

class LinuxRemove(StartupRemove):
    def remove(self, command: str):
        init_system: str = utils.init_system()

        systemd: SystemDLinuxRemove = SystemDLinuxRemove()
        upstart: UpstartLinuxRemove = UpstartLinuxRemove()
        sysvinit: SysVInitLinuxRemove = SysVInitLinuxRemove()

        switch_case: Dict[str, Callable] = {
            "systemd": systemd.remove,
            "upstart": upstart.remove,
            "sysvinit": sysvinit.remove
        }

        for init_name, func in switch_case.items():
            if init_name == init_system:
                func(command)

class MacRemove(StartupRemove):
    def remove(self, command: str):
        pass

class WindowsRemove(StartupRemove):
    def remove(self, command: str):
        pass
