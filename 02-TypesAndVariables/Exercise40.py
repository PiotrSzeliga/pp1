card = input("Enter credit card number: ")
while len(card) != 16:
    card = input("Enter credit card number: ")
print(f"Card nummer: {card[0:4]} {card[4:8]} {card[8:12]} {card[12:16]}")
    
