# Integer Conversion -	O(N) ,	O(N)	
# Short and easy to read	Uses extra memory, may fail for very large numbers

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(map(str, digits))  # Efficient string construction
        n = str(int(s) + 1)  # Convert to int, add 1, and convert back
        return [int(d) for d in n]  # Convert back to list of digits