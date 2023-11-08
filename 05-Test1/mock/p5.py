def f(binary_number):
    for i in binary_number:
        if i != "0" and i != "1":
            return False
        else:
            continue
    return True
        

if __name__ == "__main__":
    print(f("1311a10100"))