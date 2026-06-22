import sys
def tsp_bruteforce_matrix(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    min_cost = [float('inf')]

    def backtrack(curr_city, count, cost, path):
        if count == n:
            min_cost[0] = min(min_cost[0], cost + graph[curr_city][0])
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                backtrack(i, count + 1, cost + graph[curr_city][i], path + [i])
                visited[i] = False

    backtrack(0, 1, 0, [0])
    return min_cost[0]
matrix1 = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(f"Output 1: {tsp_bruteforce_matrix(matrix1)}") 

matrix2 = [
    [0, 10, 10, 10],
    [10, 0, 10, 10],
    [10, 10, 0, 10],
    [10, 10, 10, 0]
]
print(f"Output 2: {tsp_bruteforce_matrix(matrix2)}") 

matrix3 = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]
print(f"Output 3: {tsp_bruteforce_matrix(matrix3)}") 