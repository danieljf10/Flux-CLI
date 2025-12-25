from commands import commands
from storage.json_storage import JSONStorage
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "..", "config.json")

storage = JSONStorage(CONFIG_FILE)
    

def start():
    while True:
        input_stream = input("User > ").strip()
        if not input_stream:
            continue

        tokens = input_stream.split()
        command_name = tokens[0]
        args = tokens[1:]

        # find the command by name
        cmd = next((c for c in commands if c.name == command_name), None)

        if cmd:
            cmd.run(args,storage)
        else:
            print("Command not recognized. Please enter 'help'")

start()
