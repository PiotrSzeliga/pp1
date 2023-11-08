def f(password):
    g = set()
    for i in password:
        g.add(i)
    print(g)
    if len(g) >= 6:
        return True
    else:
        return False
if __name__ == "__main__":
    print(f("book123"))