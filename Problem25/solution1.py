# Recursive DFS	O(N)	O(H) (O(log N) for balanced, O(N) for skewed)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Recursive DFS to check if there exists a root-to-leaf path with sum equal to targetSum.
        """
        if not root:
            return False  # Empty tree
        
        # If it's a leaf node, check if remaining sum equals node value
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recur for left & right subtrees with updated sum
        return (self.hasPathSum(root.left, targetSum - root.val) or 
                self.hasPathSum(root.right, targetSum - root.val))
