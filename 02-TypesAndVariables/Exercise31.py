import random
roll = random.randint(1,6)
guess = int(input("Guess the dice roll: "))
if roll == guess:
    print("True")
else:
    print("False")