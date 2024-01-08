class Phone():
    def __init__(self,name,battery):
        self.powered = False
        self.battery = battery
        self.name = name
    
    def show_status(self):
        print(f"Phone is powered: {self.powered}\nBattery: {self.battery}%")
    
    def turn_on(self):
        if self.battery > 0:
            if self.powered == False:
                print("Turning on the phone")
                self.powered = True
            else:
                print("Phone is already turned on")
        else:
            self.powered = False
            print("No power")

    def turn_off(self):
        if self.battery > 0:
            if self.powered == True:
                print("Turning off the phone")
                self.powered = False
            else:
                print("Phone is already turned ff")
        else:
            self.powered = False
            print("No power")

    def __str__(self):
        if self.powered == True:
            return f"{self.name} is turned on and has {self.battery}% battery"
        else:
            return f"{self.name} is turned off and has {self.battery}% battery"