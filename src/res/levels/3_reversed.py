from os import path, mkdir
from shutil import rmtree, copyfile


def gen(key, hints_data, scripts):
    new_s = scripts.copy()

    if path.isdir("./loaded"):
        rmtree("./loaded")

    mkdir("./loaded")

    copyfile("./src/res/images/1_pic.jpg", hints_data[1])

    new_s[1] = new_s[1].format(key[::-1])
    new_s[:-1] = ["\n".join(new_s[:-1])]

    return hints_data.copy(), new_s, []


def close(key, objs):
    pass