def f(c):
    sum = 0
    for i in c:
        try:
            sum += int(i)
        except ValueError:
            sum += 10
    return sum

if __name__ == "__main__":
    print(f("2k9"))
    print(f("234AJ7"))
    