# Make incompatible interfaces work together.


class OldSystem:
    def old_method(self):
        return "Old system output"


class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return self.old_system.old_method()


if __name__ == "__main__":
    adapter = Adapter(OldSystem())
    print(adapter.new_method())
