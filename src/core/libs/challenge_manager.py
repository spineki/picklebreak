"""
    Master library for challenge management.
"""

class Challenge ():
    """
        Challenge object.
    """

    def __init__ (self, level, win_frame, executer, key_gen):
        self.level = level
        self.win_frame = win_frame
        self.executer = executer
        self.key = key_gen
        self.objs = []

        self.win_frame.create()
    
    def reset (self):
        """
            Reset function called on first load, refresh and pre-code execution.
        """

        self.key.gen(self.level.name)

        ext_hints = [h[1] for h in self.level.hints]
        self.new_hints, self.new_scripts, self.objs = self.level.gen(self.key.get_key(self.level.name), ext_hints, self.level.scripts)

        parsed = [(self.level.hints[i][0], self.new_hints[i]) for i in range(len(self.level.hints))]
        self.win_frame.update(parsed, self.new_scripts)
    
    def out (self):
        """
            Out / close function called on leaving or pre-code execution.
        """

        self.level.close(self.key.get_key(self.level.name), self.objs)
    
    def execute (self):
        """
            Code execution.
        """

        self.out()
        self.reset()

        script = self.win_frame.get_script()

        self.executer.set_script(script)

        extracted_value = ""
        def send_key (val):
            global extracted_value
            extracted_value = val

        failed, code_out, code_error = self.executer.run_user_script(self.level.imports, {"send_key": send_key})

        return self.key.check(extracted_value, self.level.name), failed, code_out, code_error