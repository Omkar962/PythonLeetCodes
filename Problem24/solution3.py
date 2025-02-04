# Iterative BFS	O(N)	O(N) (all nodes in queue at deepest level)


from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS approach using a queue.
        """
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # (node, depth)
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return max_depth
