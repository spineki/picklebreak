import os.path as p
import json

SAVE_FILE = "src/res/save.txt"

class Save ():

    def __init__ (self, default, filename = SAVE_FILE):
        self.save_dict = {}
        self.file = filename

        if not p.isfile(filename):
            self.save_dict = {"level": default}
            with open(filename, "w") as f:
                json.dump(self.save_dict, f)
        
        else:
            with open(filename, "r") as f:
                self.save_dict = json.load(f)
    
    def setter (self, val):
        self.save_dict["level"] = val
        self.save(filename = self.file)
    
    def save (self, filename = SAVE_FILE):
        with open(filename, 'w') as f:
            json.dump(self.save_dict, f)