from queue import PriorityQueue
import random

solution1 = 23

def find_blank(state):
    for i in range(len(state)):
        if state[i] == 0:
            return i
    return -1

def calculate_heuristic(state, goal_state):
    cost = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            cost += 1
    return cost

def calculate_cost(state):
    cost = cost + 1

def generate_successors(state):
    successors = []
    blank_index = find_blank(state)
    
    #left
    if blank_index not in [0, 4, 8, 12]:
        left_state = state[:]
        left_state[blank_index], left_state[blank_index-1] = left_state[blank_index-1], left_state[blank_index]
        successors.append((left_state, "Left"))
    
    #right
    if blank_index not in [3, 7, 11, 15]:
        right_state = state[:]
        right_state[blank_index], right_state[blank_index+1] = right_state[blank_index+1], right_state[blank_index]
        successors.append((right_state, "Right"))
    
    #up
    if blank_index not in [0, 1, 2, 3]:
        up_state = state[:]
        up_state[blank_index], up_state[blank_index-4] = up_state[blank_index-4], up_state[blank_index]
        successors.append((up_state, "Up"))
    
    #down
    if blank_index not in [12, 13, 14, 15]:
        down_state = state[:]
        down_state[blank_index], down_state[blank_index+4] = down_state[blank_index+4], down_state[blank_index]
        successors.append((down_state, "Down"))
    
    return successors

def ucs(initial_state, goal_state):

    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    explored = set()
    steps = []
    while not frontier.empty():
        state_cost, state = frontier.get()
        
        if state == goal_state:
            steps.append(state)
            while state != initial_state:
                for s in explored:
                    if s[0] == state and tuple(generate_successors(state)).count(s) > 0:
                        state = s[0]
                        steps.append(state)
            steps.reverse()
            state_cost = calculate_cost(state,goal_state) + calculate_heuristic(state)
        break
    
        explored.add((tuple(state), state_cost))
        
        successors = generate_successors(state)
        for s in successors:
            cost = state_cost + 1
            if (tuple(s[0]), cost) not in explored:
                frontier.put((cost, s[0]))
                
    return True

initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
goal_state = [12, 1, 2, 15, 11, 6, 5, 8, 7, 10, 9, 4, 0, 13, 14, 3]

solution = ucs(initial_state, goal_state)
if solution is None:
    print("No solution found!")
else:
    dict = {0:"Up",1:"Left",2:"Right",3:"Down"}
    for x in range(solution1):
        a = random.randrange(0,4)
        print(dict[a])
