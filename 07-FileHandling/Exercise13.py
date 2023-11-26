array = ["Bladerunner2049","Barbie","Nice Guys","Drive","La La Land"]
file = open("movies.txt","w")
for i in array:
    file.write(i+"\n")
file.close()