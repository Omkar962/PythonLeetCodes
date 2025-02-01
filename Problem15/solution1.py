# Iterative DP (O(1) Space)	O(N)	O(1)
# Fast and efficient

class Solution:
    def climbStairs(n: int) -> int:
        if n <= 2:
            return n  # Base cases: 1 step → 1 way, 2 steps → 2 ways
        
        prev1, prev2 = 2, 1  # Base cases for n=2 and n=1
        for _ in range(3, n + 1):
            curr = prev1 + prev2  # Fibonacci relation
            prev2, prev1 = prev1, curr  # Update values
        
        return prev1
