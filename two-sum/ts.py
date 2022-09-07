class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
        # Brute force: O(n^2) iterate through all numbers in the list until we find that one exact solution
        for i in nums:
            for j in nums:
                print(f'{i} + {j} = {target}')
                if i + j == target:
                    print('yes')
                    return []
                    
                
                    
            
sol = Solution()
nums = [1,2,3,4,5]
target = 8
sol.twoSum(nums, target)
        
        
        
        # Better solution:
        # grab value at index i, search for target - i in list      