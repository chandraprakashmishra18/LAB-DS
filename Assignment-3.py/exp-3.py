# Experiment 16: Merge Sort (Stable, O(n log n))

# Aim:
# Learn divide & conquer and stable merging.

# What you will implement (in lab):
# Implement merge(left,right) conceptually and merge sort. Note time O(n log n) and space O(n).

# Input / Output expectation:
# Input: list. Output: sorted list.

# Lab checkpoints (faculty verifies):
# • Merge step correct
# • Student states stability + space trade-off

# Viva (answer any 3):
# 1. Why stable?
# 2. Why needs extra memory?
# 3. Use in external sorting?

# SOLUTION :

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))