
# Horizontal Scanning (Best Method) -	O(n * m) , O(1)
# Best trade-off for efficiency & readability

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  
        
        for word in strs[1:]:  
            while not word.startswith(prefix):  
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
