import json 
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "..", "config.json")

new_user = {
    "name": "",
    "theme":"dark",
    "command_history": [],
    "last_command":"",
    "history_limt": 5
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        save_settings(new_user)
        return new_user
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_settings(settings): 
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file, indent=4)

def edit_settings(args):
    field = args[0]
    value = " ".join(args[1:])

    settings = load_settings()
    if field == "name":
        settings["name"] = value
    save_settings(settings)    
    
def add_to_history(command):
    settings = load_settings()
    history = settings.get("command_history", [])
    history.append(command)
    history = history[-settings.get("history_limit", 5):]
    settings["command_history"] = history
    settings["last_command"] = command
    save_settings(settings)

def get_history():
    settings = load_settings()
    return settings.get("command_history")

load_settings()
    