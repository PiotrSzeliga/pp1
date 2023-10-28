number = 1
while number < 50:
    if number == 49:
        print(number)
        break
    elif number == 1 or number == 2:
        print(number,end="  ")
        number += 7
    elif number >= 43:
        print(number,"\n")
        number -= 41
    else:
        print(number, end=" ")
        number += 7
    
    