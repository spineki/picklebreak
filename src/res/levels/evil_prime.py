from os import path, mkdir
from shutil import rmtree, copyfile


def gen(key, hints_data, scripts):
    new_s = scripts.copy()

    if path.isdir("./loaded"):
        rmtree("./loaded")

    mkdir("./loaded")

    copyfile("./src/res/images/evil_prime.png", hints_data[2])
    new_key = 4973 * int(key,16)
    new_s[2] = new_s[2].format(new_key)

    new_s[:-1] = ["\n".join(new_s[:-1])]

    return hints_data.copy(), new_s, []


def close(key, objs):
    pass

