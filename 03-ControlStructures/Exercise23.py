year = int(input("Enter the dog's age in human years: "))
def dog():
    dogyear = 0
    for y in range(year):
        if y < 2:
            dogyear += 10.5
        else:
            dogyear += 4
    return dogyear
print(f"The dog's age in dog’s years is {dog()} years.")
    

