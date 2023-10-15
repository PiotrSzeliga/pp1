import math
height_cm = 191
feet = math.floor(height_cm*0.032808399)
inch = round((height_cm*0.032808399-feet)*12)
print(f"I am {height_cm}cm tall, i.e. {feet} feet and {inch} inches")