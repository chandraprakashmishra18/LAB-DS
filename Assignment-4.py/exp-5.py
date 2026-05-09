# 5.4. Experiment 23: Graph Build (Adjacency List)

# Aim:
# Represent directed weighted graph using adjacency list.

# What you will implement (in lab):
# Create 5–7 nodes and 8–10 edges. Store as adjacency list and print readable structure.

# Input / Output expectation:
# Input: edges. Output: adjacency list print.

# Lab checkpoints (faculty verifies):
# • Correct representation
# • Weight shown with each edge

# Viva (answer any 3):
# 1. List vs matrix?
# 2. Directed vs undirected?
# 3. Weighted graph use?

# Solution:

graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3)],
    'C': [('D', 4)],
    'D': []
}

for node in graph:
    print(node, "->", graph[node])