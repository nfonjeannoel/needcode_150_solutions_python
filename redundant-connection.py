from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        def connected(skip_edge):
            u, v = skip_edge
            visited = set()
            def dfs(i):
                visited.add(i)
                for neb in adj[i]:
                    if (i, neb) == (u, v) or (i, neb) == (v, u):
                        continue
                    if neb not in visited:
                        dfs(neb)
            dfs(1)
            return len(visited) == n

        for u, v in reversed(edges):
            if connected((u, v)):
                return [u, v]