array = [[1,2,3],[0,0,0],[0,0,0],[0,0,0],[4,5,6]]
print(array)
array[0],array[len(array)-1] = array[len(array)-1], array[0]
print(array)