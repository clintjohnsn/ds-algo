"""
leetcode 1046

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

"""
import  heapq # min heap
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        maxheap = [-stone for stone in stones] # convert min heap to max heap
        heapq.heapify(maxheap) # put all elements in max heap
        while len(maxheap) > 1:
            smash = (heapq.heappop(maxheap) - heapq.heappop(maxheap))
            if smash != 0:
                heapq.heappush(maxheap,smash) # if anything remains put it back
        if maxheap: # if any remaining value (max 1)
            return -maxheap[0]
        else: # no values remain
            return 0

# Driver
stones = [2, 7, 4, 1, 8, 1]
print(Solution().lastStoneWeight(stones))
print(Solution().lastStoneWeight([2,2]))

"""
S- O(N)
T - average O(NLogN) ??
heapifying takes O(N), taking the largest 2 out takes O(log N), 
and then this repeated until nothing remains -> this can be >> n
"""