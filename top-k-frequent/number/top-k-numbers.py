class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        result = []
        for n in nums:
            if n in num_count:
                num_count[n] +=1
            else: # not in dict
                num_count[n] = 1
                
        sorted_dict = dict(sorted(num_count.items(), key=lambda item : -item[1]))
        
        for key in sorted_dict:
            result.append(key)
            if len(result) == k:
                #return the list, leave the function
                return result