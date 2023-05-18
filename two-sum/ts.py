class Solution:
    def twoSum(self, nums, target: int):#-> List[int]:
        '''
        Option 1
        - Brute force: iterate through all numbers in the list until we find that one exact solution
        - Time complexity: O(n^2) 
        ''' 
        # for i in nums:
        #     for j in nums:
        #         print(f'{i} + {j} = {target}')
        #         if i + j == target:
        #             print('yes')
        #             return []   
                
        '''
        Option 2a
        '''
        # Use dict comprehension to add numbers onto a hash table
        # Use the built-in enumerate to add indices to the dict
        hash_table = {num: indx for indx, num in enumerate(nums)}
        
        # print(hash_table.keys())
        # Iterate through the numbers
        for number in hash_table:
            indx = hash_table[number]
            
            # Get the complement of k
            complement = target - number 
            # print(f'target: {target},\ti: {indx},\tn: {number},\tcomplement: {complement}')
            
            # Check if the complement exists in the hash_table
            if complement in hash_table.keys(): 
                # Return k and its complement
                return [indx, hash_table[complement]] #two sum found
        return [-1,-1]
        
        '''
        Option 2b
        '''
        # Create an empty hash table
        # hash_table = {}
        
        # Iterate through num list and create indices with the built in enumerate()
        # for indx, number in enumerate(nums):
        #     # Get the complement of k
        #     complement = target - number
            
        #     # Check if the complement exists in the hash_table
        #     if complement in hash_table.keys():
        #         return [indx, hash_table[complement]] #two sum found
        #     else:
        #         hash_table[number] = indx
        #     # Otherwise it adds the number and index to the hash table
        # return [-1,-1]
                    
            
sol = Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums, target))