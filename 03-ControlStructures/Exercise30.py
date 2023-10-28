time24 = input("Enter time (24-hour format): ")
if int(time24[:2]) < 13:
    print(f"Time in 12-hour format: {time24} am")
else:
    print(f"Time in 12-hour format: {int(time24[:2])-12}:{time24[3:6]}pm")