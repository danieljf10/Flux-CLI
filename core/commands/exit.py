from .CommandFormat import CommandFormat
import sys 

class Exit(CommandFormat):
    name = "exit"
    description = "exit the terminal"
    usage = "exit"

    def run(self, args, store=None):
        print("Bye Bye!")
        sys.exit()
