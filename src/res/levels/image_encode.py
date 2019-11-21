from os import path, mkdir
from shutil import rmtree, copyfile
from PIL import Image
import numpy as np

#Key have 48 characters
#Image 1280*720

def gen (key, hints_data, scripts):
    new_s = scripts.copy()
    
    raw_img = Image.open("./src/res/images/image_encoded.jpg")
    np_img = np.array(raw_img)
    
    for i in range(len(key)):
        for c in range(3):
            for ofset in range(10):
                for h in range(10):
                    np_img[h][i*10+ofset][c] = int(key[i], 16)*10

    img = Image.fromarray(np_img)
  
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    
    img.save("./loaded/encoded.png")
    
    
    new_s[:-1] = ["\n".join(new_s[:-1])]
    
    return hints_data.copy(), new_s, []

def close (key, objs):
    pass