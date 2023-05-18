# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: 
            return root
        
        # If the value of the current node is lower than the threshold
        if root.val < low:
            # the trimmed binary tree will be to the right
            return self.trimBST(root.right, low, high)
        # Else if the value is higher than the threshold
        elif root.val > high:
            # the trimmed binary tree will be to the left
            return self.trimBST(root.left, low, high)
        
        # Call the function to traverse the left subtree, then the right
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root
    
    # Time complexity O(n) where n is the number of nodes
    # Space complexity O(n) call stack could be as large as the number of nodes