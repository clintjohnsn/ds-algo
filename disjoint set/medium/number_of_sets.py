"""

Leetcode 547

https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""
class DisjointSet:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, i:int, j:int):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi < pj:
            self.parent[pi] = pj
        else:
            self.parent[pj] = pi

    def find_parent(self, i:int):
        if self.parent[i] != i:
            self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]


class Solution:
    def find_circle_num(self, is_connected: list[list[int]]) -> int:
        djs = DisjointSet(len(is_connected))
        for i in range(len(is_connected)):
            for j in range(len(is_connected[i])):
                if is_connected[i][j] and i!=j and i < j:
                    djs.union(i,j)
        for i in range(len(is_connected)):
            djs.find_parent(i)
        return len(set(djs.parent))

# Test
print(Solution().find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(Solution().find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]])) # 3
print(Solution().find_circle_num([[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])) # 3
