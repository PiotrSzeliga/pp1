def f(arr2D):
    counter = 0
    for i in arr2D:
        if i[0]**2 == i[1]:
            counter += 1
        else:
            pass

    return counter

if __name__ == "__main__":
    print(f([[4,16],[3,9],[-3,9]]))
    print(f([[4,15],[3,9],[-3,-9]]))