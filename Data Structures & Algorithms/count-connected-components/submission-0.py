class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    # Find parent of x, with path compression.
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.par[px] = py
            self.rank[py] += self.rank[px]
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = n
        uf = UnionFind(n)
        for a, b in edges:
            if uf.union(a, b):
                components -= 1
        return components
