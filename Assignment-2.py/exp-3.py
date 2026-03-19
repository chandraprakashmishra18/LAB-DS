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
        self.data = []

    def append(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            print("Underflow")
        else:
            return self.data.pop()

    def display(self):
        print(self.data)

arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)

arr.display()

arr.pop()
arr.display()

# Complexity

# Append → Amortized O(1)
# Pop → O(1)