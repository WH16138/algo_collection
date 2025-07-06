from collections import deque

def edmonds_karp(graph, source, sink):
    flow = [[0] * len(graph) for _ in range(len(graph))]
    max_flow = 0

    while 1:
        parent = [-1] * len(graph)
        que = deque([source])
        while que: # BFS to find an augmenting path
            u = que.popleft()
            for v in range(len(graph)): # Iterate through all vertices
                if parent[v] == -1 and graph[u][v] > flow[u][v]:
                    parent[v] = u # Record the path
                    que.append(v)
                    if v == sink:
                        break

        if parent[sink] == -1: # No augmenting path found
            break

        min_capacity = float('inf')
        v = sink
        while v != source: # Backtrack to find the minimum capacity
            u = parent[v]
            min_capacity = min(min_capacity, graph[u][v] - flow[u][v])
            v = parent[v]

        v = sink
        while v != source: # Update the flow along the path
            u = parent[v]
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            v = parent[v]

        max_flow += min_capacity

    return max_flow

#e.g.
n = 5
capacity = [
    [0, 10, 5, 0, 0],
    [0, 0, 15, 25, 0],
    [0, 0, 0, 10, 10],
    [0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0]]

source = 0
sink = 4
max_flow = edmonds_karp(capacity, source, sink)
print(f"Maximum flow from node {source} to node {sink} is {max_flow}")
# Output: Maximum flow from node 0 to node 4 is 15