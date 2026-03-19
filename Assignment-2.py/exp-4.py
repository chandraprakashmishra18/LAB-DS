# Aim :
#     Implement dynamic insertion and deletion without shifting.
# What you will implement (in lab) :
#     Implement SLL with insert at beginning, insert at end, delete by value, traverse. Handle
#     missing values safely.
# Input / Output expectation :
#     Input: operation sequence. Output: list after each operation.
# Lab checkpoints (faculty verifies) :
#     • Correct head/tail management
#     • delete works for head/middle/tail cases
# Viva (answer any 3) :
#     1. Why search is O(n)?
#     2. Why insert-at-head is O(1)?
#     3. Node structure?

# Solution :

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singelylinkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next

s = Singelylinkedlist()
s.insert(10)
s.insert(20)
s.insert(30)

s.display()