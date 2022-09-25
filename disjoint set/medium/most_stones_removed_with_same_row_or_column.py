"""
Leetcode 947

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
return the largest possible number of stones that can be removed.


Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

1 1 0
1 0 1 ->
0 1 1

1 x 0
x 0 x
0 x x


Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

1 0 1
0 1 0 ->
1 0 1

1 0 x
0 1 0
x 0 x


Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

"""


"""
if we make disjoint sets based on common row and coloumn, then the ans is
ans = no of stones - no of disjoint sets

"""

"""
dfs solution
similar to count no of islands
"""
class Solution:
    def dfs(self, mat:list[list[int]], i:int, j:int):
        mat[i][j] = 0
        for k in range(len(mat[i])):
            if mat[i][k] == 1:
                self.dfs(mat,i,k)
        for k in range(len(mat)):
            if mat[k][j] == 1:
                self.dfs(mat,k,j)

    def removeStones(self, stones: list[list[int]]) -> int:
        m = max(stones)[0] + 1
        n = max(stones,key=lambda x:x[1])[1] + 1
        mat = [[0] * (n) for _ in range(m)]
        for i,j in stones:
            mat[i][j] = 1
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    self.dfs(mat,i,j)
                    count +=1
        return len(stones) - count


# Test
print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])) # 3
print(Solution().removeStones([[0,0]])) # 0

"""
optimization
dfs, using the given list, O(N) time

"""
from collections import  defaultdict

class Solution:
    def dfs(self, row:defaultdict[list], column:defaultdict[list], stones: set[tuple[int]], i:int, j:int) -> None:
        if (i,j) in stones:
            stones.discard((i,j))
            for k in row[i]:
                self.dfs(row,column,stones,i,k)
            for k in column[j]:
                self.dfs(row,column,stones,k,j)
    def removeStones(self, stones: list[list[int]]) -> int:
        row = defaultdict(list)
        column = defaultdict(list)
        for i,j in stones:
            row[i].append(j)
            column[j].append(i)
        stones_set = set([(i,j) for i,j in stones])
        count = 0
        for i,j in stones:
            if (i,j) in stones_set:
                count +=1
                self.dfs(row,column,stones_set,i,j)
        return len(stones) - count
# Test
print("---------------")
print(Solution().removeStones([[0,1],[1,0]])) # 0
print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])) # 3
print(Solution().removeStones([[0,0]])) # 0


"""
disjoint set based

TODO: fix
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

    def removeStones(self, stones: list[list[int]]) -> int:
        m = max(stones)[0] + 1
        n = max(stones, key=lambda x: x[1])[1] + 1
        size = max(m,n)
        djs = DisjointSet(size)
        for i,j in stones:
            djs.union(i,j)
        for i in range(len(djs.parent)):
            djs.find_parent(i)
        return len(stones) - len(set(djs.parent))

# Test
print("---------------")
print(Solution().removeStones([[0,1],[1,0]])) # 0
print(Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5
print(Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])) # 3
print(Solution().removeStones([[0,0]])) # 0
