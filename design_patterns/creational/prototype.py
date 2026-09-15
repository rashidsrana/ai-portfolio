# Clone objects efficiently.

import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    p1 = Prototype([1, 2, 3])
    p2 = p1.clone()
    print(p1.value, p2.value)
