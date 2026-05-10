class LinkedList:

  class Node:
  
    def __init__(self, val: int, next_node: "LinkedList.Node | None"):
      self.val = val
      self.next = next_node
  
  def __init__(self):
    self.head: LinkedList.Node | None = None
    self.tail: LinkedList.Node | None = None
  
  def get(self, index: int) -> int:
    current_index = 0
    current_node = self.head
    while current_node:
      if current_index == index:
        return current_node.val
      current_index += 1
      current_node = current_node.next
    return -1
  
  def insertHead(self, val: int) -> None:
    self.head = LinkedList.Node(val, self.head)
    if not self.tail:
      self.tail = self.head
  
  def insertTail(self, val: int) -> None:
    new_node = LinkedList.Node(val, None)
    if self.tail:
      self.tail.next = new_node
    if not self.head:
      self.head = new_node
    self.tail = new_node
  
  def remove(self, index: int) -> bool:
    current_index = 0
    index_for_previous = index - 1
    current_node = self.head
  
    while current_index < index_for_previous and current_node:
      current_index += 1
      current_node = current_node.next
  
    if not current_node: # Not found
      return False
    if not current_node.next: # Only one node
      if index != 0:
        return False
      self.head = self.tail = None
    elif self.tail == current_node.next: # Last elem
      self.tail = current_node
      self.tail.next = None
    elif index == 0: # First elem
      self.head = current_node.next
    else:
      current_node.next = current_node.next.next
    return True

  def getValues(self) -> list[int]:
    values = []
    current_node = self.head
    while current_node:
      values.append(current_node.val)
      current_node = current_node.next
    return values
