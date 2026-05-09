# 5.6. Experiment 25: DFS Traversal

# Aim:
# Traverse graph deeply and output traversal order.

# What you will implement (in lab):
# Implement DFS(start) recursively or using stack. Print DFS order from start node.

# Input / Output expectation:
# Input: start node. Output: DFS traversal list.

# Lab checkpoints (faculty verifies):
# • Correct DFS traversal
# • Visited prevents cycles

# Viva (answer any 3):
# 1. DFS vs BFS?
# 2. Recursion depth issue?
# 3. Use case of DFS?

# Solution:

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor, _ in graph[node]:
            dfs(graph, neighbor, visited)

dfs(graph, 'A') # type: ignore