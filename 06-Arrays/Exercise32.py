def occurs(number, array):
    if number in array:
        return True
    else:
        return False
n = " "
list = [15, 38, 7, 23, 14]

while n != "":
    n = int(input("Enter a number: "))
    if occurs(n, list) == False:
        print(f"{n} not in array")
    else:
        print(f"{n} in array")

