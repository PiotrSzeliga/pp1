import random
class Thermometer():
    def __init__(self):
        self.working = False
        self.temperature = None

    def turn_on(self):
        if self.working == False:
            self.working = True
        else:
            pass
    def turn_off(self):
        if self.working == True:
            self.working = False
        else:
            pass
    
    def measure_temperature(self):
        if self.working == True:
            self.temperature = round(random.uniform(34.0,42.0),1)

    def display_temperature(self):
        print(f"Temperature: {self.temperature}C",end=" ")
        if self.temperature > 37:
            print("(fever)")
        if self.temperature > 41:
            print("CRITICAL TEMPERATURE!!")

thermomether = Thermometer()
thermomether.turn_on()
thermomether.measure_temperature()
thermomether.display_temperature()
thermomether.turn_off

