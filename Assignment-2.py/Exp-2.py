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

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

result = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix Addition Result:")
for row in result:
    print(row)