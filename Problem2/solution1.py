#String Conversion (str(x)) :- 	O(n) ,	O(n)	
# Simple but uses extra memory


def isPalindrome(self, x: int) -> bool:
    n=str(x)
    return n==n[::-1]