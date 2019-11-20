"""
    Master object, controlling everything.
"""

from src.core.libs.challenge_manager import Challenge
from src.core.libs.key_gen import Key
from src.core.libs.level_manager import Level
from src.core.libs.user_code_manager import Executer
from src.core.libs.gui import Application

class Core ():
    """
        Object that links the frontend with the backend and controls the game.
    """
     
    def __init__ (self):
        self.challenge = None
        self.app = Application()

        @self.app.set_exec_fct
        def execute ():
            checked, failed, code_out, code_error = self.challenge.execute()
            print(checked, failed, code_out, code_error)
    
        @self.app.set_reset_fct
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
    
    def run (self):
        self.app.mainloop()