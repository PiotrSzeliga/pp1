with open("MeatAndFish.txt","r") as file1, open("GrainsAndBread.txt","r") as file2, open("allproducts.txt","w") as file3:
    file3.write(file1.read()+file2.read())
    