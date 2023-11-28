filename = input("Enter file name: ")
counter = 0
with open(f"{filename}","r") as file:
    for line in file:
        counter += 1
print(f"File name: {filename}\n"+f"Number of lines: {counter}")