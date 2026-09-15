# Swap algorithms at runtime.


class Add:
    def execute(self, a, b):
        return a + b


class Multiply:
    def execute(self, a, b):
        return a * b


class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def compute(self, a, b):
        return self.strategy.execute(a, b)


if __name__ == "__main__":
    calc = Calculator(Add())
    print(calc.compute(3, 5))  # 8

    calc.strategy = Multiply()
    print(calc.compute(3, 5))  # 15
