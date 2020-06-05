from typing import *
import argparse
import platform
import startuppy
import sys

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    prog="startuppy",
    description="StartupPy CLI"
)

def args(arguments: List[str] = None) -> argparse.Namespace:
    if arguments is None:
        arguments: List[str] = sys.argv[1:]
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-a",
        "--add",
        help="adds a command to startup."
    )
    group.add_argument(
        "-r",
        "--remove",
        help="removes a command from startup."
    )
    return parser.parse_args(arguments)

class Main:
    def __init__(self):
        self.arguments: argparse.Namespace = args()

    def add_remove(self, command: str):
        try:
            startup: startuppy.Startup = startuppy.Startup(command)
        except FileNotFoundError:
            parser.error(f"command '{self.arguments.add or self.arguments.remove}' is not found")
            return
        except EnvironmentError:
            parser.error(f"your operating system, '{platform.system()}', is currently not compatible with StartupPy.")
            return

        try:
            return startup.remove if args().remove else startup.add()
        except EnvironmentError:
            parser.error("linux init system is unknown")

    def main(self):
        # if add argument not passed, go for the remove argument
        self.add_remove(self.arguments.add or self.arguments.remove)


if __name__ == '__main__':
    main: Main = Main()
    main.main()
