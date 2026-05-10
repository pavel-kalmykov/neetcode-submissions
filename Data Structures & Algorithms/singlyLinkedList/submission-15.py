class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

class LinkedList:
    
    def __init__(self):
        self.len = 0
        self.head = Node(None)
    
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        node = self.head.next
        for _ in range(index):
            node = node.next
        return node.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node
        self.len += 1

    def insertTail(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)
        self.len += 1

    def remove(self, index: int) -> bool:
        if index >= self.len:
            return False
        prev, node = self.head, self.head.next
        for _ in range(index):
            prev, node = node, node.next
        prev.next = node.next
        self.len -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head.next
        while node:
            values.append(node.val)
            node = node.next
        return values
