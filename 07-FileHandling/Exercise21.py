file = open("numbers2.txt","w")
for i in range(1,51):
    file.write(f"{i}\n")
file.close()
