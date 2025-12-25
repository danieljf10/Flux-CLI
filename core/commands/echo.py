from .CommandFormat import CommandFormat

class Echo(CommandFormat):
    name = "echo"
    description = "print a message to terminal"
    usage = "echo <message>"

    def run(self, args, store=None, commands=None):
        COLOR = "\033[36m"
        RESET = "\033[0m"

        print(f"{COLOR}flux >{RESET}"," ".join(args))
