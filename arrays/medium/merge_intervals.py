"""
Leetcode 56
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi],
 merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[10,11],[15,18]]
Output: [[1,6],[8,11],[15,18]]

1 <= intervals <= 10^4
0 <= starti <= endi <= 10^4

"""

"""
method: coloring 

Space = O(Range) = O(N), given constraints
time = O(n*range) = O(N^2) in the worst case
if average interval size is < log n,
 time < O(nlogn)

"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # get rid of repeated intervals
        intervals = list(set([(interval[0],interval[1]) for interval in intervals]))
        # init space
        space = [False] * (10000 + 1)
        # color the space
        for interval in intervals:
            for i in range(interval[0],interval[1]):
                space[i] = True
        output = list()
        # make new intervals
        i,j = 0,0
        while i < len(space):
            if space[i] == True:
                j = i
                while space[j] == True and j < len(space):
                    j+=1
                output.append([i,j])
                i = j
            else:
                i+=1
        # edge cases of [x,x] intervals
        for i in range(len(intervals)):
            if intervals[i][0] == intervals[i][1] and not space[intervals[i][0]] and not space[intervals[i][0]-1]:
                output.append(intervals[i])
        return  output

# tests
print(Solution().merge([[1,3],[2,6],[8,10],[10,11],[15,18]])) # [[1,6],[8,11],[15,18]]
print(Solution().merge([[1,4],[5,6]]))  # [[1,4],[5,6]]
print(Solution().merge([[2,4],[1,1]])) # [[2,4],[1,1]]
print(Solution().merge([[2,3],[5,5],[2,2],[3,4]])) # [[2,4],[5,5]]
print(Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])) # [[1,3],[4,7]]

"""
method: sorting
S = O(1)
T = O(nlogn + n) = O(nlogn)
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # get rid of repeated intervals
        intervals = list(set([(interval[0], interval[1]) for interval in intervals]))
        intervals.sort()
        output = list()
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [intervals[i][0],max(intervals[i+1][1], intervals[i][1])]
                intervals[i] = None
        return [interval for interval in intervals if interval is not None]


# tests
print("---------------------------------")
print(Solution().merge([[1,3],[2,6],[8,10],[10,11],[15,18]])) # [[1,6],[8,11],[15,18]]
print(Solution().merge([[1,4],[5,6]]))  # [[1,4],[5,6]]
print(Solution().merge([[2,4],[1,1]])) # [[2,4],[1,1]]
print(Solution().merge([[2,3],[5,5],[2,2],[3,4]])) # [[2,4],[5,5]]
print(Solution().merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])) # [[1,3],[4,7]]
print(Solution().merge([[1,4],[2,3]])) # [[1,3],[4,7]]

"""
Leetcode 435 
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

"""


class Solution:
    def erase_overlap_intervals(self, intervals:list[list[int]]) -> int:
        intervals.sort()
        count = 0
        for i in range(len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                count += 1
                # take the interval that ends earlier, reduce the no of possible overlaps
                # not the thinner interval
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i + 1] = intervals[i]
        return count


# Tests
print("---------------------------------")
print(Solution().erase_overlap_intervals( [[1,2],[2,3],[3,4],[1,3]])) # 1
print(Solution().erase_overlap_intervals( [[1,2],[1,2],[1,2]])) # 2
print(Solution().erase_overlap_intervals( [[1,2],[2,3]])) # 0
print(Solution().erase_overlap_intervals( [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])) # 7


