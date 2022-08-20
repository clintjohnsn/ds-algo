"""
Breadth-First Traversal (or Search) for a graph is similar to Breadth-First Traversal of a tree
The only catch here is, that, unlike trees, graphs may contain cycles, so we may come to the same node again
 To avoid processing a node more than once, we use a boolean visited array. 
For simplicity, it is assumed that all vertices are reachable from the starting vertex.
 BFS uses a queue data structure for traversal.

one edge case is disconnected graph

"""
from collections import defaultdict, deque
# using adjacency list representation
class Graph:
 
    def __init__(self):
      # adjacency list
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.popleft()
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def BFS_Disconnected(self,s):
        visited = [False] * (max(self.graph) + 1)
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.popleft()
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        for s in self.graph.keys():
          if visited[s] == False:
            queue.append(s)
            visited[s] = True
            while queue:
                s = queue.popleft()
                print (s, end = " ")
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
  
# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)
print()
g.BFS_Disconnected(2)