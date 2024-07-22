"""
Leetcode 621

https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
 Tasks could be done in any order. Each task is done in one unit of time.
  For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
"""
from collections import  defaultdict
import  heapq
class Solution:
    def least_interval(self, tasks: list[str], n: int) -> int:
        if n <= 0:
            return len(tasks)
        hm = defaultdict(int)
        for task in tasks:
            hm[task] +=1
        maxheap = [(-val, key) for key,val in hm.items()]
        heapq.heapify(maxheap)
        time = 0
        temp = list()
        while maxheap:
            k = n + 1
            finished = 0
            temp.clear()
            while k > 0 and maxheap:
                freq, task = heapq.heappop(maxheap)
                freq = -freq
                if freq - 1 > 0 :
                    temp.append((freq-1,task))
                else:
                    finished +=1
                k -=1
            if not temp:
                # temp is empty
                time +=finished
            else:
                time += finished + len(temp) + k
            for freq,task in temp:
                heapq.heappush(maxheap,(-freq,task))
        return time


# Test
print(Solution().least_interval(["A","A","A","B","B","B"],2)) # 8
print(Solution().least_interval(["A","A","A","B","B","B"],0)) # 6
print(Solution().least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)) # 16
print(Solution().least_interval(["A","A","A","B","B","B","C","C","D","E","F","G"], 3)) # 16

"""
S = O(n), t= O(1) solution

The key is to find out how many idles do we need.

eg 3 A, 2 B, 1 C
A ? ? A ? ? A
"?" is "empty" slots.

Now we can use the same way to arrange B and C

A B C A B # A
"#" is idle

Now we have a way to arrange tasks
but don't need actually arrange them.  
we only need to get the total idles
no of tasks + idles = total time taken
With the fact that A is the task with most frequency, it should need more idles than any other tasks
finding no of idles with A is enough

A separated slots into (count(A) - 1) = 2 parts, each part has length n.
number of parts separated by A: partCount = count(A) - 1; 
emptySlots = partCount * n;
availableTasks = tasks.length - count(A)
idles = max(0, emptySlots - availableTasks);

case: more than one task with most frequency
3 A 3 B 2 C 1 D, n = 3

A B ? ? A B ? ? A B

partCount = count(A) - 1
emptySlots = partCount * (n - (count of tasks with most frequency - 1))
availableTasks = tasks.length - count(A) * count of tasks with most frenquency
idles = max(0, emptySlots - availableTasks)
result = tasks.length + idles

case: What if we have more than n tasks with most frequency 
 3A, 3B, 3C, 3D, 2E, n = 2. 
 You can always first arrange A, B, C, D as:
A B C D E| A B C D E| A B C D
emptySlots < 0 means you have already got enough tasks to fill in each part to make arranged tasks valid
"""

class Solution:
    def least_interval(self, tasks: list[str], n: int) -> int:
        counter = [0]  * 26
        for task in tasks:
            counter[ord(task)-ord("A")] +=1
        count = max(counter)
        parts =  count - 1
        max_freq_tasks = counter.count(count)
        empty_slots = parts * (n-max_freq_tasks + 1)
        available_tasks = len(tasks) - count * max_freq_tasks
        idles = max(0,empty_slots-available_tasks)
        return len(tasks) + idles

# Test
print("-----------------------------")
print(Solution().least_interval(["A","A","A","B","B","B"],2)) # 8
print(Solution().least_interval(["A","A","A","B","B","B"],0)) # 6
print(Solution().least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)) # 16
print(Solution().least_interval(["A","A","A","B","B","B","C","C","D","E","F","G"], 3)) # 16