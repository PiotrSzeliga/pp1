washing_product = "jacket" #possible underwear, shoes, jacket
rinse = False
spin = False
time = 0
if washing_product == "shoes":
    time += 20
elif washing_product == "underwear":
    time += 70
elif washing_product == "jacket":
    time += 40
if rinse == True:
    time += 15
if spin == True:
    time += 9
print(f"Total washing time: {time} minutes")
