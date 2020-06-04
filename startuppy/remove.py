class StartupRemove:
    def remove(self, command: str):
        raise NotImplementedError

class SystemDLinuxAdd(StartupRemove):
    def remove(self, command: str):
        pass

class UpstartLinuxAdd(StartupRemove):
    def remove(self, command: str):
        pass

class SysVInitLinuxAdd(StartupRemove):
    def remove(self, command: str):
        pass

class LinuxRemove(StartupRemove):
    def remove(self, command: str):
        pass

class MacRemove(StartupRemove):
    def remove(self, command: str):
        pass

class WindowsRemove(StartupRemove):
    def remove(self, command: str):
        pass
