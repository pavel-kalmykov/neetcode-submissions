from dataclasses import dataclass


@dataclass
class HashPair:
    key: int
    value: int


class HashTable:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table: list[None | HashPair] = [None] * capacity
        self.size = 0

    def hash(self, key: int) -> int:
        return hash(key) % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True:
            if (curr := self.table[index]) is None:
                self.table[index] = HashPair(key, value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                break
            elif curr.key == key:
                self.table[index] = HashPair(key, value)
                break
            index = (index + 1) % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)
        while (curr := self.table[index]) is not None:
            if curr.key == key:
                return curr.value
            index = (index + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while (curr := self.table[index]) is not None:
            if curr.key == key:
                self.table[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table: list[None | HashPair] = [None] * self.capacity
        old_table = self.table
        self.table = new_table
        self.size = 0
        for curr in old_table:
            if curr is not None:
                self.insert(curr.key, curr.value)
