from commands import commands
from storage.json_storage import JSONStorage
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "..", "config.json")

storage = JSONStorage(CONFIG_FILE)

os.system("cls" if os.name == "nt" else "clear")

def start():
    while True:
        input_stream = input("User > ").strip()
        if not input_stream:
            continue

        tokens = input_stream.split()
        command_name = tokens[0]
        args = tokens[1:]

        # find the command by name
        cmd = commands.get(command_name)
        if cmd:
            cmd.run(args,storage, commands)
            if storage:
                storage.add_to_history(input_stream)
        else:
            print("Command not recognized. Please enter 'help'")

start()
