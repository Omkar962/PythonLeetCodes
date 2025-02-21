# BFS:
# Time Complexity: O(N) (each node is visited once)
# Space Complexity: O(N) (in the worst case, all nodes are in the queue)
# BFS is generally better for finding the minimum depth since it terminates early. 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])  
        
        while queue:
            node, depth = queue.popleft()
     
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0