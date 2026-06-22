def min_containers(weights, max_capacity):
    if not weights: return 0
    containers = 1
    current_capacity = 0
    for w in weights:
        if current_capacity + w <= max_capacity:
            current_capacity += w
        else:
            containers += 1
            current_capacity = w
    return containers
print(f"Min Containers Ex 1: {min_containers([5, 10, 15, 20, 25, 30, 35], 50)}")
print(f"Min Containers Ex 2: {min_containers([10, 20, 30, 40, 50, 60, 70, 80], 100)}")