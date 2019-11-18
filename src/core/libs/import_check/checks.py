"""
    Lib that checks if the user's script imports valid modules.
"""

# re is Python's library for regular epressions
import re

# RegExes used for spliting and finding
IMPORT_REGEXP = r"(from[ \t]*[A-Za-z0-9._]+[ \t]*import[ \t]*[A-Za-z0-9._]+)|(import[ \t]*[A-Za-z0-9._]+)[\n; ]"
IMPORT_REP = r"import[ \t]*"
FROM_REP = r"from[ \t]*"
FROM_SPLIT = r"[ \t]*import[ \t]*"

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
        Checks if the script has a valid import list.
    """

    script_imports = get_extended_import_list(script)
    ret = True

    for imp in script_imports:
        ret = True in [ext in import_list for ext in imp]
        if ret: break
    
    return ret