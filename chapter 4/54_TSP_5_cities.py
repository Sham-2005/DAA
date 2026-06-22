import itertools
def tsp_5_cities():
    cities = ['A', 'B', 'C', 'D', 'E']
    dist = {
        ('A','B'): 10, ('A','C'): 15, ('A','D'): 20, ('A','E'): 25,
        ('B','C'): 35, ('B','D'): 25, ('B','E'): 30,
        ('C','D'): 30, ('C','E'): 20,
        ('D','E'): 15
    }
    def get_d(c1, c2):
        if c1 == c2: return 0
        pair = tuple(sorted((c1, c2)))
        return dist.get(pair, float('inf'))
    min_len = float('inf')
    best_path = []
    for p in itertools.permutations(['B', 'C', 'D', 'E']):
        path = ['A'] + list(p)
        current_len = 0
        for i in range(len(path) - 1):
            current_len += get_d(path[i], path[i+1])
        current_len += get_d(path[-1], 'A') 
        if current_len < min_len:
            min_len = current_len
            best_path = path + ['A']
    return best_path, min_len
path, length = tsp_5_cities()
print(f"Shortest Route: {path}, Distance: {length}")