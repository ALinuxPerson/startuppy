from startuppy.remove import StartupRemove
from startuppy.add import StartupAdd
import os

class Startup:
    def __init__(self, command: str):
        self.command: str = os.path.abspath(command)

    def add(self, command: str):
        pass

    def remove(self, command: str):
        pass
