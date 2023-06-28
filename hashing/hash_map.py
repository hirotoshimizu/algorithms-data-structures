from typing import Any, Optional


class Pair:
    def __init__(self, key: Any, val: Any) -> None:
        self.key = key
        self.val = val


class HashMap:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key: str) -> int:
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key: str) -> Optional[str]:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key: str, val: str) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            index = index % self.capacity

    def rehash(self) -> None:
        self.capacity = 2 * self.capacity
        new_map = []
        for _ in range(self.capacity):
            new_map.append(None)

        old_map = self.map
        self.map = new_map
        self.size = 0
        for pair in old_map:
            if pair:
                self.put(pair.key, pair.val)


if __name__ == "__main__":
    hash_map = HashMap()
    hash_map.put("Taro", "Tokyo")
    hash_map.put("Hanako", "Osaka")
    name1 = hash_map.hash("Taro")
    name2 = hash_map.hash("Hanako")
    print(hash_map.map[name1].key)
    print(hash_map.map[name1].val)
    print(hash_map.map[name2].key)
    print(hash_map.map[name2].val)
