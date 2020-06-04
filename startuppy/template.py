from startuppy.remove import StartupRemove
from startuppy.add import StartupAdd

class Startup:
    def __init__(self, add: StartupAdd, remove: StartupRemove, command: str):
        self._add: StartupAdd = add
        self._remove: StartupRemove = remove
        self.command: str = command

    def add(self, command: str):
        pass

    def remove(self, command: str):
        pass
