array1 = [3,2,1]    
array2 = [5,3,1]


def compare(array1,array2):
        if len(array1) == len(array2):
                for i in range(len(array1)):
                    if array1[i-1] == array2[i-1]:
                           continue
                    else: 
                        return "Not the same"
                return "The same"
        
        else:
              return "Not the same"

print(compare(array1,array2))