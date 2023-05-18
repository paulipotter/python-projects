# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # will be forwarding over at each step
        carry = 0
        
        # variable for final result
        final_result = ListNode(0)
        
        # var to use in order to move towards the next node at each iteration
        pointer = final_result
        # note any update in pointer will reflect on final_result
        
        #iterate over the linked lists
        while l1 or l2 or carry:
            # get the digits from the individual nodes
            # use if statement to handle when val is None
            first_number = l1.val if l1.val else 0
            second_number = l2.val if l2.val else 0
            
            # add both numbers and any potential carry
            summation = first_number + second_number + carry
            
            # get the digit of the solution
            number = summation % 10
            
            # get the carry with floor division
            carry = summation // 10
            
            # store the result to the pointer
            pointer.next = ListNode(number)
            
            # move the pointer to the next node
            pointer = pointer.next
            
            # move the nodes of the list to the next if not none
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
    
# Time Complexity: O(max(l1.len, l2.len))
        