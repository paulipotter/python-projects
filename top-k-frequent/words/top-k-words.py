class Solution:
    def topKFrequent(self, words, k: int):
        
        # Create an empty hash table
        freq = {}
        ''' Part 1 - put the keys in a hash table '''
        '''
            Option 1
        '''
        # it word is already in the list, word ++ else add the word to the list with a counter of 1
        for w in words:
            if w in freq:
                freq[w] += 1 
            else: 
                freq[w] = 1
            
        ''' Part 2 - Sort the dict by key in ascending order
        - Lambda can take any number of arguments, but can only have one expression.
        - lambda arguments : expression
        - example: add_ten = (lambda a : a + 10)
        '''
       
        # -x[1] - sort the values in decreasing order
        # x[0] if two values have the same freq, sort in ascending order
        sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        print(sorted_freq)

            
        return [w[0] for w in sorted_freq][:k]
            
        
    
words = ['anna', 'jesus', 'anna','anna', 'jesus', 'anna']
k = 2
sol = Solution()
print(sol.topKFrequent(words, k))