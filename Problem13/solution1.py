# Right-to-Left Traversal -	 O(N) ,	O(1)	
# Efficient, minimal memory usage Slightly more code

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                c+=1
            if c>0 and s[i]==" ":
                break
        return c


