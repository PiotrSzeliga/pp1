def is_binary(n):
    for i in str(n):
        if i == "1" or i == "0":
            continue
        else:
            return False
    return True


