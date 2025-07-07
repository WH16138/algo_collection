from collections import deque

def spfa(start, graph, N):
    """
    Shortest Path Faster Algorithm (SPFA) for single-source shortest paths in a directed weighted graph.
    Args:
        start (int): The starting node index (0-based).
        graph (List[List[Tuple[int, float]]]): Adjacency list representing the graph, where graph[u] is a list of (v, cost) pairs.
        N (int): The number of nodes in the graph.
    Returns:
        List[float]: The shortest distances from the start node to every other node. If a node is unreachable, its distance will be float('inf').
    """
    INF = float('inf')
    dist = [INF] * N
    in_queue = [False] * N

    dist[start] = 0
    que = deque([start])
    in_queue[start] = True

    while que:
        u = que.popleft()
        in_queue[u] = False

        for v, cost in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if not in_queue[v]:
                    que.append(v)
                    in_queue[v] = True

    return dist