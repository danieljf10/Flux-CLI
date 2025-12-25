from .BaseStorage import BaseStorage
import json
import os 

class JSONStorage(BaseStorage):
    def __init__(self, filename):
        self.filename = filename 
        if not os.path.exists(self.filename):
            self.create_user()
    
    def load(self):
        with open(self.filename, "r") as file:
            return json.load(file)
    
    def save(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def create_user(self):
        default_user = {
            "username":"User",
            "servername":"Server",
            "theme":"dark",
            "command_history":[],
            "last_command":"",
            "history_limit":5
        }
        self.save(default_user)

    def add_to_history(self, command):
        current_settings = self.load()
        history = current_settings.get("command_history", [])
        history.append(command)
        history = history[-current_settings.get("history_limit", 5):]
        current_settings["command_history"] = history
        current_settings["last_command"] = command
        self.save(current_settings)
    
    def get_history(self):
        current_settings = self.load()
        return current_settings.get("command_history")


