import itertools
import math
def dist(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
def tsp(cities):
    start_city = cities[0]
    other_cities = cities[1:]
    min_distance = float('inf')
    best_path = []
    for perm in itertools.permutations(other_cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_dist = 0
        for i in range(len(current_path) - 1):
            current_dist += dist(current_path[i], current_path[i+1])
        if current_dist < min_distance:
            min_distance = current_dist
            best_path = current_path
    return min_distance, best_path
cities1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
d, p = tsp(cities1)
print(f"Shortest Distance: {d}")
print(f"Shortest Path: {p}")