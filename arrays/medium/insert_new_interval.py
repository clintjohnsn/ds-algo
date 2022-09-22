"""
Leetcode 57
You are given an array of non-overlapping intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                new_start = intervals[i][0]
            if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                new_end = intervals[i][1]
        out = list()
        i = 0
        inserted = False
        while i < len(intervals):
            if not inserted and new_start <= intervals[i][0]:
                while i < len(intervals) and new_end >= intervals[i][1]:
                    i += 1
                out.append([new_start,new_end])
                inserted = True
            if i < len(intervals):
                out.append(intervals[i])
                i += 1
        if not inserted:
            out.append([new_start,new_end])
        return out


print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])) #  [[1,2],[3,10],[12,16]]
print(Solution().insert( [[1,3],[6,9]],[2,5])) # [[1,5],[6,9]]
print(Solution().insert( [],[2,5])) # [[2,5]]
print(Solution().insert( [[1,5]],[2,3])) # [[1,5]]
print(Solution().insert( [[1,5]],[6,8])) # [[1,5],[6,8]]
print(Solution().insert( [[6,8]],[1,5])) # [[1,5],[6,8]]
print(Solution().insert( [[2,5],[6,7],[8,9]],[0,1])) # [[0,1],[2,5],[6,7],[8,9]]


"""
cleaner solution

"""

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = list(), list()
        for interval in intervals:
            if interval[1] < s:
                left += interval,
            elif interval[0] > e:
                right += interval,
            else:
                s = min(s, interval[0])
                e = max(e, interval[1])
        return left + [[s, e]] + right


print("-------------------")
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])) #  [[1,2],[3,10],[12,16]]
print(Solution().insert( [[1,3],[6,9]],[2,5])) # [[1,5],[6,9]]
print(Solution().insert( [],[2,5])) # [[2,5]]
print(Solution().insert( [[1,5]],[2,3])) # [[1,5]]
print(Solution().insert( [[1,5]],[6,8])) # [[1,5],[6,8]]
print(Solution().insert( [[6,8]],[1,5])) # [[1,5],[6,8]]
print(Solution().insert( [[2,5],[6,7],[8,9]],[0,1])) # [[0,1],[2,5],[6,7],[8,9]]