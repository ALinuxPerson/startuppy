from typing import *
import platform
import ctypes
import sys
import os

def init_system():
    """
    Checks for the init system of a linux system

    :return: init system
    """

    switch_case: Dict[str, bool] = {
        "systemd": os.path.exists("/run/systemd/system"),
        "upstart": os.path.exists("/usr/share/upstart"),
        "sysvinit": os.path.exists("/etc/init.d")
    }

    for init_name, check in switch_case.items():
        if check:
            return init_name
    else:
        if platform.system() != "Linux":
            raise OSError(f"'{platform.system()}' is not Linux")
        raise EnvironmentError("init system is unknown")

def python_in_interactive() -> bool:
    """
    Checks if python is being run in interactive mode (aka REPL)
    :return: True or False depending whether or not python is being run in interactive mode
    """

    return hasattr(sys, "ps1")

def root() -> bool:
    """
    Checks if python is being run as the root user.
    :return: True if python is being run as root, else False
    """
    if platform.system() in ("Linux", "Darwin"):
        return os.geteuid() == 0
    if platform == "Windows":
        return ctypes.windll.shell32.IsUserAnAdmin() == True
    raise EnvironmentError("unknown operating system")
