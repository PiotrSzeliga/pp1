import re
with open("grades.txt","r") as file:
    x = file.read()
    pattern = r"\d.\d"
    y = re.findall(pattern,x)
    sum = 0
    for i in y:
        sum += float(i)
    mean = sum/len(y)
    print(mean)