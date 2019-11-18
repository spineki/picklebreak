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
        error = "No error"
        user_code = "print('banane');x=0/0"
        # create file-like string to capture output
        codeOut = StringIO()
        # capture output and errors
        sys.stdout = codeOut

        try:
            exec(user_code)

        except Exception as e:
            error = str(e)

        finally:
            sys.stdout = sys.__stdout__
            code_out = codeOut.getvalue()
            print("out: " + code_out)
            print("error: " + error)
            codeOut.close()


if __name__ == '__main__':
    core = Core()
    core.run_user_code()