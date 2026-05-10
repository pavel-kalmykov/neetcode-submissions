class LinkedList:
  class Node:
      def __init__(self, val: int, next_node: "LinkedList.Node | None"):
          self.val = val
          self.next = next_node

  def __init__(self):
      self.head: LinkedList.Node | None = None

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

  def insertTail(self, val: int) -> None:
      if not self.head:
          self.insertHead(val)
          return
      current_node = self.head
      while current_node.next:
          current_node = current_node.next
      current_node.next = LinkedList.Node(val, None)

  def remove(self, index: int) -> bool:
      if index == 0 and self.head:
          self.head = self.head.next
          return True
      current_index = 0
      current_node = self.head
      while current_node:
          if current_index + 1 == index and current_node.next:
              current_node.next = current_node.next.next
              return True
          current_index += 1
          current_node = current_node.next
      return False

  def getValues(self) -> list[int]:
      values = []
      current_node = self.head
      while current_node:
          values.append(current_node.val)
          current_node = current_node.next
      return values
