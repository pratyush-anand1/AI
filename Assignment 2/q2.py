import numpy as np

point1 = np.array([1,2,4])
point2 = np.array([3,2,6])

#Euclidain distance
dist = np.linalg.norm(point1 - point2)
print(dist)

#s = np.sum(np.square(p1-p2))
#dist = np.sqrt(s)

#Product Relation Coefficent
pcc = np.corrcoef(point1,point2)
print(pcc)