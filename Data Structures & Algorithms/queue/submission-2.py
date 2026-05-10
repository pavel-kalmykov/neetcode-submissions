class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def isEmpty(self) -> bool:
        return self.head.next is self.tail
        
    def append(self, value: int) -> None:
        new_node = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
    def appendleft(self, value: int) -> None:
        new_node = Node(value, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        return last.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.head.next
        first.next.prev = self.head
        self.head.next = first.next
        return first.val
