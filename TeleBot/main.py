import sys

from .core.commands.main import handle_commands


def command():
    args = sys.argv
    if len(args) > 1:
        handle_commands(args[1:])
    else:
        print("Please provide atleast one argument")
