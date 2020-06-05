from startuppy import utils
from typing import *
import elevate
import os

class StartupAdd:
    def _filename(self, command: str) -> str:
        raise NotImplementedError

    def add(self, command: str):
        raise NotImplementedError

class SystemDLinuxAdd(StartupAdd):
    def _filename(self, command: str) -> str:
        return f"{os.path.basename(command)}-startuppy.service"

    def add(self, command: str):
        import configparser

        config: configparser.ConfigParser = configparser.ConfigParser()

        elevate.elevate(graphical=False)

        config["Unit"] = {
            "Description": f"{os.path.dirname(command)}: Created by StartupPy"
        }
        config["Service"] = {
            "Type": "simple",
            "ExecStart": command
        }
        config["Install"] = {
            "WantedBy": "multi-user.target"
        }

        with open(f"/etc/systemd/system/{self._filename(command)}", "w") as service:
            config.write(service)

class UpstartLinuxAdd(StartupAdd):
    def _filename(self, command: str) -> str:
        return f"{os.path.basename(command)}-startuppy.conf"

    def add(self, command: str):
        elevate.elevate(graphical=False)

        buffer: str = (f"start on filesystem\n"
                       f"exec {command}")

        with open(f"/etc/init/{self._filename(command)}", "w") as script:
            script.write(buffer)

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
