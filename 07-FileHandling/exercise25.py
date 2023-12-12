import re
with open("message.txt","r") as file:
    message = file.read()
    temperatures = re.findall(r"\d{2}",message)
    x = " ".join(temperatures)
    print(x)

