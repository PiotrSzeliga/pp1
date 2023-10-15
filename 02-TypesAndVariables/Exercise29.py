import random
total = 0
for i in range(3):
   roll = random.randint(1,6)
   total += roll
   print(roll)
print(f"Sum of dice rolled: {total}")


