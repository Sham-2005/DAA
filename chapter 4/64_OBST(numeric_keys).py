def obst_numeric(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    for i in range(n): cost[i][i] = freq[i]
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = float('inf')
            weight_sum = sum(freq[i:j+1])
            for r in range(i, j + 1):
                c = weight_sum
                if r > i: c += cost[i][r-1]
                if r < j: c += cost[r+1][j]
                if c < cost[i][j]: cost[i][j] = c
    return cost[0][n-1]
print(f"OBST (10,12,16,21): {obst_numeric([10,12,16,21], [4,2,6,3])}") 
print(f"OBST (10,12): {obst_numeric([10,12], [34,50])}") 