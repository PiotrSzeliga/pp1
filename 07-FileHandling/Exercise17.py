file = open("sample.txt","r")
enter = ""
while enter == "":
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    enter = input("")
file.close()