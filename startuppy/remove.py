from typing import *
import os

class StartupRemove:
    def remove(self, command: str):
        raise NotImplementedError

class SystemDLinuxRemove(StartupRemove):
    def remove(self, command: str):
        pass

class UpstartLinuxRemove(StartupRemove):
    def remove(self, command: str):
        pass

class SysVInitLinuxRemove(StartupRemove):
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

    def remove(self, command: str):
        init_system: str = self._init_system

        systemd: SystemDLinuxRemove = SystemDLinuxRemove()
        upstart: UpstartLinuxRemove = UpstartLinuxRemove()
        sysvinit: SysVInitLinuxRemove = SysVInitLinuxRemove()

        switch_case: Dict[str, Callable] = {
            "systemd": systemd.remove,
            "upstart": upstart.remove,
            "sysvinit": sysvinit.remove
        }

        for init_system_name, func in switch_case.items():
            if init_system_name == init_system:
                func(command)

class MacRemove(StartupRemove):
    def remove(self, command: str):
        pass

class WindowsRemove(StartupRemove):
    def remove(self, command: str):
        pass
