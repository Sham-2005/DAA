def get_convex_hull(points):
    n = len(points)
    if n < 3: return points
    hull = set()
    for i in range(n):
        for j in range(n):
            if i == j: continue
            valid_edge = True
            for k in range(n):
                if k == i or k == j: continue
                cp = (points[j][0] - points[i][0]) * (points[k][1] - points[i][1]) - \
                     (points[j][1] - points[i][1]) * (points[k][0] - points[i][0])
                if cp < 0: 
                    valid_edge = False
                    break
            if valid_edge:
                hull.add(points[i])
                hull.add(points[j])
    return sorted(list(hull))
pts = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
print(get_convex_hull(pts))