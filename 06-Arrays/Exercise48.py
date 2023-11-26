def create_2d_arr(x,y):
    array = []
    for v in range(y):
        array.append([0 for h in range(x)])
    return array


print(create_2d_arr(3,5))