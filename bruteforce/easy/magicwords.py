# replace every character in string with the closest prime ASCII value

def findClosestPrime(c):
    dif = 1
    while(True):
        b = c - dif
        f = c + dif
        if isPrime(b):
            return b
        elif isPrime(f):
            return f
        elif b < 67: #limits
            return 67
        elif f > 113:
            return 113
        else:
            dif += 1

def isPrime(c):
    for i in range(2,c-1):
        if c % i == 0:
            return False
    return True

T = int(input()) #no of strings
for t in range(T):
    N = int(input()) #length of string
    st = input() #string
    l = []
    for c in st:
        c = ord(c)
        if isPrime(c):
            k = c
        else:
            k = findClosestPrime(c)
        l.append(chr(k))
    print("".join(l))
