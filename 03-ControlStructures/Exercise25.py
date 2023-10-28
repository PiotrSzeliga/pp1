number = int(input("Number of products purchased: "))
price = int(input("Product price: "))
pay = 0
for x in range(number):
    if x < 2:
        pay += price
    else:
        pay += 0.75*price
print(f"Amount to pay: {pay}")

