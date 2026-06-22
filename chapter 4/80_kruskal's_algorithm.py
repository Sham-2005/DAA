class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False
def kruskal_mst(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0
    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
    return mst_edges, total_weight
edges_k1 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst1, w1 = kruskal_mst(4, edges_k1)
print(f"MST 1 Weight: {w1}, Edges: {mst1}")
edges_k2 = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
mst2, w2 = kruskal_mst(5, edges_k2)
print(f"MST 2 Weight: {w2}, Edges: {mst2}")