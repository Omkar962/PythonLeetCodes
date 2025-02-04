# Time Complexity: O(N) → Each node is visited once.
# Space Complexity: O(H) → Due to recursion, where  H is the height of the tree. In a balanced tree, H=O(logN), in the worst case (skewed tree), H=O(N).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0
            lheight=checkHeight(node.left)
            rheight=checkHeight(node.right)

            if lheight==-1 or rheight==-1 or abs(lheight-rheight)>1:
                return -1
            return max(lheight,rheight)+1
        return checkHeight(root)!=-1
        