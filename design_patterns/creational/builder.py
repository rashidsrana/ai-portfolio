# Build complex objects step‑by‑step.


class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def add_ram(self, ram):
        self.computer.ram = ram
        return self

    def build(self):
        return self.computer


if __name__ == "__main__":
    pc = ComputerBuilder().add_cpu("i9").add_ram("32GB").build()
    print(pc.cpu, pc.ram)
