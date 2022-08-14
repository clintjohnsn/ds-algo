"""

Given a linked list where every node represents a linked list and contains two pointers of its type: 

Pointer to next node in the main list (we call it right pointer) 
Pointer to a linked list (we call it the down pointer)
All linked lists are sorted

flatten this ds into a linked list. resultant linked list should also be sorted

eg

Input:  5 -> 10 -> 19 -> 28
        |     |     |     |
        7     20    22    35
        |           |      |
        8           50     40
        |                   |
        30                 45

Output: 5->7->8->10->19->20->22->28->30->35->40->45->50

# Method 1
Recursively call to merge the current linked list with the next linked list
If the current linked list is empty or there is no next linked list then return the current linked list (Base Case)
Start merging the linked lists, starting from the last linked list

Time Complexity: O(N * N * M) – where N is the no of nodes in the main linked list and M is the no of nodes in a single sub-linked list 
Explanation: As we are merging 2 lists at a time,

After adding the first 2 lists, the time taken will be O(M+M) = O(2M).
Then we will merge another list to above merged list -> time = O(2M + M) = O(3M).
Then we will merge another list -> time = O(3M + M).
We will keep merging lists to previously merged lists until all lists are merged.
Total time taken will be O(2M + 3M + 4M + …. N*M) = (2 + 3 + 4 + … + N) * M
Using arithmetic sum formula: time = O((N * N + N – 2) * M/2)
The above expression is roughly equal to O(N * N * M) for a large value of N
Auxiliary Space: O(N*M) – because of the recursion. 
The recursive functions will use a recursive stack of a size equivalent to a total number of elements in the lists, which is N*M.

# Method 2
Create a priority queue(Min-Heap) and push the head node of every linked list into it
While the priority queue is not empty, extract the minimum value node from it 
and if there is a next node linked to the minimum value node then push it into the priority queue
Also, print the value of the node every time after extracting the minimum value node

Time Complexity: O(N * M * log(N)) – where N is the no of nodes in the main linked list (reachable using the next pointer) and M is the no of nodes in a single sub-linked list (reachable using a bottom pointer).
Auxiliary Space: O(N) – where N is the no of nodes in the main linked list (reachable using the next pointer).
"""

