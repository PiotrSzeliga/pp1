correct = 1234
incorrect = 1
while True:
    pin = input("Enter 4-digit PIN code: ")
    if incorrect == 3:
        print("Sorry, your payment card has been blocked.")
        break
    elif pin != correct:
        incorrect += 1
        print("Incorrect...")
    else:
        print("PIN code correct")
        break
    
        
        
    
