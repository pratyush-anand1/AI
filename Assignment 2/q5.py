import numpy as np
from scipy.spatial.distance import cityblock

x1 = np.array([1,2,3,4,5,6])
x2 = np.array([10,20,30,1,2,3])
print(cityblock(x1, x2))

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=3
n=3
k = 0; l = 0
print("Spiral order")
while (k < m and l < n):
     for i in range(l, n):
         print(arr[k][i])
     k += 1
     for i in range(k, m):    
         print(arr[i][n - 1])
     n -= 1
     if ( k < m):
         for i in range(n - 1, (l - 1), -1):
             print(arr[m - 1][i])  
         m -= 1
     if (l < n):
         for i in range(m - 1, k - 1, -1):
             print(arr[i][l])
         l += 1