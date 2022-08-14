"""
cache size  = The number of page frames that the cache can hold at a time
LRU caching scheme is to remove the least recently used frame when the cache is full 
and a new page is referenced which is not there in the cache
Need the operations to be O(1)

1. Queue: doubly-linked list. The maximum size of the queue will be equal to the cache size. 
    The most recently used pages will be near the front end and the least recently used pages will be near the rear end.
2. A Hashmap with the page number as key and the address of the corresponding queue node as value.

1. on new access, if page in hashmap (hit) move its node to front of the queue else (fault) add a new node to the front of the queue  
2. update the corresponding node address in the hash map. 
3. If the queue is full, we remove a node from the rear of the queue, and add the new node to the front of the queue.



OR

LinkedHashMap in Java or OrderedDict in Python (3.6+ the built-in dict class now keeps its items ordered as well)
Maintains the order of insertion in the dict
"""

# from collections import OrderedDict
 
# class LRUCache:
 
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity
 
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         else:
#             self.cache.move_to_end(key)
#             return self.cache[key]
 
#     def put(self, key: int, value: int) -> None:
#         self.cache[key] = value
#         self.cache.move_to_end(key)
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last = False)
 
 
# ## RUNNER

# cache = LRUCache(3)
# cache.put(1, 1)
# print(cache.cache)
# cache.put(2, 2)
# print(cache.cache)
# cache.get(1)
# print(cache.cache)
# cache.put(3, 3)
# print(cache.cache)
# cache.get(2)
# print(cache.cache)
# cache.put(4, 4)
# print(cache.cache)
# cache.get(1)
# print(cache.cache)
# cache.get(3)
# print(cache.cache)
# cache.get(4)
# print(cache.cache)


# ---------------------
from collections import deque
class LRU:
    
    def __init__(self, capacity:int) -> None:
        self.dq = deque()
        self.hm = dict()
        self.capacity = capacity
        self.size = 0

    # gets the value if present in cache
    def get(self,key:int)->int:
        if key in self.hm:
            self.dq.remove(self.hm[key])
            self.dq.append(self.hm[key])
            return self.hm[key]
        return -1
    
    def refer(self,key:int,page:int) -> int:
        if self.get(key) != -1:
            return self.get(key)
        else: # not in cache
            if self.size != self.capacity:
                self.size +=1
            else:
                val = self.dq.popleft()
                self.hm.pop(val) 
                # key and val is considered the same as page no here, popping item will be O(N)
                # other way is to have a ds for page with key/page no and the value both
            self.dq.append(page)
            self.hm[key] = page
            return page


# ## RUNNER
cache = LRU(3)
cache.refer(1, 1)
print(cache.dq)
cache.refer(2, 2)
print(cache.dq)
cache.get(1)
print(cache.dq)
cache.refer(3, 3)
print(cache.dq)
cache.get(2)
print(cache.dq)
cache.refer(4, 4)
print(cache.dq)
cache.get(1)
print(cache.dq)
cache.get(3)
print(cache.dq)
cache.get(4)
print(cache.dq)
