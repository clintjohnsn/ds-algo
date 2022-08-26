"""
 Given a string, find the length of the longest substring without repeating characters.
 For example, the longest substrings without repeating characters
 for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6. For “BBBB” the
longest substring is “B”, with length 1

 n*(n+1)/2 substrings. Whether a substirng contains all unique characters or not
  can be checked in linear time by scanning
  it from left to right and keeping a map of visited characters.
   brute force Time complexity of this solution would be O(n^3).

  """

NO_OF_CHARS = 256

def longestUniqueSubsttr(string):
	n = len(string)
	cur_len = 1	 # To store the length of current substring
	max_len = 1	 # To store the result
	prev_index = 0 # To store the previous index
	i = 0

	# Initialize the visited array as -1, -1 is used to indicate
	# that character has not been visited yet.
	visited = [-1] * NO_OF_CHARS

	# Mark first character as visited by storing the index of
	# first character in visited array.
	visited[ord(string[0])] = 0

	# Start from the second character. First character is already
	# processed (cur_len and max_len are initialized as 1, and
	# visited[str[0]] is set
	for i in range(1,n):
		prev_index = visited[ord(string[i])]

		# If the current character is not present in the already
		# processed substring or it is not part of the current NRCS,
		# then do cur_len++
		if prev_index == -1 or (i - cur_len > prev_index):
			cur_len+=1

		# If the current character is present in currently considered
		# NRCS, then update NRCS to start from the next character of
		# previous instance.
		else:
			# Also, when we are changing the NRCS, we should also
			# check whether length of the previous NRCS was greater
			# than max_len or not.
			if cur_len > max_len:
				max_len = cur_len

			cur_len = i - prev_index

		# update the index of current character
		visited[ord(string[i])] = i

	# Compare the length of last NRCS with max_len and update
	# max_len if needed
	if cur_len > max_len:
		max_len = cur_len

	return max_len

# Driver program to test the above function
string = "ABDEFGABEF"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print ("The length of the longest non-repeating character" +
	" substring is " + str(length))


# Time Complexity: O(n + d) where n is length of the input string and d is number
# of characters in input string alphabet. For example, if string consists of
# lowercase English characters then value of d is 26.
#
# Auxiliary Space: O(d)


def lengthOfLongestSubstring(self, s: str) -> int:
	hm = dict()
	k = -1
	maxstr = 0
	for i in range(len(s)):
		if s[i] not in hm:
			hm[s[i]] = i
		else:
			k = max(k, hm[s[i]])
			hm[s[i]] = i
		maxstr = max(maxstr, i - k)
	return maxstr

"""
if we know that the charset is rather small, we can mimic what a HashSet/HashMap does with a boolean/integer array as direct access table. 
Though the time complexity of query or insertion is still O(1), the constant factor is smaller in an array than in a HashMap/HashSet. 
Thus, we can achieve a shorter runtime by the replacement here.
"""