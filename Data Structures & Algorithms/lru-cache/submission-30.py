# Definition for doubly-linked list node.
class ListNode:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}
        self.LRU = None      # least recently used
        self.latest = None   # most recently used

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        cur = self.keys[key]

        # si ya es el más reciente, no mover nada
        if cur == self.latest:
            return cur.val

        # si es el LRU
        elif cur == self.LRU:
            self.LRU = cur.next
            if self.LRU:
                self.LRU.prev = None

            cur.next = None
            cur.prev = self.latest
            self.latest.next = cur
            self.latest = cur

        # si está en medio
        else:
            prev = cur.prev
            next_ = cur.next

            prev.next = next_
            next_.prev = prev

            cur.prev = self.latest
            cur.next = None
            self.latest.next = cur
            self.latest = cur

        return cur.val

    def put(self, key: int, value: int) -> None:
        # si la key ya existe, actualizar valor y mover a latest
        if key in self.keys:
            self.keys[key].val = value
            self.get(key)
            return

        # si está vacío
        if not self.LRU:
            new_node = ListNode(value, key)
            self.keys[key] = new_node
            self.LRU = new_node
            self.latest = new_node
            return

        # agregar nuevo nodo al final
        new_node = ListNode(value, key)
        new_node.prev = self.latest
        self.latest.next = new_node
        self.latest = new_node
        self.keys[key] = new_node

        # si excede capacidad, borrar LRU
        if len(self.keys) > self.capacity:
            old_lru = self.LRU
            del self.keys[old_lru.key]

            self.LRU = old_lru.next
            if self.LRU:
                self.LRU.prev = None

            old_lru.next = None
