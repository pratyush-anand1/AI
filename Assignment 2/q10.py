import math

def dist_(v1,v2,v3,p):
  a=((pow((abs(v1[0]-v1[1])),p))+ (pow((abs(v2[0]-v2[1])),p))+ (pow((abs(v3[0]-v3[1])),p)) ) 
  return pow(a,(1/p)) 
  
l=[[1,2], [2,3], [1,5]]

m1=dist_(l[0],l[1],l[2],1) 
m2=dist_(l[0],l[1],l[2],2) 
m3=dist_(l[0],l[1],l[2],3) 
m4=dist_(l[0],l[1],l[2],4) 
print(m1) 
print(m2) 
print(m3) 
print(m4)

print("\n")

def minkowski(p1,p2,p3,p):
     s1=pow((abs(p1[0]-p1[1])),p)
     s2=pow((abs(p2[0]-p2[1])),p)
     s3=pow((abs(p3[0]-p3[1])),p)
     s=pow((s1+s2+s3),(1/p)) 
     print("%.3f"%s) 
p1=[1,2] 
p2=[2,3] 
p3=[1,5] 
#minkowski(p1,p2,p3,1) 
#minkowski(p1,p2,p3,2) 
#minkowski(p1,p2,p3,3) 
#minkowski(p1,p2,p3,4)