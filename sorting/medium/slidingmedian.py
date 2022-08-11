# If the amount spent by a client on a particular day is greater than or equal to  
# twice the client's median spending for a trailing number of days, they send the client a notification about potential fraud.
# Given the number of trailing days d  and a client's total daily expenditures for a period of n days,
#  find and print the number of times the client will receive a notification over all n days.

# constraint : expenditure < 210

# n = 9 d = 5
# expenditures = 2 3 4 2 3 6 8 4 5

# o/p 2

# 2 3 4 2 3 -> 2 2 3 3 4 -> median = 3
# 6 >= 2*3, count =1

# 3 4 2 3 6 -> 2 3 3 4 6 -> median = 3
# 8 >= 2*3, count =2 

# 4 2 3 6 8 -> 2 3 4 6 8 -> median 4
# 4 < 2*4, count remains same ..

countarr = [0] * 210

def add(x):
    countarr[x] +=1

def remove(x):
    countarr[x] -=1
    
def median(d):
    s = 0
    for i,x in enumerate(countarr):
        s += x
        if s >= d/2:
            if d % 2 == 1:
                return i
            else:
                if s - d/2 > 0:
                    return i
                else:
                    j = i+1
                    while(countarr[j]==0):
                        j+=1
                    return (i + j)/2
                    
        

def sliding_medium(expenditure, d):
    count = 0
    for i in range(d):
        add(expenditure[i])
    for i in range(d,len(expenditure)):
        # print(countarr)
        # print(median(d))
        if expenditure[i] >= 2* median(d):
            count+=1
        remove(expenditure[i-d])
        add(expenditure[i])
    return count

# ex = [2,3, 4, 2, 3, 6, 8, 4, 5]
# d = 4
# print("ans",sliding_medium(ex,d))

with open("test.txt","r") as fr:
    content = fr.readlines()
    n, d = list(map(int,content[0].split(" ")))
    ex = list(map(int,content[1].split(" ")))
    print(sliding_medium(ex,d))