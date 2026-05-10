class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

class LinkedList:
    
    def __init__(self):
        self.head = Node(None)
    
    def get(self, index: int) -> int:
        node = self.head.next
        i = 0
        while node:
            if index == i:
                return node.val
            i += 1
            node = node.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node

    def insertTail(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

    def remove(self, index: int) -> bool:
        prev, node = self.head, self.head.next
        i = 0
        while node:
            if index == i:
                prev.next = node.next
                return True
            i += 1
            prev, node = node, node.next
        return False

    def getValues(self) -> List[int]:
        values = []
        node = self.head.next
        while node:
            values.append(node.val)
            node = node.next
        return values
