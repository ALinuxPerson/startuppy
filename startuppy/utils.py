from typing import *
import platform
import os

def init_system():
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
