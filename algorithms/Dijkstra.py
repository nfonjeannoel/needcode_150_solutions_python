"""
(Works great with non-negative weights, no stop limits)
Problem

You are given a city road map with travel times between intersections. Find the shortest travel time from intersection A (0) to all others.

Graph (non-negative weights):

0 --(4)--> 1
0 --(2)--> 2
1 --(5)--> 2
1 --(10)-> 3
2 --(3)--> 3
"""

import heapq
from collections import defaultdict


def dijkstra(num_nodes, edges, start):
    graph = defaultdict(list)

    # Build adjacency list
    for s, d, w in edges:
        graph[s].append((d, w))

    # Distance array
    min_distance = [float('inf')] * num_nodes
    min_distance[start] = 0

    # Priority queue: (distance_so_far, node)
    pq = [(0, start)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > min_distance[node]:
            continue
        for neb, w in graph[node]:
            new_dist = curr_dist + w
            if new_dist < min_distance[neb]:
                min_distance[neb] = new_dist
                heapq.heappush(pq, (new_dist, neb))

    return min_distance
