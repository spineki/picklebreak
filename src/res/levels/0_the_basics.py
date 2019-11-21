from os import path, mkdir
from shutil import rmtree, copyfile

def gen (key, hints_data, scripts):
    new_s = scripts.copy()
    
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    
    copyfile("./src/res/images/0_pic.jpg", hints_data[1])
    
    for i in range(len(new_s)):
        new_s[i] = new_s[i].format(key)
    
    new_s[:-1] = ["\n".join(new_s[:-1])]

    return hints_data.copy(), new_s, []

def close (key, objs):
    pass