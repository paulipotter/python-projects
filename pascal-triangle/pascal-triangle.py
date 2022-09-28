'''
Time complexity: O(n^2)
Space complexity: O(n^2)
where n = numRows
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pyramid = []
        
        if numRows < 1:
            return pyramid
 
        for i in range(0, numRows):    
            # Clear the row every time
            row = []
            # if at the beginning, append 1
            if i == 0:
                row.append(1)
            else: # index equals 1 or greater
                # insert a 1 at the very beginning
                row.insert(0, 1)
                # insert a 1 right at the end
                row.insert(i, 1)
                
                # iterate the middle spots from index 1 to i-1
                for j in range(1, i):
                    # get the number top left
                    top_left = pyramid[i - 1][j  - 1]
                    
                    # get the number top right
                    top_right = pyramid[i - 1][j]
                    
                    # insert at index j the sum of top left and right
                    row.insert(j, top_left + top_right)
                
            pyramid.append(row)
                    
        return pyramid
