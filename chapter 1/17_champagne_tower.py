def champagneTower(poured, query_row, query_glass):
    tower = [[0] * k for k in range(1, 102)]
    tower[0][0] = poured
    for r in range(query_row + 1):
        for c in range(r + 1):
            excess = (tower[r][c] - 1.0) / 2.0
            if excess > 0:
                tower[r+1][c] += excess
                tower[r+1][c+1] += excess
    return min(1, tower[query_row][query_glass])
print(champagneTower(1, 1, 1))
print(champagneTower(2, 1, 1))