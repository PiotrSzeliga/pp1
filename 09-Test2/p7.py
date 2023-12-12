def f(d,v):
    counter = 0
    for key,value in d.items():
        if value is not v:
            counter += 1
        else:
            pass
    return counter


if __name__ == "__main__":
    print(f({"a":True,"b":False,"c":True,"d":True,"e":True},True))
    print(f({"a":True,"b":False,"c":True,"d":True,"e":True},False))
            