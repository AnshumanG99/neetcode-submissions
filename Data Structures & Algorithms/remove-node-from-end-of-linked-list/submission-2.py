# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        right = head
        prev = ListNode(0, head)
        answer = prev

        while n > 0: 
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            prev = prev.next
        
        prev.next = prev.next.next

        return answer.next
        
        