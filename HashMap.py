class HashMap:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def hash(self, key):
        h = 0
        if type(key) is str:
            for i in key:
                h = (h + ord(i)) % 10
            return h
        return key % 10

    def __setitem__(self, key, value):
        h = self.hash(key)
        for i in range(h, self.MAX):
            if self.arr[i] == None:
                self.arr[i] = (key, value)
                return
            elif self.arr[i][0] == key:
                self.arr[i] = (key, value)
                return
        for i in range(0, h):
            if self.arr[i] == None:
                self.arr[i] = (key, value)
                return
            elif self.arr[i][0] == key:
                self.arr[i] = (key, value)
                return
        print('the Map is full')
            

    def __getitem__(self, key):
        h = self.hash(key)
        for i in range(h, self.MAX):
            if self.arr[h][0] == key:
                return self.arr[h][1]
        for i in range(0, h):
            if self.arr[h][0] == key:
                return self.arr[1]
        print('Item is not in the Map')


    def __delitem__(self, key):
        h = self.hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = []
                return


if __name__ == '__main__':
    t = HashMap()
    t['feb 1'] = 'saturday'
    t['feb 2'] = 'sundaty'
    t['feb 3'] = 'monday'
    t['feb 4'] = 'tuesday'
    t['feb 5'] = 'wendsday'
    t['feb 6'] = 'thursday'
    t['feb 7'] = 'friday'
    t['feb 8'] = 'saturday'
    t['feb 9'] = 'sunday'
    print(t.arr)
    print(t['feb 9'])
