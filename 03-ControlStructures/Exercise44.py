list = []

while True:
    list.append(int(input("Enter a number: ")))
    if list[-1] == 0:
        break
    else:
        continue
print(f"RESULT: Quantity={len(list)-1}, Sum={sum(list)}, Mean={sum(list)/(len(list)-1)}")
        

