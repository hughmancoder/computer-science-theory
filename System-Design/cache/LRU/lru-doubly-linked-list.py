class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
"""
Raw implementation of LRU cache with doubly linked list, without OrderedDict
Refer to my other implementation for the abstrcted version using OrderedDict
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # maintain a doubly linked list to order the nodes with most recently used nodes at tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move_to_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                self.remove_from_head()
            new_node = ListNode(key, value)
            self.cache[key] = new_node 
            self.add_to_end(new_node)
        
    def remove_from_head(self):
        if self.head.next != self.tail:
            node_to_remove = self.head.next
            del self.cache[node_to_remove.key]
            self.head.next = node_to_remove.next
            node_to_remove.next.prev = self.head
    
    def add_to_end(self, node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def move_to_end(self, node):
        if node != self.tail.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
            last_node = self.tail.prev
            last_node.next = node
            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node
