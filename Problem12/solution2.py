# Built-in bin(int(a, 2) + int(b, 2)) -	O(N + M) ,	O(1)
# Very simple Not allowed in some interviews

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        c=bin(a+b)
        return c[2:]