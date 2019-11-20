"""
    Basic lib to manage the challenges keys.
"""

from random import random
from time import time_ns
import hashlib

class Key ():

    def __init__ (self):
        self.loaded_key = ""
        self.valid = False

    def gen (self):
        """
            Used to create and retrieve the key to resolve the challenge.
        """

        # This function is used whenever a random byte is needed.
        f = lambda : int(random() * random() * time_ns()/10000) % 0x100

        st = hashlib.new("sha256")
        for i in range(f() * f()): st.update(bytes([f() for j in range(f() % 0x10)]))

        self.loaded_key = st.hexdigest()
        self.valid = False
    
    def get_key (self):
        return self.loaded_key

    def check (self, key_check):
        """
            Check if the entered key is correct.
        """

        self.valid = self.loaded_key == key_check