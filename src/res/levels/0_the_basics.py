def gen (key, hints_data, scripts):
    new_s = scripts.copy()
    
    for i in range(len(new_s)):
        new_s[i] = new_s[i].format(key)
    
    new_s[:-1] = ["\n".join(new_s[:-1])]

    return hints_data.copy(), new_s, []

def close (key, objs):
    pass