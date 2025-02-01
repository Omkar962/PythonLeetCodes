# Right-to-Left Traversal (Optimal)	O(N)	O(1)	
# Efficient, no extra space needed	Requires manual carry handling

class Solution:
    def plusOne(digits: list[int]) -> list[int]:
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, return immediately
            digits[i] = 0  # Set current digit to 0 and continue
        
        # If all digits were 9, we need an extra leading 1
        return [1] + digits

