def isAnagram(a,b):
    dicta = {}
    dictb = {}
    for x in a:
        if x in dicta.keys():
            dicta[x] = dicta[x] + 1
        else:
           dicta[x] = 1
    for y in b:
        if y in dictb.keys():
            dictb[y] = dictb[y] + 1
        else:
            dictb[y] = 1
    if dicta == dictb:
        return True
    else:
        return False

a = input("Enter string 1:")
b = input("Enter string 2:")
if(isAnagram(a,b)):
    print("The strings are anagram")
else:
    print("The strings are not anagram")