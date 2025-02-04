# Iterative DFS	O(N)	O(H) (stack stores at most H elements)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Iterative DFS using a stack.
        """
        if not root:
            return False
        
        stack = [(root, root.val)]  # (current node, sum so far)
        
        while stack:
            node, current_sum = stack.pop()
            
            # Check if it's a leaf node with the correct sum
            if not node.left and not node.right and current_sum == targetSum:
                return True
            
            # Push children to stack with updated sum
            if node.right:
                stack.append((node.right, current_sum + node.right.val))
            if node.left:
                stack.append((node.left, current_sum + node.left.val))
        
        return False  # No valid path found
