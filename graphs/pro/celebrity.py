"""
https://www.geeksforgeeks.org/the-celebrity-problem/

In a party of N people, only one person is known to everyone. 
Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. 
We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
We can describe the problem input as an array of numbers/characters representing persons in the party. 
We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise
HaveAcquaintance(A,A) = false
HaveAcquaintance can be a adjacency matrix

eg
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2
Explanation: The person with ID 2 does not 
know anyone but everyone knows him

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity
Explanation: There is no celebrity.
could have loners too - dont know anyone, but not everyone knows them

any sort of brute force is T =  O(n^2). do better.

eg:
    keep 2 lists  indegree and outdegree. for every i,j calculate indegree outdegree, check which has indegree n and outdegree 0


# METHOD 1 Recursion
 if the ‘potential celebrity’ of N-1 persons is known
 between n and this pc(n-1), pc(n) is
    if n knows n-1, n cannot be, pc(n) =pc(n-1)
    else if n-1 knows n, n-1 cannot be, pc(n) = n
    else (dont know each other), neither can be , pc(n) = -1
2 * n calls

once we have pc(n) check if everyone knows them and they dont know anyone (2n calls)

or, simpler
If A knows B, then A can’t be a celebrity. Discard A, and B may be celebrity.
If A doesn’t know B, then B can’t be a celebrity. Discard B, and A may be celebrity.

"""


# T = O(n)
# S = O(1) + (O(n) for recursive stack)

n = 4
# Person with id 2 is celebrity
MATRIX = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]
 
def knows(a, b):
    return MATRIX[a][b]
 
def pc(n):

    if (n == 0):
        return 0;
 
    # Find the celebrity with n-1
    # persons
    id = pc(n - 1)
 
    # If there are no celebrities
    if (id == -1):
        return n - 1
    # if the id knows the nth person
    # then the id cannot be a celebrity, but nth person
    # could be on
    elif knows(id, n - 1):
          return n - 1
    # if the id knows the nth person
    # then the id cannot be a celebrity, but nth person
    # could be one
    elif knows(n - 1, id):
          return id
    return - 1

#cleaner
def alt_pc(n):
    if n == 0:
        return n
    p = alt_pc(n-1)
    if knows(p,n):
        return n
    else:
        return p

# tail recursive
def alt_pc_2(i,n,pc):
    if i == n:
        return pc
    if i == 0:
        pc = 0
    if knows(pc,i):
        pc = i
    return alt_pc_2(i+1,n,pc)

def celebrity(n):
    # id=alt_pc(n-1)
    # id = pc(n)
    # id = alt_pc_2(0,n,0)
    if (id == -1):
        return id
    else:
        c1=0
        c2=0
        for i in range(n):
            if (i != id):
                c1 += knows(id, i)
                c2 += knows(i, id)
        if (c1 == 0 and c2 == n - 1):
            return id
        return -1
 
## driver
print(celebrity(n))
