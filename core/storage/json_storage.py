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

    def set_field(self, key, value): 
        user = self.load()
        user[key] = value 
        self.save(user)