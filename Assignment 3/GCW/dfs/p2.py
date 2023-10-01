dict = {0:"1111",1:"0101",2:"1011",3:"1101",4:"1100",5:"0010",6:"0001",7:"0100",8:"1010",9:"0000"}
pos = {"0":"right","1":"left"}

v = [[] for i in range(100)]
def addEdge(x, y):
    v[x].append(y)
    v[y].append(x)

def printPath(stack):
    for i in range(len(stack) - 1):
        j = dict[stack[i]]
        for x in j:
            l=0
            print("{ Man:",pos[j[l]],",Cabbage:",pos[(j[l+1])],",Goat:",pos[j[l+2]],",Wolf:",pos[j[l+3]],"}") 
            print(" ")
            break
    j = dict[stack[-1]]
    l=0
    print("{ Man:",pos[j[l]],",Cabbage:",pos[(j[l+1])],",Goat:",pos[j[l+2]],",Wolf:",pos[j[l+3]],"}")
        
def DFS(vis, x, y, stack):
    stack.append(x)
    if (x == y):
        printPath(stack)
        return 
    vis[x] = True

    if (len(v[x]) > 0):
        for j in v[x]:
        
            if (vis[j] == False):
                DFS(vis, j, y, stack)
                
    del stack[-1]

def DFSCall(x, y, n, stack):	
    
    vis = [0 for i in range(n + 1)]
    DFS(vis, x, y, stack)
   

n = 10

addEdge(0,1)
addEdge(1,3)
addEdge(2,5)
addEdge(2,6)
addEdge(3,6)
addEdge(3,7)
addEdge(4,7)
addEdge(4,5)
addEdge(5,8)
addEdge(8,9)
stack = []
DFSCall(0, 9, n, stack)