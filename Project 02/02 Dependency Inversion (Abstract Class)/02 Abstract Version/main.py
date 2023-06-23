from abc import ABC, abstractclassmethod

class Switchable(ABC):

    @abstractclassmethod
    def turn_on(self):
        """Turn on method"""

    @abstractclassmethod
    def turn_off(self):
        """Turn off method"""


class LightBulb(Switchable):

    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turnd off...")


class Television(Switchable):

    def turn_on(self):
        print("Television: turned on...")

    def turn_off(self):
        print("Television: turnd off...")


class ElectricPowerSwich:

    def __init__(self, client: Switchable):
        self.client = client
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


if __name__ == "__main__":

    light = LightBulb()
    swich = ElectricPowerSwich(light)
    swich.press()
    swich.press()

    TV = Television()
    swich = ElectricPowerSwich(TV)
    swich.press()
    swich.press()


