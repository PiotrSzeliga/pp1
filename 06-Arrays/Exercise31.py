array = [2, 3, 2, 5, 8, 1, 9, 8]
for i in range(len(array)):
    if array.count(array[i]) == 1:
        print(array[i])
    else:
        continue

