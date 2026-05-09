# Experiment 15: Insertion Sort (Advantage on Nearly Sorted)

# Aim:
# Implement insertion sort and observe behavior on nearly sorted data.

# What you will implement (in lab):
# Implement insertion sort and optionally print pass-wise array for a small input.

# Input / Output expectation:
# Input: list. Output: sorted list (+ optional pass prints).

# Lab checkpoints (faculty verifies):
# • Correct for duplicates
# • Student explains “nearly sorted” benefit

# Viva (answer any 3):
# 1. Worst-case input?
# 2. Is insertion stable?
# 3. Space complexity?

# SOLUTION :

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([5, 2, 9, 1, 5, 6]))