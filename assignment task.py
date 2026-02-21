# 1-) Recursive approach on Factorial 
def fact(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1 :
        return 1
    else :
        return n * fact(n-1)
    
print(fact(4))
# TIME COMPLEXITY : 
    # Each time recursive call reduces by 1 so ,
    # TOTAL NO OF CALLS = n
    # T(n) = T(n-1) + O(1)
# Time Complexity:
    # O(n)
    
# Space Complexity :
    # Each recursive call is stored in the call stack for n times.
    # Stack depth = n
    # O(n)