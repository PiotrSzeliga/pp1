array = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return lambda pts: pts>=limit

print(list(filter(min_pts(70),array)))
print(list(filter(min_pts(40),array)))
print(list(filter(min_pts(30),array)))