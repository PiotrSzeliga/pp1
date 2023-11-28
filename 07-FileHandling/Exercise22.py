import random
file = open("numbers3.txt","w")
for i in range(50):
    file.write(f"{random.randrange(100,1000)}\n")
file.close()