def f(e):
    x = []
    for i in e:
        x.append(i)
    sum = 0
    for i in range(0,len(x)):
        try:
            sum += int(x[i])
        except ValueError:
            if x[i] == "+":
                pass
            else:
                sum -= 2*int(x[i+1])
    return sum


if __name__ == "__main__":
    print(f("2+3"))
        


