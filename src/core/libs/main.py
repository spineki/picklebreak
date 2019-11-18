import sys
from io import StringIO

from src.core.libs.GUI.test import Application


class Core:
    def __init__(self):
        # self.window = Application()
        pass

    def handle_user_code(self, user_code):
        """
        A function that handle user code:
        First, verifies imports statements, then executes code, finally returns out and errors
        ARGS:
            None
        RETURN:
            pour le moment, wip
        """

        #user_code = "print('banane');x=0/0" # normally, caught from the gui

        # here, Yohann verification.
        #
        # here, launch user code
        code_bool, code_error, code_out = self.run_user_code(user_code)
        if code_out.strip() == "pickle":
            code_out += "\n Noice \n "
        code_out += "\n ********* \n "
        return code_bool, code_error, code_out

    def run_user_code(self, user_code):
        """
        run user code and catch errors
        ARGS:
            None
        RETURN:
            TRUE if the code was successfully executed, else False
        """
        #user_code = self.window.get_code()
        code_error = "No error"
        code_bool = True

        # create file-like string to capture output
        codeOut = StringIO()

        # capture output and errors
        sys.stdout = codeOut

        try:
            exec(user_code)


        except Exception as e:
            code_error = str(e)
            code_bool = False

        finally:
            sys.stdout = sys.__stdout__
            code_out = codeOut.getvalue()
            codeOut.close()
            return code_bool, code_error, code_out


if __name__ == '__main__':
    core = Core()
    print(core.handle_user_code())