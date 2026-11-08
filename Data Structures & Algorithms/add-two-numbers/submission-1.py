# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        answerhead = answer = ListNode()

        while l1 or l2 or carry:
            l1val = 0
            l2val = 0

            if l1:
                l1val = l1.val
                l1 = l1.next
            
            if l2:
                l2val = l2.val
                l2 = l2.next
            
            value = l1val + l2val + carry

            carry = 0
            
            if value >= 10:
                carry = 1
                value -= 10
            
            answer.next = ListNode(value)
            answer = answer.next
        
        return answerhead.next