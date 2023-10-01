import numpy as np
#Angle between two vectors 
point1 = np.array([2,1,2])
point2 = np.array([1,1,1])
cosangle = point1.dot(point2)/(np.linalg.norm(point1) * np.linalg.norm(point2))
print(np.arccos(cosangle))
#print(math.degrees(np.arccos(cosangle)))