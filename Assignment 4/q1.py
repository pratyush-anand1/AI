import numpy as np
import time
a1=np.random.rand(10,10)
print(a1)

arr1 = np.empty([10,10])
arr2= np.empty([10,10])

begin1 = time.time()
for i in range(0,10):
    for j in range(0,10):
        arr1[i][j]  = a1[i][j] + 10
end1= time.time()

begin2= time.time()
arr2 = arr2 + 10
end2 = time.time()

print("Process 1 and 2 respectively take time : ", end1-begin1,end2-begin2)