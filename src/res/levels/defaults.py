"""
    Example of backend file.
"""

def gen (key, hints_data, scripts):
    """
        This function will be called on set and reset of the level.
        The level key, the hints_data and the scripts table are given as parameters.
        This function must returns a tuple with the 2 first elements being a parsed version of
        hints_data and scripts, and the third additionnal objects that needs to be closed
        is a special way.
    """

    new = hints_data.copy()
    new[0] = new[0].format(key)

    return new, scripts.copy(), [5]

def close (key, objs):
    """
        This fuction is called on exit and reset of the level (before gen).
        It is used to softly close / kill objects or do post-level cleaning.
    """

    print(objs[0])