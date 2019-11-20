"""
    Master object, controlling everything.
"""

from libs.challenge_manager import Challenge
from libs.key_gen import Key
from libs.level_manager import Level
from libs.user_code_manager import Executer
# from libs.gui.fram import WinFrame

class Core ():
    """
        Object that links the frontend with the backend and controls the game.
    """
     
    def __init__ (self):
        self.challenge = None
        self.app = None

        def execute ():
            checked, failed, code_out, code_error = self.challenge.execute()
    
        def refresh ():
            self.challenge.out()
            self.challenge.reset()

    def load_challenge (self, name):
        """
            Load a challenge from level name.
        """

        level = Level(name)
        self.challenge = Challenge(level, self.app, Executer(), Key())

        self.challenge.reset()