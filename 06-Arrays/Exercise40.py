import random
array = [random.randrange(1,999) for x in range(8)]
def kom(array):
    print("-"*(len(array)*5+1))
    for i in array:
        print(f"|{i:>4}",end="")
    print("|\n"+"-"*(len(array)*5+1))
    

kom(array)

