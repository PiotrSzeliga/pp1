def avg_speed(distance,hours,minutes):
    time = int(hours) + int(minutes)/60
    average = int(distance)/time
    return average

distance = input("Enter distance in km: ") 
hours = input("Enter number of travel hours: ") 
minutes = input("Enter number of travel minutes: ") 
print(avg_speed(distance,hours,minutes))