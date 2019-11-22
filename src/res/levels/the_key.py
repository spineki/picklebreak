from os import path, mkdir
from shutil import rmtree, copyfile

def gen (key, hints_data, scripts):
    new_s = scripts.copy()
    
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    
    copyfile("./src/res/images/15_the_key.jpg", hints_data[1])
    scripts[6]=scripts[6].format(key)
    return hints_data.copy(),new_s,[]

def close (key, objs):
    pass