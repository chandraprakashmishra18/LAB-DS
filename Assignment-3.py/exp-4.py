# Experiment 17: Quick Sort (Partition + Worst Case)

# Aim:
# Implement quick sort and understand pivot impact on performance.

# What you will implement (in lab):
# Implement quick sort using a clear partition scheme (e.g., last pivot). Explain worst-case
# scenario (already sorted + bad pivot).

# Input / Output expectation:
# Input: list. Output: sorted list.

# Lab checkpoints (faculty verifies):
# • Partition correct
# • Student writes worst-case condition in 2 lines

# Viva (answer any 3):
# 1. Worst-case for quick sort?
# 2. Is quick sort stable?
# 3. Average time?

# SOLUTION :

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([10, 7, 8, 9, 1, 5]))