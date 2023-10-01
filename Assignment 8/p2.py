# Import necessary libraries
from pulp import *

# Define the graph as an adjacency matrix
graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

# Define the number of nodes and colors
num_nodes = len(graph)
num_colors = 3

# Create the ILP problem
prob = LpProblem("Graph Coloring Problem", LpMinimize)

# Create the decision variables
vars = LpVariable.dicts("node_color", [(i, j) for i in range(num_nodes) for j in range(num_colors)], 0, 1, LpInteger)

# Add the objective function (not needed for feasibility problems)
prob += 0

# Add the constraints
for i in range(num_nodes):
    prob += lpSum([vars[(i, j)] for j in range(num_colors)]) == 1  # Each node is assigned exactly one color
for i in range(num_nodes):
    for j in range(num_nodes):
        if graph[i][j] == 1:
            for k in range(num_colors):
                prob += vars[(i, k)] + vars[(j, k)] <= 1  # Nodes connected by an edge cannot have the same color

# Solve the ILP problem
prob.solve()

# Print the optimal solution
print("Optimal Solution:")
for i in range(num_nodes):
    for j in range(num_colors):
        if value(vars[(i, j)]) == 1:
            print(f"Node {i} is colored with color {j}")
