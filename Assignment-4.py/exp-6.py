# 5.5. Experiment 24: BFS Traversal

# Aim:
# Traverse graph level-wise and output traversal order.

# What you will implement (in lab):
# Implement BFS(start) using queue and visited set. Print BFS order from a chosen start
# node.

# Input / Output expectation:
# Input: start node. Output: BFS traversal list.

# Lab checkpoints (faculty verifies):
# • Queue-based correct traversal
# • Visited prevents cycles

# Viva (answer any 3):
# 1. Why queue in BFS?
# 2. Shortest path relation?
# 3. Complexity O(V+E)?

# Solution:
    
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor, _ in graph[node]:
                queue.append(neighbor)

bfs(graph, 'A') # type: ignore