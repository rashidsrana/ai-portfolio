# One object notifies many listeners.


class Observer:
    def update(self, message):
        print("Received:", message)


class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, obs):
        self.observers.append(obs)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)


if __name__ == "__main__":
    s = Subject()
    s.subscribe(Observer())
    s.subscribe(Observer())
    s.notify("Event happened!")
