def f(x,y):
    sum = 0
    for i in range(x,y+1):
        if i%2 == 0 and i%3 == 0 and i%4 != 0:
            sum += i
        else:
            continue
    return sum

if __name__ == "__main__":
    print(f(10,30))