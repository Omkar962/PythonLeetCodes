# Optimized (Hash Map) -	O(n) , O(n)
# Faster & more scalable

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        w = {}
        
        for i in range(len(nums)):
            d=target-nums[i]
            
            if d in w:
                return [w[d],i]
            
            w[nums[i]]=i

        return []
		
      