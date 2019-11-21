def gen (key, hints_data, scripts):
    new_s = scripts.copy()
    
    new_s[1] = new_s[1].format(int(key, 16))
    
    new_s[:-1] = ["\n".join(new_s[:-1])]

    return hints_data.copy(), new_s, []

def close (key, objs):
    pass