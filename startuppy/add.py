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

class MacAdd(StartupAdd):
    def add(self, command: str):
        pass

class WindowsAdd(StartupAdd):
    def add(self, command: str):
        pass
