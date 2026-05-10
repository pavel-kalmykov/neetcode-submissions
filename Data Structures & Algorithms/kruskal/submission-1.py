class UnionFind:
    def __init__(self, n):
        self.parent = self.makeSet(n)
        self.size = [1] * n
        self.count = n

    def makeSet(self, n):
        return [x for x in range(n)]

    # Time: O(logn) | Space: O(1)
    def find(self, node):
        while node != self.parent[node]:
            # path compression
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    # Time: O(1) | Space: O(1)
    def union(self, node1, node2) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        # already in the same set
        if root1 == root2:
            return False

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += 1
        else:
            self.parent[root1] = root2
            self.size[root2] += 1

        self.count -= 1
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heapq.heapify((pq := [(weight, src, dst) for src, dst, weight in edges]))
        uf = UnionFind(n)
        count = cost = 0
        while count < n - 1 and pq:
            weight, src, dst = heapq.heappop(pq)
            if not uf.union(src, dst):
                continue
            cost += weight
            count += 1
        return cost if count == n - 1 else -1
