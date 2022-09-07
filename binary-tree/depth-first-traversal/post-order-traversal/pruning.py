# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # get rid of 0s that have no children (null values)
        # post order traveersal: left, right, root
        
        # if root if equal to none/not root
        if not root: return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # if the current root equals zero and it has no children
        if root.val == 0 and not root.right and not root.left:
            # we can go ahead and prune! its value
            return None
        else: # root value is not 0 OR it is 0 but has a non-zero child
            return root
        
        