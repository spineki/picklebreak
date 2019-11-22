from pytest import *
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
from core.libs.key_gen import Key
import json

def test_gen():
    key = Key()
    key.gen()
    assert len(key.loaded_key) == 64

def test_get_key():
    key = Key()
    key.gen()
    assert key.get_key() == key.loaded_key

def test_check():
    key = Key()
    key.gen()
    key.check(key.loaded_key)
    assert key.valid