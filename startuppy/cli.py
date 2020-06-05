from typing import *
import argparse
import platform
import sys

parser: argparse.ArgumentParser = argparse.ArgumentParser(description="StartupPy CLI")

def args(arguments: List[str] = None) -> argparse.Namespace:
    if arguments is None:
        arguments: List[str] = sys.argv[1:]
    group = parser.add_mutually_exclusive_group()
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

def add():
    pass

def remove():
    pass

def main():
    arguments: argparse.Namespace = args()
    current_os: str = platform.system()
    if current_os not in ("Linux", "Windows", "Darwin"):
        parser.error(f"your operating system, '{current_os}', is currently not compatible with startup.")


if __name__ == '__main__':
    main()
