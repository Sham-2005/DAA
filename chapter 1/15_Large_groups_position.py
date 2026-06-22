def largeGroupPositions(s):
    ans = []
    i = 0 
    n = len(s)
    for j in range(n):
        if j == n - 1 or s[j] != s[j + 1]:
            if j - i + 1 >= 3:
                ans.append([i, j])
            i = j + 1
    return ans

print(largeGroupPositions("abbxxxxzzy"))