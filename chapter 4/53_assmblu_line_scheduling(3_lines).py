def assembly_line_3():
    S = [[5, 9, 3], [6, 8, 4], [7, 6, 5]]
    T = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]
    n_stations = 3
    n_lines = 3
    dp = [[0] * n_stations for _ in range(n_lines)]
    for i in range(n_lines):
        dp[i][0] = S[i][0]
    for j in range(1, n_stations):
        for i in range(n_lines):
            best = float('inf')
            for k in range(n_lines):
                cost = dp[k][j-1] + T[k][i] + S[i][j]
                if cost < best:
                    best = cost
            dp[i][j] = best
    return min(dp[i][n_stations-1] for i in range(n_lines))
print("Min Production Time:", assembly_line_3())