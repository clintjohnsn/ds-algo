"""
Leetcode 815
https://leetcode.com/problems/bus-routes/

Bus Routes

You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7],
this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially),
 and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target.
 Return -1 if it is not possible.

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1

"""

"""
bfs - shortest path unweighted

taking stops as nodes

memory limit exceeded
"""
from collections import  defaultdict

class Solution:
    def num_buses(self, routes: list[list[int]], source: int, target: int) -> int:
        hm = defaultdict(set)
        visited = set()
        for route in routes:
            for i in route:
                hm[i].update(set(route).difference({i}))
        q = [source]
        count = -1
        while q:
            count +=1
            next = list()
            for i in q:
                if i not in visited:
                    visited.add(i)
                    if i == target:
                        return count
                    next.extend([j for j in hm[i] if j not in visited])
            q = next
        return -1

# Test
print(Solution().num_buses([[1, 2, 7], [3, 6, 7]], 1, 6)) # 2
print(Solution().num_buses([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12)) # -1


"""
again , using bfs - shortest path unweighted

taking buses as nodes

min number of buses -> shortest path
can switch buses if common stop exists -> edges

"""

from collections import  defaultdict

class Solution:
    def bfs(self,bus:int,target:int,graph: defaultdict[list], routes: list[list[int]]):
        visited = set()
        count = 0
        q = [bus]
        while q:
            count +=1
            next = list()
            for i in q:
                if i not in visited:
                    visited.add(i)
                    if target in routes[i]:
                        return count
                    else:
                        next.extend(graph[i])
            q = next
        return float("inf")



    def num_buses(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(list)
        for i in range(len(routes)-1):
            for j in range(i+1,len(routes)):
                if set(routes[i]).intersection(set(routes[j])):
                    graph[i].append(j)
                    graph[j].append(i)
        count = float("inf")
        for i in range(len(routes)):
            if source in routes[i]:
                count = min(count,self.bfs(i,target, graph,routes))
        return -1 if count == float("inf") else count

# Test
print("--------------------------")
print(Solution().num_buses([[1, 2, 7], [3, 6, 7]], 1, 6)) # 2
print(Solution().num_buses([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12)) # -1