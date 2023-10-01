#8 Queens using UCS

#by default priority queue pops elements in ascending order 

from queue import PriorityQueue

def ucs_8queens():
    start_state = []
    n = int(input("Enter the board dimesion (n) : "))
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
                q.put((cost + 1, child))

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

solution = ucs_8queens()
if solution is not None:
    print(solution)
else:
    print("No solution found.")


#The cost of the starting state is 0, since there are no queens placed on the board yet. When generating the successor states, 
#we place a queen in the next row of the board, which means the cost of the successor state is the number of queens already placed on the board plus 1.
#The cost is used as the priority value in the priority queue, so the algorithm explores the states in increasing order of their cost. 
#This ensures that we explore the states with fewer queens first, which may lead to a solution faster than exploring the states with more queens.
#The goal of the algorithm is to find a solution state with 8 queens placed on the board, which means the cost of the solution state will be 8. 
#Once a solution state is found, the algorithm can terminate and return the solution.