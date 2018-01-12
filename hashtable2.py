class MyHashTable:

    def __init__(self, size):
        self.size = 0
        self.hash_size = size
        self.rehash_count = 1
        self.hash_table = [None] * size

    def _hash_func(self, key):
        return abs(hash(key)) % self.hash_size

    def _search_key(self, key):
        n = self._hash_func(key)
        count = 0
        while count < self.hash_size:
            data = self.hash_table[n]
            if data is None:
                break
            if data and data[0] == key:
                return n
            n = (n + 1) % self.hash_size
            count += 1
        return -1

    def search(self, key):
        n = self._search_key(key)
        if n >= 0: return self.hash_table[n][1]
        return None

    def insert(self, key, value):
        n = self._search_key(key)
        if n < 0:
            n = self._hash_func(key)
            count = 0
            while count < self.hash_size:
                if not self.hash_table[n]:
                    self.size += 1
                    break
                n = (n + 1) % self.hash_size
                count += 1
            else:
                # self.rehash()
                raise IndexError
        self.hash_table[n] = (key, value)
        return value

    # def rehash(self):
    #     self.rehash_count += 1
    #     kv = []
    #     for item in self.hash_table:
    #         if item is not None:
    #             kv.append(item)
    #     self.hash_table.clear()
    #     self.hash_table = [None] * self.hash_size * self.rehash_count
    #     for k,v in kv:
    #         self.insert(k,v)

    def delete(self, key):
        n = self._search_key(key)
        value = None
        if n >= 0:
            value = self.hash_table[n][1]
            self.hash_table[n] = ()
            self.size -= 1
        return value

    def traverse(self):
        for data in self.hash_table:
            if data: yield data

    def __len__(self):
        return self.size

if __name__ == "__main__":
    hash_size = 5
    hash_table = MyHashTable(hash_size)
    hash_table.insert("100", "aaaa")
    hash_table.insert("200", "bbbb")
    hash_table.insert("300", "cccc")
    hash_table.insert("400", "dddd")
    hash_table.insert("500", "dddd")
    hash_table.insert("500", "dddd")
    print(hash_table.search("100"))
    print(hash_table.search("200"))
    print(hash_table.search("300"))
    print(hash_table.search("400"))
    print(hash_table.search("500"))
