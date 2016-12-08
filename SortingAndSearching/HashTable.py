class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.data = [None] * size

    def put(self, key, data):
        hash_value = self.__hash_func(key)
        if not self.keys[hash_value]:
            self.keys[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.keys[hash_value] == key:  # replace
                self.data[hash_value] = data

            else:  # collision!
                new_hash_value = self.__rehash(hash_value, 1)
                print(new_hash_value)
                found = False
                stop = False
                while self.keys[new_hash_value] != key and self.keys[new_hash_value]:
                    #if new_hash_value == hash_value:
                     #   raise KeyError
                    new_hash_value = self.__rehash(new_hash_value, 1)
                if self.keys[new_hash_value] == key:
                    self.data[new_hash_value] = data
                else:
                    self.keys[new_hash_value] = key
                    self.data[new_hash_value] = data

    def get(self, key):
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.data[i]
        raise KeyError
    def __repr__(self):
        return str(list(zip(self.keys, self.data)))

    def __hash_func(self, key):  # determine which slot key should go into
        return key % self.size
    def __rehash(self, curr_value, increment):
        return (curr_value + increment) % self.size

    def __getitem__(self, key):
        return self.get(key)
    def __setitem__(self, key, value):
        self.put(key, value)
h = HashTable(11)
h.put(75, '9th spot')
h.put(56, '1st spot')
h.put(57, '2nd spot')
h.put(67, '3rd spot')
h.put(67, '3rd spot revised')
h[95] = 'Yay'
print(h[57])
'''
print(h.get(67))
print(h.get(56))
print(h.get(80))
'''
print(h)
