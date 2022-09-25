"""
Leetcode 208
Implement Trie (Prefix Tree)
 tree data structure used to efficiently store and retrieve keys in a dataset of strings
https://www.geeksforgeeks.org/trie-delete/
https://www.geeksforgeeks.org/trie-insert-and-search/

insert - Inserts the string word into the trie.
search-  Returns true if the string word is in the trie
startsWith(String prefix) - Returns true if there is a previously inserted string word that has the prefix

word and prefix consist only of lowercase English letters.
"""

"""
Time complexity: insert, search, startswith = O(m), m is the length of string
Space complexity - O(alphabet_size * m * n), n is the no of keys
"""
class Node:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if node.children[ord(word[i])-ord("a")] is None:
                node.children[ord(word[i])- ord("a")] = Node()
            node = node.children[ord(word[i])- ord("a")]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if node.children[ord(word[i]) - ord("a")] is None:
                return False
            else:
                node = node.children[ord(word[i]) - ord("a")]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if node.children[ord(prefix[i]) - ord("a")] is None:
                return False
            else:
                node = node.children[ord(prefix[i]) - ord("a")]
        return True

# Test
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))     # return True