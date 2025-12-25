from .CommandFormat import CommandFormat

class Set(CommandFormat):
    name = "set"
    description = ""
    usage = ""

    def run(self, args, store=None):
        key = args[0]
        value = " ".join(args[1:])
        store.set_field(key, value)