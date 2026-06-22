import itertools
def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    workers = range(n)
    tasks = range(n)
    min_cost = float('inf')
    best_assignment = []
    for perm in itertools.permutations(workers):
        current_cost = 0
        current_assignment = []
        for task_idx, worker_idx in enumerate(perm):
            current_cost += cost_matrix[worker_idx][task_idx]
            current_assignment.append((f"worker {worker_idx + 1}", f"task {task_idx + 1}"))
        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = current_assignment
    return best_assignment, min_cost
matrix = [[3, 10, 7], [8, 5, 12], [4, 6, 9]]
assign, cost = assignment_problem(matrix)
print(f"Optimal Assignment: {assign}")
print(f"Total Cost: {cost}")