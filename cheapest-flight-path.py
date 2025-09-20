import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]


class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Min-heap: (cost_so_far, node, stops_used)
        heap = [(0, src, 0)]

        # Keep track of the best cost to reach (node, stops)
        best = [[float("inf")] * (k + 2) for _ in range(n)]
        best[src][0] = 0

        while heap:
            cost, node, stops = heapq.heappop(heap)
            # If we reach destination, return the cost
            if node == dst:
                return cost

            # If we’ve already used k+1 edges, can’t continue
            if stops == k + 1:
                continue

            # Explore neighbors
            for nei, price in graph[node]:
                new_cost = cost + price
                if new_cost < best[nei][stops + 1]:
                    best[nei][stops + 1] = new_cost
                    heapq.heappush(heap, (new_cost, nei, stops + 1))

        return -1
