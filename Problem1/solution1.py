# Brute force approach :- O(n²) ,O(1) 
# Slow for large inputs

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  

     
                      
        