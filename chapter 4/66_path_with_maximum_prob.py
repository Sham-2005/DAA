import heapq
def max_probability(n, edges, succProb, start, end):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, succProb[i]))
        adj[v].append((u, succProb[i]))
    pq = [(-1.0, start)] 
    probs = [0.0] * n
    probs[start] = 1.0
    while pq:
        p, node = heapq.heappop(pq)
        p = -p
        if node == end: return p
        for neighbor, weight in adj[node]:
            if p * weight > probs[neighbor]:
                probs[neighbor] = p * weight
                heapq.heappush(pq, (-probs[neighbor], neighbor))
    return 0.0
print(f"Max Prob: {max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2)}")