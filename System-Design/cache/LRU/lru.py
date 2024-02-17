from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # most recently used items are at end
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(key)
        