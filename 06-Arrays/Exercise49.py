array = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

multiplicator = 1
number = 1
for row in array:
    for element in row:
        print(number*multiplicator, end=" ")
        multiplicator += 1
    print("\n")
    number += 1
    multiplicator = 1

        