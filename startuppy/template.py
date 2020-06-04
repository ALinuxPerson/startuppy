from startuppy.remove import StartupRemove
from startuppy.add import StartupAdd

class Startup:
    def __init__(self, add: StartupAdd, remove: StartupRemove):
        self._add: StartupAdd = add
        self._remove: StartupRemove = remove

    def add(self):
        pass

    def remove(self):
        pass
