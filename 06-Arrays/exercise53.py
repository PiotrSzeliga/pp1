def identity_matrix(n):
    array = [[0 for k in range(n)] for i in range(n)]
    for i in range(0,len(array)):
        array[i][i] = 1
    return array
print(identity_matrix(5))