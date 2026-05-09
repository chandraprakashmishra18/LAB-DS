# 5.2. Experiment 21: BST Delete (All Cases)

# Aim:
# Delete nodes correctly and keep BST valid (all 3 cases).

# What you will implement (in lab):
# Implement delete handling: leaf, one child, two children (successor). Print inorder after
# each delete as proof.

# Input / Output expectation:
# Input: delete keys. Output: inorder after each deletion.

# Lab checkpoints (faculty verifies):
# • All delete cases tested
# • Proof via inorder after each operation

# Viva (answer any 3):
# 1. Inorder successor meaning?
# 2. Why delete is tricky?
# 3. How to verify correctness?

# Solution:

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if not root:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

root = delete(root, 50) # type: ignore
inorder(root) # type: ignore