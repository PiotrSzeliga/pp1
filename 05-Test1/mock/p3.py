def f(name):
    output = name[0]
    for i in range(1,len(name)):
        if name[i] == " ":
            output += name[i+1]
    return output

if __name__ == "__main__":
    print(f("For Your Information"))