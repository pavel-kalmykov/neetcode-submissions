from collections import deque


class Graph:
    
    def __init__(self):
        self.nodes: dict[int, list[int]] = {}

    def addEdge(self, src: int, dst: int) -> None:
        for vertex in [src, dst]:
            if not vertex in self.nodes:
                self.nodes[vertex] = []
        self.nodes[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        for vertex in [src, dst]:
            if not vertex in self.nodes:
                return False
        self.nodes[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = {src}
        queue = deque([src])

        while queue:
            for _ in range(len(queue)):
                vertex = queue.popleft()
                if vertex == dst:
                    return True
                for neighbour in self.nodes[vertex]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        return False

