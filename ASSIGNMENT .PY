
# 1.)SOLUTION 1

def get_factorial(n):
    """Recursive Factorial: Time O(n)"""
    if n <= 1:
        return 1
    return n * get_factorial(n - 1)

def fib_naive(n):
    """Naive Fibonacci: Time O(2^n)"""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memoized(n, memo=None):
    """Memoized Fibonacci: Time O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]

def main():
    print("--- PART 1: RECURSION ---")
    
    # Taking user input instead of fixed numbers
    val = int(input("Enter a number to calculate Factorial and Fibonacci: "))

    # 1. Factorial
    print(f"\nFactorial of {val}: {get_factorial(val)}")
    
    # 2. Fibonacci Comparison
    print(f"\nComputing Fibonacci({val})...")
    print(f"Memoized Result (Fast): {fib_memoized(val)}")
    
    # Warning for Naive: If val is too high (e.g., > 35), it will freeze the computer
    if val > 30:
        print("Note: Skipping Naive version for high input to avoid system hang.")
    else:
        print(f"Naive Result (Slow):  {fib_naive(val)}")

if __name__ == "__main__":
    main()
# <=================CODE ENDS==========================>

# 3.) SOLUTION

def tower_of_hanoi(n, source, auxiliary, destination):
    # Recursive function to solve Tower of Hanoi.
    # n: Number of disks
    # source: The starting peg (A)
    # auxiliary: The middle peg (B)
    # destination: The target peg (C)
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    
    # Step 1: Move n-1 disks from Source to Auxiliary
    count1 = tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # Step 2: Move the nth (largest) disk to Destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move n-1 disks from Auxiliary to Destination
    count2 = tower_of_hanoi(n-1, auxiliary, source, destination)
    
    return count1 + 1 + count2

def main():
    print("--- PART 2: TOWER OF HANOI ---")
    
    n = int(input("Enter number of disks (N=3 for manual trace): "))
    
    print(f"\nMove Sequence for N={n}:")
    print("-" * 30)
    total_moves = tower_of_hanoi(n, 'A', 'B', 'C')
    print("-" * 30)
    print(f"Total moves required: {total_moves}")

if __name__ == "__main__":
    main()
# <===============CODE ENDS==========================>

# 4.)SOLUTION 4

# THEORY & COMPLEXITY ANALYSIS:
# -----------------------------
# 1. Recurrence Relation: T(n) = 2T(n-1) + 1
# 2. Time Complexity: O(2ⁿ) - Exponential
#    - Every additional disk doubles the number of moves required.
# 3. Space Complexity: O(n) - Linear
#    - Based on the maximum depth of the recursion stack.

# MANUAL TRACE FOR N = 3 (A=Source, B=Aux, C=Dest):
# -------------------------------------------------
# Step 1: Move Disk 1 from A to C
# Step 2: Move Disk 2 from A to B
# Step 3: Move Disk 1 from C to B
# Step 4: Move Disk 3 from A to C  <-- Midpoint (Largest Disk)
# Step 5: Move Disk 1 from B to A
# Step 6: Move Disk 2 from B to C
# Step 7: Move Disk 1 from A to C




def solve_hanoi(n, src, aux, dest, move_count=[0]):
    # Solves Hanoi and tracks steps.
    # Using a list for move_count to keep it mutable across recursive calls.
    
    if n == 1:
        move_count[0] += 1
        print(f"Step {move_count[0]}: Move Disk 1 from {src} to {dest}")
        return

    # Move n-1 disks from Source to Aux
    solve_hanoi(n - 1, src, dest, aux, move_count)

    # Move the actual nth disk
    move_count[0] += 1
    print(f"Step {move_count[0]}: Move Disk {n} from {src} to {dest}")

    # Move n-1 disks from Aux to Dest
    solve_hanoi(n - 1, aux, src, dest, move_count)

def main():
    print("=== TOWER OF HANOI RECURSIVE SOLVER ===")
    try:
        n = int(input("Enter number of disks: "))
        if n < 1:
            print("Please enter a positive integer.")
            return

        print(f"\nSolution for {n} disks:")
        print("-" * 35)
        
        counter = [0]
        solve_hanoi(n, 'Peg A', 'Peg B', 'Peg C', counter)
        
        print("-" * 35)
        print(f"Total Moves (2^{n} - 1) = {counter[0]}")
        
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
# <=============CODE ENDS===================>