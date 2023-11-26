f = open("numbers.txt","tr")
g = f.readlines()
sum = 0
for i in g:
    sum += int(i)
f.close()
print(sum)
print(g)

