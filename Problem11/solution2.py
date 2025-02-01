# Newton’s Method -	O(log x) (fastest) , O(1)	
# Very fast convergence	

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = x
        while ans * ans > x:
            ans = (ans + x // ans) // 2
        return ans