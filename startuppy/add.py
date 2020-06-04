from typing import *
import os

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
    @property
    def _init_system(self):
        switch_case: Dict[str, bool] = {
            "systemd": os.path.exists("/usr/lib/systemd"),
            "upstart": os.path.exists("/usr/share/upstart"),
            "sysvinit": os.path.exists("/etc/init.d")
        }

        for init_system, check in switch_case.items():
            if check:
                return init_system
        else:
            raise SystemError("init is unknown")

    def add(self, command: str):
        init_system: str = self._init_system

        systemd: SystemDLinuxAdd = SystemDLinuxAdd()
        upstart: UpstartLinuxAdd = UpstartLinuxAdd()
        sysvinit: SysVInitLinuxAdd = SysVInitLinuxAdd()

        switch_case: Dict[str, Callable] = {
            "systemd": systemd.add,
            "upstart": upstart.add,
            "sysvinit": sysvinit.add
        }

        for init_system_name, func in switch_case.items():
            if init_system_name == init_system:
                func(command)

class MacAdd(StartupAdd):
    def add(self, command: str):
        pass

class WindowsAdd(StartupAdd):
    def add(self, command: str):
        pass
