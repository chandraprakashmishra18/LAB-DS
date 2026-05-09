# 5.9. Experiment 28: Bloom Filter (Concept + Toy Demo)

# Aim:
# Introduce probabilistic membership test used in modern systems.

# What you will implement (in lab):
# Explain bloom filter (bit array + k hash functions). Demonstrate toy membership test
# and false positive concept.

# Input / Output expectation:
# Input: insert items + query items. Output: “possibly present” / “definitely not present”.

# Lab checkpoints (faculty verifies):
# • Student explains false positives clearly
# • Demonstration includes 1 meaningful query

# Viva (answer any 3):
# 1. Can bloom filter have false negatives?
# 2. Why memory efficient?
# 3. Industry use (DB, cache, security)?

# Solution:

class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    def hash1(self, item):
        return hash(item) % self.size

    def hash2(self, item):
        return (hash(item) * 7) % self.size

    def add(self, item):
        self.bit_array[self.hash1(item)] = 1
        self.bit_array[self.hash2(item)] = 1

    def check(self, item):
        if self.bit_array[self.hash1(item)] == 1 and self.bit_array[self.hash2(item)] == 1:
            return "Possibly Present"
        return "Definitely Not Present"

bf = BloomFilter(10)
bf.add("apple")
print(bf.check("apple"))
print(bf.check("banana"))