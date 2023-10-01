import random

graph = [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 0],
         [1, 0, 0, 0]]
def get_dominating_set():
    solution = [random.randint(0, 1) for _ in range(len(graph))]
    
    cost = sum(solution)
    
    while True:

        neighbor = list(solution)
        index = random.randint(0, len(graph) - 1)
        neighbor[index] = 1 - neighbor[index]         
        neighbor_cost = sum(neighbor)
    
        if neighbor_cost < cost and is_dominating_set(neighbor):
            solution = neighbor
            cost = neighbor_cost
    
        else:
            return solution
        
def is_dominating_set(solution):
    for i in range(len(graph)):
        if solution[i] == 0:
            if all(graph[i][j] == 0 or solution[j] == 0 for j in range(len(graph))):
                return False
    return True

solution = get_dominating_set()
print(solution)