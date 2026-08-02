# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondhalf = slow.next
        slow.next = None
        secprev = None

        while secondhalf:
            temp = secondhalf.next
            secondhalf.next = secprev
            secprev = secondhalf
            secondhalf = temp
        
        while head and secprev:
            headtemp = head.next
            sectemp = secprev.next

            head.next = secprev
            secprev.next = headtemp

            head = headtemp
            secprev = sectemp
            
        
        return None
        