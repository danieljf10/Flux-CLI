from .CommandFormat import CommandFormat
import json


class Flux(CommandFormat):
    name = "flux"
    description = "edit the config"
    usage = "flux <subcommand> [args]"

    subcommands = ["show","set", "get", "reset"]

    def run(self, args, store=None, commands=None):
        if not args:
            return
        sub = args[0]
        subsub = args[1:]

        match sub: 
            case "show":
                if store:
                    data = store.load()
                    for k, v in data.items():
                        print(f"{k} : {v}")
            case "set":
                print("set commands")
            case "get":
                print("get commands")
            case "reset":
                if store:
                    store.create_user()
                print("config has been reset...")
               
        return