"""
    Master library for challenge management.
"""

class Challenge ():
    """
        Challenge object. Makes the link between every back-end object.
    """

    def __init__ (self, level, app, executer, key_gen):
        self.level = level
        self.app = app
        self.executer = executer
        self.key = key_gen
        self.objs = []

        self.key.gen()

        ext_hints = [h[1] for h in self.level.hints]
        self.new_hints, self.new_scripts, self.objs = self.level.gen(self.key.get_key(), ext_hints, self.level.scripts)

        parsed = [(self.level.hints[i][0], self.new_hints[i]) for i in range(len(self.level.hints))]
        self.app.turbo_init_level(parsed, self.new_scripts)
        self.level.close(self.key.get_key(), self.objs)
    
    def reset (self):
        """
            Reset function called on first load, refresh and pre-code execution.
        """

        self.key.gen()

        ext_hints = [h[1] for h in self.level.hints]
        self.new_hints, self.new_scripts, self.objs = self.level.gen(self.key.get_key(), ext_hints, self.level.scripts)

        parsed = [(self.level.hints[i][0], self.new_hints[i]) for i in range(len(self.level.hints))]
        self.app.turbo_update_level(parsed, self.new_scripts)
    
    def out (self):
        """
            Out / close function called on leaving or pre-code execution.
        """

        self.level.close(self.key.get_key(), self.objs)
    
    def execute (self):
        """
            Executes user's code and returns code's status.
        """

        self.out()
        self.reset()

        script = self.app.get_script()

        self.executer.set_script(script)

        failed, code_out, code_error = self.executer.run_user_script(self.level.imports, {"send_key": self.key.check})

        return self.key.valid, failed, code_out, code_error