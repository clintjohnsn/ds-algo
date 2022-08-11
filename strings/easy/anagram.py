# An anagram of a string is another string that contains same characters, only the order of characters can be different.

# method 1 : sort and compare
# T - O(nlogn)
# S - O(1)

# method 2: counting characters in bins
# 1) Create count arrays of size 256 for both strings. Initialize all values in count arrays as 0.
# 2) Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
# 3) Compare count arrays. If both count arrays are same, then return true.

NO_OF_CHARS = 256

def areAnagram(str1, str2):

    # Create two count arrays and initialize all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    # For each character in input strings, increment count
    # in the corresponding count array
    for i in str1:
        count1[ord(i)]+=1

    for i in str2:
        count2[ord(i)]+=1


    # Compare count arrays
    for i in xrange(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1

# Driver program to test the above functions
str1 = "aaca"
str2 = "acaa"
if areAnagram(str1, str2):
    print "The two strings are anagram of each other"
else:
    print "The two strings are not anagram of each other"
