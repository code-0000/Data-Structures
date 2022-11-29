class HashMap:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def hash(self, key):
        h = 0
        if type(key) is str:
            for i in key:
                h = (h + ord(i)) % 10
            return h
        return key % 10

    def __setitem__(self, key, value):
        h = self.hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, value)
                return
        self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.hash(key)
        for element in (self.arr[h]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = []
                return


if __name__ == '__main__':
    t = HashMap()
        