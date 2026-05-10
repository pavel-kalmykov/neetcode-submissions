class DequeItem:

  def __init__(
      self,
      value: int,
      prev_item: "DequeItem | None" = None,
      next_item: "DequeItem | None" = None,
  ):
    self.value = value
    self.prev = prev_item
    self.next = next_item


class Deque:

  def __init__(self):
    self.head = DequeItem(-1)
    self.tail = DequeItem(-1)

    self.head.next = self.tail
    self.tail.prev = self.head

  def isEmpty(self) -> bool:
    return self.head.next is self.tail

  def append(self, value: int) -> None:
    assert self.tail.prev
    new_item = DequeItem(value, self.tail.prev, self.tail)
    self.tail.prev.next = new_item
    self.tail.prev = new_item

  def appendleft(self, value: int) -> None:
    assert self.head.next
    new_item = DequeItem(value, self.head, self.head.next)
    self.head.next.prev = new_item
    self.head.next = new_item

  def pop(self) -> int:
    if self.isEmpty():
      return -1
    return self.__delete_item(self.tail.prev).value

  def popleft(self) -> int:
    if self.isEmpty():
      return -1
    return self.__delete_item(self.head.next).value

  def __delete_item(self, item: DequeItem| None) -> DequeItem:
    assert item and item.prev and item.next
    item.prev.next = item.next
    item.next.prev = item.prev
    return item

