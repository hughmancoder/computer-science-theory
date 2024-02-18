class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None

class HashMap:
    def __init__(self):
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key, value):
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.key == key:
                    cur.value = value  # Update value
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key):
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key):
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.key == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    break
                cur, prev = cur.next, prev.next

def main():
    my_map = HashMap()

    # Test put()
    my_map.put(1, 10) 
    my_map.put(2, 20)
    my_map.put(1, 15)  # Update existing value

    # Test get()
    print(my_map.get(1))   # Should print 15
    print(my_map.get(3))   # Should print -1 (not found)

    # Test remove()
    my_map.remove(2)
    print(my_map.get(2))   # Should print -1 

if __name__ == "__main__":
    main()
