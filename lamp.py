class Lamp:
    def __init__(self, light=False):
        self.light = light

    def turn_on(self):
        self.light = True

    def turn_off(self):
        self.light = False

    def is_lightening(self):
        return self.light



