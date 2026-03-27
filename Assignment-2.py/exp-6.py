# Aim :
#     Build stack using linked list and apply to bracket validation.
# What you will implement (in lab) :
#     Implement Stack (push/pop/peek) using SLL head as top. Use it to validate (), , [] in
#     strings.
# Input / Output expectation :
#     Input: strings. Output: True/False for each test string.
# Lab checkpoints (faculty verifies) :
#     • Correct matching logic
#     • Handles empty string and mismatch cases
# Viva (answer any 3) :
#     1. Why stack is ideal here?
#     2. What fails in ”([)]”?
#     3. Underflow meaning?

# Solution :

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


# Function to validate brackets
def is_valid(expr):
    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in expr:
        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":
            if stack.is_empty():
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return stack.is_empty()


# Driver code
n = int(input("Enter number of test cases: "))

for _ in range(n):
    s = input("Enter string: ")
    print(is_valid(s))