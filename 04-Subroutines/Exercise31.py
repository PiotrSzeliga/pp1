def f(x,y):
    z = 0
    for i in range(x,y+1):
        if i%2 == 0 and i < 0:
            z += 1
    return z



if __name__ == "__main__":
    print(f(-1,11))