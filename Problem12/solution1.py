# Bitwise Addition (Manual) -	O(max(N, M))  ,	O(max(N, M))	
# Works in all languages, optimized	Requires implementation effort

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            sum_ = carry
            if i >= 0:
                sum_ += int(a[i])
                i -= 1
            if j >= 0:
                sum_ += int(b[j])
                j -= 1

            result.append(str(sum_ % 2))  
            carry = sum_ // 2 

        return ''.join(result[::-1]) 