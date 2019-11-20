"""
    Library used to manage levels.
"""

import importlib
import json
import os

LEVELS_FILE = "src/res/levels/levels.json"

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

    def __init__(self, json_data):
        self.name = json_data["id"]
        self.next = json_data["next"]
        self.imports = json_data["imports"]
        self.scripts = json_data["scripts"]

        #backend_import = importlib.import_module("src.res.levels." + json_data["backend"])
        #self.gen = backend_import.gen
        #self.close = backend_import.close

        self.hints = []
        for h in json_data["hints"]:
            e = (h["type"], h["data"])
            self.hints.append(e)

def load_level(level,file = LEVELS_FILE):
    """
        Load a level from its name.
    """

    with open(file, 'r') as f:
        dic = json.load(f)
    return dic[level]

def write_level (level = None, backend_file = None,file = LEVELS_FILE):
    """
        Write a new level to the json. Creates an empty one if no args are passed
    """

    with open(file, 'r') as f:
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
    
    with open(file, 'w') as f:
        json.dump(dic, f, indent=4)

def del_level(level,file= LEVELS_FILE):
    """
        Deletes a level from its object or name.
    """

    fichier = open(file,'r')
    dic = json.load(fichier)
    fichier = open(file,'w')
    del dic[str(level)]
    json.dump(dic,fichier,indent=4)
    fichier.close()