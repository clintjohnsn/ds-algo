"""
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. 
The only catch here is, 
unlike trees, graphs may contain cycles (a node may be visited twice).
To avoid processing a node more than once, use a boolean visited array. 

"""
from collections import defaultdict
# adjacency list representation
class Graph:
    def __init__(self):
        # adjacency list
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A function used by DFS
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)
        # for disconnected graph, check if any remain unvisited and print
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)
 
# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
g.DFS(2)

# Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# Space Complexity: O(V), since an extra visited array of size V is required.