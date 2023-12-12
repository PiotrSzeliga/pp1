import re
with open("sample.txt","r") as file:
    x = file.read()
    z = r"\b[a-zA-Z]{8,}\b"
    y = re.findall(z,x)
    print(len(y))