import sys
def dijkstra_matrix(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    visited = [False] * n
    for _ in range(n):
        min_val = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i
        if u == -1: break
        visited[u] = True
        for v in range(n):
            if (not visited[v] and 
                graph[u][v] != float('inf') and 
                dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]
    return [d if d != float('inf') else 'Inf' for d in dist]
inf = float('inf')
g1 = [[0, 10, 3, inf, inf], 
      [inf, 0, 1, 2, inf], 
      [inf, 4, 0, 8, 2], 
      [inf, inf, inf, 0, 7], 
      [inf, inf, inf, 9, 0]]
print(f"Dijkstra Matrix Ex 1: {dijkstra_matrix(g1, 0)}")
g2 = [[0, 5, inf, 10], 
      [inf, 0, 3, inf], 
      [inf, inf, 0, 1], 
      [inf, inf, inf, 0]]
print(f"Dijkstra Matrix Ex 2: {dijkstra_matrix(g2, 0)}")