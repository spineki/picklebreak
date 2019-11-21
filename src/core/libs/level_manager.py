"""
    Library used to manage levels.
"""

import importlib
import json

LEVELS_FILE = "src/res/levels/levels.json"
LEVELS_JSON = None

class Level ():
    """
        Object representing a level. It needs to be loaded from a json file with collected functions.
        The json file for a level must looks like:
        {
            "id"        : <level id>,
            "next"      : <next level name>,
            "backend"   : <backend script file>,
            "scripts"   : [<script sets>, ...],
            "imports"   : [<valid module name>, ...],
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

    def __init__ (self, level_name, levels_file = LEVELS_FILE):
        global LEVELS_JSON
        if LEVELS_JSON == None:
            with open(levels_file, 'r') as f:
                LEVELS_JSON = json.load(f)
        
        json_data = LEVELS_JSON[level_name]

        self.name = json_data["id"]
        self.next = json_data["next"]
        self.imports = json_data["imports"]
        self.scripts = json_data["scripts"]
        try:
            backend_import = importlib.import_module("src.res.levels." + json_data["backend"])
        except ModuleNotFoundError:
            backend_import = importlib.import_module("res.levels." + json_data["backend"],"src")
        self.gen = backend_import.gen
        self.close = backend_import.close
        
        self.hints = []
        for h in json_data["hints"]:
            e = (h["type"], h["data"])
            self.hints.append(e)

    @staticmethod
    def write (level = None, backend_file = None, levels_file = LEVELS_FILE):
        """
            Write a new level to the json. Creates an empty one if no args are passed
        """

        with open(levels_file, 'r') as f:
            dic = json.load(f)

        if level == None: # Create a new level if level == None

            new_name = "new_0"
            while new_name in dic:
                new_name = "new_" + str(int(new_name[4:]) + 1)

            dic[new_name] = {
                "id": new_name,
                "next": "",
                "backend": "",
                "scripts": [""],
                "imports": [],
                "hints": []
            }

        else:
            dic[level.name] = {
                "id": level.name,
                "next": level.next,
                "backend": backend_file,
                "scripts": level.scripts,
                "imports": level.imports,
                "hints": [
                    {
                        "type": h[0],
                        "data": h[1]
                    } for h in level.hints
                ]
            }
        
        with open(levels_file, 'w') as f:
            json.dump(dic, f, indent=4)

    @staticmethod
    def delete (level,levels_file=LEVELS_FILE):
        """
            Deletes a level from its object or name.
        """

        with open(levels_file, "r") as f:
            dic = json.load(f)

        if isinstance(level, Level):
            del dic[level.name]
        else:
            del dic[level]

        with open(LEVELS_FILE, 'w') as f:
            json.dump(dic, f, indent=4)
