# Linear Scan -	O(n)	O(1)	
# Scans every element until it finds target

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        else:
            return len(nums)