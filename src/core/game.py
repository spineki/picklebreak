"""
    Master object, controlling everything.
"""

from libs.challenge_manager import Challenge
from libs.key_gen import Key
from libs.level_manager import load_level
from libs.user_code_manager import Executer
# from libs.gui.fram import WinFrame

class Core ():
     
    def __init__ (self):
        self.challenge = None
        self.app = None
        # Here loads and init tkinter app

        self.win_frame = None

    def load_challenge (self, name):
        level = load_level(name)
        self.challenge = Challenge(level, self.win_frame, Executer(), Key())

        self.challenge.setter()
        self.challenge.reset()
    
    def execute (self):
        checked, failed, code_out, code_error = self.challenge.execute()
    
    def refresh (self):
        self.challenge.out()
        self.challenge.reset()