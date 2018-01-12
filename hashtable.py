# coding: utf-8

from __future__ import print_function

class MyHashTable:

    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def hash(self, k):
        return len(k) % self.size

    def _search_hash(self, k):
        h = self.hash(k)
        if self.table[h] == k:
            return h
        else:
            count = 0
            while count < self.size:
                if h != self.size - 1:
                    h += 1
                else:
                    h = 0
                if self.table[h] == k:
                    return h
                else:
                    count += 1
            if count >= self.size:
                return None

    def insert(self, k):
        h = self.hash(k)
        if self.table[h] == None or self.table[h] == "deleted":
            self.table[h] = k
        else:
            count = 0
            while count < self.size:
                if h != self.size - 1:
                    h += 1
                else:
                    h = 0
                if self.table[h] == None or self.table[h] == "deleted":
                    self.table[h] = k
                    break
                else:
                    count += 1
            if count >= self.size:
                print("no empty column")

    def delete(self, k):
        h = self._search_hash(k)
        if h != None:
            self.table[h] = "deleted"
        else:
            print("no item")

    def search(self, k):
        h = self._search_hash(k)
        if h != None:
            return self.table[h]
        else:
            return("no item")

if __name__ == "__main__":
    hash_table = MyHashTable()
    hash_table.insert("100")
    hash_table.insert("200")
    hash_table.insert("300")
    hash_table.insert("400")
    hash_table.insert("500")
    hash_table.insert("600")
    print(hash_table.search("100"))
    print(hash_table.search("200"))
