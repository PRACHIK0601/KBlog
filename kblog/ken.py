#!/bin/python3

import os
from collections import defaultdict, deque

#
# Complete the 'getNumPairs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. WEIGHTED_INTEGER_GRAPH server
#  2. INTEGER signal_speed
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getNumPairs(server_nodes, server_from, server_to, server_weight, signal_speed):
    # Create the graph as an adjacency list
    graph = {i: [] for i in range(1, server_nodes + 1)}
    for i in range(len(server_from)):
        graph[server_from[i]].append((server_to[i], server_weight[i]))
        graph[server_to[i]].append((server_from[i], server_weight[i]))

    # BFS to calculate shortest distances from the starting node
    def bfs(start_node):
        distances = {i: float('inf') for i in range(1, server_nodes + 1)}
        distances[start_node] = 0
        queue = deque([(start_node, 0)])  # (node, distance)

        while queue:
            node, dist = queue.popleft()
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    queue.append((neighbor, new_dist))
        
        return distances

    result = []

    # For each server, calculate distances and count valid pairs
    for server in range(1, server_nodes + 1):
        distances = bfs(server)
        
        # Group nodes by distance % signal_speed
        modulo_groups = defaultdict(list)
        for node, dist in distances.items():
            modulo_groups[dist % signal_speed].append(node)
        
        # Count pairs
        pairs_count = 0
        for nodes in modulo_groups.values():
            n = len(nodes)
            pairs_count += (n * (n - 1)) // 2  # Number of pairs in a group
        
        result.append(pairs_count)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # File handler for output

    server_nodes, server_edges = map(int, input().rstrip().split())

    server_from = []
    server_to = []
    server_weight = []

    for _ in range(server_edges):
        from_node, to_node, weight = map(int, input().rstrip().split())
        server_from.append(from_node)
        server_to.append(to_node)
        server_weight.append(weight)

    signal_speed = int(input().strip())

    result = getNumPairs(server_nodes, server_from, server_to, server_weight, signal_speed)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
