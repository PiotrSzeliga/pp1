decimal = int(input("Enter decimal number: "))
binary = []
while decimal > 0:
    binary.append((decimal%2))
    decimal //= 2
for i in reversed(binary):
    print(i,end="")



 


    

    
