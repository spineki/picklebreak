import os.path as p
import json

SAVE_FILE = "src/res/save.txt"

class Save ():

    def __init__ (self, default, filename = SAVE_FILE):
        self.save = {}

        if not p.isfile(filename):
            self.save = {"level": default}
            with open(filename, "w") as f:
                json.dump(self.save, f)
        
        else:
            with open(filename, "r") as f:
                self.save = json.load(f)
    
    def setter (self, val):
        self.save["level"] = val
        self.save()
    
    def save (self, filename = SAVE_FILE):
        with open(filename, 'w') as f:
            json.dump(self.save, f)