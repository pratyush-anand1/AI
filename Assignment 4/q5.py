import random

def higheshFrequency(l):
    freq = {}
    for x in l:
        if x in freq.keys():
            freq[x] = freq[x] + 1
        else:
            freq[x] = 1
    a = sorted(freq.values(),reverse=True)[0]
    idx = list(filter(lambda x: freq[x] == a, freq))[0]
    print("Highest occuring elemnt is",idx , ",frequenecy:",a, " times")
    i=0
    print("Occuring at index:")
    for x in l:
        if idx == l[i]:
            print(i)
        i = i + 1
    


l = []
for i in range(0,10):
    l.append(random.randrange(5,10))
print(l)
higheshFrequency(l)