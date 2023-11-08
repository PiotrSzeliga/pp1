def f(detector):
    g = 0
    for i in detector:
        if g == 3:
            return True
        elif i == "+":
            g += 1
        elif i == "-":
            g -= 1
    return False

            



if __name__ == "__main__":
    print(f("+-++-++-+---"))