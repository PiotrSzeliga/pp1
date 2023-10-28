amount = int(input("Enter the amount in PLN: "))
five = amount//5
two = (amount-five*5)//2
one = (amount-five*5)%2
print(f"The amount of PLN {amount} in coins:\n5zł - {five}\n2zł - {two}\n1zł - {one}")