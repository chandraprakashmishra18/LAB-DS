# Aim :
#   Learn bidirectional links and correct pointer updates.
# What you will implement (in lab) :
#   Implement DLL with insert after node(target,x) and delete at position(pos). Maintain
#   prev/next correctly.
# Input / Output expectation. :
#    Input: target/position. Output: list after each operation.
# Lab checkpoints (faculty verifies) :
#   • prev pointers correct
#    • delete updates head/tail safely
# Viva (answer any 3) :
#   1. DLL advantage over SLL?
#   2. Browser history mapping?
#   3. Deletion ease in DLL?

# Solution :
# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert after a target value
    def insert_after(self, target, x):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            if temp.data == target:
                new_node = Node(x)

                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:  # middle case
                    temp.next.prev = new_node
                else:  # tail case
                    self.tail = new_node

                temp.next = new_node
                return

            temp = temp.next

        print("Target not found")

    # Delete at position (1-based index)
    def delete_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return

        # Case 1: delete head
        if pos == 1:
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:  # list became empty
                self.tail = None
            return

        temp = self.head
        count = 1

        # Traverse to position
        while temp and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        # Case 2: delete middle or tail
        if temp.next:
            temp.next.prev = temp.prev
        else:  # tail case
            self.tail = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    # Traverse forward
    def traverse(self):
        temp = self.head
        res = []
        while temp:
            res.append(temp.data)
            temp = temp.next
        print(res)
        
dll = DLL()

# manually create initial list
dll.head = Node(10)
dll.tail = dll.head

dll.insert_after(10, 20)
dll.traverse()      # [10, 20]

dll.insert_after(10, 15)
dll.traverse()      # [10, 15, 20]

dll.delete_pos(2)
dll.traverse()      # [10, 20]

dll.delete_pos(1)
dll.traverse()      # [20]

dll.delete_pos(5)   # Position out of range