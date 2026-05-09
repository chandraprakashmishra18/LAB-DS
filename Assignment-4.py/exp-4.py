# 5.3. Experiment 22: Heap / Priority Queue (Industry)

# Aim:
# Implement priority queue operations used in scheduling and real-time systems.

# What you will implement (in lab):
# Min-heap or max-heap with insert, peek, extract-min/max. Show extraction order to verify correctness.

# Input / Output expectation:
# Input: priorities. Output: extracted sequence + heap state.

# Lab checkpoints (faculty verifies):
# • Heap property maintained
# • Correct extraction order

# Viva (answer any 3):
# 1. Why heap for priority queues?
# 2. Insert/extract complexity?
# 3. Where used in industry?

# Solution:

import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print("Min:", heap[0])
print("Extract:", heapq.heappop(heap))
print("Heap:", heap)