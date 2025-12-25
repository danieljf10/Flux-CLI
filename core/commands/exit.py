from .CommandFormat import CommandFormat
import sys 

class Exit(CommandFormat):
    name = "exit"
    description = "exit the terminal"
    usage = "exit"

    def run(self, args, store=None, commands=None):
        print("Disconnecting...")
        sys.exit()
