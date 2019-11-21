from pytest import *
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from core.libs.user_code_manager import Executer

def test_set_script():
    executer = Executer()
    executer.set_script("this is a script")
    assert executer.script == "this is a script\n"

def test_get_import_list():
    assert True

def test_get_extended_import_list():
    assert True