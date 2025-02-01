# Binary Search	- O(log x) , O(1)	
# Efficient, structured approach	
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        
        l=0
        r=x//2

        while l<=r:
            m=(l+r)//2

            if m*m==x:
                return m
            elif m*m <x:
                l=m+1
                ans=m
            else:
                r=m-1
        return ans