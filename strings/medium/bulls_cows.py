"""
Leetcode 299

You write down a secret number and ask your friend to guess what the number is.
The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number
but are located in the wrong position.

The hint should be formatted as "xAyB",
 where x is the number of bulls and y is the number of cows.

Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"

"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        sm = [0] * 10
        gm = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
            else:
                sm[int(secret[i])] +=1
                gm[int(guess[i])] +=1
        for i in range(10):
            cows += min(sm[i],gm[i])
        return str(bulls) + "A" + str(cows) + "B"

print(Solution().getHint("1807","7810"))
print(Solution().getHint("1123","0111"))

