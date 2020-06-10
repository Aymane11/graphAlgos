# Search (exploration) Algorithms 
>Visiting every vertex and edge exactly once in a well-defined order

## Uses :
- Maze solving

## BFS (Breadth First Search)
> Can also be used to find shortest path

![Dijkstra](https://github.com/Aymane11/graphAlgos/blob/master/search/BFS.gif)

#### Pseudocode
```C
BFS(graph,start)
    create a queue Q and an array visited
    add start to visited
    enqueue start into Q
    while Q is not empty
        u = Q.dequeue()
        for every adjacent node of u do
                if neighbor not in visited then
                    add neighbor to visited
                    enqueue neighbor into Q
```

#### Credits
Visualizations : [Visualgo's Website](https://visualgo.net/en/sssp)