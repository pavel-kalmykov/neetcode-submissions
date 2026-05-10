class UnionFind:
    
    def __init__(self, n: int):
        self.parents = {}
        self.ranks = {}
        self.num_components = n

        for i in range(n):
            self.parents[i] = i
            self.ranks[i] = 0

    def find(self, x: int) -> int:
        p = self.parents[x]
        while self.parents[p] != p:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p2] > self.ranks[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1
        
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
