from numpy.linalg import eig
import numpy as np

a = np.random.randint(10,size=(10,10))
b = np.random.randint(10,size=(10,10))
c = np.transpose(a)
print(c * b)
u1,v1 = eig(a*b)
u2,v2 = eig(b*a)
print("Value:",u1,",Vector:",v1)
print("Value:",u2,",Vector:",v2)