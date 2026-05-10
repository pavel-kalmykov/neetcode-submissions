class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjacencies = {i: [] for i in range(n)}
        for source, dest, weight in edges:
            adjacencies[source].append((dest, weight))

        shortest_paths: dict[int, int] = {}
        min_heap = [(0, src)]
        while min_heap and len(shortest_paths) < n:
            weight, node = heapq.heappop(min_heap)
            if node in shortest_paths:
                continue
            shortest_paths[node] = weight

            for neigh_node, neigh_weight in adjacencies[node]:
                if neigh_node not in shortest_paths:
                    heapq.heappush(min_heap, (weight + neigh_weight, neigh_node))

        if len(shortest_paths) < n:
            for i in range(n):
                shortest_paths.setdefault(i, -1)

        return shortest_paths
