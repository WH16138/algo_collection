import sys
sys.setrecursionlimit(10**7)

def tarjan(N, adj):
    visi_time = [0] * (N + 1)
    time_low = [0] * (N + 1)
    visited = [False] * (N + 1)
    is_art = [False] * (N + 1)
    bridges = []

    time = 0

    def dfs(u, par):
        nonlocal time
        visited[u] = True
        time += 1
        visi_time[u] = time
        time_low[u] = time

        child_count = 0

        for v in adj[u]:
            if not visited[v]:
                child_count += 1
                dfs(v, u)
                time_low[u] = min(time_low[u], time_low[v])
                if par != -1 and time_low[v] >= visi_time[u]:
                    is_art[u] = True
                if time_low[v] > visi_time[u]:
                    bridges.append((u,v))
            elif v != par:
                time_low[u] = min(time_low[u], visi_time[v])
        if par == -1 and child_count >=2:
                is_art[u] = True

    for u in range(1, N+1): # if graph is not connected 
        if not visited[u]:
            dfs(u, -1)

    articulation_points = [u for u in range(1, N+1) if is_art[u]]
    return articulation_points, sorted(bridges)


# test case 1
if __name__ == "__main__":
    N = 5
    adj = {
        1: [2, 4],
        2: [1, 3, 5],
        3: [2],
        4: [1],
        5: [2]
    }

    arts, brs = tarjan(N, adj)
    print("단절점:", arts)  # expected output: [1, 2]
    print("단절선:", brs)   # expected output: [(1, 2), (1, 4), (2, 3), (2, 5)]