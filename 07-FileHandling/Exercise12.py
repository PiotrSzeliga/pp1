name = "Piotr Szeliga"
university = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt","w")
file.write(name+"\n"+university+"\n"+field)
file.close()