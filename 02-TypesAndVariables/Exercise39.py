price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
print("Price with discount: ",round(price-price*discount/100,2),"\nReduction: ",round(price*discount/100,2))