from collections import defaultdict
from errno import E2BIG


"""
Find the smallest window in a string containing all characters of another string
Eg

Input: string = “this is a test string”, pattern = “tist” 
Output: Minimum window is “t stri” 
Explanation: “t stri” contains all the characters of pattern.

Input: string = “geeksforgeeks”, pattern = “ork” 
Output: Minimum window is “ksfor”

TODO: this
"""
def find_substring(x,y):
  pat = [0] * 256
  visited = [0] * 256
  fstart,fend = -1, float('inf')
  start,end = -1,-1
  for c in y:
    pat[ord(c)] +=1
    visited[ord(c)] +=1
  for i in range(len(x)):
    if visited[ord(x[i])] != 0:
      if start == -1:
        start,end = i,i
      else:
        end = i
      visited[ord(x[i])] -= 1
      if sum(visited) == 0:
        if end - start < fend - fstart:
          fend = end
          fstart = start
        visited[ord(x[start])] += 1
        start = ?
  print(x[fstart:fend+1])

x = "this is a test string"
y = "tist"
x1 = "geeksforgeeks"
y1 = "ork"
find_substring(x,y)
find_substring(x1,y1)