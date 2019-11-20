from pytest import *
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from core.libs.level_manager import load_level,Level

def test_load_level():
    json_data = load_level("pickle_level",file = "json_test_file.json")
    level = Level(json_data)
    assert level.name == "26"
    assert level.next == "27"
    assert level.scripts == ["print(\"This script cannot be modified\")",""]
    assert level.imports == ["i","m","p","o","r","t","s"]
    assert level.hints == [('text', "WOW!!! The key is {}")]