
'''
https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/

A car factory has two assembly lines, each with n stations. 
A station is denoted by Si,j where i is either 1 or 2 and indicates the assembly line the station is on,
and j indicates the number of the station. The time taken per station is denoted by ai,j.
 Each station is dedicated to some sort of work like engine fitting, body fitting, painting, and so on. 
 So, a car chassis must pass through each of the n stations in order before exiting the factory. 
 The parallel stations of the two assembly lines perform the same task. 
 After it passes through station Si,j, it will continue to station Si,j+1 unless 
 it decides to transfer to the other line. 
 Continuing on the same line incurs no extra cost, 
 but transferring from line i at station j – 1 to station j on the other line takes time ti,j.
Each assembly line takes an entry time ei and exit time xi which may be different for the two lines. 
Give an algorithm for computing the minimum time it will take to build a car chassis.


'''
# Time taken for station j on ith (0/1) line
def T(mem,n,i,j):
    if mem[i][j] != None:
        return mem[i][j]
    # end of the line
    else:
        if j + 1== n:
            # exit time for ith line
            mem[i][j] = a[i][j] + x[i]
        else:
             mem[i][j] =  min((a[i][j] + T(mem,n,i,j+1)),
                              (a[i][j] + t[i][j+1] + T(mem,n, ((i+1)%2) ,j+1)))
        return mem[i][j]

def assembly_line_scheduling():
    n = len(a[0])
    mem = [[None] * n for i in range(2)]
    return min( (e[0] + T(mem,n,0,0)),
                (e[1] + T(mem,n,1,0)))


## Driver Code
a = [ [ 4, 5, 3, 2 ],
      [ 2, 10, 1, 4 ] ] 
t = [ [ 0, 7, 4, 5 ],
      [ 0, 9, 2, 8 ] ]
e = [ 10, 12 ] 
x = [ 18, 7 ] # ans 35

print(assembly_line_scheduling())