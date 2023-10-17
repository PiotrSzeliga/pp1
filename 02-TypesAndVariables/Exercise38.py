number = input("Enter phone number: ")
while len(number) != 9:
    number = input("Enter phone number correctly: ")
print(f"Phone number: "+number[:3]+"-"+number[4:7]+"-"+number[-3:])




