import itertools
def solve_knapsack(weights, values, capacity):
    n = len(weights)
    indices = range(n)
    max_value = 0
    best_selection = []
    for r in range(1, n + 1):
        for subset in itertools.combinations(indices, r):
            current_weight = sum(weights[i] for i in subset)
            current_value = sum(values[i] for i in subset)
            if current_weight <= capacity:
                if current_value > max_value:
                    max_value = current_value
                    best_selection = list(subset)
    return best_selection, max_value
w = [2, 3, 1]
v = [4, 5, 3]
cap = 4
sel, val = solve_knapsack(w, v, cap)
print(f"Optimal Selection: {sel}") 
print(f"Total Value: {val}")       