dictionary = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

print(" ".join(x[0] for x in filter(lambda x: x[1]>0,dictionary.items())))

