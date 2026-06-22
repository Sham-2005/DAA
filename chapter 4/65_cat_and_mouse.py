from collections import deque
def cat_mouse_game(graph):
    n = len(graph)
    color = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    for m in range(n):
        for c in range(n):
            degree[m][c][1] = len(graph[m])
            degree[m][c][2] = len(graph[c])
            if 0 in graph[c]:
                degree[m][c][2] -= 1
    queue = deque()
    for c in range(1, n):
        for t in range(1, 3):
            color[0][c][t] = 1
            queue.append((0, c, t, 1))
    for i in range(1, n):
        for t in range(1, 3):
            color[i][i][t] = 2
            queue.append((i, i, t, 2))
    while queue:
        m, c, t, res = queue.popleft()
        prev_t = 3 - t  
        sources = []
        if prev_t == 1: 
            for prev_m in graph[m]:
                sources.append((prev_m, c, 1))
        else: 
            for prev_c in graph[c]:
                if prev_c != 0: 
                    sources.append((m, prev_c, 2))
        for pm, pc, pt in sources:
            if color[pm][pc][pt] != 0:
                continue
            if pt == res: 
                color[pm][pc][pt] = res
                queue.append((pm, pc, pt, res))
            else:
                degree[pm][pc][pt] -= 1
                if degree[pm][pc][pt] == 0:
                    color[pm][pc][pt] = res
                    queue.append((pm, pc, pt, res))
    return color[1][2][1]
graph1 = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
print(f"Ex 1 Output: {cat_mouse_game(graph1)}") 
graph2 = [[1,3],[0],[3],[0,2]]
print(f"Ex 2 Output: {cat_mouse_game(graph2)}")