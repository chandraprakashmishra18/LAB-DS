# Experiment 18: Heap Sort (Heapify + Sorting)

# Aim:
# Use heapify idea to sort in O(n log n) and connect to priority queue.

# What you will implement (in lab):
# Implement heapify + heap sort (min or max). Explain why heap sort is not stable.

# Input / Output expectation:
# Input: list. Output: sorted list.

# Lab checkpoints (faculty verifies):
# • Heap property maintained
# • Correct final sort result

# Viva (answer any 3):
# 1. Why heap sort not stable?
# 2. Heap vs BST for top-k?
# 3. Real priority queue use?

# SOLUTION :

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


print(heap_sort([12, 11, 13, 5, 6, 7]))