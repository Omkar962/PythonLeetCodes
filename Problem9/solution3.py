# KMP Algorithm	- O(n + m) , O(m)	
# Best for large inputs (e.g., DNA sequences, large texts)

def strStr(haystack: str, needle: str) -> int:
    def computeLPS(pattern):
        lps = [0] * len(pattern)
        j = 0 
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n, m = len(haystack), len(needle)
    if m == 0:
        return 0

    lps = computeLPS(needle)
    i = j = 0  

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                return i - j  
        else:
            if j != 0:
                j = lps[j - 1] 
            else:
                i += 1

    return -1
