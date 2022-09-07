# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # key: vertical axis, value: list
        lookup = defaultdict(list) 
        #dfs
        def dfs(node, x, y):
            if not node: return
            
            # make it a heap to take care of node locations
            # make sure vertical order is maintained
            heappush(lookup[x],(-y,node.val))
            
            #traverse to the left
            dfs(node.left, x-1, y-1)
            
            #traverse to the right
            dfs(node.right, x+1, y-1)
        dfs(root, 0, 0)
        
        output =[]
        for key, value in sorted(lookup.items()):
            temp = []
            # while we have our heap
            while value:
                # pop off whatever is in the heap
                # will contain the y and node values
                item = heappop(value)
                
                # add the second item (node value) to the temp list
                # we can ignore the y-value
                temp.append(item[1])
                
            output.append(temp)
            
        return output
