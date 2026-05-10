class MyStack:

    def __init__(self):
        self.queue = deque()
        self.aux_queue = deque()

    def push(self, x: int) -> None:
        self.aux_queue.append(x)
        while self.queue:
            self.aux_queue.append(self.queue.popleft())
        self.queue, self.aux_queue = self.aux_queue, self.queue

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()