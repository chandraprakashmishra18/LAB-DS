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

stack = []

def check_parentheses(exp):
    for ch in exp:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return "Unbalanced"
            stack.pop()

    if not stack:
        return "Balanced"
    else:
        return "Unbalanced"

expr = "(a+b)*(c+d)"
print(check_parentheses(expr))