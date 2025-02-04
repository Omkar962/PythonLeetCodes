# Iterative DFS	O(N)	O(H) (same as recursive)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Iterative DFS approach using a stack.
        """
        if not root:
            return 0
        
        stack = [(root, 1)]  # (node, depth)
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        
        return max_depth
