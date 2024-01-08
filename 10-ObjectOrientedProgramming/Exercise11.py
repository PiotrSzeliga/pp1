class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
        self.volume = 0
    
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
            if self.channel_no > len(self.channels):
                print(f"TV is turned on, channel {self.channel_no}.not available")
            else:
                print(f"TV is turned on, channel {self.channel_no}.{self.channels[self.channel_no-1]}")
            print(f"Volume: {self.volume}/10")
        else:
            print(f"TV is turned off")

    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no

    def show_channels(self):
        print(f"Channels: {", ".join(self.channels)}")
    
    def volume_up(self):
        if self.volume == 10:
            pass
        else:
            self.volume += 1

    def volume_down(self):
        if self.volume == 0:
             pass
        else:
            self.volume -= 1

TV1 = TV()
TV1.show_status()
TV1.turn_on()
TV1.show_channels()
TV1.show_status()
TV1.set_channel(20)
TV1.show_status()
[TV1.volume_up() for i in range(3)]
TV1.show_status()
TV1.volume_down()
TV1.show_status()
TV1.turn_off()
TV1.show_status()