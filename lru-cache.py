class Node:
    def __init__(self, key, val):
        self.key, self.value = key, val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key to node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache.get(key)
        # remove node from double linked lis
        self.removeFromDll(node)
        # add node to head of dll to show most recently used
        self.addHeadToDll(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self.removeFromDll(node)
            self.addHeadToDll(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.prev.key]
                self.removeFromDll(self.tail.prev)
            node = Node(key, value)
            self.cache[key] = node
            self.addHeadToDll(node)

    def removeFromDll(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addHeadToDll(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))  # return 1
    lru.put(3, 3)  # evicts key 2
    print(lru.get(2))  # return -1 (not found)
    lru.put(4, 4)  # evicts key 1
    print(lru.get(1))  # return -1 (not found)
    print(lru.get(3))  # return 3
    print(lru.get(4))  # return 4


