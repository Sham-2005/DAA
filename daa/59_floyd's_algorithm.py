def find_city_threshold_1(n, edges, distanceThreshold):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = dist[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    min_reachable = n
    res = -1
    for i in range(n):
        count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
        if count <= min_reachable:
            min_reachable = count
            res = i
    return res
print(f"Output: {find_city_threshold_1(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)}") 