def sum(a,b,c,d,e):
    return a+b+c+d+e

def sumlist(l):
    s = 0
    for k in l:
        s = s + k
    return s

a = 10
b = 12
c = 10
d = 8
e = 14 
print(sum(a,b,c,d,e))

l=[10,12,10,8,14]
print(sumlist(l))