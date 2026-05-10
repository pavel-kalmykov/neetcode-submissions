class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def topological_dfs(node: int) -> bool:
            if node in curr_path:
                return False
            if node in visited:
                return True
            curr_path.add(node)
            visited.add(node)

            for neighbor in adj[node]:
                if not topological_dfs(neighbor):
                    return False

            top_sort.append(node)
            curr_path.remove(node)
            return True

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        top_sort = []
        visited = set()
        curr_path = set()

        for node in range(n):
            if not topological_dfs(node):
                return []

        top_sort.reverse()
        return top_sort
