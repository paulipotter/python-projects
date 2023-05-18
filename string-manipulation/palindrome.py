import re
def isPalindrome( s: str) -> bool:
    # Assumption: no str s will ever be empty

    ''' 
    Part 1 - clean up string
    - Remove any non alpha numeric character and replace with ''
    - make sure all characters are lowercase
    - we can use the same variable or a new variable. Same variable saves space
    '''
    '''
        OPTION 1
        - Use list comprehension and .isalphanum() to only keep alphanumeric characters
        - Python treats strings like a list of characters by default (iterable)
        - Iterate through the characters and use str built-in join to make a string 
        with only alphanum characters
    '''
    # s = ''.join(character for character in s if character.isalnum()).lower()
    
    
    '''
        OPTION 2
        - import re and use re.sub to replace non-relevant characters with ''
        ^ -> not
        0-9a-zA-Z -> any of these characters
        + -> match 1 or more pls   
    '''
    s = (re.sub('[^0-9a-zA-Z]+','',s)).lower()
    


    '''
    Part 2 - check if str is a palindrome
    '''
    # create a list of characters
    # iterate through the char and only add to the list if the char is alphanumeric
    # new_str = [character.lower() for character in s if character.isalnum()]
    # return new_str == new_str[::-1]
    # list[::-1] its a built in utility from python and its time complexity is O(n)
    
    '''
    OPTION 1
        - Use list[::-1] it's a built in utility that reverses the 
            - Time complexity O(n)
        
    '''
    # return s == s[::-1]

    '''
    OPTION 2
    - use a while loop to run through <s> and symmetrically compare the first and last characters
    - Will break as soon as it finds any sort of inconsistency
    - Leaving the while loop means we didn't find any inconsistency, hence palindrome
    '''
    first = 0
    last = len(s) - 1
    while first < last:
        if s[first] == s[last]:
            first += 1
            last -= 1
        else: return False
    return True
    


s = "Was it a .car or a cat I saw"
print(isPalindrome(s))