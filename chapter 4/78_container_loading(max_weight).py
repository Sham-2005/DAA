def max_weight_loading(weights, capacity):
    weights.sort(reverse=True)
    current_load = 0
    for w in weights:
        if current_load + w <= capacity:
            current_load += w
    return current_load
print(f"Max Load Ex 1: {max_weight_loading([10, 20, 30, 40, 50], 60)}")
print(f"Max Load Ex 2: {max_weight_loading([5, 10, 15, 20, 25, 30], 50)}")