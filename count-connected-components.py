from typing import List
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build undirected adjacency list
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        count = 0

        for i in range(n):
            if i in visited:
                continue
            # New component found
            count += 1
            q = deque([i])
            visited.add(i)  # mark when enqueuing

            while q:
                v = q.popleft()
                for nb in adj[v]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)

        return count
