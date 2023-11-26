def bubblesort(array):
    l = len(array) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0,l):
            if array[i]>array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
    return array

array = [1,2,6,4,5,9,8,7]

print(bubblesort(array))