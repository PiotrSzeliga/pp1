celcius = float(input("Enter temperature in Celcius: "))
#asks for user's input and converts it fron string to floating poit number
kelvin = celcius-273.15
#calculates kelvin from celcius
farenheit = celcius*1.8+32
#uses fornula to calculate farenheit from celcius
print("Temperature in:\n","   Celcius: {}\n".format(celcius),"   Kelvin: {}\n".format(kelvin),"   Farenheit: {}".format(farenheit) )