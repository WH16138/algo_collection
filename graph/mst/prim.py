import heapq

n,m = map(int,input().split())

adj = [[] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))

def prim(n,adj):
    visited = [0]*n
    min_heap = [(0,0)] # w,u
    mst = 0
    while min_heap:
        w,u = heapq.heappop(min_heap)
        if visited(u):
            continue
        visited[u] = 1
        mst += w
        for v,cost in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (cost,v))
    return mst