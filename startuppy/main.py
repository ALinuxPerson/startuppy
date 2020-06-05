from startuppy.remove import (
    StartupRemove,
    LinuxRemove,
    WindowsRemove,
    MacRemove
)
from startuppy.add import (
    StartupAdd,
    LinuxAdd,
    WindowsAdd,
    MacAdd
)
from typing import *
import platform
import os

class Startup:
    def __init__(self, command: str):
        self.command: str = os.path.abspath(command)

    @property
    def _add_choice(self) -> Type[StartupAdd]:
        os_platform: str = platform.system()

        switch_case: Dict[str, Type[StartupAdd]] = {
            "Linux": LinuxAdd,
            "Windows": WindowsAdd,
            "Darwin": MacAdd
        }

        try:
            return switch_case[os_platform]
        except KeyError:
            raise EnvironmentError("unknown operating system")

    @property
    def _remove_choice(self) -> Type[StartupRemove]:
        os_platform: str = platform.system()

        switch_case: Dict[str, Type[StartupRemove]] = {
            "Linux": LinuxRemove,
            "Windows": WindowsRemove,
            "Darwin": MacRemove
        }

        try:
            return switch_case[os_platform]
        except KeyError:
            raise EnvironmentError("unknown operating system")

    def add(self, command: str):
        pass

    def remove(self, command: str):
        pass
