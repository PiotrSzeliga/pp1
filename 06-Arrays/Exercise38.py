array = [1,2,3,4,5,6,7,8,9,10]
n = 0
counter = 0
while n != "":
    n = int(input("Enter a number: "))
    for i in array:
        if i > (n):
            counter += 1
        else:
            continue
    print(counter)
    counter = 0