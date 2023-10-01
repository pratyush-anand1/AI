from pulp import *
from z3 import *

x1=bool("x1")
x2=bool("x2")
x3=bool("x3")
x4=bool("x4")
x5=bool("x5")
x6=bool("x6")


f1=Or([Not(x1),Not(x2),x3])
f2=Or([x2,Not(x3),Not(x4)])
f3=Or([Not(x2),x3,Not(x4)])
f4=Or([x3,Not(x4),x5])
f5=Or([x1,x5,Not(x6)])


prob = LpProblem("3-SAT", LpMaximize)


x1_lp = LpVariable("x1", cat=LpBinary)
x2_lp = LpVariable("x2", cat=LpBinary)
x3_lp = LpVariable("x3", cat=LpBinary)
x4_lp = LpVariable("x4", cat=LpBinary)
x5_lp = LpVariable("x5", cat=LpBinary)
x6_lp = LpVariable("x6", cat=LpBinary)
f1_lp = LpVariable("f1", cat=LpBinary)
f2_lp = LpVariable("f2", cat=LpBinary)
f3_lp = LpVariable("f3", cat=LpBinary)
f4_lp = LpVariable("f4", cat=LpBinary)
f5_lp = LpVariable("f5", cat=LpBinary)


prob += f1_lp + f2_lp + f3_lp + f4_lp + f5_lp


prob += -x1_lp + f1_lp + f5_lp >= 0
prob += -x2_lp + f1_lp + f2_lp + f3_lp >= 0
prob += x1_lp + x2_lp - x3_lp + f2_lp + f3_lp >= 1
prob += x2_lp + x3_lp - x4_lp + f2_lp + f3_lp + f4_lp >= 1
prob += -x3_lp + x5_lp + f4_lp >= 0
prob += -x5_lp + x6_lp + f5_lp >= 0


status = prob.solve()

if status != LpStatusOptimal:
    print("No solution found.")
else:
    x1_val = int(value(x1_lp))
    x2_val = int(value(x2_lp))
    x3_val = int(value(x3_lp))
    x4_val = int(value(x4_lp))
    x5_val = int(value(x5_lp))
    x6_val = int(value(x6_lp))
    f1_val = int(value(f1_lp))
    f2_val = int(value(f2_lp))
    f3_val = int(value(f3_lp))
    f4_val = int(value(f4_lp))
    f5_val = int(value(f5_lp))
    

    x1_bool = bool(x1_val)
    x2_bool = bool(x2_val)