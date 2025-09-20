"""
(Handles negative weights, can detect negative cycles)

Problem

A currency exchange system with possible gains/losses. Find the cheapest cost from node 0 to all others.
Graph (negative edge allowed):

0 --(4)--> 1
0 --(5)--> 2
1 --(-3)--> 2
2 --(2)--> 3
"""


def bellman_ford(num_nodes, edges, start):
    # Distance array
    min_distance = [float('inf')] * num_nodes
    min_distance[start] = 0

    # Relax all edges num_nodes - 1 times
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in edges:
            if min_distance[u] == float("inf"):
                continue
            if min_distance[u] + w < min_distance[v]:
                min_distance[v] = min_distance[u] + w
                updated = True
        if not updated:  # optimisation for early stop
            break

    # check for negative cycles
    for u, v, w in edges:
        if min_distance[u] != float("inf") and min_distance[u] + w < min_distance[v]:
            raise ValueError("Negative cycle detected")
    return min_distance
