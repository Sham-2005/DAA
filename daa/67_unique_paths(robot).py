def unique_paths(m, n):
    row = [1] * n
    for i in range(m - 1):
        new_row = [1] * n
        for j in range(1, n):
            new_row[j] = new_row[j-1] + row[j]
        row = new_row
    return row[-1]
print(f"3x7: {unique_paths(3, 7)}") 
print(f"3x2: {unique_paths(3, 2)}") 