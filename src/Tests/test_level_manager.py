from pytest import *
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from core.libs.level_manager import load_level,write_level,Level

def test_load_level():
    level = Level("pickle_level",file = "json_test_file.json")
    #level = Level(json_data)
    assert level.name == "26"
    assert level.next == "27"
    assert level.scripts == ["print(\"This script cannot be modified\")",""]
    assert level.imports == ["i","m","p","o","r","t","s"]
    assert level.hints == [('text', "WOW!!! The key is {}")]

def test_write_level():
    level = Level("pickle_level",file = "json_test_file.json")
    level.name = "34"
    Level.write(level, file = "json_test_file.json")
    level.name = "45"
    level.write(file = "json_test_file.json")
    json_data = load_level("34",file = "json_test_file.json")
    level2=Level(json_data)
    assert level2 != level