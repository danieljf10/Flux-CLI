from .CommandFormat import CommandFormat
import json


class Flux(CommandFormat):
    name = "flux"
    description = "edit the config"
    usage = "flux <subcommand> [args]"

    subcommands = ["show","set", "get", "reset"]
    subcommand_description = ["show a list of flux config settings", "set a flux config setting", "get a flux config setting", "reset flux config settings"]
    subcommand_usage = ["show", "set <key> <value>", "get <key>","reset"]

    def run(self, args, store=None, commands=None):
        if not args:
            for x, y, z in zip(self.subcommands, self.subcommand_description, self.subcommand_usage):
                print(f"{x:<10} {z:<20} {y}")
            return
        sub = args[0]
        
        key = args[1] if len(args) > 1 else None
        value = args[2] if len(args) > 2 else None

        if store: 
            data = store.load()
            match sub: 
                case "show":
                    for k, v in data.items():
                        print(f"{k} : {v}")
                    return
                case "set":
                    data[key] = value 
                    store.save(data)
                    return
                case "get":
                    print(data[key])
                    return
                case "reset":
                    store.create_user()
                    print("config has been reset...")   
                    return
            print("Unknown flux command. Please type 'flux' for a list of flux commands.")
        return