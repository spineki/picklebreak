import importlib
import json

LEVELS_FILE = "src/res/levels/levels.json"

class Level ():
    """
        Object representing a level. It needs to be loaded from a json file with collected functions.
        The json file for a level must looks like:
        {
            "id"        : <level name>,
            "next"      : <next level name>,
            "backend"   : <backend script file>
            "hints"     : [{
                "type"  : <data type>
                "data"  : <file path>/<text>
                },
                { ... }, ... ]
        }

        Backend script file must be composed of 2 functions and be located in src/res/levels/:
            gen (key, hints_data)   -> Builds everything needed for the level. Returns a list of useable objects.
            close (key, objs)       -> Smoothly kills everything.
    """

    def __init__ (self, json_data):
        self.name = json_data["id"]
        self.next = json_data["next"]

        backend_import = importlib.import_module("src.res.levels." + json_data["backend"])
        self.gen = backend_import.gen
        self.close = backend_import.close

        self.hints = []
        for h in json_data["hints"]:
            e = (h["type"], h["data"])
            self.hints.append(e)

def load_level (level):
    with open(LEVELS_FILE, 'r') as f:
        dic = json.load(f)
    return Level(dic[level])

def write_level (level = None, backend_file = None):
    with open(LEVELS_FILE, 'r') as f:
        dic = json.load(f)

    if level == None: # Create a new level if level == None

        L = list(dic.keys())
        for i in range(len(L)):
            L[i] = int(L[i])
        maximum = max(L) # Search for maximum to create a new level

        dic[str(maximum + 1)] = {
            "id": maximum + 1,
            "next": "",
            "backend": "",
            "hints": []
        }

    else:
        dic[level.name] = {
            "id": level.name,
            "next": level.next,
            "backend": backend_file,
            "hints": [
                {
                    "type": h[0],
                    "data": h[1]
                } for h in level.hints
            ]
        }
    
    with open(LEVELS_FILE, 'r') as f:
        json.dump(dic, f, indent=4)

def del_level (level):
    with open(LEVELS_FILE, "r") as f:
        dic = json.load(f)

    del dic[level.name]

    with open(LEVELS_FILE, 'r') as f:
        json.dump(dic, f, indent=4)