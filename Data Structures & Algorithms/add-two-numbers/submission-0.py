# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = dummy = ListNode(0)
        carry = 0

        while l1 or l2 or carry:

            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            value = l1val + l2val + carry

            carry = 0

            if value >= 10:
                value -= 10
                carry = 1
            
            answer.next = ListNode(value)
            answer = answer.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
            
            
        
