class StartupAdd:
    pass

class StartupRemove:
    pass

class Startup:
    def __init__(self, add: StartupAdd, remove: StartupRemove):
        self._add: StartupAdd = add
        self._remove: StartupRemove = remove
