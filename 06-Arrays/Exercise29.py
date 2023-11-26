array1 = [4,36,12,28,9,44,5] 
array2 = [5,1,36]
for i in range(len(array1)):
    if array1[i-1] in array2:
        continue
    else:
        print(array1[i-1])