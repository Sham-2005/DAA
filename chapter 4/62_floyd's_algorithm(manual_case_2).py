def floyd_manual_2():
    mapping = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
    n = 5
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    edges_data = [
        ('B','A',2),('A','C',3),('C','D',1),('D','A',6),('C','B',7),
        ('C','A',2),('A','B',4),('B','C',1),('B','E',6),('E','A',1),
        ('A','D',5),('D','E',2),('E','D',4),('D','C',1),('C','D',3)
    ] 
    for u, v, w in edges_data:
        i, j = mapping[u], mapping[v]
        dist[i][j] = min(dist[i][j], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print(f"C to A: {dist[mapping['C']][mapping['A']]}") 
    print(f"E to C: {dist[mapping['E']][mapping['C']]}") 
floyd_manual_2() 