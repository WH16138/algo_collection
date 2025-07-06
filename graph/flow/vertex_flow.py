from collections import deque

def edmonds_karp(graph, source, sink):
    # Initialize flow matrix with 0s
    flow = [[0] * len(graph) for _ in range(len(graph))]
    max_flow = 0

    while True:
        # BFS to find shortest augmenting path
        parent = [-1] * len(graph)
        que = deque([source])
        while que:
            u = que.popleft()
            for v in range(len(graph)):
                # If v is unvisited and residual capacity exists
                if parent[v] == -1 and graph[u][v] > flow[u][v]:
                    parent[v] = u
                    que.append(v)
                    if v == sink:
                        break  # Early exit if sink is reached

        if parent[sink] == -1:
            # No more augmenting paths exist
            break

        # Find bottleneck (minimum residual capacity) along the path
        min_capacity = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            min_capacity = min(min_capacity, graph[u][v] - flow[u][v])
            v = parent[v]

        # Update flow along the path
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += min_capacity
            flow[v][u] -= min_capacity
            v = parent[v]

        # Accumulate total flow
        max_flow += min_capacity

    return max_flow

# Read number of vertices (n) and number of edges (p)
n, p = map(int, input().split())

# We define:
# - sourceOut: split "source" node's output half
# - sinkIn: split "sink" node's input half
sourceOut = n + 1  # Assuming node 1 is source, we use 1+n as sourceOut
sinkIn = 2         # Node 2 is the sink's input half (unsplit, as no in/out needed)

# Capacities
Ecap = 1  # Edge capacity (bidirectional in input)
Vcap = 1  # Vertex capacity (default 1 per vertex)

# Total number of vertices = 2*n (each node is split into in and out)
capacity = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

# Read and construct the graph with node-splitting and edge constraints
for _ in range(p):
    u, v = map(int, input().split())

    # Add edge u_out -> v_in (u's out half to v's in half)
    capacity[n + u][v] += Ecap
    capacity[v][n + v] = Vcap  # v_in -> v_out to enforce vertex capacity

    # Add edge v_out -> u_in as graph is undirected
    capacity[n + v][u] += Ecap
    capacity[u][n + u] = Vcap  # u_in -> u_out

# Compute and print the max flow from sourceOut to sinkIn
print(edmonds_karp(capacity, sourceOut, sinkIn))

# 백준 2316 문제의 정답 코드