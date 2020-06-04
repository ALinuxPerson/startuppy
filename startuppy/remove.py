class StartupRemove:
    def remove(self):
        raise NotImplementedError

class LinuxRemove(StartupRemove):
    def remove(self):
        pass

class MacRemove(StartupRemove):
    def remove(self):
        pass

class WindowsRemove(StartupRemove):
    def remove(self):
        pass
