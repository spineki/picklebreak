"""
    Library that checks and execute user's script.
"""

import sys
from io import StringIO
import re

# RegExes used for spliting and finding
IMPORT_REGEXP = r"(from[ \t]+[A-Za-z0-9._]+[ \t]+import[ \t]+[A-Za-z0-9._]+)|(import[ \t]+[A-Za-z0-9._]+)[\n; ]"
IMPORT_REP = r"import[ \t]+"
FROM_REP = r"from[ \t]+"
FROM_SPLIT = r"[ \t]+import[ \t]+"

class Executer ():

    def __init__ (self):
        self.script = ""

    def set_script (self, script):
        self.script = script + "\n"

    def get_import_list (self):
        """
            Retrieve basic import list of the user's script.
            "import X" is translated to X.
            "from X import Y" is translated to X.Y.
        """

        matches = re.findall(IMPORT_REGEXP, self.script)
        imports = [e[1] for e in matches if e[1] != ""]
        froms = [e[0] for e in matches if e[0] != ""]

        imports = [re.sub(IMPORT_REP, "", e) for e in imports]
        froms = [re.sub(FROM_REP, "", e) for e in froms]
        froms = [re.sub(FROM_SPLIT, ".", e) for e in froms]

        return imports + froms

    def get_extended_import_list (self):
        """
            Retrieve the extended list of imports.
            X.Y.Z is translated to [X, X.Y, X.Y.Z].
        """

        l = self.get_import_list()
        ret = []
        for e in l:
            n_e = e.split(".")
            ret.append([".".join(n_e[:i + 1]) for i in range(len(n_e))])
        return ret

    def has_valid_imports (self, import_list):
        """
            Checks if the script has a valid import list. If not, returns the invalid module.
        """

        script_imports = self.get_extended_import_list()
        ret = True

        for imp in script_imports:
            ret = True in [ext in import_list for ext in imp]
            if not ret: return ret, imp[-1]
        
        return ret, None

    def run_user_script (self, valid_imports, glob = {}):
        """
            Function that runs script under a restricted environment.
        """

        failed, code_out, code_error = False, "", ""

        imp_res, imp_issue = self.has_valid_imports(valid_imports)

        if not imp_res:
            failed = True
            code_error = "ImportError: {} module cannot be imported. Unauthorised import.".format(imp_issue)
            return failed, code_out, code_error
        
        print_catch = StringIO()
        sys.stdout = print_catch

        try:
            exec(self.script, glob)
            failed = False
        
        except Exception as e:
            code_error = "{} in script execution: {}".format(type(e).__name__, e)
            failed = True
        
        finally:
            sys.stdout = sys.__stdout__
            code_out = print_catch.getvalue()
            print_catch.close()

            return failed, code_out, code_error