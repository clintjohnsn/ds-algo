"""
Leetcode 39
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target
 You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
"""

from copy import copy
class Solution:
    def combination_helper(self, candidates: list[int], target: int, res: set[tuple], combination: list[int]) -> None:
        if target == 0:
            res.add(tuple(combination))
        else:
            for i in range(len(candidates)):
                if target - candidates[i] >= 0:
                    new_combination = copy(combination)
                    new_combination[i] += 1
                    self.combination_helper(candidates, target-candidates[i],res,new_combination)

    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = set()
        result = list()
        combination = [0] * len(candidates)
        self.combination_helper(candidates,target,res,combination)
        for combination in res:
            k = list()
            for i in range(len(combination)):
                k.extend([candidates[i]] * combination[i])
            result.append(k)
        return result

print(Solution().combination_sum([2, 3, 6, 7], 7)) #  [[2,2,3],[7]]
print(Solution().combination_sum([2, 3, 5], 8)) #   [[2,2,2,2],[2,3,3],[3,5]]
