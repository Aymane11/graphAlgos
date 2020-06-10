from sys import maxsize
from collections import deque,defaultdict
inf = int(maxsize)

class Edge:
    def __init__(self,frm,to,cost=1):
        self.frm = frm
        self.to = to
        self.cost = cost

    def __str__(self):
        return str(tuple([self.frm,self.to,self.cost]))

class Graph:
    def __init__(self,directed=False):
        self.graph = defaultdict(dict) # adjacency list { ID : { adjNode : dist(ID,adjNode) } }
        self.directed = directed
    
    def addEdge(self,frm,to,cost=1):
        self.graph[frm][to] = cost
        if self.directed == False:
            self.graph[to][frm] = cost
    
    def getEdges(self):
        E = []
        for node in self.graph:
            for adj in self.graph[node]:
                cost = self.graph[node][adj]
                E.append(Edge(node,adj,cost))
        return E

    def distance(self,frm,to):
        if frm == to :
            return 0
        if to not in self.graph[frm]:
            return inf
        return self.graph[frm][to]
    
    def __str__(self):
        return ''.join(str(node) + ':' + str(self.graph[node]) + "\n" for node in self.graph)

    def BellmanFord(self,start):
        distance , parent = [inf] * len(self.graph) , [-1] * len(self.graph)
        distance[start] = 0
        for _ in range(len(self.graph)-1):
            for edge in self.getEdges():
                if  distance[edge.to] > distance[edge.frm] + edge.cost :
                    distance[edge.to] = distance[edge.frm] + edge.cost
                    parent[edge.to] = edge.frm
        for edge in self.getEdges():
            if  distance[edge.to] > distance[edge.frm] + edge.cost :
                print("Graph contains a negative-weight cycle")
                return -1
        printSolution(distance,parent)
        return

def printSolution(dist, parent):
    src = 0
    print("From-->To \t\tDistance from Source \t Path",end="")
    for i in range(1, len(dist)):
        print(''.join(f"\n {src} --> {i} \t\t{dist[i]} \t\t\t" if dist[i]!=inf else f"\n {src} --> {i} \t\tInf \t\t\t") , end=" ")
        if dist[i] != inf:
            printPath(parent,i)
        else:
            print("No path",end="")

def printPath(parent, j):
    if parent[j] == -1 : 
        print (j,end=" ")
        return
    printPath(parent , parent[j])
    print (j,end=" ")

def printArr(dist, n):
    print ("Vertex\tDistance from source")
    for i in range(n):
        print (f"{i}\t\t{dist[i]}")

def main():
    G1 = Graph(directed = False)
    G1.addEdge(0, 1, 4)
    G1.addEdge(0, 7, 8)
    G1.addEdge(1, 2, 8)
    G1.addEdge(1, 7, 11)
    G1.addEdge(2, 3, 7)
    G1.addEdge(2, 8, 2)
    G1.addEdge(2, 5, 4)
    G1.addEdge(3, 4, 9)
    G1.addEdge(3, 5, 14)
    G1.addEdge(4, 5, 10)
    G1.addEdge(5, 6, 2)
    G1.addEdge(6, 7, 1)
    G1.addEdge(6, 8, 6)
    G1.addEdge(7, 8, 7)

    print(G1)


    G1.BellmanFord(0)


if __name__ == "__main__":
    main()