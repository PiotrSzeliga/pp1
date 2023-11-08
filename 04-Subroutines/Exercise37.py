def f(n):
    m = [0,1]
    for i in range(3,n+1):
        m.append(m[-2]+m[-1])
    return m[-1]


if __name__ == "__main__":
    print(f(7))