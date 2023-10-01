#8 queens using A*

from queue import PriorityQueue

def a_star_8queens():
    start_state = []
    n = int(input("Enter the board dimension (n): "))
    for i in range(n):
        start_state.append(-1)

    q = PriorityQueue()
    q.put((0, start_state))

    while not q.empty():
        node = q.get()
        cost = node[0]
        state = node[1]

        if is_goal_state(state):
            return state

        for col in range(n):
            if is_valid(state, col):
                child = state.copy()
                child[state.index(-1)] = col
                h_cost = heuristic(child)
                q.put((cost + 1 + h_cost, child))

    return None

def is_valid(state, col):
    row = state.index(-1)
    for i in range(row):
        #diagonal check : aboslute differnce between current column and column of the queen in previous row(if = row distance,attack possible)
        if state[i] == col or abs(state[i] - col) == row - i:
            return False
    return True

def is_goal_state(state):
    return state.count(-1) == 0

def heuristic(state):
    attacks = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

solution = a_star_8queens()
if solution is not None:
    print(solution)
else:
    print("No solution found.")
