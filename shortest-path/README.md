# Shortest Path Algorithms 
>Finding the shortest path from a source node to another (or all) node in the graph

## Uses :
- Maps
- Networks
- Games

## Dijkstra
<img src="https://i.imgur.com/ZcfGmdz.gif" width="250" title="Dijkstra">

#### Pseudocode
###### Using priority queue
```C
Dijkstra(graph,source):
    distance[], parent[]
    Initialize distances of all vertices as infinite.
    Initialize parents of all vertices as -1.
    Create an empty priority queue pq. Every item of pq is a pair (weight,vertex).
    Insert source vertex into pq and set distance[source] = 0.
    While pq is not empty
        Extract minimum distance vertex from pq (which is the top element), name it u
        For every vertex v adjacent of u do
            If dist[v] > dist[u] + weight(u, v) then
                dist[v] = dist[u] + weight(u, v)
                Insert the pair (distance(u , v) , v) into the pq (Even if it's already there)
                Set parent[v] to u
    return distance[], parent[]
```

## Bellman-Ford

<img src="https://github.com/Aymane11/graphAlgos/blob/master/shortest-path/BF.gif?raw=true" width="250" title="Bellman-Ford">


#### Pseudocode
```C
BellmanFord(graph,source):
    distance[], parent[]
    Initialize distances of all vertices as infinite.
    Initialize parents of all vertices as -1.
    distance[source] = 0
    for i from 1 to size(vertices)−1 do (i.e : loop |V|−1 times)
        for every edge (u, v, weight) in edges do
            if distance[v] > distance[u] + weight then
                distance[v] = distance[u] + weight
                parent[v] = u

    (check for negative-weight cycles)
    for every edge (u, v, weight) in edges do
        if distance[v] > distance[u] + weight then
            Error : The graph contains a negative-weight cycle
    return distance[], parent[]
```

#### Credits
Visualizations : [Visualgo's Website](https://visualgo.net/en/sssp)
