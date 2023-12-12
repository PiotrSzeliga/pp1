def f(t):
    import re
    pattern = r"\d+"
    with open(f"{t}","r") as text:
        x = text.read()
        y = re.findall(pattern,x)
    suma = 0
    for i in y:
        suma += int(i)
    return suma


if __name__ == "__main__":
    print(f("t.txt"))