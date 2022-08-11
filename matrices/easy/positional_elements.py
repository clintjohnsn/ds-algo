# EASY
# Find number of positional elements in a matrix. 
# positional element is one which is either minimum or maximum in a row or column
# assume matrix has distinct elements - no multiple min or max in a row or column

def countPositional(a,m,n):
    count = 0
    rowmax = [0]*m
    rowmin = [0]*m
    colmax = [0]*n
    colmin = [0]*n
    for i in range(m):
        rowmax[i] = max(a[i])
        rowmin[i] = min(a[i])
    for j in range(n):
        aux = []
        for i in range(m):
            aux.append(a[i][j])
        colmax[j] = max(aux)
        colmin[j] = min(aux)
    for i in range(m):
        for j in range(n):
            if a[i][j] == rowmax[i] or a[i][j] == rowmin[i] or a[i][j] == colmax[j] or a[i][j] == colmin[j]:
                count +=1
    return count

a = [[1,3,4],
    [5,2,9],
    [8,7,6]]
m = n = 3
print(countPositional(a,m,n))