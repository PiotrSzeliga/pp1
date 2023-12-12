array = [[-38, 19], [5,40],[-7,11],[29,16]]
def f(array):
    maximum = 0
    minimum = 0
    maximum_location = []
    minimum_location = []
    for i in range(0,len(array)):
        for b in range(0,len(array[i])):
            if array[i][b] > maximum:
                maximum = array[i][b]
                maximum_location = [i,b]
            elif array[i][b] < minimum:
                minimum = array[i][b]
                minimum_location = [i,b]
            else:
                pass
    x = f"maximum={maximum} array[{maximum_location[0]}][{maximum_location[1]}]\nminimum={minimum} array[{minimum_location[0]}][{minimum_location[1]}]"
    return x

print(f([[-38, 19], [5,40],[-7,11],[29,16]]))
    