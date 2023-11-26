list = [1,2,3,4,5]
def change(array):
    print(array)
    array[0] += -1
    print(array)
    array[-1] += 4
    print(array)  
    array[round(len(array)/2)] *= 2
    print(array)  

print(change(list))