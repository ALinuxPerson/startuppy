import argparse

parser: argparse.ArgumentParser = argparse.ArgumentParser(description="StartupPy CLI")
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
arguments = parser.parse_args()
