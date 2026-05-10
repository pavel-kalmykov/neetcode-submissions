class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        queue = deque([(0, 0)])

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == m - 1 and c == n - 1:
                    return length
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dr, dc = r + dr, c + dc
                    if not(
                        0 <= dr < m
                        and 0 <= dc < n
                        and not visited[dr][dc]
                        and grid[dr][dc] == 0
                    ):
                        continue
                    visited[dr][dc] = True
                    queue.append((dr, dc))
            length += 1
        return -1
