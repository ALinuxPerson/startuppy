from startuppy import utils
from typing import *

class StartupAdd:
    def add(self, command: str):
        raise NotImplementedError

class SystemDLinuxAdd(StartupAdd):
    def add(self, command: str):
        pass

class UpstartLinuxAdd(StartupAdd):
    def add(self, command: str):
        pass

class SysVInitLinuxAdd(StartupAdd):
    def add(self, command: str):
        pass

class LinuxAdd(StartupAdd):
    def add(self, command: str):
        init_system: str = utils.init_system()

        systemd: SystemDLinuxAdd = SystemDLinuxAdd()
        upstart: UpstartLinuxAdd = UpstartLinuxAdd()
        sysvinit: SysVInitLinuxAdd = SysVInitLinuxAdd()

        switch_case: Dict[str, Callable] = {
            "systemd": systemd.add,
            "upstart": upstart.add,
            "sysvinit": sysvinit.add
        }

        for init_name, func in switch_case.items():
            if init_name == init_system:
                func(command)

class MacAdd(StartupAdd):
    def add(self, command: str):
        pass

class WindowsAdd(StartupAdd):
    def add(self, command: str):
        pass
