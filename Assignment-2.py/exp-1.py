# Experiment 7:
#   Arrays 1D (Operations + Shifting Cost)
# Aim :
#   Understand how insert/delete in arrays causes shifting and impacts complexity.
# What you will implement (in lab)
#   Perform insert at start/middle/end and delete at start/middle/end. For each case, compute and report approximate shift count.
# Input / Output expectation :
#      Input: list + position + value. Output: updated list + shift count + complexity statement.
# Lab checkpoints (faculty verifies) :
#    • Correct shift reasoning
#    • Student can explain O(1) vs O(n) operations
# Viva (answer any 3) :
#   1. Why index access is O(1)?
#   2. Why insertion at start is O(n)?
#   3. Static vs dynamic arrays?

# SOLUTION :

arr = [5,10,15,20,25]

# Insert at position
pos = 2
val = 8

arr.insert(pos, val)
print("Array after insertion:", arr)

# Delete element
del arr[pos]
print("Array after deletion:", arr)

            # TIME COMPLEXITY
# | Operation           | Time Complexity |
# | ------------------- | --------------- |
# | Insert at beginning | O(n)            |
# | Insert at middle    | O(n)            |
# | Insert at end       | O(1)            |
# | Delete              | O(n)            |
