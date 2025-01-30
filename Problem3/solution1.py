# Stack-based approach -	O(n)  ,	O(n)	
# Each character is processed once

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  

        for char in s:
            if char in mapping:  
                if stack:
                    top_element=stack.pop()
                else:
                    top_element = '#'

                if top_element != mapping[char]:  
                    return False  
            else:
                stack.append(char)   
        return not stack  




