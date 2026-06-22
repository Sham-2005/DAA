import heapq
def network_delay_time(times, n, k):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append((v, w))
    pq = [(0, k)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist: continue
        dist[node] = d
        for neighbor, weight in adj[node]:
            if neighbor not in dist:
                heapq.heappush(pq, (d + weight, neighbor))
    return max(dist.values()) if len(dist) == n else -1
print(f"Delay: {network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2)}") 