from .CommandFormat import CommandFormat

class Help(CommandFormat):
    name = "help"
    description = "prints this list"
    usage = "help"

    def run(self, args, store=None, commands=None):
        for cmd in commands.values():
            print(f"{cmd.usage:<30} {cmd.description}")
