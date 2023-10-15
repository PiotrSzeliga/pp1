import random
roll = random.randint(1,6)
special = [1,6]
print(f"Dice rolled: {roll}")
if roll in special:
    print("Special number: True")
else:
    print("Special number: False")