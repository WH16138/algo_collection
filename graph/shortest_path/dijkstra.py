import heapq as h

def dijkstra(n, adj, s=1):
    dist = [float("inf")] * (n+1) # minimum distance
    dist[s] = 0 # initializing the starting node
    visited = [0] * (n+1) 
    parent = [-1] * (n+1) # route tracking

    que = [(0, s)] # (dist, node)
    while que:
        d, u = h.heappop(que)
        if visited[u]:continue
        visited[u] = 1
        for v, cost in adj[u]:
            if d + cost < dist[v]:
                dist[v] = d + cost
                parent[v] = u
                h.heappush(que, (dist[v], v))

    return dist, parent

# ex 1
N, M, S = 3, 3, 1
adj = [[] for _ in range(N+1)]
adj[1].append((2, 4))
adj[1].append((3, 1))
adj[3].append((2, 2))
print(dijkstra(N, adj, S))
# ([inf, 0, 3, 1], [-1, -1, 3, 1])

# ex 2
N, M, S = 4, 2, 1
adj = [[] for _ in range(N+1)]
adj[1].append((2, 5))
adj[3].append((4, 7))
print(dijkstra(N, adj, S))
# ([inf, 0, 5, inf, inf], [-1, -1, 1, -1, -1])

# ex 3
N, M, S = 5, 6, 2
adj = [[] for _ in range(N+1)]
adj[1].append((2, 2))
adj[1].append((3, 5))
adj[2].append((3, 1))
adj[2].append((4, 2))
adj[3].append((5, 3))
adj[4].append((5, 1))
print(dijkstra(N, adj, S))
# ([inf, inf, 0, 1, 2, 3], [-1, -1, -1, 2, 2, 4])