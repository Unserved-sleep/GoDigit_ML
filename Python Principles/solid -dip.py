from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on")

    def turn_off(self):
        print("LightBulb: turned off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on")

    def turn_off(self):
        print("Fan: turned off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
        self.is_on = False

    def press(self):
        if self.is_on:
            self.device.turn_off()
            self.is_on = False
        else:
            self.device.turn_on()
            self.is_on = True


bulb = LightBulb()
fan = Fan()

switch = Switch(bulb)
switch.press()
switch.press()

switch = Switch(fan)
switch.press()
switch.press()  