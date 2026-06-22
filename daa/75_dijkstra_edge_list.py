import heapq
def dijkstra_edge_list(n, edges, source, target):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    pq = [(0, source)]
    dist = {source: 0}
    while pq:
        d, u = heapq.heappop(pq)
        if u == target:
            return d
        if d > dist.get(u, float('inf')):
            continue
        for v, w in adj[u]:
            if dist.get(u) + w < dist.get(v, float('inf')):
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))   
    return -1
edges1 = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
          (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
def dijkstra_edge_list_undirected(n, edges, source, target):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    pq = [(0, source)]
    dist = {i: float('inf') for i in range(n)}
    dist[source] = 0
    while pq:
        d, u = heapq.heappop(pq)
        if u == target: return d
        if d > dist[u]: continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return -1
print(f"Dijkstra Edge Ex 1: {dijkstra_edge_list_undirected(6, edges1, 0, 4)}") 
edges2 = [(0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4), (2, 3, 9), 
          (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)]
print(f"Dijkstra Edge Ex 2: {dijkstra_edge_list_undirected(5, edges2, 0, 3)}") 