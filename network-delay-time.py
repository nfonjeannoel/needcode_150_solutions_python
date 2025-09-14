from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        nebs = defaultdict(list)
        for u, v, w in times:
            nebs[u].append((v, w))
        minHeap = [(0, k)]
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for neb, w2 in nebs[n1]:
                if neb in visited:
                    continue
                heapq.heappush(minHeap, (w1 + w2, neb))

        return t if len(visited) == n else -1


from collections import defaultdict
import heapq


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return

            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1

