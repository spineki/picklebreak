import sys
from io import StringIO

from src.core.libs.GUI.test import Application
from src.core.libs.level_loader import LevelLoader

class Core:
    def __init__(self):
        # self.window = Application()
        self.level_loader = LevelLoader()

    def handle_user_code(self):
        """
        A function that handle user code:
        First, verifies imports statements, then executes code, finally returns out and errors
        ARGS:
            None
        RETURN:
            pour le moment, wip
        """

        user_code = "print('banane');x=0/0" # normally, caught from the gui

        # here, Yohan verification.
        #
        # here, launch user code
        user_code_result = self.run_user_code(user_code)
        return user_code_result

    def run_user_code(self, user_code):
        """
        run user code and catch errors
        ARGS:
            None
        RETURN:
            TRUE if the code was successfully executed, else False
        """
        #user_code = self.window.get_code()
        error = "No error"
        # create file-like string to capture output
        codeOut = StringIO()

        # capture output and errors
        sys.stdout = codeOut

        try:
            exec(user_code)
            return True

        except Exception as e:
            error = str(e)
            return False

        finally:
            sys.stdout = sys.__stdout__
            code_out = codeOut.getvalue()
            print("Out: " + code_out)
            print("Error: " + error)
            codeOut.close()


if __name__ == '__main__':
    core = Core()
    print(core.handle_user_code())