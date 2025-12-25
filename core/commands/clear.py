from .CommandFormat import CommandFormat
import os

class Clear(CommandFormat):
    name = "clear"
    description = "clear the terminal"
    usage = "clear"

    def run(self, args, store=None, commands=None):
        os.system("cls" if os.name == "nt" else "clear")