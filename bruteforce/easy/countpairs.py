#  Given an array of integers 
#  representing the color of each sock, determine how many pairs of socks with matching colors there are.

def sockMerchant(n, ar):
    s = {}
    for x in ar:
        if x in s:
            s[x] +=1
        else:
            s[x] = 1
    return sum([s[x]//2 for x in s ])