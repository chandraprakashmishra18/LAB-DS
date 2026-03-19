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

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new=Node(data)
        if self.head!=None:
            self.head.prev=new
            new.next=self.head
        self.head=new

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" <-> ")
            temp=temp.next

d=DLL()
d.insert(10)
d.insert(20)
d.insert(30)

d.display()