# 4.1. Experiment 14: O(n2) Sorts + Counting

# Aim:
# Understand cost drivers (comparisons/swaps) and quadratic growth.

# What you will implement (in lab):
# Implement bubble or selection sort and count comparisons and swaps. Compare counts
# on random vs sorted small inputs.

# Input / Output expectation:
# Input: list. Output: sorted list + comparisons + swaps.

# Lab checkpoints (faculty verifies):
# • Counting is correct
# • Student explains best/worst case briefly

# Viva (answer any 3):
# 1. Stable vs unstable?
# 2. In-place meaning?
# 3. Why O(n2) is slow?

# SOLUTION :

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps


arr = [5, 3, 8, 4, 2]
sorted_arr, comp, swp = bubble_sort(arr)
print("Sorted:", sorted_arr)
print("Comparisons:", comp, "Swaps:", swp)