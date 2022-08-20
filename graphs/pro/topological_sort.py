"""
https://www.geeksforgeeks.org/topological-sorting/

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that 
for every directed edge u v, vertex u comes before v in the ordering. 
Topological Sorting for a graph is not possible if the graph is not a DAG.

eg for the DAG

5 -> 2 -> 3 -> 1
4 -> 1
5 -> 0
4 -> 0

o/p 5 4 2 3 1 0 or 4 5 2 3 1 0 or...

There can be more than one topological sorting for a graph
The first vertex in topological sorting is always a vertex with in-degree as 0

Applications: 
Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs.
instruction scheduling, ordering of formula cell evaluation when recomputing formula values in spreadsheets,
 logic synthesis, determining the order of compilation tasks to perform in make files,
  data serialization, and resolving symbol dependencies in linkers


Method 1
Like dfs, but call all adjacent nodes (neighbours) first and put them in a stack, then put the vertice itself in stack
vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on) are already in the stack. 

Time Complexity: O(V+E). 
The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS
Auxiliary space: O(V). 
The extra space is needed for the stack.

# Method 2
Kahn's algorithm
https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
A DAG G has at least one vertex with in-degree 0 and one vertex with out-degree 0. 
Kahn's algo is basically bfs, with indegrees
first process indegree 0s
Then after execution of all those 0 indegree, we will execute v's which are directly dependent on currently resolved v 
(currently resolved v's direct dependent's  indegree will reduce by 1, if no other dependency, then ready to be processed) 

Time Complexity: O(V+E). 
Auxiliary Space: O(V).

# TODO: all topological sorts of a DAG
https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/

"""
# Method 1
# adjacency list representation
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(deque)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        # self.graph.update({u:self.graph.get(u,[]) +[v]})
 
    def topological_sort_util(self, v, visited,stack):
        visited.add(v)
        for neighbour in self.graph.get(v,[]):
            if neighbour not in visited:
                self.topological_sort_util(neighbour, visited,stack)
        stack.append(v)
 
    def topological_sort(self):
        visited = set()
        stack = deque()
        for vertex in self.graph:
            if vertex not in visited:
                self.topological_sort_util(vertex, visited,stack)
        stack.reverse()
        print(stack)

    def kahns_topological_sort(self):
        count = 0
        sorted = []
        # calculate indegree for all vertices
        indegree = [0] * len(self.graph)
        for v in self.graph:
            for e in self.graph[v]:
                indegree[e] +=1
        # put indegree 0 vertices in q
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        # process q, breaking indegrees
        while q:
            v = q.popleft()
            sorted.append(v)
            for neighbour in self.graph[v]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
            count +=1
        if count != len(self.graph):
            # if not processed, it means indegree of v never became 0
            # which implies cycle
            print("cycle detected!")
        else:
            print(sorted)
        
        

# Driver code
g = Graph()
g.addEdge(5, 0)
g.addEdge(5, 2)
g.addEdge(4, 1)
g.addEdge(4, 0)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.graph[0]
g.graph[1]
# needed if default dict is used
# trying to fetch a vertex without outgoing edges will add an empty adjacency list to the graph
g.topological_sort()
g.kahns_topological_sort()
