avg_speed = lambda distance,hours,minutes: int(distance)/(int(hours)+int(minutes)/60)
result = avg_speed(70,1,23)
print(result)