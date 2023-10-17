import math
circumference = float(input("Enter tree circumference: "))
diameter = circumference/math.pi
print("Tree can be cut down: ",diameter>50)