def f(arr):
    counter = 0
    for i in arr:
        if arr.count(i) > 1:
            pass
        else:
            counter += 1

    return counter


if __name__ == "__main__":
    print(f([11,22,33,11]))
    print(f([11,22,11,11,22,35,27,11,22,14]))