# solution 1 : doubly linked list + dict
class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key, self.val = key, val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.add(self.dict[key])
            return self.dict[key].val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, value)
        self.add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            self.dict.pop(self.head.next.key)
            self.remove(self.head.next)
    
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
        
    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node

# solution 2: OrderedDict
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

c = LRUCache(1)
c.put(2, 1)
print(c.get(2))
c.put(3,2)
print(c.get(2))
print(c.get(3))
