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
        revprev = None

        while secondhalf:
            temp = secondhalf.next
            secondhalf.next = revprev
            revprev = secondhalf
            secondhalf = temp
        
        while head and revprev:
            temp = head.next
            revtemp = revprev.next

            head.next = revprev
            revprev.next = temp

            head = temp
            revprev = revtemp

        return None