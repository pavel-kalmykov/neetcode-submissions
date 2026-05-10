class Solution:

    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 1 or visited[r][c]:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            visited[r][c] = True
            count = 0 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
            visited[r][c] = False
            return count

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        return dfs(0, 0)
