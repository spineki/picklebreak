import sys
from io import StringIO

from src.core.libs.GUI.test import Application
from src.core.libs.level_loader import LevelLoader

class Core:
    def __init__(self):
        # self.window = Application()
        self.level_loader = LevelLoader()

    def run_user_code(self):
        #user_code = self.window.get_code()

        # create file-like string to capture output
        codeOut = StringIO()
        codeErr = StringIO()

        # capture output and errors
        sys.stdout = codeOut
        sys.stderr = codeErr
        user_code = "print('banane')"

        exec(user_code)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        code_error = codeErr.getvalue()

        print("error: " + code_error)

        code_out = codeOut.getvalue()

        print("out: " + code_out)

        codeOut.close()
        codeErr.close()

if __name__ == '__main__':
    core = Core()
    core.run_user_code()