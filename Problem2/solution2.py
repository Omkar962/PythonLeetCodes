#Optimized (Half Reverse) -	O(log n) ,	O(1)	
# Slightly faster, fewer calculations

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        
        rev=0
        while x > rev:
            d=x % 10
            rev = rev * 10 + x % 10
            x //= 10
        return rev == x or x == rev // 10
