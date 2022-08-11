# Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
# Input:
# Matrix:
#  1  2  3
#  4  5  6
#  7  8  9
# Output:
#  3  6  9 
#  2  5  8 
#  1  4  7 

# 1: 0,0 - 2,0
# 7: 2,0 - 2,2
# 9: 2,2 - 0,2
# 3: 0,2 - 0,0

# 2: 0,1 - 1,0
# 4: 1,0 - 2,1
# 8: 2,1 - 1,2
# 6: 1,2 - 0,1

def rotate(M,n):
    i,j = 0,0




# driver
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix,len(matrix))