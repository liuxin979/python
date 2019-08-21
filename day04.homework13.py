class Fan(object):
    def __init__(self, speed = 1, on = False, radius = 5, color = "blue"):
        self.speed = speed
        self.on = on
        self.radius = radius
        self.color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, new_on):
        self._on = new_on

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

if __name__ == "__main__":
    fan1 = Fan(3, True, 10, "yellow")
    print("speed: ", fan1._speed)
    print("radius: ", fan1._radius)
    print("color: ", fan1._color)
    print("on: ", fan1._on)
    print("#######################")
    fan2 = Fan(2, False, 5, "blue")
    print("speed: ", fan2._speed)
    print("radius: ", fan2._radius)
    print("color: ", fan2._color)
    print("on: ", fan2._on)
