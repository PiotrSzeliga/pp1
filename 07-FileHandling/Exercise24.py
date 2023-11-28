import csv
with open("studentslist.txt","r") as file:
    for line in file:
        print(csv.reader(file,delimiter=","))
    