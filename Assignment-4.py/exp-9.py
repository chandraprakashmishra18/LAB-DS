# 5.8. Experiment 27: Trie (Prefix Tree)

# Aim:
# Support prefix queries like autocomplete using trie.

# What you will implement (in lab):
# Implement trie insert/search/startsWith. Use a small word set and test prefix searches.

# Input / Output expectation:
# Input: words + prefixes. Output: True/False for exact and prefix match.

# Lab checkpoints (faculty verifies):
# • Prefix matching correct
# • Student explains why trie is fast for prefix

# Viva (answer any 3):
# 1. Trie vs hash map for prefix?
# 2. Space trade-off?
# 3. Autocomplete use?

# Solution:

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

t = Trie()
t.insert("apple")
print(t.search("apple"))
print(t.startsWith("app"))