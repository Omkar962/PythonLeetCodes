# Time Complexity  O(n): We visit each node once, where n is the number of nodes in the trees.

# Space Complexity O(h): The space complexity is determined by the maximum height of the recursion stack, where h is the height of the tree. In the worst case (skewed tree), this can be O(n).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        
        # If one of the nodes is None, or the values are different, trees are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
