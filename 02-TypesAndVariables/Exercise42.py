binary = input("Enter 4 digit binary number: ")
decimal = 0
digit = 0
for i in range(4):
    if binary[digit] == "1":
        decimal += 2**(3-i)
        digit += 1
    else:
        digit += 1
print(decimal)