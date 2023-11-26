array1 = [1,2,4]
array2 = [1,4,5,6,7]

def subset(array1, array2):
    for i in array1:
        if i in array2:
            continue
        else:
            return "Is not a subset"
    return "Is a subset"

print(subset(array1,array2))