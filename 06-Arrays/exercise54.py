array1 = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 0]]
def transpose_matrix(m):
    n = [[m[i][b] for i in range(0,len(m))] for b in range(0,len(m[0]))]
    print(n)
    
transpose_matrix(array1)