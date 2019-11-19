"""
    Basic lib to manage the challenges keys.
"""

from random import random
from time import time_ns
import hashlib

class Key ():

    def __init__ (self):
        self.loaded_keys = {}

    def gen (self, id_name):
        """
            Used to create and retrieve the key to resolve the challenge.
        """

        # This function is used whenever a random byte is needed.
        f = lambda : int(random() * random() * time_ns()/10000) % 0x100

        st = hashlib.new("sha256")
        for i in range(f() * f()): st.update(bytes([f() for j in range(f() % 0x10)]))

        self.loaded_keys[id_name] = st.hexdigest()

    def check (self, key_check, id_name):
        """
            Check if the entered key is correct.
        """

        return self.loaded_keys[id_name] == key_check

    def clear_keys (self, keys = []):
        """
            Clears the loaded keys. If keys = 'all', removes all the loaded keys.
        """

        if keys == "all":
            self.loaded_keys.clear()
        else:
            for k in keys: del self.loaded_keys[k]