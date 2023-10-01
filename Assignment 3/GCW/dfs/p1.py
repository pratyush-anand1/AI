from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self,i,visited):
        visited[i] = 1
        print(i,end=" ")

        for x in self.graph[i]:
            if visited[x] == 0:
                self.DFSUtil(x,visited)
        

    def DFS(self):
        v = len(self.graph)

        visited = [0]*(v)
        for i in range(v):
            if(visited[i] == 0):
                self.DFSUtil(i,visited)

g = Graph()

dict = {0:"1111",1:"0101",2:"1011",3:"1101",4:"1100",5:"0010",6:"0001",7:"0100",8:"1010",9:"0000"}
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
g.DFS()
secDict = {0:"right",1:"right"}