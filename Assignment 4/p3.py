#8 queens using branch and bound depth first search

from queue import PriorityQueue

def bbdfs_8queens():
    start_state = []
    n = int(input("Enter the board dimension (n): "))
    for i in range(n):
        start_state.append(-1)

    stack = [(0, start_state)]
    best_cost = float('inf')
    best_solution = None

    while stack:
        node = stack.pop()
        cost = node[0]
        state = node[1]

        if cost >= best_cost:  # prune if cost is higher than the best solution found so far
            continue

        if is_goal_state(state):
            best_cost = cost
            best_solution = state
            continue

        row = state.index(-1)
        for col in range(n):
            if is_valid(state, col):
                child = state.copy()
                child[row] = col
                child_cost = cost + 1 + lower_bound(child)  # compute cost of child node
                stack.append((child_cost, child))

    return best_solution

def is_valid(state, col):
    row = state.index(-1)
    for i in range(row):
        #diagonal check : aboslute differnce between current column and column of the queen in previous row(if = row distance,attack possible)
        if state[i] == col or abs(state[i] - col) == row - i:
            return False
    return True

def is_goal_state(state):
    return state.count(-1) == 0

def lower_bound(state):
    # compute a lower bound on the cost of the optimal solution that can be obtained from the given state
    # one possible lower bound is the number of conflicts between queens on the board
    conflicts = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i]-state[j]) == j-i:
                conflicts += 1
    return conflicts

# the is_valid and is_goal_state functions remain the same as in the original code

solution = bbdfs_8queens()
if solution is not None:
    print(solution)
else:
    print("No solution found.")
