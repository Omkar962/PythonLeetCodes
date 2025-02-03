# Time Complexity: O(n): Each node is visited once.
# Space Complexity: O(1): No extra space is used (in-place traversal).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    current = root
    
    while current:
        if not current.left:
            result.append(current.val)  # Visit node if no left child
            current = current.right     # Move to right child
        else:
            # Find inorder predecessor (rightmost node in left subtree)
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                predecessor.right = current  # Make current as right child of predecessor
                current = current.left      # Move to left child
            else:
                predecessor.right = None    # Restore the tree structure
                result.append(current.val)  # Visit node
                current = current.right     # Move to right child
    
    return result
