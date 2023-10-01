from collections import defaultdict 

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def DLS(self,s,t,maxDepth):
        if s == t:
            return True
        
        if maxDepth <= 0:
            return False

        for i in self.graph[s]:
            if(self.DLS(i,t,maxDepth-1)):
                return True
        return False

    def IDDFS(self,s,t,maxDepth):

        for i in range(maxDepth):
            if(self.DLS(s,t,maxDepth)):
                return True
        return False

g = Graph()
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(4,7)
g.addEdge(4,5)
g.addEdge(5,8)
g.addEdge(8,9)
if g.IDDFS(0,9,7) == True: #threshold:6
    print("Reachable")
else:
    print("Not Reachable")