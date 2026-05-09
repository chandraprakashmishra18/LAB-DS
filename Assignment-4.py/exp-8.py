# 5.7. Experiment 26: Hash Table (Separate Chaining)

# Aim:
# Handle collisions using separate chaining and verify retrieval after collisions.

# What you will implement (in lab):
# Implement insert/get/delete with chaining. Use key % tableSize hash. Demonstrate collisions with multiple keys.

# Input / Output expectation:
# Input: key-value pairs. Output: bucket display + get/delete results.

# Lab checkpoints (faculty verifies):
# • Collisions demonstrated clearly
# • delete removes correct pair

# Viva (answer any 3):
# 1. Collision meaning?
# 2. Why chaining works?
# 3. Load factor?

# Solution:

class HashTable:
    def __init__(self, size):
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = key % len(self.table)
        self.table[index].append((key, value))

    def get(self, key):
        index = key % len(self.table)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = key % len(self.table)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

ht = HashTable(5)
ht.insert(1, "A")
ht.insert(6, "B")
print(ht.get(6))
ht.delete(6)
print(ht.get(6))