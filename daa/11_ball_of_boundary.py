def findPaths(m, n, maxMove, startRow, startColumn):
    memo = {}

    def solve(i, j, moves):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1 
        if moves == 0:
            return 0 
        if (i, j, moves) in memo:
            return memo[(i, j, moves)]
        
        res = 0
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            res += solve(i + x, j + y, moves - 1)
        
        memo[(i, j, moves)] = res
        return res

    return solve(startRow, startColumn, maxMove)

print(findPaths(2, 2, 2, 0, 0))