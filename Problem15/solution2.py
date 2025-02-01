# Memoization (Top-Down DP)	O(N)	O(N)	
# Optimized recursion	Extra space

class Solution:
    def climbStairs(n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        if n <= 2:
            return n
        memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
        return memo[n]