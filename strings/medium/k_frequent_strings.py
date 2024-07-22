"""
Leetcode 692
https://leetcode.com/problems/top-k-frequent-words/

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
 with the number of occurrence being 4, 3, 2 and 1 respectively.

 Input : ["i","love","leetcode","i","love","coding"]
k = 3
output: ["i","love","coding"]
"""

from collections import defaultdict
import heapq

class Node:
    def __init__(self,freq:int,val:str):
        self.freq = freq
        self.val = val

    def __lt__(self, other):
        return (self.freq < other.freq) or (self.freq == other.freq and self.val > other.val)

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        hm = defaultdict(int)
        for word in words:
            hm[word] +=1
        minheap = list()
        freq = [Node(freq,word) for word,freq in hm.items()]
        for i in range(k):
            minheap.append(freq[i])
        heapq.heapify(minheap)
        for i in range(k,len(freq)):
            smallest = heapq.heappop(minheap)
            if freq[i].freq > smallest.freq or (freq[i].freq == smallest.freq and freq[i].val < smallest.val):
                heapq.heappush(minheap,freq[i])
            else:
                heapq.heappush(minheap,smallest)
        minheap.sort(key=lambda x:(-x.freq,x.val))
        return [node.val for node in minheap]


words1 = ["i","love","leetcode","i","love","coding"] #  ["i","love"]
words2 = ["the","day","is","sunny","the","the","the","sunny","is","is"] # ["the","is","sunny","day"]
words3 = ["i","love","leetcode","i","love","coding"] # ["i","love","coding"]
print(Solution().topKFrequent(words1,2))
print(Solution().topKFrequent(words2,4))
print(Solution().topKFrequent(words3,3))
