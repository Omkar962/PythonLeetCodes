# Recursive DFS	O(N)	O(H) (O(log N) for balanced, O(N) for skewed)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Returns the maximum depth of a binary tree.
        """
        if not root:
            return 0  # Base case: empty tree
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1  # Add 1 for the current node
