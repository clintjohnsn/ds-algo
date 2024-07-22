"""
Leetcode 735
https://leetcode.com/problems/asteroid-collision/

asteroid collision

given an array asteroids
For each asteroid, the absolute value represents its size, and the sign represents its direction
 Each asteroid moves at the same speed.
 Find out the state of the asteroids after all collisions
 If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
 Two asteroids moving in the same direction will never meet (same speed)

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
"""

class Solution:
    def asteroid_collision(self, asteroids: list[int]) -> list[int]:
        stack = list()
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            if asteroid < 0:
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        asteroid = None
                        break
                    else:
                        break
                if (not stack or stack[-1] < 0) and asteroid is not None:
                    stack.append(asteroid)
        return stack

#Test
print(Solution().asteroid_collision([5, 10, -5])) # [5,10]
print(Solution().asteroid_collision([8, -8])) #  []
print(Solution().asteroid_collision([10, 2, -5])) # [10]
print(Solution().asteroid_collision([-2, -1, 1, 2])) # [-2,-1,1,2]
print(Solution().asteroid_collision([-2, 1, -2, -1])) # [-2,-2,-1]
print(Solution().asteroid_collision([-2, 1, -1, -1])) # [-2,-1]

"""
alternate impl
"""

class Solution(object):
    def asteroid_collision(self, asteroids):
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans


"""
T = O(N)
S = O(N)
"""