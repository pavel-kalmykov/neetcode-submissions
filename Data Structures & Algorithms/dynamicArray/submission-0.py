class DynamicArray:

  def __init__(self, capacity: int):
    self.__capacity = capacity
    self.__size = 0
    self.__data: list[None | int] = [None] * capacity

  def get(self, i: int) -> int:
    v = self.__data[i]
    assert isinstance(v, int)
    return v

  def set(self, i: int, n: int) -> None:
    self.__data[i] = n

  def pushback(self, n: int) -> None:
    self.__size += 1
    if self.__size > self.__capacity:
      self.resize()
    last_index = self.__size - 1
    self.__data[last_index] = n

  def popback(self) -> int:
    last_index = self.__size - 1
    v = self.__data[last_index]
    self.__size -= 1
    assert isinstance(v, int)
    return v
    

  def resize(self) -> None:
    self.__data = self.__data + [None] * self.__capacity
    self.__capacity *= 2

  def getSize(self) -> int:
    return self.__size

  def getCapacity(self) -> int:
    return self.__capacity
