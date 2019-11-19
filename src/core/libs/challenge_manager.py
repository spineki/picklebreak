"""
    Master library for challenge management.
"""

from src.core.libs.user_code_manager import run_user_script

class Challenge ():

    def __init__ (self, level, win_frame):
        self.level = level
        self.win_frame = win_frame
        self.key = ""
        self.objs = []
    
    def reset (self):
        """
            Reset function called on first load, refresh and pre-code execution.
        """

        self.key = "" # NEW KEY GEN

        ext_hints = [h[1] for h in self.level.hints]
        self.new_hints, self.new_scripts, self.objs = self.level.gen(self.key, ext_hints, self.level.scripts)

        parsed = [(self.level.hints[i][0], self.new_hints[i]) for i in range(len(self.level.hints))]
        # UPDATE WIN_FRAME
    
    def out (self):
        """
            Out / close function called on leaving or pre-code execution.
        """

        self.level.close(self.key, self.objs)
    
    def execute (self): # , script) SCRIPT AS PARAMETER
        """
            Code execution.
        """

        self.out()
        self.reset()

        script = "" # OR RETRIEVE CODE FROM WINFRAME

        extracted_value = ""
        def send_key (val): extracted_value = val

        run_user_script(script, self.level.imports, {"send_key": send_key})

        return extracted_value == self.key