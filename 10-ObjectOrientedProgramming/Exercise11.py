class TV():
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if self.is_on:
            print(f"TV is already turned on")
        else:
            print(f"Turning on the TV")
            self.is_on = True
    def turn_off(self):
        if not self.is_on:
            print(f"TV is already turned off")
        else:
            print(f"Turning off the TV")
            self.is_on = False

    def show_status(self):
        if self.is_on:
            print(f"TV is turned on")
        else:
            print(f"TV is turned off")

TV1 = TV()
TV1.show_status()
TV1.turn_on()
TV1.show_status()