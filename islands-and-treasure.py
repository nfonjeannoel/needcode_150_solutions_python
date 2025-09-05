from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque([(r, c)])
            visited = [[False] * COLS for _ in range(ROWS)]
            visited[r][c] == True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        # found treasure
                        return steps
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc] and grid[nr][nc] != -1:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)


from collections import deque


class Solution2:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()

        def addCell(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == -1 or (r, c) in visit:
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))

        dist = 0
        while q:
            lenq = len(q)
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1









