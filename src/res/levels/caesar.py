from os import path, mkdir
from shutil import rmtree, copyfile


#Key have 48 characters


def gen (key, hints_data, scripts):
    new_s = scripts.copy()
    dico = {"y" : "a", "z" :"b", "8": "0", "9": "1"}
    new_key = ""
    for i in key:
        if(i in dico):
            new_key += dico[i]
        else:
            new_key += chr(ord(i) + 2)
    

  
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    copyfile("./src/res/images/caesar.jpg", hints_data[1])
  
    new_s[1] = new_s[1].format(new_key)
    new_s[:-1] = ["\n".join(new_s[:-1])]
    
    return hints_data.copy(), new_s, []

def close (key, objs):
    pass