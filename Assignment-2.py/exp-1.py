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

def insert_array(arr, pos, value):
    n = len(arr)
    shifts = n - pos  # elements to shift right 
    arr.insert(pos, value)

    # Time Complexity
    if pos == n:
        complexity = "O(1)"
    else:
        complexity = "O(n)"

    return arr, shifts, complexity


def delete_array(arr, pos):
    n = len(arr)
    shifts = n - pos - 1  # elements to shift left that's why we'll use -1 as well here 
    arr.pop(pos)

    # Time Complexity
    if pos == n - 1:
        complexity = "O(1)"
    else:
        complexity = "O(n)"

    return arr, shifts, complexity

# ----------- DRIVER CODE -----------

arr = [10, 20, 30, 40]

print("Original Array:", arr)

# Insert operations
print("\n--- INSERT OPERATIONS ---")
print("Insert at Start:", insert_array(arr.copy(), 0, 5))
print("Insert at Middle:", insert_array(arr.copy(), 2, 25))
print("Insert at End:", insert_array(arr.copy(), len(arr), 50))

# Delete operations
print("\n--- DELETE OPERATIONS ---")
print("Delete at Start:", delete_array(arr.copy(), 0))
print("Delete at Middle:", delete_array(arr.copy(), 2))
print("Delete at End:", delete_array(arr.copy(), len(arr)-1))

#              Observation Table
        #     -------------------
# Operation	            |   Shift Count	  |  Time Complexity
# --------------------- | --------------- | -------------------
# Insert at Start	    |    n	          |      O(n)
# Insert at Middle	    |    n/2	      |      O(n)
# Insert at End	        |    0	          |      O(1)
# Delete at Start	    |    n-1	      |      O(n)
# Delete at Middle	    |    n/2 	      |      O(n)
# Delete at End	        |    0	          |      O(1)

# Operations at the start and middle require shifting, hence O(n) complexity.
# Operations at the end do not require shifting, hence O(1) complexity.
# This demonstrates why arrays are inefficient for frequent insertions/deletions except at the end.