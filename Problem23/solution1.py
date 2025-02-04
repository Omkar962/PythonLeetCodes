# Time Complexity:  O(N) (each element is processed once)
# Space Complexity: O(N) (for recursive stack in worst case, O(logN) for balanced case)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])

        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root