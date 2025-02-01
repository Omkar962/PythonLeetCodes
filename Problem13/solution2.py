# Python Built-in (split())	- O(N)	, O(N)	
# Short and readable	Uses extra space

class Solution:
    def lengthOfLastWord(s: str) -> int:
        return len(s.strip().split()[-1])