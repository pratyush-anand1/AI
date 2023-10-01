from pulp import *


prob = LpProblem("Task Assignment", LpMaximize)

agents = ['A', 'B', 'C', 'D']
tasks = [1, 2, 3, 4]
assign = LpVariable.dicts("assign", [(a,t) for a in agents for t in tasks], cat='Binary')

profit_table = {
    ('A',1): 10, ('A',2): 12, ('A',3): 19, ('A',4): 11,
    ('B',1): 5, ('B',2): 10, ('B',3): 7, ('B',4): 8,
    ('C',1): 12, ('C',2): 14, ('C',3): 13, ('C',4): 11,
    ('D',1): 8, ('D',2): 15, ('D',3): 11, ('D',4): 9
}
prob += lpSum([profit_table[(a,t)] * assign[(a,t)] for a in agents for t in tasks])

for t in tasks:
    prob += lpSum([assign[(a,t)] for a in agents]) <= 1

for a in agents:
    prob += lpSum([assign[(a,t)] for t in tasks]) <= 1


prob.solve()

print("Optimal Assignments:")
for a in agents:
    for t in tasks:
        if value(assign[(a,t)]) == 1:
            print("  Assign agent", a, "to task", t)
print("Total Profit:", value(prob.objective))