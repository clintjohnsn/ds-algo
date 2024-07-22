"""
Leetcode 210
https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses
 If it is impossible to finish all courses, return an empty array.


Topological Sorted Order


"""

"""
in-degree + bfs solution

no indegree = no pre req
when you take a course , reduce indegrees of children
cycle = indegree never becomes zero

"""

from collections import  deque
class Node:

    def __init__(self, val):
        self.val = val
        self.children = []
        self.inbound = 0


class Solution:
    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        courses = [Node(i) for i in range(num_courses)]
        for prerequisite in prerequisites:
            courses[prerequisite[1]].children.append(courses[prerequisite[0]])
            courses[prerequisite[0]].inbound +=1
        q = deque()
        for i in range(len(courses)):
            if courses[i].inbound == 0:
                q.append(courses[i])
        ans = list()
        while q:
            course = q.popleft()
            ans.append(course.val)
            for child in course.children:
                child.inbound -=1
                if child.inbound <= 0:
                    q.append(child)
        if len(ans) != num_courses:
            return []
        return ans



# Test
print(Solution().find_order(2, [[1, 0]])) #  [0,1]
print(Solution().find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])) #  [0,2,1,3] or  [0,1,2,3]
print(Solution().find_order(1, [])) # [0]
print(Solution().find_order(3, [[1, 0], [1, 2], [0, 1]])) #[]

"""
can also use a stack. That however, will give us a different ordering than what we might get from the queue
(since everything in the queue/stack has indegree 0)

Time Complexity: O(V+E) where V represents the number of vertices and E represents the number of edges.
We pop each node exactly once from the zero in-degree queue and that gives us V. 
Also, for each vertex, we iterate over its adjacency list and in totality,
we iterate over all the edges in the graph which gives us E. 

Space Complexity: O(V + E). We use an intermediate queue data structure to keep all the nodes with 0 in-degree.
In the worst case, there won't be any prerequisite relationship and the queue will contain all the vertices initially 
since all of them will have 0 in-degree. That gives us O(V).
Additionally, we also use the adjacency list to represent our graph initially.
The space occupied is defined by the number of edges because for each node as the key,
we have all its adjacent nodes in the form of a list as the value. Hence O(E).
or alternatively, if alteast every vertex is present in the list, O(V+E)
     
So, the overall space complexity is O(V + E)

"""

"""
alternate impl with adjacency list
"""

from collections import defaultdict, deque
class Solution:
    def find_order(self, num_courses, prerequisites):
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1
        zero_indegree_queue = deque([k for k in range(num_courses) if k not in indegree])
        topological_sorted_order = []
        # Until there are nodes in the Q
        while zero_indegree_queue:
            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)
            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1
                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == num_courses else []



# Test
print("---------------------------")
print(Solution().find_order(2, [[1, 0]])) #  [0,1]
print(Solution().find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])) #  [0,2,1,3] or  [0,1,2,3]
print(Solution().find_order(1, [])) # [0]
print(Solution().find_order(3, [[1, 0], [1, 2], [0, 1]])) #[]

"""
Using DFS

something like postorder - process all the child(dependent) nodes before the parent(dependency), 
and put it on a stack 

T = O(V+E)

S = O(V+E)
adjacency = O(E)
recursion stack = O(E)
visited = O(V)
"""




class Solution:
    def dfs(self,i:int, adj: defaultdict[list], stack: list[int], visited: list[int]):
        visited[i] = 1
        # visited three colours to detect cycles
        for child in adj[i]:
            if visited[child] == 0:
                self.dfs(child, adj, stack,visited)
            if visited[child] == 1:
                # cycle
                return
        visited[i] = 2
        stack.append(i)

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
        stack = list()
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                self.dfs(i, adj,stack, visited)
        return list(reversed(stack)) if len(stack) == numCourses else []

print("---------------------------")
print(Solution().findOrder(2, [[1, 0]])) #  [0,1]
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])) #  [0,2,1,3] or  [0,1,2,3]
print(Solution().findOrder(1, [])) # [0]
print(Solution().findOrder(3, [[1, 0], [1, 2], [0, 1]])) #[]
