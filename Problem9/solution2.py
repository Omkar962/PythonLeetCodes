# Sliding Window (Brute Force)	- O(n * m) ,	O(1)	
# Simple but slow for large inputs

def strStr(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):  
        if haystack[i:i+m] == needle:  
            return i  

    return -1  