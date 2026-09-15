# Encapsulate actions as objects.


class Light:
    def on(self):
        print("Light ON")

    def off(self):
        print("Light OFF")


class Command:
    def execute(self):
        pass


class LightOn(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOff(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


if __name__ == "__main__":
    light = Light()
    LightOn(light).execute()
    LightOff(light).execute()
