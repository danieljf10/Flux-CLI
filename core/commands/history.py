from .CommandFormat import CommandFormat


class History(CommandFormat):
    name = "history"
    description = "see history"
    usage = "history"

    def run(self, args, store=None, commands=None):
        history = store.get_history()
        for i, cmd in enumerate(history, start=1):
            print(f"{i}: {cmd}")