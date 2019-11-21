from pytest import *
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from core.libs.save import Save
import json



def test_save():
    default = "0_the_basics"
    filename = "save.txt"
    a = Save(default,filename="save.txt")
    a.save_dict = {"level": "2_test_pickle"}
    a.save(filename)
    with open(filename, 'r') as f:
        verif = json.load(f)
    assert verif == {"level": "2_test_pickle"}

def test_setter():
    default = "0_the_basics"
    a = Save(default,filename="save.txt")
    a.setter("2_test_pickle")
    assert a.save_dict == {"level": "2_test_pickle"}
    a.setter("1_test")
