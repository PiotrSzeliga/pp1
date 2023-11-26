array = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]

def lastRow(array):
    sum = 0
    for i in array[len(array)-1]:
        sum += i
    return sum

print(lastRow(array))