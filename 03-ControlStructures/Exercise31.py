x = -5
y = -40
if x == 0 and y == 0:
    print(f"Point P({x},{y}) is in the middle of coordinate system")
elif x == 0:
    print(f"Point P({x},{y}) is on x axis")
elif y == 0:
    print(f"Point P({x},{y}) is on y axis")
elif x > 0:
    if y > 0:
        print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
    else:
        print((f"Point P({x},{y}) is in the fourth quadrant of the coordinate system"))
else:
    if y > 0:
        print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
    else:
        print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")

