number = (input("Enter number: "))
if int(number) >= 0:
    print(f"|{number}|= {number}")
else:
    print(f"|{number}|= {number[1:]}")
