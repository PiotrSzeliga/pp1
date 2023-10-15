height = float(input("Enter your height in cm: "))/100
weight = float(input("Enter your weight in kg: "))
bmi = weight/height**2
print(F"Your BMI index: {bmi}")
if 18.5 <= bmi <= 24.9:
    print("Correct weight: True")
else:
    print("Correct weight: False")