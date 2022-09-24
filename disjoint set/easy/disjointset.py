class DisjointSet:

  def __init__(self, n):
    self.rank = [1] * n
    self.parent = [i for i in range(n)]

  def find(self, x):
    # Finds the representative of the set
    # that x is an element of
    if (self.parent[x] != x):
      # if x is not the parent of itself Then x is not the representative of its set
      # so we recursively call Find on its parent and move i's node directly under the representative of this set
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
# update rank?

  # Do union of two sets represented
  # by x and y.
  def union(self, x, y):
    # Find representatives of x and y
    xset = self.find(x)
    yset = self.find(y)
    # If they are already in same set
    if xset == yset:
      return
    # Put smaller ranked item under bigger ranked item if ranks are different
    if self.rank[xset] < self.rank[yset]:
      self.parent[xset] = yset
    elif self.rank[xset] > self.rank[yset]:
      self.parent[yset] = xset
    # If ranks are same,doesn't matter which one goes where
    # increment rank of tree
    else:
      self.parent[yset] = xset
      self.rank[xset] = self.rank[xset] + 1

# Driver code
obj = DisjointSet(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)
print(obj.find(4) == obj.find(0))
print(obj.find(1) == obj.find(0))
print(obj.parent)
print(obj.rank)