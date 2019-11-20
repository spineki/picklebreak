from pytest import *
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from core.libs.level_manager import Level

def test_load_level():
    """ 
    Test of the data of a level from the json file
    """

    level = Level("pickle_level",levels_file = "json_test_file.json") 
    assert level.name == "26"
    assert level.next == "27"
    assert level.scripts == ["print(\"This script cannot be modified\")",""]
    assert level.imports == ["i","m","p","o","r","t","s"]
    assert level.hints == [('text', "WOW!!! The key is {}")]

def test_write_level():
    """
    Test to write in the json file
    """
    
    level = Level("pickle_level",levels_file = "json_test_file.json")
    level2 = Level("pickle_level",levels_file = "json_test_file.json")
    level.name = "34"
    Level.write(level, levels_file = "json_test_file.json")
    level.name = "45"
    level.write(level,levels_file = "json_test_file.json")
    assert level2 != level