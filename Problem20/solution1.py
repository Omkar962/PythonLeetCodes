
# The isMirror function checks if two trees are mirror images by recursively comparing their root values and their left and right subtrees.
# The isSymmetric function calls isMirror with the left and right subtrees of the root.
# Time Complexity  O(n): Each node is visited once where n is the number of nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # Helper function to check if two trees are mirrors of each other
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        return isMirror(root.left, root.right)
