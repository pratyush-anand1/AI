def newList(l):
    nList = []
    for x in l:
        if x not in nList:
            nList.append(x)
    return nList

l = [1,2,3,5,6,7,1,3,5,6,7,8]
nList = newList(l)
print(nList)