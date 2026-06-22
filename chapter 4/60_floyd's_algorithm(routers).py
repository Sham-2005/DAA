def floyd_routers():
    nodes = {c: i for i, c in enumerate("ABCDEF")}
    n = 6
    inf = float('inf')
    dist = [[inf] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    edges = [('A','B',1),('A','C',5),('B','C',2),('B','D',1),
             ('C','E',3),('D','E',1),('D','F',6),('E','F',2)]
    def run_floyd(current_edges):
        d = [row[:] for row in dist]
        for u, v, w in current_edges:
            d[nodes[u]][nodes[v]] = w
            d[nodes[v]][nodes[u]] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d
    d1 = run_floyd(edges)
    edges_fail = [e for e in edges if not ({e[0],e[1]} == {'B','D'})]
    d2 = run_floyd(edges_fail)
    print(f"A to F (Normal): {d1[nodes['A']][nodes['F']]}")
    print(f"A to F (Failure): {d2[nodes['A']][nodes['F']]}")
floyd_routers() 