def count_tuples(A, B, C, D):
    map_ab = {}
    count = 0
    for a in A:
        for b in B:
            s = a + b
            map_ab[s] = map_ab.get(s, 0) + 1
    for c in C:
        for d in D:
            target = -(c + d)
            if target in map_ab:
                count += map_ab[target]
    return count
print(count_tuples([1, 2], [-2, -1], [-1, 2], [0, 2])) 