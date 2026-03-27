# Aim :
#   Practice 2D arrays for real-world tabular data and understand traversal complexity.
# What you will implement (in lab) :
#   Create a matrix and implement: row sum, column sum, search for a value, and transpose
#   (conceptual output).
# Input / Output expectation :
#   Input: matrix. Output: computed sums + search result + transpose preview.
# Lab checkpoints (faculty verifies) :
#   • Correct row/column traversal
#   • Clean output formatting
# Viva (answer any 3) :
#   1. Complexity of scanning a matrix?
#   2. Real-world use of 2D arrays?
#   3. Memory layout idea (row-wise)?

# SOLUTION :

# 2D Array (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)
    
# -------- ROW SUM --------
print("\nRow Sum:")
for i in range(len(matrix)):
    print("Row", i, "sum =", sum(matrix[i]))

# -------- COLUMN SUM --------
print("\nColumn Sum:")
for j in range(len(matrix[0])):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]
    print("Column", j, "sum =", col_sum)

# -------- SEARCH --------
target = 5
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            print("\nElement", target, "found at position:", (i, j))
            found = True

if not found:
    print("\nElement not found")

# -------- TRANSPOSE --------
print("\nTranspose:")

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()
    
# Traversing a matrix requires visiting each element → O(n × m)
# Row and column operations depend on nested loops
# 2D arrays are useful for representing structured/tabular data