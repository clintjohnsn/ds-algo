# Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
#  Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

#  in - abba
# out - 4
# [a,a], [ab,ba] [b,b] [abb, bba]

def dr(subst):
    k = {}
    for i in subst:
        if i in k:
            k[i]+=1
        else:
            k[i] = 1
    return "".join([str((key,k[key])) for key in sorted(k.keys())])
        


def anagrams(s):
    dt = {}
    count = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if dr(s[i:j]) in dt:
                dt[dr(s[i:j])] += 1
            else:
                dt[dr(s[i:j])] = 1
    for k,v in dt.items():
        count += v * (v-1)/2
    return int(count)