from collections import deque
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
def kruskal_weight(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    weight = 0
    count = 0
    for u, v, w in edges:
        if uf.union(u, v):
            weight += w
            count += 1
    return weight if count == n - 1 else float('inf')
def find_path_max_weight(adj, start, end):
    queue = deque([(start, [])]) 
    visited = {start}
    while queue:
        curr, path = queue.popleft()
        if curr == end:
            return path
        for neighbor, weight in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                edge = (min(curr, neighbor), max(curr, neighbor), weight)
                queue.append((neighbor, path + [edge]))
    return []
def verify_mst_uniqueness(n, all_edges, given_mst):
    optimal_weight = kruskal_weight(n, list(all_edges))
    given_weight = sum(w for u, v, w in given_mst)
    if given_weight != optimal_weight:
        print("The given set is not a Minimum Spanning Tree (Weights do not match).")
        return
    mst_adj = [[] for _ in range(n)]
    mst_edges_set = set()
    for u, v, w in given_mst:
        mst_adj[u].append((v, w))
        mst_adj[v].append((u, w))
        mst_edges_set.add((min(u,v), max(u,v), w))
    for u, v, w in all_edges:
        normalized_edge = (min(u,v), max(u,v), w)
        if normalized_edge in mst_edges_set:
            continue
        path_in_mst = find_path_max_weight(mst_adj, u, v)
        for pu, pv, pw in path_in_mst:
            if pw == w:
                print("Is the given MST unique?")
                print("False")
                new_mst = list(given_mst)
                for i, edge in enumerate(new_mst):
                    norm = (min(edge[0], edge[1]), max(edge[0], edge[1]), edge[2])
                    if norm == (pu, pv, pw):
                        new_mst.pop(i)
                        break
                new_mst.append((u, v, w))
                print(f"Another possible MST: {new_mst}")
                print(f"Total weight of MST: {given_weight}")
                return
    print("Is the given MST unique?")
    print("True")
print("--- Test Case 1 ---")
edges1 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
given_mst1 = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
verify_mst_uniqueness(4, edges1, given_mst1)
print("\n--- Test Case 2 ---")
edges2 = [(0, 1, 1), (0, 2, 1), (1, 3, 2), (2, 3, 2), (3, 4, 3), (4, 2, 3)]
given_mst2 = [(0, 1, 1), (0, 2, 1), (1, 3, 2), (3, 4, 3)]
verify_mst_uniqueness(5, edges2, given_mst2)
