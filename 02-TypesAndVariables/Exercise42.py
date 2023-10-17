binary = input("Enter binary number: ")
decimal = 0
b_list = list(binary)
counter = len(b_list) - 1
counterer = 0
for d in b_list:
    if list[counter] == 1:
        decimal += 2**(counter)
        counter -= 1
        counterer += 1

print(decimal)