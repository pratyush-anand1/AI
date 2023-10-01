from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self,s,goalState):
        l = []
        visited = [False] * (max(self.graph)+1)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s=queue.pop(0)
            l.append(s)
            print(s)

            if s==goalState:
                break

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print("Here")
        return l

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
l = g.BFS(0,9)
pos = {"0":"right","1":"left"}
for y in l:
        j = dict[y]
        for x in j:
            print(j)
            l=0
            print("{ Man:",pos[j[l]],",Cabbage:",pos[(j[l+1])],",Goat:",pos[j[l+2]],",Wolf:",pos[j[l+3]],"}") 
            print(" ")
            break