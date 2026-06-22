import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def closest_pair(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
closest, min_d = closest_pair(points)
print(f"Closest pair: {closest[0]} - {closest[1]}") 
print(f"Minimum distance: {min_d}") 
