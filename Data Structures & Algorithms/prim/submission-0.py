class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, weight in edges:
            adj[src].append((dst, weight))
            adj[dst].append((src, weight))

        heapq.heapify((pq := [(weight, neighbor) for neighbor, weight in adj[0]]))
        mst = 0
        visited = {0}
        while pq:
            weight, node = heapq.heappop(pq)
            if node in visited:
                continue

            mst += weight
            visited.add(node)
            if len(visited) == n:
                return mst
            for neigh_node, neigh_weight in adj[node]:
                if neigh_node not in visited:
                    heapq.heappush(pq, (neigh_weight, neigh_node))
        return -1
