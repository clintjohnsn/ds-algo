"""
Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
Input:
Matrix:
 1  2  3
 4  5  6
 7  8  9
Output:
 3  6  9 
 2  5  8 
 1  4  7 

1: 0,0 - 2,0
7: 2,0 - 2,2
9: 2,2 - 0,2
3: 0,2 - 0,0

2: 0,1 - 1,0
4: 1,0 - 2,1
8: 2,1 - 1,2
6: 1,2 - 0,1

TODO: this
"""

def rt(M,i,j):
    pass    

def rotate(M):
    n = len(M)
    rt(M,0,n-1)


def printm(M):
    n = len(M)
    for i in range(n):
        print()
        for j in range(n):
            print(M[i][j],end='')

# # driver
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
 
# Test case 2
mat2 = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]
 
# Test case 3
mat3 = [ [1, 2 ],
        [4, 5 ] ]
         
rotate(mat)
printm(mat)