from os import path, mkdir
from shutil import rmtree, copyfile
import pickle as p

def gen (key, hints_data, scripts):
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    
    copyfile("./src/res/images/pickle0.jpg", hints_data[1])
    
    pre_data = list(key)
    pre_data = p.dumps(pre_data)
    data = b'Good, you were able to open this file, what now?\nYou maybe want to have this key but you wonder where it\'s hidden. Well, it\'s here:' + pre_data
    data = p.dumps(data)
    
    with open("./loaded/ahah.p", "wb") as f:
        f.write(data)

    return hints_data.copy(), scripts.copy(), []

def close (key, objs):
    pass