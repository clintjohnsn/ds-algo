"""
Leetcode 322
coin change

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""


"""
recursive
"""

counter = {}
counter["recursive"] = 0
counter["memoized"] = 0


class Solution:
    def coin_change_helper(self, coins: list[int], amount: int) -> int | float:
        counter["recursive"] += 1
        if amount < 0:
            return float("inf")
        if amount == 0:
            return 0
        counts = [1 + self.coin_change_helper(coins, amount - coin) for coin in coins]
        return min(counts)

    def coin_change(self, coins: list[int], amount: int) -> int:
        count = self.coin_change_helper(coins, amount)
        return -1 if count == float("inf") else count


# Test
print(Solution().coin_change([1, 2, 5], 11)) # 3
print(Solution().coin_change([2], 3)) # -1
print(Solution().coin_change([1], 0)) # 0

print("-----------------")

"""
memoized
"""

class Solution:
    def coin_change_helper(self, coins: list[int], amount: int, mem: list[int]) -> int | float:
        counter["memoized"] += 1
        if amount < 0:
            return float("inf")
        if mem[amount] != -1:
            return mem[amount]
        counts = [1 + self.coin_change_helper(coins, amount - coin, mem) for coin in coins]
        mem[amount] = min(counts)
        return mem[amount]

    def coin_change(self, coins: list[int], amount: int) -> int:
        mem = [-1] * (amount + 1)
        mem[0] = 0
        count = self.coin_change_helper(coins, amount, mem)
        return -1 if count == float("inf") else count

# Test
print(Solution().coin_change([1, 2, 5], 11)) # 3
print(Solution().coin_change([2], 3)) # -1
print(Solution().coin_change([1], 0)) # 0

"""
bottom up approach
TODO
"""

print("-----------------")
print(counter)
