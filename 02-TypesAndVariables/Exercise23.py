import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
circumference = a + b + c
half_circumference = (a + b + c ) / 2
area = math.sqrt(half_circumference*(half_circumference-a)*(half_circumference-b)*(half_circumference-c))
print(f"Triangle area: {area}",f"Triangle circumference: {circumference}")

