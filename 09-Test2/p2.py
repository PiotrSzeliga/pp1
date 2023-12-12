def f(x):
    number = 0
    for i in x:
        if i == "+":
            number += 1
        else:
            number -= 1 
    return number

if __name__ == "__main__":
    print(f("+-+++---"))
    print(f("+-+++++-"))