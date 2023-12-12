import csv
with open("studentslist.txt","r") as file:
    csv_reader = csv.reader(file)
    with open("studentlist2.txt","w") as file2:
        next(csv_reader)
        for line in csv_reader:
            if int(line[2]) < 30:
                    file2.write(f"{line[0]:<8} {line[1]:<9} {line[4]}\n")
            else:
                pass
    