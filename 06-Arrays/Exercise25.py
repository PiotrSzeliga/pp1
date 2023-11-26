array = [15, 8, 31, 47, 2, 19]
counter = len(array)
sum = 0
while counter != 0:
    sum += array[counter-1]
    counter -= 1

print(sum/len(array))