#8 queens using hill climbing (steepst accent)

import random

def hill_climbing_8queens():
    n = int(input("Enter the board dimension (n): "))
    current_state = generate_random_state(n)
    print("Randomly generaed initial state : ",current_state)

    while True:
        best_successor = None
        best_score = score_state(current_state)

        if best_score == 0:  # found a solution
            print("Global minimum reached!")
            print(current_state)
            #return current_state

        for successor in generate_successors(current_state):
            score = score_state(successor)
            if score < best_score:
                best_successor = successor
                best_score = score

        if best_successor is None:  # reached a local minimum
            print("Stuck in Local minima")
            print(current_state)
            return None

        current_state = best_successor

def generate_random_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def generate_successors(state):
    n = len(state)
    successors = []
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                successor = state.copy()
                successor[col] = row
                successors.append(successor)
    return successors

def score_state(state):
    # compute the number of conflicts between queens on the board
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == j-i:
                conflicts += 1
    return conflicts

solution = hill_climbing_8queens()