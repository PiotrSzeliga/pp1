f = open("sample.txt","r")
for line in f:
    print(f.readline())
f.close()