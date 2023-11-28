with open("movies.txt") as f:
    for line in f:
        print(line, end="")
    f.close()
