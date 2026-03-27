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
# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        # If list was empty
        if self.tail is None:
            self.tail = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # Delete by value
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Case 1: delete head
        if self.head.data == value:
            self.head = self.head.next

            if self.head is None:  # list became empty
                self.tail = None
            return

        # Case 2: delete middle/tail
        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next

                # If tail deleted
                if curr == self.tail:
                    self.tail = prev
                return

            prev = curr
            curr = curr.next

        print("Value not found")

    # Traverse
    def traverse(self):
        temp = self.head
        result = []

        while temp:
            result.append(temp.data)
            temp = temp.next

        print(result)
        
s = SLL()

s.insert_begin(10)
s.traverse()       # [10]

s.insert_end(20)
s.traverse()       # [10, 20]

s.insert_begin(5)
s.traverse()       # [5, 10, 20]

s.delete(10)
s.traverse()       # [5, 20]

s.delete(5)
s.traverse()       # [20]

s.delete(100)      # Value not found