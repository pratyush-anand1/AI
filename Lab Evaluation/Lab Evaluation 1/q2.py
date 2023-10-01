import numpy as np
import random
import time

m1 = int(input("Enter value of m1:"))
n1 = int(input("Enter value of n1:"))
r1 = int(input("Enter value of r1:"))


m2 = int(input("Enter value of m2:"))
n2 = int(input("Enter value of n2:"))
r2 = int(input("Enter value of r2:"))


t1 = np.random.normal(0,1,(m1,n1,r1))
print("Tensor t1:")
print(t1)
t2 = np.random.uniform(0,1,(m2,n2,r2))
print("Tensor t2:")
print(t2)

c1 = int(input("Enter value of c1:"))
c2 = int(input("Enter value of c2:"))
c3 = int(input("Enter value of c3:"))

s1 = time.perf_counter()
res = c1*t1 + c2*t2 + c3
e1 = time.perf_counter()

print("Resulting tensor:")
print(res)
print("Time taken to perform operation:",e1-s1,"seconds")
