# Given two integers x and n, write a function to compute x^n.
# x * x .. n times = T : O(n)


def power(x, y):
    if(y == 0): return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0):
        return temp * temp
    else:
        if(y > 0): return x * temp * temp
        else: return (temp * temp) / x
     
# Driver Code
x, y = 2, -3
print('%.6f' %(power(x, y)))
x = 2; y = 3
print(power(x, y))

# T - O(logn) base 2