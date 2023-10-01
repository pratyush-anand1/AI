from z3 import *

# Define the Sudoku grid
grid = [[Int("cell_%s_%s" % (i, j)) for j in range(9)] for i in range(9)]

# Define the solver
solver = Solver()

# Define the constraints for the rows, columns, and squares
for i in range(9):
    for j in range(9):
        # Each cell must contain a value between 1 and 9
        solver.add(And(grid[i][j] >= 1, grid[i][j] <= 9))
        
        # Each row must contain unique values
        solver.add(Distinct(grid[i]))
        
        # Each column must contain unique values
        solver.add(Distinct([grid[k][j] for k in range(9)]))
        
        # Each square must contain unique values
        row_offset, col_offset = 3 * (i // 3), 3 * (j // 3)
        solver.add(Distinct([grid[row_offset + k][col_offset + l] for k in range(3) for l in range(3)]))

# Define the initial values
initial_values = [
    (0, 0, 5), (0, 1, 3), (0, 4, 7),
    (1, 0, 6), (1, 3, 1), (1, 4, 9), 
    (2, 1, 9), (2, 2, 8), (2, 7, 6),
    (3, 0, 8), (3, 4, 6), (3, 8, 3),
    (4, 0, 4), (4, 3, 8), (4, 5, 3), 
    (5, 0, 7), (5, 4, 2), (5, 8, 6),
    (6, 1, 6), (6, 6, 2), (6, 7, 8),
    (7, 3, 4), (7, 4, 1), (7, 5, 9), 
    (8, 4, 8), (8, 7, 7), (8, 8, 9)
]

# Add the initial values to the solver
for i, j, val in initial_values:
    solver.add(grid[i][j] == val)

# Solve the puzzle
if solver.check() == sat:
    model = solver.model()
    solution = [[model.evaluate(grid[i][j]).as_long() for j in range(9)] for i in range(9)]
    for row in solution:
        print(row)
else:
    print("No solution found.")