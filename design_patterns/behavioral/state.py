# Object changes behavior based on internal state.


class State:
    def handle(self):
        pass


class Happy(State):
    def handle(self):
        print("I'm happy!")


class Sad(State):
    def handle(self):
        print("I'm sad.")


class Person:
    def __init__(self, state):
        self.state = state

    def act(self):
        self.state.handle()


if __name__ == "__main__":
    p = Person(Happy())
    p.act()
    p.state = Sad()
    p.act()
