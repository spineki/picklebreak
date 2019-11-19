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

def get_import_list (script):
    """
        Retrieve basic import list of the user's script.
        "import X" is translated to X.
        "from X import Y" is translated to X.Y.
    """

    matches = re.findall(IMPORT_REGEXP, script)
    imports = [e[1] for e in matches if e[1] != ""]
    froms = [e[0] for e in matches if e[0] != ""]

    imports = [re.sub(IMPORT_REP, "", e) for e in imports]
    froms = [re.sub(FROM_REP, "", e) for e in froms]
    froms = [re.sub(FROM_SPLIT, ".", e) for e in froms]

    return imports + froms

def get_extended_import_list (script):
    """
        Retrieve the extended list of imports.
        X.Y.Z is translated to [X, X.Y, X.Y.Z].
    """

    l = get_import_list(script)
    ret = []
    for e in l:
        n_e = e.split(".")
        ret.append([".".join(n_e[:i + 1]) for i in range(len(n_e))])
    return ret

def has_valid_imports (script, import_list):
    """
        Checks if the script has a valid import list. If not, returns the invalid module.
    """

    script_imports = get_extended_import_list(script)
    ret = True

    for imp in script_imports:
        ret = True in [ext in import_list for ext in imp]
        if not ret: return ret, imp[-1]
    
    return ret, None

def run_user_script (script, valid_imports, glob = {}):
    """
        Function that runs script under a restricted environment.
    """

    script += "\n"

    failed, code_out, code_error = False, "", ""

    imp_res, imp_issue = has_valid_imports(script, valid_imports)

    if not imp_res:
        failed = True
        code_error = "ImportError: {} module cannot be imported. Unauthorised import.".format(imp_issue)
        return failed, code_out, code_error
    
    print_catch = StringIO()
    sys.stdout = print_catch

    try:
        exec(script, glob)
        failed = False
    
    except Exception as e:
        code_error = "Exception in script execution: {}".format(str(e))
        failed = True
    
    finally:
        sys.stdout = sys.__stdout__
        code_out = print_catch.getvalue()
        print_catch.close()

        return failed, code_out, code_error