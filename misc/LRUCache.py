from collections import OrderedDict

class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key, last=False)
            return self[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self:
            if len(self) == self._capacity:
                self.popitem(last=True)
        self[key] = value
        self.move_to_end(key, last=False)
