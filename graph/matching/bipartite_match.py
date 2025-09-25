N, M = 5,5
fromTo = [[1, 4],
          [3, 5],
          [2, 5],
          [1, 2],
          [3, 4]]

def find_bipartite_match(f):
    for to in fromTo[f]:
        if visited[to]:
            continue
        visited[to] = True
        if assigned[to] == -1 or find_bipartite_match(assigned[to]):
            assigned[to] = f
            return True
    return False

visited = [False] * (M + 1)
assigned = [-1] * (M + 1)
result = 0
for e in range(N):
    visited = [False] * (M + 1)
    if find_bipartite_match(e):
        result += 1
print(result)