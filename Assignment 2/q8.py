import numpy as np

X = np.random.randint(10,size=(10,10))
Y = np.random.randint(10,size=(10,10))
Xin = np.linalg.inv(X)
Xtr = np.transpose(X)
print(Xin*Y)
print(Xtr*X)
print(Xtr*Y)