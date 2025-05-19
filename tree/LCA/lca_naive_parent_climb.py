from collections import deque
N = 10

adjlist = []

parent = [0]*(N)
dist = [0]*(N)
depth = [0]*(N)

root = 1
parent[root] = -1
q = deque([root])

while q:
    cur = q.popleft()

    for next, w in adjlist[cur]:
        if parent[cur] == next:
            continue
        parent[next] = cur
        dist[next] = w
        depth[next] = depth[cur] + 1
        q.append(next)

def lca(x,y):
    while x != y:
        if depth[x] == depth[y]:
            x = parent[x]
            y = parent[y]
        elif depth[x] > depth[y]:
            x = parent[x]
        else:
            y = parent[y]
    return x