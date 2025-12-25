from .CommandFormat import CommandFormat

class Say(CommandFormat):
    name = "say"
    description = ""
    usage = ""

    def run(self, args, store=None):
        print("[Server] >"," ".join(args))
