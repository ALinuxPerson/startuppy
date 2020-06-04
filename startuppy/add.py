class StartupAdd:
    def add(self):
        raise NotImplementedError

class LinuxAdd(StartupAdd):
    def add(self):
        pass

class MacAdd(StartupAdd):
    def add(self):
        pass

class WindowsAdd(StartupAdd):
    def add(self):
        pass
