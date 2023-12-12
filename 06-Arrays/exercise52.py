array = [[1,0,2],[3,0,4],[5,0,6],[7,0,8],[9,0,10]]
def f(array):
    print(array)
    for i in range(0,len(array)):
        array[i][0], array[i][-1] = array[i][-1], array[i][0] 
    print(array)

f(array)