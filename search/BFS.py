from collections import deque,defaultdict
from queue import PriorityQueue

class unweighted_Graph:
    def __init__(self,directed=False):
        self.graph = defaultdict(list) # adjacency list {ID : adjNode}
        self.directed = directed

    def addEdge(self,frm,to):
        self.graph[frm].append(to)
        if self.directed == False:
            self.graph[to].append(frm)
    
    def getNeighbors(self,node):
        return self.graph[node]
    
    def __str__(self):
        return ''.join(str(node) + ':' + str(self.graph[node]) + "\n" for node in self.graph)

    def BFS(self,start):
        """
        create a queue Q
        mark start as visited
        enqueue start into Q
        while Q is non-empty 
            remove the head u of Q 
            mark and enqueue all (unvisited) neighbours of u
        """
        Q = deque()
        Q.append(start)
        visited = set()
        visited.add(start)
        while Q :
            head = Q.popleft()
            print(head, end = " ")
            for neighbor in self.graph[head] :
                if neighbor not in visited :
                    visited.add(neighbor)
                    Q.append(neighbor)

def main():

    G = unweighted_Graph(directed = True)
    
    G.addEdge(0, 1)
    G.addEdge(0, 2)
    G.addEdge(1, 2)
    G.addEdge(2, 0)
    G.addEdge(2, 3)
    G.addEdge(3, 3)

    print(G)

    G.BFS(2) #2 0 3 1

if __name__ == "__main__":
    main()