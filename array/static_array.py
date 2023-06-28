from typing import Any


class Array:
    def __init__(self) -> None:
        self.capacity = 2
        self.length = 0
        self.array = [0] * 2

    def insert_end(self, n: Any) -> None:
        if self.length < self.capacity:
            self.array[self.length] = n

    def remove_end(self):
        if self.length > 0:
            self.array[self.length - 1] = 0

    def insert_middle(self, i: int, n: Any) -> None:
        for index in range(self.length - 1, i - 1, -1):
            self.array[index + 1] = self.array[index]
        self.array[i] = n

    def remove_middle(self, i: int) -> None:
        for index in range(i + 1, self.length):
            self.array[index - 1] = self.array[index]

    def print_arr(self) -> None:
        for i in range(self.capacity):
            print(self.array[i])
