with open("movies.txt","r") as file:
    with open("copy.txt","w") as file2:
        file2.write(file.read())