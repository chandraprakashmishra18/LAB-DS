# Aim :
#   Understand how dynamic arrays grow and why append is amortized O(1).
# What you will implement (in lab) :
#   Implement capacity/size based DynamicArray with append (doubling resize) and pop
#   from end. Print (size, capacity) after each append.
# Input / Output expectation :
#   Input: sequence of appends and pops. Output: state print showing resize event(s).
# Lab checkpoints (faculty verifies) :
#   • Resize happens and state shown
#   • Student writes short amortized explanation
# Viva (answer any 3) :
#   1. What is amortized complexity?
#   2. Why doubling helps?
#    3. Why pop-end is O(1)?

#   Solution :
class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = [0] * self.capacity

    def append(self, x):
        # Resize if full
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [0] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            print("Resized to", self.capacity)

        self.arr[self.size] = x
        self.size += 1
        print("Added:", x, "| Size:", self.size, "| Capacity:", self.capacity)

    def pop(self):
        if self.size == 0:
            print("Underflow")
            return
        self.size -= 1
        print("Removed | Size:", self.size, "| Capacity:", self.capacity)


# -------- DRIVER CODE --------
d = DynamicArray()

d.append(60)
d.append(45)
d.append(80)
d.append(20)

d.pop()

#           Observation
# ---------------------------------------
# Capacity doubles when array becomes full
# Resize happens rarely
# Most appends take constant time
# ----------------------------------------------------------
# ----------------------------------------------------------

#           Conclusion
# ------------------------------------
# Dynamic arrays use resizing strategy (doubling) to maintain efficient performance.
# Append is amortized O(1), while pop from end is O(1).
# ------------------------------------------------------------
# ------------------------------------------------------------