from startuppy import add, remove, utils
from typing import *
import platform
import os

__all__: List[str] = ["add", "remove"]

class Startup:
    def __init__(self, command: str):
        self.command: str = os.path.abspath(command)
        if not os.path.exists(self.command) or not os.path.isfile(self.command) or not self.command:
            raise FileNotFoundError("invalid command")
        if platform.system() not in ("Linux", "Windows", "Darwin"):
            raise SystemError(f"operating system '{platform.system()}' not compatible")
        if utils.python_in_interactive():
            raise EnvironmentError("please launch python in script mode then try again.")

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
            raise EnvironmentError("unknown operating system") from None

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
