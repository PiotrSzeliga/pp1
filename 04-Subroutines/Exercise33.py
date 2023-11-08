def f(n):
    m = ""
    for i in range(n):
        m += "*"
        if i < n-1:
            m += "/"
    return m



if __name__ == "__main__":
    print(f(10))