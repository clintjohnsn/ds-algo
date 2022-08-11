# An hourglass in A  is a subset of values with indices falling in this pattern in matrix's graphical representation:
# a b c
#   d
# e f g

# Calculate the hourglass sum for every hourglass in matrix , then print the maximum hourglass sum

# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0

#  16 hourglasses are
#  -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18

#   highest 28

def hourglassSum(arr):
    m = float('-inf')
    if len(arr) < 3:
        return 0
    for i in range(1,len(arr)-1):
        for j in range(1,len(arr)-1):
            sum = arr[i][j] + arr[i-1][j] + arr[i-1][j-1]+ arr[i-1][j+1]+ arr[i+1][j]+ \
            arr[i+1][j-1]+ arr[i+1][j+1]
            m = max(sum,m)
    return m