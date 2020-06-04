class StartupAdd:
    def add(self, command: str):
        raise NotImplementedError

class SystemDLinuxAdd:
    def add(self, command: str):
        pass

class UpstartLinuxAdd:
    def add(self, command: str):
        pass

class SysVInitLinuxAdd:
    def add(self, command: str):
        pass

class MacAdd(StartupAdd):
    def add(self, command: str):
        pass

class WindowsAdd(StartupAdd):
    def add(self, command: str):
        pass
