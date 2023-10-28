fibonacci = [0,1]
for i in range(18):
    fibonacci.append(fibonacci[i]+fibonacci[i+1])
for i in range(len(fibonacci)):
    print(fibonacci[i], end=" ")


    