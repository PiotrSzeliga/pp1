array = [1,2,3,4,5,6,7,8,9,10]
array2 = []
for i in array:
    if i%2 == 0:
        continue
    else:
        array2.append(i)
        array.remove(i)
array = array+array2
print(array)