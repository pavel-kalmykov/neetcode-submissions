class MyLinkedListNode:

    def __init__(self, val = None, prev_node = None, next_node = None) -> None:
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node


class MyLinkedList:

    def __init__(self):
        self.head = MyLinkedListNode()
        self.tail = MyLinkedListNode()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.len = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        curr = self.head.next_node
        for _ in range(index):
            curr = curr.next_node
        return curr.val


    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedListNode(val, self.head, self.head.next_node)
        self.head.next_node.prev_node = new_node
        self.head.next_node = new_node
        self.len += 1

    def addAtTail(self, val: int) -> None:
        new_node = MyLinkedListNode(val, self.tail.prev_node, self.tail)
        self.tail.prev_node.next_node = new_node
        self.tail.prev_node = new_node
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        elif index == self.len:
            return self.addAtTail(val)
        curr = self.head.next_node
        for _ in range(index):
            curr = curr.next_node

        new_node = MyLinkedListNode(val, curr.prev_node, curr)
        curr.prev_node.next_node = new_node
        curr.prev_node = new_node
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        curr = self.head.next_node
        for _ in range(index):
            curr = curr.next_node

        curr.prev_node.next_node = curr.next_node
        curr.next_node.prev_node = curr.prev_node
        self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)