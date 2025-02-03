# Time Complexity  O(m + n): Each element is processed once.
# Space Complexity O(1): The merge is done in-place without extra space.


# Solved with three pointers and in-place modification:

# Start merging from the end of nums1 to avoid overwriting elements.

# Use three pointers:

# p1 pointing to the last valid element in nums1 (index m-1).
# p2 pointing to the last element in nums2 (index n-1).
# p pointing to the last position in nums1 (index m+n-1).
# Compare nums1[p1] and nums2[p2]:

# Place the larger value at nums1[p].
# Move the corresponding pointer.
# Repeat until one array is exhausted.
# If elements remain in nums2, copy them to nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 has remaining elements, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
