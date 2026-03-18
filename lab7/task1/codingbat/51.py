def xyz_there(str):
    if str.startswith("xyz"):
        return True
    for i in range(1, len(str)-2):
        if str[i:i+3] == "xyz" and str[i-1] != ".":
            return True
    return False