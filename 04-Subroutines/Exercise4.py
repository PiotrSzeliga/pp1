#4 d
#5 d

def computepay():
    hours = int(input("Enter hours: "))
    rate = int(input("Enter rate: "))
    print(f"Pay: {hours*rate}")

def computegrade():
    score = int(input("Enter score: "))
    if score >= 0.9:
        print("A")
    elif 0.9 > score >= 0.8:
        print("B")
    elif 0.8 > score >= 0.7:
        print("C")
    elif 0.7 > score >= 0.6:
        print("D")
    else:
        print("F")