import sys
from io import StringIO
from src.core.libs.import_check import has_valid_imports

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