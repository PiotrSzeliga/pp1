buying_rate = float(input("Enter buying rate: "))
selling_rate = float(input("Enter selling rate: "))
spread = abs(buying_rate-selling_rate)
print(f" Bank buys EUR: {buying_rate:.4f}\n",f"Bank sells EUR: {selling_rate:.4f}\n",f"Spread: {spread:.4f}")