from startuppy import add, remove, utils
from typing import *
import platform
import elevate
import os

__all__: List[str] = ["add", "remove"]

def _elevate(show_console: bool = True, graphical: bool = True):
    if utils.python_in_interactive():
        raise EnvironmentError("please launch python in script mode then try again.")
    elevate.elevate(show_console=show_console, graphical=graphical)

elevate.elevate = _elevate  # override elevate method

class Startup:
    def __init__(self, command: str):
        self.command: str = os.path.abspath(command)
        if not os.path.exists(self.command) or not os.path.isfile(self.command) or not self.command:
            raise FileNotFoundError("invalid command")

    @property
    def _add_choice(self) -> Type[add.StartupAdd]:
        os_platform: str = platform.system()

        switch_case: Dict[str, Type[add.StartupAdd]] = {
            "Linux": add.LinuxAdd,
            "Windows": add.WindowsAdd,
            "Darwin": add.MacAdd
        }

        try:
            return switch_case[os_platform]
        except KeyError:
            raise EnvironmentError("unknown operating system")

    @property
    def _remove_choice(self) -> Type[remove.StartupRemove]:
        os_platform: str = platform.system()

        switch_case: Dict[str, Type[remove.StartupRemove]] = {
            "Linux": remove.LinuxRemove,
            "Windows": remove.WindowsRemove,
            "Darwin": remove.MacRemove
        }

        try:
            return switch_case[os_platform]
        except KeyError:
            raise EnvironmentError("unknown operating system")

    def add(self):
        startup_add: add.StartupAdd = self._add_choice()
        return startup_add.add(self.command)

    def remove(self):
        startup_remove: remove.StartupRemove = self._remove_choice()
        return startup_remove.remove(self.command)

    def __repr__(self):
        return f"Startup('{self.command}')"
