"""
Given a directed graph, check whether the graph contains a cycle or not

1. Using DFS
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
DFS for a connected graph produces a tree. 
There is a cycle in a graph only if there is a back edge present in the graph.
 A back edge is an edge that is from a node to itself (self-loop) or one of its ancestors in the tree produced by DFS.
 For a disconnected graph, Get the DFS forest as output. To detect cycle, check for a cycle in individual trees by checking back edges.

 To detect a back edge, keep track of vertices currently in the recursion stack of function for DFS traversal. 
 If a vertex is reached that is already in the recursion stack, then there is a cycle in the tree. 
 The edge that connects the current vertex to the vertex in the recursion stack is a back edge.

Time Complexity: O(V+E). 
Time Complexity of this method is same as time complexity of DFS traversal which is O(V+E).
Space Complexity: O(V). 
To store the visited and recursion stack O(V) space is needed.

"""

"""
2. Coloring
https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/ 
Perform, DFS, assign one of three colors

WHITE : Vertex is not processed yet. Initially, all vertices are WHITE.
GRAY: Vertex is being processed (DFS for this vertex has started, but not finished
   which means that all descendants (in DFS tree) of this vertex are not processed yet 
   (or this vertex is in the function call stack)
BLACK : Vertex and all its descendants are processed. 

While doing DFS, if an edge is encountered from current vertex to a GRAY vertex, then this edge is back edge and hence there is a cycle.
Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity :O(V). 
Since an extra color array is needed of size V.
"""

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(deque)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
      self.graph[u].append(v)
    
    # helper for detect cycle with colors
    def dcc_helper(self,v,colors):
      status = False
      colors[v] = 1
      for neighbour in self.graph[v]:
        if colors[neighbour] == 1:
          return True
        elif colors[neighbour] == 0:
          status = self.dcc_helper(neighbour,colors)
      colors[v] = 2
      return status

    # method 2 detech with colors
    def detect_cycle_colors(self):
      colors = [0] * (len(self.graph.items()) + 1)
      for v in self.graph:
        if colors[v] == 0:
          if self.dcc_helper(v,colors):
            return True
      return False

    # helper for method 1
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
        recStack[v] = False
        return False
  
    # method1
    def isCyclic(self):
        visited = [False] * (len(self.graph) + 1)
        recStack = [False] * (len(self.graph) + 1)
        for node in range(len(self.graph)):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False


#driver
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.detect_cycle_colors())
print(g.isCyclic())