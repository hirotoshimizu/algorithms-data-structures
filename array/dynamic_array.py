from typing import Any


class Array:
    def __init__(self) -> None:
        self.capacity = 2
        self.length = 0
        self.array = [0] * 2

    def pushback(self, n: Any) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def resize(self):
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def popback(self):
        if self.length > 0:
            self.length -= 1

    def get(self, i: int) -> int | None:
        if i < self.length:
            return self.array[i]

    def insert(self, i: int, n: Any) -> None:
        if i < self.length:
            self.array[i] = n
            return

    def print(self) -> None:
        for i in range(len(self.length)):
            print(self.array[i])
        print()
