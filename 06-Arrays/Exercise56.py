array = [[5,0,3,7,5],
[9,0,9,1,2]]

def flatominator(n):
    flat = []
    for x in array:
        for y in x:
            flat.append(y)
    return flat

print(flatominator(array))
