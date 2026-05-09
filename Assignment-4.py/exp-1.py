# 5.1. Experiment 20: BST Insert/Search/Inorder:
    
# Aim:
# Build BST and prove sorted output using inorder traversal.

# What you will implement (in lab):
# Implement BST insert, search, inorder traversal. Use a fixed dataset and print inorder
# result.

# Input / Output expectation:
# Input: keys to insert + keys to search. Output: inorder list + found/not found.

# Lab checkpoints (faculty verifies):
# • BST property maintained
# • Inorder output sorted

# Viva (answer any 3):
# 1. Why inorder gives sorted?
# 2. Worst-case BST height?
# 3. Average complexity?

# Solution:

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None
for x in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, x)

inorder(root)
print("\nSearch 40:", search(root, 40) is not None)