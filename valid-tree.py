from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for neb in adj[i]:
                if neb == prev:
                    # we came from this node. False loop. goes both direction
                    continue
                if not dfs(neb, i): return False

            return True

        return dfs(0, -1) and len(visited) == n

from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for neb in adj[node]:
                if neb == parent:
                    continue
                if neb in visit:
                    return False
                visit.add(neb)
                q.append((neb, node))

        return len(visit) == n