# Aim :
#     Implement queue with head+tail pointers and connect to BFS usage.
# What you will implement (in lab) :
#     Implement Queue with enqueue, dequeue, front. Ensure O(1) enqueue via tail pointer.
# Input / Output expectation :
#     Input: operation sequence. Output: removed values + current front + final state.
# Lab checkpoints (faculty verifies) :
#     • Tail pointer used
#     • Underflow safe handling
# Viva (answer any 3) :
#     1. BFS uses queue ?
#     2. FIFO meaning?
#     3. Scheduling example?

# Solution :

# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue using Linked List
class Queue:
    def __init__(self):
        self.front = None   # head
        self.rear = None    # tail

    # Enqueue (O(1))
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    # Dequeue (O(1))
    def dequeue(self):
        if self.front is None:
            return None   # Underflow

        temp = self.front
        self.front = self.front.next

        if self.front is None:   # queue becomes empty
            self.rear = None

        return temp.data

    # Get front element
    def get_front(self):
        if self.front:
            return self.front.data
        return None

    # Display queue
    def display(self):
        temp = self.front
        res = []
        while temp:
            res.append(temp.data)
            temp = temp.next
        print(res)
        
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Dequeued:", q.dequeue())   
print("Front:", q.get_front())    

q.enqueue(40)

print("Dequeued:", q.dequeue())  
print("Front:", q.get_front())   

q.display()   