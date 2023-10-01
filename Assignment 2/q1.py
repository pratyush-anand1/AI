import numpy as np
import time

m1=np.random.randint(0,10,size=(10,10))
m2=np.random.randint(1,11,size=(10,10))
m2=np.transpose(m2)
m3=np.random.randint(0,1,size=(10,10))
start=time.perf_counter()
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            m3[i][j]+=m1[i][k]*m2[k][j]
end=time.perf_counter()
t1=end-start
print(m3)


start1=time.perf_counter()
m3=np.dot(m1,m2)
end1=time.perf_counter()
t2=end1-start1
print("\n",m3)
print("Speed up",t1/t2)