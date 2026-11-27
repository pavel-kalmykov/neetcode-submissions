class BrowserHistoryNode:

    def __init__(self, url = None, prev_node = None, next_node = None) -> None:
        self.url = url
        self.prev_node = prev_node
        self.next_node = next_node


class BrowserHistory:

    def __init__(self, homepage: str):
        self.index = BrowserHistoryNode(homepage, None, None)
        self.head = BrowserHistoryNode(None, None, self.index)
        self.tail = BrowserHistoryNode(None, self.index, None)
        self.index.prev_node = self.head
        self.index.next_node = self.tail

    def visit(self, url: str) -> None:
        new_node = BrowserHistoryNode(url, self.index, self.tail)
        self.tail.prev_node = new_node
        self.index.next_node = new_node
        self.index = new_node

    def back(self, steps: int) -> str:
        while self.index.prev_node is not self.head and steps > 0:
            self.index = self.index.prev_node
            steps -= 1
        return self.index.url

    def forward(self, steps: int) -> str:
        while self.index.next_node is not self.tail and steps > 0:
            self.index = self.index.next_node
            steps -= 1
        return self.index.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)