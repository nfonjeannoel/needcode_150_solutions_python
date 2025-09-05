from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            visited.add((sr, sc))
            region = [(sr, sc)]
            touches_border = (sr == 0 or sc == 0 or sr == ROWS-1 or sc == COLS-1)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < ROWS and 0 <= nc < COLS):
                        continue
                    if board[nr][nc] != 'O' or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    region.append((nr, nc))
                    if nr == 0 or nc == 0 or nr == ROWS-1 or nc == COLS-1:
                        touches_border = True
                    q.append((nr, nc))

            # Flip only if fully enclosed
            if not touches_border:
                for r, c in region:
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visited:
                    bfs(r, c)

from collections import deque
from typing import List

class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # start from outer elemts. Could also use for r, for c
        # then check if O or r in [0, ROWS-1] or c in [0, cols - 1]
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"