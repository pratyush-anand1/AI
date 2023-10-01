#Graph colouring using Genetic Algorithm

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

# Define the size of the population and the number of generations
POPULATION_SIZE = 10
NUM_GENERATIONS = 100

# Define the fitness function
def fitness(solution):
    conflicts = 0
    for node in graph:
        color = solution[node]
        for neighbor in graph[node]:
            if solution[neighbor] == color:
                conflicts += 1
    return conflicts

# Define the crossover function
def crossover(parent1, parent2):
    child = {}
    for node in graph:
        if random.random() < 0.5:
            child[node] = parent1[node]
        else:
            child[node] = parent2[node]
    return child

# Define the mutation function
def mutate(solution):
    node = random.choice(list(graph.keys()))
    solution[node] = random.choice(colors)
    return solution

# Initialize the population
population = []
for i in range(POPULATION_SIZE):
    solution = {}
    for node in graph:
        solution[node] = random.choice(colors)
    population.append(solution)

# Evolve the population
for generation in range(NUM_GENERATIONS):
    # Evaluate the fitness of each solution
    fitness_scores = []
    for solution in population:
        fitness_scores.append((solution, fitness(solution)))
    fitness_scores.sort(key=lambda x: x[1])

    # Select the parents for the next generation
    parents = [solution for solution, fitness in fitness_scores[:int(POPULATION_SIZE/2)]]

    # Generate the offspring for the next generation
    offspring = []
    while len(offspring) < POPULATION_SIZE - len(parents):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = crossover(parent1, parent2)
        if random.random() < 0.1:
            child = mutate(child)
        offspring.append(child)

    # Add the parents to the next generation
    population = parents + offspring

# Print the best solution found
best_solution, best_fitness = min(fitness_scores, key=lambda x: x[1])
print('Best solution found:')
print(best_solution)
print('Fitness:', best_fitness)
