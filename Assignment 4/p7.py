#Graph colouring using hill climbing

import random

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

# Define the possible colors
colors = ['red', 'green', 'blue', 'yellow']

# Define the size of the population and the number of iterations
NUM_ITERATIONS = 100

# Define the fitness function
def fitness(solution):
    conflicts = 0
    for node in graph:
        color = solution[node]
        for neighbor in graph[node]:
            if solution[neighbor] == color:
                conflicts += 1
    return conflicts

# Initialize the solution randomly
solution = {}
for node in graph:
    solution[node] = random.choice(colors)

# Optimize the solution using hill climbing
for i in range(NUM_ITERATIONS):
    # Evaluate the fitness of the current solution
    current_fitness = fitness(solution)

    # Generate a neighbor solution by randomly changing the color of a single node
    neighbor = solution.copy()
    node = random.choice(list(graph.keys()))
    neighbor[node] = random.choice(colors)

    # Evaluate the fitness of the neighbor solution
    neighbor_fitness = fitness(neighbor)

    # If the neighbor solution is better, accept it as the new current solution
    if neighbor_fitness < current_fitness:
        solution = neighbor
        current_fitness = neighbor_fitness

# Print the best solution found
print('Best solution found:')
print(solution)
print('Fitness:', fitness(solution))
