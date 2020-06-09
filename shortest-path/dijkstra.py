from collections import deque,defaultdict
from queue import PriorityQueue
from sys import maxsize

inf = int(maxsize)

class weighted_Graph:
    def __init__(self,directed=False):
        self.graph = defaultdict(dict) # adjacency list { ID : { adjNode : dist(ID,adjNode) } }
        self.directed = directed

    def addEdge(self,frm,to,cost=1):
        self.graph[frm][to] = cost
        if self.directed == False:
            self.graph[to][frm] = cost
    
    def getNeighbors(self,node):
        return self.graph[node].keys()
    
    def distance(self,frm,to):
        if frm == to :
            return 0
        if to not in self.graph[frm]:
            return inf
        return self.graph[frm][to]
    
    def __str__(self):
        return ''.join(str(node) + ':' + str(self.graph[node]) + "\n" for node in self.graph)

    def addToPQ(self,frm,to,PQ):
        PQ.put((self.distance(frm,to),to))
    
    def dijkstra(self,start):
        """
        Dijkstra(graph,source):
            Initialize distances of all vertices as infinite.
            Create an empty priority queue pq. Every item of pq is a pair (weight, vertex).
            Insert source vertex into pq and make its distance as 0.
            While either pq doesn't become empty
                Extract minimum distance vertex from pq, name it u
                For every vertex v adjacent of u do
                    If dist[v] > dist[u] + weight(u, v)
                        dist[v] = dist[u] + weight(u, v)
                        Insert v into the pq (Even if v is already there)
                        parent of v is u
            Print distance array dist[] to print all shortest paths.
        """        
        dist = [inf] * len(self.graph)
        parent = [-1] * len(self.graph)
        pq = PriorityQueue()
        self.addToPQ(start,start,pq)
        dist[start] = 0
        while pq.empty() == False:
            head = pq.get()[1]
            for neighbor in self.getNeighbors(head):
                if dist[neighbor] > dist[head] + self.distance(head, neighbor):
                    dist[neighbor] = dist[head] + self.distance(head, neighbor)
                    self.addToPQ(head,neighbor,pq)
                    parent[neighbor] = head
        printSolution(dist,parent) 
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
    G1 = weighted_Graph(directed = False)

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

    G1.dijkstra(0)
    

    G2 = weighted_Graph(directed = True)
    G2.addEdge(0,1,1)
    G2.addEdge(0,2,7)
    G2.addEdge(1,3,9)
    G2.addEdge(1,5,15)
    G2.addEdge(2,4,4)
    G2.addEdge(3,4,10)
    G2.addEdge(3,5,5)
    G2.addEdge(4,5,3)
    G2.addEdge(5,5,1) #node with no neighbors


    print(G2)

    G2.dijkstra(0)



if __name__ == "__main__":
    main()