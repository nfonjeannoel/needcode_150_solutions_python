from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            count = 0
            while q:
                row, col = q.popleft()
                count += 1
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))

            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    islands = max(bfs(r, c), islands)

        return islands


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(dfs(r, c), area)

        return area