class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        h = self._hash(key)
        for idx, element in enumerate(self.map[h]):
            if element[0] == key:
                self.map[h][idx] = (key, value)
                return
        self.map[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for element in self.map[h]:
            if element[0] == key:
                return element[1]
        return None

    def remove(self, key):
        h = self._hash(key)
        self.map[h] = [pair for pair in self.map[h] if pair[0] != key]


if __name__ == "__main__":
    hm = HashMap()
    hm.put("name", "Rashid")
    hm.put("age", 35)
    print(hm.get("name"))
    hm.remove("name")
    print(hm.get("name"))
