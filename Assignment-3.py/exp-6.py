# 4.6. Experiment 19: Benchmark Harness (Datasets + Timing Table)

# Aim:
# Measure execution time fairly and compare algorithms on different input types.

# What you will implement (in lab):
# Generate random/sorted/reverse datasets for sizes 1000/5000/10000. Time insertion,
# merge, quick and print a table (27 values).

# Input / Output expectation:
# Input: sizes + seed. Output: timing table with clear labels.

# Lab checkpoints (faculty verifies):
# • Copy input before sorting
# • Clean timing table produced

# Viva (answer any 3):
# 1. Why reverse is worst for insertion?
# 2. Why quick may degrade on sorted with bad pivot?
# 3. Why merge stable but uses memory?

# SOLUTION :

import time
import random

def test_sort(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start


arr = [random.randint(1, 1000) for _ in range(1000)]

print("Insertion:", test_sort(insertion_sort, arr))
print("Merge:", test_sort(merge_sort, arr))
print("Quick:", test_sort(quick_sort, arr))