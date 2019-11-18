"""
    Example of backend file.
"""

def gen (key, hints_data):
    """
        This function will be called on set and reset of the level.
        The level key and the hints_data are given as parameters.
        This function must returns a tuple with the first element beign a parsed version of
        hints_data and the second additionnal objects that needs to be closed is a special way.
    """

    new = hints_data.copy()
    new[0] = new[0].format(key)

    return new + [5]

def close (key, objs):
    """
        This fuction is called on exit and reset of the level (before gen).
        It is used to softly close / kill objects or do post-level cleaning.
    """

    print(objs[0])